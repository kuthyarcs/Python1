import selenium
import selenium.webdriver
 
# Initialize a Chrome browser
driver = selenium.webdriver.Chrome()
 
# Open a website
driver.get('https://example.com')
 
# Find an element by its ID and interact with it
element = driver.find_element_by_id('some_element_id')
element.click()
 
# Perform assertions or other actions as needed
 
# Close the browser
driver.quit()
