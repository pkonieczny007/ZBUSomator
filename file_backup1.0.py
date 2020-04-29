import os

filename = "T122D90218.KW"

#Zbus cnc file open
with open(filename) as f:
    file = f.read()

#backuping
filename_backup = filename+'.bak'
print(filename_backup)

#ckecking backup
if filename_backup in os.listdir():
    print('backup file is existing')
else:
    with open(filename_backup, 'a') as backup:
        file_backup = backup.write(file)
    print('creating backup is complete!')

#create upgraded ZBUS file

with open(filename,'w') as f:
    file = f.write(file[9::])
print('utworzono nowa wersje')
