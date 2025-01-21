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

    #Execute set of command on the switch 
    set_command = {"show version", 
                   "show system", 
                   "show ip int br", 
                   "show int eth 1/1/1"
                   }
    output = connection.send_config_set(set_command)
    print(output)

    #Execute command on the switch from file
    with open('aruba_config', 'r') as config_file:
        for config in config_file:
            print('config')
            output= connection.send_config_from_file(config_file='aruba_config')
            print(output)
    
finally:
    # Close the connection
    connection.disconnect()
    print("SSH connection closed")