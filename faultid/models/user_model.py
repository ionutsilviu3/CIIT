import re
import bcrypt
import numpy as np
import pandas as pd


class UserModel:
    def __init__(self, client, query_master):
        """
        Initialize the UserModel.

        Args:
            client (DatabaseClient): The database client for executing queries.
            query_master (QueryMaster): The query master for generating SQL queries.
        """
        self.client = client
        self.query_master = query_master
        self.current_user_id = None

    def is_valid(self, user_credentials):
        """
        Validate user credentials.

        Args:
            user_credentials (dict): A dictionary containing 'email' and 'password'.

        Returns:
            bool: True if the credentials are valid, False otherwise.
        """
        email = user_credentials.get('email')
        password = user_credentials.get('password')
        user = self.get_user_by_email(email)
        if user is not None:
            hashed_password = user['password'][0]
            if hashed_password is not None:
                if self.verify_password(password, hashed_password):
                    self.current_user_id = int(user['id'][0])
                    return True
            else:
                hashed_password = self.hash_password(password)
                self.current_user_id = int(user['id'][0])
                self.set_hashed_password(self.current_user_id, hashed_password)
                new_role_id = self.get_role_id_by_name("Engineer")
                self.modify_user_role(self.current_user_id, new_role_id)
                return True
        return False

    def get_user_by_email(self, email):
        """
        Retrieve a user by email.

        Args:
            email (str): The email of the user.

        Returns:
            DataFrame: A DataFrame containing user details or None if not found.
        """
        query = self.query_master.get_user_by_email_query()
        result = self.client.execute_query(query, params={"email": email})
        if result is not None and not result.empty:
            return result
        return None

    def get_role(self, user_id):
        """
        Retrieve the role of a user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            DataFrame: A DataFrame containing the user's role.
        """
        query = self.query_master.get_user_role_query()
        result = self.client.execute_query(query, params={"user_id": user_id})
        return result

    def get_all_users(self):
        """
        Retrieve all users.

        Returns:
            DataFrame: A DataFrame containing all users' emails.
        """
        query = self.query_master.get_all_users_emails_query()
        result = self.client.execute_query(query)
        return result

    def get_subordinate_users(self, role_id):
        """
        Retrieve subordinate users based on role ID.

        Args:
            role_id (int): The role ID.

        Returns:
            DataFrame: A DataFrame containing subordinate users.
        """
        query = self.query_master.get_subordinate_users_query()
        result = self.client.execute_query(query, params={"role_id": role_id})
        return result

    def delete_user(self, user_id):
        """
        Delete a user by ID.

        Args:
            user_id (int): The ID of the user to delete.
        """
        query = self.query_master.delete_user_by_id_query()
        self.client.execute_query(
            query, params={"id": user_id}, fetch_results=False)

    def modify_user_role(self, user_id, role_id):
        """
        Modify a user's role.

        Args:
            user_id (int): The ID of the user.
            role_id (int): The new role ID.
        """
        query = self.query_master.modify_user_role_query()
        self.client.execute_query(
            query, params={"user_id": user_id, "role_id": role_id}, fetch_results=False)

    def add_new_user(self, email):
        """
        Add a new user.

        Args:
            email (str): The email of the new user.
        """
        role_name = "Unregistered"
        role_id = self.get_role_id_by_name(role_name)
        query = self.query_master.create_new_user_query()
        self.client.execute_query(
            query, params={"email": email, "role_id": role_id}, fetch_results=False)
        new_user = self.get_user_by_email(email)
        new_user_id = int(new_user['id'][0])
        self.insert_ids(new_user_id, role_id)

    def get_role_id_by_name(self, role_name):
        """
        Get the role ID by role name.

        Args:
            role_name (str): The name of the role.

        Returns:
            int: The role ID.
        """
        query = self.query_master.get_role_id_query()
        result = self.client.execute_query(
            query, params={"role_name": role_name})
        return int(result['id'][0])

    def insert_ids(self, user_id, role_id):
        """
        Insert user ID and role ID into the user roles table.

        Args:
            user_id (int): The user ID.
            role_id (int): The role ID.
        """
        query = self.query_master.insert_ids_in_user_roles_query()
        self.client.execute_query(
            query, params={"user_id": user_id, "role_id": role_id}, fetch_results=False)

    def set_hashed_password(self, user_id, hashed_password):
        """
        Set a hashed password for a user.

        Args:
            user_id (int): The user ID.
            hashed_password (str): The hashed password.
        """
        query = self.query_master.set_user_password_query()
        self.client.execute_query(
            query, params={"id": user_id, "password": hashed_password}, fetch_results=False)

    def hash_password(self, password: str) -> str:
        """
        Hash a password using bcrypt.

        Args:
            password (str): The password to be hashed.

        Returns:
            str: The hashed password.
        """
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode(), salt)
        return hashed_password.decode()

    def is_email_in_valid_format(self, email):
        """
        Check if the email is in a valid format.

        Args:
            email (str): The email to check.

        Returns:
            bool: True if the email is valid, False otherwise.
        """
        pattern = r'^([!#-\'*+/-9=?A-Z^-~-]+(\.[!#-\'*+/-9=?A-Z^-~-]+)*|"([]!#-[^-~ \t]|(\\\\[\\t -~]))+")@([!#-\'*+/-9=?A-Z^-~-]+(\.[!#-\'*+/-9=?A-Z^-~-]+)*|\[[\t -Z^-~]*])$'
        return re.match(pattern, email) is not None

    def validate_email(self, email) -> str:
        """
        Validate an email address.

        Args:
            email (str): The email to validate.

        Returns:
            str: An error message if invalid, otherwise None.
        """
        if email is None:
            return "The email cannot be empty!"
        if not self.is_email_in_valid_format(email):
            return "The email is not in a valid format."
        if self.get_user_by_email(email) is not None:
            return "The user already exists in the database!"
        return None

    def verify_password(self, password: str, hashed_password: str) -> bool:
        """
        Verify a password against a hashed password using bcrypt.

        Args:
            password (str): The password to verify.
            hashed_password (str): The hashed password to compare against.

        Returns:
            bool: True if the password matches the hash, False otherwise.
        """
        return bcrypt.checkpw(password.encode(), hashed_password.encode())