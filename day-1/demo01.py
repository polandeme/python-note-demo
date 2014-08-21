#2014/8/20 15:42:22
import urllib2
contents = urllib2.urlopen("http://www.baidu.com").readlines()
for line in contents:
    print line + "<br>"
    
