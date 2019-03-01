# python-ssh-server-template
template for a command based async SSH server

# Usage

1) Generate a keypair for the server: `ssh-keygen -t rsa`
1) Put the private key  as `server_host_key` somewhere (or if using for real, put a real key there)
2) set the ENV variable `SERVER_HOST_KEY_LOC`
3) Make an `authorized_keys` directory somewhere
4) Add the client public keys into the file `../path_to_authorized_keys/CLIENT_USERNAME`
5) set the ENV variable `SERVER_AUTHORIZED_KEYS_DIR`
5) Start the server

```
cd server
python echo_server.py
```

SSH into it (from another terminal window, assuming `ssh_client_key.pub` is in the file  `SERVER_AUTHORIZED_KEYS_DIR/myclient`:

```
ssh -p 8022  myclient@localhost -i ssh_client_key
```

The current command terminator is `;`. The server will print each command the client enters, until the client closes their connection.
