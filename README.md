# Hyperswitch HTML + Python Integration

Build a simple checkout form to collect payment details. Included are some basic
build and run scripts you can use to start up the application.

## Running the sample

1. Add your keys :
    - Navigate to `public/script.js` and replace the placeholder `HYPERSWITCH_PUBLISHABLE_KEY` with your publishable key.
    - Navigate to `server.py` and replace the placeholder `HYPERSWITCH_API_KEY` with your API key.
  
2. Install the dependencies : 

~~~
pip3 install -r requirements.txt
~~~

3. Run the server :
~~~
export FLASK_APP=server.py
python3 -m flask run --port=4242
~~~

4. The sample app is now accessible here : [http://localhost:4242/index.html](http://localhost:4242/index.html).
