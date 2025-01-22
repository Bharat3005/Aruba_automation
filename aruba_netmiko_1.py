from netmiko import ConnectHandler

# Define the device parameters
aruba_cx_device = {
    'device_type': 'aruba_aoscx',  # Device type for Aruba AOS-CX
    'host': '192.168.1.1',          # Replace with the IP address of your switch
    'username': 'admin',            # Replace with your username
    'password': 'your_password',     # Replace with your password
    'secret': 'your_enable_password', # Optional: replace if enable password is set
}

# Establish the SSH connection
try:
    connection = ConnectHandler(**aruba_cx_device)
    
    # Enter enable mode if secret is provided
    if aruba_cx_device.get('secret'):
        connection.enable()

    # Send a command to the switch
    output = connection.send_command("show version")
    
    # Print the output of the command
    print(output)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Disconnect from the device
    connection.disconnect()
