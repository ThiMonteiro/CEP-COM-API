import requests
import json
import re


class BuscarEndereco:
    def __init__(self, cep) -> None:
        # Para não deixar o cep com algumas pontuações
        cep = cep.replace('-', '').replace('.', '').replace(' ', '')

        # Verifica se o CEP é válido
        if self.meu_cep_eh_valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP Inválido!!")

    def __str__(self) -> str:
        return self.formato_cep()

    def meu_cep_eh_valido(self, cep):
        '''
        Função que vai retornar True(Verdadeiro) ou False(Falso) se o CEP tiver ou não 8 caracteres
        '''
        if len(cep) == 8:
            return True
        else:
            return False

    def formato_cep(self):
        '''
        Função que formata o CEP para ficar no padrão
        '''
        padrao_cep = re.compile(r'(\d){5}(\d){3}')
        resultado = re.match(padrao_cep, self.cep)
        cep_formatado = f'{resultado.group(0)[0:5]}-{resultado.group(0)[5:8]}'
        return cep_formatado

    def busque_informacoes_do_cep(self):
        '''
        Função que busca na nossa a API as informações do CEP
        '''
        link = f"https://viacep.com.br/ws/{self.cep}/json/"
        request = requests.get(link).json()
        return request

    def endereco(self):
        '''
        Função que retornar as informações
        '''
        rua = self.busque_informacoes_do_cep()['logradouro']
        bairro = self.busque_informacoes_do_cep()['bairro']
        cidade = self.busque_informacoes_do_cep()['localidade']
        estado = self.busque_informacoes_do_cep()['uf']

        return f'{rua}, {bairro}, {cidade} - {estado}'


# ----------------------------------------

cep1 = BuscarEndereco("22041011")
print("-"*30)
print(cep1.endereco())
print("-"*30)

# ----------------------------------------

cep2 = BuscarEndereco("22050002")
print(cep2.endereco())
print("-"*30)

# ----------------------------------------

cep3 = BuscarEndereco("21032000")
print(cep3.endereco())
print("-"*30)

# ----------------------------------------
