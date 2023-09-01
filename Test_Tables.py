#!/usr/bin/python3
# Functions to pull data from sql databases and test against data found in source files.

import sqlite3

#############################################################################################################
#                                Test Data Types for Each Table Column
#############################################################################################################

# Function gets data type of every column in table and stores it as a list
def get_column_datatypes(db_name, table_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # Get a list of all columns in the table
    c.execute("PRAGMA table_info({})".format(table_name))
    columns = c.fetchall()

    column_datatypes = []
    for column in columns:
        column_datatypes.append(column[2]) # Column in position 2 holds data types

    conn.close()
    
    return column_datatypes


# Function tests data types in Dog, Cat, and Contact tables
# if condition returns true, print message; otherwise, AssertionError is raised
def test_column_datatypes(db_name):
    dogDataTypes = get_column_datatypes('Furever.db', 'Dog')
    catDataTypes = get_column_datatypes('Furever.db', 'Cat')
    contactDataTypes = get_column_datatypes('Furever.db', 'Contact')
    
    # test dog table
    assert dogDataTypes == ['INT', 'varchar(45)', 'varchar(1000)', 'varchar(20)', 'float', 
                            'varchar(10)', 'varchar(10)', 'varchar(10)', 'varchar(10)'], f"expected data match for dog data types"
    print("Test passed - Data types for columns in Dog table match as expected")
    
    # test cat table
    assert catDataTypes == ['INT', 'varchar(45)', 'varchar(1000)', 'varchar(20)', 'float', 
                            'varchar(10)', 'varchar(10)', 'varchar(10)', 'varchar(10)'], f"expected data match for cat data types"
    print("Test passed - Data types for columns in Cat table match as expected")
    
    # test contact table
    assert contactDataTypes == ['INTEGER', 'VARCHAR(20)', 'VARCHAR(12)', 'INTEGER', 'VARCHAR(45)', 'VARCHAR(100)', 'INTEGER', 'VARCHAR(45)', 'INTEGER', 'INTEGER', 'VARCHAR(45)', 'VARCHAR(45)', 'VARCHAR(100)', 'INTEGER', 'INTEGER', 'INTEGER'], f"expected data match for contact data types"
    print("Test passed - Data types for columns in Contact table match as expected")

# call function
test_column_datatypes('Furever.db')


#############################################################################################################
#                                           Test Table Contents
#############################################################################################################

# Function gets data from table and stores it
def get_data(db_name, table_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute(f"SELECT * FROM {table_name}")
    data = c.fetchall()
    conn.close()
    
    return data


# Function tests data in Dog, Cat, and Adoption tables
# if condition returns true, print message; otherwise, AssertionError is raised
def test_table_data(db_name):
    dogData = get_data('Furever.db', 'Dog')
    catData = get_data('Furever.db', 'Cat')
    
    # test dog table
    assert dogData == [(36636186, 'Mojo', "He is a perfect dog in many ways. He can be left alone with the roam of the house and just sleeps. He only chews on his toys. He's potty trained. He's a hilarious home companion.  He has no resource guarding and is great with body handling, he just loves any attention!  He's smart and can be desensitized to triggers like vacuums and blenders with steady positive association.  He may not have had socialization as a puppy to normal household things like this.", 'Terrier, American Pit Bull/Mix', 6.5, 'Male', 'Brindle', 'Medium', 'Foster Care'),
                       (42904054, 'Jane', "I'm a Golden Girl in dog form: sassy, sprightly, and a card-carrying member of the AARP. An athletic and active gal, my hobbies include food puzzles, enjoying belly rubs, and tap dancing! I need a kind adopter to make me feel safe and loved for the rest of my years: someone to appreciate my marvelous, unique qualities. I'm a resilient, physically strong, sweetie-pie: well-mannered indoors, and don't require long walks, but would be happiest with a quiet yard of my own. No humans under 12 years, or kitties or doggos please.", 'Terrier,Pit Bull/Mix', 11.0, 'Female', 'Brindle', 'Large', 'Foster Care'), 
                       (43078721, 'Ra', "Ra is a spirited and smart boy with loads of personality. He's looking for the perfect forever home with the right balance of love, training and structure to help him continue to blossom.", 'Terrier,American Pit Bull/Mix', 4.5, 'Male', 'Brown', 'Medium', 'Foster Care'), 
                       (45447002, 'Puck', "Hi, I'm Puck, and like most everyone, I have some quirks but that just makes me more interesting. My foster mom says I have lots of nuance... If you don't know what a Belgian Malinois is, you should read up about us - we are known for loyalty, herding and protection. Me personally, well I'm almost five years old, and have often been told that I'm a handsome boy with my shiny brindle coat and expressive ears. I'm also a fast sprinter with quick reflexes and I love to hunt for small critters outside and chase soccer balls!", 'Terrier, American Pit Bull/Mix', 5.5, 'Male', 'Brindle', 'Large', 'Foster Care'), 
                       (48818187, 'Pickles', "Pickles didn't have the best start to his life...he came to us from a situation where he was not consistently treated with love and kindness. It takes a little bit of time for him to warm up and trust, but once you're in he is totally in love with you! He spent some time in a foster home, and his foster parent told us Pickles was so sweet and loving. He was an incredibly polite houseguest! His favorite nap spots were on the couch or on the floor next to it with his people nearby for some petting and affection. In the morning he likes to run his zoomies out and is always up for a game of ball in the yard. He's super athletic and very fast! He walks fairly well on leash, but will pull sometimes. The good news is that he's treat motivated and is a quick study, so he's ready to learn to have better leash manners.", 'Terrier, Pit Bull/Mix', 3.0, 'Male', 'Mixed', 'Large', 'Dog Kennels'), 
                       (50272539, 'Thomas', "We understand that Thomas may seem shy and anxious at first (especially with men), but with the right training and patience, he has the potential to become a loyal and loving companion. He know lots of cues: sit, stay, come, shake, spin, and leave it! If you're willing to give him a chance, Thomas will reward you with his playful and affectionate personality. Come meet Thomas and see if he's the perfect match for your family.", 'Shepherd/Mixed', 1.5, 'Male', 'Mixed', 'Large', 'Dog Kennels'), 
                       (51599202, 'Chase', "He gets along well with other most other dogs and most children, making him a great addition to your family. With his curious personality, he'll keep you entertained for hours! Chase is prone to mood swings, so we recommend an adopter with extensive dog experience.", 'Bulldog', 2.0, 'Male', 'Black', 'Large', 'Dog Kennels'), 
                       (51962699, 'Debo', "Very affectionate and loves attention. He looks so serious in his photos - but he is not! What we love most is that Debo is a young pup with a lot of energy and a lot of love to give. He is already learned Sit, Down and Touch. What he loves most: Debo loves to explore and sniff everything in sight. He hasn't really figured out fetch yet, but he's eager to learn new things and loves to please his humans. He also loves attention and cuddles, and he's always up for a good belly rub.", 'Rottweiler', 0.5, 'Male', 'Black', 'Large', 'Dog Kennels'), 
                       (52006141, 'Ruby', "Ruby is looking for her forever home where she can feel safe and loved. She's an affectionate and loyal companion who just needs a little patience and love to help her come out of her shell. Come meet Ruby at the Seattle Animal Shelter and give her the chance to steal your heart!", 'Pinscher', 2.0, 'Female', 'Tan', 'Medium', 'Dog Kennels'), 
                       (52053831, 'Hoss', "Hoss is a sweet-natured, easy-going lovebug. His favorite thing in the world is snuggling up with a human, and his second favorite is burrowing under a blanket. In his foster home, he has shown that he gets along well with cats and other small dogs. He'll snuggle with any critter that will let him! When he's not busy snuggling or burrowing, Hoss enjoys playing with squeaky toys and going for short walks. He loves car rides, but he's also happy to stay home while you're out stocking up on kibble. This affectionate little guy would love to meet you!", 'Chihuaha', 2.0, 'Male', 'Black', 'Small', 'Foster Care'), 
                       (52086329, 'Peter', "Peter is a sweet boy who just needs the right home to thrive. He can be shy at first, but once he warms up to you, he's an absolute love bug. He's house-trained and knows basic commands, making him a joy to have around the house. He hasn't yet been crate trained.", 'American Pit Bull/Mix', 6.0, 'Male', 'Black', 'Large', 'Dog Kennels'), 
                       (50858047, 'Chewy', "Chewy is an active guy who loves to be outside regardless of the weather. He is a true PNW pup, he would spend all day playing in the rain if we let him! He is a busy guy looking for an equally busy home, with a routine he can learn, and plenty of outdoor adventuring. Chewy would do best in a home without younger children. His greatest wish is to go home with another dog who will run, chase, wrestle and tug with him all day. Chewy loves other dogs so much he doesn't mind sharing all of his toys, bowls, and people with them. He LOVES going for walks, and is making progress working on his leash behavior but will need a patient and persistent parent to continue his training so that everyone can love the walk as much as him!", 'Siberian Husky', 1.0, 'Male', 'Mixed', 'Large', 'Foster Care'), 
                       (52129288, 'Cotton', "Hello, my name is Cotton! I enjoy walks and playing with my sister Nova. I'm a friendly dog that loves to hangout!", 'Alaskan Husky', 3.0, 'Male', 'White', 'Large', 'Dog Kennels'), 
                       (52129291, 'Nova', "Hello, my name is Nova! I enjoy walks and playing with my brother Cotton. I'm a friendly dog that loves to hangout!", 'Border Collie', 2.0, 'Male', 'Mixed', 'Large', 'Dog Kennels'), 
                       (52091971, 'Steelhead', 'Steelhead is a young guy who is bouncy and full of fun! He gets along with other dogs and loves all the people he has met.', 'American Pit Bull/Mix', 0.5, 'Male', 'Mixed', 'Large', 'Dog Kennels')], f"expected data match"
    
    print("Test passed - Data in Dog table match as expected")
    
    # test cat table
    assert catData == [(51289678, 'Mocha', "Mocha is an intelligent cat who, after getting over her initial shyness, is friendly and social. Although she doesn't care for full body pets or being picked up, she loves head and ear scritches and will hang out next to you on the couch. She also enjoys playing, looking out the window, and finding high perches where she can survey the room and take a nap. She's a graceful girl who doesn't break things, and she's a pro with her scratching pad. Mocha is looking for a home with no other cats and mature guardians who can read cat body language and respect her boundaries. In return you will be getting a sweet, lovely companion.", 'Domestic Shorthair/Mix', 8.5, 'Female', 'Brown', 'Medium', 'Foster Care'), 
                       (52058185, 'Peppi', "Like peanut butter and jelly, cups and saucers, Kermit and Miss Piggy, some things are meant to be together. And that's especially true for Peppi and Stanley. This adorable mom and son pair were brought to SAS together, and were briefly separated, but when staff saw how much they missed each other, they were reunited at their foster parent's home. Peppi didn't eat while they were apart. When Stanley saw Peppi again, he mewed happily for the first time! They were so happy to be back together. Now they sleep together like magnets and Stanley follows his mom devotedly wherever she goes.", 'Domestic Medium Hair/Mix', 4, 'Female', 'Mixed', 'Medium', 'Foster Care'), 
                       (52072231, 'Stanley', "Like peanut butter and jelly, cups and saucers, Kermit and Miss Piggy, some things are meant to be together. And that's especially true for Peppi and Stanley. This adorable mom and son pair were brought to SAS together, and were briefly separated, but when staff saw how much they missed each other, they were reunited at their foster parent's home. Peppi didn't eat while they were apart. When Stanley saw Peppi again, he mewed happily for the first time! They were so happy to be back together. Now they sleep together like magnets and Stanley follows his mom devotedly wherever she goes.", 'Domestic Longhair/Mix', 2, 'Male', 'Orange', 'Medium', 'Foster Care'), 
                       (52106194, 'Lily', "Hi! I'm a sweet, timid kitty who loves head scratches and Churu treats! Once I feel comfortable with you, I'm inquisitive and playful. Toys with strings and feathers are my favorite. I also enjoy snuggling in blankets, giving head bumps and bird watching. I have very polite litter box manners. When I'm not curled up next to you, I'll be napping nearby because I like the company.", 'Domestic Medium Hair/Mix', 2, 'Female', 'Mixed', 'Small', 'Foster Care'), 
                       (52167059, 'Boris', 'Boris is a gentle cat who true to his breed is a chatty boy.', 'Siamese/Mix', 6, 'Male', 'Seal', 'Large', 'Cat Free Roaming Room')], f"expected data match"
    print("Test passed - Data in Cat table match as expected")

# call function
test_table_data('Furever.db')