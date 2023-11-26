import click
import os
import sqlutil
import scaffold
import json

while 0 == 0:
    dataCache = {
        "path":"C:\\Users\\littl\\OneDrive\\Documents\\GitHub\\Megascans-Asset-Translator"
    }
    
    with open("data.json", 'r') as json_file:
        setData = json.load(json_file)

    @click.group()
    def main():
        pass


    @main.command(help='Navigates to a Directory')
    @click.argument('path')
    def cd(path):
        if os.path.isdir(path) == True:
            dataCache["path"] = path
            scaffold.initsetup(dataCache)
        else:
            print("ERROR -- Specified Path Not Found")



    @main.command(help='Enters into SQL Console')
    @click.option('--read', '-r', is_flag=True, help='Makes Table Request Read Only')
    def console(read):
        if read != True:
            prompstartassurence = 0
            while 0 == 0:
                if prompstartassurence == 0:
                    click.secho('SQL CONSOLE 👍')
                command = click.prompt(f"{setData['path']} ~$")
                dbname = scaffold.databaseLocator(dataCache["path"])
                retstate = sqlutil.cmd(command, dbname[0])
                print(retstate)
                prompstartassurence += 1




    if __name__ == '__main__':
        main()