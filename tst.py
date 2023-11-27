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
        numColums = len(sqlutil.cmd(command, dbname[0]))
        # ds = sqlutil.cmd(command, dbname[0])[0][1]
        rowCache = []
        rowLst = []
        rowStr = ""
        for columNameAppend in range(numColums):
            rowCache.append(sqlutil.cmd(command, dbname[0])[columNameAppend][1])
        for rows in range(rngLen + 1):
            itmCmd = f"SELECT {', '.join(str(column) for column in rowCache)} FROM {table} WHERE rowid = {rows + 1}"
            response = sqlutil.cmd(itmCmd, dbname[0])
            for colums in range(numColums):
                if rows == 0:
                    rowStr = rowStr + rowCache[colums] + " | "
                    rowLst.append(rowStr)
                    rowStr = ""
                else:
                    print(rowLst)
                    rowStr = rowStr + response[0][colums] + " | "
                    rowLst.append(rowStr)
                    rowStr = ""
                    
        for rowPrn in range(len(rowLst)):
            print(rowLst[rowPrn])
visual("table", "assets")