import click
import os
import sqlutil
import scaffold
import json
import structs


with open("data.json", 'r') as json_file:
    setData = json.load(json_file)
@click.group()
def main():
    pass

#
# -- CD COMMAND
@main.command(help='Navigates to a Directory')
@click.argument('path')
def cd(path):
    if os.path.isdir(path) == True:
        scaffold.datachache(path)
    else:
        structs.error("ERROR -- Specified Path Not Found")
        
#
# -- CONSOLE COMMAND
@main.command(help='Enters into SQL Console')
@click.option('--read', '-r', is_flag=True, help='Makes Table Request Read Only')
def console(read):
    dataCache = scaffold.initsetup()
    if read != True:
        # prompstartassurence = 0
        click.secho('SQL CONSOLE 👍')
        while 0 == 0:
            if len(scaffold.databaseLocator(dataCache["path"])) >= 1:
                command = click.prompt(f"{setData['path']} ~$")
                if command == "--help":
                    structs.help()
                else:
                    dbname = scaffold.databaseLocator(dataCache["path"])
                    try:
                        retstate = sqlutil.cmd(command, dbname[0])
                        print(retstate)
                    except:
                        structs.error("Error -- Database Error -- Type '--help' for help")
            else:
                structs.error("Error -- No Database Found at the Specified Path -- Type 'cd' to specify a new path")
                break

#
# -- VISUAL COMMAND
@main.command()
@click.argument('elements')
@click.argument('table')
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
            click.echo(row)


            
if __name__ == '__main__':
        main()