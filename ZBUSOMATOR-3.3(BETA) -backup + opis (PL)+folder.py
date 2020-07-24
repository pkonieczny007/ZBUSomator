import os
''' dołożono tworzenie pliku .bak w folderze \backup
dodano opis w działania programu języku PL '''


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
            #ENG version:    
            #print(f'creating backup: {filename_backup} is complete!')

            #PL version:
            print(f'{filename_backup}: utworzono backup!')                

            #create upgraded ZBUS file
            with open(filename,'w') as f:
                file = f.write(file[9::])
                #ENG version: 
                #print(f'creating new version ZBUS file: {filename} is complete!')

                #PL version: 
                print(f'{filename}: utworzono nową wersje pliku ZBUS!')    
        else:
            #ENG version: 
            #print(f'backup file: {filename_backup} is existing. THANK YOU!')

            #PL version: 
            print(f'{filename_backup}: backup istnieje! BRAK MODYFIKACJI PLIKU!')

#3.3 dodano otwieranie folderu ZBUS
path_open = r"\\10.4.0.2\cncprogr"
path_open = os.path.realpath(path_open)
os.startfile(path_open)


# dołożone w 3.1
input("\n\nAby zakonczyc ENTER")
    
