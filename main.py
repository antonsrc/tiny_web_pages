# name: tinywp (tiny web pages)
# ver: 0.1.220625
# descr: static site generator on python
# aurhor: Moshnyakov Anton (anton.source@gmail.com)

import os
import os.path

def readSource(address_, name_):
    fileName = os.path.join(address_, name_)
    f = open(str(fileName), 'r', encoding='utf-8')
    pageData = f.readlines()
    f.close()
    return pageData


def makeSiteDir(address_):
    sitePath = address_.replace('source', 'website', 1)
    if not os.path.exists(sitePath):
        os.mkdir(sitePath)
    return sitePath

def pTagConvert(data):
    joinData = ''.join(data)
    tagData = joinData.replace('\n', '</p>\n<p>')
    content = '<p>' + tagData + '</p>'
    return content

HTMLFORM = '''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <title>{0}</title>
</head>
<body>
{1}
</body>
</html>    
'''

tree = list(os.walk('.'))

for address, dirs, files in tree:
    for name in files:
        if name[-4:] != '.txt':
            continue
        header, *content = readSource(address, name)
        
        if header.find('header:') == 0 or content[0].find('content:') == 0:
            header = header.replace('header:', '', 1).strip()
            content[0] = content[0].replace('content:', '', 1).lstrip()
        else:
            continue
        
        siteAddress = makeSiteDir(address)
        siteName = name.replace('.txt', '.html')

        siteFilePath = str(os.path.join(siteAddress, siteName))
        f = open(str(siteFilePath), 'w', encoding='utf-8')

        contentPtag = pTagConvert(content)

        f.write(HTMLFORM.format(header, contentPtag))
        f.close()

# comment 5