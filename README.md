Eventex
---------

[![Build Status](https://travis-ci.org/juliosaraiva/wttd-eventex.svg?branch=master)](https://travis-ci.org/juliosaraiva/wttd-eventex)
[![Build status](https://ci.appveyor.com/api/projects/status/79v28mmbro641lj5?svg=true)](https://ci.appveyor.com/project/juliosaraiva/wttd-eventex)

Sistema de eventos encomendado pela Morena.

##### Como desenvolver?


1. Clone o repositório.
2. Crie um virtualenv com python 3.7
3. Ative o virtualenv
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone https://git.juliosaraiva.com.br/juliosaraiva/wttd-eventex.git
cd wttd/
python3 -m venv .wttd
source .wttd/bin/activate
pip install -e requirements.txt
cp contrib/env-sample .env
python manage.py test
```

##### Como fazer o deploy?


1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Define uma SECRET_KEY segura para a instância.
4. Defina DEBUG=False
5. Configure o serviço de email
6. Envie o código para o heroku


```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# Configuro o email
git push heroku master --force
```