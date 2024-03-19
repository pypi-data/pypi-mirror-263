from extras.plugins import PluginConfig

class NetBoxGrassConfig(PluginConfig):
    name = 'netbox_grass'
    verbose_name = ' NetBox Grass'
    description = 'Back up Configuration of Network Devices in NetBox'
    version = '0.1'
    base_url = 'grass'

config = NetBoxGrassConfig