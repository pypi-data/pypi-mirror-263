import pandas as pd

def compara(ai,aj,max=True):
  # Maximização
  d = ai - aj
  if (max):
    if d <= 0:
      F = 0 # D <= 0
    elif d > 0: #se D > 0
      F = 1
  # Minimização
  else:
    if d <= 0:
      F = 1
    elif d > 0:
      F = 0

  return F

def compara_2(ai,aj,q,max=True):
  # Maximização
  d = ai - aj
  if (max):
    if d <= q:
      F = 0 # D <= 0
    elif d > q: #se D > 0
      F = 1
  # Minimização
  else:
    if d <= q:
      F = 1
    elif d > q:
      F = 0

  return F

def compara_3(ai,aj,q,max=True):
  # Maximização
  d = ai - aj
  if (max):
    if d <= 0:
      F = 0
    elif d >= 0 and d <= q:
      F = d / q
    elif d > q:
      F = 1
  # Minimização
  else:
    if d <= 0:
      F = 1
    elif d >= 0 and d <= q:
      F = d / q
    elif d > q:
      F = 0

  return F

def compara_4(ai,aj,q,p,max=True):
  # Maximização
  d = ai - aj
  if (max):
    if d <= q:
      F = 0
    elif q < d and d <= p:
      F = 0.5
    elif d > p:
      F = 1
  # Minimização
  else:
    if d <= q:
      F = 1
    elif q < d and d <= p:
      F = 0.5
    elif d > p:
      F = 0

  return F

def compara_5(ai,aj,q,p,max=True):
  # Maximização
  d = ai - aj
  if (max):
    if d <= q:
      F = 0
    elif q < d and d <= p:
      F = (d-q)/(p-q)
    elif d > p:
      F = 1
  # Minimização
  else:
    if d <= q:
      F = 1
    elif q < d and d <= p:
      F = (d-q)/(p-q)
    elif d > p:
      F = 0

  return F

def compara_6(ai,aj,s,max=True):
  # Maximização
  d = ai - aj
  if (max):
    if d <= 0:
      F = 0
    elif d > 0:
      F = 1 - math.exp(-d ** 2)
  # Minimização
  else:
    if d <= 0:
      F = 1 - math.exp(-d ** 2)
    elif d > 0:
      F = 0

  return F

# Cria a matriz para cálculo do Fluxo positivo
def tabelaC(df,crit,min,tipo,q,p):
  tc1 = []
  for i in df.index:
    ai = df.loc[i,crit]
    aux = []
    # Comparação de ai com cada aj.
    for j in df.index:
      aj = df.loc[j,crit]
      if (min):
        if tipo == 1:
          res = compara(ai,aj,False)
        elif tipo == 2:
          res = compara_2(ai,aj,q,False)
        elif tipo ==3:
          res = compara_3(ai,aj,q,False)
        elif tipo == 4:
          res = compara_4(ai,aj,q,p,False)
        elif tipo == 5:
          res = compara_5(ai,aj,q,p,False)
        elif tipo == 6:
          res = compara_6(ai,aj,q,False)
      else:
        if tipo == 1:
          res = compara(ai,aj,True)
        elif tipo == 2:
          res = compara_2(ai,aj,q,True)
        elif tipo == 3:
          res = compara_3(ai,aj,q,True)
        elif tipo == 4:
          res = compara_4(ai,aj,q,p,True)
        elif tipo == 5:
          res = compara_5(ai,aj,q,p,True)
        elif tipo == 6:
          res = compara_6(ai,aj,q,True)
      aux.append(res)
    tc1.append(aux)

  return tc1


# Cria a matriz para cálculo do Fluxo negativo
def tabelaCM(df,crit,min,tipo,q,p):
  tc1 = []
  for i in df.index:
    ai = df.loc[i,crit]
    aux = []
    # Comparação de ai com cada aj, porém com preferência para aj.
    for j in df.index:
      aj = df.loc[j,crit]
      if (min):
        if tipo == 1:
          res = compara(aj,ai,False)
        elif tipo == 2:
          res = compara_2(aj,ai,q,False)
        elif tipo == 3:
          res = compara_3(aj,ai,q,False)
        elif tipo == 4:
          res = compara_4(aj,ai,q,p,False)
        elif tipo == 5:
          res = compara_5(aj,ai,q,p,False)
        elif tipo == 6:
          res = compara_6(aj,ai,q,False)
      else:
        if tipo == 1:
          res = compara(aj,ai,True)
        elif tipo == 2:
          res = compara_2(aj,ai,q,True)
        elif tipo == 3:
          res = compara_3(aj,ai,q,True)
        elif tipo == 4:
          res = compara_4(aj,ai,q,p,True)
        elif tipo == 5:
          res = compara_5(aj,ai,q,p,True)
        elif tipo == 6:
          res = compara_6(aj,ai,q,True)
      aux.append(res)
    tc1.append(aux)
  return tc1

# Cálculo do Fluxo+ para todos os critérios
def calcFluxoPositivo(df,pesos,objetivos,tipo,q,p):

  # Obtendo o número de alternativas (linhas da tabela).
  rows = df.index
  m = len(rows)
  # Obtendo os critérios (colunas da tabela).
  columns = df.columns
  n = len(columns)

  # Comparando as alternativas em relação ao primeiro critério, já aplicando os pesos.
  tc = tabelaC(df,columns[0],objetivos[0],tipo,q,p)
  dc = pesos[0]*pd.DataFrame(data=tc)

  #restante dos critérios, já somando os valores obtidos com a matriz do primeiro critério
  for i in range(1,n):
    tci = tabelaC(df,columns[i],objetivos[i],tipo,q,p)
    dci = pesos[i]*pd.DataFrame(data=tci)
    dc = dc.add(dci, fill_value=0)

  # Resultando final do Fluxo positivo: Soma das linhas
  dc.loc[:,'Total'] = dc.sum(axis = 1, skipna = True)
  dc['Total'] = (dc['Total']).round(2)
  print(dc)
  return dc['Total']


# Cálculo do Fluxo- para todos os critérios
def calcFluxoNegativo(df,pesos,objetivos,tipo,q,p):

  # Obtendo o número de alternativas (linhas da tabela).
  rows = df.index
  m = len(rows)
  # Obtendo os critérios (colunas da tabela).
  columns = df.columns
  n = len(columns)

  # Comparando as alternativas em relação ao primeiro critério, já aplicando os pesos.
  tc2 = tabelaCM(df,columns[0],objetivos[0],tipo,q,p)
  dc2 = pesos[0]*pd.DataFrame(data=tc2)

  #restante dos critérios, já somando os valores obtidos com a matriz do primeiro critério
  for i in range(1,n):
    tci2 = tabelaCM(df,columns[i],objetivos[i],tipo,q,p)
    dci2 = pesos[i]*pd.DataFrame(data=tci2)
    dc2 = dc2.add(dci2, fill_value=0)

  # Resultando final do Fluxo negativo: Soma das colunas
  dc2.loc[:,'Total'] = dc2.sum(axis = 1, skipna = True)
  dc2['Total'] = (dc2['Total']).round(2)
  print(dc2)
  return dc2['Total']


def promethee(df,pesos,objetivos,tipo,q=0,p=0):
  # Cálculo do Fluxo+.
  print('Cálculos do Fluxo+')
  dcp = calcFluxoPositivo(df,pesos,objetivos,tipo,q,p)

  # Cálculo do Fluxo-.
  print('Cálculos do Fluxo-')
  dcn = calcFluxoNegativo(df,pesos,objetivos,tipo,q,p)

  #retorna o fluxo líquido, subtraíndo o fluxo positivo do negativo
  return dcp-dcn