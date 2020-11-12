from django.shortcuts import render
from django.http import HttpResponse
from django.http import QueryDict

import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features,EntitiesOptions,ConceptsOptions,SyntaxOptions,KeywordsOptions

from buscador.dicionario import Dicionario
a = Dicionario()
# from templates.buscador import index


def index(request):
    # return HttpResponse('<h1>Hello World</h1>')
    return render(request,'index.html')

def listagem(request):
    token= 'sQ3sDnp9bK7cm-m6jtwtrsJmUQ9Rk_E1eIUOwahXEjri'

    authenticator = IAMAuthenticator(token)
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2020-08-01',
        authenticator=authenticator
    )
    natural_language_understanding.set_service_url(
        'https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/c13d7eae-7792-45c5-931f-6a375605d467'
    )
    response = natural_language_understanding.analyze(
    text=request.GET['busca'],
    features=Features(
        entities=EntitiesOptions(limit=50),
        concepts=ConceptsOptions(),
        syntax=SyntaxOptions(sentences=True),
        keywords=KeywordsOptions(sentiment=True)

    )).get_result()

    valida_Busca = {
        'Concepts':[],
        'Keywords':[],
        'Entities':[],
        'Sintaxes':[]
    }

    concepts=[]
    for b in response['concepts']:
        if b['relevance'] > 0.4:
            concepts.append(b)
    valida_Busca['Concepts'].append(concepts)

    keywords =[]
    for c in response['keywords']:
        if c['relevance'] > 0.4:
            keywords.append(c)
    valida_Busca['Keywords'].append(keywords)

    entities=[]
    for e in response['entities']:
        if e["relevance"] > 0.3:
            entities.append(e)
    valida_Busca['Entities'].append(entities)

    sitaxes=[]
    for d in response['syntax']['sentences']:
        sitaxes.append(d)
    valida_Busca['Sintaxes'].append(sitaxes)

    base = a.getDicionario()
    somaTotal=[]
    # print(base[0]["Concepts"])
    soma=0
    for i in base[0]["Concepts"]:
        # print(i)
        for compara in valida_Busca["Concepts"]:
            for ele in compara:
                if i['text'] == ele["text"]:
                    soma+=1
    
    for index in range(3):
        soma=0
        for x in base[index]["Concepts"]:
            for compara in valida_Busca["Concepts"]:
                    for ele in compara:
                        if x["text"] in ele["text"]:
                            soma+=1
        for x in base[index]["Keywords"]:
            for compara in valida_Busca["Keywords"]:
                    for ele in compara:
                        if x["text"] in ele["text"]:
                            soma+=0.8
        for x in base[index]["Entities"]:
            for compara in valida_Busca["Entities"]:
                    for ele in compara:
                        if x["text"] in ele["text"]:
                            soma+=0.6
        for x in base[index]["Sintaxes"]:
            for compara in valida_Busca["Sintaxes"]:
                    for ele in compara:
                        if x["text"] in ele["text"]:
                            soma+=0.2
        somaTotal.append(soma)

    somatoria=0
    for calc in somaTotal:
        somatoria += calc
    somatoria/=len(somaTotal)

    
    retornoValores=[]
    for q in range(len(somaTotal)):
        retornoIndices=[]
        if somaTotal[q] >= somatoria:
            retornoIndices.append(q)
            retornoIndices.append(somaTotal[q])
            retornoValores.append(retornoIndices)

    print(retornoValores)
    retornoIndices = sorted(retornoValores, key= lambda valores:valores[1], reverse=True)
    print(retornoIndices)
    retorno={
        'data':[]
    }
    retorno['data'].append({'buscado':request.GET['busca']})
    documento={
        'lista':[]
    }
    for u in retornoIndices:
        documento['lista'].append({'documento':base[u[0]]["Documento"], 'resumo':base[u[0]]["Resumo"]})
    retorno['data'].append(documento)
    

    #return HttpResponse(json.dumps(retorno, indent=2))
    return render(request,'index.html',context=retorno)