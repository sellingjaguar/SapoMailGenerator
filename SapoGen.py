from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random


def random_string() :
       random_string = ''

       for _ in range(random.randint(10, 14)) :
              type = random.randint(1, 3)
              if type == 1 :
                     random_integer = random.randint(65, 90)
              elif type == 2 :
                     random_integer = random.randint(97, 122)
              elif type == 3 :
                     random_integer = random.randint(48, 57)

              random_string += (chr(random_integer))

       return random_string


def generate_acc() :

       firefox_profile = webdriver.FirefoxProfile()
       firefox_profile.set_preference("browser.privatebrowsing.autostart", True)

       driver = webdriver.Firefox(firefox_profile=firefox_profile)

       driver.get('https://mail.sapo.pt/registo/')
       driver.set_window_size(500, 500)

       try :
              # acc data
              name = "Jonas Alberto"
              mail = random_string()
              password = "LOLxd1234"

              WebDriverWait(driver, 10).until(
                     EC.presence_of_element_located((By.CSS_SELECTOR, "button.sc-ifAKCX:nth-child(2)"))).click()

              # fill data
              driver.find_element_by_id("name").send_keys(name)
              driver.find_element_by_id("email").send_keys(mail)
              driver.find_element_by_id("password").send_keys(password)
              driver.find_element_by_id("passwordConfirm").send_keys(password)

              gender = random.randint(1, 2)
              if gender == 1 :
                     driver.find_element_by_xpath("//*[@id='registo']/fieldset[1]/div[6]/label[2]/input").click()
              else :
                     driver.find_element_by_xpath("//*[@id='registo']/fieldset[1]/div[6]/label[3]/input").click()

              Select(driver.find_element_by_name("day")).select_by_value(str(random.randint(1, 28)))
              Select(driver.find_element_by_name("month")).select_by_value(str(random.randint(1, 12)))
              Select(driver.find_element_by_name("year")).select_by_value(str(random.randint(1960, 2001)))

              driver.find_element_by_id("terms").click()

              code = input("Captcha: ")

              if code == "0" :
                     print("Image load failed")
                     raise Exception
              else:
                     driver.find_element_by_name("captcha").send_keys(code)


              driver.find_element_by_name("createEmail").click()

              driver.switch_to.alert.accept()

              WebDriverWait(driver, 3).until(EC.url_to_be("https://mail.sapo.pt/registo/dadosRegisto.php"))

              print("Account created")
              email = mail + "@sapo.pt"

              file = open("accountlist.txt", "a")

              file.write(email + ":" + password + "\n")

              file.close()

       except :
              print("Page load failed")
       driver.close()


while (1) :
       try :
              generate_acc()
       except :
              continue
