import numpy
from pandas import Series, DataFrame
import pandas as pd

obj= Series([4,7, -5, 3])

obj

obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])


obj2

obj2['a']
obj2['d'] = 42
obj2 > 6

obj2[obj2 > 0]

pi = lambda x: x+42
obj2 * 2

pi(obj2)

sdata = {"São Paulo": 20000, "Minas": 12000, "Santa Catarina": 5000, "Rio de Janeiro": 12}

obj3 = Series(sdata)

obj3

stados = ["São Paulo", "Minas", "Santa Catarina", "Rio Grande do Sul"]

obj4 = Series(sdata, index=stados)

obj4

obj3 + obj4

data = {'state': ['Ohio', 'Ohio','Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}

frame = DataFrame(data)

frame


frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'])

frame2.columns

frame2['debt'] = frame2.state == 'Ohio'

frame2

idiota = {"python": {"idiota": "sim", "succincto": "meh"},
          "clojure": {"idiota": "não", "succincto": "sim"}}

frame3 = DataFrame(idiota)

frame3.T

lang = [{"name": "clojure", "idiota": "não", "succincto": "sim"},
        {"name": "python",  "idiota": "sim", "succincto": "meh"},
        {"name": "java",    "idiota": "sim", "succincto": "não"}]

DataFrame.from_records(lang, index="name")








