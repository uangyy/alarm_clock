#!/root/.pyenv/shims/python
#! -*- coding:utf-8 -*-

import subprocess, getopt, sys, os, time, random

from baidu_voice import echo_time, echo_str

from get_weather import get_weather_str

from utils import string_to_int

import logger, logging

random.seed(time.time())

song_dir = "/root/Music/songs/"

DEFAULT = 0
RANDOM = 1

logger = logging.getLogger(__name__)


def generate_playlist(*, mode = DEFAULT, size = -1):

    songs = [s for s in os.listdir(song_dir) if s.endswith(".mp3")]

    if mode == RANDOM:
        random.shuffle(songs)
    else:
        pass

    with open("{}playlist.lst".format(song_dir), "w") as lst:
        for s in songs[ : size]:
            lst.write("{}\n".format(s))



def play_songs(*, name = "", volume = 0):

    with open("{}playlist.lst".format(song_dir), "r") as lst:
        for one_song in lst:
            time.sleep(2)
            echo_time(volume)
            tell_weather(city = "北京", volume = volume)
            time.sleep(1)
            play_cmd = "mplayer -volume {} {}\"{}\"".format(volume, song_dir, one_song.strip())
            logger.info(play_cmd)
            cmd_res = subprocess.getstatusoutput(play_cmd)


def tell_weather(city = "北京", volume = 0):
    weather_str = get_weather_str(city = city)
    logger.info("{}:{}".format(city, weather_str))

    echo_str(volume = volume, text = weather_str)


    
if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "m:s:n:v:", ["mode=", "size=", "name=", "volume="])
    except getopt.GetoptError:
        logger.info("getopt error", exc_info = True)
        sys.exit(1)

    mode = DEFAULT
    size = -1
    name = ""
    volume = 21
    for o, v in opts:
        if o in ("-m", "--mode"):
            mode = v
            if v.lower().find("rand") != -1:
                mode = RANDOM
        
        if o in("-s", "--size"):
            size = string_to_int(v)
            if size <= 0:
                size = -1

        if o in("-n", "--name"):
            name = v

        if o in("-v", "--volume"):
            volume = string_to_int(v)

    generate_playlist(mode = mode, size = size)
    #cmd = "mplayer -playlist {}playlist.lst".format(song_dir)
    #cmd_res = subprocess.getstatusoutput(cmd)


    play_songs(name = name, volume = volume)
