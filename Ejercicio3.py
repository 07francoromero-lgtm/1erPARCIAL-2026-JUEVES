def interrupciones(a,b):
    if b == 0:
       return 0
    else:
       return a + interrupciones(a,b-1)


   
       