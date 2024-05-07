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

    # Connection function
    def connect(self):
        try:
            connection_string = f"postgresql://{self.user}:{self.password}@{self.end_point}:{self.port}/{self.db}"
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
        
    #TODO remove, used for temp inserts
    def execute_query_t(self, df, update=False, batch_size=1000):
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



    def execute_query(self, query, params=None):
        try:
            df = pd.read_sql(text(query), self.engine, params=params)
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







