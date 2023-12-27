from collections import defaultdict
from itertools import groupby

# fake data from https://www.mockaroo.com
data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""


def group_names_by_country(data: str = data) -> defaultdict:

    countries = defaultdict(list)





    for k,g in groupby(data.split('\n')[1:],lambda x: x.split(',')[-1]):
        print(k,list(g))



        

if __name__ == "__main__":

    group_names_by_country()
