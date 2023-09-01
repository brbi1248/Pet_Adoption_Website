#!/usr/bin/python3

#===============================================================================
# Furever.py hosts the backend sever for FurEver Pet.
# Furever.py uses the Flask micro web framework, for more information please
# check out: https://flask.palletsprojects.com/en/2.2.x/quickstart/
#
# Webpages to cover:
# '/' -- Homepage, the entry of Furever Pet
# '/aboutus' -- About the authors, mission statement, privacy policy, and the contact information
# '/adoptionform' -- provides a real adpotion form to simulate the adoption process
# '/contacts' -- adds new contacts to the "Contact" table in the database, update the User Information page
# '/cats' -- the search and display tool to retrieve cats with user-selected cat features 
# '/dogs' -- the search and display tool to retrieve cats with user-selected dog features
# '/cat_*' -- individual cat pages
# '/dog_*' -- individual dog pages
#===============================================================================

import prefix
from flask import Flask, url_for, make_response, render_template, request, json
from markupsafe import escape
import sqlite3
#import psycopg2

conn = sqlite3.connect('Furever.db', check_same_thread=False)
c = conn.cursor()

# create app to use in this Flask application
app = Flask(__name__)


prefix.use_PrefixMiddleware(app)   

def query_db(query, args=(), one=False):
    c.execute(query, args)
    r = [dict((c.description[i][0], value) \
               for i, value in enumerate(row)) for row in c.fetchall()]
    return (r[0] if r else None) if one else r

# test route to show prefix settings
@app.route('/prefix_url')  
def prefix_url():
    return 'The URL for this page is {}'.format(url_for('prefix_url'))

#homepage
@app.route('/')
def homepage():
    return render_template('Homepage.html')

#about us
@app.route('/aboutus')
def aboutus():
    return render_template('AboutUs.html')

#adoption form
@app.route('/adoptionform')
def adoptionform():
    return render_template('AdoptionForm.html')

#insert a new contact
# This code defines a route for adding a new contact to the "Contact" table in the database.
# When a POST request is made to the "/contact" route, the contact() function is executed.
@app.route('/contact', methods = ['POST'])
def contact():
    # Convert the request form data to a dictionary and then to a JSON string
    data = json.dumps(request.form.to_dict(flat=False))
    # Parse the JSON string back into a dictionary
    data = json.loads(data)
    # Execute the SQL query to insert a new record into the "Contact" table.
    # The query uses placeholders `?` for values to prevent SQL injection.
    # These placeholders will be replaced with the actual values in the following tuple.
    c.execute('''
        INSERT INTO Contact (Name,
                    PhoneNumber,
                    TitleAnimalId,
                    Occupation,
                    Address,
                    DurationOfResidence,
                    Email,
                    AdultCount,
                    KidCount,
                    HomeType,
                    HouseholdDescription,
                    Landlord,
                    Allergy,
                    Agreement,
                    TimeCommitment) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
    # The following lines use the dictionary 'data' to access specific form values.
    # The [0] is used because the form values are stored as lists in the dictionary,
    # with the actual value being the first element of the list.
    # For example, 'data['fname'][0]' retrieves the first (and only) element of
    # the 'fname' list, which is the name entered by the user in the form.
    str(data['fname'][0] or ''),
    str(data['phone'][0]  or ''),
    data['animalId'][0],
    str(data['occupation'][0]  or ''),
    str(data['address'][0]  or ''),
    data['addresslen'][0],
    str(data['email'][0]  or ''),
    data['adultcount'][0],
    data['kidcount'][0],
    str(data['hometype'][0]  or ''),
    str(data['household'][0]  or ''),
    str(data['landlord'][0]  or ''),
    1 if 'allergy' in data and data['allergy'][0]  == 'allergy-yes' else 0,
    1 if 'decision' in data and data['decision'][0]  == 'decision-yes' else 0,
    1 if 'time' in data and data['time'][0]  == 'time-yes' else 0
    ))
    # Commit the transaction to the database
    conn.commit()
    return 'Success! For any questions, contact us by sending an email to david.knox@colorado.edu'

#show contacts
@app.route('/contacts')
def contacts():
    contacts = query_db("select * from Contact")
    return render_template('userInformation.html', contacts = contacts)

#helper function for both dog and cat search pages
def get_filtered_petIDs(petType, breed, age, size, gender, color):
    ''' 
    Input validation/fix.
    '''
    if petType != 'Dog': petType = 'Cat';
    
    '''
    Instantiate an empty set to collect IDs of user-preferred pets.
    Find the intersection of pet IDs among different attributes.
    '''
    petIDsByBreed = set();
    petIDsByAge = set();
    petIDsBySize = set();
    petIDsByGender = set();
    petIDsByColor = set();
    
    c.execute(f'SELECT * FROM {petType}');
    allPets = c.fetchall();
    
    for pet in allPets: 
        if breed == 'Any' or breed in pet[3]: petIDsByBreed.add(pet[0]);
    
    for pet in allPets:
        if age == 'Any': petIDsByAge.add(pet[0]);
        else:
            #print(age)
            ageRange = age.split('-');
            #print('ageRange[0] ', ageRange[0])
            minAge = float(ageRange[0]);
            maxAge = float(ageRange[1]);
            if minAge < pet[4] and pet[4] <= maxAge: petIDsByAge.add(pet[0]);

    for pet in allPets:
        if size == 'Any' or pet[7] == size: petIDsBySize.add(pet[0]);
    
    for pet in allPets:
        if gender == 'Any' or pet[5] == gender: petIDsByGender.add(pet[0]);
    
    for pet in allPets: 
        if color == 'Any' or pet[6] == color: petIDsByColor.add(pet[0]);
    
    petIDSet = petIDsByBreed.intersection(petIDsByAge).intersection(petIDsBySize).intersection(petIDsByGender).intersection(petIDsByColor);
    
    return petIDSet;

#search page for cats, the URL queries can be ommited 
@app.route('/cats')
def catpage():
    petType = 'Cat'
    '''
    Get multiple attributes of pets from the user input.
    The default value is a Kleen star if unassigned.
    '''
    breed = request.args.get('breed', 'Any').replace('%20', ' ');
    age = request.args.get('age', 'Any');
    size = request.args.get('size', 'Any');
    gender = request.args.get('gender', 'Any');
    color = request.args.get('color', 'Any');
    petIDSet = get_filtered_petIDs(petType, breed, age, size, gender, color);
    
    return render_template('CatPage.html', petIDSet=petIDSet, petType=petType, breed=breed, age=age, size=size, gender=gender, color=color)

#search page for dogs, the URL queries can be ommited 
@app.route('/dogs')
def dogpage():
    petType = 'Dog'
    '''
    Get multiple attributes of pets from the user input.
    The default value is a Kleen star if unassigned.
    '''
    breed = request.args.get('breed', 'Any').replace('%20', ' ');
    age = request.args.get('age', 'Any');
    size = request.args.get('size', 'Any');
    gender = request.args.get('gender', 'Any');
    color = request.args.get('color', 'Any');
    petIDSet = get_filtered_petIDs(petType, breed, age, size, gender, color);
    
    return render_template('DogPage.html', petIDSet=petIDSet, petType=petType, breed=breed, age=age, size=size, gender=gender, color=color)

# 15 ids for dogs page 
@app.route('/dog_36636186')
def dog_366():
    c.execute("SELECT name, description, breed, age, gender, color, size, location FROM Dog")
    myresult = c.fetchall()[0]
    name, description, breed, age, gender, color, size, location = myresult
    return render_template('dog_36636186.html',name=name, description=description, breed=breed, age=age, gender=gender, color=color,size=size, location=location)
@app.route('/dog_42904054')
def dog_429():
    # c.execute("select name from Dog")
    # myresult = c.fetchall()
    # name =  myresult[1][0]
    # c.execute("select description from Dog")
    # myresult2 = c.fetchall()
    # description =  myresult2[1][0]
    # c.execute("select breed from Dog")
    # myresult3 = c.fetchall()
    # breed = myresult3[1][0]
    # c.execute("select age from Dog")
    # myresult4 = c.fetchall()
    # age = myresult4[1][0]
    # c.execute("select gender from Dog")
    # myresult5 = c.fetchall()
    # gender = myresult5[1][0]
    # c.execute("select color from Dog")
    # myresult6 = c.fetchall()
    # color = myresult6[1][0]
    # c.execute("select size from Dog")
    # myresult7 = c.fetchall()
    # size = myresult7[1][0]
    # c.execute("select location from Dog")
    # myresult8 = c.fetchall()
    # location = myresult8[1][0]
    c.execute("SELECT name, description, breed, age, gender, color, size, location FROM Dog")
    myresult = c.fetchall()[1]
    name, description, breed, age, gender, color, size, location = myresult
    return render_template('dog_42904054.html',name=name, description=description, breed=breed, age=age, gender=gender, color=color,size=size, location=location)

@app.route('/dog_43078721')
def dog_430():
    c.execute("SELECT name, description, breed, age, gender, color, size, location FROM Dog")
    myresult = c.fetchall()[2]
    name, description, breed, age, gender, color, size, location = myresult
    return render_template('dog_43078721.html',name=name, description=description, breed=breed, age=age, gender=gender, color=color,size=size, location=location)
@app.route('/dog_45447002')
def dog_454():
    c.execute("SELECT name, description, breed, age, gender, color, size, location FROM Dog")
    myresult = c.fetchall()[3]
    name, description, breed, age, gender, color, size, location = myresult
    return render_template('dog_45447002.html',name=name, description=description, breed=breed, age=age, gender=gender, color=color,size=size, location=location)
@app.route('/dog_48818187')
def dog_488():
    c.execute("SELECT name, description, breed, age, gender, color, size, location FROM Dog")
    myresult = c.fetchall()[4]
    name, description, breed, age, gender, color, size, location = myresult
    return render_template('dog_48818187.html',name=name, description=description, breed=breed, age=age, gender=gender, color=color,size=size, location=location)
@app.route('/dog_50272539')
def dog_5027():
  
    c.execute("SELECT name, description, breed, age, gender, color, size, location FROM Dog")
    myresult = c.fetchall()[5]
    name, description, breed, age, gender, color, size, location = myresult
    return render_template('dog_50272539.html',name=name, description=description, breed=breed, age=age, gender=gender, color=color,size=size, location=location)
@app.route('/dog_51599202')
def dog_515():
    c.execute("SELECT name, description, breed, age, gender, color, size, location FROM Dog")
    myresult = c.fetchall()[6]
    name, description, breed, age, gender, color, size, location = myresult
    return render_template('dog_51599202.html',name=name, description=description, breed=breed, age=age, gender=gender, color=color,size=size, location=location)
@app.route('/dog_51962699')
def dog_519():
    c.execute("SELECT name, description, breed, age, gender, color, size, location FROM Dog")
    myresult = c.fetchall()[7]
    name, description, breed, age, gender, color, size, location = myresult
    return render_template('dog_51962699.html',name=name, description=description, breed=breed, age=age, gender=gender, color=color,size=size, location=location)
@app.route('/dog_52006141')
def dog_5200():
    c.execute("SELECT name, description, breed, age, gender, color, size, location FROM Dog")
    myresult = c.fetchall()[8]
    name, description, breed, age, gender, color, size, location = myresult
    return render_template('dog_52006141.html',name=name, description=description, breed=breed, age=age, gender=gender, color=color,size=size, location=location)
@app.route('/dog_52053831')
def dog_5205():
    c.execute("SELECT name, description, breed, age, gender, color, size, location FROM Dog")
    myresult = c.fetchall()[9]
    name, description, breed, age, gender, color, size, location = myresult
    return render_template('dog_52053831.html',name=name, description=description, breed=breed, age=age, gender=gender, color=color,size=size, location=location)
@app.route('/dog_52086329')
def dog_5208():
    c.execute("SELECT name, description, breed, age, gender, color, size, location FROM Dog")
    myresult = c.fetchall()[10]
    name, description, breed, age, gender, color, size, location = myresult
    return render_template('dog_52086329.html',name=name, description=description, breed=breed, age=age, gender=gender, color=color,size=size, location=location)
@app.route('/dog_50858047')
def dog_5085():
    c.execute("SELECT name, description, breed, age, gender, color, size, location FROM Dog")
    myresult = c.fetchall()[11]
    name, description, breed, age, gender, color, size, location = myresult
    return render_template('dog_50858047.html',name=name, description=description, breed=breed, age=age, gender=gender, color=color,size=size, location=location)
@app.route('/dog_52129288')
def dog_52129288():
    c.execute("SELECT name, description, breed, age, gender, color, size, location FROM Dog")
    myresult = c.fetchall()[12]
    name, description, breed, age, gender, color, size, location = myresult
    return render_template('dog_52129288.html',name=name, description=description, breed=breed, age=age, gender=gender, color=color,size=size, location=location)
@app.route('/dog_52129291')
def dog_5212921():
    c.execute("SELECT name, description, breed, age, gender, color, size, location FROM Dog")
    myresult = c.fetchall()[13]
    name, description, breed, age, gender, color, size, location = myresult
    return render_template('dog_52129291.html',name=name, description=description, breed=breed, age=age, gender=gender, color=color,size=size, location=location)
@app.route('/dog_52091971')
def dog_520919():
    c.execute("SELECT name, description, breed, age, gender, color, size, location FROM Dog")
    myresult = c.fetchall()[14]
    name, description, breed, age, gender, color, size, location = myresult
    return render_template('dog_52091971.html',name=name, description=description, breed=breed, age=age, gender=gender, color=color,size=size, location=location)

# # 5 ids for cat page 
@app.route('/cat_51289678')
def cat_512():
 
    c.execute("SELECT name, description, breed, age, gender, color, size, location FROM Cat")
    myresult = c.fetchall()[0]
    name, description, breed, age, gender, color, size, location = myresult
    return render_template('cat_51289678.html', name=name, description=description, breed=breed, age=age, gender=gender, color=color,size=size, location=location)
@app.route('/cat_52058185')
def cat_520():
    c.execute("SELECT name, description, breed, age, gender, color, size, location FROM Cat")
    myresult = c.fetchall()[1]
    name, description, breed, age, gender, color, size, location = myresult
    return render_template('cat_52058185.html', name=name, description=description, breed=breed, age=age, gender=gender, color=color,size=size, location=location)
@app.route('/cat_52072231')
def cat_5207():
    c.execute("SELECT name, description, breed, age, gender, color, size, location FROM Cat")
    myresult = c.fetchall()[2]
    name, description, breed, age, gender, color, size, location = myresult
    return render_template('cat_52072231.html',name=name, description=description, breed=breed, age=age, gender=gender, color=color,size=size, location=location)
@app.route('/cat_52106194')
def cat_521():
    c.execute("SELECT name, description, breed, age, gender, color, size, location FROM Cat")
    myresult = c.fetchall()[3]
    name, description, breed, age, gender, color, size, location = myresult
    return render_template('cat_52106194.html',name=name, description=description, breed=breed, age=age, gender=gender, color=color,size=size, location=location)
@app.route('/cat_52167059')
def cat_5216():
    c.execute("SELECT name, description, breed, age, gender, color, size, location FROM Cat")
    myresult = c.fetchall()[4]
    name, description, breed, age, gender, color, size, location = myresult
    return render_template('cat_52167059.html', name=name, description=description, breed=breed, age=age, gender=gender, color=color,size=size, location=location)
###############################################################################
# main driver function
