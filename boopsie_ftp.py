import os
from datetime import date
import zipfile
from ftplib import FTP

zipped = True
host = os.environ.get('boopsie_host')
user = os.environ.get('boopsie_user')
password = os.environ.get('boopsie_password')
local_directory = r'C:\ProgramData\Polaris\SrServiceRoot\hermione\18\scheduledjobs'
remote_directory = 'darien'
filename_trunc = 'bib_Boopsie Full MARC_{}'.format(date.today().strftime('%m%d%Y'))
filename = ''
for f in os.listdir(local_directory):
    if f.startswith(filename_trunc): filename = f
    
def zip_file(filename, directory):
    full_filename = '{}\\{}'.format(directory, filename)
    zip_filename = filename.split('.')[0]+'.zip'
    zf = zipfile.ZipFile(zip_filename, mode='w')
    try:
        zf.write(full_filename, filename)
    finally:
        zf.close()
    return zip_filename

def ftp_put(host, user, password, filename, directory):
    full_filename = '{}\\{}'.format(directory, filename)
    ftp = FTP(host, user, password)
    ftp.cwd(remote_directory)
    with open(full_filename, 'rb') as f:
        ftp.storbinary('STOR {}'.format(filename), f)

if filename:
    if zipped:
        filename = zip_file(filename, local_directory)
        local_directory = '.'
    ftp_put(host, user, password, filename, local_directory)
    if zipped:
        os.remove(filename)
