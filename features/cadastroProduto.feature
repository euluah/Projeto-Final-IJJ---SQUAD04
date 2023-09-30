Feature: Cadastro de produto

@cadastro_produto
Scenario: Cadastro de produto com sucesso
    Given que o vendedor está logado no site e acessa a página de cadastro de produto
    When o vendedor preenche os campos obrigatórios com informações válidas e clica no botão "Cadastrar Produto"
    Then o produto é registrado com sucesso e uma mensagem de confirmação é exibida