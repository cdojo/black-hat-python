#!/usr/bin/python

import threading
import paramiko
import subprocess

# 1 - We create a function called ssh_comand, which makes a connection to an SSH server and runs single command.
def ssh_command(ip, user, passwd, command):
	client = paramiko.SSHClient()

	# 2 - Paramiko supports authentication with keys instead of password authentication.
	# client.load_host_keys('/home/justin/.ssh/known_hosts')

	# 3 - Because we're controlling both ends of this connection, we set the policy to accept the SSH key
	# for the SSH server we're connecting to and make the connection.
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(ip, username=user, password=passwd)

	ssh_session = client.get_transport().open_session()

	if ssh_session.active:
		# 4- Finally, assuming the connection is made, we run the command that we passed along in the call
		# to the ssh_command() function.
		ssh_session.exec_command(command)

		print ssh_session.recv(1024)

	return


ssh_command('localhost', 'root', 'toor', 'id')
