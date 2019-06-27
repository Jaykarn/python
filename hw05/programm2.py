import os
M = int(input('введите M:'))
count = 0
while count < M:
    N = input('N:')
    S = input('S:')
    count += 1
#os.system("programm1.py" + ' ' + '-' + 'N' + ' ' + N + ' ' + '-' + 'S' + ' ' + S)
    os.system(f'programm1.py -N {N} -S {S}')