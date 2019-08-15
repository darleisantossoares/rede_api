# coding: utf-8
from datetime import datetime
from .exceptions import RequestGetError
import base64
import json
import os
import requests
import sys

BASE_URL_HOMOLOG = 'https://api-hom.userede.com.br/redelabs'
BASE_URL_PROD = 'https://api.userede.com.br/redelabs'

class AuthorizationToken:

    def __init__(self, user, password, token_user, token_pass, sandbox=False):
        self.user = user
        self.password = password
        self.token_user = token_user
        self.token_pass = token_pass
        self.header_authorization = {
                   'Content-Type': 'application/x-www-form-urlencoded',
                   'authorization': self._token_base_64()
        }
        self.payload = 'grant_type=password&username='+user+'&password='+password

    def createToken(self):
        r = requests.post(
            BASE_URL_PROD+'/oauth/token',
            headers=self.header_authorization,
            data=self.payload,
            auth=(self.token_user, self.token_pass))

        assert (r.status_code == requests.codes.ok), "Token request error"

        return json.loads(r.text)

    def _token_base_64(self):
        _token = self.token_user + ':' + self.token_pass
        return base64.b64encode(_token.encode())



class RequestsConciliacao:

    def __init__(self, user, password, token_user, token_pass, sandbox=False):
        auth = AuthorizationToken(user, password, token_user, token_pass, sandbox)
        self.authorization = auth.createToken()
        self.token = self.authorization.get('token_type') + ' ' + self.authorization.get('access_token')
        self.urlbase = BASE_URL_HOMOLOG if sandbox else BASE_URL_PROD

        self.header_request = {
            'content-type': 'application/json',
            'Authorization': self.token
        }

    def get(self, url, params: dict):
        r = requests.get(self.urlbase+url, headers=self.header_request, params=params)

        if r.status_code != requests.codes.ok:
            raise RequestGetError(r.status_code, r.text)

        return r.json()

    def post(self, url, params, data=None):
        r = requests.post(self.urlbase+url, headers=self.header_request, params=params, data=data)

        if r.status_code != requests.codes.ok:
            raise RequestGetError(r.status_code, r.text)

        return r.json()

    def put(self, url, data=None):
        r = requests.put(self.urlbase+url, headers=self.header_request, data=data)

        if r.status_code != requests.codes.ok:
            raise RequestGetError(r.status_code, r.text)

        return r.json()

    # C O N C I L I A C A O
    def consultarVendas(self, params: dict):
        return self.get('/conciliation/v1/sales', params)

    def consultarParcelas(self, params: dict):
        return self.get('/conciliation/v1/sales/installments', params)

    def consultarPagamentosSumarizadosCIP(self, params:dict):
        return self.get('/conciliation/v1/payments', params)

    def _consultarpagamentosOrdemCredito(self, **kwargs):
        # MÉTODO ESTÁ COMO PRIVADO POIS ESTÁ EM CONSTRUÇÃO POR PARTE DA REDE
        pass

    def _consultarRecebiveis(self, **kwargs):
        # MÉTODO ESTÁ COMO PRIVADO POIS ESTÁ EM CONSTRUÇÃO POR PARTE DA REDE
        pass

    def consultarRecebiveisSumarizados(self, params):
        url = '/conciliation/v1/receivables/summary'
        return self.get(url, params)

    def consultarDebitos(self, params: dict):
        return self.get('/conciliation/v1/charges', params)

    def _consultarDebitosSumarizados(self, params: dict):
        # MÉTODO ESTÁ COMO PRIVADO POIS ESTÁ EM CONSTRUÇÃO POR PARTE DA REDE
        url = '/conciliation/v1/charges/summary'
        return self.get(url, None)

    def consultarListaAjusteDebitos(self):
        # MÉTODO COM ERRO DO LADO DA REDE...
        url = '/conciliation/v1/charges/adjustment-types'
        return self.get(url, None)


    # C R E D E N C I A M E N T O
    def criarPropostaCredenciamento(self, data: dict):
        url = '/proposal/v1/affiliates'
        return self.post(url, None, data)

    def consultarPropostaCredenciamentoPorId(self, id: str):
        url = '/proposal/v1/affiliates/{id}'.format(id=id)
        return self.get(url, {})

    def consultarEstabelecimentoComercial(self, params: dict):
        url = '/customer/v1/merchants'
        return self.get(url, params)

    def cancelarEstabelecimentoComercial(self, id: int):
        url = '/customer/v1/merchants/{id}/cancel'.format(id=str(id))
        return self.put(url)

    def consultarPrecos(self, params: dict):
        return self.get('/proposal/v1/pricing', params)

    def consultarMCCs(self, params: dict):
        return self.get('/brand/v1/mcc', params)

    def createLeadCredenciamento(self, params: dict, data: dict):
        return self.post('/proposal/v1/lead', params, data)

    def consultarProdutosMdr(self, id: int):
        url = '/customer/v1/merchants/{id}/products/mdr'.format(id=str(id))
        return self.get(url)

    def consultarProdutosFlex(self, id: int):
        url = 'customer/v1/merchants/{id}/products/flex'.format(id=str(id))
        return self.get(url)

    def consultarProdutosAluguel(self, id: int):
        url = 'customer/v1/merchants/{id}/products/technologies'.format(id=str(id))
        return self.get(url)

    def consultarDomicilioBancarioPontoVenda(self, id: int):
        url = 'customer/v1/merchants/{id}/bank-accounts'.format(id=str(id))
        return self.get(url)
