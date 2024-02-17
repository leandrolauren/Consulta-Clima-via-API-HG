# pip install Pillow

def find_weather ():
    
    from PIL import Image
    import requests


    API_KEY = 'SUA_API_KEY'

    cidade = input('Digite a cidade a ser buscada: ')

    link = f'https://api.hgbrasil.com/weather?format=json-cors&key={API_KEY}&city_name={cidade}'

    requisicao = requests.get(link)

    requisicao_dic = requisicao.json()

    descricao = requisicao_dic['results']['description']
    temp = requisicao_dic['results']['temp']
    cidade = requisicao_dic['results']['city']
    data_consulta = requisicao_dic['results']['date']
    hora_cosulta = requisicao_dic['results']['time']
    condicao = requisicao_dic['results']['condition_slug']
    fase_lua = requisicao_dic['results']['moon_phase']

    caminho_clima = '.\\imagens-climas\\' + condicao + '.png'
    caminho_lua = '.\\fases-lua\\' + fase_lua + '.png'

    imagem_clima = Image.open(caminho_clima)
    imagem_lua = Image.open(caminho_lua)

    print(f'A cidade pesquisada: {cidade}. \nClima: {descricao}. \nTemperatura: {temp}°C \nConsulta em {data_consulta} {hora_cosulta}')

    temp_fahr = temp * 1.8 + 32
    print(f'A temperatura convertida para Fahrenheit:  {round(temp_fahr,1)}°F')

    imagem_clima.show()
    imagem_lua.show()
    

find_weather()
