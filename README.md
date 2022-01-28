## Weibo Spider for *Structured address*(POI name)

## 爬取微博 *结构化地址*（POI名称）

### 项目功能 Function
设置关键词keyword（城市/疫情/人名等）、时间段date、小时间隔interval，获取https://s.weibo.com/中带定位的微博签到数据，
具体爬取内容可在items.py中查看。

##### 每次使用前登录weibo.cn检查并更新setting中的**Cookies**

### Quick start
cd {$(your project path)}/weibo
python begin.py

url构造例子：
https://s.weibo.com/weibo?q=%E6%B7%B1%E5%9C%B3&region=custom:44:3&scope=ori&suball=1&timescope=custom:2019-04-30-20:2019-05-01-00&Refer=SWeibo_box
  
 
### 输出 Output
- 微博id：微博的id，为一串数字形式
- 微博bid：微博的bid
- 用户id：user_id
- 用户昵称：screen_name
- 微博内容：微博正文
- 微博发布位置：位置微博中的发布位置
- 微博发布时间：微博发布时的时间，精确到分钟

### 使用说明
本程序的所有配置都在setting.py文件中完成，该文件位于“weibo-search\weibo\settings.py”。

### 1.下载脚本 
```bash
$ git clone https://github.com/strawmelon11/weibo-search.git
```
### 2.安装Scrapy
本程序依赖Scrapy，需要安装Scrapy和相关依赖。
```bash
$ pip install scrapy
```
### 3.安装项目依赖
```
$ pip install -r requirements.txt
```

### 4.设置cookie
settings.py中的DEFAULT_REQUEST_HEADERS中的cookie是我们需要填的值，如何获取cookie详见文末的[如何获取cookie](#如何获取cookie)

### 5.设置搜索关键词
修改setting.py文件夹中的KEYWORD_LIST参数。
如果你想搜索一个关键词，如“深圳”：
```
KEYWORD_LIST = ['深圳']
```
如果你想分别搜索多个关键词，如想要分别获得“深圳”和“机场”的搜索结果：
```
KEYWORD_LIST = ['深圳', '机场']
```
如果你想搜索同时包含多个关键词的微博，如同时包含“深圳”和“机场”微博的搜索结果：
```
KEYWORD_LIST = ['深圳 机场']
```
如果你想搜索微博话题，即包含#的内容，如“#深圳#”：
```
KEYWORD_LIST = ['#深圳#']
```
也可以把关键词写进txt文件里，然后将txt文件路径赋值给KEYWORD_LIST，如：
```
KEYWORD_LIST = 'keyword_list.txt'
```
txt文件中每个关键词占一行。

### 6.设置搜索时间范围
START_DATE代表搜索的起始日期，END_DATE代表搜索的结束日期
```
START_DATE = '2020-06-01'
END_DATE = '2020-06-02'
```
### 7.设置结果保存类型（可选）
ITEM_PIPELINES是我们可选的结果保存类型，第一个代表去重，第二个代表写入csv文件，第三个代表写入MySQL数据库，第四个代表写入MongDB数据库。

### 8.设置等待时间（可选）
DOWNLOAD_DELAY代表访问完一个页面再访问下一个时需要等待的时间，默认为10秒。如我想设置等待15秒左右，可以修改setting.py文件的DOWNLOAD_DELAY参数：
```
DOWNLOAD_DELAY = 15
```

### 9.设置微博类型（可选）
WEIBO_TYPE筛选要搜索的微博类型，0代表搜索全部微博，1代表搜索全部原创微博，2代表热门微博，3代表关注人微博，4代表认证用户微博，5代表媒体微博，6代表观点微博。比如我想要搜索全部原创微博，修改setting.py文件的WEIBO_TYPE参数：
```
WEIBO_TYPE = 1
```

### 10.设置包含内容（可选）
CONTAIN_TYPE筛选结果微博中必需包含的内容，0代表不筛选，获取全部微博，1代表搜索包含图片的微博，2代表包含视频的微博，3代表包含音乐的微博，4代表包含短链接的微博。比如我想筛选包含图片的微博，修改setting.py文件的CONTAIN_TYPE参数：
```
CONTAIN_TYPE = 1
```

### 11.筛选微博发布地区（可选）
REGION筛选微博的发布地区，精确到省或直辖市，值不应包含“省”或“市”等字，如想筛选北京市的微博请用“北京”而不是“北京市”，想要筛选安徽省的微博请用“安徽”而不是“安徽省”，可以写多个地区，具体支持的地名见region.py文件，注意只支持省或直辖市的名字，省下面的市名及直辖市下面的区县名不支持，不筛选请用”全部“。比如我想要筛选发布地在山东省的微博：
```
REGION = ['山东']
```

### 12.配置数据库（可选）
MONGO_URI是MongoDB数据库的配置；<br>
MYSQL开头的是MySQL数据库的配置。

### 13.运行程序
```bash
$ scrapy crawl search -s JOBDIR=crawls/search
```


## 如何获取cookie
1.用Chrome打开<https://passport.weibo.cn/signin/login>；<br>
2.输入微博的用户名、密码，登录，如图所示：
![](https://picture.cognize.me/cognize/github/weibospider/cookie1.png)
登录成功后会跳转到<https://m.weibo.cn>;<br>
3.按F12键打开Chrome开发者工具，在地址栏输入并跳转到<https://weibo.cn>，跳转后会显示如下类似界面:
![](https://picture.cognize.me/cognize/github/weibospider/cookie2.png)
4.依此点击Chrome开发者工具中的Network->Name中的weibo.cn->Headers->Request Headers，"Cookie:"后的值即为我们要找的cookie值，复制即可，如图所示：
![](https://picture.cognize.me/cognize/github/weibospider/cookie3.png)
