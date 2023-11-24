from num2words import num2words
from word2number import w2n

def add(query):
    query = query.replace('what is', '')
 
    if '+' in query:
        list = query.split('+')
    if 'plus' in query:
        list = query.split('plus')
    if 'add' in query:
        query = query.replace('add', '')
        if 'to' in query:
            list = query.split('to')
        else:
            list = query.split('and')

    try:
        list[0] = num2words(list[0])
    except:
        pass 
    try:
        list[1] = num2words(list[1])
    except:
        pass 
    a = w2n.word_to_num(list[0])
    b = w2n.word_to_num(list[1])
          
    return num2words(a + b)

def subtract(query):
    query = query.replace('what is', '')

    if '-' in query:
        list = query.split('-')
    if 'minus' in query:
        list = query.split('minus')
    if 'subtract' in query:
        query = query.replace('subtract', '')
        list = query.split('from')

    try:
        list[0] = num2words(list[0])
    except:
        pass 
    try:
        list[1] = num2words(list[1])
    except:
        pass 
    a = w2n.word_to_num(list[0])
    b = w2n.word_to_num(list[1])
          
    return num2words(a - b)

def divide(query):
    if 'divided by' in query:
        query = query.replace('what is', '')
        list = query.split('divided by')
    elif 'divide' in query:
        query = query.replace('divide', '')
        if 'by' in query:
            list = query.split('by')
        else:
            list = query.split('from')

    try:
        list[0] = num2words(list[0])
    except:
        pass 
    try:
        list[1] = num2words(list[1])
    except:
        pass 
    a = w2n.word_to_num(list[0])
    b = w2n.word_to_num(list[1])
          
    return num2words(a / b)

def multiply(query):
    if 'what is' in query:
        query = query.replace('what is', '')
        if 'times' in query:
            list = query.split('times')
        else:
            list = query.split('multiplied by')
    elif 'multiply' in query:
        query = query.replace('multiply', '')
        if 'by' in query:
            list = query.split('by')
        else:
            list = query.split('times') 

    try:
        list[0] = num2words(list[0])
    except:
        pass 
    try:
        list[1] = num2words(list[1])
    except:
        pass 
    a = w2n.word_to_num(list[0])
    b = w2n.word_to_num(list[1])
          
    return num2words(a * b)

def lol():
    print('lol')