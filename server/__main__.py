import asyncio
import asyncssh
import sys
from server.echo_server import start_server


def main():

    loop = asyncio.get_event_loop()


    try:
        loop.run_until_complete(start_server())
    except (OSError, asyncssh.Error) as exc:
        sys.exit('Error starting server: ' + str(exc))

    loop.run_forever()


if __name__ == "__main__":
    main()
