#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import requests,json,time,hashlib,os

class DDNS:
    def __init__(self):
        self.api_key = ''
        self.secret_key = ''
        self.domain = ''
        self.url = 'https://www.cloudxns.net/api2/ddns'
        self.ip = "http://haobingo.com/ip.php"
        self.timestamp = time.ctime()
		
    def getAPI_HMAC(self,data):
        str = self.api_key + self.url + data + self.timestamp + self.secret_key
        m2 = hashlib.md5()   
        m2.update(str)
        api_hmac = m2.hexdigest()
        return api_hmac
    
    def getIP(self):
        self.curip = requests.get(url = self.ip).content.strip()
        return self.curip
    
    def log(self,string):
        logfile = os.path.join(os.path.split(os.path.realpath(__file__))[0],'log')
        with open(logfile,'a+')as f:
            f.write(string)
            
    def run(self):
        self.ip = self.getIP()
        #data = {'domain': self.domain,'ip': self.ip }
        data = {'domain': self.domain}
        data = json.dumps(data)
        headers = {'API-KEY': self.api_key,
                    'API-REQUEST-DATE': self.timestamp,
                    'API-HMAC': self.getAPI_HMAC(data)
                    }
        r = requests.post(self.url,data=data,headers=headers)
        res = json.loads(r.content)['message'].strip()
        message = '[%s] Update %s : %s\t%s\n' %(self.timestamp, self.domain,self.ip,res)
        print(message)
        self.log(message)
        
			
if __name__ == '__main__':
    ddns =  DDNS()
    ddns.run()
