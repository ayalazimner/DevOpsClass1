from selenium import webdriver
#driver is a variable name whch holds the session of the url
driver = webdriver.Chrome(executable_path='D:\Python\chromedriver_win32\chromedriver.exe')
#maximum default time to wait for elements to load:
driver.implicitly_wait(10)
driver.get("https://translate.google.com/")
#current url will show the current url
print("current URL: ", driver.current_url)
#title returns the tab title as shown in chrome
print("title: ",driver.title)
if driver.title=="Google Translate":
    print("tab is correct")
else:
    print("incorrect tab")

#get the page source
print("---SOURCE---\n",driver.page_source)
print("---END SOURCE---")


#LOCATORS: finding elements in the html page
#Locator type ID: unique name of the element
my_list=driver.find_elements_by_id("source")
print("ID element list:\n",my_list[0])

#XPath - this is a custom locator, we will use it when we have no data on the element, we only a specified element with which we can't locate.
#xpath=//tagname[@attribute='value'], example:
my_element=driver.find_element_by_xpath("/html/body[@class='displaying-homepage']/div[@class='frame']/div[@class='page tlid-homepage homepage translate-text']/div[@class='homepage-content-wrap']/div[@class='tlid-source-target main-header']/div[@class='source-target-row']/div[@class='tlid-input input']/div[@class='source-wrap']/div[@class='input-full-height-wrapper tlid-input-full-height-wrapper']/div[@class='source-input']/div[@id='input-wrap']/textarea[@id='source']")
print("xpath element:\n",my_element)

#CONTROLLERS
button_element=driver.find_element_by_id("source")
button_element.send_keys("hello")
import time
time.sleep(5)
button_element.clear()
print("button displayed: ",button_element.is_displayed())

my_element_language=driver.find_element_by_xpath("/html/body[@class='displaying-homepage with-lang-list']/div[@class='frame']/div[@class='page tlid-homepage homepage translate-text']/div[@class='homepage-content-wrap']/div[@class='tlid-source-target main-header']/div[@class='source-target-row']/div[@class='tlid-input input']/div[@class='tlid-language-bar ls-wrap']/div[@class='sl-wrap']/div[@class='sl-more tlid-open-source-language-list']")
my_element_language.click()

my_element_language=driver.find_element_by_xpath("/html/body[@class='displaying-homepage with-lang-list']/div[@class='frame']/div[@class='page tlid-language-picker-page language-picker-page']/div[@class='language-picker-wrapper']/div[@class='outer-wrap']/div[@class='language-list'][1]/div[@class='language_list_languages language_list_sl_list tw-ll-top'][1]/div[@class='language-list-unfiltered-langs-sl_list']/div[@class='language_list_section'][2]/div[@class='language_list_item_wrapper language_list_item_wrapper-hu']/div[@class='language_list_item language_list_item_language_name']")
my_element_language.click()



#driver quit closes all tabs related to the session
#driver.quit()


