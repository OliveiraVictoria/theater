from django.shortcuts import render
from theater import views


filme1 = Filme(id =1, name="Hora do Hush 3", descricao ="Depois de um atentado contra o Embaixador Han, Lee e Carter vão para Paris para proteger uma francesa que sabe demais sobre os secretos líderes do Triad. Enquanto isso, eles também precisam lutar contra a máfia chinesa de Paris e um amigo de infância de Lee conforme eles procuram por um envelope que contem a identidade de um poderoso chefão do crime." )
filme2 = Filme(id =2, name="Annabelle - A Criação do Mal", descricao ="Anos após a trágica morte de sua filha, um habilidoso artesão de bonecas e sua esposa decidem, por caridade, acolher em sua casa uma freira e dezenas de meninas desalojadas de um orfanato. Atormentado pelas lembranças traumáticas, o casal ainda precisa lidar com um amendrontador demônio do passado: Annabelle, criação do artesão.")
filme3 = Filme(id =3, name="Jumanji", descricao ="Quatro adolescentes encontram um videogame cuja ação se passa em uma floresta tropical. Empolgados com o jogo, eles escolhem seus avatares para o desafio, mas um evento inesperado faz com que eles sejam transportados para dentro do universo fictício, transformando-os nos personagens da aventura.")
filmes = [filme1, filme2, filme3]

def filme(request):
    return render(request,"index.html",{"lista":filme})


def ver_filme(request, id:int):
    for filme in filmes:
        if filme.get_id() == id:
            return render(request,"filmes.html",{"filme":filme})