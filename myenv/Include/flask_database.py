import sqlite3

# Function to initialize the database
def initialize_database():
    conn = sqlite3.connect('poems.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS poems')

    # Create the table
    cursor.execute('''
        CREATE TABLE poems (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            text TEXT
        )''')

    # Insert initial data
    poems_data = [
        ('The Road Not Taken', 'Robert Frost', 'Two roads diverged in a yellow wood, And sorry I could not travel both...'),
        ('Ozymandias', 'Percy Bysshe Shelley', 'I met a traveller from an antique land Who said: Two vast and trunkless legs of stone...'),
        ('Daffodils', 'William Wordsworth', 'I wandered lonely as a cloud That floats on high o''er vales and hills...'),
        ('Sonnet 18', 'William Shakespeare', 'Shall I compare thee to a summer''s day? Thou art more lovely and more temperate...'),
        ('The Raven', 'Edgar Allan Poe', 'Once upon a midnight dreary, while I pondered, weak and weary...')
    ]
    cursor.executemany('INSERT INTO poems (title, author, text) VALUES (?, ?, ?)', poems_data)

    conn.commit()
    conn.close()
# Call initialize_database function
initialize_database()

# Retrieve and print all poems
conn = sqlite3.connect('poems.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM poems')
poems = cursor.fetchall()
for poem in poems:
    print(poem)
conn.close()
