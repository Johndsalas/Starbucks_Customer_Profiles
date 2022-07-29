'Contains functions for exploring the Satrbucks survey data'
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

################################### Part I: What are the customers characteristics? ####################################
 
def gender_pie(df):
    'Creates pie chart of gender distribution'
    
    # set values and labels for chart
    values = [len(df.gender[df.gender == 'Male']), len(df.gender[df.gender == 'Female'])]
    labels = ['Male','Female'] 

    # generate and show chart
    plt.pie(values, labels=labels, autopct='%.0f%%', colors=['#ffc3a0', '#c0d6e4'])
    plt.title('Gender is evenly divided amoung Starbucks customers')
    plt.show()


def age_pie(df):
    'Creates pie chart of age distribution'

    # set values and labels for chart
    values = [len(df.age_group[df.age_group == 'Below 20']), 
              len(df.age_group[df.age_group == 'From 20 to 29']),
              len(df.age_group[df.age_group == 'From 30 to 39']),
              len(df.age_group[df.age_group == '40 and above'])]
    
    labels = ['Below 20','From 20 to 29', 'From 30 to 39', '40 and above'] 

    # generate and show chart
    plt.pie(values, labels=labels, autopct='%.0f%%', colors=['#ffc3a0', '#c0d6e4', '#cf98eb', '#77d198'])
    plt.title('The majority of Starbucks customers are between the age of 20 and 29')
    plt.show()


def employment_pie(df):
    'Creates pie chart of age distribution'

    # set values and labels for chart
    values = [len(df.employment_status[df.employment_status == 'Employed']), 
              len(df.employment_status[df.employment_status == 'Student']),
              len(df.employment_status[df.employment_status == 'Self-employed']),
              len(df.employment_status[df.employment_status == 'Housewife'])]
    
    labels = ['Employed','Student', 'Self-employed', 'Housewife'] 

    # generate and show chart
    plt.pie(values, labels=labels, autopct='%.0f%%', colors=['#ffc3a0', '#c0d6e4', '#cf98eb', '#77d198'])
    plt.title('1/2 of Starbucks customers are Employed 1/3 of them are students')
    plt.show()


def income_pie(df):
    'Creates a pie chart of the income distribution'

    values = [len(df.annual_income_group[df.annual_income_group == 'Less than RM25,000']), 
          len(df.annual_income_group[df.annual_income_group == 'RM25,000 - RM50,000']),
          len(df.annual_income_group[df.annual_income_group == 'RM50,000 - RM100,000']),
          len(df.annual_income_group[(df.annual_income_group == 'RM100,000 - RM150,000') 
                                     | (df.annual_income_group == 'More than RM150,000')])]

    labels = ['Less than RM25,000', 
            'RM25,000 - RM50,000 ',
            'RM50,000 - RM100,000',
            'More than RM100,000'] 

    plt.pie(values, labels=labels, autopct='%.0f%%', colors=['#ffc3a0', '#c0d6e4', '#cf98eb', '#77d198'])
    plt.title('Over 1/2 of Starbucks customers make less than 25K annually')
    plt.show()


def visit_pie(df):
    'Creates a pie chart of the income distribution'
    values = [len(df.visit_frequency[(df.visit_frequency == 'Daily')
                                | (df.visit_frequency == 'Weekly')]),
          len(df.visit_frequency[(df.visit_frequency == 'Monthly')]),
          len(df.visit_frequency[(df.visit_frequency == 'Rarely') 
                                | (df.visit_frequency == 'Never')])]

    labels = ['Daily or Weekly', 
            'Monthly',
            'Rarely or Never'] 

    plt.pie(values, labels=labels, autopct='%.0f%%', colors=['#ffc3a0', '#c0d6e4', '#cf98eb'])
    plt.title('Most of Starbucks customers visit infrequently')
    plt.show()


def distance_pie(df):
    'Creates a pie chart of the distance from Starbucks distribution'

    values = [len(df.distance_away[(df.distance_away == 'more than 3km')]),
          len(df.distance_away[(df.distance_away == '1km - 3km')]),
          len(df.distance_away[(df.distance_away == 'within 1km')])]

    labels = ['more than 3km', 
              '1km - 3km',
              'within 1km'] 

    plt.pie(values, labels=labels, autopct='%.0f%%', colors=['#ffc3a0', '#c0d6e4', '#cf98eb'])
    plt.title('1/2 of Starbucks customers live more than 3km from a Satrbucks')
    plt.show()


def spend_pie(df):
    'Creates distribution of spent per visit distribution'

    values = [len(df.spend_per_visit[df.spend_per_visit == 'Zero']), 
          len(df.spend_per_visit[df.spend_per_visit == 'Less than RM20']),
          len(df.spend_per_visit[df.spend_per_visit == 'Around RM20 - RM40']),
          len(df.spend_per_visit[(df.spend_per_visit == 'More than RM40')])]

    labels = ['Zero', 
            'Less than RM20',
            'Around RM20 - RM40',
            'More than RM40'] 

    plt.pie(values, labels=labels, autopct='%.0f%%', colors=['#ffc3a0', '#c0d6e4', '#cf98eb', '#77d198'])
    plt.title('A majority of Starbucks customers spend less than 20RM per visit')
    plt.show()