from views.admin_window import AdminWindow


class AdminController:
    def __init__(self, app, model):
        self.model = model
        self.view = AdminWindow(app)
        self.view.validate_signal.connect(self.validate_input_email)
        self.view.delete_user_signal.connect(self.delete_user)
        self.view.user_selected_signal.connect(self.user_selected)
    
    def add_new_user(self, email):
        self.model.add_new_user(email)
        self.view.add_new_user(email)
    
    def delete_user(self, email):
        user_id = self.model.get_user_by_email(email)['id'][0]
        self.model.delete_user(int(user_id))
        self.view.delete_user(email)
        
    def modify_user_role(self, email, role):
        user_id = self.model.get_user_by_email(email)['id'][0]
        engineer_role_id = self.model.get_role_id_by_name("Engineer")
        manager_role_id = self.model.get_role_id_by_name("Manager")
        if role == "Manager":
            self.model.modify_user_role(int(user_id), engineer_role_id)
            self.view.modify_user_role(email, "Engineer")
        elif role =="Engineer":
            self.model.modify_user_role(int(user_id), manager_role_id)
            self.view.modify_user_role(email, "Manager")
            #update chart when existing
    
    def user_selected(self, email, role):
        if role != "Unregistred":
            self.view.enable_modify_role_button(role)
        self.view.enable_delete_button()
        
    def validate_input_email(self):
        email = self.view.get_input()
        result = self.is_email_valid(email)
        if result is not None:
            self.view.handle_error_message(True, custom_message=result)
        else:
            self.add_new_user(email)
 
    def is_email_valid(self, email):
        result = self.model.validate_email(email)
        return result
 
    def show_users(self):
        user_role = self.model.get_role(self.model.current_user_id)
        user_role = int(user_role['id'][0])
        users = self.model.get_subordinate_users(user_role)
        self.view.set_users(users)
        self.view.update_chart()
        
