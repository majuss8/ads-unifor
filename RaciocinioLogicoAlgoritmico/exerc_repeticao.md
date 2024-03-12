**Disciplina:** Raciocínio Lógico Algorítmico
**Orientador:** Prof. Ricardo Carubbi
## Lista exercícios - Estruturas de Repetição

1) Atualize o algoritmo para determinar se um número inteiro e positivo é par ou ímpar, usando uma laço condicional para aceitar apenas números maiores ou iguais a zero.

### Fluxograma
```mermaid
flowchart TD
A([INICIO]) --> B{{Digite um número: }}
B --> C[/num/]
C --> D{num > -1}
D --TRUE--> E{num % 2 == 0}
D --FALSE--> H{{"'[ERRO] O número informado é negativo, digite um valor positivo!'"}}
H --> B
E --TRUE--> F{{'O número informado é par!'}}
E --FALSE--> G{{'O número informado é ímpar!'}}
F --> I([FIM])
G --> I
``` 

### Pseudocódigo
```
1)	ALGORITMO par_impar
2)	DECLARE num: INTEIRO
3)	INICIO
4)	ESCREVA 'Digite um número: '
5)	LEIA num
6)	SE num < 0 ENTAO
7)		REPITA
8)			ESCREVA '[ERRO] O número informado é negativo, digite um valor positivo: '
9)			LEIA num
10)		ATE_QUE num > -1
11)	FIM_SE
12)	SE num % 2 == 0 ENTAO
13)		ESCREVA 'O número informado é par!'
14)	SENAO 
15)		ESCREVA 'O número informado é ímpar!'
16)	FIM_ALGORITMO
```

### Teste de Mesa

| num | num > -1 | num % 2 == 0 | Saída
|--- |--- |--- |--- |
| -1 | false |  | '[ERRO] O número informado é negativo, digite um valor positivo: ' |
| 0 | true | true | 'O número informado é par!' |
| 1 | true | false | 'O número informado é ímpar!'|
| 2 | true | true | 'O número informado é par!'

2) Faça um algoritmo que exiba na tela uma contagem de 0 até 30, exibindo apenas os múltiplos de 3.

### Fluxograma
```mermaid
flowchart TD
A([INICIO]) --> B[/n, num/]
B --> C[n = 30]
C --> D[num = 1]
D --> 
```
