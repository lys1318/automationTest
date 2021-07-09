from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pc_targetChk
import pyautogui as py
import time

pwd = 'qwer1234'
timeout = 10

class SignUp:
    def __init__(self, driver):
        self.driver = driver
    
    def signUp_into_web(self):
        index = 1
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, '_personalEmailId'))).send_keys('test000'+str(index))
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, '_personalEmailAddr'))).send_keys('naver.com')
        py.hotkey('tab')
        
        emailChk = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//p[@data-join-area="email"]'))).get_attribute('style')

        while emailChk == 'display: block;':
            tryId = ''
            index += 1
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, '_personalEmailId'))).clear()
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, '_personalEmailId'))).send_keys('test000'+str(index))
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//label[@for="_password"]'))).click()
            emailChk = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//p[@data-join-area="email"]'))).get_attribute('style')
            tryId = 'test000'+str(index)+'@naver.com'

        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, '_password'))).send_keys(pwd)
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, '_pwConfirm'))).send_keys(pwd)
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, '_name'))).send_keys('이영성')
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, '_phone'))).send_keys('01071271318')
        py.hotkey('tab')

        phoneCertChk = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, '_phoneConfirm'))).text

        if phoneCertChk:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btns_sys.bluegray_mid_d'))).click()
            time.sleep(1)
            self.driver.switch_to_alert().accept()
            
            w = py.getWindowsWithTitle("Pushbullet - Your devices working better together - Chrome")[0]
            
            if w.isActive == False:
                w.activate()
            
            pc_targetChk.my_click("C:/python study/pc/etc/CertificationNumberSend.png", 60)

            CertNumber = py.locateOnScreen("C:/python study/pc/etc/CertificationNumber.png", confidence=0.8)

            py.click(CertNumber)
            py.sleep(1)
            py.moveTo(796, 894)
            py.doubleClick()
            py.hotkey('ctrl','c')
            py.hotkey('alt','tab')
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, '_certifyNo'))).click()
            py.hotkey('ctrl','v')
            py.hotkey('backspace')
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btns_sys.bluegray_mid_d'))).click()
            time.sleep(1)
            self.driver.switch_to_alert().accept()
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, '_birth'))).send_keys('19850223')
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.chk_box.chk_big .ico'))).click()
        else:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, '_birth'))).send_keys('19850223')
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.chk_box.chk_big .ico'))).click()

        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btns_sys.red_big_xb.add_space'))).click()
        time.sleep(2)

        completeId = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, 'point'))).text
        if completeId == tryId:
            print("회원가입 성공")
        else:
            print("회원가입 실패")

        self.driver.quit()