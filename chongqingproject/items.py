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
	collection = "chongqing.companyinformation"
	province_company_id = scrapy.Field()
	social_credit_code = scrapy.Field()
	company_name = scrapy.Field()
	sourceouname = scrapy.Field()
	url = scrapy.Field()
	ceoname = scrapy.Field()
	ctoname = scrapy.Field()
	regis_address = scrapy.Field()
	leal_person = scrapy.Field()
	business_address = scrapy.Field()
	regis_type = scrapy.Field()
	registered_capital = scrapy.Field()
	build_date = scrapy.Field()
	contact_person = scrapy.Field()
	leal_person_title = scrapy.Field()
	postalcode = scrapy.Field()
	contact_phone = scrapy.Field()
	contact_address = scrapy.Field()
	tech_lead_duty = scrapy.Field()
	fax = scrapy.Field()
	tel = scrapy.Field()
	website = scrapy.Field()
	email = scrapy.Field()
	reg_address_province = scrapy.Field()
	reg_address_country = scrapy.Field()
	contact_tel = scrapy.Field()
	enginer = scrapy.Field()
	department = scrapy.Field()
	danweitype = scrapy.Field()
	area_code = scrapy.Field()
	source = scrapy.Field()
	status = scrapy.Field()
	create_time = scrapy.Field()
	modification_time = scrapy.Field()
	is_delete = scrapy.Field()

class PersonInformationItem(scrapy.Item):
	collection = "chongqing.personinformation"
	person_name = scrapy.Field()
	province_person_id = scrapy.Field()
	company_name = scrapy.Field()
	province_company_id = scrapy.Field()
	person_sex = scrapy.Field()
	nation = scrapy.Field()
	birthday = scrapy.Field()
	in_date = scrapy.Field()
	year = scrapy.Field()
	tel = scrapy.Field()
	phone = scrapy.Field()
	url = scrapy.Field()
	department = scrapy.Field()
	person_identification_type = scrapy.Field()
	person_identification_id = scrapy.Field()
	create_time = scrapy.Field()
	modification_time = scrapy.Field()
	is_delete = scrapy.Field()
	source = scrapy.Field()
	status = scrapy.Field()

class PersonCertificateItem(scrapy.Item):
	collection = "chongqing.personcertificate"
	province_person_id = scrapy.Field()
	aptitude_name = scrapy.Field()
	certificate_num = scrapy.Field()
	reg_num = scrapy.Field()
	reg_credential_num = scrapy.Field()
	certificate_useful_time = scrapy.Field()
	aptitude_accept_date = scrapy.Field()
	title = scrapy.Field()
	duty = scrapy.Field()
	worklicense_num = scrapy.Field()
	major = scrapy.Field()
	level = scrapy.Field()
	aptitude_type = scrapy.Field()
	certificate_seal_id = scrapy.Field()
	company_name = scrapy.Field()
	certificate_company_name = scrapy.Field()
	certificate_company_id = scrapy.Field()
	create_time = scrapy.Field()
	modification_time = scrapy.Field()
	is_delete = scrapy.Field()
	source = scrapy.Field()
	status = scrapy.Field()
	person_name = scrapy.Field()

class AptitudeItem(scrapy.Item):
	collection = "chongqing.companyaptitude"
	province_company_id = scrapy.Field()
	aptitude_id = scrapy.Field()
	aptitude_organ = scrapy.Field()
	aptitude_startime = scrapy.Field()
	aptitude_endtime = scrapy.Field()
	aptitude_name = scrapy.Field()
	level = scrapy.Field()
	check_time = scrapy.Field()
	aptitude_small = scrapy.Field()
	aptitude_credit_level = scrapy.Field()
	aptitude_major = scrapy.Field()
	aptitude_large = scrapy.Field()
	aptitude_ser = scrapy.Field()
	approval_number = scrapy.Field()
	aptitude_usefultime = scrapy.Field()
	aptitude_type = scrapy.Field()
	source = scrapy.Field()
	status = scrapy.Field()
	create_time = scrapy.Field()
	modification_time = scrapy.Field()
	is_delete = scrapy.Field()
	company_name = scrapy.Field()

class BeianItem(scrapy.Item):
	collection = "province.beianinformation"
	company_name = scrapy.Field()
	social_credit_code = scrapy.Field()
	record_province = scrapy.Field()
	status = scrapy.Field()
	create_time = scrapy.Field()
	modification_time = scrapy.Field()
	is_delete = scrapy.Field()



