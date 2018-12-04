# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item,Field

class BaseballItem(Item):
    team=Field()
    average_bat_age = Field()
    runs_per_game=Field()
    games = Field()
    PA = Field()
    AB = Field()
    runs = Field()
    hits=Field()
    doubles = Field()
    triples = Field()
    HR = Field()
    RBI = Field()
    SB = Field()
    CS = Field()
    BB = Field()
    SO = Field()
    BA = Field()
    OBP = Field()
    SLG = Field()
    OPS = Field()
    OPSP = Field()
    TB = Field()
    GDP = Field()
    HBP = Field()
    SH = Field()
    SF = Field()
    LOB = Field()
    
