import http.cookiejar, urllib.request
import re, os
import sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') 
cj = http.cookiejar.MozillaCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
first_page = opener.open("http://www.enanchu.com/login").read().decode("utf-8")

imgpattern = re.findall('(<li>.*?<div class="font">验证码：</div>(.*?)</li>)', first_page, re.S)
img = re.search('id="cm" src="(.*?)"', str(imgpattern), re.S).group(1)

captcha_pic = opener.open( 'http://www.enanchu.com'+ str(img)).read()
open("PG.jpg", 'wb').write(captcha_pic)
os.system("start PG.jpg");
captcha_code = input("Captcha : ")
id = 'kaifeng'
password = '123456'
postinfo = {
    'userName': id,
    'Password': password,
    'code': str(captcha_code),
}
login_data = urllib.parse.urlencode(postinfo).encode('utf-8')

url = urllib.request.Request("http://www.enanchu.com/login.shtml", login_data)
url.add_header("User-Agent","Chrome/18.1.2.3")
ResponseData = opener.open(url).read().decode("utf8", 'ignore')
f = open("out.html","w",encoding='utf-8')  
f.write(ResponseData)
f.close()

for ind, cookie in enumerate(cj):
    print("%d - %s" %(ind, cookie))
cj.save("cookie.txt")