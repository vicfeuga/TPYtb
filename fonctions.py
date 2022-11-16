#!/usr/bin/env python
import json
import requests
from bs4 import BeautifulSoup
from time import sleep
import re

#create ytb video url
def idtoURL(id):
   return('https://www.youtube.com/watch?v='+id)

#convert url to request
def URLtoRes(url):
   data=[]
   #User Agent
   headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"}
   #requete de connexion
   return(requests.get(url,headers=headers))
   
#create soup
def RestoSoup(r):
   #parse la page resultat
   return(BeautifulSoup(r.text, 'html.parser'))

#return number of likes
def find_likes(soup):
   data2 = re.search(r"var ytInitialData = ({.*?});", soup.prettify()).group(1)
   data2 = json.loads(data2)
   videoPrimaryInfoRenderer = data2['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer']
   likes_str = videoPrimaryInfoRenderer['videoActions']['menuRenderer']['topLevelButtons'][0]['segmentedLikeDislikeButtonRenderer']['likeButton']['toggleButtonRenderer']['defaultText']['accessibility']['accessibilityData']['label']
   likes_str = likes_str.split(' ')[0].replace(',','')[:-6]
   likes_str = likes_str.replace('\u202f','')
   return(int(likes_str))

#find all informations of a video
def find_informations(i):
   
   d = dict()
   d['id_vid_video'] = i
   r = URLtoRes(idtoURL(i))

   try:
      soup = RestoSoup(r)
      
      data = re.search(r"var ytInitialPlayerResponse = ({.*?});", soup.prettify()).group(1)
      data=json.loads(data)

      id = data['videoDetails']['videoId']

      d['id_vid_video'] = id

      d['titre'] = data['videoDetails']['title']
      d['nom_chaine'] = data['videoDetails']['author']
      d['description'] = data['videoDetails']['shortDescription']
      d['liens_desc'] = re.findall(r'(https?://\S+)', d['description'])
      d['nb_likes'] = find_likes(soup)

   except:
      pass

   return(d)

#write down the output file
def read_input(input_para):
   with open(input_para,'r') as f:
      return(json.load(f))

#write down the output file
def write_output(output_para,data):
   with open(output_para,'w') as f:
        json.dump(data,f,indent=4,ensure_ascii=False)