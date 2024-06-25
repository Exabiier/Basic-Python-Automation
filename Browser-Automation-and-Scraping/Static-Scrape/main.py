from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

# def get_driver():
#     # Setup for my Webscraper
#     driver_path = './ChromeDriver/chromedriver'
#     service = Service(driver_path)

#     # The options for the Driver object:
#     options = webdriver.ChromeOptions()
#     options.add_argument("disable-infobars")
#     options.add_argument("start-maximized")
#     options.add_argument("disable-dev-shm-usage")
#     options.add_argument("no-sandbox")
#     options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     options.add_argument("disable-blink-features=AutomationControlled")


#     # The Driver object
#     driver = webdriver.Chrome(service=service, options=options)

#     driver.get("http://automated.pythonanywhere.com")
#     return driver

# def main():
#     driver = get_driver()
#     element = driver.find_element_by_xpath("/html/body/div[1]/div/h1[1]")
#     return element
    
# print(main())

def get_driver():
    # Setup for my Webscraper
    driver_path = './ChromeDriver/chromedriver'
    service = Service(driver_path)

    # The options for the Driver object:
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_argument("disable-blink-features=AutomationControlled")

    # The Driver object
    driver = webdriver.Chrome(service=service, options=options)

    return driver

def main():
    driver = get_driver()
    driver.get("http://automated.pythonanywhere.com")
    
    # Example: Find an element and return its text
    try:
        element = driver.find_element(by="xpath", value="/html/body/div[1]/div/p")
        print("Element found:", element.text)
    except Exception as e:
        print("Error finding element:", e)
    
    driver.quit()

if __name__ == "__main__":
    main()

