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

* 修改 ddns.py 中的 ***self.api_key*** ***self.secret_key*** ***self.domain***
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
1 根据CloudXNS **DDNS 快速修改解析记录值** 说明，IP 值为空时 API 自动获取客户端 IP，故此脚本可不获取本地公网IP。

2 频繁更新解析记录，只要A记录IP不发生改变，CloudXNS并不会接受变更，查阅 **获取解析记录列表** 中可证实更新时间并未发生改变。无需担心因频繁更新IP而导致的DNS查询更新不及时。

3 亦可使用 [CloudXNS Python SDK](https://www.cloudxns.net/Support/detail/id/680.html) ，代码更为简洁。
