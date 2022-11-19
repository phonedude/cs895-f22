from urllib.parse import urlparse
import pandas as pd
import json

def alphabetize_params(url):
    o = urlparse(url)
    params = sorted(o.query.split('&'))
    return '&'.join(params)

def filter_timemap(timemap):
    try:
        jso = pd.read_json(timemap)
    except:
        return
    
    urif = alphabetize_params(jso.loc['first']['original_uri'])
    
    mementos = jso.loc['list']['mementos']
    mementos2 = []
    for memento in mementos:
        uric = alphabetize_params(memento['uri'])
        if uric == urif:
            mementos2.append(memento)
    
    json2 = {}
    json2['original_url'] = jso.loc['first']['original_uri']
    json2['self'] = jso.loc['first']['self']
    json2['mementos'] = {}
    json2['mementos']['list'] = mementos2
    json2['mementos']['first'] = mementos2[0]
    json2['mementos']['last'] = mementos2[-1]
    json2['timemap_uri'] = {}
    
    prefix = json2['self'].replace('json/' + json2['original_url'], '')
    json2['timemap_uri']['link_format'] = prefix + 'link/' + json2['original_url']
    json2['timemap_uri']['json_format'] = json2['self']
    json2['timemap_uri']['cdxj_format'] = prefix + 'cdxj/' + json2['original_url']
    json2['timegate_uri'] = jso.loc['first']['timegate_uri']
    
    print(json.dumps(json2, indent = 2))

filter_timemap('00051.json')
    
    
