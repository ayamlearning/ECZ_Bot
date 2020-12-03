import sys, os
sys.path.append('/var/www/webApp/webApp')

from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
import requests 
from flask import Flask,request,session
import psycopg2
import os
from datetime import datetime
import logging
import news_bl as news
import centres_bl as centres

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
logging.info(str(current_time))
constituencies=list(centres.list_constituencies())


@app.route("/")
def index():
    return "Mulenga Bot Home"


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
   
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    body=""
    inc_message=incoming_msg.lower()

    if inc_message=='hi':
        body="Hi! my name is Patrick. I will provide you with "
        body+="information relating to the on-going voter registration.\n"
        body+="Please reply with the following options to get started.  \n\n"
        body+="1. Latest News \n 2. Search for Voter Registration Centre"

    elif inc_message in ['1','2']:
        selOption=int(incoming_msg)
        output=menu_options(selOption)
        msg.body(output)
        responded = True

    elif inc_message in constituencies:
        body=centres.search_by_constituency(incoming_msg)

    else:
        body="Please reply with the following options to get started.  \n\n"
        body+="1. Latest News \n 2. Search for Voter Registration Centre"

    msg.body(body)

    return str(resp)
    
def menu_options(par): 
    switcher = { 
        1: news.get_all(),
        2: search_centre_by_const(),
    } 
    return switcher.get(par, False)     


def search_centre_by_const():
    return "Enter Constituency Name (e.g Chawama):"
    
if __name__ == '__main__':
    app.run(debug=True)

