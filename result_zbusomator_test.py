import os

results = [filename for filename in os.listdir() if filename.endswith('.KW')]

for result in results:
    with open(result) as f:
        file = f.read()
        print(result, ': ')
        print(file[0:2])
        a = [i for i in file[0:2]]
        

print('results: ',results)


