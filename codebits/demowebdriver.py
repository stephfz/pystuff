# http://stackoverflow.com/questions/8255929/running-webdriver-chrome-with-selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get(""{{ your url}}"")


driver.find_element_by_id("{{ element_id }}").send_keys("{ somevalue }""})
driver.find_element_by_xpath("//button[contains(.,'Search')]").click(); #xpath example
#driver.close()
