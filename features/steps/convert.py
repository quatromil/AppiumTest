from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
from behave import *
from selenium.webdriver.support.ui import WebDriverWait


@given("I start the App")
def open_app(context):
    print(context.driver)


@when('I open the Menu')
def open_menu(context):
    menuBtn = WebDriverWait(context.driver, 30).until(
        EC.element_to_be_clickable((MobileBy.XPATH, "//android.widget.ImageButton[@content-desc='Abrir el cajon de navegacion']"))
    )
    menuBtn.click()


@when('I press keys for the value')
def perform_keys(context):
    firstBtn = WebDriverWait(context.driver, 30).until(
        EC.element_to_be_clickable((MobileBy.XPATH, "//*[@resource-id='com.ba.universalconverter:id/buttons_row_1']/android.widget.Button[1]"))
    )
    firstBtn.click()

    secondBtn = WebDriverWait(context.driver, 30).until(
        EC.element_to_be_clickable((MobileBy.XPATH, "//*[@resource-id='com.ba.universalconverter:id/buttons_row_2']/android.widget.Button[2]"))
    )
    secondBtn.click()


@when('I go to Area option')
def go_area(context):
    areaBtn = WebDriverWait(context.driver, 30).until(
        EC.element_to_be_clickable((MobileBy.XPATH, "(//android.widget.ImageView[@content-desc='Categoría icono'])[5]"))
    )
    areaBtn.click()


@when('I go to Volume option')
def go_volume(context):
    volumeBtn = WebDriverWait(context.driver, 30).until(
        EC.element_to_be_clickable((MobileBy.XPATH, "(//android.widget.ImageView[@content-desc='Categoría icono'])[6]"))
    )
    volumeBtn.click()


@when('I perform Dropdown')
def drop_down(context):
    i = 1
    while i <= 3:
        action = TouchAction(context.driver)
        action.press(x=200, y=700).move_to(x=200, y=50).release().perform()
        i = i + 1


@then('I see result')
def see_result(context):
    print(context.driver)


@when('I go to Velocity option')
def go_velocity(context):
    velocityBtn = WebDriverWait(context.driver, 30).until(
        EC.element_to_be_clickable((MobileBy.XPATH, "(//android.widget.ImageView[@content-desc='Categoría icono'])[4]"))
    )
    velocityBtn.click()


@when('I go to Aceleration option')
def go_aceleration(context):
    acelerationBtn = WebDriverWait(context.driver, 30).until(
        EC.element_to_be_clickable((MobileBy.XPATH, "(//android.widget.ImageView[@content-desc='Categoría icono'])[5]"))
    )
    acelerationBtn.click()


@when('I go to Angular Velocity option')
def go_angular(context):
    angularBtn = WebDriverWait(context.driver, 30).until(
        EC.element_to_be_clickable((MobileBy.XPATH, "(//android.widget.ImageView[@content-desc='Categoría icono'])[6]"))
    )
    angularBtn.click()


@when('I go to Fluid Velocity option')
def go_fluid(context):
    fluidBtn = WebDriverWait(context.driver, 30).until(
        EC.element_to_be_clickable((MobileBy.XPATH, "(//android.widget.ImageView[@content-desc='Categoría icono'])[7]"))
    )
    fluidBtn.click()
