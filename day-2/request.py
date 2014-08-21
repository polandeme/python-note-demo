# 发送get请求
import urllib
import urllib2

url = 'http://www.zhihu.com/lastread/touch'

data = {}
data['word'] = '爬虫'
data['tn'] = '99984161_hao_pg'

value = urllib.urlencode(data)
print value 
url = 'http://www.baidu.com/s?' + value
response = urllib2.urlopen(url)
the_page =  response.read()
print the_page
