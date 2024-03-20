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
from typing import List, Dict

from hcilib.base.combase import ApiConBase, printstep


class ApiConBr(ApiConBase):
    """
    Connection class to deal with Index backup/restore operations
    """
    def __init__(self, *args, **kwargs):
        """
        param hci:  the HCIs FQDN
        """
        super().__init__(*args, **kwargs)

    def indexlist(self, verbose: bool) -> Dict:
        """
        Get a list of Indexes from HCI.

        :param verbose:  if True, add index statistics
        :returns:        a dict of Indexes
        """
        r = self.client.get(f'/api/workflow/indexes')

        # indexes = {'myindex': {'UUID': 'uuid', 'size': 0}}
        indexes = {}
        if r.status_code == 200:
            for idx in r.json():
                indexes[idx['name']] = {'uuid': idx['uuid'],
                                        'plugin': idx['pluginDisplayName']}
        else:
            sys.exit(f'fatal: failed getting the index list - http {r.status_code}')

        if verbose:
            for i in indexes:
                r = self.client.get(f'/api/workflow/indexes/{indexes[i]["uuid"]}/statistics')
                if r.status_code == 200:
                    for entry in r.json():
                        indexes[i][entry['name']] = entry['value']
                else:
                    return f'fatal: failed getting the index statistics of "{i}" - http {r.status_code}'

        return indexes

    def backupstart(self, indexname: str):
        """
        Start an index backup.
        """
        r = self.client.post(f'/api/workflow/recovery/backup/indexes/{indexname}/start')
        if r.status_code == 201:
            return f'Backup of "{indexname}" started'
        else:
            return f'fatal: failed to start a backup of "{indexname}"- http {r.status_code}'


    def backupstatus(self, indexname: str) -> str:
        """
        Get the status of an index backup.

        :param indexname:  the index's name
        :return:           a status string
        """
        r = self.client.get(f'/api/workflow/recovery/backup/indexes/{indexname}/status')
        if r.status_code == 200:
            return r.json()["state"]
        else:
            return f'fatal: failed getting the backup status of "{indexname}" - http {r.status_code}'

    def backuplist(self, indexname: str):
        """
        List index backups.
        """
        r = self.client.get(f'/api/workflow/recovery/backup/indexes/{indexname}/list')

        backups = {}
        if r.status_code == 200:
            res = r.json()
            for bk in res['backups']:
                backups[bk['backupId']] = bk['startTime']
            return backups
        else:
            return f'fatal: failed getting the backup list of "{indexname}" - http {r.status_code}'

    def backupdelete(self, indexname: str, full_delete: bool, delete_all_but: int, delete_id: int):
        """
        Delete an index backup or parts of it.
        """
        if full_delete:
            body = {'deleteAllBackups': full_delete}
        elif delete_all_but:
            body = {'maxNumBackups': delete_all_but}
        elif delete_id > -1:
            body = {'backupId': delete_id}
        else:
            return 'error: invalid parameters'

        r = self.client.post(f'/api/workflow/recovery/backup/indexes/{indexname}/delete', json=body)
        if r.status_code == 200:
            return f'delete ({body}) successful'
        else:
            return f'fatal: delete ({body}) failed - http {r.status_code}'

    def restorestart(self, srcindexname: str, tgtindexname: str, backup_id: int=-1) -> str:
        """
        Start an index restore.
        """
        body = {'sourceIndexName': srcindexname,
                'destinationIndexName': tgtindexname,
                'backupId': backup_id}
        r = self.client.post(f'/api/workflow/recovery/restore/indexes/start', json=body)
        if r.status_code == 201:
            return f'restore started'
        else:
            return f'fatal: restore failed - http {r.status_code}'

    def restorestatus(self, tgtindexname: str):
        """
        Get the status of an index restore.
        """
        r = self.client.get(f'/api/workflow/recovery/restore/indexes/{tgtindexname}/status')
        if r.status_code == 200:
            return r.json()["state"]
        else:
            return f'fatal: restore status failed" - http {r.status_code}'



