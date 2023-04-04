# AlphaCube

### Autores:
- [Marcelo Rabello Barranco](https://github.com/Maraba23)
- [Thomas Chiari Ciocchetti de Souza](https://github.com/thomaschiari)

### Descrição:
O Projeto AlphaCube é um projeto que utiliza a biblioteca `Pygame` para desenhar um cubo rotativo em 3 dimensões. O cubo pode ser rotacionado em torno de seus eixos X, Y e Z.
O programa também permite que o usuário ajuste a distância focal da câmera virtual utilizada para renderizar o cubo de 3 para 2 dimensões através de um controle deslizante.
Se trata de um programa que simula o uso de ferramentas como OpenGL para simular a renderização de objetos 3D em 2D, movendo o cubo em torno de um eixo e alterando a distância focal da câmera virtual.

### Requisitos e Instruções:
1. Certifique-se de ter instalado Python na versão 3.9 ou superior.
2. Clone o repositório do projeto através do comando no terminal: 
`git clone https://github.com/Maraba23/AlphaCube.git`
3. Acesse a pasta do projeto através do comando no terminal:
`cd AlphaCube`
4. (Recomendado) Crie um ambiente virtual para o projeto através do comando no terminal:
`python3 -m venv env`
5. Ative o ambiente virtual através do comando no terminal:
`source env/bin/activate` (Linux)
`env\Scripts\Activate.ps1` (Windows)
6. Instale as dependências do projeto através do comando no terminal:
`pip install -r requirements.txt`
7. Execute o programa através do comando no terminal:
`python3 AlphaCube.py`
8. Para desativar o ambiente virtual, basta executar o comando no terminal:
`deactivate`

### Teoria:
O projeto usa como base a teoria por trás de uma câmera Pinhole, que consiste em uma câmera com um pequeno orifício e um aparato fotossensível. Quando a luz entra pelo orifício, gera uma imagem invertida no aparato.
Em um plano cartesiano bidimensional, é possível pensar na câmera com o orifício sendo o ponto (0, 0), e o aparato sendo uma reta que fica a uma distância *d* desse orifício. Assim, diversos pontos no plano cartesiano podem ser projetados nessa reta, como mostra a figura a seguir:

![Pinhole Camera](pinhole_2d.jpeg)

Na figura, o aparato é representado pela reta *y = -1*, e a distância focal *d* é representada pela distância entre o ponto (0, 0) e a reta *y = -1*, que é igual a 1.
Assim, é possível projetar o ponto $x_0, y_0$ na reta *y = -1* e obter o ponto $x_p, y_p$, utilizando semelhança de triângulos.
No caso acima, é importante notar que a dimensão *z* é fixa, ou seja, há apenas duas dimensões.
É possível alterar isso fixando uma das demais dimensões, tornando as outras duas variáveis. 

Por semelhança de triângulos, no caso acima, temos que:

$$
tan(\theta) = \frac{x_0}{y_0} = \frac{x_p}{y_p}
$$

Ou seja, 

$$
x_p = \frac{x_0}{y_0}y_p
$$



