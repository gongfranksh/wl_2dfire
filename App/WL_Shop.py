import json
import os
import time

from App import daily_dir_name, daily_file_folder, MY_APPID
from Utils.bn_2dfire_tools import bn_2dfire_connect_Request
from config import url_api_v2, method_v2_shoplist, app_key, cache_store

def get_2dfire_shop_from_api():
    print('get_2dfire_shop_from_api')
    MY_URL = url_api_v2
    ewh_request = bn_2dfire_connect_Request()

    MY_DATA = {
        "method": method_v2_shoplist,
        "appKey": app_key ,
        "v": "1.0",
        "timestamp": str(int(time.time() * 1000)),
        "lang": '',
    }

    recordset = ewh_request.get_json(MY_URL, MY_APPID, MY_DATA)
    if recordset is not None:
        if 'data' in recordset:
            # _logger.info(recordset)
            print (recordset['data']['data'])
            with open(daily_file_folder+os.sep + cache_store,'wt') as f:
                f.write(json.dumps(recordset['data']['data']))


def get_2dfire_shop_from_cache():
    with open(daily_file_folder + os.sep + cache_store, 'r') as f:
        rst=(json.load(f))
    return  rst

