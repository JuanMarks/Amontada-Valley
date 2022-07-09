# Amontada-Valley
> Status: Cursando 

 Codigos das aulas dos cursos do Alura que estou fazendo junto da Amontada-Valley


# Iniciando Com Django

## Criando ambiente virtual


```bash
# Crie a pasta onde voce quer fazer o ambiente virtual depois faça
# Dentro da pasta pelo o bash faça
python3 -m venv ./venv
# Carregando ambiente virtual dentro do vs code com o local da pasta aberto no vs code
source "caminho"/venv/bin/activate
# ou
"caminho"/venv/bin/activate
# ou em windows 
"caminho"/venv/Scripts/activate
# com o ambiente virtual ativado no vs code faça
pip install django
```

## Iniciando Projeto
No vs code no terminal bash com o ambiente virtual ativado faça
```bash
django-admin startproject "nome do projeto"
```

<p><br>No arquivo settings.py mudar o timezone para America/Fortaleza e a linguagem para pt-br<br></p>
<p><br>Subindo servidor django sempre verificando se o ambiente virtual esta ativado</p>

```bash
python manage.py runserver
```

Criando app com 
```bash
python manage.py startapp "nome do app"
```
