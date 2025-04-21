""" 
Connect to remote servers via SSH (Secure Shell).
Run commands on remote servers.
Transfer files between your local system and the remote server using SFTP (SSH File Transfer Protocol).
It’s a great tool for automating tasks, managing remote servers, and securely interacting with systems over a network.
"""

# connect to remote server
import paramiko

# Create an SSH client object, which is used to interact with the remote server.
ssh = paramiko.SSHClient()

# Automatically add the server’s host key (for simplicity in demo, but be cautious in production)
#This method tells the client to automatically trust the server.
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the server (replace with actual server address and login details)
# note here add them as env variables
# key_filename: This is the path to your private key file (my-key.pem).
key_filename = '/path'
ssh.connect('remote_server_address', username='your_username', password='your_password',key_filename=key_filename)

# Once connected, you can run commands, etc.

# Close the connection when done
ssh.close()

#----------------------------------------------------

"""
Running commands remotely 
"""
stdin, stdout, stderr = ssh.exec_command('ls /path/to/directory')

# Print the output
print(stdout.read().decode())

#----------------------------------------------------
"""
Transfering data using SFTP 
"""
# Open an SFTP session
sftp = ssh.open_sftp()

# Upload a file from local to remote server
sftp.put('local_file.txt', '/remote/path/remote_file.txt')

# Download a file from remote to local machine
sftp.get('/remote/path/remote_file.txt', 'downloaded_file.txt')


# Close the SFTP connection
sftp.close()

#-------------------------------------------------