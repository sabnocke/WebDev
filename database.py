from sqlalchemy import create_engine, text, select
from sqlalchemy.orm import Session

db_connection_string = (
    "mysql+pymysql://user:password@connect/db_name"
    "?ssl_ca='cert'")

engine = \
    create_engine(db_connection_string)

with Session(engine) as session:
    stmt = select(text('*')).select_from(text('saferoom'))

    execute = session.execute(stmt)
    list_dict = [row._asdict() for row in execute.all()]

    print(list_dict)

