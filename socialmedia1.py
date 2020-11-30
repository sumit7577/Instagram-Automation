from selenium import webdriver  
from selenium.webdriver.firefox.firefox\_binary import FirefoxBinary
import  clipboard
import time
import random
import  names as a


binary = FirefoxBinary('/root/Downloads/firefox/firefox')  
driver = webdriver.Firefox(firefox\_binary=binary)

name = a.get_first_name()
passw = "test@"+str(random.randrange(0,10000))

def tempmail():
    while True:
      driver.get("https://generator.email")
      driver.find_element_by_css_selector("button[type=button]").send_keys(submit)
      email = driver.find_element_by_id("copbtn").getText()
      time.sleep(4)
      insta()
      
def insta():
  while True:
    driver.get("https://www.instagram.com/accounts/emailsignup/")
      driver.find_element_by_name("emailOrPhone").send_keys(str(email))
      driver.find_element_by_name("fullName").send_keys(name+" kumar")
      driver.find_element_by_name("username").send_keys(name+str(random.randrange(0,100)))
      driver.find_element_by_name("password").send_keys(passw)
      btn = driver.find_element_by_xpath("//*[@id="react-root"]/section/main/div/div/div[1]/div/form/div[7]/div/button")
    btn.click()
    with open("/storage/emulated/0",mode = "w") as file:
    	file.write(email, passw)
    	
tempmail()