response.css('.country-box h6::text').get()
response.css('.country-box a::attr(href)').get()
response.css('.job-title h3::text').get()
#scholarship data 


main_selector = response.css("div.single-job").getall()
scholarship_name =  response.css('.job-title h3::text').get()
deadline = response.css('.job-dates p:nth-child(2)::text').get()
degree = response.css('.info-bottom p:nth-child(2) span::text').get()
university_name =  response.xpath("//div[@class='job-list']/ul/li/div[@class='list-col'][3]/text()").get()
level = response.xpath("//div[@class='job-list']/ul/li[3]/div[@class='list-col'][3]/text()").get()
country = response.xpath("//div[@class='job-list']/ul/li[7]/div[@class='list-col'][3]/text()").get()




----------------------------------------------------------------------
level =  response.xpath("//div[@class='sch_title']//span[@class='otherp'][1]/text()").get(default='').strip()
course = response.xpath("//div[@class='sch_title']//span[@class='otherp'][2]/text()").get(default='').strip()
----------------------------------------------------------------------------
scholarship_name =  response.xpath('//div[@class="sch_title"]/text()').get(default='').strip()
scholarship_text = scholarship_name.replace('\xa0',' ')
-------------------------------------------------------------------------
deadline = response.css('div.sch_country strong::text').get()
university = response.xpath('normalize-space(//p[strong="University or Organization:"]/text())').get()
university_text = university.replace('\xa0',' ')
------------------------------------------------------------------------
country = response.xpath('normalize-space(//p[strong="The award can be taken in the\xa0"]/text())').get()
response.css('div.sch_country small:nth-child(1)::text').get()


----------------------------------------------------------------------------------
scholarship_name = response.css("div.job-title h3::text").get()
deadline = response.css("p.last-date::text").get()
response.css("div.info-bottom p:nth-child::text").get()
level = response.css("div.info-bottom span::text").get()
field = response.xpath("/html/body/main/section[2]/div/div/div[1]/div[1]/div[2]/div[5]/div[1]/div/div[2]/p[2]/span/text()").get()
university_name = response.xpath("/html/body/main/section[2]/div/div/div[1]/div[1]/div[2]/div[5]/div[2]/div[2]/ul/li[1]/div[3]/text()").get()
country = response.xpath("/html/body/main/section[2]/div/div/div[1]/div[1]/div[2]/div[5]/div[2]/div[2]/ul/li[7]/div[3]/text()").get()

response.xpath("//div[@class ='info-bottom']/p/span/tex").get()



----------------------------------------------------------------------------------------------------

a_href_for_Bachelors = response.css("div.large-4.medium-4.small-12.columns a::attr(href)").get()
Bachelors_text = response.css("h4 center::text").get()

a_href_for_Marsters = response.css("div.large-4.medium-4.small-12.columns a::attr(href)").getall()[1]
Masters_text = response.css("h4 center::text").getall()[1]

a_href_for_PHD = response.css("div.large-4.medium-4.small-12.columns a::attr(href)").getall()[2]
PHD_text = response.css("h4 center::text").getall()[2]

response.css("div.icon-text-boxes-section white-bg").getall()

response.css("section.icon-text-boxes-section.white-bg")

------------------------------------------------------------------------------------------------------
tables_data = response.css("table.table.table-sm.table-striped.table-bordered.bg-white").getall()

scholarship_name =  response.css("tr.featured a::text").get()
scholarship_link = response.css("tr.featured a::attr(href)").get()
country name = response.css("p.award-restriction:nth-of-type(2)::text").get()
description = response.css("div.award-description p::text").get()
response.css("div.clear:nth-of-type(3)::text").get()
deadline = response.css("div.clear:nth-of-type(3) p::text").get()