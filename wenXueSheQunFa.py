'''
实现群发邮件功能。
1.读取xlsx文件的基本内容，并生成相应的文本
2.使用邮件客户端发送过去
'''

# 发送邮件的函数
def sendMailUsingQQMail(person='2273067585@qq.com',smtpserver='smtp.qq.com',
                        username='2273067585@qq.com',password='jsmvjhbewpqlebga',
                        Subject="Nothing",Text="Nothing"):
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
    # HTML形式的邮件
    msg = MIMEText('<html><h1>' + Text + '</h1></html>', 'html', 'utf-8')
    msg['Subject'] = Header(Subject, 'utf-8')
    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.login(username, password)
    smtp.sendmail(username, person, msg.as_string())
    smtp.quit()
    print("===========================\n"
          +"发送给"+person+"的邮件成功。\n发送主题为:\n"+Subject+"\n发送内容为：\n"+Text+'\n')

def mainOfWenXueSheQunFa():

    import os
    # import requests
    import xlrd  # 读取xlsx文件

    path="D://allDataForWindows//document//Tencent Files//2273067585//FileRecv//新建 Microsoft Excel 工作表.xlsx"
    workbook=xlrd.open_workbook(path)
    sheet=workbook.sheet_by_index(0)
    sheetList=[]
    for i in range(sheet.nrows):
        temp_list=[]
        for j in range(sheet.ncols):
            temp_list.append(sheet.cell_value(i,j))
        # print(temp_list)
        sheetList.append(temp_list)
    print(sheetList)
    # lis=sheetList[1:-1,:] #不允许切片操作，哈哈

    # 开始进行发邮件操作
    for ii in range(len(sheetList)):
        if ii==0:
            continue  #是类别，没有数据
        else:
            keyText=sheetList[ii][:]
            print(keyText)
            if keyText[3]=='南湖':
                usualText='{0}，您好，您的文章{1}已经被鼎原文学社刊载！' \
                          '在德育加分之余特送您鼎原文学社社刊一份。' \
                          '请于2019年6月5日(星期三)下午七点到九点至大成304来取，等你来哦！' \
                          '(本讯息在接受到肯定回复时生效，退订请回TD)'.format(keyText[1],keyText[0])
                sender=str(int(keyText[5]))+'@qq.com'
                zhuti="【鼎原文学社稿件刊登通知】"
                sendMailUsingQQMail(person=sender,Subject=zhuti,Text=usualText)
# run
mainOfWenXueSheQunFa()


