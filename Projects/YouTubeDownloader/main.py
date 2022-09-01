import downloadfunc
     
#---Main----
downloadfunc.printTitle()
key = 'Y'

while True:
    op = downloadfunc.option()
    if op == '1':
        downloadfunc.fileDownload(True)
    elif op == '2':
        downloadfunc.fileDownload(False)
    else:
        print('\nExit...\n')
        break
    
    while True:
        key =str(input('Do you want to continue? [Y/N]')).upper()
        if key == 'N':
            print('\nExit...\n')
            exit(1)
        elif key == 'Y':
            break
        else:
            print('Invalid option, please insert "Y" or "N"')