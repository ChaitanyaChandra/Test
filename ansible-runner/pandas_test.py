import pandas as pd

my_data = {
    'one' : 'ok',
    'two' : 'not ok',
    'three' : 'ok',
    'four' : 'ok',
    'five' : 'not ok'
}

import pandas as pd

my_data = {
    'one': 'ok',
    'two': 'not ok',
    'three': 'ok',
    'four': 'ok',
    'five': 'not ok'
}

df = pd.DataFrame(list(my_data.values()), columns=['items'])

print(df)
