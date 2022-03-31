import requests
from bs4 import BeautifulSoup

# send notification to Line Notify
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

# variables
courseNo = "INST682" # course number
termID = 202208 # semester / term 
token = "h3V6o4fQUxqOOzj11AJXOm508hFHrb9EVbqZH52Y2JZ" # replace with your Line Notify token
message = f"{courseNo} 有空位了"     # message shows in Line Notify

# get number of available seat
url = f"https://app.testudo.umd.edu/soc/search?courseId={courseNo}&sectionId=&termId={termID}&_openSectionsOnly=on&creditCompare=%3E%3D&credits=0.0&courseLevelFilter=GRAD&instructor=&_facetoface=on&_blended=on&_online=on&courseStartCompare=&courseStartHour=&courseStartMin=&courseStartAM=&courseEndHour=&courseEndMin=&courseEndAM=&teachingCenter=ALL&_classDay1=on&_classDay2=on&_classDay3=on&_classDay4=on&_classDay5=on"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
result = soup.find("span", class_='open-seats-count')
result_text = result.get_text()
print("Current available seat: ",result_text)

# check whether available seat exsits or not, and send Line notification accordingly
checkPoint = int(result_text)

if checkPoint > 0:
    post_data(message, token)



