import scrapy  

class firstSpider(scrapy.Spider): 
   name = "first" 
   allowed_domains = ["https://www.wikipedia.org/"] 
   start_urls = ["https://en.wikipedia.org/wiki/Edge_computing" ] 

   def parse(self, response): 
      filename = response.url.split("/")[-2] + '.html' 
      with open(filename, 'wb') as f: 
         f.write(response.body)
  