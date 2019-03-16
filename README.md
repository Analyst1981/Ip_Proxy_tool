# Ip_Proxy_tool
获取代理,,建立代理池，提供ip网络接口
# Ip_Proxy_tool

## 安装

### 安装Python

至少Python3.5以上

### 安装mysql

安装好之后将mysql服务开启

### 配置代理池

```
cd Ip_Proxy_tool
```

进入Ip_Proxy_tool目录，修改settings.py文件

修改mysql 用户名 密码

#### 安装依赖

```
pip3 install -r requirements.txt
```

#### 首先建立数据库表
python CreateTable.py

#user='root', passwd='toor', db='spiders'
 注意此处的数据库、用户名和密码

其次，打开代理池和API

python run.py

## 获取代理

利用requests获取方法代理的实例



```python get_proxy_example.py
具体如下
def get_proxy():
    r = requests.get('http://127.0.0.1:5555/random')
    soup = BeautifulSoup(r.text, "lxml")
    trs=soup.find("div",id="container").find_all("tr")
    for tr in trs[1:]:
        IP = tr.find_all("td")[0].get_text()
        PORT = tr.find_all("td")[1].get_text()
    proxies = {
        'http': 'http://' +IP+":"+PORT,
        'https': 'https://' +IP+":"+PORT
    }    
    return proxies
```
如果需要添加别的一些代理网站，可以修改 crawler.py 
