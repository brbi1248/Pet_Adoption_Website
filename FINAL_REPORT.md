# Project title: Pet Adoption Website

# Team members' names:
* Mayra Weidner - MYWeidner, mawe7753@colorado.edu
* Brittany Bilotti - brbi1248 - brbi1248@colorado.edu
* Mayumi Shimobe - Mayumi-GT - mash8545@colorado.edu
* Zack Cheng - zacktcheng - tsch3115@colorado.edu

# Project tracker link
Access our Trello board [here](https://trello.com/w/fantasticfour82).

# Link to 5 minute video: a demo for a potential customer
Access our a demo video [here](/Demo.mp4)

# Version control repository link
* Access out GItHub repositoty commit history [here](https://github.com/Fantastic4Project3308/PetRescue/commits/main)
* Access our Trello board [here](https://trello.com/w/fantasticfour82)

# Final Status Report

## What you completed
  * Scrum meeting every week (once or twice a week)
    * Link to the GitHub weekly status [here](https://trello.com/w/fantasticfour82)
    * Follow the best practice of Agile meeting style
    * We took turn to be the scrum master each week or sprint
  * Recorded meeting minutes on GitHub
    * Link to the GitHub weekly status [here](/WeeklyStatus/WEEKLY_STATUS.md)
  * Project management with Trello
    * Communicate and discuss at our weekly meeting to distribute tasks efficiently
  * Webscraping
    * Webscraped script that scrape webpages on petango.com
    * Collected pet information in text and html files
  * Website design mockup
    * Researched Wix.com and pet adaption websites to create simple mockup designs
    * Created pdf files of webpage design and links between pages    
  * Flask Backend
    * Created eight routes 
        1. '/' -- Homepage, the entry of Furever Pet
        2. '/aboutus' -- About the authors, mission statement, privacy policy, and the contact information
        3. '/adoptionform' -- provides a real adpotion form to simulate the adoption process
        4. '/contacts' -- adds new contacts to the "Contact" table in the database, update the User Information page
        5. '/cats' -- the search and display tool to retrieve cats with user-selected cat features 
        6. '/dogs' -- the search and display tool to retrieve cats with user-selected dog features
        7. '/cat_*' -- individual cat pages
        8. '/dog_*' -- individual dog pages
  * Sqlite database
    * Created dictionary with animal data from webscraping text pages
    * Created `cat`, `dog` and `contact` tables 
    * Used the tables to dynamically insert into webpages
  * Frontend (HTML/ CSS/ Javascript)
    * Created webdesign HTML template, CSS style, for all pages
    * Collected free images from webscraping for animals and logos
    * Created javascript to enable links between pages
    * Used javascript to send a request to backend to rerender search results
    * See below for a couple of screenshots of our website 
    <br>
    <img src="static/finalreport_Images/homepage.png" alt="Homepage" WIDTH=30% ALIGH="LEFT"/>
    <br>
    <img src="static/finalreport_Images/cats.png" alt="Cats" WIDTH=30% ALIGH="LEFT"/>
    <br>
    <img src="static/finalreport_Images/adaptionform.png" alt="Form" WIDTH=30% ALIGH="LEFT"/>
    <br>
  * Testing SQL/ tables
    * Used python assert statements to test whether data types in Sqlite database match as expected
    * Tested that table contents matched as expected based on the data scraped
    * Tested that routes rendered data from Sqlite database as expected
    * Used Python unittest to ensure that filter options on Dog and Cat pages pulled data from Sqlite database as expected
  * Version control
    * Consistently used GitHub to update files up-to-date
    * Used individual `branch` as needed on GitHub
  * Test deployment
    * Used Render.com as our PaaS to deploy our website
    * Created wsgi file to direct render to read from our flask application

  
## What you were in the middle of implementing
  * Improve `mailto` by having a pop-up for user to send an email to Dr. Knox
  * Implement a link to `adaption form` on each animal pages

## What you had planned for the future
   * Increase the variety of animals
   * Improve the webscraping to imcorporate hundreds of animals
   * Use coding instead of hard coding practice for each animals
   * Create a volunteer page
   * Improve the frontend to make it more dynamic with popular frameworks like Reacts.js and Vue.js
   * Improve the webdesign to be more user friendly by modern design using libraries like bootstrap css
   * Practice `Pull Request Reviews` for better security

## Any known problems (bugs, issues)
  * Slow wakefulness due to free website hosting


# Access our website via public hosting site [here](https://fureverpet.onrender.com/).
