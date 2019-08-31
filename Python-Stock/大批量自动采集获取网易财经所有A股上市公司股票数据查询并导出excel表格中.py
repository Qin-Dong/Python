# -*- coding: utf-8-*-
# @Date    : 2014-05-20
# @Author  : Lifemaxer
# @Website : http://lifemaxer.com
# @Description1:  python-大批量自动采集获取网易财经所有A股上市公司股票资产负债率
# @Description2:  并导入excel表格中
# @Description3:  替换下方中文可修改成获取任意财务数据
# @Tools-Required: BeautifulSoup, xlwt
import re
import urllib.request
import urllib.parse
import xlwt
from bs4 import BeautifulSoup
count = 1
class getstock:
    def __init__(self):
        pass

    def go(self):
        #定义网址，获取上交所创业板只需对应修改stock_num为6开头或3开头即可
        stock_num = str(count).zfill(6)
        url = 'http://quotes.money.163.com/f10/zycwzb_'+stock_num+',year.html'
        print(u"代码:" + stock_num)
        headers = {'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'}
        req = urllib.request.Request(url, headers = headers)
        try:
            content = urllib.request.urlopen(req).read()
        except:
            return
        soup = BeautifulSoup(content, "html.parser")
        #获取名称
        name = soup.find('h1',class_='name').contents[1].contents[0].encode('gb18030').decode('gb18030')
        print(name)
        ws.write(count, 0, stock_num)
        ws.write(count, 1, name)
        #获取负债率
        a = soup.find_all(class_='table_bg001 border_box fund_analys')
        for i in a:
            #此处替换中文可修改成获取任意财务数据
            if i.find('td class',text=re.compile(u'主营业务利润率(%)')):
               b = i.find('td',text=re.compile(u'主营业务利润率(%)')).parent.contents
               print(b)
               #网易财经默认一页最多显示2008-2013年年报共6年
               number = [3,4,5,6,7,8]
               for num in number:
                   if num < len(b):
                         data = b[num].contents[0].decode('unicode_escape')
                         ws.write(count, num-1, data)

if __name__ == '__main__':
    #定义excel表格内容
    wb = xlwt.Workbook()
    ws = wb.add_sheet(u'资产负债表')
    ws.write(0, 0, u'股票代码')
    ws.write(0, 1, u'股票名称')
    ws.write(0, 2, u'2017-12-31')
    ws.write(0, 3, u'2016-12-31')
    ws.write(0, 4, u'2015-12-31')
    ws.write(0, 5, u'2014-12-31')
    ws.write(0, 6, u'2013-12-31')
    ws.write(0, 7, u'2012-12-31')
    gs = getstock()
    #目前深证最大号为002725，获取上交所创业板请修改相应最大号码
    while count <=5:
        gs.go()
        wb.save('stockdebt.xls')
        count += 1
