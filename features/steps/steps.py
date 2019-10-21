from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait

@given(u'I am on "{Language}"')
def step_impl(context,Language):
    context.driver.get("https://www.avast.com/" + Language + "/lp-business-aff-secureline-45")

@when(u'I confirm cookies')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div[4]/div/div/span/span').click()

@when(u'One year five PC license is selected')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div[1]').click()

@then(u'Price is displayed')
def step_impl(context):
    context.firstPrice=context.driver.find_element_by_xpath('//*[@id="top"]/div/div[1]/div[2]/div/div[2]/span[1]').text

@when(u'I click on checkout')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="top"]/div/div[1]/div[2]/div/div[3]/a').click()

@then(u'Wait for "{Target}" to load')
def step_impl(context, Target):
    element = WebDriverWait(context.driver, 10).until(
    lambda x: x.find_element_by_xpath(Target))
    context.secondPrice=context.driver.find_element_by_xpath(Target).text
    
@then(u'Compare both prices')
def step_imp(context):
    context.firstPrice=context.firstPrice.replace(" ","")
    context.secondPrice=context.secondPrice.replace(" ","")
    print(context.firstPrice, context.secondPrice)
    if(context.firstPrice!=context.secondPrice):
     assert False,"Prices do not match"
