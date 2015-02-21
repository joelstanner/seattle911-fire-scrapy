# -*- coding: utf-8 -*-

# Scrapy settings for seattle911 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'seattle911'

SPIDER_MODULES = ['seattle911.spiders']
NEWSPIDER_MODULE = 'seattle911.spiders'

DOWNLOAD_DELAY = 6

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'seattle911 project for codefellows.org SEA-D31 (+http://www.codefellows.com)'
