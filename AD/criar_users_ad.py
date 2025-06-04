#!/bin/python3
### Conexao com o server AD
#
# FALTA CENAS QUE NÃO PASSEI, BE CAREFUL
#

# Modulos 
from ldap3 import Server, Connection, ALL, NTLM, MODIFY_REPLACE
from ldap3.core.exceptions import LDA

# Configuration
DOMAIN_NAME = "ciseg.internal"
DOMAIN_CONTROLLER = ""
ADMIN_USERNAME = ""
ADMIN_PASSWORD = ""
BASE_DN = ""
NEW_USER = "rogelio.rodrigues"
NEW_USER_DN = f"CN={NEW_USER},CN=Users,{BASE_DN}"
NEW_USER_PASSWORD = "User_!23"

try:
    # Conexao ao DC
    server = Server(DOMAIN_CONTROLLER, get_info=ALL)
    conn = Connection(server, user=ADMIN_USERNAME, password=ADMIN_PASSWORD, authentication=NTLM, auto_bind=True)

except:
    pass
