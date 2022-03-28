from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

from time import sleep
import os


# start browser
opts = Options()
browser = Chrome('/usr/local/bin/chromedriver')
browser.get('https://www.eolymp.com/ru/submissions/submit')

# login
login = browser.find_element_by_id("username").send_keys("tester1")
password = browser.find_element_by_id("password").send_keys("qwerty123")
browser.find_element_by_xpath('/html/body/main/div[2]/form/div/div[2]/input').click()

#directory with all files to upload
all_files = os.listdir('data_to_upload/e-olymp-master/0000-0999/')

for file in all_files:
    one_file_to_upload = 'data_to_upload/e-olymp-master/0000-0999/' + file
    f = open(one_file_to_upload, 'r',  encoding="utf-8")

    name_file = file.split()

    if name_file[0][0] == "P":
        name_file[0] = name_file[0][7:11]

    sleep(2)

    body_example = browser.find_element_by_id("submit_source").send_keys(*f)
    print("body ok")

    sleep(2)

    number_example = browser.find_element_by_id("submit_problem").send_keys(name_file[0])

    sleep(2)

    f.close()

    browser.find_element_by_name('submit').submit()
    print("click ok")

    sleep(2)

  #  browser.close()
    browser.get('https://www.eolymp.com/ru/submissions/submit')

