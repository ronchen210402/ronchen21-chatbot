from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

from time import sleep

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('XXX')
# Channel Secret
handler = WebhookHandler('OOO')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    textin = event.message.text

    if '自我介紹' in textin:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='在大學時期，我有很多機會可以開發遊戲、網頁，同時也利用閒暇時間，學習網路管理與系統管理。我很喜歡探索新的知識，所以我在大四時上了機器學習的課，也加入量子電路的研討會。我相信我額外學習的這些技能，可以在未來某個時候利用到，也讓我這個人更有價值。\
                                                                        \n\n除了喜歡探索新知識，我認為我最大的優點是我對學習的熱衷。就像上述所說，為了增進我的技能，我努力鑽研各項知識，而就因為我對學習的執著，我發現我的學習速度變得很快，而我覺得我善於學習的能力，可以讓我很快的適應萬變的科技業。\
                                                                        \n\n在團隊合作方面，我善於觀察他人的狀況，聆聽他人意見，向別人學習。我同時也擅長表達我的想法，善於做出對當下最好的決定。當團隊氣氛不佳時，我會用我的幽默帶起氣氛；當團隊一籌莫展時，我也可以用我豐富的想像與創造力，尋找突破口。這些優點讓我在團隊合作的方面佔據優勢。\
                                                                        \n\n但是，綜觀我的學習歷程，我發現我缺乏對於工作上的經驗。我並不想只成為一個會讀書的人，我更希望我可以用我的知識步入產業。所以我想要申請一個實習，我相信依我快速學習、應變的能力，我可以完成許多不同的挑戰。'))
    elif '專案' in textin:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='加密貨幣 ML 專案：https://github.com/ronchen210402/NTU_ML_Final_2021\
                                                                          \neBPF project：https://github.com/ronchen210402/eBPF_project\
                                                                          \nOnline Pokemon：https://github.com/ronchen210402/web_final_duplicated\
                                                                          \nICCAD Contest：https://github.com/ronchen210402/2021_ICCAD_contest_P1\
                                                                          \nFRAIG：https://drive.google.com/file/d/1R_p0SgF7yoj0k_qVb8aTptfV--a3PThz/view'))
    elif '工作' in textin:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='ApooEdu 阿柏教育\
                                                                          \nCofounder & COO\
                                                                          \n• Design and offer project based programming courses to beginners( >200 students per year).\
                                                                          \n• Host AI workshops for colleges and industry.\
                                                                          \n• Build online judge system for student to hand in their assignment.'))
    elif '你的照片' in textin or '大頭照' in textin:
        line_bot_api.reply_message(event.reply_token, ImageSendMessage(original_content_url='https://i.imgur.com/RM6x69R.jpeg', preview_image_url='https://i.imgur.com/RM6x69R.jpeg'))
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='我不懂你說什麼，請再說一次'))


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
