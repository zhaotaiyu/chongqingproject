# -*- coding: gbk -*-

from scrapy import Request, FormRequest
import datetime
from chongqingproject.items import *

class ChongqingSpider(scrapy.Spider):
    name = 'chongqing'
    allowed_domains = ['183.66.171.75']
    #start_urls = ['http://183.66.171.75:88/CQCollect/Qy_Query/YhzSgqy/YhzSgqy_List.aspx']
    #start_urls = ['http://183.66.171.75:88/CQCollect/Qy_Query/Ryxxbs/Rybabs_List.aspx']
    # start_urls = ['http://183.66.171.75:88/CQCollect/Qy_Query/Jlqy/Jlqy_List.aspx']
    # start_urls = ['http://183.66.171.75:88/CQCollect/Qy_Query/Jlqy/WdJlqy_List.aspx']
    # start_urls = ['http://183.66.171.75:88/CQCollect/Qy_Query/Hntqy/Hntqy_List.aspx']
    # start_urls = ['http://183.66.171.75:88/CQCollect/Qy_Query/Zbdljg/Zbdljg_List.aspx']
    # start_urls = ['http://183.66.171.75:88/CQCollect/Qy_Query/Zljcjg/Zljcjg_List.aspx']
    # start_urls = ['http://183.66.171.75:88/CQCollect/Qy_Query/Zjzxjg/Zjzxjg_List.aspx']
    # start_urls = ['http://183.66.171.75:88/CQCollect/Qy_Query/Zjzxjg/Wd_Zjzxjg_List.aspx']
    start_urls = ['http://183.66.171.75:88/CQCollect/Qy_Query/YhzSgqy/YhzSgqy_List.aspx','http://183.66.171.75:88/CQCollect/Qy_Query/Ryxxbs/Rybabs_List.aspx','http://183.66.171.75:88/CQCollect/Qy_Query/Jlqy/Jlqy_List.aspx','http://183.66.171.75:88/CQCollect/Qy_Query/Hntqy/Hntqy_List.aspx','http://183.66.171.75:88/CQCollect/Qy_Query/Zbdljg/Zbdljg_List.aspx','http://183.66.171.75:88/CQCollect/Qy_Query/Zljcjg/Zljcjg_List.aspx','http://183.66.171.75:88/CQCollect/Qy_Query/Zjzxjg/Zjzxjg_List.aspx','http://183.66.171.75:88/CQCollect/Qy_Query/Zjzxjg/Wd_Zjzxjg_List.aspx','http://183.66.171.75:88/CQCollect/Qy_Query/Jlqy/WdJlqy_List.aspx']

    def parse(self, response):
        __VIEWSTATE = response.xpath("//input[@name='__VIEWSTATE']/@value").extract_first()
        __EVENTTARGET = 'TurnPage1:LB_Next'
        # 施工企业
        if response.url == "http://183.66.171.75:88/CQCollect/Qy_Query/YhzSgqy/YhzSgqy_List.aspx":
            total_page = response.xpath("//span[@id='TurnPage1_pagecount']/text()").extract_first()
            now_page = response.xpath("//span[@id='TurnPage1_currentpage']/text()").extract_first()
            tr_list = response.xpath("//table[@id='DataGrid1']/tr")
            for tr in tr_list[1:]:
                href = tr.xpath("./td[2]/font/a/@href").extract_first().strip().split("'")[1].replace("$", ":")
                department = tr.xpath("./td[5]/font/text()").extract_first()
                formdata = {
                    '__EVENTTARGET': href,
                    '__VIEWSTATE': __VIEWSTATE
                }
                yield FormRequest(response.url, formdata=formdata, callback=self.parse_middle,
                                  meta={"department": department})
        # 外地施工入渝信息报送企业
        if response.url == "http://183.66.171.75:88/CQCollect/Qy_Query/Ryxxbs/Rybabs_List.aspx":
            total_page = response.xpath("//span[@id='TurnPage1_pagecount']/text()").extract_first()
            now_page = response.xpath("//span[@id='TurnPage1_currentpage']/text()").extract_first()
            tr_list = response.xpath("//table[@id='DataGrid1']/tr")
            for tr in tr_list[1:]:
                href = tr.xpath("./td[2]/font/a/@href").extract_first().strip().split("'")[1].replace("$", ":")
                department = tr.xpath("./td[6]/font/text()").extract_first()
                formdata = {
                    '__EVENTTARGET': href,
                    '__VIEWSTATE': __VIEWSTATE
                }
                yield FormRequest(response.url, formdata=formdata, callback=self.parse_middle,
                                  meta={"department": department})
        # 本地监理企业
        if response.url == "http://183.66.171.75:88/CQCollect/Qy_Query/Jlqy/Jlqy_List.aspx":
            total_page = response.xpath("//span[@id='TurnPage1_pagecount']/text()").extract_first()
            now_page = response.xpath("//span[@id='TurnPage1_currentpage']/text()").extract_first()
            c_info_list = self.parse_bendijianli(response)
            for c_info in c_info_list:
                yield c_info
        # 外地监理企业
        if response.url == "http://183.66.171.75:88/CQCollect/Qy_Query/Jlqy/WdJlqy_List.aspx":
            total_page = response.xpath("//span[@id='TurnPage1_pagecount']/text()").extract_first()
            now_page = response.xpath("//span[@id='TurnPage1_currentpage']/text()").extract_first()
            c_info_list = self.parse_waidijianli(response)
            for c_info in c_info_list:
                yield c_info
        # 混凝土企业
        if response.url == "http://183.66.171.75:88/CQCollect/Qy_Query/Hntqy/Hntqy_List.aspx":
            __EVENTTARGET = 'Pager1:LB_Next'
            total_page = response.xpath("//span[@id='Pager1_Pages']/text()").extract_first()
            now_page = response.xpath("//span[@id='Pager1_CPage']/text()").extract_first()
            tr_list = response.xpath("//table[@id='DataGrid1']/tr")
            for tr in tr_list[1:]:
                href = tr.xpath("./td[2]/font/a/@href").extract_first().strip().split("'")[1].replace("$", ":")
                formdata = {
                    '__EVENTTARGET': href,
                    '__VIEWSTATE': __VIEWSTATE
                }
                yield FormRequest(response.url, formdata=formdata, callback=self.parse_hunningtu)
        # 招标代理机构
        if response.url == "http://183.66.171.75:88/CQCollect/Qy_Query/Zbdljg/Zbdljg_List.aspx":
            total_page = response.xpath("//span[@id='TurnPage1_pagecount']/text()").extract_first()
            now_page = response.xpath("//span[@id='TurnPage1_currentpage']/text()").extract_first()
            tr_list = response.xpath("//table[@id='DataGrid1']/tr")
            for tr in tr_list[1:]:
                href = tr.xpath("./td[2]/font/a/@href").extract_first().strip().split("'")[1].replace("$", ":")
                formdata = {
                    '__EVENTTARGET': href,
                    '__VIEWSTATE': __VIEWSTATE
                }
                yield FormRequest(response.url, formdata=formdata, callback=self.parse_middle)
        # 质量检测机构
        if response.url == "http://183.66.171.75:88/CQCollect/Qy_Query/Zljcjg/Zljcjg_List.aspx":
            __EVENTTARGET = 'Pager1:LB_Next'
            total_page = response.xpath("//span[@id='Pager1_Pages']/text()").extract_first()
            now_page = response.xpath("//span[@id='Pager1_CPage']/text()").extract_first()
            tr_list = response.xpath("//table[@id='DataGrid1']/tr")
            for tr in tr_list[1:]:
                href = tr.xpath("./td[2]/font/a/@href").extract_first().strip().split("'")[1].replace("$", ":")
                formdata = {
                    '__EVENTTARGET': href,
                    '__VIEWSTATE': __VIEWSTATE
                }
                yield FormRequest(response.url, formdata=formdata, callback=self.parse_zhiliangjiance)
        # 本地造价咨询机构
        if response.url == "http://183.66.171.75:88/CQCollect/Qy_Query/Zjzxjg/Zjzxjg_List.aspx":
            __EVENTTARGET = 'Pager1:LB_Next'
            total_page = response.xpath("//span[@id='Pager1_Pages']/text()").extract_first()
            now_page = response.xpath("//span[@id='Pager1_CPage']/text()").extract_first()
            c_info_list = self.parse_zaojiazixun(response)
            for c_info in c_info_list:
                yield c_info
        # 外地造价咨询机构
        if response.url == "http://183.66.171.75:88/CQCollect/Qy_Query/Zjzxjg/Wd_Zjzxjg_List.aspx":
            __EVENTTARGET = 'Pager1:LB_Next'
            total_page = response.xpath("//span[@id='Pager1_Pages']/text()").extract_first()
            now_page = response.xpath("//span[@id='Pager1_CPage']/text()").extract_first()
            tr_list = response.xpath("//table[@id='DataGrid1']/tr")
            for tr in tr_list[1:]:
                href = tr.xpath("./td[2]/font/a/@href").extract_first().strip().split("'")[1].replace("$", ":")
                formdata = {
                    '__EVENTTARGET': href,
                    '__VIEWSTATE': __VIEWSTATE
                }
                yield FormRequest(response.url, formdata=formdata, callback=self.parse_waidizaojiazixun)
                person_btn = tr.xpath("./td[6]/font/a/@href").extract_first().strip().split("'")[1].replace("$", ":")
                formdata2 = {
                    '__EVENTTARGET': person_btn,
                    '__VIEWSTATE': __VIEWSTATE
                }
                yield FormRequest(response.url, formdata=formdata2, callback=self.parse_waidizaojiazixun_person)
        if int(total_page) > int(now_page):
        #if int(now_page)<5:
            formdata = {
                '__EVENTTARGET': __EVENTTARGET,
                '__VIEWSTATE': __VIEWSTATE
            }
            yield FormRequest(response.url, formdata=formdata, callback=self.parse)
    def parse_middle(self, response):
        print(response.url)
        if response.url == "http://183.66.171.75:88/CQCollect/Qy_Query/YhzSgqy/YhzSgqy_List.aspx":
            url = "http://183.66.171.75:88/CQCollect/Qy_Query/YhzSgqy/" + \
                  response.xpath("//script[1]/text()").extract_first().split("'")[1]
            yield Request(url, callback=self.parse_shigong, meta={"department": response.meta.get("department")})
        if response.url == "http://183.66.171.75:88/CQCollect/Qy_Query/Ryxxbs/Rybabs_List.aspx":
            url = "http://183.66.171.75:88/CQCollect/Qy_Query/Ryxxbs/" + \
                  response.xpath("//script[1]/text()").extract_first().split("'")[1]
            yield Request(url, callback=self.parse_ruyu, meta={"department": response.meta.get("department")})
        if response.url == "http://183.66.171.75:88/CQCollect/Qy_Query/Zbdljg/Zbdljg_List.aspx":
            url = "http://183.66.171.75:88/CQCollect/Qy_Query/Zbdljg/" + \
                  response.xpath("//script[1]/text()").extract_first().split("'")[1]
            yield Request(url, callback=self.parse_zhaobiaodaili)

    # 施工企业
    def parse_shigong(self, response):
        c_info = CompanyInformationItem()
        c_info["name"] = response.xpath("//span[@id='txt_Name']/text()").extract_first()
        c_info["department"] = response.meta.get("department")
        c_info["company_id"] = response.url.split("=")[-1]
        c_info["reg_address"] = response.xpath("//span[@id='txt_dz']/text()").extract_first()
        c_info["leal_person"] = response.xpath("//span[@id='txt_fddbr']/text()").extract_first()
        c_info["social_credit_code"] = response.xpath("//span[@id='txt_yyzzh']/text()").extract_first()
        c_info["regis_type"] = response.xpath("//span[@id='txt_jjxz']/text()").extract_first()
        c_info["enginer"] = response.xpath("//span[@id='txt_zgcs']/text()").extract_first()
        c_info["registered_capital"] = str(response.xpath("//span[@id='txt_zbj']/text()").extract_first()).strip("万元")
        c_info["postalcode"] = response.xpath("//span[@id='txt_yb']/text()").extract_first()
        c_info["danweitype"] = "施工企业"
        c_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        c_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        c_info["is_delete"] = 0
        c_info["url"] = response.url
        c_info["mark"] = "sgqy"
        tr_list = response.xpath("//table[@id='DataGrid1']/tr")
        if tr_list:
            for tr in tr_list[1:]:
                c_info["aptitude_num"] = tr.xpath("./td[2]/text()").extract_first()
                c_info["aptitude_type_b"] = tr.xpath("./td[3]/text()").extract_first()
                c_info["aptitude_type_s"] = tr.xpath("./td[4]/text()").extract_first()
                c_info["aptitude_level"] = tr.xpath("./td[5]/text()").extract_first()
                c_info["aptitude_ser"] = tr.xpath("./td[6]/text()").extract_first()
                c_info["aptitude_useful_date"] = tr.xpath("./td[7]/text()").extract_first()
                yield c_info
        else:
            yield c_info

        # 外地施工入渝信息报送企业

    def parse_ruyu(self, response):
        c_info = CompanyInformationItem()
        c_info["name"] = response.xpath("//span[@id='txt_Name']/b/font/text()").extract_first()
        c_info["company_id"] = response.url.split("=")[-1]
        c_info["reg_address"] = response.xpath("//span[@id='txt_dz']/text()").extract_first()
        c_info["leal_person"] = response.xpath("//span[@id='txt_fddbr']/text()").extract_first()
        c_info["social_credit_code"] = response.xpath("//span[@id='txt_yyzzh']/text()").extract_first()
        c_info["regis_type"] = response.xpath("//span[@id='txt_jjxz']/text()").extract_first()
        c_info["registered_capital"] = str(response.xpath("//span[@id='txt_zbj']/text()").extract_first()).strip(
            "万元(人民币)")
        c_info["postalcode"] = response.xpath("//span[@id='txt_yb']/text()").extract_first()
        c_info["danweitype"] = "施工企业"
        c_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        c_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        c_info["is_delete"] = 0
        c_info["url"] = response.url
        c_info["mark"] = "wdsgryxxbsqy"
        tr_list = response.xpath("//table[@id='DataGrid1']/tbody/tr")
        if tr_list:
            for tr in tr_list[1:]:
                c_info["aptitude_num"] = tr.xpath("./td[2]/text()").extract_first()
                c_info["aptitude_type_b"] = tr.xpath("./td[3]/text()").extract_first()
                c_info["aptitude_type_s"] = tr.xpath("./td[4]/text()").extract_first()
                c_info["aptitude_level"] = tr.xpath("./td[5]/text()").extract_first()
                c_info["aptitude_useful_date"] = tr.xpath("./td[6]/text()").extract_first()
                yield c_info
        else:
            yield c_info
        __VIEWSTATE = response.xpath("//input[@name='__VIEWSTATE']/@value").extract_first()
        # 职称人员按钮
        title_person_btn = response.xpath("//input[@id='btn_Zhcry']/@value").extract_first()
        formdata = {
            '__VIEWSTATE': __VIEWSTATE,
            'btn_Zhcry': title_person_btn.encode('gbk')
        }
        yield FormRequest(response.url, formdata=formdata, callback=self.parse_title_person)
        # 注册人员按钮
        reg_person_btn = response.xpath("//input[@id='btn_zcry']/@value").extract_first()
        formdata = {
            '__VIEWSTATE': __VIEWSTATE,
            'btn_zcry': reg_person_btn.encode('gbk')
        }
        yield FormRequest(response.url, formdata=formdata, callback=self.parse_reg_person)
        # 现场管理人员按钮
        line_management_btn = response.xpath("//input[@id='btn_xcry']/@value").extract_first()
        formdata = {
            '__VIEWSTATE': __VIEWSTATE,
            'btn_xcry': line_management_btn.encode('gbk')
        }
        yield FormRequest(response.url, formdata=formdata, callback=self.parse_line_management)

    # 解析职称人员
    def parse_title_person(self, response):
        # print(response.text)
        tr_list = response.xpath("//table[@id='DG_ZhiCry']/tr")
        if len(tr_list) != 1:
            for tr in tr_list[1:]:
                p_info = PersonInformationItem()
                p_info["name"] = tr.xpath("./td[2]/font/text()").extract_first()
                p_info["major"] = tr.xpath("./td[3]/font/text()").extract_first()
                p_info["title_level"] = tr.xpath("./td[4]/font/text()").extract_first()
                p_info["person_type"] = tr.xpath("./td[5]/font/text()").extract_first()
                p_info["company_name"] = tr.xpath("./td[6]/font/text()").extract_first()
                p_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                p_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                p_info["is_delete"] = 0
                p_info["mark"] = "wdsgryxxbsqy"
                yield p_info

    # 解析注册人员
    def parse_reg_person(self, response):
        # print(response.text)
        tr_list = response.xpath("//table[@id='DG_Zcry']/tr")
        if len(tr_list) != 1:
            for tr in tr_list[1:]:
                p_info = PersonInformationItem()
                p_info["name"] = tr.xpath("./td[2]/font/text()").extract_first()
                p_info["major"] = tr.xpath("./td[3]/font/text()").extract_first()
                p_info["person_genre"] = tr.xpath("./td[4]/font/text()").extract_first()
                p_info["person_type"] = tr.xpath("./td[5]/font/text()").extract_first()
                p_info["company_name"] = tr.xpath("./td[6]/font/text()").extract_first()
                p_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                p_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                p_info["is_delete"] = 0
                p_info["mark"] = "wdsgryxxbsqy"
                yield p_info

    # 解析现场管理人员
    def parse_line_management(self, response):
        tr_list = response.xpath("//table[@id='DG_Xcry']/tr")
        if len(tr_list) != 1:
            for tr in tr_list[1:]:
                p_info = PersonInformationItem()
                p_info["name"] = tr.xpath("./td[2]/font/text()").extract_first()
                p_info["person_genre"] = tr.xpath("./td[3]/font/text()").extract_first()
                p_info["person_type"] = tr.xpath("./td[4]/font/text()").extract_first()
                p_info["company_name"] = tr.xpath("./td[5]/font/text()").extract_first()
                p_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                p_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                p_info["is_delete"] = 0
                p_info["mark"] = "wdsgryxxbsqy"
                yield p_info

    # 本地监理企业
    def parse_bendijianli(self, response):
        tr_list = response.xpath("//table[@id='DataGrid1']/tr")
        c_info_list = []
        for tr in tr_list[1:]:
            c_info = CompanyInformationItem()
            c_info["name"] = tr.xpath("./td[2]/font/text()").extract_first()
            c_info["department"] = tr.xpath("./td[3]/font/text()").extract_first()
            c_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            c_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            c_info["is_delete"] = 0
            c_info["mark"] = "bdjlqy"
            tr2_num = len(tr.xpath("./td[4]/font/table/tr"))
            for num in range(1, tr2_num + 1):
                c_info["aptitude_speciality"] = tr.xpath(
                    "./td[4]/font/table/tr[{}]/td/text()".format(num)).extract_first()
                c_info["aptitude_level"] = tr.xpath("./td[5]/font/table/tr[{}]/td/text()".format(num)).extract_first()
                c_info["aptitude_num"] = tr.xpath("./td[6]/font/table/tr[{}]/td/text()".format(num)).extract_first()
                c_info["aptitude_useful_date"] = tr.xpath(
                    "./td[7]/font/table/tr[{}]/td/text()".format(num)).extract_first()
                c_info_list.append(c_info)
        return c_info_list

    # 外地监理企业
    def parse_waidijianli(self, response):
        __VIEWSTATE = response.xpath("//input[@name='__VIEWSTATE']/@value").extract_first()
        tr_list = response.xpath("//table[@id='DataGrid1']/tr")
        c_info_list = []
        for tr in tr_list[1:]:
            c_info = CompanyInformationItem()
            c_info["name"] = tr.xpath("./td[2]/font/text()").extract_first()
            c_info["department"] = tr.xpath("./td[3]/font/text()").extract_first()
            c_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            c_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            c_info["is_delete"] = 0
            c_info["mark"] = "bdjlqy"
            tr2_num = len(tr.xpath("./td[4]/font/table/tr"))
            for num in range(1, tr2_num + 1):
                c_info["aptitude_speciality"] = tr.xpath(
                    "./td[4]/font/table/tr[{}]/td/text()".format(num)).extract_first()
                c_info["aptitude_level"] = tr.xpath("./td[5]/font/table/tr[{}]/td/text()".format(num)).extract_first()
                c_info["aptitude_num"] = tr.xpath("./td[6]/font/table/tr[{}]/td/text()".format(num)).extract_first()
                c_info["aptitude_useful_date"] = tr.xpath(
                    "./td[7]/font/table/tr[{}]/td/text()".format(num)).extract_first()
                c_info_list.append(c_info)
            person_btn = tr.xpath("./td[8]/font/a/@href").extract_first().strip().split("'")[1].replace("$", ":")
            formdata = {
                '__EVENTTARGET': person_btn,
                '__VIEWSTATE': __VIEWSTATE
            }
            yield FormRequest(response.url, formdata=formdata, callback=self.parse_waidijianli_person)
        return c_info_list

    # 外地监理企业人员
    def parse_waidijianli_person(self, response):
        # print(response.text)
        tr_list = response.xpath("//table[@id='DataGrid1']/tr")
        if len(tr_list) != 1:
            company_name = response.xpath("//span[@id='_FName']/text()").extract_first()
            for tr in tr_list[1:]:
                p_info = PersonInformationItem()
                p_info["name"] = tr.xpath("./td[2]/font/a/font/text()").extract_first()
                p_info["person_type"] = tr.xpath("./td[3]/font/text()").extract_first()
                p_info["company_name"] = company_name
                p_info["credential_num"] = tr.xpath("./td[4]/font/text()").extract_first()
                p_info["major"] = tr.xpath("./td[5]/font/text()").extract_first()
                p_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                p_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                p_info["is_delete"] = 0
                p_info["mark"] = "wdjlqy"
                yield p_info

    # 混泥土企业
    def parse_hunningtu(self, response):
        c_info = CompanyInformationItem()
        c_info["name"] = response.xpath("//span[@id='FName']/text()").extract_first()
        c_info["reg_address"] = response.xpath("//span[@id='FAddress']/text()").extract_first()
        c_info["leal_person"] = response.xpath("//span[@id='FCorporation']/text()").extract_first()
        c_info["regis_type"] = response.xpath("//span[@id='FUnitType']/text()").extract_first()
        c_info["registered_capital"] = response.xpath("//span[@id='FMoney']/text()").extract_first()
        c_info["danweitype"] = "混凝土企业"
        c_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        c_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        c_info["is_delete"] = 0
        c_info["mark"] = "hntqy"
        c_info["aptitude_num"] = response.xpath("//span[@id='FGradeID']/text()").extract_first()
        c_info["aptitude_level"] = response.xpath("//span[@id='FGrade']/text()").extract_first()
        c_info["general_manager"] = response.xpath("//span[@id='FManager']/text()").extract_first()
        c_info["tech_lead"] = response.xpath("//span[@id='FPrincipal']/text()").extract_first()
        c_info["lab_manager"] = response.xpath("//span[@id='FDirector']/text()").extract_first()
        c_info["tel"] = response.xpath("//span[@id='FPhone']/text()").extract_first()
        yield c_info

    # 招标代理机构
    def parse_zhaobiaodaili(self, response):
        c_info = CompanyInformationItem()
        c_info["name"] = response.xpath("//span[@id='FEnterpriseName']/text()").extract_first()
        c_info["reg_address"] = response.xpath("//span[@id='FAddress']/text()").extract_first()
        c_info["social_credit_code"] = response.xpath("//span[@id='FBusinessID']/text()").extract_first()
        c_info["registered_capital"] = response.xpath("//span[@id='FLoginCapital']/text()").extract_first()
        c_info["danweitype"] = "招标代理机构"
        c_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        c_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        c_info["is_delete"] = 0
        c_info["mark"] = "zbdljg"
        c_info["aptitude_num"] = response.xpath("//span[@id='FCertificatenumber']/text()").extract_first()
        c_info["aptitude_level"] = response.xpath("//span[@id='FQualificationLevel']/text()").extract_first()
        c_info["build_date"] = response.xpath("//span[@id='FBeginDate']/text()").extract_first()
        c_info["fax"] = response.xpath("//span[@id='FFax']/text()").extract_first()
        c_info["tel"] = response.xpath("//span[@id='FPhone']/text()").extract_first()
        # yield c_info
        check_id = response.url.split("?")[-1]
        person_url = "http://183.66.171.75:88/CQCollect/Qy_Query/Zbdljg/Zbdljg_ryqk.aspx?" + check_id
        yield Request(person_url, callback=self.parse_zhaobiaodaili_person)

    def parse_zhaobiaodaili_person(self, response):
        tr_list = response.xpath("//table[@id='DataGrid1']/tr")
        if len(tr_list) != 1:
            for tr in tr_list[1:]:
                p_info = PersonInformationItem()
                p_info["name"] = tr.xpath("./td[2]/font/a/font/text()").extract_first()
                p_info["company_name"] = tr.xpath("./td[4]/font/text()").extract_first()
                p_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                p_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                p_info["is_delete"] = 0
                p_info["mark"] = "zbdljg"
                p_info["sex"] = tr.xpath("./td[3]/font/text()").extract_first()
                yield p_info

    # 质量检测机构
    def parse_zhiliangjiance(self, response):
        c_info = CompanyInformationItem()
        c_info["name"] = response.xpath("//span[@id='FName']/text()").extract_first()
        c_info["reg_address"] = response.xpath("//span[@id='FAddress']/text()").extract_first()
        c_info["danweitype"] = "质量检测机构"
        c_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        c_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        c_info["is_delete"] = 0
        c_info["mark"] = "zljcjg"
        c_info["contact_person"] = response.xpath("//span[@id='FManager']/text()").extract_first()
        c_info["postalcode"] = response.xpath("//span[@id='FPhone']/text()").extract_first()
        yield c_info

    # 本地造价咨询机构
    def parse_zaojiazixun(self, response):
        __VIEWSTATE = response.xpath("//input[@name='__VIEWSTATE']/@value").extract_first()
        tr_list = response.xpath("//table[@id='DataGrid1']/tr")
        c_info_list = []
        for tr in tr_list[1:]:
            c_info = CompanyInformationItem()
            c_info["name"] = tr.xpath("./td[2]/font/a/font/text()").extract_first()
            c_info["aptitude_level"] = tr.xpath("./td[3]/font/text()").extract_first()
            c_info["aptitude_num"] = tr.xpath("./td[4]/font/text()").extract_first()
            c_info["aptitude_useful_date"] = tr.xpath("./td[5]/font/text()").extract_first()
            c_info["danweitype"] = "造价咨询机构"
            c_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            c_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            c_info["is_delete"] = 0
            c_info["mark"] = "bdzjzxjg"
            c_info_list.append(c_info)
            person_btn = tr.xpath("./td[6]/font/a/@href").extract_first().strip().split("'")[1].replace("$", ":")
            formdata = {
                '__EVENTTARGET': person_btn,
                '__VIEWSTATE': __VIEWSTATE
            }
            yield FormRequest(response.url, formdata=formdata, callback=self.parse_zaojiazixun_person)
        return c_info_list

    def parse_zaojiazixun_person(self, response):
        tr_list = response.xpath("//table[@id='DataGrid1']/tr")
        if len(tr_list) != 1:
            for tr in tr_list[1:]:
                p_info = PersonInformationItem()
                p_info["name"] = tr.xpath("./td[2]/font/a/font/text()").extract_first()
                p_info["sex"] = tr.xpath("./td[3]/font/text()").extract_first()
                p_info["credential_num"] = tr.xpath("./td[4]/font/text()").extract_first()
                p_info["company_name"] = tr.xpath("./td[5]/font/text()").extract_first()
                p_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                p_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                p_info["is_delete"] = 0
                p_info["mark"] = "bdzjzxjg"
                yield p_info

            # 外地造价咨询机构

    def parse_waidizaojiazixun(self, response):
        c_info = CompanyInformationItem()
        c_info["company_id"] = response.url.split("=")[-1]
        c_info["name"] = response.xpath("//span[@id='FBaseinfoName']/text()").extract_first()
        c_info["reg_address"] = response.xpath("//span[@id='FLXDZ']/text()").extract_first()
        c_info["leal_person"] = response.xpath("//span[@id='FFR']/text()").extract_first()
        c_info["regis_type"] = response.xpath("//span[@id='FQYLX']/text()").extract_first()
        c_info["registered_capital"] = response.xpath("//span[@id='FZCZB']/text()").extract_first()
        if c_info["registered_capital"]:
            c_info["registered_capital"] = c_info["registered_capital"].strip("万元")
        c_info["postalcode"] = response.xpath("//span[@id='FYB']/text()").extract_first()
        c_info["department"] = response.xpath("//span[@id='FDX']/text()").extract_first()
        c_info["danweitype"] = "造价咨询机构"
        c_info["url"] = response.url
        c_info["aptitude_num"] = response.xpath("//span[@id='FZZZH']/text()").extract_first()
        c_info["aptitude_level"] = response.xpath("//span[@id='FQYDJ']/text()").extract_first()
        c_info["mark"] = "wdzjzxjg"
        c_info["aptitude_useful_date"] = response.xpath("//span[@id='FYXQ']/text()").extract_first()
        c_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        c_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        c_info["is_delete"] = 0
        c_info["tech_lead"] = response.xpath("//span[@id='FJSFZR']/text()").extract_first()
        c_info["fax"] = response.xpath("//span[@id='FCZ']/text()").extract_first()
        c_info["zjgcs_sum"] = response.xpath("//span[@id='FZJGCSZS']/text()").extract_first()
        c_info["zjy_sum"] = response.xpath("//span[@id='FZJYZS']/text()").extract_first()
        c_info["gjzc_sum"] = response.xpath("//span[@id='FGJZC']/text()").extract_first()
        c_info["zjzc_sum"] = response.xpath("//span[@id='FZJZC']/text()").extract_first()
        c_info["aptitude_accept_date"] = response.xpath("//span[@id='FHDZZSJ']/text()").extract_first()
        c_info["approval_number"] = response.xpath("//span[@id='FPZWH']/text()").extract_first()
        yield c_info

    def parse_waidizaojiazixun_person(self, response):
        tr_list = response.xpath("//table[@id='DataGrid1']/tr")
        if len(tr_list) != 1:
            for tr in tr_list[1:]:
                p_info = PersonInformationItem()
                p_info["name"] = tr.xpath("./td[2]/font/a/font/text()").extract_first()
                p_info["sex"] = tr.xpath("./td[3]/font/text()").extract_first()
                p_info["credential_num"] = tr.xpath("./td[4]/font/text()").extract_first()
                p_info["company_name"] = tr.xpath("./td[5]/font/text()").extract_first()
                p_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                p_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                p_info["is_delete"] = 0
                p_info["mark"] = "wdzjzxjg"
                yield p_info
