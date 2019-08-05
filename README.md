# API Rede

Documentação da API:
* Conciliação.: https://conciliationrede.docs.apiary.io
* Credenciamento.: https://affiliationrede.docs.apiary.io

### Forma de uso:

```
from rede import api

r = api.RequestsConciliacao(
    COLOCAR_SEU_USUARIO,
    COLOCAR_SUA_SENHA,
    COLOCAR_SEU_USERNAME_REDE,
    COLOCAR_SEU_PASSWORD_REDE
)

params = {
    'personType':'JURIDICA',
    'documentNumber':'3422594000117'
}

result = r.consultarEstabelecimentoComercial(params)

print(result)

```

A package faz a autenticação, gera um token de acesso e com esse token consulta os estabelecimentos comerciais do CNPJ 3422594000117

### Métodos disponíveis

Todos os métodos disponíveis na documentação da rede foram implementados, sendo eles.:

#### Credenciamento
* Realizar Proposta de Credenciamento (criarPropostaCredenciamento)
* Consultar Proposta de Credenciamento por Id (consultarPropostaCredenciamentoPorId)
* Consultar Estabelecimento Comercial (consultarEstabelecimentoComercial)
* Cancelar Estabelecimento Comercial (cancelarEstabelecimentoComercial)
* Consultar Preços (consultarPrecos)
* Consultar MCCs (consultarMCCs)
* Realizar Lead Credenciamento (createLeadCredenciamento)

#### Conciliação
* Consultar Vendas (consultarVendas)
* Consultar Parcelas (consultarParcelas)
* Consultar Pagamentos - Visão Sumarizada CIP (consultarPagamentosSumarizadosCIP)
* Consultar Pagamentos - Visão Ordem de Crédito (Sem método, API EM CONSTRUÇÃO)
* Consultar Recebíveis (Sem método, API EM CONSTRUÇÃO)
* Consultar Recebíveis - Visão Sumarizada (consultarRecebiveisSumarizados)
* Consultar Débitos - Visão Detalhada (consultarDebitos)
* Consultar Débitos - Visão Sumarizada (Sem método, API EM CONSTRUÇÃO)
* Consultar Lista de Ajustes de Débito (consultarListaAjusteDebitos)


### Ambiente
Até o exato momento a rede só disponibilizou o ambiente de homologação, porém para selecionar o ambiente basta criar uma estância da classe da seguinte forma

```
r = api.RequestsConciliacao(
    COLOCAR_SEU_USUARIO,
    COLOCAR_SUA_SENHA,
    COLOCAR_SEU_USERNAME_REDE,
    COLOCAR_SEU_PASSWORD_REDE,
    True
) # Desta forma seleciona automaticamente o Sandbox (Homologação está selecionado como ambiente)

prd = api.RequestsConciliacao(
  COLOCAR_SEU_USUARIO,
  COLOCAR_SUA_SENHA,
  COLOCAR_SEU_USERNAME_REDE,
  COLOCAR_SEU_PASSWORD_REDE,
  False
) # Desta forma seleciona-se o ambiente de produção

```

## TO-DO
* Validar bodies em métodos POST para verificar se todos os campos obrigatórios estão presentes
* Validar todos os query string parameters obrigatórios estão presentes na URL
* Criar mensagem amigável para o usuário quando faltar um parametro obrigatório
* Caso resultados retornem paginados criar método recursivo para busca de todos os dados em somente uma chamada
