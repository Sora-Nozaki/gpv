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
    `grid_data` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL PRIMARY KEY,
    `announced` INT(12) NOT NULL ,
    `grid` varchar(255) NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci''')

    cur.execute('INSERT IGNORE INTO `cloud` VALUES(%s,%s,%s )',(grid_data,announced,grid))

    cur.close()
    conn.commit()    # コミットする
    conn.close()

def db_select_data(branch):
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
    `announced` INT(12) NOT NULL PRIMARY KEY,
    `grid` varchar(255) NOT NULL PRIMARY KEY) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci''')

    cur.execute('INSERT IGNORE INTO `cloud` VALUES("example_data",, )')
    conn.commit()

    cur.execute('SELECT name FROM grid_data ORDER BY announced DESC') #announcedの挙動が確認してない

    recent_file = cur.fetchone()[0]

    cur.close()
    conn.close()     # データベースオジェクトを閉じる
    return recent_file
