from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.touch_action import TouchAction
import time

timeout = 10
# NAIVE = "NATIVE_APP"
# WEVIEW = "WEBVIEW_com.wemakeprice"

class BeaminSignUp:
    def __init__(self, driver):
        self.driver = driver
    
    def btnEnabledChk(self):
        while True:
            btnEnabled = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((MobileBy.ID, 'com.sampleapp:id/menu_textbutton'))).get_attribute('enabled')
            if btnEnabled == 'true':
                # 버튼 클릭
                WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((MobileBy.ID, 'com.sampleapp:id/menu_textbutton'))).click()
                break
    
    def textInput(self, text, order):
        if order == 0:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((MobileBy.ID, 'com.sampleapp:id/input_edittext'))).send_keys(text)
        else:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located((MobileBy.ID, 'com.sampleapp:id/input_edittext')))[order].send_keys(text)

    def beaminSignUp_into_app(self):
        # 마이페이지 아이콘 클릭
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((MobileBy.ID, 'com.sampleapp:id/myBaeminButton'))).click()
        # 로그인 여부 체크
        loginEl = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.FrameLayout[@resource-id="com.sampleapp:id/headerLayout"]/*/android.view.ViewGroup')))
        loginAtt = loginEl.get_attribute('resource-id')
        if loginAtt == 'com.sampleapp:id/drawer_login_user_info_layout':
            loginEl.click()
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((MobileBy.ID, 'com.sampleapp:id/logout_textview'))).click()
        # 로그인 메뉴 클릭
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((MobileBy.ID, 'com.sampleapp:id/drawer_menu_logout_login_iv'))).click()
        # 회원가입 메뉴 클릭
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((MobileBy.ID, 'com.sampleapp:id/sign_up_button'))).click()
        # 전체동의 체크박스 클릭
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((MobileBy.ID, 'com.sampleapp:id/agreeAllTermsCheckbox'))).click()
        # 다음으로 버튼 클릭
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((MobileBy.ID, 'com.sampleapp:id/termsNextButton'))).click()
        # 휴대전화 인풋박스에 번호 입력
        BeaminSignUp.textInput(self, '01071271318', 0)
        # 인증번호 받기 버튼 클릭
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((MobileBy.ID, 'com.sampleapp:id/authNumberGetButton'))).click()
        # 다음 버튼 활성화 여부 체크 후 클릭
        BeaminSignUp.btnEnabledChk(self)
        # 이메일주소 입력
        BeaminSignUp.textInput(self, 'test00001@naver.com', 0)
        # 중복확인 버튼 클릭
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((MobileBy.ID, 'com.sampleapp:id/emailIdCheckButton'))).click()
        # 키보드 숨기기
        self.driver.hide_keyboard()
        # 닉네임 입력
        BeaminSignUp.textInput(self, 'test00001', 1)
        # 비밀번호 입력
        BeaminSignUp.textInput(self, 'qwert13579', 2)
        # 생년월일 입력
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.FrameLayout[4]//android.widget.EditText'))).click()
        actions = ActionChains(self.driver).send_keys(19850223)
        actions.perform()
        # 숫자 키패드의 완료 버튼 클릭 (키입력명령 동작 하지 않아 좌표로 클릭함)
        TouchAction(self.driver).tap(None, 1240, 2160).perform()
        # 완료 버튼 활성화 여부 체크 후 클릭
        BeaminSignUp.btnEnabledChk(self)
        # 앱 종료
        # self.driver.close_app()

class ScrollSwipe(BeaminSignUp):
    def __init__(self, driver):
        BeaminSignUp.__init__(self, driver)

    def commonScroll(self, anchorX, startY, endY):
        self.driver.swipe(anchorX, startY, anchorX, endY, duration=2000)

    def elScroll(self, El):
        print("[SCROLL] Element Scroll Start")
        dim = El.size
        width, height = dim['width'], dim['height']
        AnchorX = width * 0.5
        StartY = (El.location['y'] + height) * 0.9
        EndY = (El.location['y'] + height) * 0.1
        ScrollSwipe.commonScroll(self, AnchorX, StartY, EndY)
        print(f"StartY : {StartY} / EndY : {EndY}")
        print("[SCROLL] Element Scroll End")

    def elPlusScroll(self, El, plusValue):
        print("[SCROLL] Element+ Scroll Start")
        dim = El.size
        width, height = dim['width'], dim['height']
        AnchorX = width * 0.5
        StartY = ((El.location['y'] + height) * 0.9) + plusValue
        EndY = ((El.location['y'] + height) * 0.1)
        ScrollSwipe.commonScroll(self, AnchorX, StartY, EndY)
        print(f"StartY : {StartY} / EndY : {EndY} / plusValue : {plusValue}")
        print("[SCROLL] Element+ Scroll End")

class setContext(BeaminSignUp):
    def __init__(self, driver):
        BeaminSignUp.__init__(self, driver)
        
    def switchContext(self, context):
        print('[CONTEXT] Device Context Switch Start')
        print('Now Driver Context : ' + self.driver.context)
        print('SET Context : ' + context)
        contexts = self.driver.contexts
        for c in contexts:
            if c in context:
                self.driver.switch_to.context(c)
                print('Success Switch Context')
                break
        print('[CONTEXT] Device Context Switch End')