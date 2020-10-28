
class Dicionario:
    valida_Doc = {
        'Concepts':[],
        'Keywords':[],
        'Entities':[],
        'Sintaxes':[],
        'Resumo':'',
        'Documento':''
    }

    def __init__(self):
        self.dicionario = {
            0:{
                'Concepts':[{
                "text": "Recurso especial",
                "relevance": 0.916226,
            },
            {
                "text": "Recurso extraordinário",
                "relevance": 0.797744,
            },
            {
                "text": "Inovação",
                "relevance": 0.719832,
            },
            {
                "text": "Recurso",
                "relevance": 0.698337,
            }],
                'Keywords':[{
                "text": "AGRAVO REGIMENTAL",
                "sentiment": {
                "score": -0.613393,
                "label": "negative"
                },
                "relevance": 0.804081,
                "count": 2
            },
            {
                "text": "COMPENSAÇÃO INTEGRAL",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.673508,
                "count": 1
            },
            {
                "text": "REINCIDÊNCIA ESPECÍFICA",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.533272,
                "count": 1
            },
            {
                "text": "NO RECURSO ESPECIAL",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.523558,
                "count": 1
            },
            {
                "text": "RÉU MULTIRREINCIDENTE",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.512871,
                "count": 1
            },
            {
                "text": "ROUBO MAJORADO",
                "sentiment": {
                "score": -0.674011,
                "label": "negative"
                },
                "relevance": 0.512871,
                "count": 1
            },
            {
                "text": "ALEGAÇÃO",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.488259,
                "count": 1
            },
            {
                "text": "ACRÉSCIMO DE FUNDAMENTOS NA DECISÃO",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.481514,
                "count": 1
            },
            {
                "text": "MENORIDADE RELATIVA",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.460635,
                "count": 1
            },
            {
                "text": "PLEITO",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.412648,
                "count": 2
            }],
                'Entities':[{
                "type": "Organization",
                "text": "AGRAVO REGIMENTAL",
                "relevance": 0.95577,
                "count": 1
            },
            {
                "type": "Organization",
                "text": "INTEGRAL",
                "relevance": 0.457162,
                "count": 1
            },
            {
                "type": "Organization",
                "text": "FUNDAMENTOS",
                "relevance": 0.314423,
                "count": 1
            }],
                'Sintaxes':[{
                "text": "AGRAVO REGIMENTAL NO RECURSO ESPECIAL.",
                "location": [
                0,
                38
                ]
            },
            {
                "text": "PENAL.",
                "location": [
                39,
                45
                ]
            },
            {
                "text": "ROUBO MAJORADO.",
                "location": [
                46,
                61
                ]
            },
            {
                "text": "PLEITO PELA COMPENSAÇÃO INTEGRAL ENTRE A REINCIDÊNCIA ESPECÍFICA E A MENORIDADE RELATIVA.",
                "location": [
                62,
                151
                ]
            },
            {
                "text": "ALEGAÇÃO DE QUE HOUVE INOVAÇÃO OU ACRÉSCIMO DE FUNDAMENTOS NA DECISÃO AGRAVADA PARA NEGAR O PLEITO.",
                "location": [
                152,
                251
                ]
            },
            {
                "text": "INSUBSISTENTE.",
                "location": [
                252,
                266
                ]
            },
            {
                "text": "RÉU MULTIRREINCIDENTE.",
                "location": [
                267,
                289
                ]
            },
            {
                "text": "IMPOSSIBILIDADE.",
                "location": [
                290,
                306
                ]
            },
            {
                "text": "PRECEDENTES.",
                "location": [
                307,
                319
                ]
            },
            {
                "text": "AGRAVO REGIMENTAL DESPROVIDO",
                "location": [
                320,
                348
                ]
            }],
                'Resumo':'AGRAVO REGIMENTAL NO RECURSO ESPECIAL. PENAL. ROUBO MAJORADO. PLEITO PELA COMPENSAÇÃO INTEGRAL ENTRE A REINCIDÊNCIA ESPECÍFICA E A MENORIDADE RELATIVA. ALEGAÇÃO DE QUE HOUVE INOVAÇÃO OU ACRÉSCIMO DE FUNDAMENTOS NA DECISÃO AGRAVADA PARA NEGAR O PLEITO. INSUBSISTENTE. RÉU MULTIRREINCIDENTE. IMPOSSIBILIDADE. PRECEDENTES. AGRAVO REGIMENTAL DESPROVIDO'
            ,
                'Documento':'https://scon.stj.jus.br/SCON/GetInteiroTeorDoAcordao?num_registro=201901738903&dt_publicacao=29/06/2020'
            },
            1:{
                'Concepts':[{
                "text": "Droga",
                "relevance": 0.984652,
            },
            {
                "text": "Habeas corpus",
                "relevance": 0.984322,
            },
            {
                "text": "Guarda Municipal",
                "relevance": 0.945645,
            },
            {
                "text": "Flagrante",
                "relevance": 0.920487,
            },
            {
                "text": "Crime",
                "relevance": 0.870609,
            },
            {
                "text": "Narcotráfico",
                "relevance": 0.753188,
            },
            {
                "text": "STJ",
                "relevance": 0.686557,
            },
            {
                "text": "Reclusão",
                "relevance": 0.604496,
            }],
                'Keywords':[{
                "text": "RECONHECIMENTO DA PROPRIEDADE DA DROGA",
                "sentiment": {
                "score": -0.724676,
                "label": "negative"
                },
                "relevance": 0.70747,
                "count": 1
            },
            {
                "text": "INCIDÊNCIA DA SÚMULA N.",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.691078,
                "count": 1
            },
            {
                "text": "CRIME DE TRÁFICO DE DROGAS",
                "sentiment": {
                "score": -0.590386,
                "label": "negative"
                },
                "relevance": 0.647338,
                "count": 1
            },
            {
                "text": "WRIT NÃO CONHECIDO",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.644134,
                "count": 1
            },
            {
                "text": "DOSIMETRIA DA PENA",
                "sentiment": {
                "score": -0.695658,
                "label": "negative"
                },
                "relevance": 0.56148,
                "count": 1
            },
            {
                "text": "CONSUMO PESSOAL",
                "sentiment": {
                "score": -0.776587,
                "label": "negative"
                },
                "relevance": 0.51825,
                "count": 1
            },
            {
                "text": "INCIDÊNCIA DA ATENUANTE DA CONFISSÃO ESPONTÂNEA",
                "sentiment": {
                "score": -0.825957,
                "label": "negative"
                },
                "relevance": 0.497369,
                "count": 1
            },
            {
                "text": "NECESSIDADE DE REEXAME FÁTICO-PROBATÓRIO",
                "sentiment": {
                "score": -0.664238,
                "label": "negative"
                },
                "relevance": 0.474076,
                "count": 1
            },
            {
                "text": "HABEAS CORPUS SUBSTITUTIVO DE RECURSO PRÓPRIO",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.474076,
                "count": 1
            },
            {
                "text": "INVIABILIDADE DE EXAME NA VIA ELEITA",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.474076,
                "count": 1
            },
            {
                "text": "PRISÃO",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.456808,
                "count": 1
            },
            {
                "text": "FLAGRANTE PELA GUARDA MUNICIPAL",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.453761,
                "count": 1
            },
            {
                "text": "INADEQUAÇÃO",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.43308,
                "count": 1
            },
            {
                "text": "NULIDADE",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.406958,
                "count": 1
            },
            {
                "text": "STJ",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.406958,
                "count": 1
            },
            {
                "text": "ABSOLVIÇÃO",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.406958,
                "count": 1
            },
            {
                "text": "CPP",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.406958,
                "count": 1
            },
            {
                "text": "ART",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.406958,
                "count": 1
            },
            {
                "text": "POSSIBILIDADE",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.406958,
                "count": 1
            }],
                'Entities':[{
                "type": "Organization",
                "text": "VIA ELEITA",
                "relevance": 0.954934,
                "count": 2
            },
            {
                "type": "Organization",
                "text": "CRIME DE TRÁFICO DE DROGAS",
                "relevance": 0.640048,
                "count": 1
            },
            {
                "type": "Organization",
                "text": "GUARDA MUNICIPAL",
                "relevance": 0.561367,
                "count": 1
            },
            {
                "type": "Organization",
                "text": "CPP",
                "relevance": 0.506532,
                "count": 1
            },
            {
                "type": "Number",
                "text": "301",
                "relevance": 0.337506,
                "count": 1
            },
            {
                "type": "Organization",
                "text": "DOSIMETRIA DA PENA",
                "relevance": 0.327519,
                "count": 1
            }],
                'Sintaxes':[{
                "text": "HABEAS CORPUS SUBSTITUTIVO DE RECURSO PRÓPRIO.",
                "location": [
                0,
                46
                ]
            },
            {
                "text": "INADEQUAÇÃO DA VIA ELEITA.",
                "location": [
                47,
                73
                ]
            },
            {
                "text": "CRIME DE TRÁFICO DE DROGAS.",
                "location": [
                74,
                101
                ]
            },
            {
                "text": "NULIDADE.",
                "location": [
                102,
                111
                ]
            },
            {
                "text": "PRISÃO EM FLAGRANTE PELA GUARDA MUNICIPAL.",
                "location": [
                112,
                154
                ]
            },
            {
                "text": "POSSIBILIDADE.",
                "location": [
                155,
                169
                ]
            },
            {
                "text": "ART.",
                "location": [
                170,
                174
                ]
            },
            {
                "text": "301 DO CPP.",
                "location": [
                175,
                186
                ]
            },
            {
                "text": "PRETENDIDA ABSOLVIÇÃO.",
                "location": [
                187,
                209
                ]
            },
            {
                "text": "INVIABILIDADE DE EXAME NA VIA ELEITA.",
                "location": [
                210,
                247
                ]
            },
            {
                "text": "NECESSIDADE DE REEXAME FÁTICO-PROBATÓRIO.",
                "location": [
                248,
                289
                ]
            },
            {
                "text": "DOSIMETRIA DA PENA.",
                "location": [
                290,
                309
                ]
            },
            {
                "text": "RECONHECIMENTO DA PROPRIEDADE DA DROGA PARA CONSUMO PESSOAL.",
                "location": [
                310,
                370
                ]
            },
            {
                "text": "NÃO INCIDÊNCIA DA ATENUANTE DA CONFISSÃO ESPONTÂNEA.",
                "location": [
                371,
                423
                ]
            },
            {
                "text": "INCIDÊNCIA DA SÚMULA N. 630/STJ.",
                "location": [
                424,
                456
                ]
            },
            {
                "text": "WRIT NÃO CONHECIDO.",
                "location": [
                457,
                476
                ]
            }],
                'Resumo':'HABEAS CORPUS SUBSTITUTIVO DE RECURSO PRÓPRIO. INADEQUAÇÃO DA VIA ELEITA. CRIME DE TRÁFICO DE DROGAS. NULIDADE. PRISÃO EM FLAGRANTE PELA GUARDA MUNICIPAL. POSSIBILIDADE. ART. 301 DO CPP. PRETENDIDA ABSOLVIÇÃO. INVIABILIDADE DE EXAME NA VIA ELEITA. NECESSIDADE DE REEXAME FÁTICO-PROBATÓRIO. DOSIMETRIA DA PENA. RECONHECIMENTO DA PROPRIEDADE DA DROGA PARA CONSUMO PESSOAL. NÃO INCIDÊNCIA DA ATENUANTE DA CONFISSÃO ESPONTÂNEA. INCIDÊNCIA DA SÚMULA N. 630/STJ. WRIT NÃO CONHECIDO'
            ,
                'Documento':'https://scon.stj.jus.br/SCON/GetInteiroTeorDoAcordao?num_registro=202001321559&dt_publicacao=31/08/2020'
            },
            2:{
                'Concepts':[{
                "text": "Júri",
                "relevance": 0.992933,
            },
            {
                "text": "Habeas corpus",
                "relevance": 0.990244,
            },
            {
                "text": "Tribunal",
                "relevance": 0.858564,
            },
            {
                "text": "Réu",
                "relevance": 0.780425,
            },
            {
                "text": "Poder Judiciário",
                "relevance": 0.674307,
            },
            {
                "text": "Homicídio",
                "relevance": 0.636577,
            },
            {
                "text": "STJ",
                "relevance": 0.633905,
            },
            {
                "text": "Crime",
                "relevance": 0.619957,
            }],
                'Keywords':[{
                "text": "PENA-BASE",
                "sentiment": {
                "score": -0.727702,
                "label": "negative"
                },
                "relevance": 0.667835,
                "count": 1
            },
            {
                "text": "CIRCUNSTÂNCIA NEUTRA",
                "sentiment": {
                "score": -0.723761,
                "label": "negative"
                },
                "relevance": 0.667232,
                "count": 1
            },
            {
                "text": "CONFISSÃO ESPONTÂNEA",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.585854,
                "count": 1
            },
            {
                "text": "QUANTUM DE REDUÇÃO",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.585854,
                "count": 1
            },
            {
                "text": "COMPORTAMENTO DA VÍTIMA",
                "sentiment": {
                "score": -0.74309,
                "label": "negative"
                },
                "relevance": 0.575051,
                "count": 1
            },
            {
                "text": "PENA SUPERIOR",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.574607,
                "count": 1
            },
            {
                "text": "CIRCUNSTÂNCIA JUDICIAL DESFAVORÁVEL",
                "sentiment": {
                "score": -0.762563,
                "label": "negative"
                },
                "relevance": 0.572259,
                "count": 1
            },
            {
                "text": "FLAGRANTE ILEGALIDADE EVIDENCIADA",
                "sentiment": {
                "score": -0.608461,
                "label": "negative"
                },
                "relevance": 0.554993,
                "count": 1
            },
            {
                "text": "WRIT NÃO CONHECIDO",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.535645,
                "count": 1
            },
            {
                "text": "HOMICÍDIO QUALIFICADO",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.53494,
                "count": 1
            },
            {
                "text": "TRIBUNAL DO JÚRI",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.53494,
                "count": 1
            },
            {
                "text": "DEPOIMENTO DO RÉU",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.527429,
                "count": 1
            },
            {
                "text": "CRITÉRIO DO ITER CRIMINIS PERCORRIDO OBSERVADO",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.47306,
                "count": 1
            },
            {
                "text": "HABEAS CORPUS SUBSTITUTIVO DE RECURSO PRÓPRIO",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.47306,
                "count": 1
            },
            {
                "text": "MAIORES INCURSÕES QUE DEMANDARIAM REVOLVIMENTO FÁTICO-PROBATÓRIO",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.471654,
                "count": 1
            },
            {
                "text": "INTERFERÊCIA DECISIVA DA VÍTIMA NA PRÁTICA DELITIVA NÃO EVIDENCIADA",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.466334,
                "count": 1
            },
            {
                "text": "ATENUANTE",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.46086,
                "count": 1
            },
            {
                "text": "ORDEM",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.444049,
                "count": 1
            },
            {
                "text": "REGIME",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.444049,
                "count": 1
            },
            {
                "text": "SÚMULA",
                "sentiment": {
                "score": -0.608461,
                "label": "negative"
                },
                "relevance": 0.435083,
                "count": 1
            },
            {
                "text": "TENTATIVA",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.425438,
                "count": 2
            },
            {
                "text": "OFÍCIO",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.425438,
                "count": 1
            },
            {
                "text": "ANOS",
                "sentiment": {
                "score": -0.762563,
                "label": "negative"
                },
                "relevance": 0.425438,
                "count": 1
            },
            {
                "text": "STJ",
                "sentiment": {
                "score": -0.608461,
                "label": "negative"
                },
                "relevance": 0.425438,
                "count": 1
            },
            {
                "text": "PLENÁRIO",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.425438,
                "count": 1
            },
            {
                "text": "FAVORÁVEL",
                "sentiment": {
                "score": -0.723761,
                "label": "negative"
                },
                "relevance": 0.425438,
                "count": 1
            },
            {
                "text": "DOSIMETRIA",
                "sentiment": {
                "score": -0.690582,
                "label": "negative"
                },
                "relevance": 0.425438,
                "count": 1
            },
            {
                "text": "INADEQUAÇÃO",
                "sentiment": {
                "score": 0,
                "label": "neutral"
                },
                "relevance": 0.425438,
                "count": 1
            }],
                'Entities':[{
                "type": "Organization",
                "text": "INADEQUAÇÃO",
                "relevance": 0.950251,
                "count": 1
            },
            {
                "type": "Organization",
                "text": "PENA-BASE",
                "relevance": 0.887534,
                "count": 1
            },
            {
                "type": "Organization",
                "text": "NEUTRA",
                "relevance": 0.832792,
                "count": 1
            },
            {
                "type": "Organization",
                "text": "INTERFERÊCIA DECISIVA DA VÍTIMA NA PRÁTICA DELITIVA",
                "relevance": 0.781762,
                "count": 1
            },
            {
                "type": "Organization",
                "text": "CONFISSÃO ESPONTÂNEA QUALIFICADA",
                "relevance": 0.708737,
                "count": 1
            },
            {
                "type": "Organization",
                "text": "TRIBUNAL DO JÚRI",
                "relevance": 0.675563,
                "count": 1
            },
            {
                "type": "Organization",
                "text": "ATENUANTE",
                "relevance": 0.656708,
                "count": 1
            },
            {
                "type": "Organization",
                "text": "SÚMULA",
                "relevance": 0.586183,
                "count": 1
            },
            {
                "type": "Organization",
                "text": "QUANTUM DE REDUÇÃO PELA TENTATIVA",
                "relevance": 0.494257,
                "count": 1
            },
            {
                "type": "Organization",
                "text": "ITER",
                "relevance": 0.445492,
                "count": 1
            },
            {
                "type": "Organization",
                "text": "STJ",
                "relevance": 0.386377,
                "count": 1
            }],
                'Sintaxes':[ {
                "text": "PENAL.",
                "location": [
                0,
                6
                ]
            },
            {
                "text": "HABEAS CORPUS SUBSTITUTIVO DE RECURSO PRÓPRIO.",
                "location": [
                7,
                53
                ]
            },
            {
                "text": "INADEQUAÇÃO.",
                "location": [
                54,
                66
                ]
            },
            {
                "text": "HOMICÍDIO QUALIFICADO.",
                "location": [
                67,
                89
                ]
            },
            {
                "text": "TENTATIVA.",
                "location": [
                90,
                100
                ]
            },
            {
                "text": "DOSIMETRIA.",
                "location": [
                101,
                112
                ]
            },
            {
                "text": "PENA-BASE.",
                "location": [
                113,
                123
                ]
            },
            {
                "text": "COMPORTAMENTO DA VÍTIMA.",
                "location": [
                124,
                148
                ]
            },
            {
                "text": "CIRCUNSTÂNCIA NEUTRA OU FAVORÁVEL.",
                "location": [
                149,
                183
                ]
            },
            {
                "text": "INTERFERÊCIA DECISIVA DA VÍTIMA NA PRÁTICA DELITIVA NÃO EVIDENCIADA.",
                "location": [
                184,
                252
                ]
            },
            {
                "text": "CONFISSÃO ESPONTÂNEA QUALIFICADA.",
                "location": [
                253,
                286
                ]
            },
            {
                "text": "TRIBUNAL DO JÚRI.",
                "location": [
                287,
                304
                ]
            },
            {
                "text": "ATENUANTE APRESENTA NO DEPOIMENTO DO RÉU EM PLENÁRIO.",
                "location": [
                305,
                358
                ]
            },
            {
                "text": "SÚMULA 545/STJ.",
                "location": [
                359,
                374
                ]
            },
            {
                "text": "FLAGRANTE ILEGALIDADE EVIDENCIADA.",
                "location": [
                375,
                409
                ]
            },
            {
                "text": "QUANTUM DE REDUÇÃO PELA TENTATIVA.",
                "location": [
                410,
                444
                ]
            },
            {
                "text": "CRITÉRIO DO ITER CRIMINIS PERCORRIDO OBSERVADO.",
                "location": [
                445,
                492
                ]
            },
            {
                "text": "MAIORES INCURSÕES QUE DEMANDARIAM REVOLVIMENTO FÁTICO-PROBATÓRIO.",
                "location": [
                493,
                558
                ]
            },
            {
                "text": "REGIME FECHADO JUSTIFICADO.",
                "location": [
                559,
                586
                ]
            },
            {
                "text": "PENA SUPERIOR A 4 E INFERIOR A 8 ANOS.",
                "location": [
                587,
                625
                ]
            },
            {
                "text": "CIRCUNSTÂNCIA JUDICIAL DESFAVORÁVEL.",
                "location": [
                626,
                662
                ]
            },
            {
                "text": "WRIT NÃO CONHECIDO.",
                "location": [
                663,
                682
                ]
            },
            {
                "text": "ORDEM CONCEDIDA DE OFÍCIO.",
                "location": [
                683,
                709
                ]
            }],
                'Resumo':'PENAL. HABEAS CORPUS SUBSTITUTIVO DE RECURSO PRÓPRIO. INADEQUAÇÃO. HOMICÍDIO QUALIFICADO. TENTATIVA. DOSIMETRIA. PENA-BASE. COMPORTAMENTO DA VÍTIMA. CIRCUNSTÂNCIA NEUTRA OU FAVORÁVEL. INTERFERÊCIA DECISIVA DA VÍTIMA NA PRÁTICA DELITIVA NÃO EVIDENCIADA. CONFISSÃO ESPONTÂNEA QUALIFICADA. TRIBUNAL DO JÚRI. ATENUANTE APRESENTA NO DEPOIMENTO DO RÉU EM PLENÁRIO. SÚMULA 545/STJ. FLAGRANTE ILEGALIDADE EVIDENCIADA. QUANTUM DE REDUÇÃO PELA TENTATIVA. CRITÉRIO DO ITER CRIMINIS PERCORRIDO OBSERVADO. MAIORES INCURSÕES QUE DEMANDARIAM REVOLVIMENTO FÁTICO-PROBATÓRIO. REGIME FECHADO JUSTIFICADO. PENA SUPERIOR A 4 E INFERIOR A 8 ANOS. CIRCUNSTÂNCIA JUDICIAL DESFAVORÁVEL. WRIT NÃO CONHECIDO. ORDEM CONCEDIDA DE OFÍCIO. '
            ,
                'Documento':'https://scon.stj.jus.br/SCON/GetInteiroTeorDoAcordao?num_registro=202001706966&dt_publicacao=03/09/2020'
            }
        }

    def getDicionario(self):
        return self.dicionario