#!/usr/bin/python3
# Functions to test queries in Furever.py are pulling data from database tables correctly.
# The functions in Furever.py were used to render the information on the website. 
# Table contents have already been tested in Test_tables.py 

####### IMPORTANT ####### Be sure to activate virtual environment before running this test file. See installation instructions at https://flask.palletsprojects.com/en/2.2.x/installation/.
# To run use: python -m unittest -v  Test_Queries.py

import sqlite3
from Furever import app
import unittest
from Furever import get_filtered_petIDs

###############################################################################################
#             Dog Query Test - Test Data Rendered on Webpages Matches Database                                          
###############################################################################################

# Function tests data used to render dog_36636186.html against data in Furever.db
def test_dog_366(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/dog_36636186' and store the response
    response = app.test_client().get('/dog_36636186')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Dog table for data associated with id=36636186
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Dog WHERE id=36636186''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    # hard coded decsription with HTML character entity to represent '
    # ' renders correctly on webpage, but unable to compare to DB without hardcoding
    expected_description = "He is a perfect dog in many ways. He can be left alone with the roam of the house and just sleeps. He only chews on his toys. He&#39;s potty trained. He&#39;s a hilarious home companion.  He has no resource guarding and is great with body handling, he just loves any attention!  He&#39;s smart and can be desensitized to triggers like vacuums and blenders with steady positive association.  He may not have had socialization as a puppy to normal household things like this."
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
    # Print a message indicating that the test passed
    print("test_dog_366: Test passed - Data used to render @app.route('/dog_36636186') matched as expected.")

# Call the function with the name of the database file
test_dog_366('Furever.db')


# Function tests data used to render dog_42904054.html against data in Furever.db
def test_dog_429(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/dog_42904054' and store the response
    response = app.test_client().get('/dog_42904054')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Dog table for data associated with id=42904054
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Dog WHERE id=42904054''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    # hard coded decsription with HTML character entity to represent '
    # ' renders correctly on webpage, but unable to compare to DB without hardcoding
    expected_description = "I&#39;m a Golden Girl in dog form: sassy, sprightly, and a card-carrying member of the AARP. An athletic and active gal, my hobbies include food puzzles, enjoying belly rubs, and tap dancing! I need a kind adopter to make me feel safe and loved for the rest of my years: someone to appreciate my marvelous, unique qualities. I&#39;m a resilient, physically strong, sweetie-pie: well-mannered indoors, and don&#39;t require long walks, but would be happiest with a quiet yard of my own. No humans under 12 years, or kitties or doggos please."
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
    # Print a message indicating that the test passed
    print("test_dog_429: Test passed - Data used to render @app.route('/dog_42904054') matched as expected.")

# Call the function with the name of the database file
test_dog_429('Furever.db')


# Function tests data used to render dog_43078721.html against data in Furever.db
def test_dog_430(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/dog_42904054' and store the response
    response = app.test_client().get('/dog_43078721')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Dog table for data associated with id=43078721
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Dog WHERE id=43078721''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    # hard coded decsription with HTML character entity to represent '
    # ' renders correctly on webpage, but unable to compare to DB without hardcoding
    expected_description = "Ra is a spirited and smart boy with loads of personality. He&#39;s looking for the perfect forever home with the right balance of love, training and structure to help him continue to blossom."
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
     # Print a message indicating that the test passed
    print("test_dog_430: Test passed - Data used to render @app.route('/dog_43078721') matched as expected.")

# Call the function with the name of the database file    
test_dog_430('Furever.db')


# Function tests data used to render dog_45447002.html against data in Furever.db
def test_dog_454(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/dog_45447002' and store the response
    response = app.test_client().get('dog_45447002')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Dog table for data associated with id=45447002
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Dog WHERE id=45447002''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    # hard coded decsription with HTML character entity to represent '
    # ' renders correctly on webpage, but unable to compare to DB without hardcoding
    expected_description = "Hi, I&#39;m Puck, and like most everyone, I have some quirks but that just makes me more interesting. My foster mom says I have lots of nuance... If you don&#39;t know what a Belgian Malinois is, you should read up about us - we are known for loyalty, herding and protection. Me personally, well I&#39;m almost five years old, and have often been told that I&#39;m a handsome boy with my shiny brindle coat and expressive ears. I&#39;m also a fast sprinter with quick reflexes and I love to hunt for small critters outside and chase soccer balls!"
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
     # Print a message indicating that the test passed
    print("test_dog_454: Test passed - Data used to render @app.route('/dog_45447002') matched as expected.")

# Call the function with the name of the database file   
test_dog_454('Furever.db')


# Function tests data used to render dog_48818187.html against data in Furever.db
def test_dog_488(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/dog_48818187' and store the response
    response = app.test_client().get('dog_48818187')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Dog table for data associated with id=48818187
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Dog WHERE id=48818187''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    # hard coded decsription with HTML character entity to represent '
    # ' renders correctly on webpage, but unable to compare to DB without hardcoding
    expected_description = "Pickles didn&#39;t have the best start to his life...he came to us from a situation where he was not consistently treated with love and kindness. It takes a little bit of time for him to warm up and trust, but once you&#39;re in he is totally in love with you! He spent some time in a foster home, and his foster parent told us Pickles was so sweet and loving. He was an incredibly polite houseguest! His favorite nap spots were on the couch or on the floor next to it with his people nearby for some petting and affection. In the morning he likes to run his zoomies out and is always up for a game of ball in the yard. He&#39;s super athletic and very fast! He walks fairly well on leash, but will pull sometimes. The good news is that he&#39;s treat motivated and is a quick study, so he&#39;s ready to learn to have better leash manners."
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
    # Print a message indicating that the test passed
    print("test_dog_488: Test passed - Data used to render @app.route('/dog_48818187') matched as expected.")

# Call the function with the name of the database file   
test_dog_488('Furever.db')


# Function tests data used to render dog_50272539.html against data in Furever.db
def test_dog_5027(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/dog_50272539' and store the response
    response = app.test_client().get('dog_50272539')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Dog table for data associated with id=50272539
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Dog WHERE id=50272539''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    # hard coded decsription with HTML character entity to represent '
    # ' renders correctly on webpage, but unable to compare to DB without hardcoding
    expected_description = "We understand that Thomas may seem shy and anxious at first (especially with men), but with the right training and patience, he has the potential to become a loyal and loving companion. He know lots of cues: sit, stay, come, shake, spin, and leave it! If you&#39;re willing to give him a chance, Thomas will reward you with his playful and affectionate personality. Come meet Thomas and see if he&#39;s the perfect match for your family."
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
    # Print a message indicating that the test passed
    print("test_dog_5027: Test passed - Data used to render @app.route('/dog_50272539') matched as expected.")

# Call the function with the name of the database file   
test_dog_5027('Furever.db')


# Function tests data used to render dog_51599202.html against data in Furever.db
def test_dog_515(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/dog_51599202' and store the response
    response = app.test_client().get('dog_51599202')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Dog table for data associated with id=51599202
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Dog WHERE id=51599202''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    # hard coded decsription with HTML character entity to represent '
    # ' renders correctly on webpage, but unable to compare to DB without hardcoding
    expected_description = "He gets along well with other most other dogs and most children, making him a great addition to your family. With his curious personality, he&#39;ll keep you entertained for hours! Chase is prone to mood swings, so we recommend an adopter with extensive dog experience."
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
    # Print a message indicating that the test passed
    print("test_dog_515: Test passed - Data used to render @app.route('/dog_51599202') matched as expected.")

# Call the function with the name of the database file   
test_dog_515('Furever.db')


# Function tests data used to render dog_51962699.html against data in Furever.db
def test_dog_519(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/dog_51962699' and store the response
    response = app.test_client().get('dog_51962699')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Dog table for data associated with id=51962699
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Dog WHERE id=51962699''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    # hard coded decsription with HTML character entity to represent '
    # ' renders correctly on webpage, but unable to compare to DB without hardcoding
    expected_description = "Very affectionate and loves attention. He looks so serious in his photos - but he is not! What we love most is that Debo is a young pup with a lot of energy and a lot of love to give. He is already learned Sit, Down and Touch. What he loves most: Debo loves to explore and sniff everything in sight. He hasn&#39;t really figured out fetch yet, but he&#39;s eager to learn new things and loves to please his humans. He also loves attention and cuddles, and he&#39;s always up for a good belly rub."
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
    # Print a message indicating that the test passed
    print("test_dog_519: Test passed - Data used to render @app.route('/dog_51962699') matched as expected.")

# Call the function with the name of the database file   
test_dog_519('Furever.db')


# Function tests data used to render dog_52006141.html against data in Furever.db
def test_dog_5200(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/dog_52006141' and store the response
    response = app.test_client().get('dog_52006141')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Dog table for data associated with id=52006141
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Dog WHERE id=52006141''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    # hard coded decsription with HTML character entity to represent '
    # ' renders correctly on webpage, but unable to compare to DB without hardcoding
    expected_description = "Ruby is looking for her forever home where she can feel safe and loved. She&#39;s an affectionate and loyal companion who just needs a little patience and love to help her come out of her shell. Come meet Ruby at the Seattle Animal Shelter and give her the chance to steal your heart!"
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
    # Print a message indicating that the test passed
    print("test_dog_5200: Test passed - Data used to render @app.route('/dog_52006141') matched as expected.")

# Call the function with the name of the database file   
test_dog_5200('Furever.db')


# Function tests data used to render dog_52053831.html against data in Furever.db
def test_dog_5205(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/dog_52053831' and store the response
    response = app.test_client().get('dog_52053831')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Dog table for data associated with id=52053831
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Dog WHERE id=52053831''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    # hard coded decsription with HTML character entity to represent '
    # ' renders correctly on webpage, but unable to compare to DB without hardcoding
    expected_description = "Hoss is a sweet-natured, easy-going lovebug. His favorite thing in the world is snuggling up with a human, and his second favorite is burrowing under a blanket. In his foster home, he has shown that he gets along well with cats and other small dogs. He&#39;ll snuggle with any critter that will let him! When he&#39;s not busy snuggling or burrowing, Hoss enjoys playing with squeaky toys and going for short walks. He loves car rides, but he&#39;s also happy to stay home while you&#39;re out stocking up on kibble. This affectionate little guy would love to meet you!"
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
    # Print a message indicating that the test passed
    print("test_dog_5205: Test passed - Data used to render @app.route('/dog_52053831') matched as expected.")

# Call the function with the name of the database file  
test_dog_5205('Furever.db')


# Function tests data used to render dog_52086329.html against data in Furever.db
def test_dog_5208(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/dog_52086329' and store the response
    response = app.test_client().get('dog_52086329')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Dog table for data associated with id=52086329
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Dog WHERE id=52086329''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    # hard coded decsription with HTML character entity to represent '
    # ' renders correctly on webpage, but unable to compare to DB without hardcoding
    expected_description = "Peter is a sweet boy who just needs the right home to thrive. He can be shy at first, but once he warms up to you, he&#39;s an absolute love bug. He&#39;s house-trained and knows basic commands, making him a joy to have around the house. He hasn&#39;t yet been crate trained."
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
    # Print a message indicating that the test passed
    print("test_dog_5208: Test passed - Data used to render @app.route('/dog_52086329') matched as expected.")

# Call the function with the name of the database file   
test_dog_5208('Furever.db')


# Function tests data used to render dog_50858047.html against data in Furever.db
def test_dog_5085(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/dog_50858047' and store the response
    response = app.test_client().get('dog_50858047')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Dog table for data associated with id=50858047
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Dog WHERE id=50858047''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    # hard coded decsription with HTML character entity to represent '
    # ' renders correctly on webpage, but unable to compare to DB without hardcoding
    expected_description = "Chewy is an active guy who loves to be outside regardless of the weather. He is a true PNW pup, he would spend all day playing in the rain if we let him! He is a busy guy looking for an equally busy home, with a routine he can learn, and plenty of outdoor adventuring. Chewy would do best in a home without younger children. His greatest wish is to go home with another dog who will run, chase, wrestle and tug with him all day. Chewy loves other dogs so much he doesn&#39;t mind sharing all of his toys, bowls, and people with them. He LOVES going for walks, and is making progress working on his leash behavior but will need a patient and persistent parent to continue his training so that everyone can love the walk as much as him!"
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
    # Print a message indicating that the test passed
    print("test_dog_5085: Test passed - Data used to render @app.route('/dog_50858047') matched as expected.")

# Call the function with the name of the database file   
test_dog_5085('Furever.db')


# Function tests data used to render dog_52129288.html against data in Furever.db
def test_dog_52129288(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/dog_52129288' and store the response
    response = app.test_client().get('dog_52129288')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Dog table for data associated with id=50858047
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Dog WHERE id=52129288''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    # hard coded decsription with HTML character entity to represent '
    # ' renders correctly on webpage, but unable to compare to DB without hardcoding
    expected_description = "Hello, my name is Cotton! I enjoy walks and playing with my sister Nova. I&#39;m a friendly dog that loves to hangout!"
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
    # Print a message indicating that the test passed
    print("test_dog_52129288: Test passed - Data used to render @app.route('/dog_52129288') matched as expected.")

# Call the function with the name of the database file  
test_dog_52129288('Furever.db')


# Function tests data used to render dog_52129291.html against data in Furever.db
def test_dog_52129291(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/dog_52129291' and store the response
    response = app.test_client().get('dog_52129291')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Dog table for data associated with id=52129291
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Dog WHERE id=52129291''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    # hard coded decsription with HTML character entity to represent '
    # ' renders correctly on webpage, but unable to compare to DB without hardcoding
    expected_description = "Hello, my name is Nova! I enjoy walks and playing with my brother Cotton. I&#39;m a friendly dog that loves to hangout!"
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
    # Print a message indicating that the test passed
    print("test_dog_52129291: Test passed - Data used to render @app.route('/dog_52129291') matched as expected.")

# Call the function with the name of the database file  
test_dog_52129291('Furever.db')


# Function tests data used to render dog_52091971.html against data in Furever.db
def test_dog_520919(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/dog_52091971' and store the response
    response = app.test_client().get('dog_52091971')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Dog table for data associated with id=52091971
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Dog WHERE id=52091971''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    expected_description = expected_data[1]
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
    # Print a message indicating that the test passed
    print("test_dog_520919: Test passed - Data used to render @app.route('/dog_52091971') matched as expected.")

# Call the function with the name of the database file   
test_dog_520919('Furever.db')

# ###############################################################################################
#              Cat Query Test - Test Data Rendered on Webpages Matches Database                                            
# ###############################################################################################

# Function tests data used to render cat_51289678.html against data in Furever.db
def test_cat_512(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/cat_51289678' and store the response
    response = app.test_client().get('cat_51289678')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Cat table for data associated with id=51289678
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Cat WHERE id=51289678''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    # hard coded decsription with HTML character entity to represent '
    # ' renders correctly on webpage, but unable to compare to DB without hardcoding
    expected_description = "Mocha is an intelligent cat who, after getting over her initial shyness, is friendly and social. Although she doesn&#39;t care for full body pets or being picked up, she loves head and ear scritches and will hang out next to you on the couch. She also enjoys playing, looking out the window, and finding high perches where she can survey the room and take a nap. She&#39;s a graceful girl who doesn&#39;t break things, and she&#39;s a pro with her scratching pad. Mocha is looking for a home with no other cats and mature guardians who can read cat body language and respect her boundaries. In return you will be getting a sweet, lovely companion."
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
    # Print a message indicating that the test passed
    print("test_cat_512: Test passed - Data used to render @app.route('/cat_51289678') matched as expected.")

# Call the function with the name of the database file   
test_cat_512('Furever.db')


# Function tests data used to render cat_52058185.html against data in Furever.db
def test_cat_520(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/cat_52058185' and store the response
    response = app.test_client().get('cat_52058185')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Cat table for data associated with id=52058185
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Cat WHERE id=52058185''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    # hard coded decsription with HTML character entity to represent '
    # ' renders correctly on webpage, but unable to compare to DB without hardcoding
    expected_description = "Like peanut butter and jelly, cups and saucers, Kermit and Miss Piggy, some things are meant to be together. And that&#39;s especially true for Peppi and Stanley. This adorable mom and son pair were brought to SAS together, and were briefly separated, but when staff saw how much they missed each other, they were reunited at their foster parent&#39;s home. Peppi didn&#39;t eat while they were apart. When Stanley saw Peppi again, he mewed happily for the first time! They were so happy to be back together. Now they sleep together like magnets and Stanley follows his mom devotedly wherever she goes."
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
    # Print a message indicating that the test passed
    print("test_cat_520: Test passed - Data used to render @app.route('/cat_52058185') matched as expected.")

# Call the function with the name of the database file    
test_cat_520('Furever.db')


# Function tests data used to render cat_52072231.html against data in Furever.db
def test_cat_5207(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/cat_52072231' and store the response
    response = app.test_client().get('cat_52072231')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Cat table for data associated with id=52072231
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Cat WHERE id=52072231''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    # hard coded decsription with HTML character entity to represent '
    # ' renders correctly on webpage, but unable to compare to DB without hardcoding
    expected_description = "Like peanut butter and jelly, cups and saucers, Kermit and Miss Piggy, some things are meant to be together. And that&#39;s especially true for Peppi and Stanley. This adorable mom and son pair were brought to SAS together, and were briefly separated, but when staff saw how much they missed each other, they were reunited at their foster parent&#39;s home. Peppi didn&#39;t eat while they were apart. When Stanley saw Peppi again, he mewed happily for the first time! They were so happy to be back together. Now they sleep together like magnets and Stanley follows his mom devotedly wherever she goes."
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
    # Print a message indicating that the test passed
    print("test_cat_5207: Test passed - Data used to render @app.route('/cat_52072231') matched as expected.")

# Call the function with the name of the database file    
test_cat_5207('Furever.db')


# Function tests data used to render cat_52106194.html against data in Furever.db
def test_cat_521(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/cat_52106194' and store the response
    response = app.test_client().get('cat_52106194')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Cat table for data associated with id=52106194
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Cat WHERE id=52106194''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    # hard coded decsription with HTML character entity to represent '
    # ' renders correctly on webpage, but unable to compare to DB without hardcoding
    expected_description = "Hi! I&#39;m a sweet, timid kitty who loves head scratches and Churu treats! Once I feel comfortable with you, I&#39;m inquisitive and playful. Toys with strings and feathers are my favorite. I also enjoy snuggling in blankets, giving head bumps and bird watching. I have very polite litter box manners. When I&#39;m not curled up next to you, I&#39;ll be napping nearby because I like the company."
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
    # Print a message indicating that the test passed
    print("test_cat_521: Test passed - Data used to render @app.route('/cat_52106194') matched as expected.")

# Call the function with the name of the database file    
test_cat_521('Furever.db')


# Function tests data used to render cat_52167059.html against data in Furever.db
def test_cat_5216(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/cat_52167059' and store the response
    response = app.test_client().get('cat_52167059')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Cat table for data associated with id=52167059
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Cat WHERE id=52167059''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    expected_description = expected_data[1]
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
    # Print a message indicating that the test passed

    print("test_cat_5216: Test passed - Data used to render @app.route('/cat_52167059') matched as expected.")

# Call the function with the name of the database file     
test_cat_5216('Furever.db')

###############################################################################################
#             Dog Query Test - Test Data Rendered on Dog Page When Filtered                                         
###############################################################################################
# Unittesting below test that the get_filtered_petIDs() is pulling the correct data from the Database
# The get_filtered_petIDs() is a helper function that pulls data from the database everytime a user filters
# breed, age, gender, color, and size on the Dog page
# Users are not able to make invalid filtering requests as only valid options are available on the webpage
# Thus, our testing will test the following scenarios:
#        1. various valid filter options
#        2. if no filter options are selected by user
#        3. if user filters for options that do not fit any dog in the database

class TestGetFilteredPetIDs(unittest.TestCase):
    # Function to test filter options avaiable on the Dog page('/dogs'). Set returned will include pet ids.
    def test_valid_input1(self):
        # Connect to the database
        conn = sqlite3.connect('Furever.db')
        c = conn.cursor()

        # Define filter criteria SQL query
        petType = 'Dog'
        breed = 'Any'
        age = 'Any'
        gender = 'Female'
        color = 'Any'
        size = 'Any'

        # Create a SQL query to retrieve the pet IDs that match the filter criteria
        # Start with a basic query to select all pets of the specified gender
        # Initialize the parameters tuple with the gender filter
        query = "SELECT id FROM Dog WHERE gender=?" 
        params = (gender,) 

        # If filters were specified, add them to the query
        # Add the filters to the parameters tuple
        if breed != 'Any':
            query += " AND breed=?" 
            params += (breed,)  
        if age != 'Any':
            query += " AND age=?" 
            params += (age,)  
        if color != 'Any':
            query += " AND color=?"  
            params += (color,) 
        if size != 'Any':
            query += " AND size=?" 
            params += (size,)  

        # Execute the SQL query and store the results in a set
        c.execute(query, params)
        sql_output = c.fetchall()
        expected_output = set([x[0] for x in sql_output])
        #print(f"test_valid_input1 - expected output: {expected_output}")

        # Use a test request context to simulate a GET request to the website with the filter criteria as URL parameters
        with app.test_request_context('/?petType={}&breed={}&age={}&size={}&gender={}&color={}'.format(
                petType, breed, age, size, gender, color)):
            # Call the get_filtered_petIDs function with the filter criteria and store the result in a variable
            result = get_filtered_petIDs(petType, breed, age, size, gender, color)
            #print(f"test_valid_input1 - result from get_filtered_petIDs: {result}")

            # Check that the result matches the expected output
            self.assertEqual(result, expected_output, "test_valid_input1: Test passed - Data rendered on webpage matches database as expected")

        # Close the database connection
        conn.close()
        
        
    # Function to test filter options avaiable on the Dog page('/dogs'). Set returned will include pet ids.
    def test_valid_input2(self):
        # Connect to the database
        conn = sqlite3.connect('Furever.db')
        c = conn.cursor()
        
        # Define filter criteria
        petType = 'Dog'
        breed = 'Any'
        age = 'Any'
        gender = 'Male'
        color = 'Any'
        size = 'Any'
        
        # Create a SQL query to retrieve the pet IDs that match the filter criteria
        # Start with a basic query to select all pets of the specified gender
        # Initialize the parameters tuple with the gender filter
        query = "SELECT id FROM Dog WHERE gender=?" 
        params = (gender,) 
        
        # If filters were specified, add them to the query
        # Add the filters to the parameters tuple
        if breed != 'Any':
            query += " AND breed=?" 
            params += (breed,)  
        if age != 'Any':
            query += " AND age=?" 
            params += (age,)  
        if color != 'Any':
            query += " AND color=?"  
            params += (color,) 
        if size != 'Any':
            query += " AND size=?" 
            params += (size,)  
        
        # Execute the SQL query and store the results in a set
        c.execute(query, params)
        sql_output = c.fetchall()
        expected_output = set([x[0] for x in sql_output])
        #print(f"test_valid_input2 - expected output: {expected_output}")
        
        # Use a test request context to simulate a GET request to the website with the filter criteria as URL parameters
        with app.test_request_context('/?petType={}&breed={}&age={}&size={}&gender={}&color={}'.format(
                petType, breed, age, size, gender, color)):
            # Call the get_filtered_petIDs function with the filter criteria and store the result in a variable
            result = get_filtered_petIDs(petType, breed, age, size, gender, color)
            #print(f"test_valid_input2 - result from get_filtered_petIDs: {result}")
            
            # Check that the result matches the expected output
            self.assertEqual(result, expected_output, "test_valid_input2: Test passed - Data rendered on webpage matches database as expected")
        
        # Close the database connection
        conn.close()     
        
        
    # Function to test filter options avaiable on the Dog page('/dogs'). Set returned will include pet ids.
    def test_valid_input3(self):
        # Connect to the database
        conn = sqlite3.connect('Furever.db')
        c = conn.cursor()
        
        # Define filter criteria
        petType = 'Dog'
        breed = 'Any'
        age = 'Any'
        gender = 'Male'
        color = 'Mixed'
        size = 'Any'
        
        # Create a SQL query to retrieve the pet IDs that match the filter criteria
        # Start with a basic query to select all pets of the specified gender
        # Initialize the parameters tuple with the gender filter
        query = "SELECT id FROM Dog WHERE gender=?" 
        params = (gender,) 
        
        # If filters were specified, add them to the query
        # Add the filters to the parameters tuple
        if breed != 'Any':
            query += " AND breed=?" 
            params += (breed,)  
        if age != 'Any':
            query += " AND age=?" 
            params += (age,)  
        if color != 'Any':
            query += " AND color=?"  
            params += (color,) 
        if size != 'Any':
            query += " AND size=?" 
            params += (size,)  
        
        # Execute the SQL query and store the results in a set
        c.execute(query, params)
        sql_output = c.fetchall()
        expected_output = set([x[0] for x in sql_output])
        #print(f"test_valid_input3 - expected output: {expected_output}")
        
        # Use a test request context to simulate a GET request to the website with the filter criteria as URL parameters
        with app.test_request_context('/?petType={}&breed={}&age={}&size={}&gender={}&color={}'.format(
                petType, breed, age, size, gender, color)):
            # Call the get_filtered_petIDs function with the filter criteria and store the result in a variable
            result = get_filtered_petIDs(petType, breed, age, size, gender, color)
            #print(f"test_valid_input3 - result from get_filtered_petIDs: {result}")
            
            # Check that the result matches the expected output
            self.assertEqual(result, expected_output, "test_valid_input3: Test passed - Data rendered on webpage matches database as expected")
        
        # Close the database connection
        conn.close()  
        
        
    # Function to test filter options avaiable on the Dog page('/dogs'). Set returned will include pet ids.   
    def test_valid_input4(self):
        # Connect to the database
        conn = sqlite3.connect('Furever.db')
        c = conn.cursor()
        
        # Define filter criteria
        petType = 'Dog'
        breed = 'Any'
        age = 'Any' # wild card (since data type is float, we can't * as the wild card)
        gender = 'Female'
        color = 'Any'
        size = 'Large'
        
        # Create a SQL query to retrieve the pet IDs that match the filter criteria
        # Start with a basic query to select all pets of the specified gender
        # Initialize the parameters tuple with the gender filter
        query = "SELECT id FROM Dog WHERE gender=?" 
        params = (gender,) 
        
        # If filters were specified, add them to the query
        # Add the filters to the parameters tuple
        if breed != 'Any':
            query += " AND breed=?" 
            params += (breed,)  
        if age != 'Any':
            query += " AND age=?" 
            params += (age,)  
        if color != 'Any':
            query += " AND color=?"  
            params += (color,) 
        if size != 'Any':
            query += " AND size=?" 
            params += (size,)  
        
        # Execute the SQL query and store the results in a set
        c.execute(query, params)
        sql_output = c.fetchall()
        expected_output = set([x[0] for x in sql_output])
        #print(f"test_valid_input4 - expected output: {expected_output}")
        
        # Use a test request context to simulate a GET request to the website with the filter criteria as URL parameters
        with app.test_request_context('/?petType={}&breed={}&age={}&size={}&gender={}&color={}'.format(
                petType, breed, age, size, gender, color)):
            # Call the get_filtered_petIDs function with the filter criteria and store the result in a variable
            result = get_filtered_petIDs(petType, breed, age, size, gender, color)
            #print(f"test_valid_input4 - result from get_filtered_petIDs: {result}")
            
            # Check that the result matches the expected output
            self.assertEqual(result, expected_output, "test_valid_input4: Test passed - Data rendered on webpage matches database as expected")
        
        # Close the database connection
        conn.close() 
        
        
    # Function to test filter options avaiable on the Dog page('/dogs'). Set returned will include pet ids.    
    def test_valid_input5(self):
        # Connect to the database
        conn = sqlite3.connect('Furever.db')
        c = conn.cursor()
        
        # Define filter criteria
        petType = 'Dog'
        breed = 'Any'
        age = 'Any' # wild card (since data type is float, we can't * as the wild card)
        gender = 'Any'
        color = 'Mixed'
        size = 'Large'
        
        # Create a SQL query to retrieve the pet IDs that match the filter criteria
        # Start with a basic query to select all pets of the specified color
        # Initialize the parameters tuple with the color filter
        query = "SELECT id FROM Dog WHERE color=?" 
        params = (color,) 
        
        # If filters were specified, add them to the query
        # Add the filters to the parameters tuple
        if breed != 'Any':
            query += " AND breed=?" 
            params += (breed,)  
        if age != 'Any':
            query += " AND age=?" 
            params += (age,)  
        if gender != 'Any':
            query += " AND gender=?"  
            params += (gender,) 
        if size != 'Any':
            query += " AND size=?" 
            params += (size,)  
        
        # Execute the SQL query and store the results in a set
        c.execute(query, params)
        sql_output = c.fetchall()
        expected_output = set([x[0] for x in sql_output])
        #print(f"test_valid_input5 - expected output: {expected_output}")
        
        # Use a test request context to simulate a GET request to the website with the filter criteria as URL parameters
        with app.test_request_context('/?petType={}&breed={}&age={}&size={}&gender={}&color={}'.format(
                petType, breed, age, size, gender, color)):
            # Call the get_filtered_petIDs function with the filter criteria and store the result in a variable
            result = get_filtered_petIDs(petType, breed, age, size, gender, color)
            #print(f"test_valid_input5 - result from get_filtered_petIDs: {result}")
            
            # Check that the result matches the expected output
            self.assertEqual(result, expected_output, "test_valid_input5: Test passed - Data rendered on webpage matches database as expected")
        
        # Close the database connection
        conn.close() 

        
    # Function to test filter options avaiable on the Dog page('/dogs'). Set returned will include pet ids.   
    def test_valid_input6(self):
        # Connect to the database
        conn = sqlite3.connect('Furever.db')
        c = conn.cursor()
        
        # Define filter criteria
        petType = 'Dog'
        breed = 'Any'
        age = '1-5' # get_filtered_petIDs uses an exclusive min and inclusive so we are really testing ages 2, 3, 4, & 5
        gender = 'Any'
        color = 'Any'
        size = 'Any'
        
        # Split the age range into minimum and maximum age values
        min_age, max_age = age.split('-')

        # Create a SQL query to retrieve the pet IDs that match the filter criteria
        # Start with a basic query to select all pets within the specified age range
        # Initialize the parameters tuple with the minimum and maximum age filters
        query = "SELECT id FROM Dog WHERE age > ? AND age <= ?" 
        params = (min_age, max_age) 

        # If filters were specified, add them to the query
        # Add the filters to the parameters tuple
        if breed != 'Any':
            query += " AND breed=?" 
            params += (breed,)  
        if color != 'Any':
            query += " AND color=?" 
            params += (color,)  
        if gender != 'Any':
            query += " AND gender=?"  
            params += (gender,) 
        if size != 'Any':
            query += " AND size=?" 
            params += (size,) 
        
        # Execute the SQL query and store the results in a set
        c.execute(query, params)
        sql_output = c.fetchall()
        expected_output = set([x[0] for x in sql_output])
        #print(f"test_valid_input6 - expected output: {expected_output}")
        
        # Use a test request context to simulate a GET request to the website with the filter criteria as URL parameters
        with app.test_request_context('/?petType={}&breed={}&age={}&size={}&gender={}&color={}'.format(
                petType, breed, age, size, gender, color)):
            # Call the get_filtered_petIDs function with the filter criteria and store the result in a variable
            result = get_filtered_petIDs(petType, breed, age, size, gender, color)
            #print(f"test_valid_input6 - result from get_filtered_petIDs: {result}")
            
            # Check that the result matches the expected output
            self.assertEqual(result, expected_output, "test_valid_input6: Test passed - Data rendered on webpage matches database as expected")
        
        # Close the database connection
        conn.close() 
        
        
    # Function to test filter options avaiable on the Dog page('/dogs'). Set returned will include pet ids.
    def test_valid_input7(self):
        # Connect to the database
        conn = sqlite3.connect('Furever.db')
        c = conn.cursor()
        
        # Define filter criteria
        petType = 'Dog'
        breed = 'Pinscher'
        age = 'Any' # wild card (since data type is float, we can't * as the wild card)
        gender = 'Any'
        color = 'Any'
        size = 'Any'
        
        # Create a SQL query to retrieve the pet IDs that match the filter criteria
        # Start with a basic query to select all pets of the specified breed
        # Initialize the parameters tuple with the breed filter
        query = "SELECT id FROM Dog WHERE breed=?" 
        params = (breed,) 
        
        # If filters were specified, add them to the query
        # Add the filters to the parameters tuple
        if age != 'Any':
            query += " AND age=?" 
            params += (age,)  
        if color != 'Any':
            query += " AND color=?" 
            params += (color,)  
        if gender != 'Any':
            query += " AND gender=?"  
            params += (gender,) 
        if size != 'Any':
            query += " AND size=?" 
            params += (size,)  
        
        # Execute the SQL query and store the results in a set
        c.execute(query, params)
        sql_output = c.fetchall()
        expected_output = set([x[0] for x in sql_output])
        #print(f"test_valid_input7 - expected output: {expected_output}")
        
        # Use a test request context to simulate a GET request to the website with the filter criteria as URL parameters
        with app.test_request_context('/?petType={}&breed={}&age={}&size={}&gender={}&color={}'.format(
                petType, breed, age, size, gender, color)):
            # Call the get_filtered_petIDs function with the filter criteria and store the result in a variable
            result = get_filtered_petIDs(petType, breed, age, size, gender, color)
            #print(f"test_valid_input7 - result from get_filtered_petIDs: {result}")
            
            # Check that the result matches the expected output
            self.assertEqual(result, expected_output, "test_valid_input7: Test passed - Data rendered on webpage matches database as expected")
        
        # Close the database connection
        conn.close() 
        
        
    # Function to test that all available dogs are returned when no filters (Any) are chosen on Dog page('/dogs')
    def test_no_filters_selected1(self):
        # Connect to the database
        conn = sqlite3.connect('Furever.db')
        c = conn.cursor()
        
        # Define filter criteria
        petType = 'Dog'
        breed = 'Any'
        age = 'Any' # wild card (since data type is float, we can't * as the wild card)
        gender = 'Any'
        color = 'Any'
        size = 'Any'
        
        # Create a SQL query to retrieve all the pet IDs in the database
        query = "SELECT id FROM Dog" 
        
        # Execute the SQL query and store the results in a set
        c.execute(query)
        sql_output = c.fetchall()
        expected_output = set([x[0] for x in sql_output])
        #print(f"test_no_filters_selected1 - expected output: {expected_output}")
        
        # Use a test request context to simulate a GET request to the website with no filter criteria
        with app.test_request_context('/?petType={}&breed={}&age={}&size={}&gender={}&color={}'.format(
                petType, breed, age, size, gender, color)):
            # Call the get_filtered_petIDs function with the filter criteria and store the result in a variable
            result = get_filtered_petIDs(petType, breed, age, size, gender, color)
            #print(f"test_no_filters_selected1 - result from get_filtered_petIDs: {result}")
            
            # Check that the result matches the expected output
            self.assertEqual(result, expected_output, "test_no_filters_selected1: Test passed - Data rendered on webpage matches database as expected")
        
        # Close the database connection
        conn.close() 
        
        
    # Function to test filter options avaiable on the Dog page('/dogs'). Set returned should be empty as no pets fit the criteria.    
    def test_valid_input_that_returns_empty_set_of_Ids1(self):
        # Connect to the database
        conn = sqlite3.connect('Furever.db')
        c = conn.cursor()
        
        # Define filter criteria
        petType = 'Dog'
        breed = 'Shepherd/Mixed'
        age = 'Any'
        gender = 'Female'
        color = 'Any'
        size = 'Any'
        
        # Create a SQL query to retrieve the pet IDs that match the filter criteria
        # Start with a basic query to select all pets of the specified breed
        # Initialize the parameters tuple with the breed filter
        query = "SELECT id FROM Dog WHERE breed=?" 
        params = (breed,) 
        
        # If filters were specified, add them to the query
        # Add the filters to the parameters tuple
        if age != 'Any':
            query += " AND age=?" 
            params += (age,)  
        if color != 'Any':
            query += " AND color=?" 
            params += (color,)  
        if gender != 'Any':
            query += " AND gender=?"  
            params += (gender,) 
        if size != 'Any':
            query += " AND size=?" 
            params += (size,)  
        
        # Execute the SQL query and store the results in a set
        c.execute(query, params)
        sql_output = c.fetchall()
        expected_output = set([x[0] for x in sql_output])
        #print(f"test_valid_input_that_returns_empty_set_of_Ids1 - expected output: {expected_output}")
        
        # Use a test request context to simulate a GET request to the website with the filter criteria as URL parameters
        with app.test_request_context('/?petType={}&breed={}&age={}&size={}&gender={}&color={}'.format(
                petType, breed, age, size, gender, color)):
            # Call the get_filtered_petIDs function with the filter criteria and store the result in a variable
            result = get_filtered_petIDs(petType, breed, age, size, gender, color)
            #print(f"test_valid_input_that_returns_empty_set_of_Ids1 - result from get_filtered_petIDs: {result}")
            
            # Check that the result matches the expected output
            self.assertEqual(result, expected_output, "test_valid_input_that_returns_empty_set_of_Ids1: Test passed - Data rendered on webpage matches database as expected")
        
        # Close the database connection
        conn.close()  
        
        
    # Function to test filter options avaiable on the Dog page('/dogs'). Set returned should be empty as no pets fit the criteria.     
    def test_valid_input_that_returns_empty_set_of_Ids2(self):
        # Connect to the database
        conn = sqlite3.connect('Furever.db')
        c = conn.cursor()
        
        # Define filter criteria
        petType = 'Dog'
        breed = 'Any'
        age = 'Any'
        gender = 'Female'
        color = 'Mixed'
        size = 'Large'
        
        # Create a SQL query to retrieve the pet IDs that match the filter criteria
        # Start with a basic query to select all pets of the specified gender
        # Initialize the parameters tuple with the gender filter
        query = "SELECT id FROM Dog WHERE gender=?" 
        params = (gender,) 
        
        # If filters were specified, add them to the query
        # Add the filters to the parameters tuple
        if age != 'Any':
            query += " AND age=?" 
            params += (age,)  
        if color != 'Any':
            query += " AND color=?" 
            params += (color,)  
        if breed != 'Any':
            query += " AND breed=?"  
            params += (breed,) 
        if size != 'Any':
            query += " AND size=?" 
            params += (size,)  
        
        # Execute the SQL query and store the results in a set
        c.execute(query, params)
        sql_output = c.fetchall()
        expected_output = set([x[0] for x in sql_output])
        #print(f"test_valid_input_that_returns_empty_set_of_Ids2 - expected output: {expected_output}")
        
        # Use a test request context to simulate a GET request to the website with the filter criteria as URL parameters
        with app.test_request_context('/?petType={}&breed={}&age={}&size={}&gender={}&color={}'.format(
                petType, breed, age, size, gender, color)):
            # Call the get_filtered_petIDs function with the filter criteria and store the result in a variable
            result = get_filtered_petIDs(petType, breed, age, size, gender, color)
            #print(f"test_valid_input_that_returns_empty_set_of_Ids2 - result from get_filtered_petIDs: {result}")
            
            # Check that the result matches the expected output
            self.assertEqual(result, expected_output, "test_valid_input_that_returns_empty_set_of_Ids2")

            
###############################################################################################
#             Cat Query Test - Test Data Rendered on Cat Page When Filtered                                         
###############################################################################################
# Unittesting below test that the get_filtered_petIDs() is pulling the correct data from the Database
# The get_filtered_petIDs() is a helper function that pulls data from the database everytime a user filters
# breed, age, gender, color, and size on the Cat page
# Users are not able to make invalid filtering requests as only valid options are available on the webpage
# Thus, our testing will test the following scenarios:
#        1. various valid filter options
#        2. if no filter options are selected by user
#        3. if user filters for options that do not fit any cat in the database

    # Function to test filter options avaiable on the Cat page('/cats'). Set returned will include pet ids.
    def test_valid_input8(self):
        # Connect to the database
        conn = sqlite3.connect('Furever.db')
        c = conn.cursor()

        # Define filter criteria SQL query
        petType = 'Cat'
        breed = 'Any'
        age = 'Any'
        gender = 'Female'
        color = 'Any'
        size = 'Any'

        # Create a SQL query to retrieve the pet IDs that match the filter criteria
        # Start with a basic query to select all pets of the specified gender
        # Initialize the parameters tuple with the gender filter
        query = "SELECT id FROM Cat WHERE gender=?" 
        params = (gender,) 

        # If filters were specified, add them to the query
        # Add the filters to the parameters tuple
        if breed != 'Any':
            query += " AND breed=?" 
            params += (breed,)  
        if age != 'Any':
            query += " AND age=?" 
            params += (age,)  
        if color != 'Any':
            query += " AND color=?"  
            params += (color,) 
        if size != 'Any':
            query += " AND size=?" 
            params += (size,)  

        # Execute the SQL query and store the results in a set
        c.execute(query, params)
        sql_output = c.fetchall()
        expected_output = set([x[0] for x in sql_output])
        #print(f"test_valid_input8 - expected output: {expected_output}")

        # Use a test request context to simulate a GET request to the website with the filter criteria as URL parameters
        with app.test_request_context('/?petType={}&breed={}&age={}&size={}&gender={}&color={}'.format(
                petType, breed, age, size, gender, color)):
            # Call the get_filtered_petIDs function with the filter criteria and store the result in a variable
            result = get_filtered_petIDs(petType, breed, age, size, gender, color)
            #print(f"test_valid_input8 - result from get_filtered_petIDs: {result}")

            # Check that the result matches the expected output
            self.assertEqual(result, expected_output, "test_valid_input8: Test passed - Data rendered on webpage matches database as expected")

        # Close the database connection
        conn.close()
        
        
    # Function to test filter options avaiable on the Cat page('/cats'). Set returned will include pet ids.
    def test_valid_input9(self):
        # Connect to the database
        conn = sqlite3.connect('Furever.db')
        c = conn.cursor()
        
        # Define filter criteria
        petType = 'Cat'
        breed = 'Any'
        age = 'Any'
        gender = 'Male'
        color = 'Any'
        size = 'Any'
        
        # Create a SQL query to retrieve the pet IDs that match the filter criteria
        # Start with a basic query to select all pets of the specified gender
        # Initialize the parameters tuple with the gender filter
        query = "SELECT id FROM Cat WHERE gender=?" 
        params = (gender,) 
        
        # If filters were specified, add them to the query
        # Add the filters to the parameters tuple
        if breed != 'Any':
            query += " AND breed=?" 
            params += (breed,)  
        if age != 'Any':
            query += " AND age=?" 
            params += (age,)  
        if color != 'Any':
            query += " AND color=?"  
            params += (color,) 
        if size != 'Any':
            query += " AND size=?" 
            params += (size,)  
        
        # Execute the SQL query and store the results in a set
        c.execute(query, params)
        sql_output = c.fetchall()
        expected_output = set([x[0] for x in sql_output])
        #print(f"test_valid_input9 - expected output: {expected_output}")
        
        # Use a test request context to simulate a GET request to the website with the filter criteria as URL parameters
        with app.test_request_context('/?petType={}&breed={}&age={}&size={}&gender={}&color={}'.format(
                petType, breed, age, size, gender, color)):
            # Call the get_filtered_petIDs function with the filter criteria and store the result in a variable
            result = get_filtered_petIDs(petType, breed, age, size, gender, color)
            #print(f"test_valid_input9 - result from get_filtered_petIDs: {result}")
            
            # Check that the result matches the expected output
            self.assertEqual(result, expected_output, "test_valid_input9: Test passed - Data rendered on webpage matches database as expected")
        
        # Close the database connection
        conn.close()     
        
        
    # Function to test filter options avaiable on the Cat page('/cats'). Set returned will include pet ids.
    def test_valid_input10(self):
        # Connect to the database
        conn = sqlite3.connect('Furever.db')
        c = conn.cursor()
        
        # Define filter criteria
        petType = 'Cat'
        breed = 'Any'
        age = 'Any'
        gender = 'Female'
        color = 'Mixed'
        size = 'Any'
        
        # Create a SQL query to retrieve the pet IDs that match the filter criteria
        # Start with a basic query to select all pets of the specified gender
        # Initialize the parameters tuple with the gender filter
        query = "SELECT id FROM Cat WHERE gender=?" 
        params = (gender,) 
        
        # If filters were specified, add them to the query
        # Add the filters to the parameters tuple
        if breed != 'Any':
            query += " AND breed=?" 
            params += (breed,)  
        if age != 'Any':
            query += " AND age=?" 
            params += (age,)  
        if color != 'Any':
            query += " AND color=?"  
            params += (color,) 
        if size != 'Any':
            query += " AND size=?" 
            params += (size,)  
        
        # Execute the SQL query and store the results in a set
        c.execute(query, params)
        sql_output = c.fetchall()
        expected_output = set([x[0] for x in sql_output])
        #print(f"test_valid_input10 - expected output: {expected_output}")
        
        # Use a test request context to simulate a GET request to the website with the filter criteria as URL parameters
        with app.test_request_context('/?petType={}&breed={}&age={}&size={}&gender={}&color={}'.format(
                petType, breed, age, size, gender, color)):
            # Call the get_filtered_petIDs function with the filter criteria and store the result in a variable
            result = get_filtered_petIDs(petType, breed, age, size, gender, color)
            #print(f"test_valid_input10 - result from get_filtered_petIDs: {result}")
            
            # Check that the result matches the expected output
            self.assertEqual(result, expected_output, "test_valid_input10: Test passed - Data rendered on webpage matches database as expected")
        
        # Close the database connection
        conn.close()  
        
        
    # Function to test filter options avaiable on the Cat page('/cats'). Set returned will include pet ids. 
    def test_valid_input11(self):
        # Connect to the database
        conn = sqlite3.connect('Furever.db')
        c = conn.cursor()
        
        # Define filter criteria
        petType = 'Cat'
        breed = 'Any'
        age = 'Any' # wild card (since data type is float, we can't * as the wild card)
        gender = 'Female'
        color = 'Any'
        size = 'Medium'
        
        # Create a SQL query to retrieve the pet IDs that match the filter criteria
        # Start with a basic query to select all pets of the specified gender
        # Initialize the parameters tuple with the gender filter
        query = "SELECT id FROM Cat WHERE gender=?" 
        params = (gender,) 
        
        # If filters were specified, add them to the query
        # Add the filters to the parameters tuple
        if breed != 'Any':
            query += " AND breed=?" 
            params += (breed,)  
        if age != 'Any':
            query += " AND age=?" 
            params += (age,)  
        if color != 'Any':
            query += " AND color=?"  
            params += (color,) 
        if size != 'Any':
            query += " AND size=?" 
            params += (size,)  
        
        # Execute the SQL query and store the results in a set
        c.execute(query, params)
        sql_output = c.fetchall()
        expected_output = set([x[0] for x in sql_output])
        #print(f"test_valid_input11 - expected output: {expected_output}")
        
        # Use a test request context to simulate a GET request to the website with the filter criteria as URL parameters
        with app.test_request_context('/?petType={}&breed={}&age={}&size={}&gender={}&color={}'.format(
                petType, breed, age, size, gender, color)):
            # Call the get_filtered_petIDs function with the filter criteria and store the result in a variable
            result = get_filtered_petIDs(petType, breed, age, size, gender, color)
            #print(f"test_valid_input11 - result from get_filtered_petIDs: {result}")
            
            # Check that the result matches the expected output
            self.assertEqual(result, expected_output, "test_valid_input11: Test passed - Data rendered on webpage matches database as expected")
        
        # Close the database connection
        conn.close() 
        
        
    # Function to test filter options avaiable on the Cat page('/cats'). Set returned will include pet ids. 
    def test_valid_input12(self):
        # Connect to the database
        conn = sqlite3.connect('Furever.db')
        c = conn.cursor()
        
        # Define filter criteria
        petType = 'Cat'
        breed = 'Any'
        age = 'Any' # wild card (since data type is float, we can't * as the wild card)
        gender = 'Any'
        color = 'Mixed'
        size = 'Small'
        
        # Create a SQL query to retrieve the pet IDs that match the filter criteria
        # Start with a basic query to select all pets of the specified color
        # Initialize the parameters tuple with the color filter
        query = "SELECT id FROM Cat WHERE color=?" 
        params = (color,) 
        
        # If filters were specified, add them to the query
        # Add the filters to the parameters tuple
        if breed != 'Any':
            query += " AND breed=?" 
            params += (breed,)  
        if age != 'Any':
            query += " AND age=?" 
            params += (age,)  
        if gender != 'Any':
            query += " AND gender=?"  
            params += (gender,) 
        if size != 'Any':
            query += " AND size=?" 
            params += (size,)  
        
        # Execute the SQL query and store the results in a set
        c.execute(query, params)
        sql_output = c.fetchall()
        expected_output = set([x[0] for x in sql_output])
        #print(f"test_valid_input12 - expected output: {expected_output}")
        
        # Use a test request context to simulate a GET request to the website with the filter criteria as URL parameters
        with app.test_request_context('/?petType={}&breed={}&age={}&size={}&gender={}&color={}'.format(
                petType, breed, age, size, gender, color)):
            # Call the get_filtered_petIDs function with the filter criteria and store the result in a variable
            result = get_filtered_petIDs(petType, breed, age, size, gender, color)
            #print(f"test_valid_input12 - result from get_filtered_petIDs: {result}")
            
            # Check that the result matches the expected output
            self.assertEqual(result, expected_output, "test_valid_input12: Test passed - Data rendered on webpage matches database as expected")
        
        # Close the database connection
        conn.close() 

        
    # Function to test filter options avaiable on the Cat page('/cats'). Set returned will include pet ids.   
    def test_valid_input13(self):
        # Connect to the database
        conn = sqlite3.connect('Furever.db')
        c = conn.cursor()
        
        # Define filter criteria
        petType = 'Cat'
        breed = 'Any'
        age = '1-3' # get_filtered_petIDs uses an exclusive min and inclusive so we are really testing ages 2 & 3
        gender = 'Any'
        color = 'Any'
        size = 'Any'
        
        # Split the age range into minimum and maximum age values
        min_age, max_age = age.split('-')

        # Create a SQL query to retrieve the pet IDs that match the filter criteria
        # Start with a basic query to select all pets within the specified age range
        # Initialize the parameters tuple with the minimum and maximum age filters
        query = "SELECT id FROM Cat WHERE age > ? AND age <= ?" 
        params = (min_age, max_age) 

        # If filters were specified, add them to the query
        # Add the filters to the parameters tuple
        if breed != 'Any':
            query += " AND breed=?" 
            params += (breed,)  
        if color != 'Any':
            query += " AND color=?" 
            params += (color,)  
        if gender != 'Any':
            query += " AND gender=?"  
            params += (gender,) 
        if size != 'Any':
            query += " AND size=?" 
            params += (size,) 
        
        # Execute the SQL query and store the results in a set
        c.execute(query, params)
        sql_output = c.fetchall()
        expected_output = set([x[0] for x in sql_output])
        #print(f"test_valid_input13 - expected output: {expected_output}")
        
        # Use a test request context to simulate a GET request to the website with the filter criteria as URL parameters
        with app.test_request_context('/?petType={}&breed={}&age={}&size={}&gender={}&color={}'.format(
                petType, breed, age, size, gender, color)):
            # Call the get_filtered_petIDs function with the filter criteria and store the result in a variable
            result = get_filtered_petIDs(petType, breed, age, size, gender, color)
            #print(f"test_valid_input13 - result from get_filtered_petIDs: {result}")
            
            # Check that the result matches the expected output
            self.assertEqual(result, expected_output, "test_valid_input13: Test passed - Data rendered on webpage matches database as expected")
        
        # Close the database connection
        conn.close() 
        
        
    # Function to test filter options avaiable on the Cat page('/cats'). Set returned will include pet ids.
    def test_valid_input14(self):
        # Connect to the database
        conn = sqlite3.connect('Furever.db')
        c = conn.cursor()
        
        # Define filter criteria
        petType = 'Cat'
        breed = 'Domestic Shorthair/Mix'
        age = 'Any' # wild card (since data type is float, we can't * as the wild card)
        gender = 'Any'
        color = 'Any'
        size = 'Any'
        
        # Create a SQL query to retrieve the pet IDs that match the filter criteria
        # Start with a basic query to select all pets of the specified breed
        # Initialize the parameters tuple with the breed filter
        query = "SELECT id FROM Cat WHERE breed=?" 
        params = (breed,) 
        
        # If filters were specified, add them to the query
        # Add the filters to the parameters tuple
        if age != 'Any':
            query += " AND age=?" 
            params += (age,)  
        if color != 'Any':
            query += " AND color=?" 
            params += (color,)  
        if gender != 'Any':
            query += " AND gender=?"  
            params += (gender,) 
        if size != 'Any':
            query += " AND size=?" 
            params += (size,)  
        
        # Execute the SQL query and store the results in a set
        c.execute(query, params)
        sql_output = c.fetchall()
        expected_output = set([x[0] for x in sql_output])
        #print(f"test_valid_input14 - expected output: {expected_output}")
        
        # Use a test request context to simulate a GET request to the website with the filter criteria as URL parameters
        with app.test_request_context('/?petType={}&breed={}&age={}&size={}&gender={}&color={}'.format(
                petType, breed, age, size, gender, color)):
            # Call the get_filtered_petIDs function with the filter criteria and store the result in a variable
            result = get_filtered_petIDs(petType, breed, age, size, gender, color)
            #print(f"test_valid_input14 - result from get_filtered_petIDs: {result}")
            
            # Check that the result matches the expected output
            self.assertEqual(result, expected_output, "test_valid_input14: Test passed - Data rendered on webpage matches database as expected")
        
        # Close the database connection
        conn.close() 
        
        
    # Function to test that all available cats are returned when no filters (Any) are chosen on Cat page('/cats')
    def test_no_filters_selected2(self):
        # Connect to the database
        conn = sqlite3.connect('Furever.db')
        c = conn.cursor()
        
        # Define filter criteria
        petType = 'Cat'
        breed = 'Any'
        age = 'Any' 
        gender = 'Any'
        color = 'Any'
        size = 'Any'
        
        # Create a SQL query to retrieve all the pet IDs in the database
        query = "SELECT id FROM Cat" 
        
        # Execute the SQL query and store the results in a set
        c.execute(query)
        sql_output = c.fetchall()
        expected_output = set([x[0] for x in sql_output])
        #print(f"test_no_filters_selected2 - expected output: {expected_output}")
        
        # Use a test request context to simulate a GET request to the website with no filter criteria
        with app.test_request_context('/?petType={}&breed={}&age={}&size={}&gender={}&color={}'.format(
                petType, breed, age, size, gender, color)):
            # Call the get_filtered_petIDs function with the filter criteria and store the result in a variable
            result = get_filtered_petIDs(petType, breed, age, size, gender, color)
            #print(f"test_no_filters_selected2 - result from get_filtered_petIDs: {result}")
            
            # Check that the result matches the expected output
            self.assertEqual(result, expected_output, "test_no_filters_selected2: Test passed - Data rendered on webpage matches database as expected")
        
        # Close the database connection
        conn.close() 
        
        
    # Function to test filter options avaiable on the Cat page('/cats'). Set returned should be empty as no pets fit the criteria.    
    def test_valid_input_that_returns_empty_set_of_Ids3(self):
        # Connect to the database
        conn = sqlite3.connect('Furever.db')
        c = conn.cursor()
        
        # Define filter criteria
        petType = 'Cat'
        breed = 'Domestic Medium Hair/Mix'
        age = 'Any'
        gender = 'Male'
        color = 'Any'
        size = 'Any'
        
        # Create a SQL query to retrieve the pet IDs that match the filter criteria
        # Start with a basic query to select all pets of the specified breed
        # Initialize the parameters tuple with the breed filter
        query = "SELECT id FROM Cat WHERE breed=?" 
        params = (breed,) 
        
        # If filters were specified, add them to the query
        # Add the filters to the parameters tuple
        if age != 'Any':
            query += " AND age=?" 
            params += (age,)  
        if color != 'Any':
            query += " AND color=?" 
            params += (color,)  
        if gender != 'Any':
            query += " AND gender=?"  
            params += (gender,) 
        if size != 'Any':
            query += " AND size=?" 
            params += (size,)  
        
        # Execute the SQL query and store the results in a set
        c.execute(query, params)
        sql_output = c.fetchall()
        expected_output = set([x[0] for x in sql_output])
        #print(f"test_valid_input_that_returns_empty_set_of_Ids3 - expected output: {expected_output}")
        
        # Use a test request context to simulate a GET request to the website with the filter criteria as URL parameters
        with app.test_request_context('/?petType={}&breed={}&age={}&size={}&gender={}&color={}'.format(
                petType, breed, age, size, gender, color)):
            # Call the get_filtered_petIDs function with the filter criteria and store the result in a variable
            result = get_filtered_petIDs(petType, breed, age, size, gender, color)
            #print(f"test_valid_input_that_returns_empty_set_of_Ids3 - result from get_filtered_petIDs: {result}")
            
            # Check that the result matches the expected output
            self.assertEqual(result, expected_output, "test_valid_input_that_returns_empty_set_of_Ids3: Test passed - Data rendered on webpage matches database as expected")
        
        # Close the database connection
        conn.close()  
        
        
    # Function to test filter options avaiable on the Cat page('/cats'). Set returned should be empty as no pets fit the criteria.     
    def test_valid_input_that_returns_empty_set_of_Ids4(self):
        # Connect to the database
        conn = sqlite3.connect('Furever.db')
        c = conn.cursor()
        
        # Define filter criteria
        petType = 'Cat'
        breed = 'Any'
        age = 'Any'
        gender = 'Female'
        color = 'Mixed'
        size = 'Large'
        
        # Create a SQL query to retrieve the pet IDs that match the filter criteria
        # Start with a basic query to select all pets of the specified gender
        # Initialize the parameters tuple with the gender filter
        query = "SELECT id FROM Cat WHERE gender=?" 
        params = (gender,) 
        
        # If filters were specified, add them to the query
        # Add the filters to the parameters tuple
        if age != 'Any':
            query += " AND age=?" 
            params += (age,)  
        if color != 'Any':
            query += " AND color=?" 
            params += (color,)  
        if breed != 'Any':
            query += " AND breed=?"  
            params += (breed,) 
        if size != 'Any':
            query += " AND size=?" 
            params += (size,)  
        
        # Execute the SQL query and store the results in a set
        c.execute(query, params)
        sql_output = c.fetchall()
        expected_output = set([x[0] for x in sql_output])
        #print(f"test_valid_input_that_returns_empty_set_of_Ids4 - expected output: {expected_output}")
        
        # Use a test request context to simulate a GET request to the website with the filter criteria as URL parameters
        with app.test_request_context('/?petType={}&breed={}&age={}&size={}&gender={}&color={}'.format(
                petType, breed, age, size, gender, color)):
            # Call the get_filtered_petIDs function with the filter criteria and store the result in a variable
            result = get_filtered_petIDs(petType, breed, age, size, gender, color)
            #print(f"test_valid_input_that_returns_empty_set_of_Ids4 - result from get_filtered_petIDs: {result}")
            
            # Check that the result matches the expected output
            self.assertEqual(result, expected_output, "test_valid_input_that_returns_empty_set_of_Ids4: Test passed - Data rendered on webpage matches database as expected")
             
if __name__ == '__main__':
    unittest.main()