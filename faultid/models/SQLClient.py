import os
from datetime import datetime
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session, sessionmaker
import pandas as pd

from models.query_master import QueryMaster


class SQLClient:
    def __init__(self, end_point, port, db, user, password):
        """
        Initializes a SQLClient object.

        Args:
            end_point (str): The end_point of the AWS RDS.
            port (int): The port number of the SQL server.
            db (str): The name of the database.
            user (str): The user for authentication.
            password (str): The password for authentication.
        """
        self.end_point = end_point
        self.port = port
        self.db = db
        self.user = user
        self.password = password
        self.engine = None
        self.session = None
        
    def __del__(self):
        self.disconnect()

    def connect(self):
        """
        Establishes a connection to the database.
        """
        try:
            connection_string = f"postgresql://{self.user}:{self.password}@{self.end_point}:{self.port}/{self.db}"
            self.engine = create_engine(connection_string)
            Session = sessionmaker(bind=self.engine)
            self.session = Session()
            
            print("Connected to the database!")
        except Exception as e:
            print(f"Error connecting to the database: {e}")

    def disconnect(self):
        """
        Closes the connection to the database.
        """
        try:
            if self.session:
                self.session.close()
            else:
                print("No session to close.")

            if self.engine:
                self.engine.dispose()
            else:
                print("No engine to dispose.")
        except Exception as e:
            print(f"Error disconnecting from the database: {e}")

    def execute_query(self, query, params=None, fetch_results=True):
        """
        Executes a SQL query on the database.

        Args:
            query (str): The SQL query to be executed.
            params (dict): The parameters for the SQL query.
            fetch_results (bool): Flag to indicate whether to fetch results or not.

        Returns:
            DataFrame: The results of the query if fetch_results is True, else None.
        """
        try:
            with self.engine.connect() as connection:
                if fetch_results:
                    df = pd.read_sql(text(query), self.engine, params=params)
                    return df
                else:
                    connection.execute(text(query), params)
                    connection.commit()
        except Exception as e:
            print(f"SQL query execution error: {e}")
        return None

    def execute_query_as_list(self, query):
        """
        Executes a SQL query and returns the results as a list.

        Args:
            query (str): The SQL query to be executed.

        Returns:
            DataFrame: The results of the query as a DataFrame.
        """
        try:
            df = pd.read_sql(query, self.engine)
            return df.reset_index(drop=True)
        except Exception as e:
            print(f"SQL query execution error: {e}")
        return None
