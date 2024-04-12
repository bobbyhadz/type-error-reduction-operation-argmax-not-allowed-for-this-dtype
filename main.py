# Reduction operation 'argmax' not allowed for this dtype

import pandas as pd

df = pd.DataFrame({
    'experience': ['5', '14', '7', '10'],
    'salary': [175.1, 180.2, 190.3, 205.4],
}, index=['Alice', 'Bobby', 'Carl', 'Dan'])


df['experience'] = pd.to_numeric(df['experience'])

print(df.idxmax())