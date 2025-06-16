#!/bin/python3
### Conexao com o server AD
# Modulos 
from ldap3 import Server, Connection, ALL, NTLM, MODIFY_REPLACE
from ldap3.core.exceptions import LDAPException

# Configuration
DOMAIN_NAME = "ciseg.internal"
DOMAIN_CONTROLLER = "dc.ciseg.internal"
ADMIN_USERNAME = "ciseg\\Administrator"
ADMIN_PASSWORD = "User_!23"
BASE_DN = "DC=ciseg,DC=internal"
NEW_USER = "rogelio.rodrigues"
NEW_USER_DN = f"CN={NEW_USER},CN=Users,{BASE_DN}"
NEW_USER_PASSWORD = "User_!23"

try:
    # Conexao ao DC
    server = Server(DOMAIN_CONTROLLER, get_info=ALL)
    conn = Connection(server, user=ADMIN_USERNAME, password=ADMIN_PASSWORD, authentication=NTLM, auto_bind=True)

except:
    pass
