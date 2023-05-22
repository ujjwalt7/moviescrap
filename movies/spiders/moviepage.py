import scrapy


class MoviepageSpider(scrapy.Spider):
    name = "moviepage"
    allowed_domains = ["membed1.com","movembed.cc"]
    start_urls = ["https://membed1.com/"]
    
    def start_requests(self):
        yield scrapy.Request(f'https://membed1.com/{self.page}')

    # def parse(self, response):
    #     url = '/videos/rabbit-hole-season-1-episode-1'
    #     yield response.follow(url=url,callback=self.movieextract)



    def parse(self,response):
    # def movieextract(self,response):
        item = response.css("div.main-content div.video-info")
        epsList = item.css('h3.list_episdoe+ul.listing li.video-block')
        e = []
        for eps in epsList:
            e.append( {
                'title':eps.css("div.name::text").get().replace('\n',"").strip(),
                'link':eps.css("a").attrib['href'][1:],
                # 'link':response.urljoin(eps.css("a").attrib['href']),
                'img':eps.css("div.picture img").attrib['src'],
                'meta':eps.css("div.meta span.date::text").get()
            })
        
        data =  {
            'title':item.css('h1::text').get(),
            'videourl':item.css('div.watch_play div.play-video iframe').attrib['src'].replace('//',""),
            'description':item.css('div.video-details div.content-more-js::text').get().replace('\t',""),
            'eps':e,
        }
        yield scrapy.Request(url=('https://'+data["videourl"]),callback=self.getVideosData,meta={'data':data})

    def getVideosData(self,response):
        print('-------------------------------------')
        # print(response.meta['data'])
        tempdata = response.meta['data']
        item = response.css("div.videocontent")
        linklist = item.css('div#list-server-more ul.list-server-items li.linkserver')
        links=[]
        for l in linklist:
            links.append( {
                'video-title':l.css('::text').get(),
                'video-data':l.attrib['data-video'],
            })
        data = { **tempdata,'video-links':links}
        yield data
