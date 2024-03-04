## prereqipsite for running this project:

Register for a free AWS root account, read AWS documentation for more details
 - AWS EC2 instance with OPENVPN Access Server AMI
 - AWS RDS MySQL

# Installation guide


    git clone https://github.com/fishoil/privateVPN.git

Make sure virtual environment is activated,
Check project ownership 

    sudo mkdir -p /home/openvpnas/privateVPN/instance
    sudo chown -R $USER:$USER /home/openvpnas/privateVPN/instance
	  


##  Packages

    Flask  
    Flask-RESTful  
    Flask-SQLAlchemy  
    Flask-login  
    SQLAlchemy  
    pytz

