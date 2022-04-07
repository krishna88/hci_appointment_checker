
import requests
from bs4 import BeautifulSoup
import os
import telegram
import time
from datetime import datetime

# update the telegram bot token below - https://www.siteguarding.com/en/how-to-get-telegram-bot-api-token
bot=telegram.Bot(token='XXXXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXXX')

def get_calendar_data(id, qp):
    url = "https://www.hcilondon.gov.in/appointment.php?" + qp

    payload = id
    
    headers = {
    'Origin': 'https://www.hcilondon.gov.in',
    'Cookie': 'PHPSESSID=0k7vkvno53m5ausmbogdg5mie2'
    }

    try:
        response = requests.request("POST", url, headers=headers, data = payload)
        soup = BeautifulSoup(response.content, 'html.parser')
        dat = soup.find_all("ul", {"class":"dates"})
        return(str(dat))
    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else",err)
        return("ERROR")

    

while True:
    goswell = {'serviceid': '10', 'locationid': '3'}
    goswell_appointments_mar = get_calendar_data(goswell, "month=03&year=2021")
    goswell_appointments_apr = get_calendar_data(goswell, "month=04&year=2021")

    hounslow = {'serviceid': '10', 'locationid': '4'}
    hounslow_appointments_mar = get_calendar_data(hounslow, "month=03&year=2021")
    hounslow_appointments_apr = get_calendar_data(hounslow, "month=04&year=2021")

    if not (os.path.exists('goswell_appointments_mar.txt')):
        with open("goswell_appointments_mar.txt", "w") as f:
            f.write(goswell_appointments_mar)
    if not (os.path.exists('goswell_appointments_apr.txt')):
        with open("goswell_appointments_apr.txt", "w") as f:
            f.write(goswell_appointments_apr)
    if not (os.path.exists('hounslow_appointments_mar.txt')):
        with open("hounslow_appointments_mar.txt", "w") as f:
            f.write(hounslow_appointments_mar)
    if not (os.path.exists('hounslow_appointments_apr.txt')):
        with open("hounslow_appointments_apr.txt", "w") as f:
            f.write(hounslow_appointments_apr)

    with open("goswell_appointments_mar.txt", "r") as f:
        goswell_appointments_base_mar = f.read()
    with open("goswell_appointments_apr.txt", "r") as f:
        goswell_appointments_base_apr = f.read()

    with open("hounslow_appointments_mar.txt", "r") as f:
        hounslow_appointments_base_mar = f.read()
    with open("hounslow_appointments_apr.txt", "r") as f:
        hounslow_appointments_base_apr = f.read()

    if(goswell_appointments_base_mar != goswell_appointments_mar) and (goswell_appointments_mar != "ERROR"):
        print("Appointment Available in Goswell")
        with open("goswell_appointments_mar.txt", "w") as f:
            f.write(goswell_appointments_mar)
        bot.send_message(chat_id='-582140884',text="Appointment Available in Goswell - March")
   
    if(goswell_appointments_base_apr != goswell_appointments_apr) and (goswell_appointments_apr != "ERROR"):
        print("Appointment Available in Goswell")
        with open("goswell_appointments_apr.txt", "w") as f:
            f.write(goswell_appointments_apr)
        bot.send_message(chat_id='-582140884',text="Appointment Available in Goswell - April")

    if(hounslow_appointments_base_mar != hounslow_appointments_mar) and (hounslow_appointments_mar != "ERROR"):
        print("Appointment Available in Goswell")
        with open("hounslow_appointments_mar.txt", "w") as f:
            f.write(hounslow_appointments_mar)
        bot.send_message(chat_id='-582140884',text="Appointment Available in Hounslow - March")

    if(hounslow_appointments_base_apr != hounslow_appointments_apr) and (hounslow_appointments_apr != "ERROR"):
        print("Appointment Available in Goswell")
        with open("hounslow_appointments_apr.txt", "w") as f:
            f.write(hounslow_appointments_apr)
        bot.send_message(chat_id='-582140884',text="Appointment Available in Hounslow - April")

    print("Successful appointment check at : " + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
    time.sleep(900)