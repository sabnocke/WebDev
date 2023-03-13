from sqlalchemy import create_engine, text, select
from sqlalchemy.orm import Session

'''db_connection_string = "mysql+pymysql://r71icbeuey7ukv6tt5jo:pscale_pw_xjaPO2lDWZuFysBmjfdJvXcyYC479PHdyuJ9touA5Hf@eu" \
                       "-central.connect.psdb.cloud/heap?charset=utf8mb4"'''
db_connection_string = (
    "mysql+pymysql://r71icbeuey7ukv6tt5jo:pscale_pw_xjaPO2lDWZuFysBmjfdJvXcyYC479PHdyuJ9touA5Hf@eu"
    "-central.connect.psdb.cloud/heap"
    "?ssl_ca=cacert-2023-01-10.pem")

engine = \
    create_engine(db_connection_string)

with Session(engine) as session:
    stmt = select(text('*')).select_from(text('saferoom'))

    execute = session.execute(stmt)
    list_dict = [row._asdict() for row in execute.all()]

    print(list_dict)

