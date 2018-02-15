# CloudXNS DDNS

## 介绍
更新在CloudXND解析的域名。

支持python2 & python3。


## 安装

```
git clone https://github.com/HaoBingo/CloudXNS_DDNS
cd CloudXNS_DDNS
sudo pip install requests
```

* 修改 ddns.py 中的self.api_key self.secret_key self.domain
* 登录CloudXNS后访问 [此处](https://www.cloudxns.net/AccountManage/apimanage.html) 获取API

## 使用
```
python main.py
```
LINUX 下使用 crontab 设置定时任务 (python 和 ddns.py 脚本路径自行替换)

```
crontab -e
*/10 * * * * python  ddns.py    #每10分钟更新一次
```

日志记录在 log 文件中

## PS
根据CloudXNS  https://www.cloudxns.net/api2/ddns 说明，

IP 值为空时 API 自动获取客户端 IP，故此脚本可不获取本地公网IP。
