#!flask/bin/python
import atexit
import requests
import datetime
import lxml.html
import os
from flask import Flask, jsonify
from datetime import date, timedelta
from apscheduler.scheduler import Scheduler

comicJSON = {}
app = Flask(__name__)
#Start CRON Job
cron = Scheduler()
cron.start()

@cron.interval_schedule(seconds = 180)  #change it to 30 seconds on local system while testing
def job_function():
    for comicName in ['garfield','dilbert','peanuts','hagar the horrible','dennis the menace','archie','pickles','beetle bailey','blondie','wizard of id','rugrats','zits','intelligent life','bizarro','marvin']:
        if comicName == 'garfield':
            comicHTML = lxml.html.document_fromstring(requests.get("http://garfield.com/").content)
            img_src = comicHTML.xpath('//*[@id="home_comic"]/img/@src')[0]
            #print "Case 1 Successful!"
            comicJSON[comicName] = img_src
          
        
        if comicName == "dilbert":
            comicHTML = lxml.html.document_fromstring(requests.get("http://dilbert.com/").content)
            img_src = comicHTML.xpath('/html/body/div[2]/div[3]/section/div[1]/a/img/@src')[0]
            #print "Case 2 Successful!"
            comicJSON[comicName] = img_src

        
        #if comicName == "calvin and hobbes":
        #    comicHTML = lxml.html.document_fromstring(requests.get("http://www.gocomics.com/calvinandhobbes/").content)
        #    img_src = comicHTML.xpath('//*[@id="content"]/div[1]/p[1]/a/img/@src')[0]
        #    #print "Case 3 Successful!"
        #    comicJSON[comicName] = img_src

        
        #if comicName == "bloom county":
        #    comicHTML = lxml.html.document_fromstring(requests.get("http://www.gocomics.com/bloomcounty/").content)
        #    img_src = comicHTML.xpath('//*[@id="content"]/div[1]/p[1]/a/img/@src')[0]
        #    print "Case 4 Successful!"
        #    comicJSON[comicName] = img_src

        
        if comicName == "peanuts":
        #    print "Case 4 Successful!"
            comicHTML = lxml.html.document_fromstring(requests.get("http://www.arcamax.com/thefunnies/peanuts/").content)
            img_src = comicHTML.xpath('//*[@id="comic-zoom"]/@src')[0]
        #    print "Case 4 Successful!"
            comicJSON[comicName] = "http://www.arcamax.com"+img_src

        if comicName == "hagar the horrible":
            comicHTML = lxml.html.document_fromstring(requests.get("http://www.arcamax.com/thefunnies/hagarthehorrible/").content)
            img_src = comicHTML.xpath('//*[@id="comic-zoom"]/@src')[0]
        #    print "Case 4 Successful!"
            comicJSON[comicName] = "http://www.arcamax.com"+img_src

        if comicName == "dennis the menace":
            comicHTML = lxml.html.document_fromstring(requests.get("http://www.arcamax.com/thefunnies/dennisthemenace/").content)
            img_src = comicHTML.xpath('//*[@id="comic-zoom"]/@src')[0]
        #    print "Case 5 Successful!"
            comicJSON[comicName] = "http://www.arcamax.com"+img_src

        if comicName == "archie":
            comicHTML = lxml.html.document_fromstring(requests.get("http://www.arcamax.com/thefunnies/archie/").content)
            img_src = comicHTML.xpath('//*[@id="comic-zoom"]/@src')[0]
        #    print "Case 5 Successful!"
            comicJSON[comicName] = "http://www.arcamax.com"+img_src
        #    print comicJSON[comicName]

        if comicName == "pickles":
            comicHTML = lxml.html.document_fromstring(requests.get("http://www.arcamax.com/thefunnies/pickles/").content)
            img_src = comicHTML.xpath('//*[@id="comic-zoom"]/@src')[0]
        #    print "Case 6 Successful!"
            comicJSON[comicName] = "http://www.arcamax.com"+img_src
        #    print comicJSON[comicName]

        if comicName == "beetle bailey":
            comicHTML = lxml.html.document_fromstring(requests.get("http://www.arcamax.com/thefunnies/beetlebailey/").content)
            img_src = comicHTML.xpath('//*[@id="comic-zoom"]/@src')[0]
        #    print "Case 6 Successful!"
            comicJSON[comicName] = "http://www.arcamax.com"+img_src
        #    print comicJSON[comicName]

        if comicName == "blondie":
            comicHTML = lxml.html.document_fromstring(requests.get("http://www.arcamax.com/thefunnies/blondie/").content)
            img_src = comicHTML.xpath('//*[@id="comic-zoom"]/@src')[0]
        #    print "Case 6 Successful!"
            comicJSON[comicName] = "http://www.arcamax.com"+img_src
        #    print comicJSON[comicName]

        if comicName == "wizard of id":
            comicHTML = lxml.html.document_fromstring(requests.get("http://www.arcamax.com/thefunnies/wizardofid/").content)
            img_src = comicHTML.xpath('//*[@id="comic-zoom"]/@src')[0]
        #    print "Case 6 Successful!"
            comicJSON[comicName] = "http://www.arcamax.com"+img_src
        #    print comicJSON[comicName]

        if comicName == "rugrats":
            comicHTML = lxml.html.document_fromstring(requests.get("http://www.arcamax.com/thefunnies/rugrats/").content)
            img_src = comicHTML.xpath('//*[@id="comic-zoom"]/@src')[0]
        #    print "Case 6 Successful!"
            comicJSON[comicName] = "http://www.arcamax.com"+img_src
        #    print comicJSON[comicName]

        if comicName == "zits":
            comicHTML = lxml.html.document_fromstring(requests.get("http://www.arcamax.com/thefunnies/zits/").content)
            img_src = comicHTML.xpath('//*[@id="comic-zoom"]/@src')[0]
        #    print "Case 6 Successful!"
            comicJSON[comicName] = "http://www.arcamax.com"+img_src
        #    print comicJSON[comicName]

        if comicName == "intelligent life":
            comicHTML = lxml.html.document_fromstring(requests.get("http://www.arcamax.com/thefunnies/intelligentlife/").content)
            img_src = comicHTML.xpath('//*[@id="comic-zoom"]/@src')[0]
        #    print "Case 6 Successful!"
            comicJSON[comicName] = "http://www.arcamax.com"+img_src
        #    print comicJSON[comicName]

        if comicName == "bizarro":
            comicHTML = lxml.html.document_fromstring(requests.get("http://www.arcamax.com/thefunnies/bizarro/").content)
            img_src = comicHTML.xpath('//*[@id="comic-zoom"]/@src')[0]
        #    print "Case 6 Successful!"
            comicJSON[comicName] = "http://www.arcamax.com"+img_src
        #    print comicJSON[comicName]

        if comicName == "marvin":
            comicHTML = lxml.html.document_fromstring(requests.get("http://www.arcamax.com/thefunnies/marvin/").content)
            img_src = comicHTML.xpath('//*[@id="comic-zoom"]/@src')[0]
        #    print "Case 6 Successful!"
            comicJSON[comicName] = "http://www.arcamax.com"+img_src
        #    print comicJSON[comicName]


atexit.register(lambda: cron.shutdown(wait=False))
@app.route('/getComicLinks', methods=['GET'])
def get_tasks():
    #print "Request Handled"
    return jsonify(comicJSON)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port,debug=True)