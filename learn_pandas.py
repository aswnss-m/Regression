"""
Pandas is an import part in data science , as it is used to handle , modify and collect data
ftom various file formats 
Series: 
1 dimentional labelled array capable of holding any data type , its similar to a column in excel sheet

DataFrame:
2-dimentional labelled data structure with columns of potential different types
(simply its the collection of series )

Both series and dataframes are the building blocks of pandas
"""
#this is the commonly used way of importing pandas
import pandas as pd

#to read any file we use .read_<extension> : extention maybe csv , excel etc

data_frame = pd.read_csv('sajitha_hse_results.csv')

#now the data_frame holds the data inside the csv we passed , and the data_frame has a type of

type(data_frame)
#<class 'pandas.core.frame.DataFrame'>

#to know the shape of the csv file we have a similar shape attribute as of numpy in pandas too
data_frame.shape
#this will return (6, 13) which corresponds to (rows , columns)

#so we know that there are 13 columns in the data_frame and inorder to get the label of 
#all the columns we have an attribute columns which will return the list of column labels
data_frame.columns

#this is will retun Index(['Subjects', '1st CE', '1st TE', '1st Total', '2nd CE', '2nd PE',
      #  '2nd TE', '2nd Total', 'Total CE', 'Total PE', 'Total TE', 'Total','Grade Obtained'],
      # dtype='object')


#to have a sneak peek inside the data_frame we can use
data_frame.head(3)
#this shows the top 3 rows of the data_frame .head(no_of_rows)

data_frame.tail(2)
#this shows the the last 2 rows of the data_frame .tail(no_of_rows)

#inorder to get more information like datatype , memory used etc etc there are two ways 

data_frame.info()
#this gives a quick overall information about the dataframe ,
#output :
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 6 entries, 0 to 5
# Data columns (total 13 columns):
#  #   Column          Non-Null Count  Dtype 
# ---  ------          --------------  ----- 
#  0   Subjects        6 non-null      object
#  1   1st CE          6 non-null      int64 
#  2   1st TE          6 non-null      int64 
#  3   1st Total       6 non-null      int64 
#  4   2nd CE          6 non-null      int64 
#  5   2nd PE          6 non-null      object
#  6   2nd TE          6 non-null      int64 
#  7   2nd Total       6 non-null      int64 
#  8   Total CE        6 non-null      int64 
#  9   Total PE        6 non-null      object
#  10  Total TE        6 non-null      int64 
#  11  Total           6 non-null      int64 
#  12  Grade Obtained  6 non-null      object
# dtypes: int64(9), object(4)
# memory usage: 752.0+ bytes


data_frame.describe()

#this will give some more information about the data stored in the dataframe
#ouput 
#       1st CE     1st TE  1st Total  ...  Total CE    Total TE       Total
# count     6.0   6.000000   6.000000  ...       6.0    6.000000    6.000000
# mean     20.0  36.666667  56.666667  ...      40.0   77.166667  140.333333
# std       0.0  20.490648  20.490648  ...       0.0   36.074460   24.179881
# min      20.0  18.000000  38.000000  ...      40.0   41.000000  120.000000
# 25%      20.0  21.000000  41.000000  ...      40.0   52.000000  121.750000
# 50%      20.0  32.500000  52.500000  ...      40.0   78.000000  132.500000
# 75%      20.0  44.000000  64.000000  ...      40.0   80.750000  151.500000
# max      20.0  72.000000  92.000000  ...      40.0  141.000000  181.000000

# [8 rows x 9 columns]



#inorder to get the values of a single column we can specify it using the column name with the data_frame object

data_frame['Grade Obtained']
#this will return just the specified column
#output
# 0     B
# 1    A+
# 2     B
# 3     B
# 4    B+
# 5     B
# Name: Grade Obtained, dtype: object

#we can also specify multiple columns to get the values of them by

data_frame[['Subjects','Grade Obtained']]
#this will return the values of the specified columns only
#ouput
#            Subjects Grade Obtained
# 0           English              B
# 1             Hindi             A+
# 2           Physics              B
# 3         Chemistry              B
# 4  Computer Science             B+
# 5             Maths              B


#we can also slice the data frame accroding to our wish using the indexlocation atribute ( .iloc[rows,columns]  )
#where the rows and columns are similar to the string slicing " begining_index : ending_index  "
#where it will select all the rows/columns from the begining_index till the ending_index - 1

#To visualise in more we can load a different data 

data_frame_cancer = pd.read_csv('cancer_data.csv')
#this has the shape (3141, 11)
data_frame_cancer.columns

#output
# Index(['County', 'FIPS', 'Met Objective of 45.5? (1)',
#        'Age-Adjusted Death Rate',
#        'Lower 95% Confidence Interval for Death Rate',
#        'Upper 95% Confidence Interval for Death Rate',
#        'Average Deaths per Year', 'Recent Trend (2)',
#        'Recent 5-Year Trend (2) in Death Rates',
#        'Lower 95% Confidence Interval for Trend',
#        'Upper 95% Confidence Interval for Trend'],
#       dtype='object')

#now its time for the slicing
data_frame_cancer_sliced = data_frame_cancer.iloc[0:10,2:5]

#this will slice the cancer_data into a new dataframe with the columns from 3rd to 5th (index 5 contains the 6th column by the way)
# output
#   Met Objective of 45.5? (1)  ... Lower 95% Confidence Interval for Death Rate
# 0                         No  ...                                         45.9
# 1                         No  ...                                        108.9
# 2                         No  ...                                        100.2
# 3                         No  ...                                           73
# 4                         No  ...                                         83.1
# 5                         No  ...                                         89.9
# 6                         No  ...                                         90.6
# 7                         No  ...                                           87
# 8                         No  ...                                         84.8
# 9                         No  ...                                         76.4

#you can also specify the column indexes you want to slice , but rows need to be in a range 

data_frame_cancer_sliced = data_frame_cancer.iloc[:10,[0,3,6]]
#this will select the following columns
#'County','Age-Adjusted Death Rate','Average Deaths per Year' corresponding to their index locations
#output
#                         County Age-Adjusted Death Rate Average Deaths per Year
# 0                United States                      46                 157,376
# 1       Perry County, Kentucky                   125.6                      43
# 2      Powell County, Kentucky                   125.3                      18
# 3  North Slope Borough, Alaska                   124.9                       5
# 4      Owsley County, Kentucky                   118.5                       8
# 5        Union County, Florida                   113.5                      19
# 6    McCreary County, Kentucky                   111.1                      22
# 7      Leslie County, Kentucky                   110.3                      16
# 8      Martin County, Kentucky                   109.1                      14
# 9     Menifee County, Kentucky                     106                       9


#you can create and delete columns in pandas by 

data_frame['New Column'] = "n 3^07 ! "

#this creates a column with label New Column with value "n 3^07 !"
#you can easily delete the column by saying

del data_frame['New Column']

#you can also create a column with values of the exsisting columns like 

data_frame["Total TE in 1st and 2nd"] = data_frame["1st TE"] + data_frame["2nd TE"]

#this takes the value from the specified columns and adds and stored in the new column 

#we can have more controll over the string values in our data by invoking the .str object of the pandas

#FOR EXAMPLE 
#lets capitalise all the county names in our previouslys sliced data , we can do that by telling 

data_frame_cancer_sliced['County'] = data_frame_cancer_sliced['County'].str.lower()

#output
#                         County Age-Adjusted Death Rate Average Deaths per Year
# 0                united states                      46                 157,376
# 1       perry county, kentucky                   125.6                      43
# 2      powell county, kentucky                   125.3                      18
# 3  north slope borough, alaska                   124.9                       5
# 4      owsley county, kentucky                   118.5                       8
# 5        union county, florida                   113.5                      19
# 6    mccreary county, kentucky                   111.1                      22
# 7      leslie county, kentucky                   110.3                      16
# 8      martin county, kentucky                   109.1                      14
# 9     menifee county, kentucky                     106                       9

#we can also filter through the data 

#FOR EXAMPLE 
#lets create a new data frame with total marks more than 130

data_frame_filtered = data_frame[data_frame['Total'] > 130]

#this created a new data frame which has the Total value > 130 , 
data_frame_filtered['Total'].min()

# returns 141 , which is the mininmum value

#you can also pass multiple conditions like

data_frame_filtered = data_frame[(data_frame['Total'] > 140) & (data_frame['Grade Obtained'] == 'B')]

#which has only one row 

#you can also verify this by seeing the unique values which is stored in this using

data_frame_filtered['Grade Obtained'].unique()

# which returns array(['B'])

#well if we use the same function with the previous data frame we get
data_frame['Grade Obtained'].unique()
#returns array(['B', 'A+', 'B+'], dtype=object)


#sorting the data based on columns 
data_frame_cancer_sliced_sorted = data_frame_cancer_sliced.sort_values(['Age-Adjusted Death Rate','Average Deaths per Year'])

#this will sort the datas according the fisrt column and then the second column