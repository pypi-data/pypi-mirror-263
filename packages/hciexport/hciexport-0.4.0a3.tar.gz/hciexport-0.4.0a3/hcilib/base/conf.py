# The MIT License (MIT)
#
# Copyright (c) 2020-2024 Thorsten Simons (sw@snomis.eu)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
from configparser import ConfigParser
from time import asctime
from pathlib import Path

from hcilib.version import Gvars


def __readconfig(result):
    """
    Read the specified task from the config file.
    """
    conf = Path(result.configfile)
    if not conf.exists():
        template(conf)

    cnf = ConfigParser()
    cnf.read(conf)

    try:
        result.hcifqdn = cnf['HCI']['HCIFQDN']
        result.hciadminapiport = cnf['HCI']['ADMINAPIPORT']
        result.hcisearchapiport = cnf['HCI']['SEARCHAPIPORT']
        result.hciworkflowapiport = cnf['HCI']['WORKFLOWAPIPORT']
        result.user = cnf['HCI']['USER']
        result.password = cnf['HCI']['PASSWORD']
        result.realm = cnf['HCI']['REALM']
        result.granttype = cnf['HCI']['GRANTTYPE']
        result.clientsecret = cnf['HCI']['CLIENTSECRET']
        result.clientid = cnf['HCI']['CLIENTID']

        if 'task' in result:  # workflow/system config export
            result.type = result.task
            if not result.outfile:
                result.outfile = cnf[result.task]['OUTPUTFILE']
        else:  # recovery
            result.type = 'recovery'
    except KeyError as e:
        sys.exit(f'fatal: invalid configuration file - missing entry {e}')

    result.pkgname = 'HCI config package'
    result.pkgdesc = f'<p>exported: {asctime()}<br>by {Gvars.s_description} {Gvars.Version}</p>'

    return result

def template(file):
    """
    Create a configuration file template.
    """
    templ = ['[HCI]',
             '# The HCI\'s FQDN, like myhci.mydomain.com',
             'HCIFQDN = <HCI FQDN>',
             'ADMINAPIPORT = 8000',
             'SEARCHAPIPORT = 8888',
             'WORKFLOWAPIPORT = 8888',
             'USER = <user>',
             'PASSWORD = <password>',
             '# the REALM is either \'local\' for the built-in admin user or whatever',
             '# REALM was configured when integrating HCI with an external IDP',
             'REALM = <realm>',
             'GRANTTYPE = password',
             'CLIENTSECRET = hciexport',
             'CLIENTID = hciexport',
             '',
             '[system]',
             '# a default filename of your choice',
             'OUTPUTFILE = hciexport.system.package',
             '',
             '[workflows]',
             '# a default filename of your choice',
             'OUTPUTFILE = hciexport.workflow.bundle'
             ]

    print(f'configuration file {file} doesn\'t exist.')
    answer = input('Do you want to create a template configuration file? (y/n) ')
    if answer.lower() == 'y':
        with open(file, 'w') as ohdl:
            for line in templ:
                print(line, file=ohdl)
        sys.exit('template configuration file created successfully')
    else:
        sys.exit('no template configuration file created')
