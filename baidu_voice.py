#!/root/.pyenv/shims/python
#! -*- coding:utf-8 -*-
import requests, sys, subprocess, datetime, time
from utils import string_to_int

import logger, logging

logger = logging.getLogger(__name__)

def get_token():
    url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=D44vrKovmg61FFHLDdWbjs5y&client_secret=081b0637d066b5f2cbaebcc5e4505bdf&"
    res = requests.get(url, timeout = 5).json()
    token = res.get("access_token")
    return token

def generate_str():
    t = datetime.datetime.now()
    #t = datetime.datetime.strptime("00:09:00", "%H:%M:%S")
    h = string_to_int(t.hour)
    m = string_to_int(t.minute)

    h_str = ""
    m_str = ""

    if h == 2:
        h_str = "两点"
    else:
        h_str = "{}点".format(h)

    if m == 0:
        m_str = "整"
    elif m < 10:
        m_str = "零{}分".format(m)
    else:
        m_str = "{}分".format(m)

    echo_str = "现在时刻：{}{} ".format(h_str, m_str)
    return echo_str


def echo_time(volume = 21):
    try:
        tok = get_token()
        echo_str = generate_str()
        url = "http://tsn.baidu.com/text2audio?tex={}&lan=zh&cuid=9ab66b78ef7a11e6a88a001c42f4948e&ctp=1&tok={}".format(echo_str, tok)
        #res = subprocess.getstatusoutput("mpg123 \"{}\"".format(url))
        cmd = "mplayer -volume {} \"{}\"".format(2 * volume, url)
        logger.info(cmd)
        res = subprocess.getstatusoutput(cmd)
    except:
        pass


def echo_str(volume = 21, text = ""):
    if not str:
        return
    try:
        tok = get_token()
        echo_str = text
        url = "http://tsn.baidu.com/text2audio?tex={}&lan=zh&cuid=9ab66b78ef7a11e6a88a001c42f4948e&ctp=1&tok={}&per=0".format(text, tok)
        #res = subprocess.getstatusoutput("mpg123 \"{}\"".format(url))
        cmd = "mplayer -volume {} \"{}\"".format(2 * volume, url)
        logger.info(cmd)
        res = subprocess.getstatusoutput(cmd)
    except:
        pass

#echo("于洋")

'''
count = 0
while True:
    count += 1
    logger.info(count)
    if count % 50 == 0:
        echo_str(volume = 50, text = "我擦， 赶紧给我订一份饭。我饿死了。")
        time.sleep(1)
    else:
        echo_str(volume = 50, text = "崔晓静，请帮我订一份外卖！！！")
        time.sleep(1)
'''


'''
if __name__ == "__main__":
    text = sys.argv[1]
    tok = get_token()
    logger.info(tok)
    url = "http://tsn.baidu.com/text2audio?tex={}&lan=zh&cuid=9ab66b78ef7a11e6a88a001c42f4948e&ctp=1&tok=24.def46a986a2f55e7f95d4f99614d0b97.2592000.1489313938.282335-9266089".format(text)
    res = subprocess.getstatusoutput("mpg123 \"{}\"".format(url))
    logger.info(res)
'''
