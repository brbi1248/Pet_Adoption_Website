#!/usr/bin/python3

#===============================================================================
#Title: sql application
#Description: Creates dog and cat tables in database "Furever.db" and inserts 
#information for each dog and cat for adoption into tables
#Date: Apr 2023
#===============================================================================
import sqlite3

#connecting to database
conn = sqlite3.connect('Furever.db')
c= conn.cursor()

#creating cat table with attributes name, description, breed, age, gender, color, size, and location
c.execute("DROP TABLE IF EXISTS Cat")
c.execute("Create table Cat(id int, name varchar(45), description varchar(1000), breed varchar(20), age float, gender varchar(10),color varchar(10),size varchar(10), location varchar(10), primary key (id));")

#creating dog table name, description, breed, age, gender, color, size, and location
c.execute("DROP TABLE IF EXISTS Dog")
c.execute("Create table Dog(id int, name varchar(45), description varchar(1000), breed varchar(20), age float, gender varchar(10),color varchar(10),size varchar(10), location varchar(10), primary key (id));")



#creating dictionaries of all the cat information 
cat_51289679_dict = {
    'id':51289678,
    'name': 'Mocha',
    'description': "Mocha is an intelligent cat who, after getting over her initial shyness, is friendly and social. Although she doesn't care for full body pets or being picked up, she loves head and ear scritches and will hang out next to you on the couch. She also enjoys playing, looking out the window, and finding high perches where she can survey the room and take a nap. She's a graceful girl who doesn't break things, and she's a pro with her scratching pad. Mocha is looking for a home with no other cats and mature guardians who can read cat body language and respect her boundaries. In return you will be getting a sweet, lovely companion.",
    'breed': 'Domestic Shorthair/Mix',
    'age': '8.5',
    'gender': 'Female',
    'color': 'Brown',
    'size': 'Medium',
    'location': 'Foster Care'
}
cat_52058185_dict = {
    'id' : 52058185,
    'name': 'Peppi',
'description': "Like peanut butter and jelly, cups and saucers, Kermit and Miss Piggy, some things are meant to be together. And that's especially true for Peppi and Stanley. This adorable mom and son pair were brought to SAS together, and were briefly separated, but when staff saw how much they missed each other, they were reunited at their foster parent's home. Peppi didn't eat while they were apart. When Stanley saw Peppi again, he mewed happily for the first time! They were so happy to be back together. Now they sleep together like magnets and Stanley follows his mom devotedly wherever she goes.",
'breed':'Domestic Medium Hair/Mix',
'age':'4',
'gender':'Female',
'color':'Mixed',
'size':'Medium',
'location':'Foster Care' }
cat_3_dict = {
    'id' : 52072231,
    'name': 'Stanley',
'description': "Like peanut butter and jelly, cups and saucers, Kermit and Miss Piggy, some things are meant to be together. And that's especially true for Peppi and Stanley. This adorable mom and son pair were brought to SAS together, and were briefly separated, but when staff saw how much they missed each other, they were reunited at their foster parent's home. Peppi didn't eat while they were apart. When Stanley saw Peppi again, he mewed happily for the first time! They were so happy to be back together. Now they sleep together like magnets and Stanley follows his mom devotedly wherever she goes.",
'breed':'Domestic Longhair/Mix',
'age':'2',
'gender':'Male',
'color':'Orange',
'size':'Medium',
'location':'Foster Care'
}
cat_4_dict = {
    'id' : 52106194,
    'name': 'Lily',
'description': "Hi! I'm a sweet, timid kitty who loves head scratches and Churu treats! Once I feel comfortable with you, I'm inquisitive and playful. Toys with strings and feathers are my favorite. I also enjoy snuggling in blankets, giving head bumps and bird watching. I have very polite litter box manners. When I'm not curled up next to you, I'll be napping nearby because I like the company.",
    'breed':'Domestic Medium Hair/Mix',
'age':'2',
'gender':'Female',
'color':'Mixed',
'size':'Small',
'location':'Foster Care'
}
cat_5_dict = {
    'id' : 52167059,
    'name': 'Boris',
'description': "Boris is a gentle cat who true to his breed is a chatty boy.",
    'breed':'Siamese/Mix',
'age':'6',
'gender':'Male',
'color':'Seal',
'size':'Large',
'location':'Cat Free Roaming Room'
}

#creating dictionaries of all the dog information
dog1_dict = {
    'id':36636186,
    'name': 'Mojo',
    'description': "He is a perfect dog in many ways. He can be left alone with the roam of the house and just sleeps. He only chews on his toys. He's potty trained. He's a hilarious home companion.  He has no resource guarding and is great with body handling, he just loves any attention!  He's smart and can be desensitized to triggers like vacuums and blenders with steady positive association.  He may not have had socialization as a puppy to normal household things like this.",
    'breed': 'Terrier, American Pit Bull/Mix',
    'age': '6.5',
    'gender': 'Male',
    'color': 'Brindle',
    'size': 'Medium',
    'location': 'Foster Care'
}
dog2_dict = {
    'id':42904054,
    'name': 'Jane',
    'description': "I'm a Golden Girl in dog form: sassy, sprightly, and a card-carrying member of the AARP. An athletic and active gal, my hobbies include food puzzles, enjoying belly rubs, and tap dancing! I need a kind adopter to make me feel safe and loved for the rest of my years: someone to appreciate my marvelous, unique qualities. I'm a resilient, physically strong, sweetie-pie: well-mannered indoors, and don't require long walks, but would be happiest with a quiet yard of my own. No humans under 12 years, or kitties or doggos please.",
    'breed': 'Terrier,Pit Bull/Mix',
    'age': '11',
    'gender': 'Female',
    'color': 'Brindle',
    'size': 'Large',
    'location': 'Foster Care'
}
dog3_dict = {
    'id':43078721,
    'name': 'Ra',
    'description': "Ra is a spirited and smart boy with loads of personality. He's looking for the perfect forever home with the right balance of love, training and structure to help him continue to blossom.",
    'breed': 'Terrier,American Pit Bull/Mix',
    'age': '4.5',
    'gender': 'Male',
    'color': 'Brown',
    'size': 'Medium',
    'location': 'Foster Care'
}
dog4_dict = {
    'id':45447002,
    'name': 'Puck',
    'description': "Hi, I'm Puck, and like most everyone, I have some quirks but that just makes me more interesting. My foster mom says I have lots of nuance... If you don't know what a Belgian Malinois is, you should read up about us - we are known for loyalty, herding and protection. Me personally, well I'm almost five years old, and have often been told that I'm a handsome boy with my shiny brindle coat and expressive ears. I'm also a fast sprinter with quick reflexes and I love to hunt for small critters outside and chase soccer balls!",
    'breed': 'Terrier, American Pit Bull/Mix',
    'age': '5.5',
    'gender': 'Male',
    'color': 'Brindle',
    'size': 'Large',
    'location': 'Foster Care'
}
dog5_dict = {
    'id':48818187,
    'name': 'Pickles',
    'description': "Pickles didn't have the best start to his life...he came to us from a situation where he was not consistently treated with love and kindness. It takes a little bit of time for him to warm up and trust, but once you're in he is totally in love with you! He spent some time in a foster home, and his foster parent told us Pickles was so sweet and loving. He was an incredibly polite houseguest! His favorite nap spots were on the couch or on the floor next to it with his people nearby for some petting and affection. In the morning he likes to run his zoomies out and is always up for a game of ball in the yard. He's super athletic and very fast! He walks fairly well on leash, but will pull sometimes. The good news is that he's treat motivated and is a quick study, so he's ready to learn to have better leash manners.",
    'breed':'Terrier, Pit Bull/Mix',
    'age': '3.0',
    'gender': 'Male',
    'color': 'Mixed',
    'size': 'Large',
    'location': 'Dog Kennels'
}
dog6_dict = {
    'id':50272539,
    'name': 'Thomas',
    'description': "We understand that Thomas may seem shy and anxious at first (especially with men), but with the right training and patience, he has the potential to become a loyal and loving companion. He know lots of cues: sit, stay, come, shake, spin, and leave it! If you're willing to give him a chance, Thomas will reward you with his playful and affectionate personality. Come meet Thomas and see if he's the perfect match for your family.",
    'breed':'Shepherd/Mixed',
    'age': '1.5',
    'gender': 'Male',
    'color': 'Mixed',
    'size': 'Large',
    'location': 'Dog Kennels'
}
dog7_dict = {
    'id':51599202,
    'name': 'Chase',
    'description': "He gets along well with other most other dogs and most children, making him a great addition to your family. With his curious personality, he'll keep you entertained for hours! Chase is prone to mood swings, so we recommend an adopter with extensive dog experience.",
    'breed':'Bulldog',
    'age': '2',
    'gender': 'Male',
    'color': 'Black',
    'size': 'Large',
    'location': 'Dog Kennels'
}
dog8_dict = {
    'id':51962699,
    'name': 'Debo',
    'description': "Very affectionate and loves attention. He looks so serious in his photos - but he is not! What we love most is that Debo is a young pup with a lot of energy and a lot of love to give. He is already learned Sit, Down and Touch. What he loves most: Debo loves to explore and sniff everything in sight. He hasn't really figured out fetch yet, but he's eager to learn new things and loves to please his humans. He also loves attention and cuddles, and he's always up for a good belly rub.",
    'breed':'Rottweiler',
    'age': '0.5',
    'gender': 'Male',
    'color': 'Black',
    'size': 'Large',
    'location': 'Dog Kennels'
}

dog9_dict = {
    'id':52006141,
    'name': 'Ruby',
    'description': "Ruby is looking for her forever home where she can feel safe and loved. She's an affectionate and loyal companion who just needs a little patience and love to help her come out of her shell. Come meet Ruby at the Seattle Animal Shelter and give her the chance to steal your heart!",
    'breed':'Pinscher',
    'age': '2',
    'gender': 'Female',
    'color': 'Tan',
    'size': 'Medium',
    'location': 'Dog Kennels'
}

dog10_dict = {
    'id':52053831,
    'name': 'Hoss',
    'description': "Hoss is a sweet-natured, easy-going lovebug. His favorite thing in the world is snuggling up with a human, and his second favorite is burrowing under a blanket. In his foster home, he has shown that he gets along well with cats and other small dogs. He'll snuggle with any critter that will let him! When he's not busy snuggling or burrowing, Hoss enjoys playing with squeaky toys and going for short walks. He loves car rides, but he's also happy to stay home while you're out stocking up on kibble. This affectionate little guy would love to meet you!",
    'breed':'Chihuaha',
    'age': '2',
    'gender': 'Male',
    'color': 'Black',
    'size': 'Small',
    'location': 'Foster Care'
}

dog11_dict = {
    'id':52086329,
    'name': 'Peter',
    'description': "Peter is a sweet boy who just needs the right home to thrive. He can be shy at first, but once he warms up to you, he's an absolute love bug. He's house-trained and knows basic commands, making him a joy to have around the house. He hasn't yet been crate trained.",
    'breed':'American Pit Bull/Mix',
    'age': '6',
    'gender': 'Male',
    'color': 'Black',
    'size': 'Large',
    'location': 'Dog Kennels'
}

dog12_dict = {
    'id':50858047,
    'name': 'Chewy',
    'description': "Chewy is an active guy who loves to be outside regardless of the weather. He is a true PNW pup, he would spend all day playing in the rain if we let him! He is a busy guy looking for an equally busy home, with a routine he can learn, and plenty of outdoor adventuring. Chewy would do best in a home without younger children. His greatest wish is to go home with another dog who will run, chase, wrestle and tug with him all day. Chewy loves other dogs so much he doesn't mind sharing all of his toys, bowls, and people with them. He LOVES going for walks, and is making progress working on his leash behavior but will need a patient and persistent parent to continue his training so that everyone can love the walk as much as him!",
    'breed':'Siberian Husky',
    'age': '1',
    'gender': 'Male',
    'color': 'Mixed',
    'size': 'Large',
    'location': 'Foster Care'
}

dog13_dict = {
    'id':52129288,
    'name': 'Cotton',
    'description': "Hello, my name is Cotton! I enjoy walks and playing with my sister Nova. I'm a friendly dog that loves to hangout!",
    'breed':'Alaskan Husky',
    'age': '3',
    'gender': 'Male',
    'color': 'White',
    'size': 'Large',
    'location': 'Dog Kennels'
}

dog14_dict = {
    'id':52129291,
    'name': 'Nova',
    'description': "Hello, my name is Nova! I enjoy walks and playing with my brother Cotton. I'm a friendly dog that loves to hangout!",
    'breed':'Border Collie',
    'age': '2',
    'gender': 'Male',
    'color': 'Mixed',
    'size': 'Large',
    'location': 'Dog Kennels'
  
}
dog15_dict = {
    'id':52091971,
    'name': 'Steelhead',
    'description': "Steelhead is a young guy who is bouncy and full of fun! He gets along with other dogs and loves all the people he has met.",
    'breed':'American Pit Bull/Mix',
    'age': '0.5',
    'gender': 'Male',
    'color': 'Mixed',
    'size': 'Large',
    'location': 'Dog Kennels'
}

#inserting dictionary information into cat tables (5 in total)
c.execute("INSERT INTO Cat (id, name, description, breed, age, gender, color, size, location) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
          (cat_51289679_dict['id'], cat_51289679_dict['name'], cat_51289679_dict['description'], cat_51289679_dict['breed'], cat_51289679_dict['age'], cat_51289679_dict['gender'], cat_51289679_dict['color'], cat_51289679_dict['size'], cat_51289679_dict['location']))

c.execute("INSERT INTO Cat (id, name, description, breed, age, gender, color, size, location) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
          (cat_52058185_dict['id'], cat_52058185_dict['name'], cat_52058185_dict['description'], cat_52058185_dict['breed'], cat_52058185_dict['age'], cat_52058185_dict['gender'], cat_52058185_dict['color'], cat_52058185_dict['size'], cat_52058185_dict['location']))

c.execute("INSERT INTO Cat (id, name, description, breed, age, gender, color, size, location) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
          (cat_3_dict['id'], cat_3_dict['name'], cat_3_dict['description'], cat_3_dict['breed'], cat_3_dict['age'], cat_3_dict['gender'], cat_3_dict['color'], cat_3_dict['size'], cat_3_dict['location']))

c.execute("INSERT INTO Cat (id, name, description, breed, age, gender, color, size, location) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
          (cat_4_dict['id'], cat_4_dict['name'], cat_4_dict['description'], cat_4_dict['breed'], cat_4_dict['age'], cat_4_dict['gender'], cat_4_dict['color'], cat_4_dict['size'], cat_4_dict['location']))

c.execute("INSERT INTO Cat (id, name, description, breed, age, gender, color, size, location) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
          (cat_5_dict['id'], cat_5_dict['name'], cat_5_dict['description'], cat_5_dict['breed'], cat_5_dict['age'], cat_5_dict['gender'], cat_5_dict['color'], cat_5_dict['size'], cat_5_dict['location']))


#inserting dictionary information into dog tables(10 in total)
c.execute("INSERT INTO Dog (id, name, description, breed, age, gender, color, size, location) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
          (dog1_dict['id'], dog1_dict['name'], dog1_dict['description'], dog1_dict['breed'], dog1_dict['age'], dog1_dict['gender'], dog1_dict['color'], dog1_dict['size'], dog1_dict['location']))

c.execute("INSERT INTO Dog (id, name, description, breed, age, gender, color, size, location) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
          (dog2_dict['id'], dog2_dict['name'], dog2_dict['description'], dog2_dict['breed'], dog2_dict['age'], dog2_dict['gender'], dog2_dict['color'], dog2_dict['size'], dog2_dict['location']))

c.execute("INSERT INTO Dog (id, name, description, breed, age, gender, color, size, location) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
          (dog3_dict['id'], dog3_dict['name'], dog3_dict['description'], dog3_dict['breed'], dog3_dict['age'], dog3_dict['gender'], dog3_dict['color'], dog3_dict['size'], dog3_dict['location']))

c.execute("INSERT INTO Dog (id, name, description, breed, age, gender, color, size, location) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
          (dog4_dict['id'], dog4_dict['name'], dog4_dict['description'], dog4_dict['breed'], dog4_dict['age'], dog4_dict['gender'], dog4_dict['color'], dog4_dict['size'], dog4_dict['location']))

c.execute("INSERT INTO Dog (id, name, description, breed, age, gender, color, size, location) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
          (dog5_dict['id'], dog5_dict['name'], dog5_dict['description'], dog5_dict['breed'], dog5_dict['age'], dog5_dict['gender'], dog5_dict['color'], dog5_dict['size'], dog5_dict['location']))

c.execute("INSERT INTO Dog (id, name, description, breed, age, gender, color, size, location) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
          (dog6_dict['id'], dog6_dict['name'], dog6_dict['description'], dog6_dict['breed'], dog6_dict['age'], dog6_dict['gender'], dog6_dict['color'], dog6_dict['size'], dog6_dict['location']))

c.execute("INSERT INTO Dog (id, name, description, breed, age, gender, color, size, location) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
          (dog7_dict['id'], dog7_dict['name'], dog7_dict['description'], dog7_dict['breed'], dog7_dict['age'], dog7_dict['gender'], dog7_dict['color'], dog7_dict['size'], dog7_dict['location']))

c.execute("INSERT INTO Dog (id, name, description, breed, age, gender, color, size, location) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
          (dog8_dict['id'], dog8_dict['name'], dog8_dict['description'], dog8_dict['breed'], dog8_dict['age'], dog8_dict['gender'], dog8_dict['color'], dog8_dict['size'], dog8_dict['location']))

c.execute("INSERT INTO Dog (id, name, description, breed, age, gender, color, size, location) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
          (dog9_dict['id'], dog9_dict['name'], dog9_dict['description'], dog9_dict['breed'], dog9_dict['age'], dog9_dict['gender'], dog9_dict['color'], dog9_dict['size'], dog9_dict['location']))

c.execute("INSERT INTO Dog (id, name, description, breed, age, gender, color, size, location) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
          (dog10_dict['id'], dog10_dict['name'], dog10_dict['description'], dog10_dict['breed'], dog10_dict['age'], dog10_dict['gender'], dog10_dict['color'], dog10_dict['size'], dog10_dict['location']))

c.execute("INSERT INTO Dog (id, name, description, breed, age, gender, color, size, location) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
          (dog11_dict['id'], dog11_dict['name'], dog11_dict['description'], dog11_dict['breed'], dog11_dict['age'], dog11_dict['gender'], dog11_dict['color'], dog11_dict['size'], dog11_dict['location']))

c.execute("INSERT INTO Dog (id, name, description, breed, age, gender, color, size, location) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
          (dog12_dict['id'], dog12_dict['name'], dog12_dict['description'], dog12_dict['breed'], dog12_dict['age'], dog12_dict['gender'], dog12_dict['color'], dog12_dict['size'], dog12_dict['location']))

c.execute("INSERT INTO Dog (id, name, description, breed, age, gender, color, size, location) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
          (dog13_dict['id'], dog13_dict['name'], dog13_dict['description'], dog13_dict['breed'], dog13_dict['age'], dog13_dict['gender'], dog13_dict['color'], dog13_dict['size'], dog13_dict['location']))

c.execute("INSERT INTO Dog (id, name, description, breed, age, gender, color, size, location) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
          (dog14_dict['id'], dog14_dict['name'], dog14_dict['description'], dog14_dict['breed'], dog14_dict['age'], dog14_dict['gender'], dog14_dict['color'], dog14_dict['size'], dog14_dict['location']))

c.execute("INSERT INTO Dog (id, name, description, breed, age, gender, color, size, location) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
          (dog15_dict['id'], dog15_dict['name'], dog15_dict['description'], dog15_dict['breed'], dog15_dict['age'], dog15_dict['gender'], dog15_dict['color'], dog15_dict['size'], dog15_dict['location']))


#tests that all have been inserted correctly into table
try:
    c.execute("select * from Cat")
    myresult = c.fetchall()
    for x in myresult:
        print(x)
except:
    print("Error")
conn.commit()

try:
    c.execute("select * from Dog")
    myresult = c.fetchall()
    for x in myresult:
        print(x)
except:
    print("Error")
conn.commit()

