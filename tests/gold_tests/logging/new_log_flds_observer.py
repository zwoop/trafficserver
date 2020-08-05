'''
Examines log generated by new_log_flds.test.py, returns 0 if valid, 1 if not.
'''
#  Licensed to the Apache Software Foundation (ASF) under one
#  or more contributor license agreements.  See the NOTICE file
#  distributed with this work for additional information
#  regarding copyright ownership.  The ASF licenses this file
#  to you under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License.  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import sys
import csv

ccid = []
ctid = []

# Read in log fields from each line of the generated report.
#
ln_num = 0
for ln in csv.reader(sys.stdin, delimiter=' '):
    ln_num += 1
    if len(ln) != 3:
        exit(code=1)
    i = int(ln[0])
    if i < 0:
        exit(code=1)
    ccid.append(i)
    i = int(ln[1])
    if i < 0:
        exit(code=1)
    ctid.append(i)
    if ln_num == 7:
        if ln[2] != "reallyreallyreallyreallylong.com":
            exit(code=1)
    else:
        if ln[2] != "-":
            exit(code=1)

# Validate contents of report.
#
if (ccid[0] != ccid[1] and
    ccid[1] != ccid[2] and
    ccid[2] == ccid[3] and
    ctid[2] != ctid[3] and
    ccid[3] != ccid[4] and
    ccid[4] == ccid[5] and
    ctid[4] != ctid[5] and
        ccid[5] != ccid[6]):
    exit(code=0)

# Failure exit if report was not valid.
#
exit(code=1)
