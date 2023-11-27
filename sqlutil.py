import sqlite3


def cmd(command:str, database:str):
        init = sqlite3.connect(f'{database}')
        cursor = init.cursor()
        cursor.execute(f"{command}")
        if "SELECT" in command:
            type_result = cursor.fetchall()
        elif "PRAGMA" in command:
            type_result = cursor.fetchall()
        else:
            type_result = "ENDED IN ELSE"
            init.commit()
        return type_result
        