# **CEP COM API**

* Desenvolvi esse programa que busca dentro da **API** o **CEP** desejado e retorna o endereço.

# **BIBLIOTECAS USADAS**

* requests
* json
* re

# **COMO VAI FUNCIONAR O CÓDIGO?**

1º Para conseguirmos consumir os dados da **API** precismos entrar no site: https://viacep.com.br

2º Você dentro do site vai selecionar o formato que deseja. **Ex:** **Json**, **JsonP** ou **XML**.

(**OBS:** Nesse projeto eu usei o formato **Json**.)

3º Dentro do site copie o link que retorna as informações do CEP para nós:
https://viacep.com.br/ws/01001000/json/

# **Agora precisamos fazer a requisição:**

1º Você precisa fazer a importação da biblioteca **"Requests"** e **"Json"**, exemplo:

```python
import requests
import json
```

2º Agora você vai digitar o nosso código, exemplo:

```python
cep_get = requests.get("https://viacep.com.br/ws/01001000/json/")
print(cep_get)
```

(**OBS:** Se o resultado for **<Response [200]>**, mostra que solicitação funcionou.)

# **AGORA PRECISAMOS TRANSFORMAR O FORMATO JSON EM PYTHON:**

Para transformar em formato Json tem **2 formas**:

1º Criar uma variável com o mesmo nome(cep_get) e dentro da variável colocar o metodo Json(). **Exemplo:**

```python
cep_get = cep_get.json()
```

2º Colocar o metodo direto na nossa requisição. **Exemplo:**

```python
cep_get = requests.get("https://viacep.com.br/ws/01001000/json/").json()
```

* Isso é feito, pois as informações da requisição estão armazenadas dentro da variável **"cep_get"** no formato **JSON**

# **COMO POSSO VISUALIZAR AS INFORMAÇÕES AGORA?**

Basta dar um **print** em nossa variável e as informações do CEP estarão lá em formato de **dicionário**. **Exemplo:**

```python
{'cep': '01001-000', 'logradouro': 'Praça da Sé', 'complemento': 'lado ímpar', 'bairro': 'Sé', 'localidade': 'São Paulo', 'uf': 'SP', 'ibge': '3550308', 'gia': '1004', 'ddd': '11', 'siafi': '7107'}
```


# **COMO FICOU O MEU CÓDIGO:**

(**OBS:** Lembrando que esse foi o meu código final. Aplicando os conceitos de POO.)

```python
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

```