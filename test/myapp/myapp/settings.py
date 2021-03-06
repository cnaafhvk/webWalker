# -*- coding:utf-8
# 这个配置文件包含所有爬虫所需要的配置信息
# 使用自定义的localsettings.py可以重写配置信息
# Web Walker Settings
# ~~~~~~~~~~~~~~~~~~~~~~~
import pkgutil
# ~~~~~~~~~~~~~~~~~~~~~~~


# Redis host and port
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379

CUSTOM_REDIS = True

RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 408, 403, 304]

CONCURRENT_REQUESTS = 4
CONCURRENT_REQUESTS_PER_DOMAIN = 4
CONCURRENT_REQUESTS_PER_IP = 4

# 自带了一些user_agents，推荐不改
USER_AGENT_LIST = pkgutil.get_data('walker', 'user_agents.list')

# 对于有去重需求的分类链接，去重的超时时间，默认3600s
# 如果该分类抓取完毕需要很长时间，中间还有可能关闭，那这个时间需要长一点
DUPLICATE_TIMEOUT = 60*60

# 代理密码，没有就可空
PROXY_PASSWORD = ""

# 重试次数
RETRY_TIMES = 20

# 使用代理时需要提供代理文件，需要改
# PROXY_LIST = pkgutil.get_data('myapp', 'proxy.list')

# 重定向次数
REDIRECT_MAX_TIMES = 20

# 每次重定向优先级调整
REDIRECT_PRIORITY_ADJUST = -1

# 日志配置
SC_LOG_LEVEL = 'DEBUG'
SC_LOG_TYPE = "CONSOLE"
SC_LOG_JSON = False
SC_LOG_DIR = "logs"
SC_LOG_MAX_BYTES = '10MB'
SC_LOG_BACKUPS = 5
KAFKA_HOSTS = '192.168.200.58:9092'
TOPIC = "log.incoming"

# 有些网站可能需要提供一些自定义的请求头
HEADERS = {
    "ashford": {
                "Cookie": "userPrefLanguage=en_US;",
                },
}


# 需要改
BOT_NAME = 'myapp'

# 需要改
SPIDER_MODULES = ['myapp.spiders']

# 需要改
NEWSPIDER_MODULE = 'myapp.spiders'

# Enables scheduling storing requests queue in redis.
SCHEDULER = "walker.scheduler.Scheduler"

# 统计抓取信息
STATS_CLASS = 'walker.stats_collectors.StatsCollector'


# Store scraped item in redis for post-processing.
ITEM_PIPELINES = {
    'walker.pipelines.JSONPipeline': 100,
    'walker.pipelines.ItemSkipPipeline': 99,
    'walker.pipelines.LoggingBeforePipeline': 1,
    'walker.pipelines.LoggingAfterPipeline': 101,
}

SPIDER_MIDDLEWARES = {
    'scrapy.contrib.spidermiddleware.depth.DepthMiddleware': None,
}

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    #'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': None,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware':None,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': None,
    #'scrapy.contrib.downloadermiddleware.cookies.CookiesMiddleware': None,
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
    'walker.downloadermiddlewares.CustomUserAgentMiddleware': 400,
    # Handle timeout retries with the redis scheduler and logger
    'walker.downloadermiddlewares.CustomRetryMiddleware': 510,
    #"walker.downloadermiddlewares.ProxyMiddleware": 511,
    # exceptions processed in reverse order
    # custom cookies to not persist across crawl requests
    'walker.downloadermiddlewares.CustomRedirectMiddleware': 600,
    'walker.downloadermiddlewares.CustomCookiesMiddleware': 700,
}

# 在生产上关闭内建logging
LOG_ENABLED = True

# http错误也会返回
HTTPERROR_ALLOW_ALL = True

# 下载超时时间
DOWNLOAD_TIMEOUT = 30

# Avoid in-memory DNS cache. See Advanced topics of docs for info
DNSCACHE_ENABLED = True


# Local Overrides
# ~~~~~~~~~~~~~~~

try:
    from localsettings import *
except ImportError:
    pass
