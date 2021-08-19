from appium import webdriver as AppuimDriver
import aos_beaminSignUp

def test_beaminSignUp():
    Desired_Capabilites = {
        'deviceName' : 'SM-N965N',
        'platformVersion' : '10',
        'platformName' : 'Android',
        'udid' : '2121420a2c037ece',
        'automationName' : 'Appium',
        'appPackage' : 'com.sampleapp',
        'appActivity' : 'com.baemin.presentation.ui.RouterActivity',
        'systemPort' : 8200,
        'newCommandTimeout' : 3600,
        'noReset' : True,
        'chromedriverExecutable' : 'C:/python study/mobile_chromedriver.exe',
        'skipDeviceInitialization' : True,
        'skipServerInstallation' : True
    }
    driver = AppuimDriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=Desired_Capabilites)
    beaminSignUp = aos_beaminSignUp.BeaminSignUp(driver)
    beaminSignUp.beaminSignUp_into_app()

test_beaminSignUp()