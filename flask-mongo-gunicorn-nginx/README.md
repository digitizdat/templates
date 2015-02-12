
Setting up the MYAPP Web Services App
===========================================

Start with a standard Amazon AMI (Amazon Linux AMI)

Download the code
-----------------
First install the YUM components

    yum --enablerepo=epel install git nginx lighttpd python-pip gcc gcc-c++ \
        python-devel python-ipython-console atlas-devel libgfortran-devel \
        libquadmath-devel suitesparse-devel tbb-devel gcc-gfortran \
        python-virtualenv libpng-devel freetype-devel

Now upgrade the essential Python packages

    pip install -U futures greenlet eventlet trollius Flask WTForms flask-mongoengine gunicorn flask-cors

Now clone the git repo

    git clone https://github.com/digitizdat/MYAPP.git


Create the app directories
----------------------
    mkdir -p /opt/MYAPP/{etc,lib/MYAPP,log,var,img}
    touch /opt/MYAPP/log/{access,error,MYAPP}.log
    cd MYAPP
    cp etc/gunicorn.conf etc/mongo.cf /opt/MYAPP/etc/


Install the MYAPP WS app
----------------------
    cp py/__init__.py py/MYAPP*.py /opt/MYAPP/lib/MYAPP/
    cp py/controller.py /opt/MYAPP/lib/


Create the MYAPP user
----------------------
    groupadd MYAPP
    useradd -g MYAPP MYAPP


Set ownership on the /opt/MYAPP tree
-------------------------------------
    chown -R MYAPP:MYAPP /opt/MYAPP/{img,log,var}


Configure nginx
---------------
    cp -r etc/nginx /etc
    usermod -aG MYAPP nginx
    chkconfig nginx on
    service nginx start


Configure MYAPP DB access
--------------------------
    vi /opt/MYAPP/etc/mongo.cf


Test the MYAPP app config
--------------------------
    gunicorn --check-config -c /opt/MYAPP/etc/gunicorn.conf controller:app


Start the MYAPP app
--------------------
    gunicorn -c /opt/MYAPP/etc/gunicorn.conf controller:app

If when you check the process table you don't see it running, check the
/opt/MYAPP/log/error.log file.  You might want to comment out the
"daemon=True" parameter in /opt/MYAPP/etc/gunicorn.conf, and try again.  You
should be able to see the problem then.


Configure MongoDB
-----------------
If you haven't already done it, follow the instructions for installing MongoDB
by reading the mongodb/README.md file.


TROUBLESHOOTING
---------------
The main problem that might occur is: if you're not actually on an Amazon Linux
AMI (e.g. you're actually using Fedora), you might run into problems with nginx
trying to access the /opt/MYAPP/var/sock socket due to SELinux rules.
