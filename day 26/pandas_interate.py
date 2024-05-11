students_dict = {
    "student": ["Luigi", "Angela", "João"],
    "score": [77, 92, 85]
}

import pandas as pd

students_df = pd.DataFrame(students_dict)
# print(students_df)

# Loop through row of our data frame.
for (index, row) in students_df.iterrows():
    print(row) # Remeber of row.student and row.score
