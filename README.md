# Spark RPi Demo Project

## Setting up and running

Clone the project and run this command to install the python libraries using pip

    pip install -r requirements.txt

Now, run the following command to start the server

    python server.py

## API specification

Get Request: `http://<host_ip>:8080/api/object-count`

When this end-point is called, the RPi triggers capturing an image and start processing. Once it is done the response in following format would be returned to the client side.

Reponse: 
    
    {   
        count: integer,
        processed_img: string
    }
    
Here, the `processed_img` is encoded using `base64` encoding method. The client-side application has to decode that string and get the `.jpg` image back.

Cheers!
