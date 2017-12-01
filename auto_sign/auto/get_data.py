# -*- coding: utf-8 -*-
import os
import sys
import time
import urllib2
import urllib
import cookielib

def getData(params):
  filename = sys.path[0] + '/auto/' + time.strftime("%Y%m%d", time.localtime())
  # if not os.path.exists(filename):
  #   set_cookie.setCookie()
  # filename = sys.path[0] + '/auto/cookie.txt'
  cookie = cookielib.MozillaCookieJar()
  cookie.load(filename, ignore_discard=True, ignore_expires=True)
  handler=urllib2.HTTPCookieProcessor(cookie)
  opener = urllib2.build_opener(handler)

  url = 'http://jp.888ctu.com/FlightQuery/FlightQuery'  
  # params = {  
  #   'fromCityCode':'PEK',
  #   'toCityCode':'SHA',
  #   'fromDate':'2017-11-26',
  #   'returnDate':'',
  #   'carrier':'',
  #   'isFirstQuery':'1',
  #   'transitCity':'',
  #   'flightType':'1'
  # }
  post_data = urllib.urlencode(params).encode('utf-8')
  req=urllib2.Request(url, post_data)
  req.add_header("User-Agent","Chrome/18.1.2.3")
  result = opener.open(req).read()
  return result

