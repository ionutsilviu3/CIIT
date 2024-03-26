import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session, sessionmaker
import pandas as pd

from models.query_master import QueryMaster


class SQLClient:
    def __init__(self, url, port, db, user, password):
        """
        Initializes a SQLClient object.

        Args:
            url (str): The URL of the SQL server.
            port (int): The port number of the SQL server.
            db (str): The name of the database.
            user (str): The mail for authentication.
            password (str): The password for authentication.
        """
        self.url = url
        self.port = port
        self.db = db
        self.user = user
        self.password = password
        self.engine = None
        self.session = None
        self.query_master = QueryMaster()

    # Connection function
    def connect(self):
        try:
            connection_string = f"postgresql://{self.user}:{self.password}@{self.url}:{self.port}/{self.db}"
            self.engine = create_engine(connection_string)
            Session = sessionmaker(bind=self.engine)
            self.session = Session()
            print("Connected to the database!")
        except Exception as e:
            print(f"Error connecting to the database: {e}")

    # Disconnect function
    def disconnect(self):
        try:
            if self.session:
                self.session.close()
            if self.engine:
                self.engine.dispose()
            print("Disconnected from the database.")
        except Exception as e:
            print(f"Error disconnecting from the database: {e}")

    def isUserExisting(self, mail, password):
        try:
            # Define the SQL query with placeholders
            query = text(self.query_master.get_user_credentials_query())
            # Execute the query with parameters
            result = self.execute_query(query, params={"mail": mail, "password": password})
            if result is not None and not result.empty:
                return True
            else:
                return False

        except Exception as e:
            print(f"Error during login: {e}")
            return False
    
    # Query execution function

    def execute_query(self, query, params=None):
        try:
            df = pd.read_sql(query, self.engine, params=params)
            return df
        except Exception as e:
            print(f"SQL query execution error: {e}")
        return None

    def execute_query_as_list(self, query):
        try:
            df = pd.read_sql(query, self.engine)
            return df.reset_index(drop=True)
        except Exception as e:
            print(f"SQL query execution error: {e}")
        return None