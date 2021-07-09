from selenium import webdriver
import pc_signUp

def test_signUp():
    URL = 'https://front-qa.wemakeprice.com/user/join/general'
    driver = webdriver.Chrome('C:/python study/pc/etc/chromedriver.exe')
    driver.implicitly_wait(30)
    driver.get(URL)
    driver.maximize_window()
    signup = pc_signUp.SignUp(driver)
    signup.signUp_into_web()

test_signUp()