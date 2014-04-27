# PARFOR Data ingestion - Computers and disks
#
# Pulls in Computers, Disks and Partitions from a given file. Add them to RDF.
# The file format is in limbo. An example is shown but
# we will probably move it into a format that can be easily
# converted to json.
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
# LICENCE
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


import os
import re
import sys
sys.path.append('../')
sys.path.append('../ontology')
import Utils

sys.path.append('../agraph-4.11-client-python/src2')

from Ontology import Ontology
ontology = Ontology()

from Session import Session

rdf_session = Session()

REGEX_DISK = re.compile(
    ".*root disk (\d+),.*?(\d+).*? /dev(.*)")
REGEX_DISK_MOUNT_DETAIL = re.compile(".? type (.?) .*")


fileInput = "computerinput.txt"

INPUTOBJURI = ""
INPUTOBJNAME = "DataIngestor"
INPUTDATETIME = ""
INFERENCE = 0


def process_input_file(file_input):

    currentComputer = None
    currentComputerDict = {}
    currentDisk = None
    currentDiskDict = {}

    meta_key = rdf_session.do_metadata()

    fileByLine = file_input.split("\n")

    for line in fileByLine:
        fileList = line.split("\t")

        if len(fileList) == 1:
            if len(fileList[0]) > 0:
                if fileList[0][0] == "#":
                    # comment line
                    pass
                else:
                    # not a comment line.
                    currentComputer = fileList[0]
                    ida = ontology.instance.ns + Utils.get_uuid("COMP_")
                    currentComputerDict[currentComputer] = ida
                    rdf_session.add_assertion(
                        [ida,
                         ontology.rdf.type,
                         ontology.fs.Computer],
                        meta_key)
                    rdf_session.add_assertion(
                        [ida,
                         ontology.base.name,
                         currentComputer],
                        meta_key,
                        literal=True)

        elif len(fileList) == 2:
            if len(fileList[1]) > 0:
                currentDisk = fileList[1]
                ida = ontology.instance.ns + Utils.get_uuid("DISK_")
                currentDiskDict[currentDisk] = ida
                rdf_session.add_assertion(
                    [ida,
                     ontology.rdf.type,
                     ontology.fs.Disk],
                    meta_key)
                rdf_session.add_assertion(
                    [currentComputerDict[currentComputer],
                     ontology.fs.contains,
                     ida],
                    meta_key
                )
                rdf_session.add_assertion(
                    [ida,
                     ontology.base.name,
                     currentDisk],
                    meta_key,
                    literal=True)

        elif len(fileList) == 4 and currentComputer != None and currentDisk != None:
            if len(fileList[2]) > 0 and len(fileList[2]) > 0:

                partitionName = fileList[2]
                partitionMount = fileList[3]

                ida = ontology.instance.ns + Utils.get_uuid("PARTITION_")
                rdf_session.add_assertion(
                    [ida,
                     ontology.rdf.type,
                     ontology.fs.Partition],
                    meta_key)
                rdf_session.add_assertion(
                    [currentDiskDict[currentDisk],
                     ontology.fs.contains,
                     ida],
                    meta_key)
                rdf_session.add_assertion(
                    [ida,
                     ontology.base.name,
                     partitionName],
                    meta_key,
                    literal=True)
                rdf_session.add_assertion(
                    [ida,
                     ontology.base.mountPoint,
                     partitionMount],
                    meta_key,
                    literal=True)

                mountDetails = Utils.call_process("mount " + partitionMount)
                if mountDetails[0].find("type ") > 0:
#                    mountDiskDetaileRe = re.compile(".? type (.?) .*")

                    reMatch = REGEX_DISK_MOUNT_DETAIL.match(mountDetails)
                    if reMatch:
                        detail = reMatch.group(1)

                        query = "select ?s where {?s <" + \
                            ontology.base.name + "> \"" + detail + "> .}"
                        detail_obj = rdf_session.singleResponseQuery(query)
                        if detail_obj:
                            rdf_session.add_assertion(
                                [id,
                                 ontology.fs.fileSystemFormat,
                                 detail_obj],
                                meta_key)

    rdf_session.commit()
    print rdf_session.store_sizes()


def get_reasoner(reasoner_name):

    reasoner_id = ""

    get_reasoner_query = """
    select ?s where {
        ?s <""" + ontology.base.name + """> \"""" + reasoner_name + """\" .
        ?s rdf:type <""" + ontology.metadata.Reasoner + """> .
    }"""

    res2 = rdf_session.single_resp_query(get_reasoner_query, True)
    if res2:
        reasoner_id = res2

    else:
        key = ontology.metadata.ns + Utils.get_uuid("metadata_")
        rdf_session.make_triple(
            [key,
             ontology.rdf.type,
             ontology.metadata.Reasoner],
            meta_repo=True)
        rdf_session.make_triple(
            [key,
             ontology.base.name,
             INPUTOBJNAME],
            literal=True,
            meta_repo=True)
        reasoner_id = key

    print reasoner_id
    return reasoner_id


if __name__ == "__main__":

    #global INPUTOBJURI
    INPUTOBJURI = get_reasoner(INPUTOBJNAME)
    rdf_session.set_metadata_properties(INPUTOBJNAME, INPUTOBJURI, 0, "date")

    fil = open(fileInput, "r")
    FIL_TEXT = fil.read()
    process_input_file(FIL_TEXT)

    rdf_session.commit()
    print rdf_session.store_sizes()
