
#-----------------------------------------------------------
# 09.02.2018, Jeff Carrell
#
# filename = demo01-netmiko-telnet-show-ver_sample.py
#
# this is a sample script, using netmiko to telnet comm to a
#  single switch, to run a single command.
#
# see notes for each section and replace variable with
#  appropriate value.
#
# no warranty given or implied
#
# DO NOT execute scripts on a network without proper
# authorization and following established change
# management processes.
# ---------------------------------------------------------



from netmiko import ConnectHandler

switch = {
    'device_type': '<switch-brand>',                  # see notes below
    'ip': '<ip-address>',                             # see notes below
    'username': '<switch-username>',                  # see notes below
    'password': '<switch-password>',                  # see notes below 
}

net_connect = ConnectHandler(**switch)
output = net_connect.send_command("show version")     # see notes below

print(output)



#
#-----------------------------------------------------------
# substitute '<switch-brand>' for netmiko device descriptor, 
#   see netmiko docs for supported list
#  example for lab: Cisco 3850/3750/3560/2970/2811 =  'cisco_ios_telnet'
#  example for lab: Aruba 3800/3810/8400 =  'hp_procurve_telnet'
#  example for lab: HPE 5500/5900/5940 = 'hp_comware_telnet'
#-----------------------------------------------------------
# 
#-----------------------------------------------------------
# substitute '<ip-address>' for switch ip address, for lab:
#   Cisco 3850  = 10.1.1.201
#   Cisco 3750  = 10.1.1.202 
#   Cisco 2970  = 10.1.1.203   # note 2970 only supports telnet
#   Cisco IOSv  = 10.1.1.204
#   Cisco NXOS  = 10.1.1.205
#   Cisco 2811  = 10.1.1.206
#   Aruba 3810  = 10.1.1.211
#   Aruba 3800  = 10.1.1.212
#   Aruba 8400  = 10.1.1.213   # note 8400 only supports SSH
#   HPE   5900  = 10.1.1.222
#   HPE   5940  = 10.1.1.223
#   HPE VSR1000 = 10.1.1.224
#-----------------------------------------------------------
#
#-----------------------------------------------------------
# substitute '<switch-username>' for switch login name,     for lab = 'manager'
# substitute '<switch-password>' for switch login password, for lab = 'password'
#-----------------------------------------------------------
#
#-----------------------------------------------------------
# fyi, if accessing HPE 5500/5900/5940, use "display version"
#         instead of "show version"
#-----------------------------------------------------------
#