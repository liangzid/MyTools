# 发送邮件的函数
def sendMailUsingQQMail(person='2273067585@qq.com',smtpserver='smtp.qq.com',
                        username='2273067585@qq.com',password='jsmvjhbewpqlebga',
                        Subject="Nothing",Text="Nothing"):
    '''
    ======================================
    package avaliable: smtplib, email
    ======================================
    :param person:
    :param smtpserver:
    :param username:
    :param password:
    :param Subject:
    :param Text:
    :return:
    '''
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



