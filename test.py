# # Use a pipeline as a high-level helper
# from app import app
# from app.sentiment_analysis_helper import SentimentAnalyzer

# with app.app_context():
#     analyzer = SentimentAnalyzer()
#     print("I love this!", analyzer.analyze_sentiment("I love this!"))
#     print("I do not love this!", analyzer.analyze_sentiment("I do not love this!"))
#     print("I think we should follow the instruction.", analyzer.analyze_sentiment("I think we should follow the instruction."))
#     print("I am Minh", analyzer.analyze_sentiment("I am Minh"))
#     print("I think we can't make it before the deadline", analyzer.analyze_sentiment("I think we can't make it before the deadline"))

import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()

# Get a list of table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
table_names = cursor.fetchall()

# Print the list of table names
print("List of tables:")
for table_name in table_names:
    print(table_name[0])

# Close the database connection
conn.close()
