import scaffold
import sqlutil
import scaffold
import sqlutil
def visual(elements, table):
    dataCache = scaffold.initsetup()
    if elements == 'table':
        dbname = scaffold.databaseLocator(dataCache["path"])
        command = f"SELECT COUNT(*) FROM {table}"
        retstate = sqlutil.cmd(command, dbname[0])
        rngLen = retstate[0][0]
        command = f"PRAGMA table_info({table})"
        columns_info = sqlutil.cmd(command, dbname[0])
        numColumns = len(columns_info)
        column_names = [column[1] for column in columns_info]
        
        rowLst = []
        for rows in range(rngLen + 1):
            rowStr = ""
            itmCmd = f"SELECT {', '.join(column for column in column_names)} FROM {table} WHERE rowid = {rows}"
            response = sqlutil.cmd(itmCmd, dbname[0])
            for columns in range(numColumns):
                if rows == 0:
                    rowStr += column_names[columns] + " --|-- "
                else:
                    rowStr += str(response[0][columns]) + " --|-- "
            rowLst.append(rowStr)
            
        for row in rowLst:
            print(row)

visual("table", "assets")