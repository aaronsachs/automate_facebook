from selenium.webdriver.common.action_chains import ActionChains

class BaseDriver(object):
    
    # Setup driver instance for the class, go to base_url
    def __init__(self, webdriver, base_url = "https://www.facebook.com"):
        self.base_url = base_url
        self.driver = webdriver
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(base_url)
    
    # Clicks the web element with id == elt_id by default (returns None)
    # If not click then returns the element itself
    def click_or_return_elt_with_id(self, elt_id, click = True):
        elt = self.driver.find_element_by_id(elt_id)
        action = ActionChains(self.driver).click(elt)
        return action.perform() if click else elt
    
    # Returns web element with id == elt_id by default
    # If input string provided, then sends input to elt (returns None)
    def send_input_or_return_elt_with_id(self, elt_id, send_input = ""):
        elt = self.driver.find_element_by_id(elt_id)
        action = ActionChains(self.driver).click(elt).send_keys(send_input)
        return action.perform() if send_input else elt
    
    # Quits the browser
    def teardown(self):
        self.driver.quit()
