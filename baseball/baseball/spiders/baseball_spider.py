from scrapy import Spider
from scrapy.selector import Selector
from baseball.items import BaseballItem


class BaseballSpider(Spider):
    name = "baseball"
    allowed_domains = ["baseball-reference.com"]
    start_urls = [
        "https://www.baseball-reference.com/leagues/MLB/2017.shtml",
    ]

    def parse(self, response):
	team_stats = Selector(response).xpath('//*[@id="teams_standard_batting"]/tbody[1]/tr')

	for team_stat in team_stats:
	    item = BaseballItem()
	    item['team'] = team_stat.xpath('th/a/text()').extract()
            item['average_bat_age'] = team_stat.xpath('td[2]/text()').extract()
            item['runs_per_game'] = team_stat.xpath('td[3]/text()').extract()
            item['games'] = team_stat.xpath('td[4]/text()').extract()
            item['PA'] = team_stat.xpath('td[5]/text()').extract()
            item['AB'] = team_stat.xpath('td[6]/text()').extract()
            item['runs'] = team_stat.xpath('td[7]/text()').extract()
            item['hits'] = team_stat.xpath('td[8]/text()').extract()
            item['doubles'] = team_stat.xpath('td[9]/text()').extract()
            item['triples'] = team_stat.xpath('td[10]/text()').extract()
            item['HR'] = team_stat.xpath('td[11]/text()').extract()
            item['RBI'] = team_stat.xpath('td[12]/text()').extract()
            item['SB'] = team_stat.xpath('td[13]/text()').extract()
            item['CS'] = team_stat.xpath('td[14]/text()').extract()
            item['BB'] = team_stat.xpath('td[15]/text()').extract()
            item['SO'] = team_stat.xpath('td[16]/text()').extract()
            item['BA'] = team_stat.xpath('td[17]/text()').extract()
            item['OBP'] = team_stat.xpath('td[18]/text()').extract()
            item['SLG'] = team_stat.xpath('td[19]/text()').extract()
            item['OPS'] = team_stat.xpath('td[20]/text()').extract()
            item['OPSP'] = team_stat.xpath('td[21]/text()').extract()
            item['TB'] = team_stat.xpath('td[22]/text()').extract()
            item['GDP'] = team_stat.xpath('td[23]/text()').extract()
            item['HBP'] = team_stat.xpath('td[24]/text()').extract()
            item['SH'] = team_stat.xpath('td[25]/text()').extract()
            item['SF'] = team_stat.xpath('td[26]/text()').extract()
            item['LOB'] = team_stat.xpath('td[28]/text()').extract()
	    yield item
