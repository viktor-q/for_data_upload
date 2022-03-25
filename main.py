from selenium import webdriver
from time import sleep
import os



#push_data
all_files = os.listdir('data_to_upload/e-olymp-master/0000-0999/')

for file in all_files:
    PATH = "/usr/lib/chromium-browser/chromedriver"
    browser = webdriver.Chrome(PATH)

    browser.get('https://www.eolymp.com/ru/submissions/submit')

    # login
    login = browser.find_element_by_id("username").send_keys("tester1")
    password = browser.find_element_by_id("password").send_keys("qwerty123")
    browser.find_element_by_xpath('/html/body/main/div[2]/form/div/div[2]/input').click()

    # wait
    # sleep(5)

    body_into_file = 'data_to_upload/e-olymp-master/0000-0999/' + file
    f = open(body_into_file,'r')
#    print(*f) #soderjimoe
    name_file = file.split()
    if name_file[0][0] == "P":
        name_file[0] = name_file[0][7:11]
  #  print(name_file[0])

#    print(name_file[0])



    body_example = browser.find_element_by_id("submit_source").send_keys(*f)
    print("body ok")
    number_example = browser.find_element_by_id("submit_problem").send_keys(name_file[0])
    print("number", name_file[0])
    sleep(5)

    browser.find_element_by_xpath('/html/body/main/div[2]/form/div/div[2]/input').click()
    print("click ok")
    sleep(5)
    browser.close()

