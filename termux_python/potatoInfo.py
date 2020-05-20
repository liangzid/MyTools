import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
import re
import time

def getPotatoDataAsDataFrame(potato_url='https://www.cnhnb.com/hangqing/cdlist-2001521-0-15-0-0-1/',
                             ):
    # potato_url='https://www.cnhnb.com/hangqing/tudou/'

    r=requests.get(potato_url)
    # print(r.text)
    soup = bs(r.text,'html.parser')

    info_list=['time','place','price','product'] # information need to get
    data=dict()
    for every_info in info_list:
        ls=list()
        everyResult_everyInfo=soup.find_all('span',class_=every_info)
        for eachResult in everyResult_everyInfo:
            result=eachResult.string
            ls.append(result)
            # print(result)
        data[ls[0]]=ls[1:]
        # print(data)


    priceList=data['价格']
    pricess=list()
    for price in priceList:
        if re.match(r'(.*)元/斤', price) is not None:
            price=price.split('元/斤')
            price=price[0]
            price=float(price)
            pricess.append(price)
        else:
            pricess.append(None)
        # print(price)
    data['【计算使用】']=pricess
    dataFrame=pd.DataFrame(data)
    pricess=pd.Series(pricess)
    # pricess=np.array(pricess)
    # print(pricess)
    # print(pricess.describe())
    # print(dataFrame)
    return dataFrame

def getChangeInfo():
    url_list=['https://www.cnhnb.com/hangqing/cd-2001521-334-0-2610/',
              'https://www.cnhnb.com/hangqing/cd-2001521-351-0-2586/',
              'https://www.cnhnb.com/hangqing/cd-2001521-37153-0-2547/',
              'https://www.cnhnb.com/hangqing/cd-2001521-334-0-2595/'
              ]
    information=''
    for url in url_list:
        r=requests.get(url)
        soup=bs(r.text,'html.parser')
        text='<p>'+'--'*20+'</p>'
        text+='\n'
        texts=soup.meta['content']
        # print(texts)
        text+=texts
        texts=soup.find_all('div',class_='trending-data')
        # print(texts)
        i=0
        for t in texts:
            if i==2:
                text+='\n'
            text+=t.string
            text += '<p>'+t.string+'</p>'
            i+=1

        information+=text
        # print(information)
    return information


def saveData():
    nowTime=time.strftime('%Y-%m-%d', time.localtime(time.time()))
    print(time.time())
    place='山东'
    savePath='./'+place+nowTime+'.csv'
    data=getPotatoDataAsDataFrame()
    # data.to_csv(savePath)
    print('存储成功！存储在：'+savePath)

# print(time.strftime('%Y-%m-%d', time.localtime(time.time())))


# def readAndDraw():
#     nowTime = time.strftime('%Y.%m.%d', time.localtime(time.time()))
#     place = '山东'

def getAllInformation():
    df=getPotatoDataAsDataFrame()
    old_width = pd.get_option('display.max_colwidth')
    pd.set_option('display.max_colwidth', None)
    # cc=df.to_html('./temp.html', escape=False, index=False, sparsify=True, border=0, index_names=False, header=False)
    cc = df.to_html( escape=False, index=False, sparsify=True, border=0, index_names=False, header=False)
    pd.set_option('display.max_colwidth', old_width)
    # print(type(cc))

    describeInfo=pd.Series(df['【计算使用】'])
    sdata=describeInfo.describe()
    sdataa=sdata.to_frame().to_html()

    changeinfo=getChangeInfo()
    nowTime=time.strftime('%Y-%m-%d', time.localtime(time.time()))

    # print(nowTime)
    tx='<p>================================================================</p><p>发送时间：</p>\n'
    tx+='<p>'+str(nowTime)+'</p>'
    tx+='<p>今日山东地区土豆行情：</p>'
    tx+=cc
    tx+='<p>今日统计数据：</p>'
    tx+=str(sdataa)
    tx+="<p>重点关注以下对象：</p>"
    tx+=changeinfo
    tx+='<p>\n\n\n发送人：梁子\n(此邮件为自动发送，无需回复)</p>'
    print(tx)
    return tx


# 发送邮件的函数
def sendMail(person='2273067585@qq.com',smtpserver='smtp.qq.com',
                        username='2273067585@qq.com',password='jsmvjhbewpqlebga',
                        ):

    import smtplib
    from email.mime.text import MIMEText  #导入email模块，用来玩成邮件内容
    from email.header import Header       #               用来完成邮件标题的定义
    '''
    :param person: 发送的目标 
    :param smtpserver: 默认即可
    :param username:   使用发送的邮箱账号
    :param password:   密码
    :param Subject:     邮件主题
    :param Text:        邮件文本——“本质是题目但是这里就当作是文本吧”
    :return: 
    '''
    nowTime = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    Subject="["+str(nowTime)+"土豆价格情况发送]"
    Text=getAllInformation()
    # HTML形式的邮件
    msg = MIMEText('<html><h1>' + Text + '</h1></html>', 'html', 'utf-8')
    msg['Subject'] = Header(Subject, 'utf-8')
    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.login(username, password)
    smtp.sendmail(username, person, msg.as_string())
    smtp.quit()
    print("===========================\n"
          +"发送给"+person+"的邮件成功。\n发送主题为:\n"+Subject+"\n发送内容为：\n"+Text+'\n')


if __name__=="__main__":
    # saveData()
    # getChangeInfo()
    # getAllInformation()
    father='lze13581072358@163.com'
    sendMail(person=father)








# headers = {'User-Agent':'Mozilla/5.0'
#                         # 'AppleWebKit/537.36 (KHTML, like Gecko) '
#                         # 'Chrome/55.0.2883.87 '
#                         # 'Safari/537.36'
#            }