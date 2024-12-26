from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
chrome=Options()
#chrome.add_argument("--headless")
driver=webdriver.Chrome(options=chrome)
driver.get("https://www.amazon.in/")
driver.execute_script("alert('Hi This is Narendra');")
time.sleep(10)
alert=Alert(driver)
print()
print(alert.text)
print()
alert.accept()
driver.maximize_window()
print(driver.get_window_size())
win=driver.window_handles
driver.execute_script("window.open('https://google.com','_blank');")
#driver.switch_to(win[0])
driver.switch_to.window(win[0])
sel=driver.find_element(By.XPATH,"//select[@class='nav-search-dropdown searchSelect nav-progressive-attrubute nav-progressive-search-dropdown']")
sel.click()
select=Select(sel)
all=select.options
for i in all:
    print(i.text)
#select.select_by_index(2)
time.sleep(4)

select.select_by_visible_text("Baby")
print(driver.get_window_size())
screen=driver.get_screenshot_as_png()
with open('screenshot.png', 'wb') as file:
    file.write(screen)
ab=driver.find_element(By.XPATH,"//a[@class='nav-a  '][2]")
actions=ActionChains(driver)
actions.move_to_element(ab).context_click().perform()
time.sleep(10)
