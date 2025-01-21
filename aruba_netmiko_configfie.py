from netmiko import ConnectHandler

# Define the device details
RTR = {
    'device_type': 'aruba_os',
    'host': 'your_switch_ip',
    'username': 'your_username',
    'password': 'your_password',
    'port': 22,
}

try:
    # Connect to the switch
    connection = ConnectHandler(**RTR)
    print("SSH connection established")

    # List of configuration commands to execute
    config_commands = [
        'interface GigabitEthernet0/1',
        'description Connected to Server',
        'ip address 192.168.1.1 255.255.255.0',
        'no shutdown'
    ]

    # Send configuration commands
    output = connection.send_config_from_file(config_file) # type: ignore
    print(f"Configuration Output:\n{output}\n")

finally:
    # Close the connection
    connection.disconnect()
    print("SSH connection closed")