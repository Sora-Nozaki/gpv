import schedule
import time
from download_task import download
from main import main

schedule.every(1/6).minutes.do(main) #一時間ごとにダウンロードを実行する


while True:
  schedule.run_pending()
  time.sleep(1)
