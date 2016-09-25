from jinja2 import Environment, FileSystemLoader

#Temp Variables
vars = {
    'aws_psk': 'psk',
    'aws_gateway': '1.1.1.1',
    'local_ike_gw': '2.2.2.2',
    'external_interface': 'fe-0/0/0',
    'p2_auth': 'hmac-sha-256-128',
    'p2_encryption': 'aes-256-cbc',
    'p2_lifetime': '3600',
    'tunnel_unit': '10',
    'security_zone': 'trust',
    'tunnel_address': '3.3.3.3'
}

#Render template
env = Environment(loader=FileSystemLoader(''))
template = env.get_template('aws_vpn.conf')
output_from_parsed_template = template.render(vars)
print(output_from_parsed_template)

#Save template to file
with open('aws_conf.txt', 'w') as fh:
    fh.write(output_from_parsed_template)
