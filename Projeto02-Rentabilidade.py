 # Entrada de Dados
capital = int(input('Qual o valor inicial investido?: '))
 # Lista para armezanar a rentabilidade Mensal
juros_mensal = [0.02, 0.02, 0.02, 0.02, 0.02]
# Atribuindo rentabilidade a variaveis isoladas para fazermos as operaçoes
mes_01, mes_02, mes_03, mes_04, mes_05 = juros_mensal 
 # Calculo rentabilidade Total
rentabilidadeTotal = mes_01 + mes_02 + mes_03 + mes_04 + mes_05 
# Juros sobre Capital Investido
juros = capital * rentabilidadeTotal 
 # Resultado final
ganhos = capital + juros
print('De acordo com o capital inicial e uma rentabilidade de 2% ao mês, esse será seu capital após 5 meses: ', ganhos)
