import scrapy


class GdpDebtSpider(scrapy.Spider):
    name = 'gdp_debt'
    allowed_domains = ['www.worldpopulationreview.com']
    start_urls = ['http://www.worldpopulationreview.com/countries/countries-by-national-debt']

    def parse(self, response):
        linhas = response.xpath('//tbody[@class="jsx-2006211681"]/tr')
        for linha in linhas:
            yield{
                'country_name':linha.xpath('.//td/a/text()').get(),
                'debt':linha.xpath('.//td[2]/text()').get(),
                'population':linha.xpath('.//td[3]/text()').get()
            }