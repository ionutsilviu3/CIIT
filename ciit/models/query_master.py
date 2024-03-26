class QueryMaster:
    def get_user_credentials_query(self):
        return "SELECT * FROM users WHERE mail = :mail AND password = :password"
