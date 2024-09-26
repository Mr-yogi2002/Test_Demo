# code for data driven framework
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from locators import Test_Locators
from excel_functions import Excel_Functions

url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
dashboard_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
Excel_file = "test_data.xlsx"
Sheet_number = 'Sheet1'

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(15)
a=Excel_Functions(Excel_file,Sheet_number)
rows = a.Row_Count()
for row in range(2,rows+1):
    username = a.Read_Data(row,6)
    password = a.Read_Data(row,7)
    driver.find_element(by=By.XPATH,value=Test_Locators().username_locator).send_keys(username)
    driver.find_element(by=By.XPATH,value=Test_Locators().password_locator).send_keys(password)
    driver.find_element(by=By.XPATH,value=Test_Locators().submit_button).click()
    driver.implicitly_wait(10)
    if (dashboard_url in driver.current_url):
        print('Success : Test Success with username:{a}'.format(a=username))
        a.Write_Data(row,8,'TEST PASS')
        driver.back()
    elif(url in driver.current_url):
        print('Failed : Test Failed with username:{a}'.format(a=username))
        a.Write_Data(row,8,'TEST FAIL')
        driver.back()
driver.quit()
