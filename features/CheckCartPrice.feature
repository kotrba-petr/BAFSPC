Feature: Price matches the price in the cart
Scenario Outline: Check if the price for product 5PC 1Y on the "<Language>" website is the same as in the cart
  Given I am on "<Language>"
  When I confirm cookies
  And One year five PC license is selected
  Then Price is displayed
  When I click on checkout
  Then Wait for "<Target>" to load
  And Compare both prices
Examples: Languages and Targets
    |Language|Target|
    |en-us|//*[@id="ShoppingCartForm"]/div[1]/div[2]/div[1]|
    |ru-ru|//*[@id="ShoppingCartForm"]/div[1]/div[2]/div[1]|
    |pt-br|/html/body/div[1]/div[1]/div/div/div[3]/div[1]/div/form/table/tbody/tr[1]/td[3]/div/span[1]|
