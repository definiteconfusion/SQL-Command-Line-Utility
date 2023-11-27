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
@main.command(help='Navigates to a Directory')
@click.argument('path')
def cd(path):
    if os.path.isdir(path) == True:
        scaffold.datachache(path)
    else:
        structs.error("ERROR -- Specified Path Not Found")
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
            
            
if __name__ == '__main__':
        main()