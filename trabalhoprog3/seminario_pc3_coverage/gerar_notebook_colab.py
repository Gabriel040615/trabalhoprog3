"""Gera o notebook principal da apresentação no Google Colab."""

import json
from pathlib import Path


def markdown(text):
    return {"cell_type": "markdown", "metadata": {}, "source": text.splitlines(keepends=True)}


def code(text):
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": text.splitlines(keepends=True),
    }


cells = [
    markdown("""# Coverage Lab: testes, caminhos e confiança

### Programação de Computadores III — Tema 8
**Gabriel Martins Nunes · Rafaela Garcia Bernardes**

> Pergunta central: se os testes passam, como sabemos se exercitamos o código que realmente importa?

Este notebook é a apresentação. Ele alterna uma página visual animada com comandos reais de `pytest` e `coverage.py`. Executem as células na ordem; as células identificadas como **PAUSA PARA FALA** indicam quem deve explicar cada parte.
"""),
    markdown("""## Preparação no Colab

1. Faça upload do arquivo `seminario_pc3_coverage_COLAB_FINAL.zip` quando a caixa aparecer.
2. Execute esta célula uma única vez.
3. Depois, execute as demais em ordem.
"""),
    code("""# Esta célula funciona tanto no Google Colab quanto no VS Code/Jupyter.
import sys
from pathlib import Path

try:
    from google.colab import files
    em_colab = True
except ModuleNotFoundError:
    em_colab = False

if em_colab:
    print("☁️ Ambiente Google Colab detectado. Envie o arquivo ZIP do projeto.")
    uploaded = files.upload()
    zip_name = next(iter(uploaded))
    !mkdir -p /content/seminario_pc3_coverage
    !unzip -qo "$zip_name" -d /content/seminario_pc3_coverage
    %cd /content/seminario_pc3_coverage
else:
    print("💻 Ambiente VS Code/Jupyter detectado. Usando a pasta atual do projeto.")
    if not Path("requirements.txt").exists():
        raise FileNotFoundError(
            "Abra o notebook a partir da pasta seminario_pc3_coverage."
        )

!{sys.executable} -m pip -q install -r requirements.txt
print("✅ Projeto preparado. Pasta atual:", Path.cwd())
"""),
    markdown("""## Abertura — 30 segundos

**Gabriel e Rafaela:** apresentem a pergunta central. A página abaixo é o apoio visual; naveguem com as setas do teclado, os botões laterais ou os indicadores inferiores.
"""),
    code("""# A página é exibida dentro de um iframe para não alterar o visual do VS Code.
import base64
from IPython.display import HTML, display

pagina = Path("apresentacao_interativa.html").read_text(encoding="utf-8")
pagina_base64 = base64.b64encode(pagina.encode("utf-8")).decode("ascii")
display(HTML(f''' 
<iframe
  src="data:text/html;base64,{pagina_base64}"
  style="width:100%; height:720px; border:0; border-radius:14px; background:#071426;"
  title="Coverage Lab — apresentação interativa">
</iframe>
'''))
"""),
    markdown("""## PAUSA PARA FALA — conceito e ferramentas (4 min)

**Gabriel:** explique a diferença entre `pytest` (executa e avalia asserções) e `coverage.py` (mede linhas e caminhos executados). Na página animada, avance até os tópicos *Statement × Branch* e *Nosso laboratório*.

**Rafaela:** no laboratório, clique nos quatro cenários. Destaque que a mesma função possui caminhos diferentes: erro, VIP, desconto por limite e nenhum desconto.
"""),
    markdown("""## Demonstração 1 — teste verde, cobertura incompleta (3 min)

**Gabriel:** antes de executar, peça à turma uma hipótese: “se este único teste for aprovado, a cobertura será completa?”. Ele valida só o cliente VIP.
"""),
    code("""!{sys.executable} -m pytest roteiro_live/teste_inicial.py -v
!{sys.executable} -m coverage erase
!{sys.executable} -m coverage run --branch -m pytest roteiro_live/teste_inicial.py
!{sys.executable} -m coverage report -m
"""),
    markdown("""### Interpretação

**Resultado esperado e reproduzível:** 1 teste aprovado e **43%** de cobertura.  
**Gabriel:** mostre que as linhas/caminhos ausentes correspondem exatamente aos casos que não foram testados: valor negativo, cliente comum abaixo de R$ 500 e cliente comum a partir de R$ 500.
"""),
    markdown("""## Demonstração 2 — ampliar a suíte (4 min)

**Rafaela:** mostre `tests/test_loja.py`. Cada caso tem uma intenção clara: VIP, compra comum sem desconto, limite de R$ 500, compra acima do limite e entrada inválida.
"""),
    code("""!{sys.executable} -m coverage erase
!{sys.executable} -m coverage run --branch -m pytest -v
!{sys.executable} -m coverage report -m
!{sys.executable} -m coverage html
"""),
    code("""# Painel visual com dados REAIS do coverage.py, isolado do layout do notebook.
import base64
import json
from IPython.display import HTML, display

!{sys.executable} -m coverage json -o coverage.json
dados_coverage = json.loads(Path("coverage.json").read_text(encoding="utf-8"))
arquivo_loja = next(
    info for caminho, info in dados_coverage["files"].items()
    if caminho.replace("\\\\", "/").endswith("src/loja.py")
)
resumo = arquivo_loja["summary"]

painel = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>
*{{box-sizing:border-box}} body{{margin:0;background:#071426;color:#eff8ff;font-family:Arial,sans-serif}}
.wrap{{min-height:390px;padding:34px;background:radial-gradient(circle at 88% 10%,#164a72 0,transparent 36%),#071426}}
.tag{{color:#55eed0;font-size:12px;letter-spacing:.15em;font-weight:800}} h1{{margin:10px 0 8px;font-size:31px}} p{{color:#aac1d5;margin:0 0 24px;line-height:1.45}}
.grid{{display:grid;grid-template-columns:repeat(5,1fr);border:1px solid #28506e;border-radius:14px;overflow:hidden}} .item{{padding:19px 10px;text-align:center;background:#0d233d;border-right:1px solid #28506e}}.item:last-child{{border:0}}.number{{display:block;color:#55eed0;font-weight:800;font-size:30px}}.label{{color:#aac1d5;font-size:12px}}
.ok{{margin-top:21px;padding:14px 17px;border-radius:10px;background:#123d46;color:#bfffee;font-weight:700}} code{{color:#73caff}}
</style></head><body><main class="wrap"><div class="tag">RELATÓRIO REAL · COVERAGE.PY</div><h1>src/loja.py — cobertura final</h1><p>Dados produzidos nesta execução, não valores digitados manualmente.</p><div class="grid">
<div class="item"><span class="number">{resumo['num_statements']}</span><span class="label">Stmts</span></div>
<div class="item"><span class="number">{resumo['missing_lines']}</span><span class="label">Miss</span></div>
<div class="item"><span class="number">{resumo['num_branches']}</span><span class="label">Branch</span></div>
<div class="item"><span class="number">{resumo['num_partial_branches']}</span><span class="label">BrPart</span></div>
<div class="item"><span class="number">{resumo['percent_covered_display']}%</span><span class="label">Cover</span></div>
</div><div class="ok">✓ Linhas e caminhos exercitados pela suíte final. O relatório detalhado também está em <code>htmlcov/index.html</code>.</div></main></body></html>'''

dados_iframe = base64.b64encode(painel.encode("utf-8")).decode("ascii")
display(HTML(f'<iframe src="data:text/html;base64,{dados_iframe}" style="width:100%;height:430px;border:0;border-radius:14px" title="Relatório visual do coverage"></iframe>'))
"""),
    markdown("""## PAUSA PARA FALA — leitura do relatório (2 min)

**Rafaela:** explique `Stmts`, `Miss`, `Branch`, `BrPart` e `Cover`. A suíte final alcança 100% para `src/loja.py`, mas isso é uma conclusão sobre execução — não uma garantia absoluta de correção.
"""),
    markdown("""## Demonstração 3 — RED → GREEN (3 min)

**Gabriel:** este teste especifica que valor negativo deve gerar erro. A implementação usada inicialmente ainda não possui essa regra, portanto o teste precisa falhar. Isso é o estado **RED**.
"""),
    code("""# A falha é esperada aqui — ela será usada como evidência do RED.
!{sys.executable} -m pytest roteiro_live/teste_tdd_valor_negativo.py -v || true
"""),
    markdown("""**Rafaela:** agora mostre, no arquivo `roteiro_live/loja_tdd_corrigida.py`, as duas linhas que implementam a regra. A célula seguinte aplica a versão corrigida apenas para a demonstração, executa o teste verde e restaura automaticamente o arquivo incompleto.
"""),
    code("""from shutil import copyfile

incompleta = Path("roteiro_live/loja_tdd_incompleta.py")
backup = incompleta.read_text(encoding="utf-8")
try:
    copyfile("roteiro_live/loja_tdd_corrigida.py", incompleta)
    !{sys.executable} -m pytest roteiro_live/teste_tdd_valor_negativo.py -v
finally:
    incompleta.write_text(backup, encoding="utf-8")
print("✅ GREEN demonstrado; cenário RED foi restaurado para um próximo ensaio.")
"""),
    markdown("""## Demonstração 4 — 100% ainda pode ter bug (3 min)

**Ambos:** a função abaixo possui um erro intencional: dá 15% ao VIP, mas a regra deveria ser 20%. O teste é fraco: só confirma que o resultado é positivo. Ele passa e atinge 100% de cobertura mesmo sem verificar a regra correta.
"""),
    code("""!{sys.executable} -m coverage erase
!{sys.executable} -m coverage run --branch --source=roteiro_live.exemplo_100_porcento_com_bug -m pytest roteiro_live/teste_fraco_100_porcento.py -v
!{sys.executable} -m coverage report -m
"""),
    markdown("""## Conclusão — 1 min

- `pytest` indica se os comportamentos especificados foram aprovados.
- `coverage.py` aponta linhas e decisões que a suíte deixou de percorrer.
- Branch coverage amplia a análise para os dois lados de uma decisão.
- **Cobertura alta ajuda a enxergar lacunas; boas asserções e bons cenários é que testam a regra de negócio.**

### Pergunta final para a turma
> Qual caso de fronteira ou regra de negócio você adicionaria a esta aplicação?
"""),
]

notebook = {
    "cells": cells,
    "metadata": {
        "colab": {"name": "Coverage_Lab_PCIII.ipynb", "provenance": []},
        "kernelspec": {"display_name": "Python 3", "name": "python3"},
        "language_info": {"name": "python"},
    },
    "nbformat": 4,
    "nbformat_minor": 5,
}

output = Path(__file__).with_name("colab_coverage.ipynb")
output.write_text(json.dumps(notebook, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"Notebook atualizado: {output}")
