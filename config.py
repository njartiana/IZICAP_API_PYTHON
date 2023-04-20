from json import dumps
from utils.data_manager import Data
BaseUrl = "http://localhost:8080/"

body_empty = dumps({
        'username': '',
        'password': ''
    })
body_username_empty = dumps({
        'username': '',
        'password': 'admin'
    })
body_password_empty = dumps({
        'username': 'admin',
        'password': ''
    })
body_wrong_credential = dumps({
    'username': 'administrator',
    'password': 'administrator'
})
body_admin = dumps({
        'username': 'admin',
        'password': 'admin'
    })
headers = {
        'Content-type': 'application/json'
    }

base_data = [(BaseUrl+"/tokens", body_empty, headers, 401),(BaseUrl+"/tokens", body_username_empty, headers, 401)
    ,(BaseUrl+"/tokens", body_password_empty, headers, 401),(BaseUrl+"/tokens", body_wrong_credential, headers, 401)]

myData = Data()
username = myData.generate_string_value(9)
password = myData.generate_alphanumeric_value(9)

