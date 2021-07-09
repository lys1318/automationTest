from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

saveEllist = []
timeout = 10
NAIVE = "NATIVE_APP"
WEVIEW = "WEBVIEW_com.wemakeprice"

class RecentlyViewed:
    def __init__(self, driver):
        self.driver = driver
    
    def saveList(elList):
        for i in elList:
            saveEllist.append(elList)
        return saveEllist
    
    def wonderFiScroll(self):
        wonderFi = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((MobileBy.ID, "com.wemakeprice:id/v_wonder_filter")))
        dim = wonderFi.size
        wonderFiHeight = dim['height']
        ScrollSwipe.elPlusScroll(self, wonderFi, wonderFiHeight)

    def recentlyViewed_into_app(self):     
        # 카테고리 메인 이동
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((MobileBy.ID, 'com.wemakeprice:id/category_button'))).click()

        # 첫번째 대분류 그룹 카테고리 클릭
        mainGroup = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((MobileBy.ID, 'com.wemakeprice:id/rv_category')))
        WebDriverWait(mainGroup, timeout).until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.RelativeLayout[1]'))).click()

        # 하위 카테고리 클릭
        subCgyList = WebDriverWait(mainGroup, timeout).until(EC.presence_of_all_elements_located((MobileBy.ID, 'com.wemakeprice:id/tv_sub_category')))
        subCgyList[1].click()
        # 카테고리 컨텐츠 영역 엘리먼트
        cgyCont = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((MobileBy.ID, 'com.wemakeprice:id/rc_lists1')))
		# 카테고리 컨텐츠 영역 하위 FrameLayout (상품영역)
        cgyContFrame = WebDriverWait(cgyCont, timeout).until(EC.presence_of_all_elements_located((MobileBy.XPATH, '//android.widget.FrameLayout')))
        
		# 기획전 영역 유무 체크
        bannerImgYn = self.driver.find_elements_by_id('com.wemakeprice:id/v_banner_image')
        # 판매자 추천 광고 영역 유무 체크
        ptAdYn = self.driver.find_elements_by_id('com.wemakeprice:id/ll_content_title')
		# 필터버튼 노출 유무 체크
        wonderFiYn = self.driver.find_elements_by_id('com.wemakeprice:id/v_wonder_filter')
		# 중분류 카테고리 영역 element
        subCgyArea = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((MobileBy.ID, 'com.wemakeprice:id/root_layout')))

        # 헤더 및 중분류 카테고리 영역 만큼 스크롤
        ScrollSwipe.elScroll(self, subCgyArea)

        # 기획전 배너 & 판매자 추천 광고 & 원더필터에 따른 스크롤
        if bannerImgYn:
            bannerHeight = bannerImgYn[0].size['height'] * (len(bannerImgYn)-1)
            ScrollSwipe.elPlusScroll(self, bannerImgYn[0], bannerHeight)
        if ptAdYn and not wonderFiYn: # 판매자 추천 광고 Y && 원더필터 N
            ScrollSwipe.elScroll(self, cgyContFrame[0])
            cgyCont = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((MobileBy.ID, 'com.wemakeprice:id/rc_lists1')))
            cgyContFrame = WebDriverWait(cgyCont, timeout).until(EC.presence_of_all_elements_located((MobileBy.XPATH, '//android.widget.FrameLayout')))

            for i, v in enumerate(cgyContFrame):
                HeightChk = cgyContFrame[i].size['height']
                if HeightChk > 900:
                    ScrollSwipe.elScroll(self, cgyContFrame[i])
                    break
            
            # 스와이핑배너 노출 유무 체크
            swapBnYn = self.driver.find_elements_by_id("com.wemakeprice:id/vp_swapping_banner")
            # 스와이핑배너에 따른 스크롤
            if swapBnYn:
                # 스와이핑배너 영역 만큼 스크롤
                ScrollSwipe.elScroll(self, swapBnYn[0])
                # 원더 필터 영역 만큼 스크롤
                RecentlyViewed.wonderFiScroll(self)
            else:
                RecentlyViewed.wonderFiScroll(self)
        elif ptAdYn and wonderFiYn: # 판매자 추천 광고 Y && 원더필터 Y
            ScrollSwipe.elScroll(self, cgyContFrame[0])
            swapBnYn = self.driver.find_elements_by_id("com.wemakeprice:id/vp_swapping_banner")
            if swapBnYn:
                ScrollSwipe.elScroll(self, swapBnYn[0])
                time.sleep(1)
                RecentlyViewed.wonderFiScroll(self)
            else:
                RecentlyViewed.wonderFiScroll(self)
        else:
            RecentlyViewed.wonderFiScroll(self)
        
        # 상품 누적 개수 체크를 위한 변수
        prodCnt = 0

        # 상품 리스트 → 상품 상세 이동 반복 루프
        while prodCnt <= 2:
            cgyContRe = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((MobileBy.ID, 'com.wemakeprice:id/rc_lists1')))
            cgyContFrameRe = WebDriverWait(cgyContRe, timeout).until(EC.presence_of_all_elements_located((MobileBy.XPATH, '//android.widget.FrameLayout')))
			
            for i, v in enumerate(cgyContFrameRe):
                # 상품 상세 진입
                cgyContFrameRe[i].click()

                setContext.switchContext(self, WEVIEW)
                WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((MobileBy.CSS_SELECTOR, '.btn_fix .btn_zzim'))).click()
                WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((MobileBy.CSS_SELECTOR, '.btn_history'))).click()
                setContext.switchContext(self, NAIVE)
                # 2초 쉬고 뒤로가기
                # time.sleep(2)
                # self.driver.press_keycode(4)
				
                if i == 1:
                    time.sleep(1)
                    ScrollSwipe.elPlusScroll(self, cgyContFrameRe[0], 50)
                    break
                time.sleep(1)
            prodCnt += 1
        # 앱 종료
        self.driver.close_app()

class ScrollSwipe(RecentlyViewed):
    def __init__(self, driver):
        RecentlyViewed.__init__(self, driver)

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

class setContext(RecentlyViewed):
    def __init__(self, driver):
        RecentlyViewed.__init__(self, driver)
        
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