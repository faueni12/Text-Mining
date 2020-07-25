""" This file is destined to functions to automatize the data analysis in DataFrames."""
# -*- coding: UTF-8 -*- 
import pandas as pd

from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize

import settings

class Analysis:
    def __init__(self, df):
        self.df = df
        self.df_tokens = {}

    """ The function will get all word most frequents, returning a DataFrame 
    with nameToSave kwargs argument"""
    def getFrequentTokens(self, quantity=150, **kwargs):
        # Get tokens from description
        tokens = []
        for frase in self.df.apply(lambda phrase: str.lower(str(phrase))):
            tokens += word_tokenize(frase)

        # Remove stopwords
        tokens = [token for token in tokens if token not in settings.stop_words]

        # Most frequent Tokens
        freqTokens = FreqDist(tokens).most_common(quantity)
        
        # Argument "name" if you want to save in csv
        nameDf = kwargs.get("nameToSave")
        if nameDf:
            word = [w[0] for w in freqTokens]
            quantity = [q[1] for q in freqTokens]
            df = pd.DataFrame({'word':word, 'quantity':quantity})
            df.to_csv(nameDf, encoding="utf-8")

            # Save in dictionary of df tokens
            self.df_tokens[nameDf] = df

        return freqTokens

    """ The function will take all descriptions that have this tokens. """
    def analyseDescription(self, description, nameDfTokens, occurrences, separator='.', quantity=150):
        tokens = self.df_tokens[nameDfTokens]["word"][:quantity]
        # Acess each phrase, that are splitted by separator (by standard, "."),
        # to summarize the descriptions. Will choose the first one that have the quantity of tokens
        for descript in str.lower(description).split(separator):
            # count how many occurrences have in the phrase
            occurrencesTokens = [descript.count(str(token)) for token in tokens]
            qtTokens = len([occur for occur in occurrencesTokens if occur > 0])
            if qtTokens >= occurrences:
                return descript

    """ Here the simbols will be removed """
    def removeBadSimbols(self, descriptions, simbols):
        greatDescripts = []
        for descript in descriptions:
            for simbol in simbols:
                descript = ''.join(descript.split(simbol))           
            greatDescripts += [descript]
        return greatDescripts
    
    """ Remove html, javascript tags, etc """
    def removeTags(self, descriptions):
        greatDescripts = []
        for description in descriptions:
            for i in range(15):
                openTag = description.find('<')
                if openTag != -1:
                    # Find close Tag '</', if have
                    initCloseTag = description[openTag:].find('</')
                    if initCloseTag != -1:
                        endCloseTag = description[initCloseTag:].find('>')
                        description = description[:openTag] + description[endCloseTag + 1:]
                    # If is a tag without '</'
                    else:
                        endCloseTag = description[openTag:].find('>')                    
                        if endCloseTag != -1:    
                            description = description[:openTag] + description[openTag + endCloseTag + 1:]
                        else:
                            description = description[:openTag]
                # If haven't tag
                else:
                    greatDescripts += [description.strip()]
                    break
        return greatDescripts
