# selenium for web driving
import selenium
from selenium import webdriver

#Opt-in for run underlyied
'''options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')'''

# Using Chrome to access web
driver = webdriver.Chrome() 
# Open the website
driver.get('https://myflye.flyefit.ie/login')
# Select the id box
id_box = driver.find_element_by_name('email_address')
# Send id information
id_box.send_keys('youemail@mail.com')
# Find password box
pass_box = driver.find_element_by_name('password')
# Send password
pass_box.send_keys('yourpassword123')
# Find login button
login_button = driver.find_element_by_name('log_in')
# Click login
login_button.click()

# Book a new workout
book_workout_button = driver.find_element_by_css_selector('a[href^="/myflye/book-workout"]')
book_workout_button.click()
# Click on Next Page(next day)
change_page = driver.find_element_by_class_name('bar__arrow.bar__arrow--next')
change_page.click() 

#Checking the right time in week days.
#checking_time = driver.find_element_by_xpath("//*[@data-course-time='07:00 - 08:15']")
#checking_time.click()

#checking_time = driver.find_elements_by_name('btn-primary.ff_class')  
checking_time = driver.find_element_by_xpath("//*[@data-course-time='06:30 - 07:45']")
checking_time.click()
driver.implicitly_wait(10)
print(checking_time)

#Confirming booking
confirming = driver.find_element_by_xpath("//*[@id='book_class']")
confirming.click()

