import scrapy
from ..items import TripadvisorItem


class ComentariosSpider(scrapy.Spider):
    name = 'comentarios'
    allowed_domains = ['tripadvisor.com.br']
    start_urls = [
        'https://www.tripadvisor.com.br/Hotel_Review-g2572278-d3139700-Reviews-Hotel_Sesc_Triunfo-Triunfo_State_of_Pernambuco.html#REVIEWS']

    def parse(self, response):
        item = TripadvisorItem()
        comments_box = response.xpath(
            "//div[@class='cWwQK MC R2 Gi z Z BB dXjiy']")

        for box in comments_box:
            item["comment_author"] = box.xpath(
                ".//div[@class='bcaHz']/span/a/text()").get()
            item["address_author"] = box.xpath(
                ".//span[@class='default ShLyt small']/text()").get()
            item["title_comment"] = box.xpath(
                ".//div[@class='fpMxB MC _S b S6 H5 _a']/a/span/span/text()").get()
            item["body_comment"] = box.xpath(
                ".//div[@class='pIRBV _T']/q/span/text()").get()
            item["data_comment"] = box.xpath(
                ".//span[@class='euPKI _R Me S4 H3']/text()").get()
            yield item

        next_page = response.xpath(
            "//a[@class='ui_button nav next primary ' and text() = 'Próximas']/@href").get()
        if next_page:
            yield response.follow(url=next_page, callback=self.parse)
