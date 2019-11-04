import pymysql

# DB 연결용
def get_connection():
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='mypassword',
        db='mydatabase',
        charset='utf8',
        autocommit=True)
    return conn

# DB 커서 생성용
def get_cursor(conn):
    cur = conn.cursor(pymysql.cursors.DictCursor)
    return cur