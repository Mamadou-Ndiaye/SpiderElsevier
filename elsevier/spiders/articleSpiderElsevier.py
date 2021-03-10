import scrapy
from scrapy import Request

class SpiderArticleScienceDiect(scrapy.Spider):
    name = 'articleElsevier'
    start_urls = ['https://www.scirp.org/journal/articles.aspx']
    #start_urls = ['https://www.sciencedirect.com/articlelist/covid?offset=100']
    #filtrer une url plusieurs fois
    #custom_settings = {
    #    'DUPEFILTER_CLASS': 'scrapy.dupefilters.BaseDupeFilter',
    #}

##    def parse(self, response):
##        #yield response.follow(self.start_urls[0], self.autreparse)
##        return Request(self.start_urls[0], callback = self.autreparse)
##
##    def autreparse(self,response):
##        items = dict()
##        Domain = self.start_urls[0].rsplit('/')
##        all_li_items = response.css("#srp-results-list .push-m")
##        for li in all_li_items:
##            items['type']=li.css('.u-clr-grey8::text').extract_first()
##            items['titre'] = li.css('.text-s::text').extract_first()
##            Liens = li.css('.text-s').xpath('@href').get()
##            items['url']= str(Domain[0]) + "//" + str(Domain[2]) + str(Liens)
##            items['book'] = li.css('.subtype-srctitle-link span::text').extract_first()
##            items['date'] = li.css('.preceding-comma:nth-child(2)::text').extract_first()
##            items['auteurs1'] = li.css('.hor li:nth-child(1) .author::text').extract_first()
##            items['auteurs2'] = li.css('.hor li:nth-child(2) .author::text').extract_first()
##            #a=response.follow(Liens, self.secondparse)
##            #yield items
##            #items['abs']=response.follow(Liens, self.secondparse)
##            yield items
##
##    def secondparse(self,response):
##         yield {'abs':response.css('.author p::text').extract()}
    
    def parse(self,response):
        items = dict()
        # title = response.css("title::text").extract()
        Domain = self.start_urls[0].rsplit('/')
        

        #def autreparse(response):
        #   return response.css('.author p::text').extract()
            
            
        all_li_items = response.css("#ContentPlaceHolder1_div_showpaper ul")
        for ul in all_li_items:
            Titre_ = ul.css('a::text').extract_first()
            Titre = Titre_.replace("\r\n","").strip() # suppression de \n et des espaces de deb et de fin
            Types = ul.css('p:nth-child(3) > a>i::text').extract_first()
            Liens = ul.css('a').xpath('@href').get() #recupere liens 
            Liens= "https://www.scirp.org/journal/"+str(Liens) 
            #print("https://www.scirp.org/journal/"+str(Liens))
            #lienComplet = str(Domain[0]) + "//" + str(Domain[2]) + str(Liens)
            """ Book = li.css('.subtype-srctitle-link span::text').extract_first()"""
            #sDate = ul.css("p:nth-child(2)::text").extract_first()
            #print("Date is +++ ",Date)
            Auteurs1 = ul.css('p>a::text').extract()
            #print("++++",Auteurs1)
            Auteur_2=Auteurs1.pop(-2) # Ne fait pas de la liste des auteurs espaces ...
            #print("++++",Auteur)
            Auteur_1=Auteurs1.pop()   # Ne fait pas de la liste des auteurs espaces ...
            #Convert to chaine the list
            Auteurs=" ".join(str(x) for x in Auteurs1)
            
            #Auteurs2 = li.css('.hor li:nth-child(2) .author::text').extract_first()
            #abstract = response.follow(Liens, self.secondparse)
           
            items['type']= Types
            items['titre']= Titre
            #items['url'] = response.urljoin(Liens)
            items['url'] = Liens
            items['date'] = "2021"
            items['auteurs']= Auteurs
            #items['abstract'] = abstract
            yield items
            
        #next_page = response.css('#srp-pagination a::attr(href)').get()
        #next_page = response.css('a.paginator a::attr(href)').get()
        #items['test'] = response.urljoin(next_page)
        #yield Request(response.urljoin(next_url), callback=self.parse_anime_list_page)
        #print("---------",response.urljoin("?page="+str(3)))
        """if next_page is not None:
            #yield response.follow(next_page, callback =self.parse)
            yield Request(response.urljoin(next_page), callback=self.parse)"""
        for next_page in range(1,4085):
            #yield response.follow(next_page, callback =self.parse)
            #print("---------",response.urljoin("?page="+str(next_page)))
            yield Request(response.urljoin("?page="+str(next_page)), callback=self.parse)
##    
##    def secondparse(self,response):
##        yield {'abs':response.css('.author p::text').extract()} 
        
