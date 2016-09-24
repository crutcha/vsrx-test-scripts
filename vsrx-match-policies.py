from jnpr.junos import Device
from lxml import etree
from pprint import pprint

from temp_settings import host, username, password

session = Device(host=host, user=username, password=password)
session.open()

#Check if already allowed by policy
matched_policy = session.rpc.match_firewall_policies(
    from_zone = 'trust',
    to_zone = 'untrust',
    source_ip = '192.168.10.1',
    destination_ip = '8.8.8.8',
    source_port = '1',
    destination_port = '80',
    protocol = 'tcp',
    )

#Verify action defined in RPC reply
action = matched_policy.find('policy-information/policy-action/action-type')

if not action == None:
    policy = {
        'name': matched_policy.find('policy-information/policy-name').text,
        'source': [a.text 
                    for a in 
                    matched_policy.findall('policy-information/source-addresses/source-address/address-name')
        ],
        'dest': [d.text
                    for d in
                    matched_policy.findall('policy-information/destination-addresses/destination-address/address-name')
        ],
        'app': [a.text
                    for a in
                    matched_policy.findall('policy-information/applications/application/application-name')
        ]
    }

    if action.text == 'permit':
        print('Allowed by policy: {}'.format(policy))

    elif action.text == 'deny':
        print('Denied by policy: {}'.format(policy))

else:
    print('no matching policy was found.')
    


session.close()
