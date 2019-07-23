import json

from App.WL_Order import get_2dfire_order_from_cache, get_2dfire_order_detail_from_cache, seek_2dfire_order_detail
from Utils.Utils import bn_timestamp_to_date
from config import BN_DATAFORMAT, wd_useris, wd_keyid

def get_wd_need_post_json():
    recordset = get_2dfire_order_from_cache()
    needposlist=[]
    for branchrecord in recordset:
        masterset=[]
        needpos = {
        'UserID':wd_useris,
        'KeyID':wd_keyid,
        }
        for rec in branchrecord:
            storecode=rec['orderVo']['entityId']
            orderid=rec['orderVo']['orderId']

            ordertype_tmp=rec['orderVo']['orderType']

            ordertype=''

            if ordertype_tmp==1:
                ordertype='1'
            else:
                if ordertype_tmp==4 or ordertype_tmp==5:
                    ordertype = '2'
                else :
                    ordertype='9'

            master={
                    'SASRMF001':storecode,
                    'SASRMF002':bn_timestamp_to_date(rec['orderVo']['openTime']).strftime(BN_DATAFORMAT),
                    'SASRMF003':bn_timestamp_to_date(rec['orderVo']['openTime']).strftime(BN_DATAFORMAT),
                    'SASRMF004':rec['orderVo']['innerCode'],
                    'SASRMF012':rec['serviceBillVo']['discountAmount'],
                    'SASRMF013':rec['serviceBillVo']['agioTotal'],
                    'SASRMF017':'S',
                    'SASRMF023':rec['orderVo']['entityId'],
                    'SASRMF024':rec['serviceBillVo']['reserveAmount'],
                    'SASRMF026':rec['serviceBillVo']['agioServiceCharge'],
                    'SASRMF026':rec['serviceBillVo']['agioServiceCharge'],
                    'SASRMF029':ordertype,
                    'SASRMF030':'1',
                       }

            detail_total=get_2dfire_order_detail_from_cache()
            seek_details=seek_2dfire_order_detail(detail_total,storecode,orderid)
            detail_set=[]
            for dt in seek_details:
                i=1
                if 'menuCode' in dt:
                    menucode=dt['menuCode']
                else:
                    menucode=dt['name']
                detail={
                    'SASRDT001': i,
                    'SASRDT002': menucode,
                    'SASRDT003': dt['num'],
                    'SASRDT005': dt['price'],
                    'SASRDT007': dt['ratio'],
                }
                detail_set.append(detail)
                i+=1
            masterset.append({'master':master,'detail':detail_set})
            # print({'master':master,'detail':detail_set})

        needpos['SasrData']=masterset
        needposlist.append(needpos)
    # needposstr=json.dumps(needposlist)
    return needposlist
