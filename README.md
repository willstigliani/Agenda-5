# ⚡ Calculadora de Consumo Energetico
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

Este projeto tem como objetivo calcular o consumo mensal de energia elétrica de aparelhos domésticos e o custo estimado com base no tempo de uso e na potência do aparelho.

## Objetivo do Sistema

O sistema solicita ao usuário o nome do aparelho, sua potência em Watts e o tempo de uso diário em horas. Com esses dados, ele calcula o consumo total em kWh e o custo mensal em Reais (R$), utilizando uma tarifa padrão.

## Fórmula Utilizada

O cálculo do consumo mensal segue a seguinte fórmula:

$$Consumo (kWh) = \frac{Potência (W) \times Uso Diário (h) \times 30 dias}{1000}$$

O custo total é calculado multiplicando o consumo pela tarifa:
$$Custo = Consumo \times Tarifa (R\$ 0,70)$$

---

## Como Executar o Programa

1. Certifique-se de ter o **Python** instalado em sua máquina.
2. Navegue até a pasta do projeto.
3. Execute o comando abaixo no terminal:

```bash
python app.py
```

4. Siga as instruções no terminal para informar os dados do aparelho.
