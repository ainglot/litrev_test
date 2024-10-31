from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Funkcja do połączenia z bazą danych SQLite
def get_db_connection():
    conn = sqlite3.connect('test_241031115708.db')  # Użyj odpowiedniej nazwy bazy danych
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/articles', methods=['GET'])
def get_articles():
    year = request.args.get('year')
    conn = get_db_connection()
    if year:
        articles = conn.execute('SELECT * FROM articles WHERE publication_year = ?', (year,)).fetchall()
    else:
        articles = conn.execute('SELECT * FROM articles').fetchall()
    conn.close()
    return jsonify([dict(article) for article in articles])

if __name__ == '__main__':
    app.run(debug=True)
