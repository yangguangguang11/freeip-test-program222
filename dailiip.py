from lxml import etree
import urllib3
import requests


#爬取ip
def school(i, k):
    manager = urllib3.PoolManager()
    http = manager
    print("第"+str(i)+"页")
    r = http.request(
        'GET',
        "https://ip.jiangxianli.com/?page=" + str(i),
        headers={
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
            'Host': "ip.jiangxianli.com",
            'Cookie': "PSTM=1607346916; BIDUPSID=69AFB78A1A2E7FC19402DB7E41C448A8; BAIDUID=0A9A83EB086E30AD2E7AE714FAEF98A8:FG=1; __yjs_duid=1_b16d973dfef393feee90346dbe82f0d51619579133037; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; ab_sr=1.0.0_MTU2NjJhNzIwOWMzM2EyNjM4NmZhOGNhOWQxYzI5YTAwZDQ1MmI3M2Y0NjE0NTY5MmJjMjFhMTQ5ODIzNzU2NzVhM2FlYTg4OWQ1OGNjYzI0YjQ4ODIwM2ExYWQ0OGQz; BDRCVFR[CfxpvPKvC2b]=mk3SLVN4HKm; delPer=0; PSINO=1; BDUSS=cweXRYaUlCSklGWFBoeG5VS3QyZERZdEpMYUR4Y1pjeW50ZWdhZm53MndoYjFnRUFBQUFBJCQAAAAAAAAAAAEAAABlbIWtstDR9LK7wM~QxAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALD4lWCw-JVgQj; BDUSS_BFESS=cweXRYaUlCSklGWFBoeG5VS3QyZERZdEpMYUR4Y1pjeW50ZWdhZm53MndoYjFnRUFBQUFBJCQAAAAAAAAAAAEAAABlbIWtstDR9LK7wM~QxAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALD4lWCw-JVgQj; BDRCVFR[pNjdDcNFITf]=mk3SLVN4HKm; H_PS_PSSID=33985_33966_31254_34004_33759_33675_33607_26350_33996; BA_HECTOR=a48g810h8k810124f01g9bvg30r"
        },
        timeout=4.0
    )
    html = r.data.decode('utf-8', 'ignore')
    _element = etree.HTML(html)
    text = _element.xpath("//tbody/tr[" + str(k) + "]/td[1]/text()")
    port = _element.xpath("//tbody/tr[" + str(k) + "]/td[2]/text()")
    coun = _element.xpath("//tbody/tr[" + str(k) + "]/td[6]/text()")
    su = _element.xpath("//tbody/tr[" + str(k) + "]/td[8]/text()")
    ipdata = '\n'.join(text)
    port2 = '\n'.join(port)
    coun2 = '\n'.join(coun)
    su2 = '\n'.join(su)
    ipt=ipdata+":"+str(port2)
    ipo=ipdata+":"+str(port2)+"---------->"+coun2+"---------->"+su2
    print(ipo)
    return ipt
#检测代理是否可用
def check_proxy():
    for ip in open('ip.txt'):
        ip_port = ip.replace('\n', '')
        proxy = {
            'https': ip_port
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        }
        try:
            r = requests.get('http://www.baidu.com', headers=headers, proxies=proxy, timeout=3)
            if r.status_code == 200:
                print(ip_port+'----验证成功')
                with open(r'ok.txt', 'a+', encoding='utf-8') as a:
                    a.write(ip_port + '\n')
                    a.close()
        except:
            print(ip_port+'----超时')
#介绍
def title():
    print('+------------------------------------------')
    print('+  \033[1;34m所有数据来源:https://ip.jiangxianli.com                                 \033[0m')
    print('+  \033[1;34mTitle: ip代理验证v1.0                                       \033[0m')
    print('+  \033[1;36m使用格式:  python3 ipdaili.py                                            \033[0m')
    print('+  \033[1;36m作者By         >>>  11阳光                             \033[0m')
    print('+  \033[1;33m座右铭:不是杰出者才做梦，而是善梦者才杰出。\033[0m')
    print('+------------------------------------------')
#主函数
if __name__ == '__main__':
    title()
    page=str(input("\033[1;35m请输入你想爬的页数，一页15个ip,爬取的ip会存在ip.txt里面\npage >>> \033[0m"))
    for i in range(1, int(page)+1):
        for k in range(1, 16):
            text2=school(i,k)
            print(text2)
            with open(r'ip.txt','a+',encoding='utf-8') as f:
                f.write(text2+'\n')
                f.close()
    print('+  \033[1;33mip爬取完毕，下面将进行验证是否可用，可用的将被放在ok.txt,祝您旅途愉快！\033[0m')
    check_proxy()
    print('+  \033[1;33m完毕，快去ok.txt查看吧\033[0m')