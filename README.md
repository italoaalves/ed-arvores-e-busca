# Árvore AVL

Repositório do Segundo Projeto da disciplina de Estruturas de Dados. O objetivo é implementar uma Árvore AVL.

## Como executar este projeto

```bash
git clone https://github.com/italoaalves/projeto-ed-2/
cd projeto-ed-2

python app.py
```

## Especificação do projeto

Desenvolva uma aplicação que gerencie o catálogo de filmes de um
aplicativo de stream. Cada registro do catálogo deve conter o nome
do filme, ano, e id. O id é número inteiro e único que identifica o
filme. Os registros devem estar organizados em uma Árvore Binária
de Busca, balanceada (AVL), cujas chaves são os ids.

A qualquer momento um usuário poderá:

- Incluir o registro de um filme, lendo, do teclado, os seus dados.
- Buscar um filme pelo id, retornando e exibindo o nome e ano,
  em caso de sucesso. Do contrário, informar que a chave do filme
  não existe no catálogo;
- Buscar os filmes lançados em um determinado ano;
- Listar todos os títulos do catálogo, por ordem alfabética
  crescente;
- Informar a altura da árvore.
  Deverá existir um menu interativo, para que o usuário escolha as
  opções:
  1 Inserir filme
  2 Buscar filme pelo id
  3 Buscar filmes pelo ano
  4 Listar filmes em ordem alfabética
  5 Altura da árvore
  6 Exibir a árvore
  7 Sair do programa.
