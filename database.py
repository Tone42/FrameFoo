import sqlite3

def save_data(frame_name, measurements, photo_link):
    # Store the data in a database
    conn = sqlite3.connect('frameinfo.db')
    c = conn.cursor()

    # Create the table if it does not exist
    c.execute('CREATE TABLE IF NOT EXISTS data (frame_name text, measurements text, photo_link text)')

    # Insert the data into the table
    c.execute('INSERT INTO data (frame_name, measurements, photo_link) VALUES (?, ?, ?)', (frame_name, measurements, photo_link))
    conn.commit()

    conn.close()
