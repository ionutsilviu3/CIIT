import re
import bcrypt
import numpy as np
import pandas as pd


class UserModel:
    def __init__(self, client, query_master):
        self.client = client
        self.query_master = query_master
        self.current_user_id = None

    def is_valid(self, user_credentials):
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
        query = self.query_master.get_user_by_email_query()
        result = self.client.execute_query(query, params={"email": email})
        if result is not None and not result.empty:
            return result
        return None

    def get_role(self, user_id):
        query = self.query_master.get_user_role_query()
        result = self.client.execute_query(query, params={"user_id": user_id})
        return result

    def get_all_users(self):
        query = self.query_master.get_all_users_emails_query()
        result = self.client.execute_query(query)
        return result

    def get_subordinate_users(self, role_id):
        query = self.query_master.get_subordinate_users_query()
        result = self.client.execute_query(query, params={"role_id": role_id})
        return result

    def delete_user(self, user_id):
        query = self.query_master.delete_user_by_id_query()
        self.client.execute_query(
            query, params={"id": user_id}, fetch_results=False)

    def modify_user_role(self, user_id, role_id):
        query = self.query_master.modify_user_role_query()
        self.client.execute_query(
            query, params={"user_id": user_id, "role_id": role_id}, fetch_results=False)

    def add_new_user(self, email):
        role_name = "Unregistered"
        role_id = self.get_role_id_by_name(role_name)
        query = self.query_master.create_new_user_query()
        self.client.execute_query(
            query, params={"email": email, "role_id": role_id}, fetch_results=False)
        new_user = self.get_user_by_email(email)
        new_user_id = int(new_user['id'][0])
        self.insert_ids(new_user_id, role_id)

    def get_role_id_by_name(self, role_name):
        query = self.query_master.get_role_id_query()
        result = self.client.execute_query(
            query, params={"role_name": role_name})
        return int(result['id'][0])

    def insert_ids(self, user_id, role_id):
        query = self.query_master.insert_ids_in_user_roles_query()
        self.client.execute_query(
            query, params={"user_id": user_id, "role_id": role_id}, fetch_results=False)

    def set_hashed_password(self, user_id, hashed_password):
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
        # Generate a salt
        salt = bcrypt.gensalt()
        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode(), salt)
        # Return the hashed password as a string
        return hashed_password.decode()

    def is_email_in_valid_format(self, email):
        pattern = r'^([!#-\'*+/-9=?A-Z^-~-]+(\.[!#-\'*+/-9=?A-Z^-~-]+)*|"([]!#-[^-~ \t]|(\\\\[\\t -~]))+")@([!#-\'*+/-9=?A-Z^-~-]+(\.[!#-\'*+/-9=?A-Z^-~-]+)*|\[[\t -Z^-~]*])$'
        if re.match(pattern, email) is None:
            return False
        return True

    def validate_email(self, email) -> str:
        if email is None:
            return "The email can not be empty!"

        if self.is_email_in_valid_format(email) == False:
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
        # Verify the password
        return bcrypt.checkpw(password.encode(), hashed_password.encode())

    # TODO remove, used for temp inserts
    def boilerplate():

        pass
        # TODO remove, used for temp inserts
        # df = self.client.execute_query(self.query_master.get_process_events())
        # print(df)
        # r = self.generate_results(df)
        # results = pd.DataFrame(r)
        # self.replace_results_table(results)

        # serials = self.client.execute_query(self.client.query_master.get_serials())
        # serials = serials[serials['serial_type_id'] == 1]

        # process_events, results = models.create_serials_script.generate_data(serials)

        # process_event_chunks = [process_events[i:i+1000] for i in range(0, len(process_events), 1000)]
        # result_chunks = [results[i:i+1000] for i in range(0, len(results), 1000)]

        # for chunk in process_event_chunks:
        #     self.client.insert_process_events(chunk)
        # for chunk in result_chunks:
        #     self.client.insert_results(chunk)
    def generate_results(self, process_events_df):
        results = []

        # Predefined parameters and limits
        parameters_data = [
            {'name': 'Voltage', 'unit_of_measurement': 'V'},
            {'name': 'Current Draw', 'unit_of_measurement': 'A'},
            {'name': 'Resistance', 'unit_of_measurement': 'ohm'},
            {'name': 'Motor RPM', 'unit_of_measurement': 'RPM'},
            {'name': 'Pressure', 'unit_of_measurement': 'psi'},
            {'name': 'Flow Rate', 'unit_of_measurement': 'liters per hour'},
            {'name': 'Efficiency', 'unit_of_measurement': '%'},
            {'name': 'Sound Levels', 'unit_of_measurement': 'dB(A)'},
            {'name': 'Harmonic Distortion', 'unit_of_measurement': '%'},
            {'name': 'Operating Temperature', 'unit_of_measurement': '°C'}
        ]

        limits_data = [
            {'parameter_id': 1, 'lower_limit': 11.4, 'upper_limit': 12.6},
            {'parameter_id': 2, 'lower_limit': 4.75, 'upper_limit': 15.25},
            {'parameter_id': 3, 'lower_limit': 0, 'upper_limit': 0.95},
            {'parameter_id': 4, 'lower_limit': 1900, 'upper_limit': 6100},
            {'parameter_id': 5, 'lower_limit': 28.5, 'upper_limit': 81.5},
            {'parameter_id': 6, 'lower_limit': 95, 'upper_limit': 205},
            {'parameter_id': 7, 'lower_limit': 69.5, 'upper_limit': 100},
            {'parameter_id': 8, 'lower_limit': 0, 'upper_limit': 66.5},
            {'parameter_id': 9, 'lower_limit': 0, 'upper_limit': 4.75},
            {'parameter_id': 10, 'lower_limit': -42, 'upper_limit': 122}
        ]

        # Loop through each row in the process events DataFrame
        for index, row in process_events_df.iterrows():
            station_id = row['station_id']
            # Assuming 'id' column represents the event ID
            event_id = row['id']
            # Assuming 'end_time' is the correct column for the event creation time
            created_at = row['end_time']

            # Determine parameter range based on station ID
            if station_id == 1:
                parameter_range = range(1, 5)
            elif station_id == 2:
                parameter_range = range(5, 8)
            elif station_id == 3:
                parameter_range = range(8, 10)
            elif station_id == 4:
                parameter_range = [10]
            else:
                continue  # Skip if station ID is invalid

            # Generate results for each parameter in the determined range
            for parameter_id in parameter_range:
                # Adjust index to match list indexing
                parameter_data = parameters_data[parameter_id - 1]
                lower_limit = next(
                    limit['lower_limit'] for limit in limits_data if limit['parameter_id'] == parameter_id)
                upper_limit = next(
                    limit['upper_limit'] for limit in limits_data if limit['parameter_id'] == parameter_id)

                # Calculate midpoint of the limits range
                midpoint = (lower_limit + upper_limit) / 2

                # Generate result with variation around the midpoint using normal distribution
                # Adjust scale depending on the range of limits
                scale = (upper_limit - lower_limit) / \
                    20  # Adjust this factor as needed
                value = np.random.normal(midpoint, scale)

                # Ensure generated value is within limits range
                value = max(lower_limit, min(upper_limit, value))

                result = {
                    "event_id": event_id,
                    "parameter_id": parameter_id,
                    "value": value,
                    "created_at": created_at
                }
                results.append(result)

        return results
    # TODO remove, used for temp inserts

    def replace_results_table(self, new_results):
        try:

            # Create a new results table using the same schema
            create_query = """
                CREATE TABLE results (
                    -- Define columns based on your schema
                    id SERIAL PRIMARY KEY,
                    event_id INT,
                    parameter_id INT,
                    value FLOAT,
                    created_at TIMESTAMP
                )
            """
            self.client.execute_query(create_query)

            # Convert new_results to DataFrame
            new_results_df = pd.DataFrame(new_results)

            # Insert new records into the new results table
            new_results_df.to_sql(
                'results', self.client.engine, if_exists='append', index=False)

            # Commit the changes
            self.client.session.commit()

            print("Results table replaced successfully!")
        except Exception as e:
            print(f"Error replacing results table: {e}")
    # TODO remove, used for temp inserts

    def modify(self):
        df = self.client.execute_query(self.query_master.get_results())
        # Initialize variables
        event_id = 1

        # Iterate over each row in the DataFrame
        for index, row in df.iterrows():
            # Assign the current event_id to the row
            df.at[index, 'event_id'] = event_id
            # Update event_id according to the rules
            if row['parameter_id'] == 4:
                event_id += 1
            elif row['parameter_id'] == 7:
                event_id += 1
            elif row['parameter_id'] == 9:
                event_id += 1
            elif row['parameter_id'] == 10:
                event_id += 1

        self.client.execute_query_t(df, update=True, batch_size=1000)
