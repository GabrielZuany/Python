import downloadfunc
     
#---Main----
downloadfunc.printTitle()
op = downloadfunc.option()

if op == '1':
    downloadfunc.fileDownload(True)
elif op == '2':
    downloadfunc.fileDownload(False)
else:
    print('\nExit...\n')