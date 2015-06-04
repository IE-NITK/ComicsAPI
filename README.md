Comics API
==========

This is an API which will be used as backend for DuckDuckGo Instant Answers for Comic Strips

Currently added comics are

+ Garfield
+ Dilbert
+ Peanuts

Procedure for Installation
--------------------------

Clone this repository into your local system
Install Flask by running command:

    sudo pip install virtualenv

Go inside the folder of the API and create a Virtual Environment by using this command:

    virtualenv flask;flask/bin/pip install flask
    
Install Flask into it by running:

    flask/bin/pip install flask
    
Change the permissions to run it by executing:

    chmod a+x app.py
    
Then execute it by running:

    ./app.py
    
Install the necessary modules using PIP after logging onto the Flask in Virtual Environment by

    source flask/bin/activate