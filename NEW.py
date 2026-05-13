import mysql.connector as MySQL

def test_countcheck():
    # Establish database connection
    connect = MySQL.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="your_db"
    )
    cursorobj = connect.cursor()

    # Execute count queries
    cursorobj.execute("SELECT COUNT(*) FROM src")
    src_count = cursorobj.fetchone()[0]

    cursorobj.execute("SELECT COUNT(*) FROM trg")
    trg_count = cursorobj.fetchone()[0]

    # Assertion
    assert src_count == trg_count, f"Count mismatch: SRC={src_count}, TRG={trg_count}"

    # Cleanup
    cursorobj.close()
    connect.close()
