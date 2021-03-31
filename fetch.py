#This is the file for Program Number 3. -Eddie
import os
from pathlib import Path
import subprocess

  
from ftplib import FTP
# code needs to be adapted to directly retrieve from FTP
# # FTP server details
# IP = "138.47.102.120"
# PORT = 21
# USER = "anonymous"
# PASSWORD = ""
# FOLDER = "/7/"
# USE_PASSIVE = True # set to False if the connection times out

# # connect and login to the FTP server
# ftp = FTP()
# ftp.connect(IP, PORT)
# ftp.login(USER, PASSWORD)
# ftp.set_pasv(USE_PASSIVE)

# # navigate to the specified directory and list files
# ftp.cwd(FOLDER)
# files = []
# ftp.dir(files.append)

# # exit the FTP server
# ftp.quit()

# # display the folder contents
# for f in files:
# 	print(f)


### 1) Creating chmod encoding from a text
word = "Tarot"
chmod_list = []
word_out = ''
bit_length = 8
padding = '0'*(10-bit_length)
# note: going forward use something like this instead:   bin(ord(i))[2:].zfill(10)

for c in word:
    # from character to ascii integer to binary value
    cbin = bin(ord(c))
    # make it 10_bit total length
    X = padding + cbin[2:]
    # add the binary value (not including "0b")
    word_out += cbin[2:]
    rwx = ''
    # divide the 10_bit value for each character into 3 bit lengths
    for i in range(len(X)//3):
        n = i*3
        rwx+=str(int(cbin[n:n+3],2))
    chmod_list.append(rwx)
    print(c, rwx)
chmod_list = [int(x) for x in chmod_list]
chmod_list

# Create files with corresponding chmod access
my_path = 'FTPfiles/'
for i in range(5):
    full_path = my_path + 'file' + str(i+1) + '.txt'
    Path(full_path).touch()
    os.chmod(full_path, chmod_list[i])
    
    
### 2) translating chmod into a message
# Extract Chmod info from a directory & store as a list of 10-bit binary values
os.chdir(my_path)
ls_chmod  = subprocess.run(['ls', '-l'], capture_output=True)
os.chdir('..')

# taking the normal result splits the data up in a way that makes it difficult to work with...
ls_chmod = str(ls_chmod).replace('\\n', ' ')

# added the [1:] to get rid of the '-l' command
ls_chmod = [i for i in ls_chmod.split() if '-' in i][1:]

# create a list of all the rwx codes extracted in binary form
# ensure it returns 10-bit long codes
chmod_bin = []
for i in ls_chmod:
    b = ''
    for c in i:
        if c == "-":
            b += '0'
        else:
            b += '1'
    chmod_bin.append(b)
    

# Convert back to the word
word = ''
for c in chmod_bin:
    c =int(c,2)
    x = ''
    base = str(c)
    for i in base:
        b = bin(int(i))
        x += '0'*(5-len(b)) + str(bin(int(i)))[2:]
    word += chr(int(x,2))
print(word)
