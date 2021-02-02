import psycopg2
from queries import create_queries, delete_queries


def create_db():
    """
    Creates the database
    @return: cursor and connection to sparkifydb
    """
    
    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    
    return cur, conn


def delete_tables(cur, conn):
    """
    Drops the tables in the delete_queries list.
    @param cur:
    @param conn:
    """
    for query in delete_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Creates the tables in the create_queries list.
    @param cur:
    @param conn:
    """
    for query in create_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    Creates a connection and creates the Database 
    Drops the tables if they exist
    Creates the required tables
    """

    cur, conn = create_db()
    
    delete_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()