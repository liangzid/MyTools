import rsa

publicky,privky=rsa.newkeys(2048)
with open('puk.pem','w+') as f:
    f.write(publicky.save_pkcs1().decode())
with open('prk.pem','w+') as f:
    f.write(privky.save_pkcs1().decode())
something=publicky.save_pkcs1().decode()
for i in something:
    if i =='\n':
        print(1)
print(publicky)
print('---------------------------')
print(privky)