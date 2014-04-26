# PARFOR Utils.py:
#
# A collection of utilities. Bits and pieces we used
#
# This is proof-of-concept software. It was developed strictly to
# show how this might be done and as an aid to other development
# activities. It is not designed for actual use.
#
#
# REFERENCE:
#
# If you use this work, please add a reference to :
# Turnbull, B; Randhawa, Automated event and social network
# extraction from digital evidence sources with ontological
# mapping.
#
#
# LICENCE:
#
# ParFor is Copyright (C) 2013 Commonwealth of Australia.
#
# ParFor is licensed under the GNU General Public License version 3
# (#GPLv3) with extensions as allowed under clause 7 of GPLv3 to clarify
# issues of indemnity and liability.
#
# See ../COPYING file for full details.
#


"""
Unclassified.

A collection of utilities.

"""

import uuid
import subprocess
import Config
import re


def get_uuid(item):
    """
    Returns uuid
    """
    ret = item + str(uuid.uuid4())
    return ret


def call_process(command, options=None):
    '''
    Calls out to a process.
    Used for linux. 
    Returns response. 
    Options needs to be a list if it exists

    Be careful with the use of this - real use should be well contained
    because this is a potential security issue. If you use this in 
    production, wire it up to call only specific commands.
    '''

    '''
    perform basic integrity checking on allowable command.
    If you use this in production, add to this and to a more thorough
    process checking.
    '''
    allow_command = False
    for callable_command in Config.CALLABLE_COMMAND_LIST:
        return_obj = re.match(callable_command, command)
        if return_obj:
            allow_command = True

    if allow_command == False:
        return False

    if options:

        if len(options) == 1:
            proc = subprocess.Popen([command,
                                     options[0]],
                                    stdout=subprocess.PIPE,
                                    shell=True).communicate()[0]
        elif len(options) == 2:
            proc = subprocess.Popen([command,
                                     options[0],
                                     options[1]],
                                    stdout=subprocess.PIPE,
                                    shell=True).communicate()[0]
        elif len(options) == 2:
            proc = subprocess.Popen([command,
                                     options[0],
                                     options[1]],
                                    stdout=subprocess.PIPE,
                                    shell=True).communicate()[0]
        else:
            proc = subprocess.Popen([command],
                                    stdout=subprocess.PIPE,
                                    shell=True).communicate()[0]
    else:
        proc = subprocess.Popen([command],
                                stdout=subprocess.PIPE,
                                shell=True).communicate()[0]

    proc2 = proc.split("\n")
    return proc2
