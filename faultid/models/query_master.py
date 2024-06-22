class QueryMaster:
    def get_user_by_email_query(self):
        """
        Returns the SQL query to get a user by their email.

        Returns:
            str: The SQL query string.
        """
        return """SELECT *
                  FROM users
                  WHERE email = :email;
               """

    def get_all_users_emails_query(self):
        """
        Returns the SQL query to get all user emails.

        Returns:
            str: The SQL query string.
        """
        return "SELECT email FROM users"

    def get_subordinate_users_query(self):
        """
        Returns the SQL query to get subordinate users by role ID.

        Returns:
            str: The SQL query string.
        """
        return """SELECT users.email, roles.name 
                  FROM users, roles, user_roles
                  WHERE user_roles.user_id = users.id
                  AND user_roles.role_id = roles.id
                  AND roles.id > :role_id
               """

    def delete_user_by_id_query(self):
        """
        Returns the SQL query to delete a user by their ID.

        Returns:
            str: The SQL query string.
        """
        return """DELETE FROM user_roles
                  WHERE user_id = :id;
                  DELETE FROM users
                  WHERE id = :id;
               """
    
    def get_user_role_query(self):
        """
        Returns the SQL query to get the role of a user by their user ID.

        Returns:
            str: The SQL query string.
        """
        return """SELECT roles.id, roles.name 
                  FROM user_roles, roles
                  WHERE user_roles.user_id = :user_id
                  AND user_roles.role_id = roles.id
               """
    
    def modify_user_role_query(self):
        """
        Returns the SQL query to modify the role of a user by their user ID.

        Returns:
            str: The SQL query string.
        """
        return """UPDATE user_roles
                  SET role_id = :role_id
                  WHERE user_id = :user_id;
               """
    
    def set_user_password_query(self):
        """
        Returns the SQL query to set the password of a user by their user ID.

        Returns:
            str: The SQL query string.
        """
        return """UPDATE users
                  SET password = :password
                  WHERE id = :id;
               """
    
    def create_new_user_query(self):
        """
        Returns the SQL query to create a new user with the given email.

        Returns:
            str: The SQL query string.
        """
        return """INSERT INTO users (email) 
                  VALUES (:email);
               """
    
    def get_role_id_query(self):
        """
        Returns the SQL query to get the role ID by the role name.

        Returns:
            str: The SQL query string.
        """
        return """SELECT id 
                  FROM roles 
                  WHERE name = :role_name;
               """
    
    def insert_ids_in_user_roles_query(self):
        """
        Returns the SQL query to insert user and role IDs into the user_roles table.

        Returns:
            str: The SQL query string.
        """
        return """INSERT INTO user_roles (user_id, role_id) 
                  VALUES (:user_id, :role_id);
               """
    
    def serial_exists_query(self):
        """
        Returns the SQL query to check if a serial exists.

        Returns:
            str: The SQL query string.
        """
        return """SELECT EXISTS (
                    SELECT 1
                    FROM serials
                    WHERE unit_serial_number = :serial
                  );"""
    
    def get_stations_query(self, serials):
        """
        Returns the SQL query to get distinct station names for given serials.

        Args:
            serials (str): A comma-separated list of serial numbers.

        Returns:
            str: The SQL query string.
        """
        return f"""SELECT DISTINCT S.name
                  FROM ProcessEvents PE
                  JOIN Stations S ON PE.station_id = S.id
                  WHERE PE.serial_id IN (
                      SELECT id
                      FROM Serials
                      WHERE unit_serial_number IN ('{serials}')
                  );
               """
        
    def get_parts_produced(self, station, timeframe_start, timeframe_end):
        """
        Returns the SQL query to get parts produced at a station within a timeframe.

        Args:
            station (str): The station name.
            timeframe_start (str): The start datetime of the timeframe.
            timeframe_end (str): The end datetime of the timeframe.

        Returns:
            str: The SQL query string.
        """
        return f"""SELECT S.unit_serial_number
                  FROM ProcessEvents PE
                  JOIN Stations ST ON ST.id = PE.station_id
                  JOIN Serials S ON S.id = PE.serial_id
                  WHERE ST.name = '{station}'
                  AND PE.end_time BETWEEN '{timeframe_start}' AND '{timeframe_end}'
               """
    
    def get_last_datetime(self, serial):
        """
        Returns the SQL query to get the last datetime of a process event for a given serial.

        Args:
            serial (str): The serial number.

        Returns:
            str: The SQL query string.
        """
        return f"""SELECT max(PE.end_time) as end_time
                  FROM ProcessEvents PE
                  JOIN Serials S ON S.id = PE.serial_id
                  WHERE S.unit_serial_number = '{serial}'
               """

    def get_parameters_query(self, serials, station):
        """
        Returns the SQL query to get parameters for given serials at a station.

        Args:
            serials (str): A comma-separated list of serial numbers.
            station (str): The station name.

        Returns:
            str: The SQL query string.
        """
        return f"""SELECT S.unit_serial_number, P.name, L.lower_limit, R.value, L.upper_limit, R.created_at
                  FROM ProcessEvents PE
                  JOIN Stations ST ON PE.station_id = ST.id
                  JOIN Serials S ON PE.serial_id = S.id
                  JOIN Results R ON PE.id = R.event_id
                  JOIN Parameters P ON R.parameter_id = P.id
                  JOIN Limits L ON L.parameter_id = P.id
                  JOIN ProcessEventTypes PET ON PE.event_type_id = PET.id
                  WHERE S.unit_serial_number IN ('{serials}')
                  AND ST.name = '{station}'
                  AND PET.type = 'Testing'
               """
