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

<p>No arquivo settings.py mudar o timezone para America/Fortaleza e a linguagem para pt-br<br></p>

```python
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Fortaleza'
```

<p><br>Subindo servidor django sempre verificando se o ambiente virtual esta ativado</p>

```bash
python manage.py runserver
```

Criando app com 
```bash
python manage.py startapp "nome do app"
```
<p>Registre o app no arquivo settings.py na linha 33</p>

```python
INSTALLED_APPS = [
    'nome do app',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

<p>Crie um arquivo com nome de urls.py na pasta do app e faça</p>

```python
from path import django.urls
from . import views

urlpatterns = [
path('', views.index, name='index'),
]
```

<p>No arquivo views faça</p>

```python
#EXEMPLO
def index(request):
     	receitas = Receita.objects.all()

     	dados = {
          'receitas' : receitas
     	}
     	return render(request, 'index.html', dados)
```

<p>Adcionar include no arquivo urls.py do projeto </p>

```python
from django.contrib import admin
from django.urls import path, include
#EXEMPLO
urlpatterns = [
    path('', include('receitas.urls')),
    path('admin/', admin.site.urls),
]
```

<p>Criar uma pasta com nome de template no app e criar ou colocar o arquivo index.html nele</p>
<p>Gerenciando arquivos estaticos no django</p>
<p>Adcionar o caminho da templates no arquico settings.py linha 58</p>

```python
'DIRS': [os.path.join(BASE_DIR, 'nome da pasta do app/templates')]
```

<p>Configurando arquivos estaticos</p>

```python
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'nome do projeto/static')
]
```
