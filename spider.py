#正则匹配中文[\u4e00-\u9fa5]
#http://www.blogjava.net/Skynet/archive/2009/05/02/268628.html

import urllib.request
import urllib.parse
import re 

url = 'http://zh.wikipedia.org/wiki/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E5%9F%8E%E5%B8%82%E5%88%97%E8%A1%A8'
res = urllib.request.urlopen(url).read().decode('utf-8')
p = re.compile(u">[\u4e00-\u9fa5]+<")
print(re.findall(p, res))

