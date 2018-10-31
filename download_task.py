import urllib.request
import requests
from pytz import timezone
from datetime import datetime, date, timedelta
from database_controller import db_insert_file, db_select

def download():
    now_time_utc = datetime.now(timezone('UTC')) #UTC

    for i in range(3):
        today = (now_time_utc - timedelta(hours=i*3)).strftime("%Y/%m/%d") # yyyy/mm/dd
        today_str = (now_time_utc - timedelta(hours=i*3)).strftime("%Y%m%d") #yyyymmdd

        hour = str((int((now_time_utc - timedelta(hours=i*3)).strftime("%H")) // 3) * 3).zfill(2) #00,03,06,09,12,15,18,21

        file_name = "Z__C_RJTD_" + today_str + hour + "0000_MSM_GPV_Rjp_Lsurf_FH00-15_grib2.bin" #予報時間によって 00-15,16-33,34-39 と変更する

        url = "http://database2.rish.kyoto-u.ac.jp/arch/jmadata/data/gpv/original/" + today + "/" + file_name


        if db_select() == file_name:
            print("this file already exists.")
            return False
        else:
            try:
                urllib.request.urlretrieve(url,file_name)
                db_insert_file(file_name)
                print("file download complete.")
                return file_name
            except:
                print("file couldn't be downloaded.")
    return False
