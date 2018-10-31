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

    cur.execute('''CREATE TABLE IF NOT EXISTS `exe1` (
    `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL PRIMARY KEY,
    `downloaded` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci''')

    result = cur.fetchall()

    cur.execute('INSERT IGNORE INTO `exe1` VALUES(%s,CURRENT_TIMESTAMP )',(file_name,))

    conn.commit()    # コミットする

    # cur.execute('SELECT * FROM exe1 ')


def db_select():
    # 接続する
    conn = MySQLdb.connect(
     user='root',
     passwd='Snozaki0612',
     host='localhost',
     db='mysql')

    # カーソルを取得する
    cur = conn.cursor()

    cur.execute('SELECT name FROM exe1 ORDER BY downloaded DESC')
    recent_file = cur.fetchone()[0]

    cur.close()
    conn.close()     # データベースオジェクトを閉じる
    return recent_file

def db_insert_data(file_name):
    # 接続する
    conn = MySQLdb.connect(
     user='root',
     passwd='Snozaki0612',
     host='localhost',
     db='mysql')

    # カーソルを取得する
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS `grid_data` (
    `grid_data` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL PRIMARY KEY,
    `TIME` DATETIME NOT NULL ,
    `grid` DATETIME NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci''')

    result = cur.fetchall()

    cur.execute('INSERT IGNORE INTO `exe1` VALUES(%s,CURRENT_TIMESTAMP )',(file_name,))

    conn.commit()    # コミットする

    # cur.execute('SELECT * FROM exe1 ')
