# Getting started with Network Automation using Python 

## Local Workstation Setup
Be sure to complete Lesson 1 - Basic Python Tools Setup instructions from [Beau Williamson's March 2018 presentation](http://dfw.cisco-users.org/zips/20180307-Python_Workshop.pdf) before coming to the session. There is no guest Internet access at the facility, so you will want to have everything installed and ready to run.  

#### In addition, the following Python module/library add-on's need to be installed before attending the session:

- [ ] netmiko

- [ ] requests

- [ ] pprint




You can use the following command to install each package (assumes Python 3.6):  

```bash
py -3.6 -m pip install SomePackage
```



You can use the following command to verify the new packages were installed (assumes Python 3.6 is only installed version):  

```bash
python -m pip list
```

Output should look similar to this:  (maybe not exactly)

```
C:\>python -m pip list
asn1crypto (0.24.0)
bcrypt (3.1.4)
certifi (2018.8.24)
cffi (1.11.5)
cryptography (2.3.1)
idna (2.7)
netmiko (2.2.2)
paramiko (2.4.1)
pip (9.0.1)
pyasn1 (0.4.2)
pycparser (2.18)
PyNaCl (1.2.1)
pyserial (3.4)
PyYAML (3.13)
requests (2.19.1)
scp (0.11.0)
setuptools (28.8.0)
six (1.11.0)
textfsm (0.4.1)
urllib3 (1.23)
```

------

## Sample configuration files

There are sample configuration files available. One for ssh access and one for telnet access.

------

rev 09022018-0800