# =============================================================================
# Download Video/File from web
# =============================================================================

# Importing Libraries
import requests
from clint.textui import progress

# sample_link_to_test = https://files3.lynda.com/secure/courses/2314070/VBR_MP4h264_main_SD/2314070_00_01_WX30_intro.mp4?21nGQ2NTPG5kvrc8IHcQvENHWaJGCc9R1cNLWJLAEREUZN36sINBzhW4iXQDw1MFmYr7I504q2u21ygMVjBtEZ3uwTK96wDjfViq6seX_rJjb4gQQ4dhidUkiRFkWp7Cn4RLS9vvrYv73kxOF6XpH-sEDENE68IyFnv42B3DymsrzPmlDJ6ycjBdb_Q

# Download file in parts with the size of 1024
chunk_sizes = 1024

url = input('\nEnter the URL :')
# Maintain a connection for url
req = requests.get(url, stream=True)

# Input file name from user
file_name = input('\nEnter the FILE name :')

# Input file extention from user
print('\nDefault extention .MP4')
user_input = input('Want to change the default extention (y/n) :')
lower_user_input = user_input.lower()
if lower_user_input == 'y':
    print('\nExtention Example(mkv, mov, txt, avi, etc)')
    file_extention = input('Enter the EXTENTION :')
    replace_file_extention = file_extention.replace('.', '')
    file_extention = '.' + replace_file_extention
else:
    file_extention = '.mp4'

# Combining file name and file extention
files = file_name + file_extention

# Where to store the Video/File
print('\nDefault path (F:/Python/DownloadFileFromWeb/)')
path = input('Want to change the PATH location (y/n):')
lower_path = path.lower()
if lower_path == 'y':
    path = input('Enter the PATH :')
    path = path + '/' + files
else:
    # Change the path location according to u
    path = 'F:/Python/DownloadFileFromWeb/' + files
  
# Downloading File to given location 
with open(path, 'wb') as f:
    print('\nDownloading :', files)
    total_length = int(req.headers.get('content-length'))
    for chunk in progress.bar(req.iter_content(chunk_size = chunk_sizes), expected_size = (total_length / 1024) + 1):
        if chunk:
            f.write(chunk)
            f.flush()

print(' \n')