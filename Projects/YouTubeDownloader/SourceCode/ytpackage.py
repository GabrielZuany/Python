from pytube import YouTube
import urllib
import urllib.request

def printTitle():
    """
    =>Print the main layout.
    Returns:
        Nothing.
    """
    print('-'*30, f'\n{"YT DOWNLOADER" :^30}')
    print('-'*30)



def option():
    """
    =>Verify the option inserted by user. Only valid values is '1', '2' or '3'.

    Returns:
        str: valid option inserted.
    """
    valid = False
    while not valid:
        option = str(input('\n1)Download Video;\n2)Download Audio.\n3)Exit.\n-> '))
        if (option == '1' or option == '2' or option == '3') and option.isnumeric():
            return option
        else:
            print('Invalid operation, please try a valid option.\n')



def DownloadFile (video):
    """
    => Verify if the url (read by this function) exists and download accord user option.

    Args:
        video (bool): true = download video // false = download audio.
    """
    path = input('Insert the YT url: ')
    
    try: # verify if the url is valid.
        yt = YouTube(f'{path}')
        findURL = urllib.request.urlopen(f'{path}')
    except:
        print(f'Wasnt possible to find the url < "{path}" >.\nFinishing...')
    else:
        
        print('Downloading...')
        if video == True:    
            YouTube(f'{path}').streams.get_highest_resolution().download('./YT_DOWNLOADS')
            
        else:
            if yt.title.isalpha():
                param = f'{yt.title}.mp3'
            else:
                param = 'FILE.mp3'# If the video contains symbol, the script will rename it generally.
                
            YouTube(f'{path}').streams.get_audio_only().download('./YT_DOWNLOADS', filename=f'{param}')