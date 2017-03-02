import requests,bs4,os,re
print('Please enter the hashtag for which you wish to download the results')
search_tag=input()
print('Enter the folder name in which you wish to save the results')
fname=input()
res=requests.get('https://www.instagram.com/explore/tags/'+ search_tag + '/?hl=en')
prg=re.compile(r'display_src.*?jpg')
xx=prg.findall(res.text)
print('Starting download....\n')
for i in range(len(xx)):
    print((xx[i])[15:])
    dd=(xx[i])[15:]
    res1=requests.get(dd)
    imageFile = open(os.path.join(fname,os.path.basename(dd)), 'wb')
    for chunk in res1.iter_content(100000000):
                imageFile.write(chunk)
    imageFile.close()
print('Download Successful')    
