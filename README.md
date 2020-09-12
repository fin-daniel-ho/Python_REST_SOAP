### Author: Dung Ho
### Email: dung.ho@edu.turkuamk.fi
### Phone number: +358 449865555


## Overview
_This is a simple message board web application which is combination of Flask and Spyne. The application has two services: createMessage and listMessages._


## General
- The web application was implemented by using Python Flask library and RESTful protocol.
The application includes 2 services:

    + createMessage supports 2 protocols REST and SOAP11. With POST request, the request data can be sent either by Postman tool or cURL.
    With REST protocol, the request data can be retrieved from Frontend part.
    
	    Example post data (REST protocol):
	    ```
		{
		    "title": "Any",
		    "content": "Your choice of content",
		    "sender": "Seed",
		    "url": "https://www.abc.xyz"
		}
	    ```
    + listMessages: with GET request. This service supports 2 response versions.
        Version 1 returns 3 fields title, content and sender.
        Version 2 returns 4 field title, content, sender and url with the format based on the query parameter ('json' for JSON format - 'xml' for XML format).
	
	
        Example XML format:
	```
            <messages>
                <msg>
                    <title> ANY </title>
                    <content> ANY </content>
                    <sender> ANY </sender>
                    <url> https://www.abc.xyz </url>
                </msg>
            </messages>
	```

## Requirements
- Python 3.7 or above.
- Libraries: dev-requirements.txt and requirements.txt


## How to use
1. Install pipenv: 
	`pip3 install pipenv`

2. Set permission for .sh file:
    + Linux/MacOS: 
    	`sudo chmod +x start.sh`
    + Windows: skipped to step 3.

3. Run the application: 
    + Linux/MacOS terminal:
    	`./start.sh`
    + Windows CMD: (simply run) pipenv run python main.py

4. Test the API:
    You can test in the FrontEnd part, or test by using Postman or cURL.
    + Homepage: http://127.0.0.1:5000/index

    + Create Message - REST protocol: http://127.0.0.1:5000/api/createMessage
    
		Example POST request:
		```
		curl --location --request POST 'http://127.0.0.1:5000/api/createMessage' \
		--header 'Content-Type: application/json' \
		--data-raw '{
		    "title": "ANY",
		    "content": "ANY",
		    "sender": "ANY",
		    "url": "Valid URL"
		}'
		```

    + Create Message - SOAP11 protocol: http://127.0.0.1:5000/soap/create_message
    
		Example POST request:
		```
		    curl --location --request POST 'http://127.0.0.1:5000/soap/create_message' \
		    --header 'Content-Type: text/xml' \
		    --data-raw '<soap11env:Envelope xmlns:soap11env="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tns="message_board.soap">
		    <soap11env:Body>
			<ns0:create_message xmlns:ns0="message_board.soap">
			<ns0:message>
			    <ns0:title>Any</ns0:title>
			    <ns0:content>AnyContent</ns0:content>
			    <ns0:sender>Any</ns0:sender>
			    <ns0:url>AnyURL</ns0:url>
			</ns0:message>
			</ns0:create_message>
		    </soap11env:Body>
		    </soap11env:Envelope>'
		```
    + List Messages: Version1 - http://127.0.0.1:5000/api/listMessages

    + List Messages: Version2/JSON - http://127.0.0.1:5000/api/listMessages?format=json

    + List Messages: Version2/XML - http://127.0.0.1:5000/api/listMessages?format=xml
    
		Example GET request:
		```
		curl --location --request GET 'http://127.0.0.1:5000/api/listMessages?format=xml' \
		--header 'Content-Type: application/xml'
		```
