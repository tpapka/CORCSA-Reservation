from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

first_name = ""
last_name = ""
yob = ""
email = ""
phone = ""

chrome_options = Options()
prefs = {"profile.managed_default_content_settings.images":2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--headless")
chrome_options.binary_location = 'C:\\Users\\JohnSmith\\AppData\\Local\\Google\\Chrome SxS\\Application\\chrome.exe'    
browser = webdriver.Chrome("C:\\Users\\JohnSmith\\AppData\\Local\\Programs\\Python\\chromedriver.exe", chrome_options=chrome_options)  

browser.get("https://coloradodor.hosted.acftechnologies.com/WAColorado/ACFCustom/Service.aspx")

def check_date_avaialbility():
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.NAME, "ctl00$cphBody$rptService$ctl00$btnService1"))).click()
    browser.find_element_by_id("cphBody_rptUnits_btnService1_1").click()
    browser.find_element_by_id("ctl00_cphBody_rdcAvailableDates_FNN").click()
    #time.sleep(1)
    try:
        print("Searching for available day... ")
        WebDriverWait(browser, 1).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@style, 'background-color:#3C9770;')]"))).click()
        WebDriverWait(browser, 1).until(EC.presence_of_element_located((By.XPATH, "//*[@id='cphBody_rblAvailableTimes']/option[2]"))).click()
        browser.find_element_by_id("cphBody_btnNext").click()
        form_data()
    except:
        print("There are no available dates. Next page... \n")
        browser.find_element_by_id("cphBody_lnkbtnHome").click()
    
    check_date_avaialbility()

def form_data():
    print("Filling up the form...")
    WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.ID, "cphBody_txbFirstName"))).send_keys(first_name)
    browser.find_element_by_id("cphBody_txbLastName").send_keys(last_name)
    browser.find_element_by_id("cphBody_txbYOB").send_keys(yob)
    browser.find_element_by_id("cphBody_txbEmail").send_keys(email)
    browser.find_element_by_id("cphBody_txbPhoneNumber").send_keys(phone)
    browser.find_element_by_id("cphBody_btnSubmit").click()
    print("You should be getting confirmation email shortly...")
    #browser.close()

check_date_avaialbility()
