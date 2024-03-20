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
import argparse
import sys
from argparse import ArgumentParser

from hcilib.version import Gvars
from hcilib.base.conf import __readconfig

def parseargs():
    """
    args - build the argument parser, parse the command line.
    """

    # mp = mainparser
    mp = ArgumentParser()
    mp.add_argument('--version', action='version',
                    version=f"%(prog)s: {Gvars.Version}\n")
    mp.add_argument('-C', dest='configfile',
                    required=True,
                    help='configuration file')

    # sp = 1st level subparsers
    sp = mp.add_subparsers(dest='cmd',
                           title='commands')

    # export subparser
    exparser = sp.add_parser('export',
                             help='export system configuration or workflow bundle')

    exparser.add_argument('-o', dest='outfile',
                            required=False,
                            default='',
                            help='the file to write the export to '
                                 '(set default in config file)')

    exparser.add_argument(dest='task',
                          choices=['system', 'workflows'],
                          help='the task within the config file')

    # indexes subparser
    ixparser = sp.add_parser('index',
                             help='list indexes')

    ixparser.add_argument('-v', dest='verbose',
                          action='store_true',
                          help='verbose, include index statistics')

    # backup subparser
    bkparser = sp.add_parser('backup',
                             help='index backup functions')

    # 2nd level backup parser
    sp2b = bkparser.add_subparsers(dest='backupcmd',
                                   title='backup subcommands',
                                   # description='valid subcommands'
                                   )

    startparser = sp2b.add_parser('start',
                                  help='start a backup')
    startparser.add_argument(dest='index',
                             help='the index name')

    statusparser = sp2b.add_parser('status',
                                   help='get backup status')
    statusparser.add_argument(dest='index',
                              default='',
                              help='the index name')

    listparser = sp2b.add_parser('list',
                                 help='list backups')
    listparser.add_argument(dest='index',
                            default='',
                            help='the index name')

    deleteparser = sp2b.add_parser('delete',
                                   help='delete backups')
    deleteparser.add_argument(dest='index',
                              default='',
                              help='the index name')

    # these three options only apply to the delete action:
    deleteparser.add_argument('--full_delete', dest='full_delete',
                              action='store_true',
                              help='delete all backups for index')
    deleteparser.add_argument('--delete_all_but', dest='delete_all_but',
                              metavar='<count>',
                              type=int,
                              default=0,
                              help='delete all backups except the <count> latest')
    deleteparser.add_argument('--delete_id', dest='delete_id',
                              metavar='<id>',
                              type=int,
                              default=-1,
                              help='delete a backup with a specific <id>')

    # restore subparser
    reparser = sp.add_parser('restore',
                             help='restore an index')

    # 2nd level restore parser
    sp2r = reparser.add_subparsers(dest='restorecmd',
                                   title='restore subcommands',
                                   )

    rstartparser = sp2r.add_parser('start',
                                  help='start a restore')
    rstartparser.add_argument(dest='srcindex',
                              help='the restore source index name')
    rstartparser.add_argument(dest='tgtindex',
                              help='the restore target index name')
    rstartparser.add_argument(dest='backup_id',
                              metavar='<id>',
                              type=int,
                              default=-1,
                              help='restore a backup with a specific <id> (-1 is the latest)')

    rstatusparser = sp2r.add_parser('status',
                                  help='get restore status')
    rstatusparser.add_argument(dest='tgtindex',
                               help='the restore target index name')

    result = mp.parse_args()

    if not result.cmd:
        print('Fatal: I have no idea what you want me to do...', file=sys.stderr)
        sys.exit(2)

    if result.cmd == 'backup' and not result.backupcmd:
        print('Fatal: "backup" needs a subcommand - {start, status, list, delete}', file=sys.stderr)
        sys.exit(2)
    if result.cmd == 'restore' and not result.restorecmd:
        print('Fatal: "restore" needs a subcommand - {start, status}', file=sys.stderr)
        sys.exit(2)

    if result.cmd == 'backup':
        if result.backupcmd == 'delete':
            dels = 0
            if result.full_delete:
                dels += 1
            if result.delete_all_but:
                dels += 1
            if result.delete_id > -1:
                dels += 1
            if not dels:
                print('Fatal: missing information about what to delete', file=sys.stderr)
                sys.exit(2)
            elif dels > 1:
                print('Fatal: just one of the delete options is allowed', file=sys.stderr)
                sys.exit(2)

    return __readconfig(result)
