import re
from datetime import datetime
import requests

def handle(req):
    if re.search(r'\bname\b', req, re.IGNORECASE):
        return "My name is Chatbot.\nYou can call me Chatbot.\nI'm known as Chatbot."

    elif re.search(r'current (date|time)', req, re.IGNORECASE):
        now = datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S") + "\n" + now.strftime("%d/%m/%Y %I:%M %p") + "\n" + now.strftime("%A, %B %d, %Y %I:%M:%S %p")

    elif re.search(r'generate a figlet for', req, re.IGNORECASE):
        text_to_figlet = re.sub(r'generate a figlet for', '', req, flags=re.IGNORECASE).strip()
        response = requests.post("http://127.0.0.1:8080/function/figlet", data=text_to_figlet)
        if response.ok:
            return response.text
        else:
            return "There was an error generating the figlet."

    else:
        return "I am not sure how to respond to that."

