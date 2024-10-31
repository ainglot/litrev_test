# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

@app.route('/api/search', methods=['POST'])
def search():
    data = request.get_json()
    year = data.get('year')
    entries = []

    # Połączenie z bazą danych SQLite i wykonanie zapytania
    conn = sqlite3.connect('test_241031115708.db')  # Użyj swojej bazy danych
    cursor = conn.cursor()
    cursor.execute('SELECT title, author, year FROM Bibliografia WHERE year = ?', (year,))
    rows = cursor.fetchall()
    conn.close()

    # Przekształcenie wyników w listę słowników
    entries = [{'title': row[0], 'author': row[1], 'year': row[2]} for row in rows]
    return jsonify(entries)

if __name__ == '__main__':
    app.run(debug=True)
