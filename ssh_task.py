
from paramiko.client import SSHClient
from pprint import pprint

HOST = "..."
USER = "..."

client = SSHClient()
client.load_system_host_keys()
client.connect(hostname=HOST, username=USER)
stdin, stdout, stderr = client.exec_command('ls -l')

pprint(list(stdout))
print()


# upload file
open("hello.txt", "w").write("hello world\n")
sftp_client=client.open_sftp()
sftp_client.put("hello.txt", "remote_hello.txt")
sftp_client.close()


stdin, stdout, stderr = client.exec_command('cat remote_hello.txt')
pprint(list(stdout))
