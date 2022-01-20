# how-to :: DEPLOY A FLASK APP ON APACHE2
---
## Overview
Flask is not built to serve -- on its own -- persistent or high-traffic sites. Apache, on the other hand, is. Luckily, Apache can be configured to use its industrial-grade machinery to serve Flask and other apps. Deploying your Flask app to an Apache2 server will allow anyone on the web to access your app at any time.

### Estimated Time Cost: 1 hour

### Prerequisites:
- A Digital Ocean account with a payment method
- A Digital Ocean Droplet

## Instructions
1. Install and Enable mod_wsgi
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
   Add the contents of your flask app into __init__.py
   ```
   sudo nano __init__.py
   ```
   ```
   from flask import Flask
   app = Flask(__name__)
   @app.route("/")
   def hello():
   	return "Hello, I hate Digital Ocean!"
   if __name__ == "__main__":
   	app.run()
   ```
3. Install Flask
   ```
   sudo apt-get install python3-pip
   ```
   ```
   sudo pip3 install virtualenv
   ```
   replace venv with the name of virtual environment
   ```
   sudo virtualenv venv
   ```
   ```
   source venv/bin/activate
   ```
   ```
   sudo pip3 install Flask
   ```
   Test if you installed it
   ```
   sudo python3 __init__.py
   ```
4. Configure and enable virtual host (note again that all the FlaskApp -> <your_new_name>)
   ```
   sudo nano /etc/apache2/sites-available/FlaskApp.conf
   ```
   Change mywebsite.com to the IP, and FlaskApp to name of your flask app
   ```
   <VirtualHost *:80>
		ServerName mywebsite.com
		ServerAdmin admin@mywebsite.com
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
   Enable Virtual Host
   ```
   sudo a2ensite FlaskApp
   ```
5. Create WSGI file
   ```
   cd /var/www/FlaskApp
   ```
   ```
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
6. Apply changes
   ```
   sudo service apache2 restart
   ```
You should be able to access your virtual host at your ip address!

### Resources
* https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps
---

Accurate as of (last update): 2022-01-18

#### Contributors:  
Hebe Huang, pd2  
Josephine Lee, pd2  
Rachel Xiao, pd2  
