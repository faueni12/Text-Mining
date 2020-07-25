""" Settings and constants of the project """
# -*- coding: UTF-8 -*- 
from nltk.corpus import stopwords

# Words not very important for analysis
stop_words = stopwords.words('portuguese')

# Except these
stop_words.remove('não')
stop_words.remove('esta')
stop_words.remove('está')
stop_words.remove('estão')

stop_words += ['<', 'br', '>', 'nbsp', ',', '.', ';', '&', '(', ')', '!', "''", '``', 'bom', 'dia', 
    'g', '-', 'vt', 'mat', 'nº', 'pois', ':', '@', 'ter', 'gentileza', 'boa', 'tarde', 'noite',
    'obrigado', '?', 'juiz', 'hoje', 'secretaria', 'dra', 'urgencia', 'urgência', 'humberto',
    'desta', '<span>', '</span>', 'span', '/span' 'ser', 'segue', 'gt', 'intuito', '--', 'div', '/div', 'obs',
    '[',']', 'destinar', 'ronaldo', 'compor', 'após', 'segs', '2º', 'seres.', '*', 'conforme',
    'atenciosamente', 'natal', 'equipe', 'escola', '2', 'segundo', 'vara', 'judicial', 'dois',
    'apoio', 'encontra-se', '1', 'seres', 'fernades/ivia', 'ivia', 'distribuição', 
    'encaminhar', 'coordenadoria', 'feita.', '/a', 'demais', 'tácio', 'usp=sharing', '3', '4',
    'turma', 'possível', 'href', 'href=', 'urgente', 'presidência', 'usada', 'veio', 'encontra',
    ]

# Simbols to remove in the descriptions
simbols = ['</>', '<>', '/>', '"', '/i>', '<br>','</h2>', '<b>', '<ul>', '</ul', '</b>', 'li>', 
    '/li', '<li>', '</li', '<h2>', '</h3>', '<h3>', '</h1>', '<h1>', '</h4>', '<h4>', 
    '</h5>', '<h5>', '</h6>', '<h6>',  'nbsp', '&', '&nbsp', '`', '@', '/a', 'href',
    'href=', 'usp=sharing', '<span>', '</span>', '[', ']', '&', '(', ')', '!', "''",
    '"' ,'``', '/a', 'div', '/div']

simbols2 = ['</>', '<>', '/>', '"', '/i>']