import oauth2
import json
import urllib.parse
import pprint
import os

from django.http import JsonResponse
def topics(request,region_id):
    comsumer_key = os.environ.get('CONSUMER_KEY')
    comsumer_secret = os.environ.get('CONSUMER_SECRET')
    token_key = os.environ.get('TOKEN_KEY')
    token_secret = os.environ.get('TOKEN_SECRET')
    print(' consumerkey: ',comsumer_key,'\n','consumersecret: ',comsumer_secret,'\n','token_key: ',token_key,'\n','token_secret: ',token_secret)
    comsumer = oauth2.Consumer(comsumer_key, comsumer_secret)
    token = oauth2.Token(token_key, token_secret)
    cliente = oauth2.Client(comsumer, token)
    # trending topics
    requisicao = cliente.request('https://api.twitter.com/1.1/trends/place.json?id=' + str(region_id))
    decodificar = requisicao[1].decode()
    trending = json.loads(decodificar)
    # print('result: ',trending['errors'])
    if 'errors' in trending:
        print(trending['errors'])
        return JsonResponse({'errors':trending['errors']})              
    else:
        topics = trending[0]['trends']
        my_list = []
        for topic in topics:
            my_list.append({'name':topic['name'],'url':topic['url']})
        return JsonResponse({'topics':my_list})  
def search(request,query):
    comsumer_key = os.environ.get('CONSUMER_KEY')
    comsumer_secret = os.environ.get('CONSUMER_SECRET')
    token_key = os.environ.get('TOKEN_KEY')
    token_secret = os.environ.get('TOKEN_SECRET')
    comsumer = oauth2.Consumer(comsumer_key, comsumer_secret)
    token = oauth2.Token(token_key, token_secret)
    cliente = oauth2.Client(comsumer, token)
    query_codificada = urllib.parse.quote(query)
    requisicao = cliente.request('https://api.twitter.com/1.1/search/tweets.json?q='+query_codificada+'&lang=pt')
    decodificar = requisicao[1].decode()
    objeto = json.loads(decodificar)
    twittes = objeto['statuses']
    my_list = []
    for twit in twittes:
        # pprint.pprint(twit)
        my_list.append({
            'name':twit['user']['name'],
            'screen_name':twit['user']['screen_name'],
            'image_url':twit['user']['profile_image_url_https'],
            'text':twit['text'],
            'id':twit['id_str']
        })
    return JsonResponse({'twittes': my_list})