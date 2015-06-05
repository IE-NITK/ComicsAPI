Comics API
==========

This is an API which will be used as backend for DuckDuckGo Instant Answers for Comic Strips

Currently added comics are

+ Garfield
+ Dilbert
+ Peanuts
+ Hagar The Horrible
+ Dennis The Menace
+ Archie
+ Pickles
+ Beetle Bailey
+ Blondie
+ Wizard of Id
+ Rugrats
+ Zits
+ Intelligent Life
+ Bizarro
+ Marvin

More will be added soon.....

Procedure for Installation
--------------------------

Clone this repository into your local system
Install Flask by running command:

    sudo pip install virtualenv

Go inside the folder of the API and create a Virtual Environment by using this command:

    virtualenv flask
    
Install Flask into it by running:

    flask/bin/pip install flask
    
Change the permissions to run it by executing:

    chmod a+x app.py
    
Then execute it by running:

    ./app.py
    
Install the necessary modules using PIP after logging onto the Flask in Virtual Environment by

    source flask/bin/activate

The API is running. The link is [here](http://comic-relief.herokuapp.com/getComicLinks)