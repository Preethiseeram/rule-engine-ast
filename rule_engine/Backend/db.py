import sqlite3

def create_db():
    conn = sqlite3.connect('rules.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS rules
                      (id INTEGER PRIMARY KEY, rule_text TEXT)''')
    conn.commit()
    conn.close()

def store_rule(rule_text):
    conn = sqlite3.connect('rules.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO rules (rule_text) VALUES (?)", (rule_text,))
    conn.commit()
    conn.close()

def get_rules():
    conn = sqlite3.connect('rules.db')
    cursor = conn.cursor()
    cursor.execute("SELECT rule_text FROM rules")
    rules = cursor.fetchall()
    conn.close()
    return rules