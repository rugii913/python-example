# 파이썬 내장 SQLite 및 DB browser for SQLite 사용 - DB browser for SQLite https://sqlitebrowser.org/

# 사용 순서
## - 1. database 파일 열기
## - 2. 커서(cursor) 생성
## - 3. SQL 명령 실행
## - 4. 커밋 또는 롤백
## - 5. database 닫기(리소스 반환)


# 모듈 추가
import sqlite3

# -------------------------------------- #

# DDL(item 테이블 생성) 예시
## 데이터베이스 열기
conn = sqlite3.connect("myvenv/standard/chapter05/example.db")

## 커서 생성
cur = conn.cursor()

## SQL 작성
CREATE_SQL = """
    CREATE TABLE IF NOT EXISTS item(
        id integer primary key autoincrement,
        code text not null,
        name text not null,
        price integer not null
    );
"""

## SQL 실행
cur.execute("DROP TABLE IF EXISTS item")
cur.execute(CREATE_SQL)

## 데이터베이스 닫기
conn.close()

# -------------------------------------- #

# DML(item 테이블에 레코드 삽입) 예시
## 데이터베이스 열기
conn = sqlite3.connect("myvenv/standard/chapter05/example.db")

## 커서 생성
cur = conn.cursor()

## SQL 작성
INSERT_SQL = "INSERT INTO item(code, name, price) VALUES (?, ?, ?);" # ? 사용 가능

## SQL 실행 - 데이터 한 건 삽입
cur.execute(INSERT_SQL, ("A00001", "마우스", 38_000))

## SQL 실행 - 데이터 여러 건 삽입
data = ( # 중첩 튜플 혹은 중첩 리스트 등 iterable 객체로 만들어줌
    ("A00002", "에어컨", 350_000),
    ("A00003", "스마트폰", 800_000),
    ("A00004", "노트북", 650_000)
)
cur.executemany(INSERT_SQL, data)

## 커밋 - INSERT, UPDATE, DELETE는 커밋하지 않으면 반영되지 않음
conn.commit()

## 데이터베이스 닫기
conn.close()

# -------------------------------------- #

# DML(item 테이블 조회) 예시
## 데이터베이스 열기
conn = sqlite3.connect("myvenv/standard/chapter05/example.db")

## 커서 생성
cur = conn.cursor()

## SQL 작성
SELECT_SQL = "SELECT * FROM item LIMIT 2;"

## SQL 실행
cur.execute(SELECT_SQL)

rows = cur.fetchall() # SELECT는 커밋 필요 없음, 대신 cursor를 실행하기 위해 fetchall() 등 명시 필요
for row in rows:
    print(row)

## 데이터베이스 닫기
conn.close()

# -------------------------------------- #

# DML(item 테이블 레코드 수정) 예시
## 데이터베이스 열기
conn = sqlite3.connect("myvenv/standard/chapter05/example.db")

## 커서 생성
cur = conn.cursor()

## SQL 작성
UPDATE_SQL = "UPDATE item set price=650000 WHERE code='A00002';"

## SQL 실행
cur.execute(UPDATE_SQL)

## 커밋 - INSERT, UPDATE, DELETE는 커밋하지 않으면 반영되지 않음
conn.commit()

## 데이터베이스 닫기
conn.close()
