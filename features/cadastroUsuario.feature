Feature: Cadastro de Usuário

@cadastro_usuario
Scenario: Cadastro de usuário com sucesso
    Given que estou na página inicial
    When eu clicar no link “Clique aqui e registre-se”
    And preencher os campos necessários
    And clicar no botão “Criar conta”
    Then deve-se exibir a mensagem “Usuário cadastrado com sucesso”