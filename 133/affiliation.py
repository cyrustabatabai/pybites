import re
def generate_affiliation_link(url):


    parts = url.split('/')



    dp_index = parts.index('dp')

    other = parts[dp_index + 1]


    



    return f"http://www.amazon.com/dp/{other}/?tag=pyb0f-20"



