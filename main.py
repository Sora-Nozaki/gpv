from osgeo import gdal, gdalconst
import matplotlib.pyplot as plt
from download_task import download
from flask import Flask, render_template, request, url_for, redirect
import re
from datetime import datetime, timedelta
from database_controller import db_insert_data,db_select_data,db_select


# 自身の名称を app という名前でインスタンス化する
app = Flask(__name__)

def main():
    file_name = download()
    if file_name:
        # register drivers
        gdal.AllRegister()

        # create a data set object
        dataset = gdal.Open(file_name, gdalconst.GA_ReadOnly)

        latitude_end = 47.6
        longitude_end = 120

        latitude = 35.03
        longitude = 135.77

        grid_latitude = int((latitude_end - latitude) / 0.05 )
        grid_longitude = int((longitude - longitude_end) / 0.0625 )

        print(grid_latitude,grid_longitude)


        col_num = dataset.RasterXSize  # 東西のグリッドの個数
        row_num = dataset.RasterYSize  # 南北のグリッドの個数
        band_num = dataset.RasterCount # ラスターの個数

        print(col_num,row_num,band_num)

        data_everyhours = []
        hours_ago = (band_num // 12) + 1  # i時間先の予報
        for i in range(hours_ago):
            if i == 0 or i == 1:
                target_band_num = 10 * (i + 1)  # 読み込むラスターの番号
            else:
                target_band_num = 20 + (i - 1) * 12   # 読み込むラスターの番号

            print(target_band_num)
            band = dataset.GetRasterBand(target_band_num)

            # read the band as matrix
            data_matrix = band.ReadAsArray()
            data = data_matrix[grid_latitude,grid_longitude] #指定したグリッドにおけるデータ
            data_everyhours.append(str(data))

        date = int(re.search("[0-9]{10}" , file_name).group())
        print(date)
        print(re.search("[0-9]{10}" , file_name))
        print(re.search("[0-9]{10}" , file_name).group())
        print(type(re.search("[0-9]{10}" , file_name).group()))
        grid = str(grid_latitude) + "," + str(grid_longitude)
        grid_data = ','.join(data_everyhours)
        db_insert_data(grid_data,date,grid)




        plt.plot(range(len(data_everyhours)),data_everyhours)
        plt.cla()

@app.route('/')
def index():
    title = "GPV"
    message = "ようこそ！GPVへ"
     # index.html をレンダリングする
    return render_template('index.html',
                           message=message, title=title)

@app.route('/kuala-gpv', methods=['GET','POST'])
def post():
    title = "データ一覧"
    # recent_file = db_select()
    # date = re.search("[0-9]{10}" , recent_file)
    # tdatetime = datetime.strptime(date.group(), '%4Y%2m%2d%2h') #読み込んだデータの初期時間を求める(UTC)
    # date_time = (tdatetime + timedelta(hours=9))
    # date_times = []
    # for i in range(15): #hours_agoを使えそう...
    #     every_date_time = (date_time + timedelta(hours=i).strftime("%m/%d %h:00") # 11/1 6:00
    #     date_times.append(every_date_time)



    if request.method == 'POST' and request.form['passwd'] == "kuala":
        return render_template('data.html',title=title)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True # デバッグモード有効化
    app.run(host='0.0.0.0') # どこからでもアクセス可能に
