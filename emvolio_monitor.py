import requests
from datetime import date
import json
from send_webhook import send_webhook
from time import sleep


def read_data(doses):
    url = 'https://emvolio.gov.gr/app/api/CovidService/CV_TimeSlots_Free'
    login_token = 'ctaf2 login_token'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
    headers = {'User-Agent': user_agent, 'authorization': login_token}

    today = date.today()
    fDate = today.strftime('%Y-%m-%d')
    data = {'centerId': 6006, 'dose': 1, 'firstDoseDate': None, 'personId': 12072870, 'requestRecommended': False, 'selectedDate': f'{fDate}T21:00:00.000Z', 'zoneNum': None}

    res = requests.post(url, headers=headers, data=data)
    return res


def format_data(res):
    timeSlots = res['timeslotsFree']

    flag = False
    for timeSlot in timeSlots:
        if not timeSlot['percentAvailable'] == 0.0:
            flag = True
            print('Check discord')
            time = timeSlot['onDate']
            percent = timeSlot['percentAvailable']
            doses = res['doses']
            send_webhook(percent, time, doses)

    if not flag:
        print(res['errorMessage'][0])


def main(doses):
    while True:
        print('Starting...')
        res = read_data(doses)
        format_data(res.json())
        sleep(600)


if __name__ == '__main__':
    main(1)
