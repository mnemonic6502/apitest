# apitest

Tools:
- Choice of OS base, Ubuntu 18.x (no code is specific to this choice, however will need to use differing install syntax than provided in bascompins.sh)
- postgres
- Flask
- psycopg2 module
- coding Python3


Implementation approach:
* Flask connector, app and postgres db can be separated to enable differing testing scenario's over hosts. 
* Database extremely simple, just a pkey and the value stored
* psycopg2 module, to simplify coding between Python3 and postgres
* Attempted to utilise postgres SSI to avoid race conditions such as dirty reads etc, set isolation level to ISOLATION_LEVEL_SERIALIZABLE to catch most cases.


Main source provision:
- bascompins.sh for setup (see below)
- db.out; a full db dump to populated with expected database, tables and values
- restapi.py; Flask based rest api
- valuemod.py; 

Other scripts:
- resetval.py           resets the db value back to zero
- testapp1statment.sh   simple loop that logs a number of value increments to a file, useful for testing curls to the api from more than one host


To be completed:
Programatic logic for setting db isolation level, gone with ISOLATION_LEVEL_SERIALIZABLE as a catch all in all cases of x.
Need the logic to test for level and if fails to roll back transaction.

I ran tests with just enabling the isolation level and no logic, whilst better results, throws exceptions back at the user.


From bascompyins.sh setup script:

* sudo -i -u postgres
* psql -f db.out postgres

If you want the api accessible to a remote end point, remember to change app_run connect strings in the valuemod.py scripts; by default is set to localhost, app.run(). Change like this app.run(host='172.31.35.119')
Also, is segmenting the api from the db localtion, will need to uncomment listen_addresses = '*' in /etc/postgresql/10/main/postgresql.conf and add IP's/CIDR netmask under IPv4 local connections as trust in /etc/postgresql/10/main/pg_hba.conf, with IP(s) of the restapp.

To get things setup -
If using the installer script, ensure an Ubuntu based distro (tested Xubuntu 18.x)
Ensure your user has sudo access to install, NOPASSWD in sudoers will make this easier...
* run bascompyins.sh
* sudo -i -u postgres, copy db.out to postgres user, play the dump into fresh postgres service
* if running app & db separate, ensure you alter the connection strings mentioned above.
* ensure restapi.py and valuemod.py are in the same location, both should be executable (chmod u+x)
* run ./restapi.py
* send a curl or connect via a browser to *localhost:5000/api/valinc
- Change *localhost to required IP when api is remote (see above)
- also /valcheck is a API call that can be run independently to confirm the current value count without incrementing it
