# apitest

Tools:
- postgres
- Flask
- psycopg2 module
- coding Python3
* tested Ubuntu 18.x OS base, no code is specific to this choice, however will need to use differing install syntax than provided in bascompins.sh setup script.


Implementation approach:
* Flask connector, app and postgres db can be separated to enable differing testing scenario's over hosts. 
* Database extremely simple, just a pkey and the value stored
* psycopg2 module, to simplify coding between Python3 and postgres
* Attempted to utilise postgres SSI to avoid race conditions such as dirty reads etc, set isolation level to ISOLATION_LEVEL_SERIALIZABLE to catch most cases.


Main source provision:
- bascompins.sh for setup (see below)
- db.out; a full db dump populated with database, tables and values expected by the valuemod.py app
- restapi.py; Flask based rest api
- valuemod.py app; selects and updates using psycopg2 to postgres

Other scripts:
- resetval.py           resets the db value back to zero
- intsetval.py          set the initial db values, if not replaying the db.out dump during setup
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
* sudo -i -u postgres;
  - copy db.out to postgres user (if problems with access perms copy to /tmp and sudo chown postgres:postgres db.out)
  - play the dump into fresh postgres service (as above, psql -f db.out postgres)
  - IMPORTANT NOTE - if setting up the db without replaying the dump, ensure setting the initial value otherwise valuemod.py will error. You can use the intsetval.py to do this.
* if running app & db separate, ensure you alter the connection strings mentioned above.
* ensure restapi.py and valuemod.py are in the same location, both should be executable (chmod u+x)
* run ./restapi.py
* send a curl or connect via a browser to *localhost:5000/api/valinc
- Change *localhost to required IP when api is remote (see above)
- also /valcheck is a API call that can be run independently to confirm the current value count without incrementing it
