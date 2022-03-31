import requests
import os
from time import sleep


# authorise and get the token
credentials = {
    "_username": "tester1",
    "_password": "qwerty123"
}

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36'}

login_url = "https://www.eolymp.com/ru/login-check"
submit_page = "https://www.eolymp.com/ru/submissions/submit"

session = requests.session()
session.headers = headers

session.post(login_url, data=credentials)
resp = session.get(submit_page)
html = resp.text
token = html.split('name="submit[_token]" value="')[1].split('"')[0]

# make upload data from files
all_files = os.listdir('data_to_upload/e-olymp-master/0000-0999/')
for file in all_files:
    one_file_to_upload = 'data_to_upload/e-olymp-master/0000-0999/' + file
    data_in_file = open(one_file_to_upload, 'r',  encoding="utf-8").read()

    name_file = file.split()

    if name_file[0][0] == "P":
        name_file[0] = name_file[0][7:11]

# post data to website
    payload = {
        "submit[problem]": name_file[0],
        "submit[compiler]": "gpp",
        "submit[source]": data_in_file,
        "submit[_token]": token
    }

    resp = session.post(submit_page, data=payload)
    if resp.status_code == 200:
        print(name_file[0], "is OK")
    elif resp.status_code != 200:
        print(name_file[0], "is BAD")

   # sleep(1)

   