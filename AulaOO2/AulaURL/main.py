url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=Dolar&quantidade=100"
print(url)

url = url.strip()

if(url == ""):
    raise ValueError("URL Invalida")
else:
    indice_interrogacao = url.find('?')
    url_base = url[:indice_interrogacao]
    print(url_base)
    url_parametros = url[indice_interrogacao+1:]
    print(url_parametros)

    parametro_busca = 'moedaDestino'
    indice_parametro = url_parametros.find(parametro_busca)
    indice_valor = indice_parametro + len(parametro_busca) + 1
    e_comercial = url_parametros.find('&', indice_valor)

    if(e_comercial == -1):
        valor = url_parametros[indice_valor:]
    else:
        valor = url_parametros[indice_valor:e_comercial]    
    print(valor)