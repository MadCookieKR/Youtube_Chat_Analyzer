import pytchat
from graph_painter import graph_painter


if __name__ == '__main__':
    video_id: str = input("유투브 비디오 아이디를 입력해주세요. ")
    chat = pytchat.create(video_id=video_id)
    #graph_logger.log_chat_realtime(chat, weight=1.2)
    graph_painter(chat).draw_chat_graph()


