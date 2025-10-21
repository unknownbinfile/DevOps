import pymysql

# MySQL 서버에 연결
conn = pymysql.connect(
    host="localhost", # MySQL 서버 주소
    user="root",
    password = '1234',
    database="exampledb",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor

)
# 커서 생성 => 명령어 작성
cursor = conn.cursor()

# 명령어 실행
cursor.execute("SELECT DATABASE()")
# 한번 호출에 하나의 ROW를 가져올 때 사용
print("현재 데이터 베이스: ",cursor.fetchone())
# 모든 데이터
# print("현재 데이터 베이스: ",cursor.fetchall())
# ()개수 만큼
# print("현재 데이터 베이스: ",cursor.fetchmany(2))


# 연결 해제
conn.close()
