Projeto Básico da Disciplina de IJE
===================================

Projeto com o material básico para a disciplina de Introdução a Jogos Eletrônicos

## Estrutura das Pastas

```
├── assets           # Arquivos carregados dinamicamente: imagens, sons e fontes
│   ├── fonts
│   │   └── *.ttf
│   ├── sounds
│   │   └── *.ogg
│   └── sprites
│       └── *.png
├── engine           # Pasta para o código da engine
│   ├── include      # Arquivos cabeçalho da engine (.h, .hpp)
│   │   └── *.hpp
│   └── src          # Código fonte da engine (.c, .cpp)
│       └── *.cpp
├── inlcude          # Arquivos cabeçalho   (.h, .hpp)
│   └── *.hpp
└── src              # Código fonte do jogo (.c, .cpp)
    └── *.cpp
```

## Execução

### Docker

```
$ docker-compose up game
```

### CMake

Precisa ter instalado:

```
sudo apt-get install -y cmake libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev
```

Então rode:

```
mkdir build
cd build
cmake ..
make
./game
```

## Empacotamento

**TODO**
