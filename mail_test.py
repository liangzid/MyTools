'''
======================================================
此脚本写于2019年2月,用于对梁子的最新电脑进行自动化测试.
该脚本主要包括以下功能:
1.自动发送邮件;
2.获取并报告电脑的基本信息
3.根据回复确定新的对策



======================================================
'''

import smtplib  #导入发邮件模块
from email.mime.text import MIMEText  #导入email模块，用来玩成邮件内容
from email.header import Header       #               用来完成邮件标题的定义
import os
import requests

# 尝试登录东北大学ip控制网关
url = 'http://ipgw.neu.edu.cn/srun_portal_pc.php?ac_id=1&'
 
# 编辑基本信息
headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Content-Length':'98',
    'Content-Type':'application/x-www-form-urlencoded',
    'Host':'ipgw.neu.edu.cn',
    'Origin':'http://ipgw.neu.edu.cn',
    'Referer':'http://ipgw.neu.edu.cn/srun_portal_pc.php?ac_id=1&',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}
 
data = {
    'action':'login',
    'ac_id':'1',
    'username':'20163933', 
    'password':'39332016', 
    'save_me':'0'
}
login_name='20163933'
# 尝试登录 
r =requests.post(url, data = data, headers = headers)

#print(r.text)

the_first='<hh1>目前您的私人计算机liangzi-cc已经登录.由于cc文件夹下email.py脚本的运行,伟大正直善良勇敢拥有黄金气节的尊敬的团长大人您接收到了这封邮件.目前可提供给您以下信息:</hh1>'

loginUsername='<hh2>我们使用'+login_name+'登录了ip网关,输出页面为:'+r.text+'</hh2>'
log_name='<hh3>您的计算机被登录的账号是:'+os.popen('who').read()+'</hh3>'
time='<hh4>该时刻计算机显示时间为:'+os.popen('date').read()+'</hh4>'
ip='<hh5>计算机的ip信息被记录为:'+os.popen('ifconfig -a').read()+'</hh5>'
warning='<hh6>请注意您是否还保持有对您的计算机的控制权.我们掌握着该计算机的密码并随时可以进行修改工作,不过,请尽快进行.</hh6>'


def sendEMailToOnePerson(Person='liangzi20163933@qq.com',Subject='并没有什么重要的主题',Text='该邮件由liangzi-cc-lenovoxiaoxin510s自动发送于\n'):

    #此处为发送邮件的账号
    sender='2273067585@qq.com'
    #发送邮箱服务器
    smtpserver="smtp.qq.com"
    #发送邮箱用户、密码
    username='2273067585@qq.com'
    password='jsmvjhbewpqlebga'
    #HTML形式的邮件
    msg=MIMEText('<html><h1>'+Text+'</h1></html>','html','utf-8')
    msg['Subject']=Header(Subject,'utf-8')
    
    smtp=smtplib.SMTP_SSL(smtpserver,465)
    smtp.login(username,password)
    smtp.sendmail(sender,Person,msg.as_string())
    smtp.quit()


sendEMailToOnePerson(Subject='最后的提示',Text=the_first+loginUsername+log_name+time+ip+warning)

