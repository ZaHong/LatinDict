import socket
import time
import urllib
import re
lst = list()
lst2 = list()

print 'Made by William Hong\n'
print 'Powered by William Whitakers Words\n\n\n\n\n'

while True:
    url1 = raw_input('Enter: ')
    url2 = 'http://archives.nd.edu/cgi-bin/wordz.pl?keyword=' + url1
    try:
        fhand = urllib.urlopen(url2)
    except:
        print 'No Internet Connection'
        time.sleep(5)

    for line in fhand:
        line = line.rstrip()
        words = line.split()
        for i in words:
            i = i.strip()
            if i.startswith('<href'):
                continue
            lst.append(i)
            
    lengh = len(lst)
    lengh = lengh -1
    lst2 = lst[7:lengh]
    print " ".join(lst2)
    lst = list()
    lst2 = list()