import time
import argparse
from actions import *

# Parse commandline arguments
parser = argparse.ArgumentParser(description = "Input login info")

# Input email for login, defaults to "default email"
parser.add_argument(
    "--email", 
    default = "default email", 
    help = "login email"
)

# Input password for login, defaults to "default password"
parser.add_argument(
    "--password", 
    default = "default password", 
    help = "login password"
)

# Input driver type (PhantomJS headless or Chrome w/ GUI)
parser.add_argument(
    "--driver_type", 
    choices = ["chrome", "phantomjs"], 
    default = "chrome", 
    help = "choose type of webdriver"
)
args = parser.parse_args()

# Obtain email and password as defined by commandline arguments
email = args.email
password = args.password
dr_type = args.driver_type
driver = webdriver.Chrome() if dr_type == "chrome" else webdriver.PhantomJS()

# Login, get screenshot of NewsFeed, logout, quit the browser
if __name__ == "__main__":
    login(email, password, driver)
    driver.get_screenshot_as_file("news_feed.png")
    logout(driver)
    driver.quit()