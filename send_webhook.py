import requests
from datetime import datetime


def send_webhook(percent, time, doses):
    webhook_url = 'discord webhook url'
    current_time = datetime.now().strftime("%H:%M:%S")
    data = {"username": "Arnhths Covid", "embeds": [
        {
            'title': 'Βρέθηκε ραντεβού για εμβόλιο',
            'description': f'[Link](https://emvolio.gov.gr/app#/CovidVaccine/appointmentSearch)',
            'color': 1127128,
            'footer': {'text': f'Den uparxei o covid [{current_time}]', 'icon_url': 'https://www.zurich.com/es-es/products-and-services/-/media/project/zurich/dotcom/pictograms/covid-19.png'},
            'fields': [{"name": "Ποσοστό διαθεσημότητας", "value": percent, "inline": True}, {"name": "Ώρα", "value": time, "inline": True}, {"name": "Δόσεις", "value": doses, "inline": False}],
        }
    ]}

    res = requests.post(webhook_url, json=data)
    try:
        res.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e)
    else:
        print(f'Payload delivered successfully, code{res.status_code}')
