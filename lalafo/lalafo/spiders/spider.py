import scrapy

class TopazGames(scrapy.Spider):
    name = "products"

    def start_requests(self):
        urls = [
            "https://lalafo.az/"    
                    ]


        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for card in response.xpath("//div/div/div/div/section/div/div[@class='row']/div/article"):
            
            yield {
                'link':card.xpath("div/a").attrib['href'],
                "image_link": card.xpath("div/div[@class='adTile-image']/picture/source/@srcset").getall(),
                'price':card.xpath("div/p/span/text()").getall()[0],
                "description":card.xpath("div/div[@class='adTile-title__wrap']/a/text()").getall()[0]
            }

