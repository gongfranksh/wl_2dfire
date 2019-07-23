import datetime
import os
import time

from Utils.Utils import make_dir
from config import app_key, app_secret

procdate=datetime.datetime.now() - datetime.timedelta(days=1)

MY_APPID = {'bn_2dfire_app_key': app_key, 'bn_2dfire_app_secret': app_secret}

data_dir_name='datas'
daily_dir_name = data_dir_name +'\\' +procdate.strftime('%Y-%m-%d')
daily_file_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)) \
                      + os.sep \
                      + daily_dir_name
print(daily_dir_name)
make_dir(daily_file_folder)




