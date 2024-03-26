import os
import re
from dotenv import find_dotenv, load_dotenv

from models.SQLClient import SQLClient
from models.query_master import QueryMaster


class SerialModel:

    def __init__(self):
        self.serials = []
        dotenv_path = find_dotenv()
        load_dotenv(dotenv_path)
        self.client = SQLClient(
            os.getenv("URL"),
            os.getenv("PORT"),
            os.getenv("DB"),
            os.getenv("USER"),
            os.getenv("PASSWORD"),
        )
        self.query_master = QueryMaster()
        self.client.connect()

    def __del__(self):
        """
        Disconnects from the SQL client when the object is destroyed.
        """
        self.client.disconnect()

    #
    # Turning the input to uppercase and removing whitespace
    def clean_string(self, text):
        text = text.upper()
        return text.replace(" ", "")

    def add_serial(self, serial):
        """
        Adds a serial number to the list of serials.

        Args:
            serial (str): The serial number to add.
        """
        self.serials.append(serial)

    def delete_serials(self, serials):
        """
        Deletes the given serial numbers from the list of serials.

        Args:
            serials (list): The serial numbers to delete.
        """
        for serial in serials:
            if serial.text() in self.serials:
                self.serials.remove(serial.text())

    def clear_serials(self):
        """
        Clears all serial numbers from the list of serials.
        """
        self.serials.clear()

    def is_serial_in_db(self, serial):
        """
        Checks if a given serial number exists in the database.

        Args:
            serial (str): The serial number to check.

        Returns:
            bool: True if the serial number exists in the database, False otherwise.
        """
        try:
            query = self.query_master.serial_exists(serial)

            number_of_serials = self.client.execute_query(query)
            num = number_of_serials.iloc[0, 0]
            if num > 0:
                return True
            self.client.disconnect()

        except Exception as e:
            print(
                f"ERROR: Something went wrong when searching the following serial: {serial}"
            )
            print(e)
            return False
        return False

    #
    # Validating the raw input from the line edit
    def validate_serial(self, text) -> str:

        # Checking if the resulting text is not empty
        if text is None:
            return "The serial can not be empty!"

        # Checking if the text has any non-alphanumeric characters
        if bool(re.search("\W", text)) is True:
            return "The serial must contain only letters and numbers!"

        if text in self.serials:
            return "The serial is already entered, try another one!"
        # # Checking if the item is not already in the list and appending it
        # if self.lw_serials.findItems(text, QtCore.Qt.MatchFlag.MatchFixedString):
        #     self.handle_error_message(
        #         True, custom_message=
        #     )
        #     return False

        # Checking if the text is between 5 and 30 alpha-numeric chars
        if len(text) not in range(5, 30):
            return (
                "The serial must have a length \n between 5 and 20 letters and numbers!"
            )

        if self.is_serial_in_db(text) is False:
            return "The serial doesn't exist in the database!"

        return None