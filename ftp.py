from ftplib import FTP

ftp = FTP('ftp.cwi.nl')

ftp.login()

ftp.retrlines('LIST')


