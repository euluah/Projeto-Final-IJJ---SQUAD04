# Projeto de Teste QA/SQUAD04 - Sistema de Vendas do Instituto Joga Junto

## Visão Geral

Este projeto consiste no teste do sistema de vendas desenvolvido para o Instituto Joga Junto. O foco dos testes é na perspectiva do vendedor que utiliza o sistema para cadastrar produtos e realizar vendas. 

## Arquitetura do Sistema

O sistema é construído utilizando as seguintes tecnologias:

- **Frontend:** React JS, hospedado na AWS Amplify.
- **Backend:** NodeJS.
- **Banco de Dados:** MySQL (versão 8).

## Requisitos de Teste

Os seguintes requisitos devem ser testados no sistema:

1. **Cadastro de Conta:** O vendedor deve ser capaz de criar uma conta no sistema.

2. **Autenticação:** O vendedor deve ser capaz de autenticar-se no sistema usando suas credenciais.

3. **Cadastro de Produto:** Após autenticar-se, o vendedor deve poder cadastrar produtos para venda.

## Execução dos Testes

Os testes serão executados utilizando as seguintes tecnologias:

- **Behave:** Para a automação de testes de comportamento.
- **Selenium:** Para a automação de testes de interface do usuário.
- **Python:** Para a programação dos testes e scripts de automação.

## Estrutura do Projeto

A estrutura do projeto está organizada da seguinte forma:

- **features/:** Contém os cenários de teste definidos em arquivos .feature.

- **steps/:** Contém a implementação dos passos dos cenários de teste em Python.

- **pages/:** Contém classes para interagir com os elementos da interface do usuário.

- **reports/:** Armazena os resultados dos testes e relatórios gerados.

  ## Instalação

1. Clone este repositório em sua máquina local:

   ```bash
   git clone https://github.com/seu-usuario/nome-do-projeto.git
   ```
   - Navegue até o diretório do projeto:
      
   ```bash
   cd nome-do-projeto
   ```
  - Crie e ative um ambiente virtual (opcional, mas recomendado):
    ```bash
       python -m venv venv
       source venv/bin/activate
    ```

2. Executando Testes
    Você pode executar os testes de comportamento usando o Behave. Certifique-se de estar no diretório raiz do projeto.
   

   
