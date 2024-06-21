class QueryMaster:
    def get_user_by_email_query(self):
        return """SELECT *
                  FROM users
                  WHERE email = :email;
               """

    def get_all_users_emails_query(self):
        return "SELECT email FROM users"

    def get_subordinate_users_query(self):
        return """SELECT users.email, roles.name FROM users,
                    roles,
                    user_roles
                    WHERE user_roles.user_id  = users.id
                    AND user_roles.role_id = roles.id
                    AND roles.id > :role_id            
                """

    def delete_user_by_id_query(self):
        return """
                  DELETE FROM user_roles
                  WHERE user_id = :id;
                  DELETE FROM users
                  WHERE id = :id;
                  """
    
    def get_user_role_query(self):
        return """SELECT roles.id, roles.name 
                  FROM user_roles,
                       roles
                  WHERE user_roles.user_id = :user_id
                  AND user_roles.role_id = roles.id
               """
    
    def modify_user_role_query(self):
        return """UPDATE User_Roles
                    SET Role_id = :role_id
                    WHERE User_id = :user_id;
                """
    def set_user_password_query(self):
        return """UPDATE users
                SET password = :password
                WHERE id = :id;
                """
    def create_new_user_query(self):
        return """INSERT INTO users (email) VALUES (:email);
                """
    def get_role_id_query(self):
        return """SELECT id FROM roles WHERE name = :role_name;"""
    
    def insert_ids_in_user_roles_query(self):
        return """INSERT INTO user_roles (user_id, role_id) VALUES (:user_id, :role_id);"""
    
    def serial_exists_query(self):
        return """SELECT EXISTS (
                    SELECT 1
                    FROM serials
                    WHERE unit_serial_number = :serial
                    );"""

    def get_stations_query(self, serials):
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
        return f"""
        SELECT S.unit_serial_number
        FROM ProcessEvents PE
        JOIN Stations ST ON ST.id = PE.station_id
        JOIN Serials S ON S.id = PE.serial_id
        WHERE ST.name = '{station}'
        AND PE.end_time BETWEEN '{timeframe_start}' AND '{timeframe_end}'
        """
    
    def get_last_datetime(self, serial):
        return f"""
        SELECT max(PE.end_time) as end_time
        FROM ProcessEvents PE
        JOIN Serials S ON S.id = PE.serial_id
        WHERE S.unit_serial_number = '{serial}'
        """

    def get_parameters_query(self, serials, station):
        return f"""
            SELECT S.unit_serial_number, P.name, L.lower_limit, R.value, L.upper_limit, R.created_at
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
