import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests
import time





# get url

url="https://stackoverflow.com/questions"




page=requests.get(url)
soup=BeautifulSoup(page.content)

questions_container=soup.find('div',attrs={"itemprop":"mainEntity"})
questions=questions_container.find_all("div",attrs={"class":"bb bc-black-200"})

views=[]
askes=[]
votes=[]
links=[]
titles=[]
discriptions=[]
tools_questions=[]
time_questions=[]
username_questions=[]

for question in questions:
  
  prop=question.find_all("div",attrs={"class":"s-post-summary--stats-item"})
  vote=prop[0].get_attribute_list('title')#votes
  ask=prop[1].get_attribute_list('title')#asked
  view=prop[2].get_attribute_list('title')#views
  views.append(view[0])
  askes.append(ask[0])
  votes.append(str(vote))
  link=question.find('div',attrs={"class":"s-post-summary--content"}).find('h3').find('a')
  
  #link
  href_question=link.get_attribute_list('href')
  links.append(href_question[0].replace('/questions',url))
  
  #title
  title=link.find('span').getText()
  titles.append(title)
  
  #discription
  discription=question.find("div",attrs={"class":"s-post-summary--content-excerpt"}).getText()
  discriptions.append(discription)
  
  #third section
  section3=question.find("div",attrs={'class':"s-post-summary--meta"})
  
  #tools
  tools=section3.find("ul").find_all('a')
  tools_question=[]
  
  for tool in tools:
    tools_question.append(tool.getText())
  tools_questions.append(tools_question)
  
  # username
  username=section3.find("div",attrs={"class":"s-user-card s-user-card__minimal"}).find("div",attrs={'class':"s-user-card--info"}).find("div",attrs={"class":"s-user-card--link d-flex gs4"}).find('span').getText()
  username_questions.append(username)
  
  #time
  time=section3.find("time").find('span').getText()
  time_questions.append(time)

questions={
    "username":username_questions,
    "title":titles,
    "discription":discriptions,
    "tools":tools_questions,
    "time":time_questions,
    "views":views,
    "askes":askes,
    "votes":votes,
    "links":links,
}


pd.DataFrame(questions).to_excel('questions.xlsx')
pd.DataFrame(questions).to_csv('questions.csv')






#note
# css_soup.select("p.strikeout.body")
# [<p class="body strikeout"></p>]

# soup.find_all("a", attrs={"class": "sister"})
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
