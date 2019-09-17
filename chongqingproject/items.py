# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChongqingprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
#企业及资质信息
class CompanyInformationItem(scrapy.Item):
	collection = "companyinformation"
	company_id = scrapy.Field()
	name = scrapy.Field()
	reg_address = scrapy.Field()
	leal_person = scrapy.Field()
	social_credit_code = scrapy.Field()
	regis_type = scrapy.Field()
	enginer = scrapy.Field()
	registered_capital = scrapy.Field()
	postalcode = scrapy.Field()
	department = scrapy.Field()
	danweitype = scrapy.Field()
	url = scrapy.Field()
	contact_person = scrapy.Field()
	mark = scrapy.Field()
	aptitude_num = scrapy.Field()
	aptitude_type_b = scrapy.Field()
	aptitude_type_s = scrapy.Field()
	aptitude_level = scrapy.Field()
	aptitude_ser = scrapy.Field()
	aptitude_useful_date = scrapy.Field()
	create_time = scrapy.Field()
	modification_time = scrapy.Field()
	is_delete = scrapy.Field()
	aptitude_speciality = scrapy.Field()
	general_manager = scrapy.Field()
	tech_lead = scrapy.Field()
	lab_manager = scrapy.Field()
	tel = scrapy.Field()
	build_date = scrapy.Field()
	fax = scrapy.Field()
	phone = scrapy.Field()
	approval_number = scrapy.Field()
	zjgcs_sum = scrapy.Field()
	zjy_sum = scrapy.Field()
	gjzc_sum = scrapy.Field()
	zjzc_sum = scrapy.Field()
	aptitude_accept_date = scrapy.Field()




class PersonInformationItem(scrapy.Item):
	collection = "personinformation"
	name = scrapy.Field()
	major = scrapy.Field()
	title_level = scrapy.Field()
	person_type = scrapy.Field()
	company_name = scrapy.Field()
	create_time = scrapy.Field()
	modification_time = scrapy.Field()
	is_delete = scrapy.Field()
	mark = scrapy.Field()
	person_genre = scrapy.Field()
	credential_num = scrapy.Field()
	sex = scrapy.Field()


	