from sqlalchemy import create_engine

engine = create_engine("hana+hdbcli://SYSTEM:HXEHana1@127.0.0.1:39017", echo=True)
connection = engine.connect()
rs = connection.execute("SELECT 'Hello Python World' FROM DUMMY")

for row in rs:
    print(row)

