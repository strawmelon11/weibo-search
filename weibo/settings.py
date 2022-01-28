# -*- coding: utf-8 -*-

from datetime import datetime

BOT_NAME = 'weibo'
SPIDER_MODULES = ['weibo.spiders']
NEWSPIDER_MODULE = 'weibo.spiders'
COOKIES_ENABLED = False
TELNETCONSOLE_ENABLED = False
# LOG_LEVEL = 'ERROR'
# 访问完一个页面再访问下一个时需要等待的时间，默认为10秒
DOWNLOAD_DELAY = 2
# 需要定期更换cookie
DEFAULT_REQUEST_HEADERS = {
    'Accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
    'cookie': ''  # your cookie
}
ITEM_PIPELINES = {
    'weibo.pipelines.DuplicatesPipeline': 300,
    # 'weibo.pipelines.CsvPipeline': 301,
    # 'weibo.pipelines.MysqlPipeline': 302,
    'weibo.pipelines.MongoPipeline': 303,
    # 'weibo.pipelines.MyImagesPipeline': 304,
    # 'weibo.pipelines.MyVideoPipeline': 305
}

# url的构造结构
# https://s.weibo.com/weibo?q=%E6%B7%B1%E5%9C%B3&region=custom:44:3&scope=ori&suball=1&timescope=custom:2019-04-30-20:2019-05-01-00&Refer=SWeibo_box

# 要搜索的关键词列表，可写多个, 值可以是由关键词或话题组成的列表，也可以是包含关键词的txt文件路径，
# 如'keyword_list.txt'，txt文件中每个关键词占一行
KEYWORD_LIST = ['深圳']

# 或者 KEYWORD_LIST = 'keyword_list.txt'
# 要搜索的微博类型，0代表搜索全部微博，1代表搜索全部原创微博，2代表热门微博，3代表关注人微博，4代表认证用户微博，5代表媒体微博，6代表观点微博
WEIBO_TYPE = 1
# 筛选结果微博中必需包含的内容，0代表不筛选，获取全部微博，1代表搜索包含图片的微博，2代表包含视频的微博，3代表包含音乐的微博，4代表包含短链接的微博
CONTAIN_TYPE = 0
# 筛选微博的发布地区，精确到省或直辖市，值不应包含“省”或“市”等字，如想筛选北京市的微博请用“北京”而不是“北京市”，想要筛选安徽省的微博请用“安徽”而不是“安徽省”，可以写多个地区，
# 具体支持的地名见region.py文件，注意只支持省或直辖市的名字，省下面的市名及直辖市下面的区县名不支持，不筛选请用”全部“
REGION = ['深圳']
# 从region.py查询城市code,按字符串格式填写（'省:市区'。如深圳：'44:3'; 北京海淀'11:3'）
REGION_CODE='44:3'
# # 搜索的起始日期，为yyyy-mm-dd形式，搜索结果包含该日期
# START_DATE = '2019-10-01'
# # 搜索的终止日期，为yyyy-mm-dd形式，搜索结果包含该日期
# END_DATE = '2020-10-28'
# 搜索的起始日期，为yyyy-mm-dd形式，搜索结果包含该日期
START_DATE = '2021-01-01'
# 搜索的终止日期，为yyyy-mm-dd形式，搜索结果包含该日期
END_DATE = '2021-12-31'
# 图片文件存储路径
IMAGES_STORE = './'
# 视频文件存储路径
FILES_STORE = './'
# 配置MongoDB数据库
MONGO_URI = 'localhost'
# 配置MySQL数据库，以下为默认配置，可以根据实际情况更改，程序会自动生成一个名为weibo的数据库，如果想换其它名字请更改MYSQL_DATABASE值
# MYSQL_HOST = 'localhost'
# MYSQL_PORT = 3306
# MYSQL_USER = 'root'
# MYSQL_PASSWORD = '123456'
# MYSQL_DATABASE = 'weibo'
# Mongodb 数据库名
DB_NAME = 'DB'
# 数据集名称
COLLECTION_NAME = 'COLLECTION'
# 文件及路径，log目录需要先建好
today = datetime.now()
log_file_path = "log/scrapy_{}_{}_{}.log".format(today.year, today.month, today.day)

# 日志输出
LOG_LEVEL = 'INFO'
LOG_FILE = log_file_path

