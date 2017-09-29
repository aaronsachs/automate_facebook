from base_driver import BaseDriver

class HomePage(BaseDriver):

	# Type your email into the home page
    def email_input(self, send_input = ""):
        return self.send_input_or_return_elt_with_id(
            elt_id = "email", 
            send_input = send_input
         )

    # Type your password into the home page
    def password_input(self, send_input = ""):
        return self.send_input_or_return_elt_with_id(
            elt_id = "pass", 
            send_input = send_input
        )
    
    # Click the login button
    def login_button(self, click = True):
        return self.click_or_return_elt_with_id(
            elt_id = "loginbutton", 
            click = click
        )