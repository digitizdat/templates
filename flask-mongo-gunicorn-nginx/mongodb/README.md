mongodb directory
=================

This directory contains scripts and procedures needed to set up the MongoDB
instance.


Create this /etc/yum.repos.d/mongodb.repo file
----------------------------------------------
    [mongodb]
    name=MongoDB Repository
    baseurl=http://downloads-distro.mongodb.org/repo/redhat/os/x86_64/
    gpgcheck=0
    enabled=1


Install MongoDB
---------------

    yum --enablerepo=epel install -y rlwrap mongodb-org


Configure the /etc/mongod.conf file
-----------------------------------

You should see this output from this grep command:

    [root@ip-10-1-0-214 mongodb]# grep -Pv "^#|^\s*#|^$" /etc/mongod.conf 
    logpath=/var/log/mongodb/mongod.log
    logappend=true
    fork=true
    dbpath=/var/lib/mongo
    pidfilepath=/var/run/mongodb/mongod.pid
    cpu=true

*Note that the 'bind' parameter has been commented out to allow binding to all
interfaces.*

*Also note that auth is disabled for this prototype.*


Start the mongod process
------------------------

    # service mongod start


