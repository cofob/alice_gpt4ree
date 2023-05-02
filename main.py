import asyncio
import traceback
from typing import Union
from fastapi import FastAPI, Request

import datetime

from gpt4free import you
from threading import Thread
from time import sleep

app = FastAPI()

answer = None
pending_request = None

def req_thread():
    global pending_request
    while True:
        sleep(0.1)
        if pending_request is not None:
            try:
                pending_request()
            except Exception as e:
                print(f"exception in loop: {e}")
            pending_request = None

t = Thread(target=req_thread)
t.start()

CUT_WORD = ['Алиса', 'алиса']

users_state = dict()

def request_gpt(text: str):
    global pending_request
    def func():
        global answer
        r = you.Completion.create(prompt=text)
        answer = r.request
    pending_request = func

@app.post("/post")
async def post(request: Request):
    request = await request.json()
    response = {
        'session': request['session'],
        'version': request['version'],
        'response': {
            'end_session': False
        }
    }
    ## Заполняем необходимую информацию
    await handle_dialog(response, request)
    print(response)
    return response

async def handle_dialog(res,req):
    global answer

    print('start handle:', datetime.datetime.now(tz=None))
    print(req)

    if req['request']['original_utterance']:
        # Проверяем, есть ли содержимое
        request = req['request']['original_utterance']
        for word in CUT_WORD:
            if request.startswith(word):
                request = request[len(word):]
        request = request.strip()


        if answer is None:
            task = request_gpt(request)
            if answer is None:
                print('no response')
                reply = 'Не успел получить ответ. Спросите позже.'
            else:
                print(f"response: {answer}")
                reply = answer
                answer = None
        else:
            if answer is None:
                print('no response')
                reply = 'Ответа ещё нет.'
            else:
                print(f"response: {answer}")
                reply = answer
                answer = None
    else:
        reply = 'Спроси что-нибудь'

    res['response']['text'] = reply
