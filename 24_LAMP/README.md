# how-to :: CREATE A DIGITAL OCEAN DROPLET WITH UBUNTU AND APACHE
---
## Overview
Guide to creating an ubuntu 20.04 virtual machine ("droplet") and installing Apache2 web server on it.

### Estimated Time Cost: 1.5 hours

### Prerequisites:

- You will need Digital Ocean credit and an Digital Ocean account with a valid payment method.

### Instructions: 

1. Once on the projects dashboard, click "Create" and choose "Droplets" in the dropdown menu.
2. Choose Ubuntu 20.04 (LTS), the basic plan, and a regular intel CPU with an SSD. Choose the datacenter region nearest to you and "SSH keys" for authentication method.
3. Set up SSH keys with the instructions from [this link](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys)
4. Put your ssh public key and your SSH key name into the appropriate fields. Your ssh public key can be found through the terminal in `~/.ssh` and in a file ending in ".pub"
5. Click "Create Droplet"
6. Once the droplet is created, launch the console from the droplet dashboard on Digital Ocean.
7. Create sudo-enabled users using the instructions from [this link](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-sudo-enabled-user-on-ubuntu-18-04-quickstart)
8. Install pip: 
```
apt install python3-pip
```
9. Install virtual enviroments: 
```
apt install python3.8-venv
```
10. Install flask:
```
pip install Flask
```
11. Install apache:
```
sudo apt install apache2
sudo ufw allow 'Apache'
```
11. Install emacs:
```
sudo apt-get install emacs
```
12. Install tree:
```
sudo apt-get install tree
```
13. Install traceroute:
```
sudo apt-get install traceroute
```
14. Install sqlite3:
```
sudo apt-get install sqlite3
```
15. Install sl:
```
sudo apt install sl
```

### Resources
* https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-20-04
* https://www.digitalocean.com/community/questions/error-permission-denied-publickey-when-i-try-to-ssh
* https://www.digitalocean.com/community/questions/secure-ubuntu-server-for-non-root-user-using-only-ssh-keys?answer=22286
* https://www.digitalocean.com/community/tutorials/how-to-create-a-new-sudo-enabled-user-on-ubuntu-18-04-quickstart
* https://www.digitalocean.com/docs/droplets/how-to/
* https://www.digitalocean.com/community/questions/error-permission-denied-publickey-when-i-try-to-ssh?answer=44730
* https://www.digitalocean.com/docs/droplets/how-to/connect-with-ssh/putty/
* https://www.digitalocean.com/docs/droplets/how-to/add-ssh-keys/create-with-openssh/
* https://www.digitalocean.com/docs/droplets/how-to/connect-with-ssh/openssh/


---

Accurate as of (last update): 2022-01-15

#### Contributors:  
Josephine Lee, pd2  
Rachel Xiao, pd2  
Hebe Huang, pd2  
