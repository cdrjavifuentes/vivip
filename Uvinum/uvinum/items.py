# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UvinumItem(scrapy.Item):
    # define the fields for your item here like:
    
    cellar = scrapy.Field()
    store = scrapy.Field()
    category = scrapy.Field()
    name = scrapy.Field()
    source = scrapy.Field()
    precio = scrapy.Field()
    anada = scrapy.Field()
    tipo = scrapy.Field()
    puntuacion = scrapy.Field()
    do = scrapy.Field()
    volumen = scrapy.Field()
    tipouvas = scrapy.Field()
    alcohol = scrapy.Field()
    alergenos = scrapy.Field()
    notadecata = scrapy.Field()
    
    