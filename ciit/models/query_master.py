class QueryMaster:
    def get_user_credentials_query(self):
        return "SELECT * FROM users WHERE email = :email AND password = :password"
    def get_serials(self):
        return "SELECT * FROM serials"
    def insert_serials(self):
        return "INSERT INTO "