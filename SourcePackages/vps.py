import json
import requests
import math
import datetime
from pdlearn.wechat import WechatHandler

wechat = WechatHandler()

class vps:
    def get_status():
        url = 'https://api.64clouds.com/v1/getLiveServiceInfo?veid=1367527&api_key=private_yht2chD7EC2T8G23trvZJk2S'
        res = requests.get(url).json()
        useage = res.get('data_counter')/1024/1024/1024
        reset = str(datetime.datetime.fromtimestamp(res.get('data_next_reset')))
        return "已用流量：" + str(math.trunc(useage)) + " GB，重置日期：" + reset

if __name__ == '__main__':
    wechat.send_text(vps.get_status())
    
