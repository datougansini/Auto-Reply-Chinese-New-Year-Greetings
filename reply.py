import itchat,re
import time
from itchat.content import *

@itchat.msg_register([TEXT])

def text_reply(msg):
    match=re.search('春|年|新年',msg['Text'])
    if match:
        time.sleep(1)
        itchat.send(('我怕新年的钟声太响，你会听不见我的祝福，我怕除夕的鞭炮太吵，你会收不到我的问候。时至佳节，我选择现在送上新年的祝福， 提前367天给您拜个早年！祝您鼠年快乐！恭喜发财！'),msg['FromUserName'])

itchat.auto_login(enableCmdQR=True)
itchat.run()
