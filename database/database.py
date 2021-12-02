import sqlite3, random

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('database/charades.db')

    def get_cards(self, genres):
        query_string = 'WHERE GENRE ='
        for genre in genres:
            query_string += f" '{genre}' OR GENRE ="

        query_string = query_string[0:-11]
        cursor = self.connection.execute(f"SELECT QUESTION FROM QUESTIONS {query_string};")
        
        selected_cards = []
        for row in cursor:
            selected_cards.append(row[0])

        random.shuffle(selected_cards)
        return selected_cards
