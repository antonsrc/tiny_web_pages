r'''name: tiny_web_pages
ver: 0.20220722
descr: static site generator on python
aurhor: Moshnyakov Anton (anton.source@gmail.com)
'''

import os
import shutil
import sys

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

for param in sys.argv:
    if param == '-r':
        ADDRESS = r'http://antonsrc.github.io/'
    else:
        abspath = os.path.abspath('.').replace('\\', '/')
        ADDRESS = r'file:///' + abspath + r'/website/'

HTMLFORM = '''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="utf-8">
    <title>{0}</title>
    <link rel="stylesheet" type="text/css" href="{1}data/mainpage.css">
</head>
<body>
<div class="maintext">
{2}
</div>
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
        f.write(HTMLFORM.format(header, ADDRESS, add_tag_p(content)))
        f.close()

shutil.copytree('data', r'website/data', dirs_exist_ok=True)
