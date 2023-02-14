# 模块导入

import requests  #pip install requests

import parsel
import tomd
import  re

# 把文章保存成markdown格式

def download_article(article_url):
    response = requests.get(article_url)
    html = response.text
    print(html)

    # 把网页变成css选择器
    # 解析网页数据
    sel = parsel.Selector(html)
    title = sel.css('.title-article::text').get()
    content = sel.css('article').get()

    # text = tomd.Tomd(content).markdown
    # text = re.sub('<a.*?a>',"",text)  #正则表达式
    # 提取文章的内容与格式
    print(title)
    print(content)

    # with open(title + '.md',mode='w',encoding='utf-8') as f:
    #     f.write("#"+title)
    #     f.write(text)

# 博客地址u'r'l,填入即可
# article_url = 'https://blog.csdn.net/weixin_44048823/article/details/90247052'
article_url = "https://blog.csdn.net/m0_57448314/article/details/127347051"
download_article(article_url)