import ytpackage
     
#---Main----
ytpackage.printTitle()
key = 'Y'

while True:
    op = ytpackage.option()
    if op == '1':
        ytpackage.DownloadFile(True)
    elif op == '2':
        ytpackage.DownloadFile(False)
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