# Seminário PC III — Métricas e Cobertura de Código

**Disciplina:** G08PCOM3.01 — Programação de Computadores III (T01/2026.2)  
**Integrantes:** Gabriel Martins Nunes e Rafaela Garcia Bernardes  
**Tema:** Coverage com `pytest` e `coverage.py`

## Como apresentar

Este trabalho foi redesenhado para uma apresentação **sem slides**. O arquivo central é
`colab_coverage.ipynb`: ele guia a fala, executa os testes e abre a experiência visual
interativa `apresentacao_interativa.html`. A página também pode ser aberta diretamente no
navegador ou pelo VS Code durante a apresentação.

Use a página animada para explicar os conceitos e alterne para as células do notebook nos
momentos de demonstração. Assim, a turma vê tanto a ideia quanto a evidência real no terminal.

## Objetivo

Responder, com uma demonstração executável, à pergunta: **testes passando garantem que o código relevante foi exercitado?**

Não. O `pytest` executa e avalia os testes; o `coverage.py` mede quais linhas e caminhos foram executados durante essa execução. Uma cobertura alta é evidência de abrangência, não uma prova de correção.

## Estrutura

```text
seminario_pc3_coverage/
├── colab_coverage.ipynb           # apresentação e demonstração principal
├── apresentacao_interativa.html   # página animada para projetar
├── README.md
├── requirements.txt
├── .coveragerc                    # ativa branch coverage e relatório detalhado
├── src/loja.py                    # regra de negócio final
├── tests/test_loja.py             # suíte final
├── roteiro_live/                  # arquivos de apoio, não entram na suíte final
└── roteiro_live/                  # cenários controlados de demonstração
```

## Execução no VS Code ou terminal

No terminal aberto na pasta do projeto:

```bash
python -m venv .venv
```

Ative o ambiente virtual:

```powershell
# PowerShell (Windows)
.\.venv\Scripts\Activate.ps1
```

```bash
# macOS/Linux
source .venv/bin/activate
```

Instale e execute:

```bash
pip install -r requirements.txt
python -m pytest
python -m coverage run -m pytest
python -m coverage report -m
python -m coverage html
```

Abra `htmlcov/index.html` no navegador. O relatório mostra, por arquivo, `Stmts` (instruções), `Miss` (linhas não executadas), `Branch` (caminhos), `BrPart` (caminhos parciais) e `Cover` (percentual).

## Roteiro da demonstração (13–15 min)

### 1. Teste verde, cobertura insuficiente — Gabriel

Execute apenas o teste inicial, que valida exclusivamente o caminho VIP:

```bash
python -m pytest roteiro_live/teste_inicial.py -v
python -m coverage run --branch -m pytest roteiro_live/teste_inicial.py
python -m coverage report -m
```

Mensagem: **o teste passou, mas o relatório indica os ramos não exercitados** (valor negativo, cliente comum abaixo de R$ 500 e cliente comum a partir de R$ 500).

### 2. Acrescentar a suíte final — Rafaela

Apresente `tests/test_loja.py`: os casos foram parametrizados para exercitar VIP, cliente comum, limite de R$ 500 e erro para valor negativo.

```bash
python -m coverage erase
python -m coverage run --branch -m pytest
python -m coverage report -m
python -m coverage html
```

Abra `htmlcov/index.html` e clique em `src/loja.py`. Os números exibidos são produzidos no momento da execução, como exigido no roteiro da disciplina.

### 3. Microdemonstração RED → GREEN — ambos

O enunciado exige mostrar erro e solução. O arquivo `roteiro_live/loja_tdd_incompleta.py` não trata valor negativo. Execute o teste abaixo para exibir o estado vermelho:

```bash
python -m pytest roteiro_live/teste_tdd_valor_negativo.py -v
```

No editor, copie a condição inicial de `roteiro_live/loja_tdd_corrigida.py` para `loja_tdd_incompleta.py`:

```python
if valor < 0:
    raise ValueError("O valor não pode ser negativo.")
```

Rode o mesmo comando novamente: ele ficará verde. **Depois do ensaio, restaure `loja_tdd_incompleta.py`** para que o momento RED continue disponível no dia.

### 4. Por que 100% não prova ausência de bugs — ambos

`roteiro_live/exemplo_100_porcento_com_bug.py` contém, deliberadamente, desconto VIP de 15%, embora a regra seja 20%. O teste fraco só verifica se o resultado é positivo:

```bash
python -m coverage run --branch --source=roteiro_live.exemplo_100_porcento_com_bug -m pytest roteiro_live/teste_fraco_100_porcento.py
python -m coverage report -m
```

Mesmo com todas as linhas executadas, o defeito permanece porque a asserção não confere o valor correto. Esta é a distinção entre **execução** e **qualidade da verificação**.

## Para usar no Google Colab

Faça upload da pasta (ou descompacte o ZIP) e abra `colab_coverage.ipynb`. A primeira célula instala as dependências; as seguintes abrem a experiência animada, executam o cenário incompleto, a suíte final e o contraexemplo de teste fraco. Se fizer upload de um ZIP, descompacte-o e use `%cd seminario_pc3_coverage` antes de executar.

Na página interativa, avance com os botões laterais, as setas do teclado ou os indicadores inferiores. O laboratório de descontos permite trocar os valores e enxergar o caminho percorrido pela função.

## Divisão sugerida e tempo total

| Etapa | Responsável | Tempo |
|---|---:|---:|
| Abertura e pergunta central | Ambos | 0:30 |
| Conceito, pytest e statement coverage | Gabriel | 2:30 |
| Branch coverage e leitura de relatório | Rafaela | 2:30 |
| Cenário inicial e análise | Gabriel | 4:30 |
| Suíte ampliada, HTML e RED→GREEN | Rafaela | 5:30 |
| Limitações, conclusão e perguntas | Ambos | 3:00 |

Meta de ensaio: encerrar entre 18:30 e 19:30.

## Checklist antes de enviar ao SIGAA

- [ ] Os dois nomes aparecem no notebook e neste README.
- [ ] `pytest` passa em ambiente limpo.
- [ ] O cenário inicial mostra linhas/caminhos ausentes.
- [ ] `coverage html` foi aberto e conferido.
- [ ] O estado RED foi ensaiado e o arquivo incompleto foi restaurado.
- [ ] O arquivo compactado contém notebook, página interativa, código e `requirements.txt`.

## Referências

- [Coverage.py — documentação](https://coverage.readthedocs.io/)
- [Coverage.py — branch coverage](https://coverage.readthedocs.io/en/latest/branch.html)
- [pytest — documentação](https://docs.pytest.org/)
- [pytest — parametrização](https://docs.pytest.org/en/stable/how-to/parametrize.html)
