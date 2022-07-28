# -*- coding: utf-8 -*-
import scrapy


class SpedSpider(scrapy.Spider):
    name = 'Sped'
    start_urls = ['http://sped.rfb.gov.br/']

    def parse(self, response):
      for article in response.css("section"):
        link    = 'http://sped.rfb.gov.br/' + article.css("h2 a::attr(href)").extract_first()
        titulo  = article.css("h2 a::text").extract_first()
        data    = article.css("p.data::text").extract_first()

        yield {'link': link, 'titulo': titulo, 'data': data}