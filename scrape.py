from bs4 import BeautifulSoup
import requests

import csv
source=requests.get('https://medium.com/datadriveninvestor/best-ai-ml-data-science-blogs-to-follow-in-2019-c3598032e3b8').text
soup=BeautifulSoup(source,'lxml')
tit=soup.find('div',class_='ac ae af ag ah ec aj ak')
#print(tit.prettify())

csv_file=open('new.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['blog_title','blog_link','hyperlinks','author_name','blog_context'])

blog_content_main = [] 
blog_content_author = [] 
blog_content_link = [] 
hyperlink = [] 
blog_content_title = [] 
for link in tit.find_all('img',class_='ds t u em ak'):
    blog_content_link.append(link['src'])
#     print('LINKS ARE','     ',blog_link)
for para in tit.find_all('p',class_='hc hd ez at he b hf hg hh hi hj hk hl hm hn ho hp'):

    blog_content_main.append(para.text)
    #print(blog_content)
for blogt in tit.find_all('a',class_='dc by in io ip iq'):
    hyperlink.append(blogt['href'])
#   print('HYPERLINKS ARE','     ',hyperlinks)
for a_name in tit.find_all('strong',class_='he im'):
    blog_content_author.append(a_name.text[1:])
#   print(author_name)
for b_tit in tit.find_all('h1',class_='hq hr ez at as hs ht hu hv hw hx hy hz ia ib ic id'):
    blog_content_title.append(b_tit.text)
    
csv_writer.writerow([blog_content_title,blog_content_link,hyperlink,blog_content_author,blog_content_main])

   
csv_file.close()
