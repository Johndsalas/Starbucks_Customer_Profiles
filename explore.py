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

################################### Part II: Why do customers come to Starbucks? ####################################

def visit_length_pie(df):

    # set values and labels for chart
    values = [len(df.visit_length[df.visit_length == 'Below 30 minutes']), 
            len(df.visit_length[df.visit_length == 'Between 30 minutes to 1 hour']),
            len(df.visit_length[df.visit_length == 'Between 1 hour to 2 hours']),
            len(df.visit_length[(df.visit_length == 'Between 2 hours to 3 hours') 
                                | (df.visit_length == 'More than 3 hours')])]

    labels = ['< 30 min','30 min to 1 Hour', 'Between 1 and 2 Hours', '> 2 Hours'] 

    # generate and show chart
    plt.pie(values, labels=labels, autopct='%.0f%%', colors=['#ffc3a0', '#c0d6e4', '#cf98eb', '#77d198'])
    plt.title('A large majority of Starbucks customers spend less than 30 minutes per visit')
    plt.show()


def dining_type(df):

    # set values and labels for chart
    values = [len(df.dining_type[df.dining_type == 'Take away']), 
            len(df.dining_type[df.dining_type == 'Dine in']),
            len(df.dining_type[df.dining_type == 'Drive-thru'])]

    labels = ['Take away','Dine in', 'Drive-thru'] 

    # generate and show chart
    plt.pie(values, labels=labels, autopct='%.0f%%', colors=['#ffc3a0', '#c0d6e4', '#cf98eb'])
    plt.title('Only 40% of Starbucks customers are Dine in customers')
    plt.show()

def coffee_cold_drink_only(df):
    '''Create three Pie chart subplots in one figgure showing only drink buying habbits'''

    # define figure size and title
    plt.figure(figsize=(12,12))

    # first subplot
    plt.subplot(1,3,1)

    # define values and labels
    values = [len(df.most_frequent_purchase[df.most_frequent_purchase == 'Coffee']),
            len(df.most_frequent_purchase[df.most_frequent_purchase != 'Coffee'])]
    labels = ['Only Coffee', 'Other']

    # make chart and add subtitle 
    plt.pie(values, labels=labels, autopct='%.0f%%', colors=['#ffc3a0', '#c0d6e4'])
    plt.title('Customers Ordering Only Coffee')

    # second subplot
    plt.subplot(1,3,2)

    # define values and labels
    values = [len(df.most_frequent_purchase[df.most_frequent_purchase == 'Cold drinks']),
            len(df.most_frequent_purchase[df.most_frequent_purchase != 'Cold drinks'])]
    labels = ['Only Cold drink', 'Other']

    # make chart and add subtitle
    plt.pie(values, labels=labels, autopct='%.0f%%', colors=['#ffc3a0', '#c0d6e4'])
    plt.title('Customers Ordering Only Cold Drink')

    # third subplot
    plt.subplot(1,3,3)

    # define values and labels
    values = [len(df.most_frequent_purchase[(df.most_frequent_purchase == 'Coffee')
                                            | (df.most_frequent_purchase == 'Cold drinks')]),
            len(df.most_frequent_purchase[(df.most_frequent_purchase != 'Coffee')
                                            & (df.most_frequent_purchase != 'Cold drinks')])]
    labels = ['Just Drink', 'Other']

    # make chart and add subtitle
    plt.pie(values, labels=labels, autopct='%.0f%%', colors=['#ffc3a0', '#c0d6e4'])
    plt.title('Customers Ordering Just a Drink')

    # print figgure
    plt.suptitle('74% of Customers Order Only a Coffee or Only a Drink')
    plt.tight_layout()
    plt.show()


def coffee_cold_drink_include(df):

    # define figure size and title
    plt.figure(figsize=(12,12))
    plt.suptitle('Coffee and Cold Drinks are the grand Majority of Customer\'s Most Frequent Perchases')

    # first subplot
    plt.subplot(1,3,1)

    # define values and labels
    values = [len(df.Coffee[df.Coffee == True]),
            len(df.Coffee[df.Coffee == False])]
    labels = ['Order Contains Coffee', 'No Coffee']

    # make chart and add subtitle 
    plt.pie(values, labels=labels, autopct='%.0f%%', colors=['#ffc3a0', '#c0d6e4'])
    plt.title('Contains Coffee')

    # second subplot
    plt.subplot(1,3,2)

    # define values and labels
    values = [len(df['Cold drinks'][df['Cold drinks'] == True]),
            len(df['Cold drinks'][df['Cold drinks'] == False])]
    labels = ['Only Cold drink', 'No Cold Drink']

    # make chart and add subtitle
    plt.pie(values, labels=labels, autopct='%.0f%%', colors=['#ffc3a0', '#c0d6e4'])
    plt.title('Contains Cold Drinks')

    # third subplot
    plt.subplot(1,3,3)

    # define values and labels
    values = [len(df.most_frequent_purchase[(df.Coffee == True) | (df['Cold drinks'] == True)]),
            len(df.most_frequent_purchase[(df.Coffee == False) & (df['Cold drinks'] == False)])
            ]
    labels = ['Contains Drink', 'No Drink']

    # make chart and add subtitle
    plt.pie(values, labels=labels, autopct='%.0f%%', colors=['#ffc3a0', '#c0d6e4'])
    plt.title('Contains coffee or cold drink')

    # print figgure
    plt.tight_layout()
    plt.show()


def other_foods(df):

    foods = ['Pastries', 'Sandwiches', 'Juices']

    # define figure size and title
    plt.figure(figsize=(12,12))
    plt.suptitle("Other Foods in Customer's Most Frequent Orders")

    for i, food in enumerate(foods):

        # first subplot
        plt.subplot(1,3,i+1)

        # define values and labels
        values = [len(df[f'{food}'][df[f'{food}'] == True]),
                len(df[f'{food}'][df[f'{food}'] == False])]
                                            
        labels = [f'Order Contains {food}', f'No {food}']

        # make chart and add subtitle 
        plt.pie(values, labels=labels, autopct='%.0f%%', colors=['#ffc3a0', '#c0d6e4'])
        plt.title(f'Contains {food}')
                
    # print figgure
    plt.tight_layout()
    plt.show()

def omni_pie(pan_ser,title = "Super Awsome Title I'll Think of Latter"):
    
    labels = set(value for value in pan_ser)

    values = [len(pan_ser[pan_ser == label]) for label in labels]

    # generate and show chart
    plt.pie(values, labels=labels, autopct='%.0f%%', colors=['#ffc3a0', '#c0d6e4', '#cf98eb', '#77d198'])
    plt.title(f'{title}')
    plt.show()