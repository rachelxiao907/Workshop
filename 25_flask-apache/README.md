# how-to :: DEPLOY A FLASK APP ON APACHE2
---
## Overview
Flask is not built to serve -- on its own -- persistent or high-traffic sites. Apache, on the other hand, is. Luckily, Apache can be configured to use its industrial-grade machinery to serve Flask and other apps. Deploying your Flask app to an Apache2 server will allow anyone on the web to access your app at any time.

### Estimated Time Cost: 1 hour

### Prerequisites:
- A Digital Ocean account with a payment method
- A Digital Ocean Droplet

## Instructions
1. Install mod_wsgi
   ```
   sudo apt-get install libapache2-mod-wsgi-py3 python-dev
   ```
   Enable mod_wsgi
   ```
   sudo a2enmod wsgi
   ```
2. Create a Flask App
   > Replace FlaskApp with the name of your application
   ```
   cd /var/www
   ```
   ```
   sudo mkdir FlaskApp
   ```
   ```
   cd FlaskApp
   ```
   ```
   sudo mkdir FlaskApp
   ```
   ```
   cd FlaskApp
   sudo mkdir static templates
   ```
   Create an __init__.py file with your flask app content
   ```
   sudo nano __init__.py
   ```
   This can be your most basic flask app content
   ```
   from flask import Flask
   app = Flask(__name__)
   @app.route("/")
   def hello():
   	return "Hello, Digital Ocean is cool!"
   if __name__ == "__main__":
   	app.run()
   ```
3. Install Flask
   > We will use a virtual environment for our flask app
   Install pip
   ```
   sudo apt-get install python3-pip
   ```
   Install virtual environment
   ```
   sudo pip3 install virtualenv
   ```
   ```
   sudo virtualenv <venv name>
   ```
   Activate virtual environment
   ```
   source <venv name>/bin/activate
   ```
   Install Flask in virtual environment
   ```
   sudo pip3 install Flask
   ```
   Test if Flask is installed by running the app
   ```
   sudo python3 __init__.py
   ```
4. Configure and Enable a New Virtual Host
   > Replace FlaskApp with the name of your application
   ```
   sudo nano /etc/apache2/sites-available/FlaskApp.conf
   ```
   ```
   <VirtualHost *:80>
		ServerName <IP address>
		ServerAdmin admin@<IP address>
		WSGIScriptAlias / /var/www/FlaskApp/flaskapp.wsgi
		<Directory /var/www/FlaskApp/FlaskApp/>
			Order allow,deny
			Allow from all
		</Directory>
		Alias /static /var/www/FlaskApp/FlaskApp/static
		<Directory /var/www/FlaskApp/FlaskApp/static/>
			Order allow,deny
			Allow from all
		</Directory>
		ErrorLog ${APACHE_LOG_DIR}/error.log
		LogLevel warn
		CustomLog ${APACHE_LOG_DIR}/access.log combined
   </VirtualHost>
   ```
   Enable virtual host
   ```
   sudo a2ensite FlaskApp
   ```
5. Create .wsgi File
   > Serves Flask app
   ```
   cd /var/www/FlaskApp
   sudo nano flaskapp.wsgi
   ```
   ```
   #!/usr/bin/python
   import sys
   import logging
   logging.basicConfig(stream=sys.stderr)
   sys.path.insert(0,"/var/www/FlaskApp/")

   from FlaskApp import app as application
   application.secret_key = 'Add your secret key'
   ```
6. Apply Changes by Restarting Apache
   ```
   sudo service apache2 restart
   ```
You should be able to access your virtual host at your IP address!

### Resources
* https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps
---

Accurate as of (last update): 2022-01-18

#### Contributors:  
Hebe Huang, pd2  
Josephine Lee, pd2  
Rachel Xiao, pd2  
