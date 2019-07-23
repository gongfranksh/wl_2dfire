import datetime
import json
import os
from App import daily_file_folder, procdate, MY_APPID
from App.WL_Shop import get_2dfire_shop_from_cache
from Utils.bn_2dfire_tools import bn_2dfire_connect_api, split_order_byMaxNum
from config import app_secret, app_key, url_api_v1, method_v1_orderlist, cache_order, url_api_v2, method_v1_orderdetail, \
    cache_order_detail


def get_2dfire_order_from_api():

    print('get_2dfire_order_from_api')

    print(procdate)
    MY_URL = {'bn_2dfire_function_api':url_api_v1,'bn_2dfire_function_method':method_v1_orderlist}
    rst=[]
    stores = get_2dfire_shop_from_cache()
    for store in stores:

        para = {
            'para_my_url': MY_URL,
            'para_my_appid': MY_APPID,
            'para_my_store': store['shop']['entityId'],
        }

        data = {
            "currdate": procdate,
            "orderids": None
        }

        recordset = bn_2dfire_connect_api(para).Get_ResultAll(data)
        if recordset is not None:
            if 'model' in recordset:
                print(recordset)
                rst.append(recordset['model'])
                #
    with open(daily_file_folder + os.sep + cache_order, 'wt') as f:
        f.write(json.dumps(rst))
    return True


def get_2dfire_order_from_cache():
    with open(daily_file_folder + os.sep + cache_order, 'r') as f:
        rst=(json.load(f))
    return  rst

def get_2dfire_orderid_from_cache():
    orders=get_2dfire_order_from_cache()
    rst=[]
    for storeorders in orders:
        for ods in storeorders:
            # print('orderid=====>'+ods['orderVo']['orderId']+'___entityId====>'+ods['orderVo']['entityId'])
            one={'entityId':ods['orderVo']['entityId'],'orderId':ods['orderVo']['orderId']}
            rst.append(one)
    return  rst


def get_2dfire_store_orderid_from_cache(entityId):
    orders=get_2dfire_orderid_from_cache()
    rst=[]
    for one in orders:
        if one['entityId']==entityId:
            rst.append(one['orderId'])
    return  rst


def get_2dfire_order_detail_from_api():
    print('get_2dfire_order_detail_from_api')
    MY_URL = {'bn_2dfire_function_api':url_api_v1,'bn_2dfire_function_method':method_v1_orderdetail}
    currdate = procdate.strftime("%Y-%m-%d").replace('-', '')

    needstore=[]
    print(procdate)
    stores = get_2dfire_shop_from_cache()

    for store in stores:
        para = {
            'para_my_url': MY_URL,
            'para_my_appid': MY_APPID,
            'para_my_store': store['shop']['entityId'],
        }

        ld_by_orderid=get_2dfire_store_orderid_from_cache(store['shop']['entityId'])
        split_orderlist = split_order_byMaxNum(ld_by_orderid)
        remote_records = []
        for rec in split_orderlist:

            data = {
                "currdate": procdate,
                "orderids": str(rec)
            }

            recordset = bn_2dfire_connect_api(para).Get_ResultAll(data)

            if recordset is not None:
                if 'model' in recordset:
                    for rc in recordset['model']:
                        remote_records.append(rc)

        if len(remote_records)!=0:
            needstore.append(remote_records)

    with open(daily_file_folder + os.sep + cache_order_detail, 'wt') as f:
                         f.write(json.dumps(needstore))

    return True

def get_2dfire_order_detail_from_cache():
    with open(daily_file_folder + os.sep + cache_order_detail, 'r') as f:
        rst=(json.load(f))
    return  rst

def seek_2dfire_order_detail(odlists,entityid,orderid):
    rst=[]
    for odlist in odlists:
         for od in odlist:
             if od['entityId']==entityid and od['orderId']==orderid:
                 rst.append(od)
    return  rst