# Question 1: How do you import the Pandas library in Python?
import pandas as pd

# Question 2: How do you create an empty DataFrame in Pandas?Pandas

empty_dict = {}
dataframe = pd.DataFrame(empty_dict)


# Question 3: How do you create a DataFrame from a Python dictionary containing columns name and age with 3 records?

data = {
    'name': ['Pooja', 'Khushi', 'Pushpak', 'Harsh', 'Thomas', 'Prakash'],
    'age': [22, 34, 66, 33, 45, 24]
}

df = pd.DataFrame(data)
print(df)


# Question 4: How do you check the first 5 rows of a DataFrame?

print(df.head())
print(df.tail())
print(df.head(3))
print(df.tail(3))

# Question 5: How do you check the number of rows and columns in a DataFrame?

print(df.shape)

# Question 6: How do you check the data types of all columns in a DataFrame?

print(df.dtypes)

# Question 7: How do you print the first row of the DataFrame?

print(df.iloc[0])

# Question 8: Using the same DataFrame, how do you add a new column city with values ["Pune", "Mumbai", "Delhi"]?
df['city'] = ["Pune", "Mumbai", "Delhi", "Hyderabad", "Mumbai", "Bangalore"]
print(df)

# Question 9: How do you select and print only the rows where city is "Pune"?

# Solution 1
print(df[df['city'] == 'Pune'])

# Solution 2
for index, row in df.iterrows():
    if row['city'] == "Pune":
        print(row)

# Question 10: How do you select only the name and city columns from the DataFrame?

print(df[['name', 'age']])

# Question 11: How do you select all rows where age is greater than 30?

print(df[df['age'] > 30])

# Question 12: How do you select rows where age is greater than 30 and city is "Mumbai"?

print(df[(df['age'] > 30) & (df['city'] == 'Mumbai')])

# Question 13: How do you select rows where age is either less than 25 OR greater than 50?

print(df[(df['age'] < 25) | (df['age'] > 50)])

# Question 14: How do you select only the name and age columns for rows where age > 30?

print(df[df['age'] > 30][['name', 'age']])

print(df.loc[df['age'] > 30, ["name", "age"]])

# Question 15: How do you access the name value from the first row?
print(df.iloc[0]['name'])
# or
print(df.loc[0, 'name'])

# Question 16: How do you update Rajan's city from "Delhi" to "Bangalore"?

df.loc[df['name'] == 'Pushpak', 'city'] = 'Bangalore'

print(df)

# Question 17: How do you update the age of Harsh from 34 to 35?

df.loc[df["name"] == "Harsh", "age"] = 35

# Question 18: How do you create a new column is_adult that is True when age >= 18 and False otherwise?

df['is_adult'] = df['age'] >= 18
print(df)

# Question 19: How do you create a new column age_plus_5 where each value is age + 5?
df["age_plus_5"] = df["age"] + 5

# Question 20: How do you delete the city column from the DataFrame?

df.drop('city', axis=1, inplace=True)

# or

df = df.drop('city', axis=1)

# Question 21: How do you remove all rows where age < 30?

df = df[df['age'] < 30]

# or

df.drop(df[df['age'] < 30].index, inplace=True)

