#!/root/.pyenv/shims/python
#! -*- coding:utf-8 -*-

import requests, json

from cities import city_dict

import logger, logging

logger = logging.getLogger(__name__)

'''
    http://www.heweather.com/
    user:uangyy@gmail.com
'''

def get_weather_str(*, city = ""):
    if not city or not city_dict.get(city):
        print("not valid city:{}".format(city))

    weather_info = get_weather(city_dict[city])

    if weather_info:
        today = None
        try:
            today = weather_info["HeWeather5"][0]["daily_forecast"][0]
        except:
            today = None
            logger.info("get today info error", exc_info = True)

        if today:
            max_temp = today["tmp"]["max"]
            min_temp = today["tmp"]["min"]
            wind_sc = today["wind"]["sc"]
            wind_dir = today["wind"]["dir"]
            cond_d = today["cond"]["txt_d"]
            cond_n = today["cond"]["txt_n"]

            cond_str = ""
            if cond_d == cond_n:
                cond_str = "{}转{}".format(cond_d, cond_n)
            else:
                cond_str = cond_d

            wind_str = "{}, {}级".format(wind_dir, wind_sc.replace("-", "到"))

            weather_str = "{}, {}, {}, {}℃ 到 {}℃".format(city, cond_str, wind_str, min_temp, max_temp)
            logger.info(weather_str)
    else:
        weather_str = "无法获取天气信息"

    #print(weather_str)
    return weather_str
    #print(weather_info["weatherinfo"]["city"])


def get_weather(city_no):
    '''
        https://free-api.heweather.com/v5/forecast?city=CN101010100&key=181d42f15c3844a99c7b635bab70b0b6
    '''

    url = "https://free-api.heweather.com/v5/forecast?city=CN{}&key=181d42f15c3844a99c7b635bab70b0b6".format(city_no)

    weather_info = ""
    try:
        weather_info = requests.get(url, timeout = 5).content
        print(weather_info)
        #print(type(weather_info))
    except:
        pass
    
    if weather_info:
        return json.loads(weather_info.decode())
    else:
        return ""


get_weather_str(city = "北京")
