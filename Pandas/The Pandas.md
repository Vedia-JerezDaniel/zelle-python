# The Pandas

```python
movies.dtypes

dtypes.value_counts()
```

The .value_counts method returns the count of all the data types in the DataFrame when  called on the .dtypes attribute.

**The usage of .loc** specifies a selector for both rows and columns separated by  a comma. The row selector is a slice with no start or end name (:) which means  select all of the rows. The column selector will just pull out the column named  director_name. 

**The .iloc index** operation also specifies both row and column selectors. The row  selector is the slice with no start or end index (:) that selects all of the rows. The  column selector, 1, pulls off the second column (remember that Python is zero-based):

```python
movies.loc[:, "director_name"]
movies.iloc[:,1]
```

In this recipe, we determined that there were missing values in the Series by observing  that the result from the .count method did not match the .size attribute.

 A more direct  approach is to inspect the **.hasnans** attribute: 

> >> director.hasnans True 
> >>
> >> There exists a complement of .isna; 
> >>
> >> the .notna method, which returns True for all the  non-missing values:

*The correct way for debugging*

```python
(fb_likes.fillna(0)
         # .astype(int)
         .head()
)
```

```python
def debug_df(df):
    print("BEFORE")
    print(df)
    print("AFTER")
    return df
    
(fb_likes.fillna(0)
         .pipe(debug_df)
         .astype(int) 
         .head(5)
)

# Setting a global

intermediate = None
def get_intermediate(df):
    global intermediate
    intermediate = df
    return df

res = (fb_likes.fillna(0)
         .pipe(get_intermediate)
         .astype(int) 
         .head()
)


## RENAME

df.rename(columns={"A": "a", "B": "c"})

### ROWS AND COLUMNS
ids[0] = 'Ratava'
ids[1] = 'POC'
ids[2] = 'Ertceps'
columns[1] = 'director'
columns[-2] = 'aspect'
columns[-1] = 'fblikes'
movies.index = ids
movies.columns = columns

def to_clean(val):
    return val.strip().lower().replace(' ', '_')

movies.rename(columns=to_clean).head(3)

# FUNCTIONS AND COLUMNS

cols = ['actor_1_facebook_likes','actor_2_facebook_likes',
    'actor_3_facebook_likes','director_facebook_likes']

sum_col = movies[cols].sum(axis=1)
sum_col.head(5)

movies.assign(total_likes=sum_col).head(5)

# toma el indice de la columna
profit_index = movies.columns.get_loc('gross') + 1
profit_index

movies.insert(loc=profit_index,
              column='profit',
              value=movies['gross'] - movies['budget'])




```

