from appium import webdriver as AppuimDriver
import aos_recentlyViewed

def test_recentlyViewed():
    Desired_Capabilites = {
        'deviceName' : 'SM-N965N',
        'platformVersion' : '10',
        'platformName' : 'Android',
        'udid' : '2121420a2c037ece',
        'automationName' : 'Appium',
        'appPackage' : 'com.wemakeprice',
        'appActivity' : 'com.wemakeprice.intro.Act_Intro',
        'systemPort' : 8200,
        'newCommandTimeout' : 3600,
        'noReset' : True,
        'chromedriverExecutable' : 'C:/python study/mobile_chromedriver.exe',
        'skipDeviceInitialization' : True,
        'skipServerInstallation' : True
    }
    driver = AppuimDriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=Desired_Capabilites)
    recentlyViewed = aos_recentlyViewed.RecentlyViewed(driver)
    recentlyViewed.recentlyViewed_into_app()

test_recentlyViewed()