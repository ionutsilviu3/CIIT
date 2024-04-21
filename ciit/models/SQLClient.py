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
            url (str): The URL of the SQL server.
            port (int): The port number of the SQL server.
            db (str): The name of the database.
            user (str): The mail for authentication.
            password (str): The password for authentication.
        """
        self.end_point = end_point
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

    def isUserExisting(self, email, password):
        try:
            # Define the SQL query with placeholders
            query = text(self.query_master.get_user_credentials_query())
            # Execute the query with parameters
            result = self.execute_query(query, params={"email": email, "password": password})
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
    
    # Insert process events into the database
    def insert_process_events(self, process_events):
        try:
            with self.engine.begin() as conn:
                process_event_values = ', '.join(f"({event['event_type_id']}, {event['serial_id']}, {event['station_id']}, '{event['start_time']}', '{event['end_time']}')" for event in process_events)
                process_event_query = f"INSERT INTO ProcessEvents (event_type_id, serial_id, station_id, start_time, end_time) VALUES {process_event_values};"

                # Execute the SQL insert statement for process events chunk
                conn.execute(text(process_event_query))
            print("Process events inserted successfully!")
        except Exception as e:
            print(f"Error inserting process events into the database: {e}")



    # Insert results into the database
    def insert_results(self, results):
        try:
            print("START")
            with self.engine.begin() as conn:
                result_values = ', '.join(f"({result['event_id']}, {result['parameter_id']}, {result['value']}, '{result['created_at'].strftime('%Y-%m-%d %H:%M:%S')}')" for result in results)
                result_query = f"INSERT INTO Results (event_id, parameter_id, value, created_at) VALUES {result_values};"

                # Execute the SQL insert statement for results chunk
                conn.execute(text(result_query))
            print("Results inserted successfully!")
        except Exception as e:
            print(f"Error inserting results into the database: {e}")







