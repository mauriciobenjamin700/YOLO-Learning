# Passo a Passo

Este tutorial, feito em 28/05/2024 visa auxiliar a aprendizagem de novos usuários da YOLO em sua jornada.

## Conseguir Imagens

As imagens podem ser adquiridas em práticamente qualquer lugar, mas tudo vai depender do seu problema. Existem bases de imagens públicas como [OpenImages](https://storage.googleapis.com/openimages/web/index.html). Caso o seu problema sejá específico, deverá coletar suas próprias imagens e preparalas para o modelo.

Para o nosso problema iremos usar 10 imagens de Gado, visando contagem. Iremos criar o projeto de contagem de gado em imagems, onde na pasta [imagens](CattleCount/images/) serão guardadas as imagens que usaremos. Todas foram baixadas do google.

### Caso as imagens sejam poucas, será preciso realizar um aumento de imagens

Se você tem poucas imagens, podemos usar artifícios para realizar um aumento na sua base de imagens. Popularmente se usa Rotação em Nº Graus para gerar a images novas apartir das que já temos, mas existem diversas tecnicas de aumento de imagem. [Saiba mais Clicando Aqui](https://distrito.me/blog/data-augmentation-o-que-e-e-como-usar-essa-tecnica/). Em nossos exemplos usaremos rotação de 90º, 180º e 270º.

### Como rotacionar as imagens?

Pode ser um desafio para quem está começando realizar a rotação de imagens, pois isso envolve uma serie de problemas como:

- Qual ferramenta usar?
- Se minha base de imagens for mediana, vai dar muito trabalho fazer manual
- Não sei por onde começar
- etc.

Para o nosso caso, usaremos a biblioteca Open-CV da linguagem de programação [Python](https://www.python.org/) para nos auxiliar. O arquivo [rotate_images.py](CattleCount/scripts/rotate_images.py) estará encarregado de realizar o rotacionamento das imagens que usaremos e as salvar na pasta de saída [data](CattleCount/data) que contará todas as 40 imagens ao final do processo.

### Dependencias

Não vamos entrar muito em detalhes sobre questões como estrutras de dependencias, ambientes virtuais, etc.

Para realizar o nosso passo a passo no tutorial, basta ter o python instalado e executar o seguinte comando em seu terminal

```bash
pip install -r requirements.txt
```

## Realizar a Marcação e Rotular das Imagens

### Baixar o Dataset

## Treinar o Modelo

### Testar o modelo

## Implementar o Modelo

## Análisar os Resultados
