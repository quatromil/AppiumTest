from appium import webdriver


def before_scenario(context, scenario):
    context.driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities={
            'app': 'C:\\Instaladores\\PreciseUnitConversion.apk',
            'platformName': 'Android',
            'deviceName': 'TA90700J7R',
            'appPackage': 'com.ba.universalconverter',
            'appActivity': 'MainConverterActivity'
        }
    )
