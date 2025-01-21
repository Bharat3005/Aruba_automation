import paramiko

# Define the device details
RTR = {
    'hostname': 'your_switch_ip',
    'port': 22,
    'username': 'your_username',
    'password': 'your_password'
}

# Create an SSH client
client = paramiko.SSHClient()

# Automatically add the server's host key (not recommended for production)
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the switch
    client.connect(**RTR)
    print("SSH connection established")

    # Execute a command (e.g., show version)
    stdin, stdout, stderr = client.exec_command('show version') #stdin(standard_input), stdout(standard_output), stderr(standard_error) 
    print(stdout.read().decode())

finally:
    # Close the connection
    client.close()
    print("SSH connection closed")