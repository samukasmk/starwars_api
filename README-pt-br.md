# starwars_api

Esse é um projeto de exemplo de caso de uso das tecnologias: (**Flask Framework**) com banco bancos de dados **no-sql** (**MongoDB**) orientado a *documentos*.

Esse projeto implementa alguns recursos simples para gestão de dados dos filmes da sagas StarWars. E foi inspiridado na API: [https://swapi.dev/](https://swapi.dev/).

Diferentemente do [https://swapi.dev/](https://swapi.dev/) que foi construido em **Django**, esse projeto visa implementar conceitos e boas práticas de arquitetura mais abrangente, estruturando o **Framework Flask** para um grande projeto, com o sentido de abrir mais de um escopo de dados, não se restringindo apenas a `starwars_api`. 


# Instalação

A instalação mais indicada é atraves do [Docker](https://docs.docker.com/engine/install/) e [docker-compose](https://docs.docker.com/compose/install/) caso você não possua instalado na sua maquina, providencie a instalação atraves dos links prévios.

## Instalando com o docker-compose

Basta apenas executar os seguintes comandos abaixo:

```sh
git clone https://github.com/samukasmk/starwars_api.git

cd starwars_api

docker-compose up --build
```

## Exemplo de execução da aplicação com o docker-compose
![.docs/assets/docker-install.gif](.docs/assets/docker-install.gif)


# Utilizando a API Rest

Após os passoes anteriores tiverem sido executados com sucesso e executando, connect na url de seu computador: [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

![.docs/assets/api-swagger-listing.png](.docs/assets/api-swagger-listing.png)

Atualmente essa API implementa 2 endpoints:

## Planets

Endpoint que faz a gestão básicas de dados dos planetas que aparecem nos filmes dos StarWars, como população, diametro, gravidade, periodo da orbita, periodo de rotação. 

### Métodos aplicados:

 **Método** | **Endpoint**                              | **Descrição**                                                                                             
------------|-------------------------------------------|-----------------------------------------------------------------------------------------------------------
 **POST**   | /api/starwars/planet/                     | Criar um recurso do planeta 
 **GET**    | /api/starwars/planet/                     | Listar todos os recursos dos planetas                                                                     
 **GET**    | /api/starwars/planet/?movies_details=true | Liste todos os recursos dos planetas, com informações relacionadas ao filme no campo **”movies_details"** 
 **GET**    | /api/starwars/planet/<planet_id>/         | Recupere um recurso do planeta                                                                              
 **PUT**    | /api/starwars/planet/<planet_id>/         | Atualizar um recurso do planeta                                                                           
 **PATCH**  | /api/starwars/planet/<planet_id>/         | Atualização parcial de um recurso do planeta                                                              
 **DELETE** | /api/starwars/planet/<planet_id>/         | Excluir um recurso do planeta     

### Campos alteraveis:
- **name** `<StringField>`
- **rotation_period** `<IntField>`
- **orbital_period** `<IntField>`
- **diameter** `<IntField>`
- **climate** `<StringField>`
- **gravity** `<StringField>`
- **terrain** `<StringField>`
- **surface_water** `<IntField>`
- **population** `<StringField>`

### Campos read-only:
- **id** `<objectId>`: Garante especificação do documento e concede a relação externa de n-para-n de para com os **Filmes** 
- **movies** `<array>`: Exibe a relação entre os planetas e os filmes apenas como leitura, a escrita deve ser feito pelo endpoint **Filmes** previnindo erros de ma gestão de dados;
- **movies_details** `<object>`: Exibe uma versão mais detalhada da relação com os recursos de **Filmes**, para ser exibida necessita do parametro: **?movies_details=true**
- **created_at** `<datetime>`: Gestão de criação dos documentos;
- **updated_at** `<datetime>`: Gestão de ediação dos documentos;

Exemplos de uso:

#### Criando um planeta
![.docs/assets/swagger-create-planets.png](.docs/assets/swagger-create-planets.png)

#### Listando os planetas criados
![.docs/assets/swagger-planets-listing.png](.docs/assets/swagger-planets-listing.png)

#### Listagem detalhada dos filmes relacionados
![.docs/assets/swagger-planets-listing-detailed.png](.docs/assets/swagger-planets-listing-detailed.png)

#### Atualização parcial de campos especificos dos planetas
![.docs/assets/swagger-partial-update-plantets.png](.docs/assets/swagger-partial-update-plantets.png)

#### Atualização dos campos de um planeta
![.docs/assets/swagger-update-plantets.png](.docs/assets/swagger-update-plantets.png)

## Filmes

Endpoint que faz a gestão básicas de dados dos `movies` com as suas respectivas aparições em cada filme. 

### Métodos aplicados:

 **Método** | **Endpoint**                                  | **Descrição**                                                                                            
------------|-----------------------------------------------|----------------------------------------------------------------------------------------------------------
 **POST**   | /api/starwars/movie/                          | Criar um recurso de filme                                                                                
 **GET**    | /api/starwars/movie/                          | Listar todos os recursos de filmes                                                                       
 **GET**    | /api/starwars/movie/**?planets_details=true** | Listar todos os recursos de filmes (com informações relacionadas ao filme no campo **”movies_details"**) 
 **GET**    | /api/starwars/movie/<movie_id>/               | Recuperar um recurso de filme                                                                            
 **PUT**    | /api/starwars/movie/<movie_id>/               | Atualizar um recurso de filme                                                                            
 **PATCH**  | /api/starwars/movie/<movie_id>/               | Atualização parcial de um recurso de filme                                                               
 **DELETE** | /api/starwars/movie/<movie_id>/               | Excluir um recurso de filme      


### Campos alteraveis:
- **title**: `<StringField>`
- **opening_crawl**: `<StringField>`
- **episode_id**: `<IntField>`
- **director**: `<StringField>`
- **producer**: `<StringField>`
- **release_date**: `<DateField>`
- **planets** `<array>`: Exibe a relação entre os planetas e os filmes, a escrita deve ser feito pelo endpoint **Filmes** previnindo erros de ma gestão de dados;

### Campos read-only:
- **id** `<objectId>`: Garante especificação do documento e concede a relação externa de n-para-n de para com os **Planets**
- **planets_details** `<object>`: Exibe uma versão mais detalhada da relação com os recursos de **Planets**, para ser exibida necessita do parametro: **?planets_details=true**
- **created_at** `<datetime>`: Gestão de criação dos documentos;
- **updated_at** `<datetime>`: Gestão de ediação dos documentos;


Exemplos de uso:

#### Criando um Filme já o associando a 2 Planetas 

![.docs/assets/swagger-creating-movies.png](.docs/assets/swagger-creating-movies.png)

#### Listagem detalhada dos Planetas relacionados

![.docs/assets/swagger-movie-retrive-detailed.png](.docs/assets/swagger-movie-retrive-detailed.png)

#### E por ai vai...
Visite o swagger e descubra por conta própria

# Arquitetura e estrutura de pastas do projeto:

```
├── docker-compose.yml: Arquivo de definição dos serviços
├── Dockerfile: Arquivo de definição dos containers
├── Makefile: Script com comandos operacionais repetivos
├── manage.py: Script de execução do projetos
├── pyproject.toml: Arquivo com configurações de Desenvoolvimento
├── requirements-dev.txt: Dependencias dinamicas de desenvolvimento (gerados pelo Poetry)
├── requirements.txt: Dependencias dinamicas de produção (gerados pelo Poetry)
├── scripts: 
│   └── git-hooks: Scripts e automações com o git
├── settings.toml: **Arquivo com as configurações de produção da aplicação**
├── starwars_api: **Pasta da aplicação**
│   ├── extensions: Inicializadores do Flask que executam .init_app(app)
│   ├── models: Define estruturas de dados 
│   └── rest_apis: 
│       └── starwars: 
│           ├── endpoints: Views e controllers da api rest
│           ├── queries: Queries de agregração com o mongodb
│           ├── routes.py: Rotas de URL dos endpoints
│           ├── serializers: Serializão a entrada de dados JSON -> MongoDB Document e vice e versa
│           └── validators: Define validações de campos de entrada a API Rest e swagger devem ter
└── tests: 
    ├── datasets: Dados de casos de testes
    └── fixtures: Fixtures de testes unitários
```

# Desenvolvimento

## Qualidade de código

### Tipos de testes executados no projeto

| **Testes**                                        | **Descrição**                                                                   |
|---------------------------------------------------|---------------------------------------------------------------------------------|
| **[pytest](https://docs.pytest.org/)**            | Testes unitários da API Rest                                                    |
| **[mypy](https://mypy.readthedocs.io/)**          | Testes de tipagem e anotações de entrada e saida de funções, métodos, variaveis |
| **[pyflakes](https://github.com/PyCQA/pyflakes)** | Testes de sintaxe funcional que encherga além de uma importação                 |
| **[pylint](https://pylint.readthedocs.io/)**      | Testes de sintaxe avançados com analises mais complexas                         |
| **[pycodestyle](https://pycodestyle.pycqa.org/)** | Testes de compatibilidade com as boas praticas pep8                             |
| **[radon](https://radon.readthedocs.io/)**        | Testes de complexidade cicliomatica                                             |
| **[pylama](https://klen.github.io/pylama/)**      | Agregrador dos testes acima, de forma unificada                                 |
| **[isort](https://pycqa.github.io/isort/)**       | Testes de ordenação de importação                                               |
| **[bandit](https://bandit.readthedocs.io/)**      | Testes de descoberta de vunerabilidades de seguração escritas no codigo fonte   |

> Caso deseje desativar algum teste altere as configurações no arquivo **pyproject.toml**


### Executando testes unitários de forma local
```
make test
```

### Executando testes unitários pelo docker
> Observação: ainda falta ajustar erro de configuração na conexão entre o container de testes do flask e o mongo de testes

```
docker-compose up -d mongo_tests
docker-compose run --rm unit-tests
```

### Formatando arquivos python e importações
```shell
make fmt
```

### Executando checagens de segurança
```
make sec-check
```




## Agilidade no desenvolvimento

### Executando o flask na sua maquina local


#### Em modo de produção
```
docker-compose up -d mongo 
make runserver
```

#### Modos de desenvolvimentos alternativos
```
make devserver

make debugserver
```

### Automatizando comandos com o Git Hooks

#### Executando os testes unitários após cada commit
```
make activate-commit-checks
```

![.docs/assets/git-commit-hooks.png](.docs/assets/git-commit-hooks.png)


#### Formatando as mensagens de commits com o nome do branch
```
make activate-commit-msg-fmt
```

![.docs/assets/git-commit-fmt.png](.docs/assets/git-commit-fmt.png)


#### Desativando as automações instaladas de githooks
```
make deactivate-git-hooks
```


## DevOps

### Adicionar nova biblioteca python

A gestão de dependencias é feita atraves da ferramenta [python-poetry](https://python-poetry.org/) que escolhe as subversões, a fim de encontrar um meio termo para que todas as bibliotecas necessárias possam coexistir e ao mesmo tempo ter uma constante evolução, evitando vunerabilidades de segurança.

Para adicionar uma nova biblioteca requerida, o indicado é:

1.) Localiza-la no repositório [https://pypi.org/](https://pypi.org/)

2.) Obter a versão atual

3.) Declara-la no arquivo de dependencias **pyproject.toml** como uma versão atual ou superior.

Exemplo se for a versão 1.0.0 da biblioteca xpto, declara-la como:
```
xpto = "^1.0.0"
```

4.) Reconstruir os arquivos de requiments.txt

```
make build-requirements
```

O comando acima executa as seguintes operações:
- Cria um virtualenv separado (apenas para a gestão do poetry)
- Executa o poetry install
- Exporta os arquivos de requirements.txt

> Caso você queira que essa reconstrução seja feita no seu virtualenv local basta rodar o comando: **make build-requirements-local**

5.) Reconstrua seu virtualenv local

Para instalar os novos arquivos de requirements você pode executar:

**Em modo de produção:**
```
make install
```

ou 

**Em modo de desenvolvimento:**
```
make install-dev
```

