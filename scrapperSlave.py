# import urllib.request as req
# import re
# import simplejson
# import requests
# from bs4 import BeautifulSoup
#
# # def is_ascii(s):
# #     try:
# #         s.decode('ascii')
# #         # return True
# #     except UnicodeDecodeError:
# #         return False
#
#
# # def imLS():
# #     url = 'https://www.instagram.com/bas_kar_na_yar/?hl=en'
# #     data = req.Request(url)
# #     resp = req.urlopen(data)
# #     respData = resp.read()
# #
# #     dat = re.findall(r'"src"\s*:\s*"(.+?)"', str(respData))
# #     # cap = re.findall(r'"text"\s*:\s*"(.+?)"', str(respData))
# #     rec = []
# #     for x in dat:
# #         if re.search("/s640x640/", x):
# #             rec.append(x)
# #     return rec
#
#
# # cap = re.findall(r'"text"\s*:\s*"(.+?)"', str(respData))
#
# dataList = []
# link = "http://www.srmuniv.ac.in/faculty-directory/b"
# count = 0
#
# data = req.Request(link)
# resp = req.urlopen(data)
# respData = resp.read()
# remList = {r'<[td,span,img](.*?)>': '', '</[b,t](.*?)>': '--', r'<[a,b](.*?)>': '\n', 'class="(.*?)"': '',
#            '<(/h,h)(.*?)>': '**', '\\\\xc2\\\\xa0': '', '<!--(.*?)-->': ''}
# remList2 = {r'</t(.*?)>|<t(.*?)>|&nbsp;|<strong(.*?)>|</strong>|<a (.*?)>|</a>|<!--(.*?)|(.*?)-->': '',
#             '</h(.*?)>|<h(.*?)>': '*',
#             r'</span(.*?)>|<span(.*?)>|<b>|</b>': '*', r'<img (.*?)>|<div(.*?)>|</div>': '', r'\\xc2\\xa0': '',
#             '<p(.*?)>|</p>|<br />': '\n'}
#
# dat = re.findall(r'<tbody>(.*?)</tbody>', str(respData))
#
# for inf in dat:
#     inf = str(inf).replace('\\n', '').replace('\\t', '')
#     img = re.findall(r'<img (.*?)/>', str(inf))
#     for rem in remList2:
#         inf = re.sub(rem, remList2[rem], inf).replace('\n\n', '')
#     try:
#         img = re.findall('src="(.*?)"', img[0])[0]
#     except IndexError:
#         img = ''
#     dataList.append({"id": count, "data": inf, "image": img})
#     id+=1
#
# with open('data.json', 'w') as outfile:
#     simplejson.dump(dataList, outfile, indent=4, sort_keys=True)
#
