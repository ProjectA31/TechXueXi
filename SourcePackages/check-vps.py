import json
import requests
import math
import datetime
from pdlearn.wechat import WechatHandler
from pdlearn import file

wechat = WechatHandler()

class check_vps:
    def check_status():
        vps_key = file.get_json_data("user/vps_key.json", '{"api_key":""}')      
        url = 'https://api.64clouds.com/v1/getLiveServiceInfo?veid=1367527&api_key=' + vps_key["api_key"]
        res = requests.get(url).json()
        useage = res.get('data_counter')/1024/1024/1024        
        reset = datetime.datetime.fromtimestamp(res.get('data_next_reset'))
        
        json_template = '{"check-1":false, "check-2":false, "check-3":false, "check-4":false, "check-5":false, "check-6":false}'
        json_obj = file.get_json_data("user/vps_status.json", json_template)
        ret = False
        
        if useage < 100:
            json_obj = json.loads(json_template);  # reset the json obj
        elif useage > 100 and json_obj["check-1"] == False:
            json_obj["check-1"] = True
            ret = True 
        elif useage > 200 and json_obj["check-2"] == False:
            json_obj["check-2"] = True
            ret = True
        elif useage > 300 and json_obj["check-3"] == False:
            json_obj["check-3"] = True
            ret = True
        elif useage > 400 and json_obj["check-4"] == False:
            json_obj["check-4"] = True
            ret = True
        elif useage > 450 and json_obj["check-5"] == False:
            json_obj["check-5"] = True
            ret = True            
        elif useage > 480 and json_obj["check-6"] == False:
            json_obj["check-6"] = True
            ret = True
            
        file.save_json_data("user/vps_status.json", json_obj)
        
        if ret:
            ret_str = "已用流量：" + str(math.trunc(useage)) + " GB，重置日期：" + str(reset)
        else:
            ret_str = ""
        
        return ret_str

if __name__ == '__main__':
    str = check_vps.check_status()
    if str != '':
        wechat.send_text(str)
