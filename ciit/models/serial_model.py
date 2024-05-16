import os
import re
from dotenv import find_dotenv, load_dotenv

from models.SQLClient import SQLClient
from models.query_master import QueryMaster


class SerialModel:

    def __init__(self, client, query_master):
        self.serials = []
        self.client = client
        self.query_master = query_master

    # Turning the input to uppercase and removing whitespace
    def clean_string(self, text) -> str:
        text = text.upper()
        return text.replace(" ", "")

    def get_serials(self):
        return self.serials

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

    def is_serial_in_db(self, serial) -> bool:
        """
        Checks if a given serial number exists in the database.

        Args:
            serial (str): The serial number to check.

        Returns:
            bool: True if the serial number exists in the database, False otherwise.
        """
        try:
            query = self.query_master.serial_exists_query()
            result = self.client.execute_query(query, params={"serial": serial})
            result = result['exists'][0]
            return result

        except Exception as e:
            print(
                f"ERROR: Something went wrong when searching the following serial: {serial}"
            )
            print(e)
            return False

    # Validating the raw input from the line edit
    def validate_serial(self, text) -> str:

        # Checking if the resulting text is not empty
        if text is None:
            return "The serial can not be empty!"

        # Checking if the text has any non-alphanumeric characters
        if bool(re.search(r'\W', text)) is True:
            return "The serial must contain only letters and numbers!"

        if text in self.serials:
            return "The serial is already entered, try another one!"

        # Checking if the text is between 5 and 30 alpha-numeric chars
        if len(text) not in range(5, 30):
            return (
                "The serial must have a length \n between 5 and 20 letters and numbers!"
            )

        if self.is_serial_in_db(text) == False:
            return "The serial doesn't exist in the database!"

        return None