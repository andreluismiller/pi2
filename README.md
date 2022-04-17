# Sobre o projeto

A ideia é criar uma plataforma na qual agricultores familiares possam se cadastrar e oferecer o excedente de sua produção aos clientes (também cadastrados) na plataforma, que irão adquirir os alimentos por meio troca de serviços. 
O agricultor pode definir o preço - que irá balizar o que vale ou não a pena trocar - de acordo com critérios pré-estabelecidos no termo de aceite (sazonalidade do alimento, preço praticado no mercado, se é ou não orgânico, etc.). A plataforma não será responsável pelas negociações. Apenas colocará agricultores e clientes em contato para que eles negociem entre si, por meio de caixa de mensagem da própria plataforma ou outro meio de comunicação externo (whatsapp, telefone, etc.)


# Aspectos técnicos
## Back-end
Utilização de Django, framework python para desenvolvimento web
## Front-end
Utilização de HTML, CSS e Javascript


# Instruções de configuração do projeto
### 1) Instalação python
- 1.1) Caso ainda não tenha python instalado em sua máquina, basta entre [neste link](https://python.org.br/instalacao-windows/) e seguir as instruções de configuração.
- 1.2) Após a instalação, abra o terminal como usuário master e digite o comando abaixo para se certificar de que ele foi instalado corretamente:
```sh
python --version
```
### 2) Criação do repositório local
- 2.1) Crie uma pasta preferencialmente no desktop de seu computador chamada "pi";
- 2.2) Abra a pasta que criou no passo acima no Visual Studio Code, se certificando de selecionar python como linguagem do projeto (VER > PALETA DE COMANDO > SELECIONAR INTERPRETADOR PYTHON > Python 3.10);
- 2.3) Abra uma nova janela de terminal (TERMINAL > NOVO TERMINAL) e certifique de que ele esteja na pasta do projeto. Caso não esteja, basta digital o comando "cd" seguido do caminho da pasta, conforme exemplo abaixo:
```sh
cd C:\User\Desktop\pi2
```
- 2.4) O projeto rodará dentro de uma máquina virtual, e para isso é necessário criá-la, digitando o comando abaixo:
```sh
python -m venv myvenv
```
- 2.5) O próximo passo é ativar a máquina virtual (deve ser feito sempre que o projeto for aberto), digitando o comando abaixo:
```sh
myvenv\Scripts\activate
```
- 2.6) Com a máquina virtual rodando, chegou a hora de instalar o django, digitando o comando abaixo:
```sh
pip install django
```
- 2.7) Para verificar se o django foi instalado corretamente, digite o seguinte comando em uma nova janela do terminal:
```sh
django --version
```

### 3) Clone do projeto
##### PS: para este passo, é necessário ter o git bash instalado em sua máquina. Caso não tenha, [baixe-o aqui](https://gitforwindows.org) e faça a configuração com seu usuário e senha.
- 3.1) Acesse a pasta "pi2"
```sh
cd pi-2
```
- 3.2) Clone o repositório github do projeto por meio do comando:
```sh
git clone...
```

### 4) Executando o projeto
- 4.1) Acesse a pasta "pi2"
```sh
cd pi-2
```
- 4.2) Ative o ambiente virtual
```sh
myvenv\Scripts\activate
```
- 4.3) Inicie o servidor com o comando abaixo, entrando no link fornecedio (http://127.0.0.1:8000/) para verificar se a instalação foi bem-sucedida:
```sh
python manage.py runserver
```
