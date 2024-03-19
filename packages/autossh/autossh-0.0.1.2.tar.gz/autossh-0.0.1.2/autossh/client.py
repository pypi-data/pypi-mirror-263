import threading
import time
from sshtunnel import SSHTunnelForwarder

class AutoSSHTunnel:
    def __init__(self, ssh_server, ssh_username, ssh_password, remote_host, remote_port, local_port, ssh_port=22):
        self.ssh_server = ssh_server
        self.ssh_username = ssh_username
        self.ssh_password = ssh_password
        self.remote_host = remote_host
        self.remote_port = remote_port
        self.local_port = local_port
        self.ssh_port = ssh_port
        self.tunnel = None
        self.running = False
        self.lock = threading.Lock()
        self.thread = None  # Keep track of the check loop thread

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()

    def start(self):
        """Start the SSH tunnel and the check loop."""
        self.start_tunnel()
        self.start_check_loop()

    def stop(self):
        """Stop the SSH tunnel and the check loop."""
        self.stop_tunnel()
        self.running = False
        if self.thread:  # Wait for the check loop thread to finish
            self.thread.join()

    def start_tunnel(self):
        with self.lock:
            if not self.running or (self.tunnel and not self.tunnel.is_active):
                self.tunnel = SSHTunnelForwarder(
                    (self.ssh_server, self.ssh_port),
                    ssh_username=self.ssh_username,
                    ssh_password=self.ssh_password,
                    remote_bind_address=(self.remote_host, self.remote_port),
                    local_bind_address=('', self.local_port)
                )
                self.tunnel.start()
                self.running = True

    def stop_tunnel(self):
        with self.lock:
            if self.tunnel:
                self.tunnel.stop()

    def check_tunnel(self):
        with self.lock:
            if not self.tunnel or not self.tunnel.is_active:
                print("SSH tunnel is down, restarting...")
                if self.tunnel:
                    self.tunnel.stop()
                self.start_tunnel()

    def start_check_loop(self):
        def loop():
            while self.running:
                self.check_tunnel()
                time.sleep(30)

        self.thread = threading.Thread(target=loop)
        self.thread.daemon = True
        self.thread.start()

    def get_tunnel_info(self):
        """Return information about the SSH tunnel."""
        return {
            'ssh_server': self.ssh_server,
            'ssh_port': self.ssh_port,
            'remote_host': self.remote_host,
            'remote_port': self.remote_port,
            'local_port': self.local_port,
            'is_active': self.tunnel.is_active if self.tunnel else False
        }
