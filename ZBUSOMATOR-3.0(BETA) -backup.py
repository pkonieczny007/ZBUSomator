import os
''' dołożono tworzenie pliku .bak w folderze \backup '''


#searching file in folder with ending: '.KW'

for filename in os.listdir():
    if filename.endswith('.KW'):
        with open(filename) as f: #Zbus cnc file open
            file = f.read()
            
        #backuping            
        filename_backup = filename+'.bak'
        path = os.path.abspath(os.getcwd())
        path+= '\\backup'
        filename_backup_path = 'backup\\'+ filename_backup
       
        #ckecking backup
        if not filename_backup in os.listdir(path):
            with open(filename_backup_path, 'a') as backup:
                file_backup = backup.write(file)
            print(f'creating backup: {filename_backup} is complete!')

            #create upgraded ZBUS file
            with open(filename,'w') as f:
                file = f.write(file[9::])
                print('utworzono nowa wersje')
    
        else:
            print(f'backup file: {filename_backup} is existing. THANK YOU!')




    
'''
            print(f'backup file: {filename_backup} is existing')
        else:
            with open(filename_backup, 'a') as backup:
                file_backup = backup.write(file)
            print('creating backup is complete!')'''
