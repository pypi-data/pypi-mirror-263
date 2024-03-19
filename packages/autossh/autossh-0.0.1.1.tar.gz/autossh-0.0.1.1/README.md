# auto-ssh

Usage:

```python
with AutoSSHTunnel(
    ssh_server='ssh.example.com', 
    ssh_username='your_username', 
    ssh_password='your_password', 
    remote_host='remote.example.com', 
    remote_port=3306, 
    local_port=5000,
    ssh_port=2222   
) as tunnel:
    info = tunnel.get_tunnel_info()
    print(f"SSH tunnel established from local port {info['local_port']} to {info['remote_host']}:{info['remote_port']}")
    print(f"Tunnel is active: {'Yes' if info['is_active'] else 'No'}")

```
Or: 

```python
tunnel = AutoSSHTunnel(
    ssh_server='ssh.example.com', 
    ssh_username='your_username', 
    ssh_password='your_password', 
    remote_host='remote.example.com', 
    remote_port=3306, 
    local_port=5000,
    ssh_port=2222  
)

tunnel.start()

try:
    info = tunnel.get_tunnel_info()
    print(f"SSH tunnel established from local port {info['local_port']} to {info['remote_host']}:{info['remote_port']}")
    print(f"Tunnel is active: {'Yes' if info['is_active'] else 'No'}")
finally:
    tunnel.stop()
```