import numpy as np
import requests as rs
from lxml import etree
import os

if __name__ == '__main__':
    url = 'http://www.win4000.com/mt/dengziqi.html'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }
    if not os.path.exists('./邓紫棋图片'):
        os.mkdir('./邓紫棋图片/') #目录文件
    picture = rs.get(url=url,headers=headers).text
    #print(picture)
    picture_tree = etree.HTML(picture)
    picture_li = picture_tree.xpath('//div[@class="tab_box"]//ul/li')
    print(picture_li)
    # for li in picture_li:
    #     li_image = li.xpath('./a/img/@src')[0]#将列表转化为值
    #     li_path = li.xpath('./a/img/@alt')[0]+'.jpg'
    #     image_get = rs.get(url=li_image,headers=headers).content
    #     image_path = './邓紫棋图片/'+li_path
    #     with open(image_path,'wb') as bp:
    #         bp.write(image_get)
    #         print(li_path+'下载成功')
