from PyQt4 import QtGui
from PyQt4.QtGui import QTextCursor
import sys
from functools import partial
from .design import Ui_Dialog
from phonenumbers import parse, is_valid_number
from phonenumbers.phonenumberutil import NumberParseException
from .fetch_details import get_timezone, get_carrier, formatNum, get_country,parse_file_for_nums
from .utils import get_default_code
from pytz import timezone
from datetime import datetime
from pkg_resources import resource_filename


class DialerApp(QtGui.QDialog, Ui_Dialog):
    def __init__(self, num):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.objectMapSetup()
        self.loc_setting = None
        # self.ignore = False
        if num is not None:
            self.setDialerNumber(num)
            self.ignore = False

        # self.ignore = False
        num_list = list(map(str, range(0, 10))) + ['*', '#']

        for val, bt in zip(num_list, self.btn_list):
            bt.clicked.connect(partial(self.click_action, val))

        self.object_map["FileButton"].clicked.connect(self.file_nums)
        self.object_map["DelButton"].clicked.connect(self.del_action)
        self.object_map['NumTextBox'].textChanged.connect(self.num_changed)
        self.object_map['NumTextBox'].moveCursor(QTextCursor.EndOfLine)
        self.setDetails()
        self.ignore = False

    def num_changed(self):
        """Triggered when number in TextBox is changed"""
        if not self.ignore:
            # Critical section
            self.setDetails()
            """
            num = self.getDialerNumber()
            self.setDialerNumber('-' + num)
            """
            self.ignore = False

    def choose_file(self):
        """Opens a dialog box to choose a file.
        Returns path of file"""
        filepath = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '/')
        return filepath

    def file_nums(self):
        """Prints list of all numbers in a file"""
        filepath = self.choose_file()
        country_code = get_default_code()
        country_code = 'IN' if country_code[0] is None else country_code[0]
        print (parse_file_for_nums(filepath,country_code))

    def objectMapSetup(self):
        """Creates object_map. Maps human-readable object name to object"""
        self.btn_list = [self.pushButton_12,  # 0
                         self.pushButton, self.pushButton_2, self.pushButton_3,  # 123
                         self.pushButton_6, self.pushButton_4, self.pushButton_5,  # 456
                         self.pushButton_7, self.pushButton_8, self.pushButton_9,  # 789
                         self.pushButton_11, self.pushButton_10]  # *#

        self.object_map = {"NumTextBox": self.plainTextEdit,
                           "NumButtons": self.btn_list,
                           "Location": self.label,
                           "Carrier": self.label_2,
                           "Timezone": self.label_3,
                           "DelButton": self.pushButton_13,
                           "Location": self.label,
                           "FlagBox": self.label_4,
                           "FileButton":self.pushButton_15,
                           }

    def getDialerNumber(self):
        """Get number in dialer from text box.
        Returns the number as a string"""
        return str(self.object_map["NumTextBox"].toPlainText()).strip()

    def setDialerNumber(self, x):
        """Set contents of NumTextBox to given number (x)"""
        self.ignore = True
        self.object_map["NumTextBox"].setPlainText(x)
        self.object_map['NumTextBox'].moveCursor(QTextCursor.EndOfLine)

    def click_action(self, x):
        """Inserts x (a number) to NumTextBox after cursor."""
        self.object_map["NumTextBox"].insertPlainText(x)

    def del_action(self):
        """Deletes the character preceeding the cursor in NumTextBox."""
        self.setDialerNumber(self.getDialerNumber()[:-1])
        self.ignore = False
        self.num_changed()

    def setCountry(self, pnum, valid):
        """Accepts a phone number sets country details.
        If number is invalid, sets country name to NA.
        If country couldn't be determined by prefix, and IP or
        DEBDIALER_COUNTRY variable was used, it mentions the same in brackets.
        Also, sets country flag using country code.

        Args :
            pnum : PhoneNumber object
            valid : bool variable. True when number is valid, else False.
        """
        default = {"name": "NA", 'code': "NULL"}
        country = get_country(pnum.country_code) if valid else default
        flag_sp = ' ' * 20
        if valid:
            locstring = flag_sp + country['name']
            if self.loc_setting:
                locstring += '('+self.loc_setting+')'
        else:
            locstring = flag_sp + "NA"
        self.object_map['Location'].setText('Country :' + locstring)
        self.setFlag(country['code'])

    def setFlag(self, code):
        """Uses a country code to generate flag path. Sets FlagBox to flag."""
        FLAG_PATH = 'resources/flags/' + code + '-32.png'
        FULL_FLAG_PATH = resource_filename(__name__,FLAG_PATH)
        pixmap = QtGui.QPixmap(FULL_FLAG_PATH)
        pixmap = pixmap.scaledToHeight(21)
        self.object_map["FlagBox"].setPixmap(pixmap)

    def setDetails(self):
        """Gets phone number and sets details based on the number.
        If number couldn't be parsed because of missing country code,
            fetch default code using get_default_code()
            set loc_setting to 'IP' if country was determined by IP address
            set loc_setting to 'ENV' if country was determined by env variable
        Set timezone, carrier and country values.
        Format number as International Number and set it.
        """
        number = self.getDialerNumber()
        try:
            x = parse(number)
            self.loc_setting = None
        except NumberParseException as e:
            if e.error_type == 0:
                ccode,ip = get_default_code()
                if ccode:
                    x = parse(number,ccode)
                    self.loc_setting = 'IP' if ip else 'ENV'
                else:
                    return
            else:
                print (e.args)
                return
        validity = is_valid_number(x)
        self.setTimezone(x, validity)
        self.setCarrier(x, validity)
        self.setCountry(x, validity)
        formatted = formatNum(x,'inter')
        self.setDialerNumber(formatted)

    def setCarrier(self, pnum, valid):
        """Get carrier details of number and set in textbox."""
        carr = get_carrier(pnum) if valid else 'NA'
        self.object_map["Carrier"].setText('Carrier : ' + carr)

    def setTimezone(self, pnum, valid):
        """If number is valid, display Timezone names and UTC offset.
        Else, set Timezone to NA."""
        if valid:
            tz = get_timezone(pnum)[0] if valid else ''
            utcdelta = timezone(tz).utcoffset(datetime.now())
            utcoff = str(float(utcdelta.seconds) / 3600)
            self.object_map["Timezone"].setText(
                'Timezone : ' + tz + " | UTC+" + utcoff)
        else:
            self.object_map["Timezone"].setText('Timezone : NA')


def main(num):
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    # We set the form to be our DialerApp (design)
    form = DialerApp(num)
    form.show()                         # Show the form
    app.exec_()                         # and execute the app