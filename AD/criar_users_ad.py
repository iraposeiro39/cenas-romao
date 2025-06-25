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
NEW_USER = "jorge.anacleto"
NEW_USER_DN = f"CN={NEW_USER},CN=Users,{BASE_DN}"
NEW_USER_PASSWORD = "User_!23"

try:
    # Conexao ao DC
    server = Server(DOMAIN_CONTROLLER, get_info=ALL)
    conn = Connection(server, user=ADMIN_USERNAME, password=ADMIN_PASSWORD, authentication=NTLM, auto_bind=True)

    # Adicionar user
    conn.add(
        dn=NEW_USER_DN,
        object_class=['top', 'person', 'organizationalPerson', 'user'],
        attributes={
            'cn': NEW_USER,
            'givenName': 'Jorge',
            'sn': 'Anacleto',
            'displayName': 'Jorge Anacleto',
            'userPrincipalName': f'{NEW_USER}@{DOMAIN_NAME}',
            'samAccountName': NEW_USER,
            'userAccountControl': 544,
        },
    )

    # Verificar se o user foi criado com sucesso
    if conn.result['result'] == 0:
        print("User criado com sucesso!")
        # Adicionar a pass ao user
        conn.extend.microsoft.modify_password(NEW_USER_DN, NEW_USER_PASSWORD)
        conn.modify(NEW_USER_DN,{'pwdLastSet': [(MODIFY_REPLACE, ['0'])]})
        print("A pass foi alterada!")

    # Senão...
    else:
        print('Ardeu a criar o user!')

    conn.unbind()

except Exception as e:
    print(f"ERROR: {e}")
    pass
