import json
import os

from App import daily_file_folder
from App.WL_Order import get_2dfire_order_from_api, get_2dfire_order_from_cache, get_2dfire_orderid_from_cache, \
    get_2dfire_order_detail_from_api, get_2dfire_order_detail_from_cache
from App.WL_Shop import get_2dfire_shop_from_api, get_2dfire_shop_from_cache
from Wd_Order.Wd_Order import get_wd_need_post_json
from config import cache_store, cache_order

# with open(daily_file_folder+os.sep + cache_store,'r') as f:
#     print(json.load(f))
# with open(daily_file_folder+os.sep + cache_order,'r') as f:
#     records=json.load(f)
#
#
# for rec in records:
#     print(rec)

# get_2dfire_shop_from_api()
# get_2dfire_order_from_api()
# get_2dfire_order_detail_from_api()
# # record=get_2dfire_order_detail_from_cache()
# recordset=get_2dfire_order_from_cache()
# for branchrecord in recordset:
#     for rec in branchrecord:
#         print(rec['orderVo'])
#         # print(rec['totalPayVo'])
#         # print(rec['payVoList'])
#         # print(rec['kindPayVoList'])
#         # print(rec['serviceBillVo'])
#

needpostjslist=get_wd_need_post_json()
for p in needpostjslist:
    print(json.dumps(p)+'\t')


