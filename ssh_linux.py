import paramiko
import time

# 创建一个ssh对象
ssh = paramiko.SSHClient()
# 自动添加策略，保存服务器的主机名和密钥信息
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.0.11", 22, "user", "deepwise")
# 建立一个新的伪终端频道，用来执行子shell
chan = ssh.invoke_shell()
time.sleep(0.1)
chan.send("sudo su \n")
buff = ''
while not buff.endswith("user: "):
    resp = chan.recv(9999)
    buff += resp.decode("utf8")

print(buff, "%"*10)
chan.send("deepwise")
chan.send('\n')
buff = ''
while not buff.endswith("# "):
    resp = chan.recv(9999)
    buff += resp.decode("utf8")

print(buff, "&"*10)
chan.send('whoami')
chan.send('\n')
buff = ''
while not buff.endswith("# "):
    resp = chan.recv(9999)
    buff += resp.decode("utf8")
ssh.close()
result = buff
print(result, "*********")
