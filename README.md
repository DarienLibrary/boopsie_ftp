# boopsie_ftp
A python script to automate transferring .mrc files to Boopsie's FTP server

## Configuration
### Environment Variables
This script pulls the FTP host, your username and your password from the following environment variables:
```
boopsie_host
boopsie_user
boopsie_password
```
You will need to set those with your credentials.
### Hardcoded Values
The follwoing variables will need to be altered to reflect your configuration and naming conventions:
```
local_directory
remote_directory
filename_trunc
```
You will need to install Python 2.7 on your Polaris server and schedule a task to run the script sometime after the .mrc file is created but before the end of the day.
