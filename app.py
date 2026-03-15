#Calculadora de consumo de energia elétrica

#Entrada de dados
aparelho = input("Informe o nome do aparelho:\n")
potencia = float(input("Informe a potência do aparelho em Watts:\n"))
usoDiario = float(input("Informe o tempo de uso diário do aparelho em horas:\n"))

#Cálculo do consumo mensal
consumoMensal = (potencia * usoDiario * 30) / 1000
tarifa = 0.70
custoMensal = consumoMensal * tarifa

#Saída de dados
print(f"O consumo mensal do aparelho {aparelho} é de {consumoMensal:.2f} kWh. O custo estimado na cidade de São Paulo é de R$ {custoMensal:.2f} por mês.")
