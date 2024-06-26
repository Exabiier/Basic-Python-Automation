from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime as dt

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

def clean_text(text):
    # it will only extract tempature:
    output = text.split(":")
    return float(output[1])

# This funtion will make .text file for each data we retrive from the website. 
def write_function(text):
    filename = f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
    with open(filename, 'w') as file:
        file.write(text)


def main():
    driver = get_driver()
    driver.get("http://automated.pythonanywhere.com/login/")
    
    # Example: Putting in value inputs to for username and password:
    driver.find_element(by="id", value="id_username").send_keys("automated")
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()

    # scrape portion for number:
    time.sleep(3)
    try:
        element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
        element2 = clean_text(element.text)
        print("Element found:", element2)
    except Exception as e:
        print("Error finding element:", e)
    driver.quit()


    

    
    

if __name__ == "__main__":
    main()

