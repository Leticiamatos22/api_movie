# API Cine Flex

## 1. Introdução

### 1.1 Visão Geral do Projeto
O projeto API Cine Flex visa criar uma API para uma locadora de filmes, permitindo que usuários acessem e gerenciem informações sobre filmes, clientes, quantidades disponiveis entre outras funcionalidades relacionadas ao funcionamento da locadora.

### 1.2 Objetivos e Propósito do Sistema
O principal objetivo é fornecer uma plataforma eficiente para gerenciar o catálogo de filmes de uma locadora, facilitando os processos de locação, devolução e administração de clientes e estoque.

### 1.3 Benefícios Esperados do Projeto
- Automação de processos de locação e devolução.
- Melhor gestão de estoque de filmes.
- Acesso fácil às informações por meio de uma API.
- Otimização do atendimento ao cliente.
- Redução de erros humanos no processo de locação.

## 2. Visão Geral do Sistema

### 2.1 Descrição do Sistema
A API Cine Flex permitirá operações CRUD (Create, Read, Update, Delete) em entidades como filmes, clientes e transações de locação e devolução. A API será robusta, segura e de fácil integração com outros sistemas.

#### Requisitos Funcionais:
- Cadastro de filmes, clientes e transações.
- Pesquisa e consulta de filmes disponíveis.
- Registro de locações e devoluções.



## 3. Arquitetura do Sistema

### 3.1 Explicação da Arquitetura MVC
A arquitetura MVC (Model-View-Controller) será utilizada, separando a lógica de negócios, apresentação e controle das requisições.

### 3.2 Papel de Cada Componente
- *Model:* Representa os dados e a lógica de negócios.
- *View:* Interface de usuário.
- *Controller:* Gerencia as requisições do cliente, interagindo com o Model e a View.

### 3.3 Uso do Padrão Repository
O padrão Repository será utilizado para isolar o código de acesso a dados, proporcionando maior flexibilidade e testabilidade.

## 4. Funcionalidades

### 4.1 Lista Detalhada de Funcionalidades
- Cadastro de filmes e clientes.
- Consulta de filmes disponíveis.
- Registro de locações e devoluções.

### 4.2 Casos de Uso Principais
- Cliente busca por filmes disponíveis.
- Funcionário cadastra um novo filme.
- Cliente aluga um filme disponível.


### 5.1 Desempenho Esperado do Sistema
A API deve lidar com um grande volume de transações simultâneas de forma eficiente.

### 5.2 Segurança e Autenticação
Implementação de um sistema de autenticação seguro para proteger as operações sensíveis.

### 5.3 Escalabilidade e Manutenibilidade
A arquitetura será projetada para facilitar a escalabilidade horizontal e a manutenção futura.

## 6. Tecnologias Utilizadas

### 6.1 Linguagens de Programação
- Python

### 6.2 Frameworks
- Django Rest Framework (para desenvolvimento da API)

### 6.3 Bancos de Dados
- MySQL (para armazenamento de dados)

### 6.4 Ferramentas de Desenvolvimento
- Git (controle de versão)

## 7. Modelo de Dados

### 7.1 Estrutura do Banco de Dados
O banco de dados terá tabelas para filmes, clientes, transações, entre outras entidades relacionadas.

### 7.2 Relacionamentos entre Entidades
As entidades estarão relacionadas de acordo com as necessidades de negócio, como a relação entre locações e clientes.

### 7.3 Esquema de Armazenamento
Será adotado um esquema relacional para garantir integridade e consistência dos dados.

## 8. Interfaces do Usuário

### 8.1 Layout e Design das Interfaces
As interfaces serão na forma de endpoints de API, com respostas em formato JSON.

### 8.2 Funcionalidades Específicas de Cada Endpoint
Cada endpoint oferecerá funcionalidades específicas, como consulta de filmes ou registro de locações.

### 8.3 Fluxos de Interação do Usuário
Os usuários interagem com a API por meio de requisições HTTP, utilizando métodos como GET, POST, PUT e DELETE.

## 9. Arquitetura de Implementação

### 9.1 Organização do Código-Fonte
O código será organizado em módulos separados de acordo com a funcionalidade, seguindo as diretrizes do padrão MVC.

### 9.2 Divisão em Módulos e Componentes
Cada componente do sistema será encapsulado em um módulo independente, facilitando o desenvolvimento e manutenção.

### 9.3 Dependências entre Componentes
Os componentes se comunicarão por meio de interfaces bem definidas, reduzindo o acoplamento e facilitando a manutenção.

### 10.2 Procedimentos de Implantação
Procedimentos para implantação automatizada da aplicação em cada ambiente serão estabelecidos.

#Como utilizar a API
##Clone o repositório "https://github.com/Leticiamatos22/api_movie/tree/develop"

###Instale todas as dependências (Yarn )

### Testando a API
Com o servidor em execução, você pode testar a API utilizando ferramentas como Postman ou cURL.

###Exemplos de Endpoints:
###Lista de Filmes:

###Método: GET
###URL: http://localhost:8000/api/movies/
###Adicionar Filme:

###Login de Usuário:

###Método: POST
###URL: http://localhost:8000/api/login/

