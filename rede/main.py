# coding: utf-8
from datetime import datetime 
import os 
import requests 
import sys 

BASE_URL_HOMOLOG = 'https://api-hom.userede.com.br/redelabs'
BASE_URL_DEV = None
BASE_URL = None

class AuthorizationToken:
    def __init__(self):
        pass  

    def create(self):
        pass 

class Parameters:

    @staticmethod
    def parseParameters(**kwargs):
        for k, v in kwargs.items():
            pass 

class RequestsConciliacao:
    def __init__(self):
        pass 

    def consultarVendas(self, **kwargs):
        url = '/v1/sales'


    def consultarParcelas(self, **kwargs):
        url = '/v1/sales/installments' 

    def consultarPagamentosSumarizadosCIP(self, **kwargs):
        url = '/v1/payments' 

    def consultarpagamentosOrdemCredito(self, **kwargs):
        pass 

    def consultarRecebiveis(self, **kwargs):
        pass 

    def consultarRecebiveisSumarizados(self, **kwargs):
        pass 

    def consultarDebitos(self, **kwargs):
        pass 

    def consultarDebitosSumarizados(self, **kwargs):
        pass 

    def consultarListaAjusteDebitos(self, **kwargs):
        pass 


class RequestsCredenciamentos:
    def __init__(self):
        pass 

    def createPropostaCredenciamento(self, **kwargs):
        pass 

    def consultarPropostaCredenciamento(self, **kwargs):
        pass 

    def consultarEstabelecimentoComercial(self, **kwargs):
        pass 

    def cancelarEstabelcimentoComercial(self, **kwargs):
        pass 

    def consultarPrecos(self, **kwargs):
        pass 

    def consultarMCCs(self, **kwargs):
        pass 

    def realizarLeadCredenciamento(self, **kwargs):
        pass 
