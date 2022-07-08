# name: tinywp (tiny web pages)
# ver: 0.20220708
# descr: static site generator on python
# aurhor: Moshnyakov Anton (anton.source@gmail.com)

import os

def read_source_dir(address_, name_):
    fileName = os.path.join(address_, name_)
    f = open(str(fileName), 'r', encoding='utf-8')
    pageData = f.readlines()
    f.close()
    return pageData

def make_site_dir(address_):
    sitePath = address_.replace('source', 'website', 1)
    if not os.path.exists(sitePath):
        os.mkdir(sitePath)
    return sitePath

def add_tag_p(data):
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
        file_name, file_ext = os.path.splitext(name)
        if file_ext != '.txt':
            continue
        header, *content = read_source_dir(address, name)
        
        if header.find('header:') == 0 or content[0].find('content:') == 0:
            header = header.replace('header:', '', 1).strip()
            content[0] = content[0].replace('content:', '', 1).lstrip()
        else:
            continue
        
        site_dir = make_site_dir(address)
        site_name = file_name + '.html'

        f_path = str(os.path.join(site_dir, site_name))
        f = open(str(f_path), 'w', encoding='utf-8')
        f.write(HTMLFORM.format(header, add_tag_p(content)))
        f.close()