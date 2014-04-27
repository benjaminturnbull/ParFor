# PARFOR SPARQLer:
#
# SPARQLer is a small python utility that is used to create
# a basic forward-chaining rule system. It will run queries and
# insert the results. It only stops when no new references are
# generated.
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
#
#
#
# USE:
#
# Make sure the Allegrograph Python client is on your path
# (see the sys.path.append below).
# Make changes to ../Config.py as necessary.
# Add rules to the SPARQLerRules area (order and subfolders don't matter).


import sys
import os
import imp
import re

sys.path.append('../agraph-4.11-client-python/src2')
sys.path.append('../')
sys.path.append('../ontology')

import Config
from Ontology import Ontology
ontology = Ontology()

from Session import Session
rdf_session = Session()


diskRe = re.compile(".*root disk (\d+),.*?(\d+).*? /dev(.*)")


def is_valid_sparql(query):
    '''
    Returns True if valid sparql.
    Returns false if not.
    TODO!
    '''
    print "TODO"
    # TODO
    return True

initialObjs = 0
orderOfService = []


def getModuleNames(directory):
    '''
    '''
    moduleList = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                fi = str(file)
                fi = fi[:fi.rfind(".")]
                moduleList.append([fi, directory + fi])

    return moduleList
#
# coming soon - decent plugins
#
# moduleNames = getModuleNames (Config.SPARQLER_PLUGINS)
# ingestionSources = []
#
# for mod in moduleNames:
#     vars()[mod[0]] = imp.load_source(mod[0],"./"+mod[1]+".py")
#
#     print mod[0]
#     info = vars()[mod[0]].onStart()
#
#     if info:
#         info["id"] = mod[0]
#         ingestionSources.append (info)
#
# if Config.DEBUG >0:
#     print "INFO: Ingestion Sources: " + str(ingestionSources)


# collect queries in order
for root, dirs, files in os.walk(Config.SPARQLER_RULES):

    print root
    files.sort()
    for file_input in files:
        f = open(root + "/" + file_input, "r")
        text = f.read()

        textLines = text.split("\n")

        rule = ""
        name = ""
        description = ""
        type = ""

        for txt in textLines:
            if len(txt) > 0:
                if txt[0] == "#" and txt.find("Description") > 0:
                    description = txt.replace(
                        "#", "").replace("Description:", "")
                elif txt[0] == "#" and txt.find("Name") > 0:
                    name = txt.replace("#", "").replace("Name:", "")
                elif txt[0] == "#" and txt.find("Type") > 0:
                    type = txt.replace("#", "").replace("Type:", "")
                elif txt[0] == "#":
                    pass
                else:
                    rule = rule + txt + "\n"
        meta_key = rdf_session.do_metadata()
        orderOfService.append([file_input, text, name, description, meta_key])

# Checks to make sure all the SPARQL rules are collected.
#
if Config.DEBUG > 0:
    print "SPARQLer Rules Collected:"
    for ob in orderOfService:
        print(ob[0] + "    :    " + ob[1].replace("\n", "")
              .replace("  ", "").replace("\t", ""))

currentObjs = rdf_session.store_sizes()[0]

# Execute each sparql rule over until the number of new objects
# doesn't change. Once the total of objects stabilises, then the
# loop breaks (as rules can inference each other).
#
while currentObjs - initialObjs > 0:
    initialObjs = currentObjs
    for queryObj in orderOfService:
        # if config print rule executuon
        if Config.DEBUG > 0:
            print "Executing query: " + queryObj[0]

        res = rdf_session.sparql_query(queryObj[1], False)
        # if config, print result
        if Config.DEBUG > 0:
            print ">>" + str(res)
        if res:
            for sub, pred, obj in res:
                # add assertion
                rdf_session.add_assertion([sub, pred, obj], queryObj[4], True)
                # commit assertion
                rdf_session.commit()
        resList = []
    currentObjs = rdf_session.store_sizes()[0]
    rdf_session.commit()
    currentObjs = rdf_session.store_sizes()[0]

    # check sizes - how many new assertions
    if Config.DEBUG > 0:
        print str(initialObjs)
        print str(currentObjs)
