import requests


# Primeiro desafio da aula


headers = {'X-GitHub-Api-Version': '2022-11-28'}  # especificando a versão da API
r = requests.get('https://api.github.com/users/MicaelMBaruch', headers=headers)
