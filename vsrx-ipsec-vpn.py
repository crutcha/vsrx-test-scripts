from jnpr.junos import Device
from jnpr.junos.utils.config import Config

from temp_settings import host, username, password

#Local variables, will become YAML in Ansible playbook
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
    'tunnel_address': '169.254.14.202/30',
    'aws_bgp_as': '65000',
    'bgp_remote': '192.2.1.1',
    'local_as' : 65500
}

#Load device, bind config to object, open session
d = Device(host=host, user=username, password=password)
d.bind(config=Config)
d.open()

#load config and lock from edits
d.config.load(
    template_path='templates/aws_vpn.conf', 
    template_vars=vars,
    format='text'
    )
d.config.lock()

#commit check, commit, unlock
if d.config.commit_check():
    d.config.commit(timeout=300)
d.unlock()
