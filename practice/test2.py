from selenium import webdriver
# import Config

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36")

driver = webdriver.Chrome('C:/python study/selenium/chromedriver',options=options)

url = 'https://www.pushbullet.com/#setup'
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}

# driver = webdriver.Chrome('C:/python study/selenium/chromedriver')
driver.implicitly_wait(10)
driver.get(url)
driver.maximize_window()



driver.find_element_by_xpath("//img[@alt='Sign up with Google']").click()
driver.find_element_by_css_selector('.whsOnd.zHQkBf').send_keys('lys851318@gmail.com')
driver.find_element_by_xpath("//span[@class='VfPpkd-vQzf8d']").click()

# time.sleep(1)