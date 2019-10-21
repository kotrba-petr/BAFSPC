from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
def before_scenario(context, scenario):
    context.driver=webdriver.Chrome('../drivers/chromedriver.exe')
    #context.driver=webdriver.Firefox(../drivers/geckodriver.exe')
    #context.driver=webdriver.Edge(../drivers/msedgedriver.exe')
def after_scenario(context, scenario):
    time.sleep(2)
    context.driver.quit()
