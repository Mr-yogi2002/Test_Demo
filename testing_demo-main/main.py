# main.py
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from locators import Test_Locators
# from excel_functions import Excel_Functions
# from selenium.webdriver.common.action_chains import ActionChains
# url= "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
#
# dashboard_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
#
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get(url)
# driver.implicitly_wait(15)
#
#
# excel_file = "test_data.xlsx"
#
# Sheet_number = 'Sheet1'
#
# a=Excel_Functions(excel_file, Sheet_number)
# # row = s.Row_Count()
# rows = a.Row_Count()
# for row in range(2,rows+1):
#     username = a.Read_Data(row,6)
#     password = a.Read_Data(row,7)
#     driver.find_element(by=By.NAME,value=Test_Locators().username_locator).send_keys(username)
#     driver.find_element(by=By.NAME,value=Test_Locators().password_locator).send_keys(password)
#     driver.find_element(by=By.NAME,value=Test_Locators().submit_button).click()
#     driver.implicitly_wait(10)
#     if ('https://www.facebook.com/checkpoint/?next' in driver.current_url):
#         print('Success : Test Success with username:{a}'.format(a = username))
#         a.Write_Data(row,8,'TEST PASS')
#         driver.back()
#     elif('https://www.facebook.com' in driver.current_url):
#         print('Failed : Test Failed with username:{a}'.format(a = username))
#         a.Write_Data(row,8,'TEST FAIL')
#         driver.back()
# driver.quit()


# driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.maximize_window()
# driver.get(url)
# driver.implicitly_wait(15)

#
# for row in range(2,row+1):
#     username = s.Read_Data(row,6)
#     password = s.Read_Data(row,7)
#
#     driver.find_element(by=By.NAME,value=Test_Locators().username_locator).send_keys(username)
#     driver.find_element(by=By.NAME,value=Test_Locators().password_locator).send_keys(password)
#     driver.find_element(by=By.XPATH,value=Test_Locators().submit_button).click()

    # driver.implicitly_wait(15)
    # if dashboard_url in driver.current_url:
    #     print("SUCCESS : Login success with username {a}".format(a=username))
    #     s.Write_Data(row,8,"TEST PASS")
    #     logout_click1 = driver.find_element(by=By.XPATH,value=Test_Locators().logout_click)
    #     logout_click1.click()
    #     logout_button1 = driver.find_element(by=By.XPATH,value=Test_Locators().logout_button)
    #     action = ActionChains(driver)
    #     action.click(on_element=logout_button1).perform()
    #     driver.find_element(by=By.LINK_TEXT,value="Logout").click()
    #
    # elif(url in driver.current_url):
    #     print("FAIL: Login failure with username {a}".format(a=username))
    #     s.Write_Data(row,8,"TEST FAIL")
    #     driver.back()




#
# # close the web browser
# driver.quit()



