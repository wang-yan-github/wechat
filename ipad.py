from appium import webdriver

desired_caps = {
    'platformName': 'iOS',
    'platformVersion': '14.5',
    'deviceName': 'iPhone 11',
    'app': '/Users/wangyan/Desktop/微信.ipa',  # 确认路径正确
    'automationName': 'XCUITest'
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
