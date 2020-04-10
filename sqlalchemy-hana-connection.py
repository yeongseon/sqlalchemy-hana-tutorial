from sqlalchemy import create_engine

engine = create_engine("hana+pyhdb://SYSTEM:HXEHana1@127.0.0.1:39017", echo=True)
#engine = create_engine("hana+hdbcli://SYSTEM:HXEHana1@127.0.0.1:39017", echo=True)
#engine = create_engine("hana+hdbcli://T12345:Password123@127.0.0.1:39017", echo=True)
connection = engine.connect()
rs = connection.execute("SELECT 'Hello Python World' FROM DUMMY")
#rs = connection.execute("SELECT * FROM Tables")
#rs = connection.execute("SELECT * FROM STUDENTS")
#rs = connection.execute("DROP TABLE STUDENTS")

#print(len(rs))
for row in rs:
    print(row)

