import numpy as np
import pandas as pd

"""
this function is created to return the month name and its necesary month id
"""
def get_month_name(month_id):
    month_names = np.array(
        ["January ", "February", "March    ", "April    ", "May      ", "June    ", "July     ", "August  ",
         "September", "October ", "November", "December"])
    return month_names[month_id - 1]


# array to hold years and saving
prev_year = np.zeros(12)   #create the numpy array of 12 data
current_year = np.zeros(12)
savings = np.zeros(12)


"""
this function is return to validate user input 
"""
def validate_user_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError(
                    "Invalid input - the entered amount must be positive")
            return value
        except ValueError as error:
            print(error)


"""
creating the user input 
"""
print("Enter the energy bills of current year each month")
for i in range(12):
    prev_year[i] = validate_user_input(
        f"Enter bill for month {get_month_name(i + 1)}: ")

#
print("\nEnter the energy bills of last year each month")
for i in range(12):
    current_year[i] = validate_user_input(
        f"Enter bill for month {get_month_name(i + 1)}: ")


"""
this is numpy function createdd to calculate total saving and energy differences
"""
def calculate_savings(prev_year, current_year):
    difference_energy = np.array(prev_year) - np.array(current_year)
    savings = np.round((difference_energy / np.array(prev_year)) * 100, 2)
    return difference_energy, savings


# Function to calculate average savings from the np library
def calculate_average_savings(savings):
    return np.mean(savings)

# correlation coefficient to retrun the postive and negative correlation
def get_calculate_type(r):
    if r > 0:
        correlation_type = "Positive"
    elif r < 0:
        correlation_type = "Negative"
    else:
        correlation_type = "No"
    return (correlation_type)


#this function is return to do min and max saving calculation
def find_max_min_savings(savings):
    max_saving_index = np.argmax(savings)
    min_saving_index = np.argmin(savings)
    #getting month index
    max_month = max_saving_index + 1
    min_month = min_saving_index + 1
    #getting max and min values
    max_savings = savings.max()
    min_savings = savings.min()
    return max_month, min_month, max_savings, min_savings


# Replace invalid entries with NaN
def impute_nan_values(data):
    cleaned_data = []
    for value in data:
        if isinstance(value, int) or isinstance(value, float):
            cleaned_data.append(value)
        else:
            cleaned_data.append(np.nan)
    return cleaned_data

# function to return valid data set for the correlation
def calculating_corr(x, y):
    x_set = impute_nan_values(x)
    y_set = impute_nan_values(y)

    x_column = np.array(x_set)
    y_column = np.array(y_set)

    # pandas dataframe for the given columns
    df1 = pd.DataFrame({'x_column': x_column, 'y_column': y_column})

    # dropping rows with null values
    df1 = df1.dropna()

    # calculate the correlation coefficient
    correlation_coefficient = df1['x_column'].corr(df1['y_column'])

    return get_calculate_type(correlation_coefficient), correlation_coefficient


# creating a panda's DataFrame to display the values
df = pd.DataFrame({
    "2019": prev_year,
    "2020": current_year,
    "X": [100, 110, 111, None, 121, 150, 151, 152, None, "s,g", 177, 179] 
})




print("Month\t\t\t|\t\t2019\t|\t\t2020\t|\t\tX\t\t|\tSaving")
print("******\t\t\t|\t\t******\t|\t\t******\t|\t\t******\t|\t******")

# Assigning values to savings from calculate_savings function
savings, grand_total_saving = calculate_savings(prev_year, current_year)

for index, row in df.iterrows():
    year1 = row['2019']
    year2 = row['2020']
    x = row['X']

    print("%s\t\t|\t\t%d\t\t|\t\t%d\t\t|\t\t%s\t\t|\t\t%d" % (
        get_month_name(index + 1), year1, year2, str(x), savings[index]))

# Find maximum and minimum savings
# print the values with the month
(max_month, min_month, max_savings, min_savings) = find_max_min_savings(savings)
print("\nMonth that has maximum saving: %s - amount %d" % (get_month_name(max_month), max_savings))
print("month that has minimum saving: %s - amount %d" % (get_month_name(min_month), min_savings))

#calculating the average saving
average_savings = calculate_average_savings(savings)
print("Monthly average savings: %d" % average_savings)

# doing the correlation test with respect to savings
(correlation_type, r) = calculating_corr(df["X"], savings)
print("\nCorrelation coefficient between energy bills and savings: %f" % r)
print("Correlation type: %s" % correlation_type)