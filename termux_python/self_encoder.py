
import sys
import rsa

path='./极光科幻社宣传语.txt'
# path=str(sys.argv[1])
print(path)

f=open(path,'r',encoding='utf-8')
# f=open(path)
# text=f.readline()
text=f.read()
eco=text.encode()
print(eco)
eco=~eco
print(eco)
eco=~eco
print(eco)
# eco=eco.encode()
cc=eco.decode()
print(cc)

f.close()