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

from .recovery import ApiConBr
from ..base.calc import calcbytesize


def recoveryaction(opts):
    """
    Export of system configuration or workflows

    :param opts:  the cli parameters
    """
    con = ApiConBr(f'https://{opts.hcifqdn}:{opts.hciworkflowapiport}',
                   opts.granttype, opts.user, opts.password,
                   opts.clientsecret, opts.clientid, opts.realm)

    if opts.cmd == 'index':
        res = con.indexlist(opts.verbose)
        if not res:
            print('No indexes found')
        else:
            if opts.verbose:
                print(f'{"index":>20} | {"docs":>12} | {"size":>12} | {"IPL"} | {"shards"}')
                print(f'{"-"*20} + {"-"*12} + {"-"*12} + {"-"*3} + {"-"*6}')
                for idx in sorted(res):
                        print(f'{idx:>20} | {int(res[idx]["Document Count"]):>12} | '
                              f'{calcbytesize(int(res[idx]["Index Size (bytes)"])):>12} | '
                              f'{int(res[idx]["Index Protection Level"]):>3} | '
                              f'{int(res[idx]["Shard Count"]):>6}')
            else:
                print(f'{"idx":>20} | {"uuid"}')
                print(f'{"-"*20} + {"-"*36}')
                for idx in sorted(res):
                    print(f'{idx:>20} | {res[idx]["uuid"]}')

    elif opts.cmd == 'backup':
        if opts.backupcmd == 'list':
            res = con.backuplist(opts.index)
            if type(res) == str:
                print(res)
            elif res:
                print(f'backupId | start Timestamp')
                print(f'-------- + {"-"*24}')
                for x in sorted(res):
                    print(f'{int(x):>8} - {res[x]:24}')
        elif opts.backupcmd == 'start':
            res = con.backupstart(opts.index)
            print(res)
        elif opts.backupcmd == 'status':
            res = con.backupstatus(opts.index)
            print(f'{opts.index}: {res}')
        elif opts.backupcmd == 'delete':
            res = con.backupdelete(opts.index, opts.full_delete, opts.delete_all_but, opts.delete_id)
            print(f'{opts.index}: {res}')

    elif opts.cmd == 'restore':
        if opts.restorecmd == 'start':
            res = con.restorestart(opts.srcindex, opts.tgtindex, opts.backup_id)
            print(f'{opts.srcindex} ({opts.backup_id}) -> {opts.tgtindex}: {res}')
        elif opts.restorecmd == 'status':
            res = con.restorestatus(opts.tgtindex)
            print(f'{opts.tgtindex}: {res}')
