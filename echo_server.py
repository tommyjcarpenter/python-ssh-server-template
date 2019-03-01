#!/usr/bin/env python3.6
#
# Copyright (c) 2013-2018 by Ron Frederick <ronf@timeheart.net> and others.
#
# This program and the accompanying materials are made available under
# the terms of the Eclipse Public License v2.0 which accompanies this
# distribution and is available at:
#
#     http://www.eclipse.org/legal/epl-2.0/
#
# This program may also be made available under the following secondary
# licenses when the conditions for such availability set forth in the
# Eclipse Public License v2.0 are satisfied:
#
#    GNU General Public License, Version 2.0, or any later versions of
#    that license
#
# SPDX-License-Identifier: EPL-2.0 OR GPL-2.0-or-later
#
# Contributors:
#     Ron Frederick - initial implementation, API, and documentation

# To run this program, the file ``ssh_host_key`` must exist with an SSH
# private key in it to use as a server host key. An SSH host certificate
# can optionally be provided in the file ``ssh_host_key-cert.pub``.
#
# Authentication requires the directory authorized_keys to exist with
# files in it named based on the username containing the client keys
# and certificate authority keys which are accepted for that user.

import asyncio, asyncssh, sys


COMMAND_TERMINATOR = ";"


# NOTE: if you want a line by line processor (equiv to user pressing enter), rather then a terminator seperator,
# then uncomment out this.
# async def handle_client(process):
#     process.stdout.write('Enter statements, or EOF when done:\n')
#
#     total = 0
#
#     try:
#         async for line in process.stdin:
#             line = line.rstrip('\n')
#             process.stdout.write('Line was = %s\n' % line)
#             if line == "ERROR":
#                 process.stderr.write('stderr test\n')
#     except asyncssh.BreakReceived:
#         process.exit(0)


async def handle_client(process):
    process.stdout.write('Enter statements, or EOF when done:\n')

    total = 0

    while True:
        try:
            x = await process.stdin.readuntil(COMMAND_TERMINATOR)
            print(x)

            # make sure any long work done here with x is async!!

            if x == "ERROR;":
                process.stderr.write('stderr test\n')
        except asyncssh.BreakReceived:
            process.exit(0)


class MySSHServer(asyncssh.SSHServer):
    def connection_made(self, conn):
        self._conn = conn

    def begin_auth(self, username):
        try:
            self._conn.set_authorized_keys('authorized_keys/%s' % username)
        except IOError:
            pass

        return True


async def start_server():
    await asyncssh.create_server(MySSHServer, '', 8022,
                                 server_host_keys=['ssh_host_key'],
                                 process_factory=handle_client)


loop = asyncio.get_event_loop()


try:
    loop.run_until_complete(start_server())
except (OSError, asyncssh.Error) as exc:
    sys.exit('Error starting server: ' + str(exc))

loop.run_forever()
