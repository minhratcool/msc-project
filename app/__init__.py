import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_data.db'  # SQLite database URI
db = SQLAlchemy(app)

from app import routes

# def init_db():
#     conn = sqlite3.connect('user_data.db')
#     cursor = conn.cursor()
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             email TEXT NOT NULL UNIQUE,
#             name TEXT NOT NULL,
#             age INTEGER NOT NULL,
#             title TEXT NOT NULL,
#             job_description TEXT NOT NULL,
#             supervisor TEXT NOT NULL
#         )
#     ''')
#     conn.commit()
#     conn.close()

# init_db()