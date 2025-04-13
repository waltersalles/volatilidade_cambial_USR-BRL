# Relatórios Econômicos Automatizados - Volatilidade Cambial (GARCH)

Este projeto faz parte da série *Relatórios Econômicos Automatizados* e aplica um modelo econométrico GARCH(1,1) para estimar a volatilidade mensal da taxa de câmbio USD/BRL durante o ano de 2024. A análise é feita com dados simulados de variação percentual mensal.

## Tecnologias utilizadas

- Python 3
- Bibliotecas: `pandas`, `matplotlib`, `arch`

## Objetivo

Demonstrar a aplicação de um modelo GARCH (Generalized Autoregressive Conditional Heteroskedasticity), amplamente utilizado para prever a volatilidade de séries temporais financeiras.

## Visualização

O gráfico gerado mostra a volatilidade condicional estimada ao longo dos meses de 2024, permitindo identificar períodos de maior instabilidade no câmbio.

## Como executar

1. Instale a biblioteca `arch`:
```bash
pip install arch
```

2. Execute o script `volatilidade_cambial_garch.py` em seu ambiente Python.

---
Desenvolvido por Walter Salles
