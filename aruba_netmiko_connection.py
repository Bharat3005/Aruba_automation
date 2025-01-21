from netmiko import ConnectHandler
import time

# Define the device details
RTR = {
    'device_type': 'aruba_os',  # Specify the device type
    'host': 'your_switch_ip',
    'username': 'your_username',
    'password': 'your_password',
    'port': 22,  # Optional, default is 22
}

try:
    # Connect to the switch
    connection = ConnectHandler(**RTR)
    print("SSH connection established")

    # Execute a command (e.g., show version)
    output = connection.send_command('show version /n')
    print(output)

finally:
    # Close the connection
    connection.disconnect()
    print("SSH connection closed")