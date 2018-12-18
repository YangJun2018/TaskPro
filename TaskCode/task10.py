# coding:utf-8
__author__ = 'YangJun'
import paramiko, os, time


# transport = paramiko.Transport(('10.245.25.60', 22))
# transport.connect(username='nsfocus', password='nsfocus123')
# transport.close()

class Paramiko_ssh(object):
    def __init__(self, ip, port, username, password):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        self.ssh.connect(hostname=self.ip, port=self.port, username=self.username, password=self.password)

    def ssh_exc(self, cmd, path):
        # ssh = paramiko.SSHClient()
        # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        # ssh.connect(hostname='10.245.25.60', port=22, username='root', password='nsfocus!@#')
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        self.ssh.connect(hostname=self.ip, port=self.port, username=self.username, password=self.password)
        # stdin,stdout,stderr：分别表示程序的标准输入、标准输出、标准错误
        stdin, stdout, stderr = self.ssh.exec_command('cd' + path + ';' + cmd)
        # print(str(stdout.read(), encoding='utf-8'))


class Paramiko_Put(object):
    def __init__(self, ip, port, username, password, local_dir, remort_dir):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.local_dir = local_dir
        self.rt_dir = remort_dir
    def pk_connect(self):
        self.pk = paramiko.Transport(self.ip, self.port)
        self.pk.connect(username=self.username, password=self.password)
        try:
            return paramiko.SFTPClient.from_transport(self.pk)
        except Exception as e:
            print('Connect error:%s') % e
            exit()
    def pk_put(self):
        sftp = self.pk_connect()
        # 本地上传目录和文件
        files = os.listdir(self.local_dir)
        cnt = 0
        for file in files:
            sftp.put(os.path.join(self.local_dir, file), os.path.join(self.rt_dir, file))
            cnt += 1
        if cnt == len(files):
            print("% +' files put successful'" % cnt)
        else:
            print("put file error")
    def __del__(self):
        self.pk.close()


class Paramiko_Get(object):

    def __init__(self, ip, port, username, password, local_dir, remort_dir):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.local_dir = local_dir
        self.rt_dir = remort_dir
    def pk_connect(self):
        self.pk = paramiko.Transport(self.ip, self.port)
        self.pk.connect(username=self.username, password=self.password)
        try:
            return paramiko.SFTPClient.from_transport(self.pk)
        except Exception as e:
            print('Connect error:%s') % e
            exit()
    def pk_put(self):
        sftp = self.pk_connect()
        # 本地上传目录和文件
        files = sftp.listdir(self.local_dir)
        cnt = 0
        for file in files:
            sftp.get(os.path.join(self.rt_dir, file, os.path.join(self.local_dir, file)))
            cnt += 1
        if cnt == len(files):
            print("% +' files get successful'") % cnt
        else:
            print("get file error")
    def __del__(self):
        self.pk.close()
