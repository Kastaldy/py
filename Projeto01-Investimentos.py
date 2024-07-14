renda = float(input('Qual a sua Renda Mensal?'))
cdv = float(input('Qual é o seu custo de vida mensal?'))
lazer = float(input('Quanto você gasta por mês com seu Lazer?'))
conta1 = renda - cdv - lazer
resultado = conta1
print('''
De acordo com sua renda e gastos mensais, te sobra: R${} para investir'''.format(conta1))

#investimentos
recomen = str(input('O Senhor(a) gostaria de avaliar nossas recomendações?'))
if resultado > 400:
    
 cdb = resultado * 0.25
 fiis = resultado * 0.25
 acoes = resultado * 0.25
 reservaEmerg = resultado * 0.2
 educacao = resultado * 0.05
 msgr = 'Invista a quantia de R$'
 print('')
 print('''Aqui vai uma recomendação de alocação de capital mais Segura e com uma rentabilidade moderada:
      - CDB: {}{} 
      - FIIS: {}{} 
      - AÇÕES: {}{} 
      - Reserva de Emergência: {}{} 
      - Educação: {}{}'''.format(msgr, cdb, msgr, fiis, msgr, acoes, msgr, reservaEmerg, msgr, educacao))
 print('''
 E também temos uma recomendação mais arriscada, porém com maior rentabilidade:''')     
 cdb = resultado * 0.15
 fiis = resultado * 0.35
 acoes = resultado * 0.35
 reservaEmerg = resultado * 0.10
 educacao = resultado * 0.05
 msgr = 'Invista a quantia de R$'
 print('')
 print('''
      - CDB: {}{} 
      - FIIS: {}{} 
      - AÇÕES: {}{} 
      - Reserva de Emergência: {}{} 
      - Educação: {}{}'''.format(msgr, cdb, msgr, fiis, msgr, acoes, msgr, reservaEmerg, msgr, educacao))
# pequenos aportes
else: resultado < 400
cdb = resultado * 0.3
fiis = resultado * 0.15
acoes = resultado * 0.15
reservaEmerg = resultado * 0.3
educacao = resultado * 0.1
msgr = 'Invista a quantia de R$'
print('')
print('''Aqui vai uma recomendação de alocação de capital mais Segura e com uma rentabilidade moderada:
      - CDB: {}{} 
      - FIIS: {}{} 
      - AÇÕES: {}{} 
      - Reserva de Emergência: {}{} 
      - Educação: {}{}'''.format(msgr, cdb, msgr, fiis, msgr, acoes, msgr, reservaEmerg, msgr, educacao))
print('''
     E também temos uma recomendação mais arriscada, porém com maior rentabilidade:''')     
cdb = resultado * 0.15
fiis = resultado * 0.35
acoes = resultado * 0.35
reservaEmerg = resultado * 0.10
educacao = resultado * 0.05
msgr = 'Invista a quantia de R$'
print('')
print('''
      - CDB: {}{} 
      - FIIS: {}{} 
      - AÇÕES: {}{} 
      - Reserva de Emergência: {}{} 
      - Educação: {}{}'''.format(msgr, cdb, msgr, fiis, msgr, acoes, msgr, reservaEmerg, msgr, educacao))