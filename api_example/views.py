import oauth2
import json
import urllib.parse
import pprint

from django.http import JsonResponse
def names(request):
    comsumer_key = 'wk6YZttOzS50DvnvZvDwizULk'
    comsumer_secret = 'z1VbsaPJijbjzpJ1R9T2CY6LinUkBY2rsTgeQe2T6XlAH2jCKu'
    token_key = '1117253226645086208-CNnRyCPU9q0jpslFi83fglWeisbd2I'
    token_secret = 'ImDjKuEnbJsBAhRgKe4MKLi7gMHQ1Itopahx3wIR74EhY'

    comsumer = oauth2.Consumer(comsumer_key, comsumer_secret)
    token = oauth2.Token(token_key, token_secret)
    cliente = oauth2.Client(comsumer, token)
    # trending topics
    region_id = 23424768
    requisicao = cliente.request('https://api.twitter.com/1.1/trends/place.json?id=' + str(region_id))
    decodificar = requisicao[1].decode()
    trending = json.loads(decodificar,)
    topics = trending[0]['trends']
    my_list = []
    for topic in topics:
        my_list.append({'name':topic['name'],'url':topic['url']})
    return JsonResponse({'res':my_list})  
    # return JsonResponse({'names': ['William', 'Rod', 'Grant']})
