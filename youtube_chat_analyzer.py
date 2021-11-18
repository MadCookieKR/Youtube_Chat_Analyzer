import pytchat
from graph_painter import graph_painter


def analyze():
    video_id: str = input("please type youtube video id.\n유투브 비디오 아이디를 입력해주세요.\n")
    keywords = list(input(
        "Type keywords that you want to match. Separate each keyword into spaces. It doesn't matter whether it's lowercase or uppercase.\nex) lol yabe lmao\n* Type enter to keep the default setting(lmao lol lewd yabe)\n" +
        "매칭시킬 키워드를 입력해주세요. 각 키워드를 띄어쓰기로 구분해서 입력해주세요. 대소문자는 구분하지 않습니다.\n예) lol yabe lmao\n* 기본 설정(lmao lol lewd yabe) 유지하려면 엔터를 치세요.\n").split())
    try:
        chat = pytchat.create(video_id=video_id)
    except:
        print('Invalid video id. please try again.\n유효하지 않은 비디오 아이디입니다. 다시 시도해주세요.\n')
        analyze()
        return
    graph_painter(chat, keywords).draw_chat_graph()


if __name__ == '__main__':
    analyze()
