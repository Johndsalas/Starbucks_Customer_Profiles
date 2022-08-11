''' File is to save functions needed to prepare the starbucks survey data'''

# Imports
import pandas as pd
import numpy as np

############################################## Main Prepare Function ################################################

def prepare_customer_survey(df):
    '''takes in unprepared customer data and returns prepared customer data'''

    # drop timestamp
    df.drop(columns='Timestamp', inplace=True)

    # drop columns with null values
    df = df.dropna()

    # rename columns for brevity
    df = df.rename(columns={'1. Your Gender':'gender', 
                            '2. Your Age':'age_group',
                            '3. Are you currently....?':'employment_status', 
                            '4. What is your annual income?':'annual_income_group',
                            '5. How often do you visit Starbucks?':'visit_frequency',
                            '6. How do you usually enjoy Starbucks?':'dining_type',
                            '7. How much time do you normally  spend during your visit?':'visit_length',
                            '8. The nearest Starbucks\'s outlet to you is...?':'distance_away',
                            '9. Do you have Starbucks membership card?':'membership_card',
                            '10. What do you most frequently purchase at Starbucks?':'most_frequent_purchase',
                            '11. On average, how much would you spend at Starbucks per visit?':'spend_per_visit',
                            '12. How would you rate the quality of Starbucks compared to other brands (Coffee Bean, Old Town White Coffee..) to be:':'brand_rating',
                            '13. How would you rate the price range at Starbucks?':'price_rating',
                            '14. How important are sales and promotions in your purchase decision?':'promotion_importance',
                            '15. How would you rate the ambiance at Starbucks? (lighting, music, etc...)':'ambiance_rating',
                            '16. You rate the WiFi quality at Starbucks as..':'wifi_rating',
                            '17. How would you rate the service at Starbucks? (Promptness, friendliness, etc..)':'service_rating',
                            '18. How likely you will choose Starbucks for doing business meetings or hangout with friends?':'gathering_likelyhood',
                            '19. How do you come to hear of promotions at Starbucks? Check all that apply.':'promotions_from',
                            '20. Will you continue buying at Starbucks?':'continue_buying'})
    
    # remove white space at the beginning and end of each value if not an int type
    for col in df.columns:
        
        try:
    
            df[f'{col}'] = df[f'{col}'].apply(lambda value: value.strip())
        
        except:
            
            pass

    # create dummy columns for contains most frequently purchased items
    items = ['Coffee',
            'Cold drinks',
            'Pastries',
            'Sandwiches',
            'Juices']

    for item in items:

        df[f'{item}'] = df['most_frequent_purchase'].str.contains(f'{item}')

    # apply fix_never to dining_type to consolidate all never responces as never
    df['dining_type'] = df['dining_type'].apply(fix_never)


    df['promotion_importance'] = df.promotion_importance.apply(get_importance_string)
    df['gathering_likelyhood'] = df.gathering_likelyhood.apply(get_likelyhood_string)

    ratings = ['brand_rating',
               'price_rating',
               'ambiance_rating',
               'wifi_rating',
               'service_rating']

    for rating in ratings:
        
        df[f'{rating}'] = df[f'{rating}'].apply(get_rating_string)

    return df

############################################## Helper Functions ################################################

def fix_never(value):
    '''Checks values in a pandas datafrema for "Dine in", "Take away", and "Drive-thru" values
       if it is one of those values return that value otherwise return "Never"'''
    
    if (value != "Take away") & (value != "Dine in") & (value != "Drive-thru"):
    
        return "Never"
    
    else:
        
        return value

def get_importance_string(value):
    
    if value <= 2:
        
        return "unimportant"
    
    elif value == 3:
        
        return "neutral"
    
    elif value >= 4:
        
        return "important"
    
def get_likelyhood_string(value):
    
    if value <= 2:
        
        return "unlikely"
    
    elif value == 3:
        
        return "neutral"
    
    elif value >= 4:
        
        return "likely"
    
def get_rating_string(value):
    
    if value <= 2:

        return "negative"

    elif value == 3:

        return "neutral"

    elif value >= 4:

        return "positive"