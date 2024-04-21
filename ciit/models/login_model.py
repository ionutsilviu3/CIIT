import os
from models.SQLClient import SQLClient
from dotenv import find_dotenv, load_dotenv
import models.create_serials_script

class LoginModel:
    def __init__(self):
        dotenv_path = find_dotenv()
        load_dotenv(dotenv_path)
        self.client = SQLClient(os.getenv("END_POINT"), os.getenv(
            "PORT"), os.getenv("DB"), os.getenv("USER"), os.getenv("PASSWORD"))
        self.user_credentials = {}
        self.client.connect()
        
        # serials = self.client.execute_query(self.client.query_master.get_serials())
        # serials = serials[serials['serial_type_id'] == 1]
        
        # process_events, results = models.create_serials_script.generate_data(serials)
 
        # process_event_chunks = [process_events[i:i+1000] for i in range(0, len(process_events), 1000)]
        # result_chunks = [results[i:i+1000] for i in range(0, len(results), 1000)]      

        # for chunk in process_event_chunks:
        #     self.client.insert_process_events(chunk)
        # for chunk in result_chunks:
        #     self.client.insert_results(chunk)
        
    def __del__(self):
        self.client.disconnect()

    def set_credentials(self, user_credentials):
        self.user_credentials = user_credentials
        
    def is_valid(self, user_credentials):
        return self.client.isUserExisting(user_credentials.get('email'),user_credentials.get('password'))
