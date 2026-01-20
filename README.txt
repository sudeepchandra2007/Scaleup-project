-----------------------------FRONT END-----------------------------
FOR RUNNING THE FRONT END PART OF THE PROGRAM,WE SHOULD KEEP ALL THREE FILES IN A SAME FOLDER AND THEN OPEN THE HTML FILES TO RUN THEM
1.index.html
2.logo.jpg
3.logged-in.html
NOTE:-THIS DOES NOT HAVE ANY BACKEND(we haven't connected it with backend yet)
 
---------------------------BASIC DEMO WEBSITE WITH BACKEND INCLUDED---------------------
NOTE:-THIS IS A FULLY FUNCTIONING WEBSITE WITH SOME BASIC HTML(WE WILL LINK IT TO THWE UPPER FRONTEND FILES LATER)
Create a app folder to store all the files.
The folder should have a virtual environment
   To create virtual environment 
         python3 -m venv app
   where app is name of virtual environment
 This folder should contain directory to store html files named templates and to store css and js file in static.
   store html files in templates directory 
 In static create new directories css and js and store styles.css and scripts.js in the files respectively.
So our folder should look like
 
 app.py 
 venv app
 templates
    index.html
    base.html   
    login_investor.html  
    signup_investor.html  
    view_startups.html
    login_startup.html   
    signup_startup.html
 static
    css
       styles.css
    js 
       scripts.js

to run the program activate the virtual environment
source app/bin/activate
now run the python file in the environment
python3 app.py
Make sure all packages and modules are already installed in the system.
-----------------------------------------------TEAM MEMBERS AND CONTRIBUTIONS--------------------------
NAME                             CONTRIBUTION
CH.SUDEEP			FRONTEND AND VIDEO PRESENTATION
CEFAN SS                        BACKEND DEVELOPMENT
G.V.S.AKHIL  			PRESENTATION OF PPT 
R.TEJDEEP                       PRESENTATION OF PPT 
