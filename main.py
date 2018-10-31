from osgeo import gdal, gdalconst
import matplotlib.pyplot as plt
from download_task import download
from flask import Flask, render_template, request, url_for, redirect
import re
from datetime import datetime 


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
            data_everyhours.append(data)

        date = re.search("[0-9]{10}" , file_name)
        tdatetime = datetime.strptime(date, '%Y%m%d%H%M%S') #読み込んだデータの初期時間を求める(UTC)


        plt.plot(range(len(data_everyhours)),data_everyhours)

        plt.savefig('%s.png'%file_name)

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
    if request.method == 'POST' and request.form['passwd'] == "kuala":
        return render_template('data.html',title=title)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True # デバッグモード有効化
    app.run(host='0.0.0.0') # どこからでもアクセス可能に
