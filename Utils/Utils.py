import datetime
import os
import time


def make_dir(daily_file_folder):
    path = daily_file_folder.strip()
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def bn_timestamp_to_date(ymd):
    tmp_ymd = ymd

    # 毫秒级别时间戳
    if len(str(ymd)) == 13:
        tmp_ymd = ymd / 1000

    time.localtime(tmp_ymd)
    date_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(tmp_ymd))
    day = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    # day = day - datetime.timedelta(hours=8)
    return day