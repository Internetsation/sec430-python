#!/usr/bin/python
__author__ = 'kilroy'
#  (c) 2014, WasHere Consulting, Inc.
#  Written for Infinite Skills

"""

This sample Python program sets a unique cookie, and read back the results

"""
import urllib2

url = "https://www.google.com"
request = urllib2.Request(url)
resp = urllib2.urlopen(request)
cookies = resp.info()['Set-Cookie']
content = resp.read()
resp.close()

# print the content of the cookie you just set
print (cookies, content)