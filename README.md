# python-ssh-server-template
template for a command based async SSH server

# Keys
Note, this package comes with two sets of test RSA keys. They were created just for this project.

# Usage

Start the server

```
python echo_server.py
```

SSH into it (from another terminal window):

```
ssh -p 8022  myclient@localhost -i ssh_client_key
```
