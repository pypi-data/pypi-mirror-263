# autossh_py.py
import argparse
from autossh import AutoSSHTunnel  
import getpass
import sys
import time

def main():
    parser = argparse.ArgumentParser(description='Set up an SSH tunnel, similar to SSH')
    parser.add_argument('destination', nargs='?', help='SSH target in the format [user@]hostname', default='')
    parser.add_argument('-l', '--login', help='Login name (overrides user in destination)')
    parser.add_argument('-L', required=True, help='Port forwarding in the format local_port:remote_host:remote_port')
    parser.add_argument('-p', '--port', type=int, help='SSH port on the remote host (default is 22)', default=22)

    args = parser.parse_args()

    if '@' in args.destination:
        destination_parts = args.destination.rsplit('@', 1) 
        ssh_username, ssh_server = destination_parts
    else:
        ssh_server = args.destination
        ssh_username = getpass.getuser()  

    if args.login:
        ssh_username = args.login

    try:
        local_port, remote_host, remote_port = args.L.split(':')
        local_port, remote_port = int(local_port), int(remote_port)
    except ValueError:
        print("Error: Invalid port forwarding format. Expected local_port:remote_host:remote_port.")
        sys.exit(1)

    ssh_password = getpass.getpass(f"SSH Password for {ssh_username}@{ssh_server}: ")

    tunnel = AutoSSHTunnel(
        ssh_server=ssh_server,
        ssh_username=ssh_username,
        ssh_password=ssh_password,
        remote_host=remote_host,
        remote_port=remote_port,
        local_port=local_port,
        ssh_port=args.port
    )

    try:
        with tunnel:
            print(f"SSH tunnel established. Forwarding from localhost:{local_port} to {remote_host}:{remote_port}. Press Ctrl+C to exit.")
            while True:
                time.sleep(1)
                pass
    except KeyboardInterrupt:
        print("Closing SSH tunnel...")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
