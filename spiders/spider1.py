from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from projectwebscrapy.items import ProjectwebscrapyItem

class MySpider(CrawlSpider):
    name = "projectcraigs"
    allowed_domains = ["sfbay.craigslist.org"]
    start_urls = ["http://sfbay.craigslist.org/npo/"]   

    rules = (Rule (SgmlLinkExtractor(allow=("index\d00\.html", ),restrict_xpaths=('//a[@class="button next"]',))
    , callback="parse_items", follow= True),
    )

    def parse_items(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select('//span[@class="pl"]')
        items = []
        for titles in titles:
            item = ProjectwebscrapyItem()
            item ["title"] = titles.select("a/text()").extract()
            item ["link"] = titles.select("a/@href").extract()
            items.append(item)
        return(items)
