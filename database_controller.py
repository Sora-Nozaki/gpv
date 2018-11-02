import MySQLdb

def db_insert_file(file_name):
    # 接続する
    conn = MySQLdb.connect(
     user='root',
     passwd='Snozaki0612',
     host='localhost',
     db='mysql')

    # カーソルを取得する
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS `exe2` (
    `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL PRIMARY KEY,
    `downloaded` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci''')

    cur.execute('INSERT IGNORE INTO `exe2` VALUES(%s,CURRENT_TIMESTAMP )',(file_name,))

    cur.close()
    conn.commit()    # コミットする
    conn.close()


def db_select():
    # 接続する
    conn = MySQLdb.connect(
     user='root',
     passwd='Snozaki0612',
     host='localhost',
     db='mysql')

    # カーソルを取得する
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS `exe2` (
    `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL PRIMARY KEY,
    `downloaded` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci''')

    cur.execute('INSERT IGNORE INTO `exe2` VALUES("example_data",CURRENT_TIMESTAMP )')
    conn.commit()

    cur.execute('SELECT name FROM exe2 ORDER BY downloaded DESC')

    recent_file = cur.fetchone()[0]

    cur.close()
    conn.close()     # データベースオジェクトを閉じる
    return recent_file



def db_insert_data(grid_data,announced,grid):
    # 接続する
    conn = MySQLdb.connect(
     user='root',
     passwd='Snozaki0612',
     host='localhost',
     db='mysql')

    # カーソルを取得する
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS `cloud` (
    `grid_data` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `announced` INT(12) NOT NULL,
    `grid` varchar(255) NOT NULL,
    PRIMARY KEY(announced,grid)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci''')

    cur.execute('INSERT IGNORE INTO `cloud` VALUES(%s,%s,%s )',(grid_data,announced,grid))

    cur.close()
    conn.commit()    # コミットする
    conn.close()

def db_select_data(info):
    # 接続する
    conn = MySQLdb.connect(
     user='root',
     passwd='Snozaki0612',
     host='localhost',
     db='mysql')

    # カーソルを取得する
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS `cloud` (
    `grid_data` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `announced` INT(12) NOT NULL,
    `grid` varchar(255) NOT NULL,
    PRIMARY KEY(announced,grid)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci''')

    cur.execute('INSERT IGNORE INTO `cloud` VALUES("example_data","example_data","example_data" )')
    conn.commit()

    sql = "SELECT grid_data, grid FROM cloud WHERE announced = %s"
    cur.execute(sql, (info,))

    recent_all_data = []
    recent_data = cur.fetchall()                        #recent_data  (('10,20,30,40','123,256'),('50,60,70,80','132,155'))
    for record in recent_data:
        recent_every_data = []                          #record       ('10,20,30,40','123,256')
        for data in list(record):                       #data         10,20,30,40
            str_data = data.split(',')                  #str_data     ['10','20','30','40']
            float_data = [float(s) for s in str_data]   #float_data     [10,20,30,40]
            recent_every_data.append(float_data)        #recent_every_data  [[10,20,30,40],[123,256]]
        recent_all_data.append(recent_every_data)       #recent_all_data    [[[10,20,30,40],[123,256]],[[50,60,70,80],[132,155]]]

    cur.close()
    conn.close()     # データベースオジェクトを閉じる
    return recent_all_data
