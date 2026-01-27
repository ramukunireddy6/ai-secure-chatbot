import psycopg2

def query_pgvector(embedding):
    conn = psycopg2.connect("dbname=rag user=postgres")
    cur = conn.cursor()
    cur.execute("""Select content from document order by embedding <-> %s LIMIT 5 """,(embedding,))
    return [r[0] for r in cur.fetchall()]