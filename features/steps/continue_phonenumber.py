# import time
# from behave import *
# from selenium import webdriver
# #
# @given('user able to lunch the browser')
# def step_impl(context):
#     path = r"C:\Users\priya\Downloads\chromedriver_win32\chromedriver.exe"
#     context.driver = webdriver.Chrome(executable_path=path)
#
#     url = "https://in.bookmyshow.com/explore/home/bengaluru"
#     context.driver.get(url)
#
# @then('user able to click on signin button')
# def step_impl(context):
#     context.driver.find_element("xpath", "//div[text()='Sign in']").click()
#     time.sleep(3)
#
# @then('user enter the valid phone number "{phone_number}"')
# def step_impl(context,phone_number):
#     assert  len(phone_number) == 10 , "enter the valid 10 digts phone number "
#     context.driver.find_element('id','mobileNo').send_keys(phone_number)
#     time.sleep(1)
#
# @then('user able to click on continue button')
# def step_impl(context):
#     context.driver.find_element('xpath',"//button[text()='Continue']/..").click()
#     time.sleep(3)
#
#
