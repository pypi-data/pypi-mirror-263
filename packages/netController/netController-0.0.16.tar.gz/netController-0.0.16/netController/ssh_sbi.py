from netmiko import ConnectHandler
from .nas_inventory import get_host
import re

class NetworkDevice:
    """
    Represents a network device.
    DISCLAIMER: This class and its content are for training purposes only. 
    It should not be used in a production environment without proper review and modification.

    Attributes:
        hostname (str): The hostname of the network device.
        net_connect: The Netmiko connection object for the device.
    """
    def __init__(self, hostname):
        self.hostname = hostname
        self.net_connect = self.get_netmiko_connection()

    def get_netmiko_connection(self):
        """
        Establishes a Netmiko connection to a network device.

        Returns:
            net_connect (Netmiko SSH connection): The Netmiko SSH connection object.

        Raises:
            Exception: If there is an error establishing the connection.

        """
        host = get_host(hostname=self.hostname)
        device_params = {
            "host": host["ip"],
            "username": host["user"],
            "password": host["password"],
            "secret": host["password"],
            "device_type": "vyos" if host["vendor"] == "VyOS" else "juniper" if host["vendor"] == "Juniper" else "cisco_ios"
        }
        try:
            net_connect = ConnectHandler(**device_params)
            return net_connect
        except Exception as e:
            print(f'Error: {e}')
            return None

    def send_command(self, command:str):
        """
        Sends a command to the network controller and returns the output.

        Args:
            command (str): The command to be sent to the network controller.

        Returns:
            str: The output of the command execution.

        Raises:
            Exception: If an error occurs while sending the command.

        """
        try:
            output = self.net_connect.send_command(command)
            return output
        except Exception as e:
            print(f'Error: {e}')
        return None

    def get_backup(self):
        """
        Retrieves the backup configuration from the network device.

        Returns:
            str: The backup configuration if successful, otherwise an error message.

        Raises:
            Exception: If there is an error sending the command or connecting to the device.
        """
        if self.net_connect:
            try:
                if self.net_connect.device_type == "vyos":
                    output = self.send_command("show configuration commands")
                else:
                    self.net_connect.enable()
                    output = self.send_command("show running-config")
                if output:
                    return output
                return "Error retrieving backup"
            except Exception as e:
                return f"Error sending command: {e}"
        else:
            return "Error connecting to the device"

    def get_version(self):
        """
        Retrieves the version information of the network device.

        Returns:
            str: The version information of the network device.
        
        Raises:
            str: If there is an error retrieving the version information or connecting to the device.
        """
        if self.net_connect:
            try:
                if self.net_connect.device_type == "vyos":
                    output = self.send_command("show version")
                else:
                    self.net_connect.enable()
                    output = self.send_command("show version")
                if output:
                    return output
                return "Error retrieving version"
            except Exception as e:
                return f"Error sending command: {e}"
        else:
            return "Error connecting to the device"

    def configure_device(self, config: str, catch_errors:bool=False) -> str:
        """
        Configures the device with the provided configuration.

        Args:
            config (str): The configuration to be sent to the device.

        Returns:
            str: The output of the configuration command if successful, otherwise an error message.

        Raises:
            Exception: If there is an error sending the configuration.

        """
        if self.net_connect:
            try:
                if self.net_connect.device_type == "vyos":
                    config += "\ncommit\n"
                output = self.net_connect.send_config_set(config)
                if output:
                    if catch_errors:
                        errors = self.catch_config_errors(output)
                        return output,errors
                    return output
                return "Error sending configuration"
            except Exception as e:
                return f"Error sending configuration: {e}"
        else:
            return "Error connecting to the device"


    def catch_config_errors(self, config_output:str) -> str:
        """
        Catch and filter out configuration errors from the provided config_output.

        Args:
            config_output (str): The output of the configuration command.

        Returns:
            str: A string containing the filtered configuration errors.

        Raises:
            None

        """
        errors = ""
        if self.net_connect.device_type == "cisco_ios":
            exceptions = [
                "^%\sInterface\s.+\sIPv[46]\sdisabled\sand\saddress\(es\)\sremoved\sdue\sto\sdisabling\sVRF\s.+$",
                "^%\sIPv4\sand\sIPv6\saddresses\sfrom\sall\sinterfaces\nin\sVRF\s.+\shave\sbeen\bremoved$"
            ]
            # Trying to catch Cisco config errors
            for line in config_output.splitlines():
                if re.match("^%.*", line):
                    ignore = False
                    for exception in exceptions:
                        if re.match(exception, line):
                            ignore = True
                            break
                    if not ignore:
                        if errors:
                            errors += "\n"
                        errors += line
        elif self.net_connect.device_type == "vyos":
            vyos_errors = re.search("\n\n.*\n(\s+Set\sfailed\n){0,1}\n", config_output)
            if vyos_errors:
                vyos_errors = "\n".join(filter(lambda x: not re.match(r'^\s*$', x), vyos_errors.group(0).splitlines()))
                errors = vyos_errors
        return errors

    def close_connection(self):
        """
        Closes the Netmiko SSH connection to the network device.
        """
        if self.net_connect:
            self.net_connect.disconnect()