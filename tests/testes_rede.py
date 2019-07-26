import os
import os.path
import sys

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))

from pprint import pprint
from rede import api

def testa_formacao_url():
    params = {
        'token': '123456',
        'dtinicio': '20180902',
        'dtfim': '20180903'
    }

    p = api.Parameters()
    url = p.parseParametersToUrl(**params) 

    assert (url == '?token=123456&dtinicio=20180902&dtfim=20180903'),"Erro ao fazer parse dos parametros para url"

def testa_geracao_token():
    t = api.AuthorizationToken(
        os.environ['user_concil_api_rede'],
        os.environ['password_concil_api_rede'],
        os.environ['token_concil_api_rede'])
    return t.createToken()

def testa_consulta_estabelecimentos_comerciais():

    r = api.RequestsConciliacao(
        os.environ['user_concil_api_rede'],
        os.environ['password_concil_api_rede'],
        os.environ['token_concil_api_rede']
    )

    params = {
        'personType':'JURIDICA',
        'documentNumber':'3422594000117'
    }

    print(r.consultarEstabelecimentoComercial(params))

    params = {
        'personType': 'JURIDICA',
        'documentNumber': '14776142000150'
    }

    print(r.consultarEstabelecimentoComercial(params))

def testa_consulta_lista_ajuste_debitos():
    r = api.RequestsConciliacao(
        os.environ['user_concil_api_rede'],
        os.environ['password_concil_api_rede'],
        os.environ['token_concil_api_rede']
    )
    r.consultarListaAjusteDebitos()

def testa_consulta_pagamentos_sumarizado_cip():
    r = api.RequestsConciliacao(
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


def teste_consulta_proposta_credenciamento():
    r = api.RequestsConciliacao(
        os.environ['user_concil_api_rede'],
        os.environ['password_concil_api_rede'],
        os.environ['token_concil_api_rede']
    )
    print(r.consultarPropostaCredenciamentoPorId('a021ce2e-f46f-4f30-a0bd-9e2c7880b18d'))


def test_consultarVendas():
    r = api.RequestsConciliacao(
        os.environ['user_concil_api_rede'],
        os.environ['password_concil_api_rede'],
        os.environ['token_concil_api_rede']
    )
    params = {
        'parentCompanyNumber': '64166236',
        'subsidiaries': '64166236',
        'startDate': '2019-06-01',
        'endDate': '2019-06-30',
        'hasAllowCompanyNumber': True
    }
    r.consultarVendas(params)

# Teste 19 meses API Consulta Vendas
# Array de meses testados

months={'2018-01-01':'2018-01-31',
     '2018-02-01':'2018-02-28',
     '2018-03-01':'2018-03-30',
     '2018-04-01':'2018-04-30',
     '2018-05-01':'2018-05-30',
     '2018-06-01':'2018-06-30',
     '2018-07-01':'2018-07-31',
     '2018-08-01':'2018-08-30',
     '2018-09-01':'2018-09-30',
     '2018-10-01':'2018-10-31',
     '2018-11-01':'2018-11-30',
     '2018-12-01':'2018-12-31',
     '2019-01-01':'2019-01-31',
     '2019-02-01':'2019-02-28',
     '2019-03-01':'2019-03-30',
     '2019-04-01':'2019-04-30',
     '2019-05-01':'2019-05-30',
     '2019-06-01':'2019-06-30',
     '2019-07-01':'2019-07-25',
     }


def build_params(parentCompanyNumber, subsidiaries, startDate, endDate):
    params = {
        'parentCompanyNumber': parentCompanyNumber,
        'subsidiaries': subsidiaries,
        'startDate': startDate,
        'endDate': endDate,
        'hasAllowCompanyNumber': True
    }
    return params

def mytest_consultarVendas(params):
    r = api.RequestsConciliacao(
        os.environ['user_concil_api_rede'],
        os.environ['password_concil_api_rede'],
        os.environ['token_concil_api_rede']
    )
    r.consultarVendas(params)

def test_exec_consultarVendas(parentCompanyNumber, subsidiaries):
    for k, v in months.items():
        startDate = k
        endDate = v
        print('Mês --> ' + startDate + ' - ' + endDate)
        result = mytest_consultarVendas(build_params(parentCompanyNumber, subsidiaries, startDate, endDate))
        # print(result)
        if result is not None:
            return result

if __name__ == '__main__':

    # testa_formacao_url()
    # pprint(testa_geracao_token())
    # pprint(testa_consulta_estabelecimentos_comerciais())
    test_exec_consultarVendas('77879899', '77879899')
    # pprint(testa_consulta_lista_ajuste_debitos())
    # pprint(testa_consulta_pagamentos_sumarizado_cip()) # está faltando o client_id rede.exceptions.RequestGetError: 422 - {"clientId": ["Missing data for required field."]}
    #pprint(teste_consulta_proposta_credenciamento())  # rede.exceptions.RequestGetError: 404 - "Not Found" Precisa dos dados para testar, CPF e tipo de pessoa
    #pprint(test_consultarVendas())