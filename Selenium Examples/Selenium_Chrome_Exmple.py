from selenium.webdriver.common.keys import Keys
from selenium import webdriver


def ChromeDriverSetup():
    # ================================================================================================================

    # chrome_options = Options()
    # chrome_options.add_extension('D:\\PycharmProjects\\All Python Examples\\Browsec-VPN.crx')  # ADD EXTENSION Browsec-VPN  IF YOUR ChromeDriver Supports else you get Error
    # browser = webdriver.Chrome(executable_path=str(Chromedriver), chrome_options=chrome_options)

    # =================================================================================================================

    browser = webdriver.Chrome(
        executable_path='D:\\PycharmProjects\\All Python Examples\\chromedriver.exe')  # Give The Path Of Your Downloaded ChromeDriver To execute Chrome
    browser.maximize_window()  # Auto Maximize Chrome Window Using This Command
    browser.get('https://www.google.com/')  # Run Url
    for Search_text in browser.find_elements_by_xpath('//*[@class="gLFyf gsfi"]'):  # xpath Of the google Search engine
        Search_text.send_keys('python')
        Search_text.send_keys(Keys.ENTER)  # Hit The Enter using Selenium Keys
    try:
        alert = browser.switch_to_alert()  # Close Alert Popup iF it came OR if not then you get exception That's why use always (TRY EXCEPT)
        alert.dismiss()
    except:
        pass  # pass keyword is used to execute nothing; it means, when we don't want to execute code, the pass can be used to execute empty


ChromeDriverSetup()
