import pytchat
from datetime import datetime
from time_util import to_time


# 실시간으로 채팅을 받아오면서 평균을 내서 평균 * weight 이상의 채팅 갯수인 구간을 구함
# end : 여기까지만 분석한다.
def log_chat_realtime(chat: pytchat, end: datetime = None, weight: float = 1.0):
    chat.get()  # 첫 데이터는 버림
    acc = len(chat.get().items)
    count = 1
    largest = acc
    while chat.is_alive():
        chatList = chat.get().items
        if not chatList:
            continue
        if end and to_time(chatList[0].elapsedTime) > end:
            break
        current_size = len(chatList)
        largest = max(largest, current_size)
        avg = acc // count
        if current_size > (avg * weight):
            print(chatList[0].elapsedTime, end='   ')
        acc += current_size
        count += 1


# 채팅 전체를 일단 받아오고, 한번에 평균을 내서 평균 * weight 이상의 채팅 갯수인 구간을 구함
# end : 여기까지만 분석한다.
def log_chat_buffered(chat: pytchat, end: datetime = None, weight: float = 1.0):
    chat_data = []
    chat.get()  # 첫 데이터는 버림
    while chat.is_alive():
        items = chat.get().items
        if not items:
            continue
        if end and to_time(items[0].elapsedTime) > end:
            break
        chat_data.append(items)

    avg = sum(map(lambda x: len(x), chat_data)) // len(chat_data)
    for chatList in filter(lambda x: len(x) >= avg * weight, chat_data):
        if not chatList:
            continue
        print(chatList[0].elapsedTime, end='   ')
