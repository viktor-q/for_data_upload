import requests

payload = {
    "_username": "tester1",
    "_password": "qwerty123"
}

login_url = 'https://www.eolymp.com/ru/login'

to_post_data_url = 'https://www.eolymp.com/ru/submissions/submit?problem=888'

# with requests.Session() as autorize_session:
#     p = autorize_session.post(login_url, data=payload)
#     cookies = p.cookies
#     print(cookies)

to_example_load = "submit%5Bproblem%5D=888&submit%5Bcompiler%5D=gpp&submit%5Bsource%5D=test2&submit%5B_token%5D=GQb-ZTnQTI_blYk3dAwsrEwZqfvrwjC-k5DHdw2K16w"



with requests.Session() as payload_session:
    p = payload_session.post(to_post_data_url, data=to_example_load)
    print(p.status_code)
