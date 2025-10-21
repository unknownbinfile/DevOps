import pymysql

# MySQL 서버에 연결
conn = pymysql.connect(
    host="localhost", # MySQL 서버 주소
    user="root",
    password = '1234',
    database="exampledb",

)
# 커서 생성 => 명령어 작성
cursor = conn.cursor()

# 명령어 실행
cursor.execute("UPDATE users SET name = %s WHERE id = %s", ("Bob", 1))

conn.commit()
print("데이터 수정 완료")
conn.close()
