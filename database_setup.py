import sqlite3

# obtain cursor from db conn object, use to execute SQL commands (e.g. daily_entries table)
connect_DB_File = sqlite3.connect("tracker.db")

# call connect_DB_File to create cursor object
cursor_Obj = connect_DB_File.cursor()

# tell the database to create your first table: daily_entries
# columns:
    # ID - int & primary key
    # date - when entry is made
    # overall market mood - bullish/bearish/neutral
    # personal emotional state - how the market is effecting their mental well being
    # notes - leave empty if nothing to add
daily_entries_table_sql = """
CREATE TABLE daily_entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    overall_market_mood TEXT NOT NULL,
    personal_emotional_state TEXT NOT NULL,
    notes TEXT
)
"""

# method to call on cursor_Obj to execute SQL command that's stored in daily_entries_table_sql
cursor_Obj.execute(daily_entries_table_sql)

# commit changes in database, then close the connection
connect_DB_File.commit()
connect_DB_File.close()

# print statement to confirm completion
print("Database 'tracker.db' and table 'daily_entries' created successfully (if they didn't already exist).")