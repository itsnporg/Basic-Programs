import requests 
import random 
from bs4 import BeautifulSoup

def conversion(date , type): 
    convert = ['eng_to_nep', 'nep_to_eng']
    if type.lower() =='ad':
        option = convert[0]
    else : 
        option = convert[1]
        
    body = f"actionName=wdconverter&datefield={date}&convert_option={option}&state={random.random()}"    

    attributes ={
    "headers": {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9,ne;q=0.8",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "sec-ch-ua": "\"Google Chrome\";v=\"105\", \"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"105\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sec-gpc": "1",
        "x-requested-with": "XMLHttpRequest"
    },
    "referrer": "https://www.hamropatro.com/widgets/dateconverter.php",
    "referrerPolicy": "strict-origin-when-cross-origin",
    "body": body,
    "method": "POST",
    "mode": "cors",
    "credentials": "include"
    }

    url = "https://www.hamropatro.com/getMethod.php"

    r= requests.request(method = attributes["method"], url=url, headers=attributes["headers"], data=attributes["body"])

    text = r.text.split(" | ")

    text[1]= BeautifulSoup(text[1], 'html.parser').text

    return text 

print(conversion("2003-1-17","AD"))


