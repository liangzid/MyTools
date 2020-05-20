import requests






resourcePath='d://allDataForWindows//Desktop//musiclist.txt'

toPath='h://music//'

url163="http://music.163.com/song/media/outer/url?id="
m='.mp3'

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}#创建头部信息



with open(resourcePath,'r',encoding='utf-8') as f:
    for line in f.readlines():
        name=line.split(',')[0]
        id=line.split(',')[1].split('\n')[0]
        print(name)
        print(id)
        print(url163+id+m)
        res=requests.get(url163+id+m,headers=headers)
        music=res.content
        with open(toPath+name+m,'wb') as bf:
            bf.write(music)
        print('==========================================')

print("done.")

# # 测试 下载并存储一个文件
# headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}#创建头部信息
# res=requests.get('http://music.163.com/song/media/outer/url?id=30431367.mp3',headers=headers)
# music=res.content
# with open(toPath+'test'+m,'wb') as bf:
#     bf.write(music)




