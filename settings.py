# Scrapy settings for projectwebscrapy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'projectwebscrapy'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['projectwebscrapy.spiders']
NEWSPIDER_MODULE = 'projectwebscrapy.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = [
    'projectwebscrapy.pipelines.ProjectwebscrapyPipeline',
]

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "projectcraigslist"
MONGODB_COLLECTION = "articles"
