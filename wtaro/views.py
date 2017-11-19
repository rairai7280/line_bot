from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.

def index(request):
    return HttpResponse("This is bot api.")

def callback(request):
    reply = ""
    request_json = json.loads(request.body.decode('utf-8'))
    for e in request_json['events']:
        reply_token = e['replyToken']
        message_type = e['message']['type']
        if message_type == "text":
            text = e['message']['text']
            reply += replyMessage(text)
    return HttpResponse(reply)

def replyMessage(text):
    # do something

    return text + text
