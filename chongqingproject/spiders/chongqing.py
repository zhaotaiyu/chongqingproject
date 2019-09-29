# -*- coding: gbk -*-
import time

from scrapy import Request, FormRequest
import datetime
from chongqingproject.items import *

class ChongqingSpider(scrapy.Spider):
    name = 'chongqing'
    allowed_domains = ['183.66.171.75']
    #start_urls = ['http://183.66.171.75:88/CQCollect/Qy_Query/YhzSgqy/YhzSgqy_List.aspx']
    #start_urls = ['http://183.66.171.75:88/CQCollect/Qy_Query/Ryxxbs/Rybabs_List.aspx']
    #start_urls = ['http://183.66.171.75:88/CQCollect/Qy_Query/Jlqy/Jlqy_List.aspx']
    #start_urls = ['http://183.66.171.75:88/CQCollect/Qy_Query/Jlqy/WdJlqy_List.aspx']
    #start_urls = ['http://183.66.171.75:88/CQCollect/Qy_Query/Hntqy/Hntqy_List.aspx']
    #start_urls = ['http://183.66.171.75:88/CQCollect/Qy_Query/Zbdljg/Zbdljg_List.aspx']
    #start_urls = ['http://183.66.171.75:88/CQCollect/Qy_Query/Zljcjg/Zljcjg_List.aspx']
    #start_urls = ['http://183.66.171.75:88/CQCollect/Qy_Query/Zjzxjg/Zjzxjg_List.aspx']
    #start_urls = ['http://183.66.171.75:88/CQCollect/Qy_Query/Zjzxjg/Wd_Zjzxjg_List.aspx']
    start_urls = ['http://183.66.171.75:88/CQCollect/Qy_Query/YhzSgqy/YhzSgqy_List.aspx','http://183.66.171.75:88/CQCollect/Qy_Query/Ryxxbs/Rybabs_List.aspx','http://183.66.171.75:88/CQCollect/Qy_Query/Jlqy/Jlqy_List.aspx','http://183.66.171.75:88/CQCollect/Qy_Query/Hntqy/Hntqy_List.aspx','http://183.66.171.75:88/CQCollect/Qy_Query/Zbdljg/Zbdljg_List.aspx','http://183.66.171.75:88/CQCollect/Qy_Query/Zljcjg/Zljcjg_List.aspx','http://183.66.171.75:88/CQCollect/Qy_Query/Zjzxjg/Zjzxjg_List.aspx','http://183.66.171.75:88/CQCollect/Qy_Query/Zjzxjg/Wd_Zjzxjg_List.aspx','http://183.66.171.75:88/CQCollect/Qy_Query/Jlqy/WdJlqy_List.aspx']

    def parse(self, response):
        __VIEWSTATE = response.xpath("//input[@name='__VIEWSTATE']/@value").extract_first()
        __EVENTTARGET = 'TurnPage1:LB_Next'
        # ʩ����ҵ
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
        # ���ʩ��������Ϣ������ҵ
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
                yield FormRequest(response.url, formdata=formdata, callback=self.parse_middle,meta={"department": department})
        # ���ؼ�����ҵ
        if response.url == "http://183.66.171.75:88/CQCollect/Qy_Query/Jlqy/Jlqy_List.aspx":
            total_page = response.xpath("//span[@id='TurnPage1_pagecount']/text()").extract_first()
            now_page = response.xpath("//span[@id='TurnPage1_currentpage']/text()").extract_first()
            c_info_list,apt_info_list = self.parse_bendijianli(response)
            for c_info in c_info_list:
                yield c_info
            for apt_info in apt_info_list:
                yield apt_info
        # ��ؼ�����ҵ
        if response.url == "http://183.66.171.75:88/CQCollect/Qy_Query/Jlqy/WdJlqy_List.aspx":
            total_page = response.xpath("//span[@id='TurnPage1_pagecount']/text()").extract_first()
            now_page = response.xpath("//span[@id='TurnPage1_currentpage']/text()").extract_first()
            data = self.parse_waidijianli(response)
            for c_info in data.get("c_info_list"):
                yield c_info
            for apt_info in data.get("apt_info_list"):
                yield apt_info
            for request in data.get("request_list"):
                yield request
        # ��������ҵ
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
        # �б�������
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
        # ����������
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
        # ���������ѯ����
        if response.url == "http://183.66.171.75:88/CQCollect/Qy_Query/Zjzxjg/Zjzxjg_List.aspx":
            __EVENTTARGET = 'Pager1:LB_Next'
            total_page = response.xpath("//span[@id='Pager1_Pages']/text()").extract_first()
            now_page = response.xpath("//span[@id='Pager1_CPage']/text()").extract_first()
            data = self.parse_zaojiazixun(response)
            for c_info in data.get("c_info_list"):
                yield c_info
            for apt_info in data.get("apt_info_list"):
                yield apt_info
            for request in data.get("request_list"):
                yield request
        # ��������ѯ����
        if response.url == "http://183.66.171.75:88/CQCollect/Qy_Query/Zjzxjg/Wd_Zjzxjg_List.aspx":
            __EVENTTARGET = 'Pager1:LB_Next'
            total_page = response.xpath("//span[@id='Pager1_Pages']/text()").extract_first()
            now_page = response.xpath("//span[@id='Pager1_CPage']/text()").extract_first()
            tr_list = response.xpath("//table[@id='DataGrid1']/tr")
            for tr in tr_list[1:]:
                person_btn = tr.xpath("./td[6]/font/a/@href").extract_first().strip().split("'")[1].replace("$", ":")
                formdata2 = {
                    '__EVENTTARGET': person_btn,
                    '__VIEWSTATE': __VIEWSTATE
                }
                # request =  FormRequest(response.url, formdata=formdata2, callback=self.parse_waidizaojiazixun_person,
                #                   dont_filter=True)
                href = tr.xpath("./td[2]/font/a/@href").extract_first().strip().split("'")[1].replace("$", ":")
                formdata = {
                    '__EVENTTARGET': href,
                    '__VIEWSTATE': __VIEWSTATE
                }
                yield FormRequest(response.url, formdata=formdata, callback=self.parse_waidizaojiazixun,dont_filter=True,meta={"formdata2":formdata2,"url":response.url})

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

    # ʩ����ҵ
    def parse_shigong(self, response):
        province_company_id = "chongqing_" + str(int(time.time()*1000))
        c_info = CompanyInformationItem()
        c_info["company_name"] = response.xpath("//span[@id='txt_Name']/text()").extract_first()
        c_info["department"] = response.meta.get("department")
        c_info["province_company_id"] = province_company_id
        c_info["regis_address"] = response.xpath("//span[@id='txt_dz']/text()").extract_first()
        c_info["leal_person"] = response.xpath("//span[@id='txt_fddbr']/text()").extract_first()
        c_info["social_credit_code"] = response.xpath("//span[@id='txt_yyzzh']/text()").extract_first()
        c_info["regis_type"] = response.xpath("//span[@id='txt_jjxz']/text()").extract_first()
        c_info["enginer"] = response.xpath("//span[@id='txt_zgcs']/text()").extract_first()
        c_info["registered_capital"] = str(response.xpath("//span[@id='txt_zbj']/text()").extract_first()).strip("��Ԫ")
        c_info["postalcode"] = response.xpath("//span[@id='txt_yb']/text()").extract_first()
        c_info["danweitype"] = "ʩ����ҵ"
        c_info["url"] = response.url
        yield c_info
        tr_list = response.xpath("//table[@id='DataGrid1']/tr")
        if tr_list:
            for tr in tr_list[1:]:
                apt_info = AptitudeItem()
                apt_info["province_company_id"] = province_company_id
                apt_info["company_name"] = c_info["company_name"]
                apt_info["aptitude_id"] = tr.xpath("./td[2]/text()").extract_first()
                apt_info["aptitude_large"] = tr.xpath("./td[3]/text()").extract_first()
                apt_info["aptitude_small"] = tr.xpath("./td[4]/text()").extract_first()
                apt_info["level"] = tr.xpath("./td[5]/text()").extract_first()
                apt_info["aptitude_ser"] = tr.xpath("./td[6]/text()").extract_first()
                apt_info["aptitude_usefultime"] = tr.xpath("./td[7]/text()").extract_first()
                yield apt_info

        # ���ʩ��������Ϣ������ҵ
    # �������
    def parse_ruyu(self, response):
        c_info = CompanyInformationItem()
        province_company_id = "chongqing_" + str(int(time.time() * 1000))
        c_info["company_name"] = response.xpath("//span[@id='txt_Name']/b/font/text()").extract_first()
        c_info["province_company_id"] = province_company_id
        c_info["regis_address"] = response.xpath("//span[@id='txt_dz']/text()").extract_first()
        c_info["leal_person"] = response.xpath("//span[@id='txt_fddbr']/text()").extract_first()
        c_info["social_credit_code"] = response.xpath("//span[@id='txt_yyzzh']/text()").extract_first()
        c_info["regis_type"] = response.xpath("//span[@id='txt_jjxz']/text()").extract_first()
        c_info["registered_capital"] = str(response.xpath("//span[@id='txt_zbj']/text()").extract_first()).strip(
            "��Ԫ(�����)")
        c_info["postalcode"] = response.xpath("//span[@id='txt_yb']/text()").extract_first()
        c_info["danweitype"] = "ʩ����ҵ"
        c_info["url"] = response.url
        yield c_info
        beian = BeianItem()
        beian["company_name"] = c_info["company_name"]
        beian["social_credit_code"] = c_info["social_credit_code"]
        beian["record_province"] = "����"
        yield beian
        tr_list = response.xpath("//table[@id='DataGrid1']/tbody/tr")
        if tr_list:
            for tr in tr_list[1:]:
                apt_info = AptitudeItem()
                apt_info["province_company_id"] = province_company_id
                apt_info["company_name"] = c_info["company_name"]
                apt_info["aptitude_id"] = tr.xpath("./td[2]/text()").extract_first()
                apt_info["aptitude_large"] = tr.xpath("./td[3]/text()").extract_first()
                apt_info["aptitude_small"] = tr.xpath("./td[4]/text()").extract_first()
                apt_info["level"] = tr.xpath("./td[5]/text()").extract_first()
                apt_info["aptitude_usefultime"] = tr.xpath("./td[6]/text()").extract_first()
                yield apt_info
        __VIEWSTATE = response.xpath("//input[@name='__VIEWSTATE']/@value").extract_first()
        # ְ����Ա��ť
        title_person_btn = response.xpath("//input[@id='btn_Zhcry']/@value").extract_first()
        formdata = {
            '__VIEWSTATE': __VIEWSTATE,
            'btn_Zhcry': title_person_btn.encode('gbk')
        }
        yield FormRequest(response.url, formdata=formdata, callback=self.parse_title_person,meta={"province_company_id":province_company_id,"company_name":c_info["company_name"]})
        # ע����Ա��ť
        reg_person_btn = response.xpath("//input[@id='btn_zcry']/@value").extract_first()
        formdata = {
            '__VIEWSTATE': __VIEWSTATE,
            'btn_zcry': reg_person_btn.encode('gbk')
        }
        yield FormRequest(response.url, formdata=formdata, callback=self.parse_reg_person,meta={"province_company_id":province_company_id,"company_name":c_info["company_name"]})
        # �ֳ�������Ա��ť
        line_management_btn = response.xpath("//input[@id='btn_xcry']/@value").extract_first()
        formdata = {
            '__VIEWSTATE': __VIEWSTATE,
            'btn_xcry': line_management_btn.encode('gbk')
        }
        yield FormRequest(response.url, formdata=formdata, callback=self.parse_line_management,meta={"province_company_id":province_company_id,"company_name":c_info["company_name"]})
    # ����ְ����Ա
    def parse_title_person(self, response):
        tr_list = response.xpath("//table[@id='DG_ZhiCry']/tr")
        if len(tr_list) != 1:
            for tr in tr_list[1:]:
                time.sleep(0.01)
                province_person_id = "chongqing_p_" + str(int(time.time() * 1000))
                p_info = PersonInformationItem()
                p_info["province_person_id"] = province_person_id
                p_info["company_name"] = response.meta.get("company_name")
                p_info["province_company_id"] = response.meta.get("province_company_id")
                p_info["person_name"] = tr.xpath("./td[2]/font/text()").extract_first()
                yield p_info
                p_cert = PersonCertificateItem()
                p_cert["person_name"] = p_info["person_name"]
                p_cert["company_name"] = response.meta.get("company_name")
                p_cert["aptitude_type"] = "ְ����"
                p_cert["province_person_id"] = province_person_id
                p_cert["major"] = tr.xpath("./td[3]/font/text()").extract_first()
                p_cert["level"] = tr.xpath("./td[4]/font/text()").extract_first()
                p_cert["aptitude_name"] = tr.xpath("./td[5]/font/text()").extract_first()
                p_cert["certificate_company_name"] = tr.xpath("./td[6]/font/text()").extract_first()
                yield p_cert
    # ����ע����Ա
    def parse_reg_person(self, response):
        tr_list = response.xpath("//table[@id='DG_Zcry']/tr")
        if len(tr_list) != 1:
            for tr in tr_list[1:]:
                time.sleep(0.01)
                province_person_id = "chongqing_p_" + str(int(time.time() * 1000))
                p_info = PersonInformationItem()
                p_info["province_person_id"] = province_person_id
                p_info["province_company_id"] = response.meta.get("province_company_id")
                p_info["person_name"] = tr.xpath("./td[2]/font/text()").extract_first()
                p_info["company_name"] = response.meta.get("company_name")
                yield p_info
                p_cert = PersonCertificateItem()
                p_cert["person_name"] = p_info["person_name"]
                p_cert["company_name"] = response.meta.get("company_name")
                p_cert["aptitude_type"] = "ע����"
                p_cert["province_person_id"] = province_person_id
                p_cert["major"] = tr.xpath("./td[3]/font/text()").extract_first()
                p_cert["level"] = tr.xpath("./td[4]/font/text()").extract_first()
                p_cert["certificate_company_name"] = tr.xpath("./td[6]/font/text()").extract_first()
                yield p_cert
    # �����ֳ�������Ա
    def parse_line_management(self, response):
        tr_list = response.xpath("//table[@id='DG_Xcry']/tr")
        if len(tr_list) != 1:
            for tr in tr_list[1:]:
                time.sleep(0.01)
                province_person_id = "chongqing_p_" + str(int(time.time() * 1000))
                p_info = PersonInformationItem()
                p_info["province_person_id"] = province_person_id
                p_info["province_company_id"] = response.meta.get("province_company_id")
                p_info["person_name"] = tr.xpath("./td[2]/font/text()").extract_first()
                p_info["company_name"] = response.meta.get("company_name")
                yield p_info
                p_cert = PersonCertificateItem()
                p_cert["person_name"] = p_info["person_name"]
                p_cert["company_name"] = response.meta.get("company_name")
                p_cert["aptitude_type"] = "�ֳ�������Ա"
                p_cert["province_person_id"] = province_person_id
                p_cert["aptitude_name"] = tr.xpath("./td[3]/font/text()").extract_first()
                p_cert["certificate_company_name"] = tr.xpath("./td[5]/font/text()").extract_first()
                yield p_cert

    # ���ؼ�����ҵ
    def parse_bendijianli(self, response):
        tr_list = response.xpath("//table[@id='DataGrid1']/tr")
        c_info_list = []
        apt_info_list = []
        for tr in tr_list[1:]:
            time.sleep(0.01)
            province_company_id = "chongqing_" + str(int(time.time() * 1000))
            c_info = CompanyInformationItem()
            c_info["province_company_id"] = province_company_id
            c_info["company_name"] = tr.xpath("./td[2]/font/text()").extract_first()
            c_info["department"] = tr.xpath("./td[3]/font/text()").extract_first()
            c_info["danweitype"] = "������ҵ"
            tr2_num = len(tr.xpath("./td[4]/font/table/tr"))
            for num in range(1, tr2_num + 1):
                apt_info = AptitudeItem()
                apt_info["province_company_id"] = province_company_id
                apt_info["company_name"] = c_info["company_name"]
                apt_info["aptitude_major"] = tr.xpath("./td[4]/font/table/tr[{}]/td/text()".format(num)).extract_first()
                apt_info["level"] = tr.xpath("./td[5]/font/table/tr[{}]/td/text()".format(num)).extract_first()
                apt_info["aptitude_id"] = tr.xpath("./td[6]/font/table/tr[{}]/td/text()".format(num)).extract_first()
                apt_info["aptitude_usefultime"] = tr.xpath("./td[7]/font/table/tr[{}]/td/text()".format(num)).extract_first()
                apt_info_list.append(apt_info)
            c_info_list.append(c_info)
        return c_info_list,apt_info_list

    # ��ؼ�����ҵ
    def parse_waidijianli(self, response):
        __VIEWSTATE = response.xpath("//input[@name='__VIEWSTATE']/@value").extract_first()
        tr_list = response.xpath("//table[@id='DataGrid1']/tr")
        c_info_list = []
        apt_info_list = []
        request_list = []
        for tr in tr_list[1:]:
            time.sleep(0.01)
            province_company_id = "chongqing_" + str(int(time.time() * 1000))
            c_info = CompanyInformationItem()
            c_info["province_company_id"] = province_company_id
            c_info["company_name"] = tr.xpath("./td[2]/font/text()").extract_first()
            c_info["department"] = tr.xpath("./td[3]/font/text()").extract_first()
            c_info["danweitype"] = "������ҵ"
            c_info_list.append(c_info)
            tr2_num = len(tr.xpath("./td[4]/font/table/tr"))
            for num in range(1, tr2_num + 1):
                apt_info = AptitudeItem()
                apt_info["province_company_id"] = province_company_id
                apt_info["company_name"] = c_info["company_name"]
                apt_info["aptitude_major"] = tr.xpath("./td[4]/font/table/tr[{}]/td/text()".format(num)).extract_first()
                apt_info["level"] = tr.xpath("./td[5]/font/table/tr[{}]/td/text()".format(num)).extract_first()
                apt_info["aptitude_id"] = tr.xpath("./td[6]/font/table/tr[{}]/td/text()".format(num)).extract_first()
                apt_info["aptitude_usefultime"] = tr.xpath("./td[7]/font/table/tr[{}]/td/text()".format(num)).extract_first()
                apt_info_list.append(apt_info)
            person_btn = tr.xpath("./td[8]/font/a/@href").extract_first().strip().split("'")[1].replace("$", ":")
            formdata = {
                '__EVENTTARGET': person_btn,
                '__VIEWSTATE': __VIEWSTATE
            }
            request =  FormRequest(response.url, formdata=formdata, callback=self.parse_waidijianli_person,meta={"province_company_id":province_company_id})
            request_list.append(request)
        data={"c_info_list":c_info_list,"apt_info_list":apt_info_list,"request_list":request_list}
        return data
    # ��ؼ�����ҵ��Ա
    def parse_waidijianli_person(self, response):
        tr_list = response.xpath("//table[@id='DataGrid1']/tr")
        if len(tr_list) != 1:
            company_name = response.xpath("//span[@id='_FName']/text()").extract_first()
            beian = BeianItem()
            beian["company_name"] = company_name
            beian["record_province"] = "����"
            yield beian
            for tr in tr_list[1:]:
                time.sleep(0.01)
                province_person_id = "chongqing_p_" + str(int(time.time() * 1000))
                p_info = PersonInformationItem()
                p_info["company_name"] = company_name
                p_info["province_person_id"] = province_person_id
                p_info["province_company_id"] = response.meta.get("province_company_id")
                p_info["person_name"] = tr.xpath("./td[2]/font/a/font/text()").extract_first()
                p_cert = PersonCertificateItem()
                p_cert["person_name"] = p_info["person_name"]
                p_cert["province_person_id"] = province_person_id
                p_cert["aptitude_type"] = "ע����"
                p_cert["aptitude_name"] = tr.xpath("./td[3]/font/text()").extract_first()
                p_cert["company_name"] = company_name
                p_cert["certificate_company_name"] = company_name
                p_cert["certificate_num"] = tr.xpath("./td[4]/font/text()").extract_first()
                p_cert["major"] = tr.xpath("./td[5]/font/text()").extract_first()
                yield p_cert

    # ��������ҵ
    def parse_hunningtu(self, response):
        province_company_id = "chongqing_" + str(int(time.time() * 1000))
        c_info = CompanyInformationItem()
        c_info["province_company_id"] = province_company_id
        c_info["company_name"] = response.xpath("//span[@id='FName']/text()").extract_first()
        c_info["regis_address"] = response.xpath("//span[@id='FAddress']/text()").extract_first()
        c_info["leal_person"] = response.xpath("//span[@id='FCorporation']/text()").extract_first()
        c_info["regis_type"] = response.xpath("//span[@id='FUnitType']/text()").extract_first()
        c_info["registered_capital"] = response.xpath("//span[@id='FMoney']/text()").extract_first()
        c_info["danweitype"] = "��������ҵ"
        c_info["tel"] = response.xpath("//span[@id='FPhone']/text()").extract_first()
        c_info["ctoname"] = response.xpath("//span[@id='FPrincipal']/text()").extract_first()
        yield c_info
        apt_info = AptitudeItem()
        apt_info["company_name"] = c_info["company_name"]
        apt_info["province_company_id"] = province_company_id
        apt_info["aptitude_id"] = response.xpath("//span[@id='FGradeID']/text()").extract_first()
        apt_info["level"] = response.xpath("//span[@id='FGrade']/text()").extract_first()
        if apt_info["level"] or apt_info["aptitude_id"]:
            yield apt_info

    # �б�������
    def parse_zhaobiaodaili(self, response):
        province_company_id = "chongqing_" + str(int(time.time() * 1000))
        c_info = CompanyInformationItem()
        c_info["province_company_id"] = province_company_id
        c_info["company_name"] = response.xpath("//span[@id='FEnterpriseName']/text()").extract_first()
        c_info["regis_address"] = response.xpath("//span[@id='FAddress']/text()").extract_first()
        c_info["social_credit_code"] = response.xpath("//span[@id='FBusinessID']/text()").extract_first()
        c_info["registered_capital"] = response.xpath("//span[@id='FLoginCapital']/text()").extract_first()
        c_info["danweitype"] = "�б�������"
        c_info["build_date"] = response.xpath("//span[@id='FBeginDate']/text()").extract_first()
        c_info["fax"] = response.xpath("//span[@id='FFax']/text()").extract_first()
        c_info["tel"] = response.xpath("//span[@id='FPhone']/text()").extract_first()
        yield c_info
        apt_info = AptitudeItem()
        apt_info["company_name"] = c_info["company_name"]
        apt_info["province_company_id"] = province_company_id
        apt_info["aptitude_id"] = response.xpath("//span[@id='FCertificatenumber']/text()").extract_first()
        apt_info["level"] = response.xpath("//span[@id='FQualificationLevel']/text()").extract_first()
        yield apt_info
        check_id = response.url.split("?")[-1]
        person_url = "http://183.66.171.75:88/CQCollect/Qy_Query/Zbdljg/Zbdljg_ryqk.aspx?" + check_id
        yield Request(person_url, callback=self.parse_zhaobiaodaili_person,meta={"province_company_id":province_company_id})
    def parse_zhaobiaodaili_person(self, response):
        tr_list = response.xpath("//table[@id='DataGrid1']/tr")
        if len(tr_list) != 1:
            for tr in tr_list[1:]:
                time.sleep(0.01)
                province_person_id = "chongqing_p_" + str(int(time.time() * 1000))
                p_info = PersonInformationItem()
                p_info["province_person_id"] = province_person_id
                p_info["person_name"] = tr.xpath("./td[2]/font/a/font/text()").extract_first()
                p_info["province_company_id"] = response.meta.get("province_company_id")
                p_info["company_name"] = tr.xpath("./td[4]/font/text()").extract_first()
                p_info["person_sex"] = tr.xpath("./td[3]/font/text()").extract_first()
                yield p_info
                p_cert = PersonCertificateItem()
                p_cert["person_name"] = p_info["person_name"]
                p_cert["province_person_id"] = province_person_id
                p_cert["aptitude_type"] = "�б����רְ��Ա"
                p_cert["company_name"] = p_info["company_name"]
                p_cert["certificate_company_name"] = p_info["company_name"]
                yield p_cert

    # ����������
    def parse_zhiliangjiance(self, response):
        province_company_id = "chongqing_" + str(int(time.time() * 1000))
        c_info = CompanyInformationItem()
        c_info["province_company_id"] = province_company_id
        c_info["company_name"] = response.xpath("//span[@id='FName']/text()").extract_first()
        c_info["regis_address"] = response.xpath("//span[@id='FAddress']/text()").extract_first()
        c_info["danweitype"] = "����������"
        c_info["contact_person"] = response.xpath("//span[@id='FManager']/text()").extract_first()
        c_info["postalcode"] = response.xpath("//span[@id='FPhone']/text()").extract_first()
        yield c_info

    # ���������ѯ����
    def parse_zaojiazixun(self, response):
        __VIEWSTATE = response.xpath("//input[@name='__VIEWSTATE']/@value").extract_first()
        tr_list = response.xpath("//table[@id='DataGrid1']/tr")
        c_info_list = []
        apt_info_list = []
        request_list = []
        for tr in tr_list[1:]:
            time.sleep(0.01)
            province_company_id = "chongqing_" + str(int(time.time() * 1000))
            c_info = CompanyInformationItem()
            c_info["province_company_id"] = province_company_id
            c_info["company_name"] = tr.xpath("./td[2]/font/a/font/text()").extract_first()
            c_info["danweitype"] = "�����ѯ����"
            c_info_list.append(c_info)
            apt_info = AptitudeItem()
            apt_info["company_name"] = c_info["company_name"]
            apt_info["province_company_id"] = province_company_id
            apt_info["level"] = tr.xpath("./td[3]/font/text()").extract_first()
            apt_info["aptitude_id"] = tr.xpath("./td[4]/font/text()").extract_first()
            apt_info["aptitude_usefultime"] = tr.xpath("./td[5]/font/text()").extract_first()
            apt_info_list.append(apt_info)
            person_btn = tr.xpath("./td[6]/font/a/@href").extract_first().strip().split("'")[1].replace("$", ":")
            formdata = {
                '__EVENTTARGET': person_btn,
                '__VIEWSTATE': __VIEWSTATE
            }
            request =  FormRequest(response.url, formdata=formdata, callback=self.parse_zaojiazixun_person,dont_filter=True,meta={"province_company_id":province_company_id,"company_name":c_info["company_name"]})
            request_list.append(request)
        data = {"c_info_list": c_info_list, "apt_info_list": apt_info_list, "request_list": request_list}
        return data

    def parse_zaojiazixun_person(self, response):
        tr_list = response.xpath("//table[@id='DataGrid1']/tr")
        if len(tr_list) != 1:
            for tr in tr_list[1:]:
                time.sleep(0.01)
                province_person_id = "chongqing_p_" + str(int(time.time() * 1000))
                p_info = PersonInformationItem()
                p_info["province_company_id"] = response.meta.get("province_company_id")
                p_info["province_person_id"] = province_person_id
                p_info["person_name"] = tr.xpath("./td[2]/font/a/font/text()").extract_first()
                p_info["person_sex"] = tr.xpath("./td[3]/font/text()").extract_first()
                p_info["company_name"] = response.meta.get("company_name")
                yield p_info
                p_cert = PersonCertificateItem()
                p_cert["person_name"] = p_info["person_name"]
                p_cert["province_person_id"] = province_person_id
                p_cert["certificate_num"] = tr.xpath("./td[4]/font/text()").extract_first()
                p_cert["company_name"] = response.meta.get("company_name")
                p_cert["certificate_company_name"] = tr.xpath("./td[5]/font/text()").extract_first()
                p_cert["aptitude_type"] = "ע����"
                p_cert["aptitude_name"] = "ע�����ʦ"
                yield p_cert

            # ��������ѯ����

    def parse_waidizaojiazixun(self, response):
        province_company_id = "chongqing_" + str(int(time.time() * 1000))
        c_info = CompanyInformationItem()
        c_info["province_company_id"] = province_company_id
        c_info["company_name"] = response.xpath("//span[@id='FBaseinfoName']/text()").extract_first()
        c_info["regis_address"] = response.xpath("//span[@id='FLXDZ']/text()").extract_first()
        c_info["leal_person"] = response.xpath("//span[@id='FFR']/text()").extract_first()
        c_info["regis_type"] = response.xpath("//span[@id='FQYLX']/text()").extract_first()
        c_info["registered_capital"] = response.xpath("//span[@id='FZCZB']/text()").extract_first()
        if c_info["registered_capital"]:
            c_info["registered_capital"] = c_info["registered_capital"].strip("��Ԫ")
        c_info["postalcode"] = response.xpath("//span[@id='FYB']/text()").extract_first()
        c_info["department"] = response.xpath("//span[@id='FDX']/text()").extract_first()
        c_info["danweitype"] = "�����ѯ����"
        c_info["url"] = response.url
        c_info["ctoname"] = response.xpath("//span[@id='FJSFZR']/text()").extract_first()
        c_info["fax"] = response.xpath("//span[@id='FCZ']/text()").extract_first()
        yield c_info
        beian = BeianItem()
        beian["company_name"] = c_info["company_name"]
        beian["record_province"] = "����"
        yield beian
        apt_info = AptitudeItem()
        apt_info["company_name"] = c_info["company_name"]
        apt_info["province_company_id"] = province_company_id
        apt_info["aptitude_id"] = response.xpath("//span[@id='FZZZH']/text()").extract_first()
        apt_info["level"] = response.xpath("//span[@id='FQYDJ']/text()").extract_first()
        apt_info["aptitude_startime"] = response.xpath("//span[@id='FHDZZSJ']/text()").extract_first()
        apt_info["approval_number"] = response.xpath("//span[@id='FPZWH']/text()").extract_first()
        yield apt_info
        yield FormRequest(url=response.meta.get("url"),formdata=response.meta.get("formdata2"),callback=self.parse_waidizaojiazixun_person,dont_filter=True,meta={"province_company_id":province_company_id,"company_name":c_info["company_name"]})

    def parse_waidizaojiazixun_person(self, response):
        tr_list = response.xpath("//table[@id='DataGrid1']/tr")
        if len(tr_list) != 1:
            for tr in tr_list[1:]:
                time.sleep(0.01)
                province_person_id = "chongqing_p_" + str(int(time.time() * 1000))
                p_info = PersonInformationItem()
                p_info["province_company_id"] = response.meta.get("province_company_id")
                p_info["province_person_id"] = province_person_id
                p_info["person_name"] = tr.xpath("./td[2]/font/a/font/text()").extract_first()
                p_info["person_sex"] = tr.xpath("./td[3]/font/text()").extract_first()
                p_info["company_name"] = response.meta.get("company_name")
                yield p_info
                p_cert = PersonCertificateItem()
                p_cert["person_name"] = p_info["person_name"]
                p_cert["province_person_id"] = province_person_id
                p_cert["certificate_num"] = tr.xpath("./td[4]/font/text()").extract_first()
                p_cert["certificate_company_name"] = tr.xpath("./td[5]/font/text()").extract_first()
                p_cert["company_name"] = response.meta.get("company_name")
                p_cert["aptitude_type"] = "ע����"
                p_cert["aptitude_name"] = "ע�����ʦ"
                yield p_cert
