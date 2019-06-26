import os
import os.path
import sys

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))

from pprint import pprint
from rede import main

def testa_formacao_url():
    params = {
        'token': '123456',
        'dtinicio': '20180902',
        'dtfim': '20180903'
    }

    p = main.Parameters()
    url = p.parseParametersToUrl(**params) 

    assert (url == '?token=123456&dtinicio=20180902&dtfim=20180903'),"Erro ao fazer parse dos parametros para url"

def testa_geracao_token():
    t = main.AuthorizationToken(
        os.environ['user_concil_api_rede'],
        os.environ['password_concil_api_rede'],
        os.environ['token_concil_api_rede'])
    return t.createToken()

def testa_consulta_estabelecimentos_comerciais():

    r = main.RequestsConciliacao(
        os.environ['user_concil_api_rede'],
        os.environ['password_concil_api_rede'],
        os.environ['token_concil_api_rede']
    )

    params = {
        'personType':'JURIDICA',
        'documentNumber':'3422594000117'
    }

    print(r.consultarEstabelecimentoComercial(params))

def testa_consulta_lista_ajuste_debitos():
    r = main.RequestsConciliacao(
        os.environ['user_concil_api_rede'],
        os.environ['password_concil_api_rede'],
        os.environ['token_concil_api_rede']
    )
    r.consultarListaAjusteDebitos()

def testa_consulta_pagamentos_sumarizado_cip():
    r = main.RequestsConciliacao(
        os.environ['user_concil_api_rede'],
        os.environ['password_concil_api_rede'],
        os.environ['token_concil_api_rede']
    )
    params = {
        'parentCompanyNumber': '063200988',
        'subsidiaries': '063200988',
        'startDate': '2018-09-01',
        'endDate': '2018-09-30',
        'hasAllowCompanyNumber': True
    }
    r.consultarPagamentosSumarizadosCIP(params)

if __name__ == '__main__':
    # testa_formacao_url()
    # pprint(testa_geracao_token())
    testa_consulta_estabelecimentos_comerciais()
    # testa_consulta_lista_ajuste_debitos()
    # testa_consulta_pagamentos_sumarizado_cip()