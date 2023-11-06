import mysql.connector

def connect():
    config = {
        "user":"root",
        "password":"dat123456789",
        "host":"127.0.0.1",
        "port":"3306",
        "database":"giadat2",
        'raise_on_warnings': True,
        'auth_plugin':'mysql_native_password'
    }
    try:
        conn = mysql.connector.connect(**config)
        if conn.is_connected():
            print("Kết nối đến cơ sở dữ liệu thành công.")
        else:
            print("Kết nối đến cơ sở dữ liệu không thành công.")
        return conn
    except mysql.connector.Error as err:
        print(f"Lỗi 2: {err}")

