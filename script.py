from sqlalchemy import create_engine, text

engine = create_engine('postgresql://lziqbjkd:HP_7F8AFjzdQO8vXtVPrEJLV0wRRcML2@dumbo.db.elephantsql.com:5432/lziqbjkd')

queryDrop = 'DROP TABLE remplas'
querySelect = 'SELECT * FROM remplas'

with engine.connect() as conn:
    conn.execute(text(queryDrop))
    result = conn.execute(text(querySelect))
    print(result.fetchall())

