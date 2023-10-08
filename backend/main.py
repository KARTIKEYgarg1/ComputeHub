import json
import math
import datetime

def calculator(operation, number1, number2):
    if operation == 'add':
        return number1 + number2
    elif operation == 'subtract':
        return number1 - number2
    elif operation == 'multiply':
        return number1 * number2
    elif operation == 'divide':
        if number2 == 0:
            raise ValueError('Division by zero is not allowed.')
        return number1 / number2
    elif operation == 'cube':
        return number1 ** 3
    elif operation == 'root':
        if number1 < 0:
            raise ValueError('Square root is not defined for negative numbers.')
        return math.sqrt(number1)
    elif operation == 'square':
        return number1 ** 2
    elif operation == 'fact':
        if number1 < 0:
            raise ValueError('Factorial is not defined for negative numbers.')
        return math.factorial(number1)
    else:
        raise ValueError('Invalid operation.')

def temp_conversion(operation, temperature):
    if operation == 'ftoD':
        return (temperature - 32) * 5.0/9.0
    elif operation == 'dtoF':
        return temperature * 9.0/5.0 + 32
    else:
        raise ValueError('Invalid temperature conversion operation.')

def two_points(x1, y1, x2, y2):
    # Equation of line: y = mx + b, where m is the slope
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    equation_of_line = f'y = {m}x + {b}'
    
    # Manhattan distance: |x2 - x1| + |y2 - y1|
    manhattan_distance = abs(x2 - x1) + abs(y2 - y1)
    
    # Euclidean distance: sqrt((x2 - x1)^2 + (y2 - y1)^2)
    euclidean_distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    return equation_of_line, manhattan_distance, euclidean_distance

def bmi_calculator(age, weight, height):
    height_in_meters = height / 100  # convert height from cm to meters
    bmi_index = weight / (height_in_meters ** 2)
    
    if bmi_index < 18.5:
        status = 'Underweight'
    elif 18.5 <= bmi_index < 24.9:
        status = 'Normal weight'
    elif 25 <= bmi_index < 29.9:
        status = 'Overweight'
    else:
        status = 'Obese'
    
    return bmi_index, status

def age_calculator(birthdate):
    birthdate = datetime.datetime.strptime(birthdate, '%Y-%m-%d').date()
    current_date = datetime.datetime.now().date()
    
    age = current_date.year - birthdate.year - ((current_date.month, current_date.day) < (birthdate.month, birthdate.day))
    
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    birth_day_of_week = days_of_week[birthdate.weekday()]
    
    return age, birth_day_of_week

def predict_price(square_feet, bedrooms, bathrooms, location):
    locations = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego']
    location_flags = [0] * len(locations)
    if location in locations:
        location_flags[locations.index(location)] = 1
    else:
        print(f'Error: Invalid location - {location}')
        return None
    modified_values = [square_feet, bedrooms, bathrooms] + location_flags
    coeff = [-6.37542592, 1222.21821, 4252.9471, 4501.18216, 18241.0398, 3212.25088, 4652.57369, 12466.7552, -3875.22794]
    weighted_values = [modified_values[i] * coeff[i] for i in range(9)]
    predicted_price = sum(weighted_values) + 547035.8941609525
    return int(predicted_price)


def home_price_predictor(location, square_feet, bedrooms, bathrooms):
    predicted_price = predict_price(square_feet, bedrooms, bathrooms, location)
    if predicted_price is not None:
        return predicted_price
    else:
        raise ValueError('Error: Invalid location')

def lambda_handler(event, context):
    query_parameters = event.get('queryStringParameters', {})
    category = query_parameters.get('category')
    operation = query_parameters.get('operation')
    # Handle CORS
    headers = {
        'Access-Control-Allow-Origin': '*',  # Allow requests from any origin
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',
    }
            
    try:
        if not category:
            raise ValueError('Category is missing.')
        
        if category == 'calculator':
            number1 = float(query_parameters.get('number1', 0))
            number2 = float(query_parameters.get('number2', 0))
            if not number1 or not number2:
                raise ValueError('Number1 and/or Number2 is missing.')
            result = calculator(operation, number1, number2)
        elif category == 'temp_conv':
            temperature = float(query_parameters.get('temperature', 0))
            if not temperature:
                raise ValueError('Temperature is missing.')
            result = temp_conversion(operation, temperature)
        elif category == '2_points':
            x1 = float(query_parameters.get('x1', 0))
            y1 = float(query_parameters.get('y1', 0))
            x2 = float(query_parameters.get('x2', 0))
            y2 = float(query_parameters.get('y2', 0))
            if not x1 or not y1 or not x2 or not y2:
                raise ValueError('x1, y1, x2, and/or y2 is missing.')
            result = two_points(x1, y1, x2, y2)
        elif category == 'bmi':
            age = int(query_parameters.get('age', 0))
            weight = float(query_parameters.get('weight', 0))
            height = float(query_parameters.get('height', 0))
            if not age or not weight or not height:
                raise ValueError('Age, weight, and/or height is missing.')
            result = bmi_calculator(age, weight, height)
        elif category == 'age_calculator':
            birthdate = query_parameters.get('birthdate')
            if not birthdate:
                raise ValueError('Birthdate is missing.')
            result = age_calculator(birthdate)
        elif category == 'home_price_predictor':
            location = query_parameters.get('location')
            square_feet = float(query_parameters.get('square_feet', 0))
            bedrooms = int(query_parameters.get('bedrooms', 0))
            bathrooms = int(query_parameters.get('bathrooms', 0))
            if not location or not square_feet or not bedrooms or not bathrooms:
                raise ValueError('Location, square feet, bedrooms, and/or bathrooms is missing.')
            result = home_price_predictor(location, square_feet, bedrooms, bathrooms)
            
        else:
            raise ValueError('Invalid category.')
 
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({'result': result})
        }
    except ValueError as e:
        return {
            'statusCode': 400,
            'headers': headers,
            'body': json.dumps({'error': str(e)})
        }
