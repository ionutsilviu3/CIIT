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
            if self.engine:
                self.engine.dispose()
            print("Disconnected from the database.")
        except Exception as e:
            print(f"Error disconnecting from the database: {e}")
        
    #TODO remove, used for temp inserts
    def execute_query_t(self, df, update=False, batch_size=1000):
        """
        Executes queries on the database in batches.

        Args:
            df (DataFrame): The DataFrame containing the data to be used in queries.
            update (bool): Flag to indicate whether to perform update or select operation.
            batch_size (int): The size of each batch for update operations.
        """
        try:
            if update:
                # Update the database in batches
                with self.engine.connect() as connection:
                    with connection.begin():
                        total_records = len(df)
                        for chunk_start in range(0, total_records, batch_size):
                            chunk_end = min(chunk_start + batch_size, total_records)
                            chunk_df = df.iloc[chunk_start:chunk_end]
                            # Construct the UPDATE query
                            update_query = "UPDATE results SET event_id = :event_id WHERE id = :id"
                            # Execute the UPDATE query for the current chunk
                            for index, row in chunk_df.iterrows():
                                connection.execute(text(update_query), {"event_id": row['event_id'], "id": row['id']})
                            print(f"Updated {chunk_end} records out of {total_records}")
                print("Database table updated successfully!")
            else:
                # Execute the SELECT query
                query = "SELECT * FROM results"
                result_df = pd.read_sql(query, self.engine)
                return result_df
        except Exception as e:
            print(f"SQL query execution error: {e}")
        return None

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
