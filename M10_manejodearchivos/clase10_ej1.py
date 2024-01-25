import sys

if(len(sys.argv)==4):
    print('El primer argumento es:',sys.argv[1])
    print('El segundo argumento es:',sys.argv[2])
    print('El tercer argumento es:', sys.argv[3])
else:
    print("Error, se intrudujo un numero distinto de 3")