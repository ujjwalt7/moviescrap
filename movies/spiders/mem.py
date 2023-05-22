import scrapy


class MemSpider(scrapy.Spider):
    name = "mem"
    allowed_domains = ["membed1.com","movembed.cc"]
    # start_urls = ["https://membed1.com/"]
    global categ
    def start_requests(self):
        # yield scrapy.Request(f'https://membed1.com/{categ}')
        yield scrapy.Request(f'https://membed1.com/{self.cat}')

    def parse(self, response):
        print('-------------------Yo--------------------')
        items = response.css('li.video-block')

        for item in items:
            yield {
                'title':item.css("div.name::text").get().replace('\n',"").strip(),
                'link':item.css("a").attrib['href'][1:],
                # 'link':response.urljoin(item.css("a").attrib['href']),
                'img':item.css("div.picture img").attrib['src'],
                'meta':item.css("div.meta span.date::text").get()
            }

        