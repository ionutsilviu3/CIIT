class QueryMaster:
    def get_user_credentials_query(self):
        return "SELECT * FROM users WHERE email = :email AND password = :password"

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
