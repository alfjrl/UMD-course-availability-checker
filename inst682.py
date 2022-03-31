from html.parser import HTMLParser
from traceback import print_tb
import requests
from bs4 import BeautifulSoup

def post_data(message, token):
    try:
        url = "https://notify-api.line.me/api/notify"
        headers = {
            'Authorization': f'Bearer {token}'
        }
        payload = {
            'message': message
        }
        response = requests.request(
            "POST",
            url,
            headers=headers,
            data=payload
        )
        if response.status_code == 200:
            print(f"Success -> {response.text}")
    except Exception as _:
        print(_)

response = requests.get("https://app.testudo.umd.edu/soc/search?courseId=INST682&sectionId=&termId=202208&_openSectionsOnly=on&creditCompare=%3E%3D&credits=0.0&courseLevelFilter=GRAD&instructor=&_facetoface=on&_blended=on&_online=on&courseStartCompare=&courseStartHour=&courseStartMin=&courseStartAM=&courseEndHour=&courseEndMin=&courseEndAM=&teachingCenter=ALL&_classDay1=on&_classDay2=on&_classDay3=on&_classDay4=on&_classDay5=on")

soup = BeautifulSoup(response.text, 'html.parser')
result = soup.find("span", class_='open-seats-count')
result_text = result.get_text()
print(result_text)

checkPoint = int(result_text)

if 1 > 0:
    token = "h3V6o4fQUxqOOzj11AJXOm508hFHrb9EVbqZH52Y2JZ" # 您的 Token
    message = "INST682 有空位了"     # 要發送的訊息
    post_data(message, token)



