import os
import re
from dotenv import find_dotenv, load_dotenv
import pandas as pd

from models.SQLClient import SQLClient
from models.query_master import QueryMaster


class SerialModel:
    def __init__(self, client, query_master):
        """
        Initialize the SerialModel with a SQL client and query master.

        Args:
            client (SQLClient): Instance of SQLClient for database interaction.
            query_master (QueryMaster): Instance of QueryMaster for SQL queries.
        """
        self.serials = []  # Initialize an empty list to store serial numbers
        self.client = client  # Store the SQL client instance
        self.query_master = query_master  # Store the QueryMaster instance
        self.serials_limit = 50  # Set a default limit for serials

    def clean_string(self, text) -> str:
        """
        Clean and normalize the input string.

        Args:
            text (str): The input string to clean.

        Returns:
            str: The cleaned and normalized string (uppercase, no whitespace).
        """
        text = text.upper()  # Convert text to uppercase
        return text.replace(" ", "")  # Remove whitespace from text

    def get_serials(self):
        """
        Get the list of stored serial numbers.

        Returns:
            list: The list of serial numbers.
        """
        return self.serials

    def add_serial(self, serial):
        """
        Add a serial number to the list of serials.

        Args:
            serial (str): The serial number to add.
        """
        self.serials.append(serial)

    def delete_serials(self, serials):
        """
        Delete the given serial numbers from the list of serials.

        Args:
            serials (list): The list of serial numbers to delete.
        """
        for serial in serials:
            if serial in self.serials:
                self.serials.remove(serial)

    def clear_serials(self):
        """
        Clear all serial numbers from the list of serials.
        """
        self.serials.clear()

    def read_serials_from_excel(self, file_path):
        """
        Read serial numbers from an Excel file.

        Args:
            file_path (str): The path to the Excel file.

        Returns:
            list: List of serial numbers read from the Excel file.
        """
        if file_path:
            df = pd.read_excel(file_path, header=None)  # Read Excel file into DataFrame
            if not df.empty:
                return df.iloc[:, 0].tolist()  # Return first column as list
        return []  # Return empty list if file is empty or doesn't exist

    def get_serials_limit(self):
        """
        Get the limit of serial numbers that can be stored.

        Returns:
            int: The limit of serial numbers.
        """
        return self.serials_limit

    def is_serial_in_db(self, serial) -> bool:
        """
        Check if a given serial number exists in the database.

        Args:
            serial (str): The serial number to check.

        Returns:
            bool: True if the serial number exists in the database, False otherwise.
        """
        try:
            query = self.query_master.serial_exists_query()  # Get SQL query for checking serial existence
            result = self.client.execute_query(query, params={"serial": serial})  # Execute query with serial as parameter
            result = result['exists'][0]  # Get result from query (assuming it returns 'exists' column)
            return result

        except Exception as e:
            print(f"ERROR: Something went wrong when searching the following serial: {serial}")
            print(e)
            return False

    def validate_serial(self, text) -> str:
        """
        Validate a serial number.

        Args:
            text (str): The serial number to validate.

        Returns:
            str or None: Error message if validation fails, None if validation succeeds.
        """
        if text is None:
            return "The serial cannot be empty!"  # Check if serial is empty

        if bool(re.search(r'\W', text)):  # Check if serial contains non-alphanumeric characters
            return "The serial must contain only letters and numbers!"

        if text in self.serials:  # Check if serial is already in the list
            return "The serial is already entered, try another one!"

        if len(text) not in range(5, 30):  # Check if serial length is within a specific range
            return "The serial must have a length between 5 and 20 letters and numbers!"

        if not self.is_serial_in_db(text):  # Check if serial exists in the database
            return "The serial doesn't exist in the database!"

        return None  # Return None if validation passes
