# coding:utf-8
__author__ = 'YangJun'
import paramiko, subprocess

# transport = paramiko.Transport(('10.245.25.60', 22))
# transport.connect(username='nsfocus', password='nsfocus123')
# transport.close()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect(hostname='10.245.25.60', port=22, username='nsfocus', password='nsfocus123')
# stdin,stdout,stderr：分别表示程序的标准输入、标准输出、标准错误
stdin, stdout, stderr = ssh.exec_command('ls -l')
print(str(stdout.read(), encoding='utf-8'))

cd = subprocess.run()
e = subprocess.call()
c=subprocess.getoutput()
