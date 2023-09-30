Feature: Login

@login_required
Scenario: Login com sucesso
  Given que eu estou na pagina de login
  When eu informar as minhas credenciais
  Then a URL deve ser "https://projetofinal.jogajuntoinstituto.org/products"