from base_driver import BaseDriver
import time

class NavBar(BaseDriver):

	# Clicks dropdown menu in NavBar
    def dropdown_menu_button(self, click = True):
        return self.click_or_return_elt_with_id(
            elt_id = "logoutMenu", 
            click = click
        )
    
    # Clicks logout button
    def logout_button(self, click = True):
    	# If dropdown menu not open, then open it
        dropdown_elt = self.dropdown_menu_button(click = False)
        dropdown_class = dropdown_elt.get_attribute("class")
        
        if not "openToggler" in dropdown_class: self.dropdown_menu_button() 
        
        return self.click_or_return_elt_with_id(
            elt_id = "show_me_how_logout_1", 
            click = click
        )