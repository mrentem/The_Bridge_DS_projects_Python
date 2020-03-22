####################################################################################
### EXPLORATORY DATA ANALYSIS AND DATA CLEANING FUNCTIONS LIBRARY ##################
####################################################################################

# Ref.: https://towardsdatascience.com/creating-python-functions-for-exploratory-data-analysis-and-data-cleaning-2c462961bd71

## INDEX:

# 1. Handling Missing Values
# 2. Data Visualization
# 3. Handling Data Types

####################################################################################


### 1. HANDLING MISSING VALUES

# 1.1. Function to give a general idea of the percentage of missing data in each column:

def intitial_eda_checks(df):
    '''
    Takes df
    Checks nulls
    '''
    if df.isnull().sum().sum() > 0:
        mask_total = df.isnull().sum().sort_values(ascending=False) 
        total = mask_total[mask_total > 0]

        mask_percent = df.isnull().mean().sort_values(ascending=False) 
        percent = mask_percent[mask_percent > 0] 

        missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    
        print(f'Total and Percentage of NaN:\n {missing_data}')
    else: 
        print('No NaN found.')

## 1.2. Checking columns which are above a certain percentage of missing values:

def view_columns_w_many_nans(df, missing_percent):
    '''
    Checks which columns have over specified percentage of missing values
    Takes df, missing percentage
    Returns columns as a list
    '''
    mask_percent = df.isnull().mean()
    series = mask_percent[mask_percent > missing_percent]
    columns = series.index.to_list()
    print(columns) 
    return columns

## 1.3. Eliminating columns with missing values above a certain amount:

def drop_columns_w_many_nans(df, missing_percent):
    '''
    Takes df, missing percentage
    Drops the columns whose missing value is bigger than missing percentage
    Returns df
    '''
    series = view_columns_w_many_nans(df, missing_percent=missing_percent)
    list_of_cols = series.index.to_list()
    df.drop(columns=list_of_cols)
    print(list_of_cols)
    return df

# Ref.: https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html

####################################################################################

### 2. DATA VISUALIZATION

## 2.1. Ploting histogram of numeric columns:

def histograms_numeric_columns(df, numerical_columns):
    '''
    Takes df, numerical columns as list
    Returns a group of histagrams
    '''
    f = pd.melt(df, value_vars=numerical_columns) 
    g = sns.FacetGrid(f, col='variable',  col_wrap=4, sharex=False, sharey=False)
    g = g.map(sns.distplot, 'value')
    return g

## 2.2. Creating a heatmap for dependent (target) and independent variables (features):

def heatmap_numeric_w_dependent_variable(df, dependent_variable):
    '''
    Takes df, a dependant variable as str
    Returns a heatmap of all independent variables' correlations with dependent variable 
    '''
    plt.figure(figsize=(8, 10))
    g = sns.heatmap(df.corr()[[dependent_variable]].sort_values(by=dependent_variable), 
                    annot=True, 
                    cmap='coolwarm', 
                    vmin=-1,
                    vmax=1) 
    return g


####################################################################################

### 3. HANDLING DATA TYPES

## 3.1. Transforming categorical to ordinal variables:

def categorical_to_ordinal_transformer(categories):
    '''
    Returns a function that will map categories to ordinal values based on the
    order of the list of `categories` given. Ex.

    If categories is ['A', 'B', 'C'] then the transformer will map 
    'A' -> 0, 'B' -> 1, 'C' -> 2.
    '''
    return lambda categorical_value: categories.index(categorical_value)

## 3.2. 



## SINTAXIS BASICA DE UN DECORADOR:

def decorator(*args, **kwargs): 
    print("Inside decorator") 
    def inner(func): 
        print("Inside inner function") 
        print("I like", kwargs['like'])  
        return func 
    return inner 
  
@decorator(like="geeksforgeeks") 
def func(): 
    print("Inside actual function") 
  
func()