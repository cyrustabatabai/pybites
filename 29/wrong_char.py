def get_index_different_char(chars):
    










    counts = {True:0 ,False:0}



    for char in chars:
        counts[str(char).isalnum()] += 1



    
    if counts[True] == 1:
        f = lambda x: x.isalnum()
    else:
        f = lambda x: not x.isalnum()



    for i,char in enumerate(chars):
        if f(str(char)):
            return i








