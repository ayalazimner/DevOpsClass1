#Load Selenium Web Driver
from selenium import webdriver
driver = webdriver.Chrome(executable_path='D:\Python\chromedriver_win32\chromedriver.exe')

#Get website URL
parameters_file=open("D:\Python\SeleniumProject\params.txt",'r')
url=parameters_file.read()

#Open website
driver.get(url)

#Press registration/enter link
register_enter_button=driver.find_element_by_xpath("/html/body[@class='rtl desktop chrome ember-application INDlangdirRTL INDpositionRight INDDesktop INDChrome hover']/div[@id='ember572']/div[@class='main-container home-page-offset']/header[@class='m-page-header home-header']/div[@id='ember591']/div[@class='inner']/ul[@class='nav-bar buttons']/li[3]/a/span[@class='seperator-link']")
register_enter_button.click()

#Press registration link
register_button=driver.find_element_by_xpath("/html/body[@class='rtl desktop chrome ember-application INDlangdirRTL INDpositionRight INDDesktop INDChrome hover']/div[@id='ember572']/div[@class='main-container home-page-offset']/div[@class='ui-lightbox login']/div[@class='inner']/div[@class='box']/div[@class='lightbox-content']/p[@class='switch-text']/span[@class='text-btn']")
register_button.click()

#Find popup
# popup=driver.find_element_by_class_name("lightbox-content")
# popup=driver.find_element_by_class_name("main-form")
# popup=driver.find_element_by_class_name("option oldschool")
# popup=driver.find_element_by_id("ember1104")



#Enter name
import time
time.sleep(5)
a=popup=driver.find_element_by_id("ember1118")
a.click()
name_field=driver.find_element_by_xpath("/html/body[@class='rtl desktop chrome ember-application INDlangdirRTL INDpositionRight INDDesktop INDChrome hover']/div[@id='ember572']/div[@class='main-container home-page-offset']/div[@class='ui-lightbox login']/div[@class='inner']/div[@class='box']/div[@class='lightbox-content']/div[@class='main-form']/div[@class='option oldschool']/form[@id='ember1104']/div[@class='field'][1]/label[@id='ember1105']/input[@id='ember1106']")
#name_field.click()
name_field.send_keys("Ayala")