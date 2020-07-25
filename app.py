""" Here we will test the functions of analysis """ 
# -*- coding: UTF-8 -*- 
from time import sleep

import pandas as pd
import Analyse

import settings

df = pd.read_excel("csv/Histórico dos Chamados.xlsx")
descriptions = df[df["SERVICO"] == "Computadores e Acessórios"]["DESCRICAO"]

# Get tokens, make csv with them; and get summarized descriptions which contains some tokens
Analyze = Analyse.Analysis(descriptions)
nameDf = "csv/Tokens - Computadores e Acessórios.csv"
Analyze.getFrequentTokens(nameToSave=nameDf)
goodDescripts = [Analyze.analyseDescription(description, nameDf, 3)
                 for description in descriptions]
goodDescripts = [x for x in goodDescripts if x != None]

# Now, remove bad simbols
greatDescripts = Analyze.removeBadSimbols(goodDescripts, settings.simbols)
# And html/javascript tags
greatDescripts = Analyze.removeTags(greatDescripts)

# Save descripts in csv file
dfDescript = pd.Series(greatDescripts)
dfDescript.to_csv('Descrições - Computadores e Acessórios.csv', encoding='utf-8')