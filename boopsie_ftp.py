import os
from datetime import date, datetime
import zipfile
from ftplib import FTP

zipped = True
host = os.environ.get('boopsie_host')
user = os.environ.get('boopsie_user')
password = os.environ.get('boopsie_password')
local_directory = r'C:\ProgramData\Polaris\SrServiceRoot\Ginny\18\scheduledjobs'
filename_trunc = 'bib_Boopsie Full MARC_{}'.format(
    date.today().strftime('%m%d%Y'))
logfile = 'log_boopsie.txt'
filename = ''
for f in os.listdir(local_directory):
    if f.startswith(filename_trunc):
        filename = f


def zip_file(filename, directory):
    zip_filename = 'catalog_extract_full.zip'
    arcname = 'catalog_extract_full.mrc'
    zf = zipfile.ZipFile(
        zip_filename, compression=zipfile.ZIP_DEFLATED, mode='w')
    try:
        zf.write(full_filename, arcname)
    finally:
        zf.close()
    return zip_filename


def ftp_put(host, user, password, filename, directory):
    full_filename = r'{}\{}'.format(directory, filename)
    ftp = FTP(host, user, password)
    ftp.cwd('darien')
    with open(full_filename, 'rb') as f:
        ftp.storbinary('STOR {}'.format(filename), f)
    ftp.close()


if filename:
    full_filename = r'{}\{}'.format(local_directory, filename)
    if zipped:
        zip_filename = zip_file(filename, local_directory)
        ftp_put(host, user, password, zip_filename, '.')
        os.remove(zip_filename)
    else:
        ftp_put(host, user, password, filename, local_directory)
    os.remove(full_filename)
    with open(logfile, 'a') as f:
        f.write('{}: Successfully uploaded {}\n'.format(
            datetime.now(), full_filename))
else:
    with open(logfile, 'a') as f:
        f.write('{}: File not found to upload\n'.format(datetime.now()))
