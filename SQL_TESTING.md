# Table 1 - Dog
Table name: Dog    
Table Description: In this table, we'll have dog ID numbers, name, description, gender, breed, age, color, size, and location.    
Fields:  
* Title (int) - we are treating this field as a primary key or dog ID number
* Name (varchar(20)) - dog's name
* Description (varchar(500)) - dog's personality and characteristics
* Gender (varchar(6)) - dog's gender (male or female)
* Breed (varchar(20)) - dog's breed
* Age (varchar(30)) - age of dog in years/months/days
* Color (varchar(20)) - dog's primary color(s)
* Size (varchar(6)) - dog's size in small, medium, or large 
* Location (varchar(20)) - shelter/ foster care where dog is currently housed

List of tests for verifying each table:  
### Test 1
Use case name:   
Verify data types for title, name, description, gender, breed, age, color, size, and location   
Description: Test the data types  
Pre-conditions: Data types are valid for each attribute  
Test steps  
1. Loop through each column 
2. Return data
3. Verify data type matches criteria 

Expected result: Data types should match criteria  
Actual result: Data is displayed with correct data type  
Status (Pass/Fail):   
Pass - print successful message  
Fail - print error message  
Notes: N/A  
Post-conditions: Data types are validated and data is successfully inserted into table  

### Test 2
Use case name:   
Verify that dog ID and data for each attribute matches source file  
Description: Test attribute data  
Pre-conditions: The data in the source file exists and is not null  
Test steps  
1. Loop through each dog ID, if ID matches source data, then compare all attributes
2. If attributes match source data then return successful message
3. Otherwise, return error message

Expected result: Table was successfully created from source data  
Actual result: Table was successfully created from source data  
Status (Pass/Fail):   
Pass - print successful message  
Fail - print error message  
Notes: N/A  
Post-conditions: Attributes are validated and data is successfully inserted into table  

# Table 2 - Cat
Table name: Cat    
Table Description: In this table, we'll have cat ID numbers, name, description, gender, breed, age, color, size, and location.  
Fields:  
* Title (int) - we are treating this field as a primary key or cat ID number
* Name (varchar(20)) - cat's name
* Description (varchar(500)) - cat's personality and characteristics
* Gender (varchar(6)) - cat's gender (male or female)
* Breed (varchar(20)) - cat's breed
* Age (varchar(30)) - age of cat in years/months/days
* Color (varchar(20)) - cat's primary color(s)
* Size (varchar(6)) - cat's size in small, medium, or large 
* Location (varchar(20)) - shelter/ foster care where cat is currently housed

List of tests for verifying each table:  
### Test 1
Use case name:   
Verify data types for title, name, description, gender, breed, age, color, size, and location   
Description: Test the data types  
Pre-conditions: Data types are valid for each attribute  
Test steps  
1. Loop through each column 
2. Return data
3. Verify data type matches criteria 

Expected result: Data types should match criteria  
Actual result: Data is displayed with correct data type  
Status (Pass/Fail):   
Pass - print successful message  
Fail - print error message  
Notes: N/A  
Post-conditions: Data types are validated and data is successfully inserted into table  

### Test 2
Use case name:   
Verify that cat ID and data for each attribute matches source file  
Description: Test attribute data  
Pre-conditions: The data in the source file exists and is not null  
Test steps  
1. Loop through each cat ID, if ID matches source data, then compare all attributes
2. If attributes match source data then return successful message
3. Otherwise, return error message

Expected result: Table was successfully created from source data  
Actual result: Table was successfully created from source data  
Status (Pass/Fail):   
Pass - print successful message  
Fail - print error message  
Notes: N/A  
Post-conditions: Attributes are validated and data is successfully inserted into table  

# Table 3 - Adoption Form Contact List
Table name: Contact List   
Table Description: In this table, we'll have the name and phone number of anyone who is interested in adoption (i.e whoever fills out the adoption form). The table will also list the animal ID that the user was interested in adopting as well as a unique identifier assigned to each user.   
Fields:  
* ID (int) - unique identifier for each person
* Name (varchar(20)) - person's full name
* Phone Number (varchar(10)) - person's phone number
* Title (int) - animal ID

List of tests for verifying each table:  
### Test 1
Use case name:   
Verify data types for name, phone number, and animal ID    
Description: Test the data types  
Pre-conditions: Data types are valid for each attribute  
Test steps  
1. User provides name, phone number, and animal ID in adoption form
2. User clicks on submit button 
3. Verify data type for these attributes matches criteria

Expected result: Message on webpage tells user that information has been submitted once submit button is pressed  
Actual result: Message on webpage tells user that information has been submitted once submit button is pressed  
Status (Pass/Fail):  
Pass - print successful message  
Fail - print error message  
Notes: N/A  
Post-conditions: Data types are validated and user information data is added to contact list table  

# Query 1
Name: Dog query  
Description: This query will pull data from source file and insert it into the Dog table. The data in the table will then show up on each dog's html page.  
Parameters: Title (dog ID)  
Return values:  
* Name
* Description
* Gender
* Breed
* Age
* Color
* Size
* Location  

List of tests for verifying each access method    

### Test 1
Use case name:  
Verify that data attribute match data on webpage  
Description: Test webpage data  
Pre-conditions: There is data on the webpage  
Test steps
1. Go through each div on webpage and check if equal to data in dog table
2. If attributes match source data then render webpage
3. Otherwise, return 404 error

Expected result: User can load webpage  
Actual result: User is successfully navigated to webpage for dog of choice  
Status (Pass/Fail):   
Pass - print successful message  
Fail - print error message  
Notes: N/A  
Post-conditions: Send message to indicate attribute matching was successful to console log.  

### Test 2
Use case name:   
Verify that dog page updates based on user's search criteria  
Description: Test that filter on dog page renders correct SQL data attributes  
Pre-conditions: User wants to use filters to find a dog  
Test steps  
1. User selects attributes from filter search bar and hits submit button
2. Verify that webpage rendered dog images based on user selections

Expected result: Webpage is loaded with dog images that fit user search criteria  
Actual result: Webpage is loaded with dog images that fit user search criteria  
Status (Pass/Fail):   
Pass - print successful message  
Fail - print error message  
Notes: Filters on webpage are directly linked to SQL attributes. When user makes a selection and presses submit button, the query contain the attributes that fit the search criteria.   
Post-conditions: Send message to indicate search was successful to console log.  

# Query 2
Name: Cat query  
Description: This query will pull data from source file and insert it into the Cat table. The data in the table will then show up on each cat's html page.  
Parameters: Title (cat ID)  
Return values:  
* Name
* Description
* Gender
* Breed
* Age
* Color
* Size
* Location  

List of tests for verifying each access method  

### Test 1
Use case name:   
Verify that data attribute match data on webpage  
Description: Test webpage data  
Pre-conditions: There is data on the webpage  
Test steps  
1. Go through each div on webpage and check if equal to data in cat table
2. If attributes match source data then render webpage
3. Otherwise, return 404 error

Expected result: User can load webpage  
Actual result: User is successfully navigated to webpage for cat of choice  
Status (Pass/Fail):  
Pass - print successful message  
Fail - print error message  
Notes: N/A  
Post-conditions: Send message to indicate attribute matching was successful to console log.  

### Test 2
Use case name:     
Verify that cat page updates based on user's search criteria      
Description: Test that filter on cat page renders correct SQL data attributes  
Pre-conditions: User wants to use filters to find a cat  
Test steps  
1. User selects attributes from filter search bar and hits submit button
2. Verify that webpage rendered cat images based on user selections

Expected result: Webpage is loaded with cat images that fit user search criteria  
Actual result: Webpage is loaded with cat images that fit user search criteria  
Status (Pass/Fail):   
Pass - print successful message  
Fail - print error message  
Notes: Filters on webpage are directly linked to SQL attributes. When user makes a selection and presses submit button, the query contain the attributes that fit the search criteria.   
Post-conditions: Send message to indicate search was successful to console log.  

# Query 3
Name: Contact List query  
Description: This query will pull data from the adoption form which users will fill out online and output the information to a webpage for internal use.  
Parameters: none  
Return values:  
* ID
* Name
* Phone Number
* Title (animal ID  

List of tests for verifying each access method  

### Test 1
Use case name:   
Verify that user contact information is stored in table  
Description: Test that user contact data can be rendered on webpage  
Pre-conditions: The user has filled out the adoption form  
Test steps
1. Go through each attribute in table and check for null values
2. If attributes are complete, then render on webpage
3. Otherwise, exclude user information from webpage

Expected result: Webpage with viewable contact list as table  
Actual result: Contact list for internal use  
Status (Pass/Fail):   
Pass - print successful message  
Fail - print error message  
Notes: N/A  
Post-conditions: FurEver Pet employees now have a list of potential adopters  
