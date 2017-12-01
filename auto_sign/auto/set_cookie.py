# -*- coding: utf-8 -*-
# !/usr/bin/python
import io
import os
import re
import sys
import time
import pyocr
import urllib2
import urllib
import cookielib
import pyocr.builders
from PIL import Image as PI
from wand.image import Image



def setCookie():
  tools = pyocr.get_available_tools()[:]
  if len(tools)==0:
    print("no ocr tool found")
    sys.exit(1)
  tool = tools[0]
  lang = tool.get_available_languages()[0]
  req_image = []
  final_text = []
  filename = time.strftime("%Y%m%d", time.localtime()) 
  cj = cookielib.MozillaCookieJar(filename)
  opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
  first_page = opener.open("http://www.888ctu.com/Login?fromurl=http://www.888ctu.com/Main.aspx").read()
  img = re.search('<img align="top"\s+src="(.*?)"', str(first_page), re.S).group(1)
  captcha_pic = opener.open('http://www.888ctu.com/'+ str(img)).read()
  img = PI.open(io.BytesIO(captcha_pic)).convert("RGBA")
  pixdata = img.load()
  for y in range(img.size[1]):
    for x in range(img.size[0]):
      if pixdata[x, y][0] < 90:
        pixdata[x, y] = (0, 0, 0, 255)
  for y in range(img.size[1]):
    for x in range(img.size[0]):
      if pixdata[x, y][1] < 136:
        pixdata[x, y] = (0, 0, 0, 255)
  for y in range(img.size[1]):
    for x in range(img.size[0]):
      if pixdata[x, y][2] > 0:
        pixdata[x, y] = (255, 255, 255, 255)
  img.save(r"./input-black.gif", "GIF")
  image_pdf = Image(filename="./input-black.gif", resolution=300)
  image_jpeg = image_pdf.convert('jpeg')
  for img in image_jpeg.sequence:
    img_page = Image(image=img)
    req_image.append(img_page.make_blob('jpeg'))
  for img in req_image:
    txt = tool.image_to_string(
    PI.open(io.BytesIO(img)),
    lang=lang,
    builder=pyocr.builders.TextBuilder()
		  )
    final_text.append(txt)
  print final_text
  captcha_code = eval(final_text[0].replace(':','').replace('=',''))
  print captcha_code

  loginName = 'xxx'
  password = 'xxx'
  postinfo = {
		  'loginName': loginName,
		  'password': password,
		  'yzmvidate': str(captcha_code),
		  'fromurl':'http://www.888ctu.com/FMain.aspx',
		  'ajax':1
	}
  login_data = urllib.urlencode(postinfo).encode('utf-8')

  req=urllib2.Request("http://www.888ctu.com/Static/Login.aspx", login_data)
  req.add_header("User-Agent","Chrome/18.1.2.3")
  result = opener.open(req).read().decode("utf8", 'ignore')
  print result
  cj.save(ignore_discard=True, ignore_expires=True)

setCookie()