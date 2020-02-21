# apitest

Tools:
- Choice of OS base, Ubuntu 18.x (no code is specific to this choice, however will need to use differing install syntax than provided in bascompins.sh)
- postgres (only because I have most recent familiarity)
- Flask (out of the box module, nothing fancy)
- psycopg module, for communication between python and postgres
- coding Python3


Implementation approach:
Flask connector, app and postgres db can be separated to enable differing testing scenario's over hosts. 


Main source provision:
- bascompins.sh for setup (see below)
- db.out; a full db dump to populated with expected database, tables and values
- restapi.py; Flask based rest api
- valuemod.py; 


To be completed:
Programatic logic for setting db isolation level, gone with ISOLATION_LEVEL_SERIALIZABLE as a catch all in all cases of x.
Need the logic to test for level and if fails to roll back transaction.

I ran tests with just enabling the isolation level and no logic, whilst better results, throws exceptions back at the user.


From bascompyins.sh setup script:

# * sudo -i -u postgres
# * psql -f db.out postgres	you might have to tweek location of db.out

# if running a remote DB, remember to change connect strings in the valuemod.py scripts
# also, will need to uncomment listen_addresses = '*' in /etc/postgresql/10/main/postgresql.conf
# and add IP's/CIDR netmask under IPv4 local connections as trust in /etc/postgresql/10/main/pg_hba.conf

To get things setup -
E
