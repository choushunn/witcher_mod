import scrapy

from Witcher_mod.items import WitcherModItem


class WitcherSpider(scrapy.Spider):
    name = 'witcher'
    allowed_domains = ['www.3dmgame.com']
    start_urls = ['https://www.3dmgame.com/games/witcher3/resource/']

    def parse(self, response):
        item = WitcherModItem()
        data = response.xpath("/html//div[@class='Llis_4']//li")
        for each in data:
            item['name'] = each.xpath(".//a/text()").extract()[0]
            item['url'] = each.xpath(".//a/@href").extract()[0]
            item['size'] = each.xpath(".//span/text()").extract()[0]
            yield item
        try:
            next_page = response.xpath("/html//div[@class='pagewrap']//li[@class='next']/a/@href").extract()[0]
            print(next_page)
            if next_page is not None:
                # 下一页
                yield response.follow(next_page, callback=self.parse)
        except:
            print("over")
