    # importing the requests library 
import requests 
import datetime
import oauth2
import json
import urllib.parse
import pprint
from django.http import JsonResponse


comsumer_key = 'rlyhPZTFDivlA9O8N3CK8H3gg'
comsumer_secret = 'uERg967cmJ5rETjb0ZV10z7kY7y93exxvFqnIxkJhVFnnvJktO'
token_key = '1117253226645086208-ySD1QakpKdnrYF6BHoa6Cbfap2JX03'
token_secret = 'p8V8auERryx11lcPYTH4oW7Sa5GpodSenmYJ62CcDCeAa'
comsumer = oauth2.Consumer(comsumer_key, comsumer_secret)
token = oauth2.Token(token_key, token_secret)


def topics(request,region_id):
    # trending topics
    # print(' consumerkey: ',comsumer_key,'\n','consumersecret: ',comsumer_secret,'\n','token_key: ',token_key,'\n','token_secret: ',token_secret)
    cliente = oauth2.Client(comsumer, token)
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
    saveSearch(query,request)
    return JsonResponse({'twittes': my_list})

def saveSearch(query,request):
    try:
        API_ENDPOINT = "http://localhost:3001/api/searchs"
        data = {
        'searchterm':query,
        'time':datetime.datetime.now(),
        'ip':get_client_ip(request)} 
        response = requests.post(url = API_ENDPOINT, data = data) 
        print(data,response)
    except:
        print("An exception occurred in saveSearch")

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip