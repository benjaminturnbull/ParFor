# PARFOR Data ingestion - file systems, directories and files
#
# Pulls in file systems, directories and files from an RDF
# representation and back in again. Requires that computers and
# associated disks are already inputted.
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
import sys
sys.path.append('../')
sys.path.append('../ontology')

import Utils
import Config
sys.path.append('../agraph-4.11-client-python/src2')

from Ontology import Ontology
ontology = Ontology()

from Session import Session

rdf_session = Session()

INPUTOBJURI = ""
INPUTOBJNAME = "DataIngestor-Files"
INPUTDATETIME = ""
INFERENCE = 0

object_counter = 0
maxobject_counter = 0


def find_dir(path, diskid):
    """
    Finds existing directories 
    """

    contain_q = """
    select ?s where 
    {
    ?s rdf:type fs:Directory .
    ?s fs:path \"""" + path.replace ("//", "/") + """\" .
    <""" + diskid + """> fs:contains ?s
    }    
    """
    resp = rdf_session.single_resp_query(contain_q)
    if resp:
        return resp
    else:
        return None


#
# TODO this needs to be removed. It's a terrible hack. Filenames need to
# be handled better.
# proof of concept, etc.
def removeNonAscii(s):
    return "".join(filter(lambda x: ord(x) < 128, s))


#
#
#
def process_file(root,
                 basedirectory,
                 file_in,
                 onto_base):
    """
    Processes file for the following assertions:
    - base.name
    - fs.path
    - fs.size
    - fs.inode
    - fs.mtime
    - fs.atime
    - fs.ctime
    - fs.ownerAccount
    - fs.ownerGroup
    - fs.isInvisible
    - fs.contains
    """
    id = ontology.instance.ns + Utils.get_uuid("FILE_")
    meta_key = rdf_session.do_metadata()

    rdf_session.add_assertion(
        [id,
         ontology.rdf.type,
         ontology.fs.File],
        meta_key)

    file_in_name = file_in
    #file_in_name = str(file_in).decode('unicode_escape')
#    file_in_name = file_in_name.encode('utf-8')
    file_in_name = file_in_name.encode('unicode-escape')
    file_in_name = removeNonAscii(file_in_name)

#    print "%"
#    print file_in
#    print file_in_name

    rdf_session.add_assertion(
        [id,
         ontology.base.name,
         file_in_name],
        meta_key,
        True)

    file_in_folderpath = str(root)[len(basedirectory) - 1:]
    path = str(file_in_folderpath + "/" +
               str(file_in_name)).replace("//", "/")
    rdf_session.add_assertion(
        [id,
         ontology.fs.path,
         path],
        meta_key,
        True)

#    meta_inf = os.stat(str(root)+"/"+str(file_in))
    meta_inf = os.stat(str(root) + "/" + file_in)
    tmp_size = meta_inf.st_size
    if tmp_size:
        rdf_session.add_assertion(
            [id,
             ontology.fs.size,
             tmp_size],
            meta_key,
            True)

    tmp_inode = meta_inf.st_ino
    if tmp_inode:
        rdf_session.add_assertion(
            [id,
             ontology.fs.inode,
             tmp_inode],
            meta_key,
            True)
    tmp_mtime = meta_inf.st_mtime
    if tmp_mtime:
        rdf_session.add_assertion(
            [id,
             ontology.fs.mtime,
             tmp_mtime],
            meta_key,
            True)
    tmp_atime = meta_inf.st_atime
    if tmp_atime:
        rdf_session.add_assertion(
            [id,
             ontology.fs.atime,
             tmp_atime],
            meta_key,
            True)
    tmp_ctime = meta_inf.st_ctime
    if tmp_ctime:
        rdf_session.add_assertion(
            [id,
             ontology.fs.ctime,
             tmp_ctime],
            meta_key,
            True)
    tmp_uid = meta_inf.st_uid
    if tmp_uid:
        rdf_session.add_assertion(
            [id,
             ontology.fs.ownerAccount,
             tmp_uid],
            meta_key,
            True)
    tmp_gid = meta_inf.st_gid
    if tmp_gid:
        rdf_session.add_assertion(
            [id,
             ontology.fs.ownerGroup,
             tmp_gid],
            meta_key,
            True)
    if file_in_name[0] == ".":
        rdf_session.add_assertion(
            [id,
             ontology.fsdetail.isInvisible,
             True],
            meta_key,
            True)

#    else:
#        rdf_session.add_assertion (
#                                   [id,
#                                    ontology.fs.visible,
#                                    False],
#                                   meta_key,
#                                   True)

    rdf_session.add_assertion(
        [onto_base,
         ontology.fs.contains,
         id],
        meta_key,
        False)

    tmp_contains = find_dir(file_in_folderpath, onto_base)
    if not tmp_contains:
        tmp_contains = onto_base
    else:
        tmp_contains = tmp_contains["s"]
        tmp_contains = tmp_contains["value"]

    rdf_session.add_assertion(
        [tmp_contains,
         ontology.fs.contains,
         id],
        meta_key,
        False)
    rdf_session.commit()


def process_dir(root,
                basedirectory,
                dir_in,
                onto_base):
    """
    Processes directory for the following assertions:
    - base.name
    - fs.path
    - fs.size
    - fs.inode
    - fs.mtime
    - fs.atime
    - fs.ctime
    - fs.ownerAccount
    - fs.ownerGroup
    - fs.isInvisible
    - fs.contains
    """
    id = ontology.instance.ns + Utils.get_uuid("DIR_")
    meta_key = rdf_session.do_metadata()

    rdf_session.add_assertion(
        [id,
         ontology.rdf.type,
         ontology.fs.Directory],
        meta_key)

    dir_in_name = dir_in
    dir_in_name = dir_in_name.encode('unicode-escape')

    rdf_session.add_assertion(
        [id,
         ontology.base.name,
         dir_in_name],
        meta_key,
        True)

    file_in_folderpath = str(root)[len(basedirectory) - 1:]
    path = str(file_in_folderpath + "/" + str(dir_in_name)).replace("//", "/")
    rdf_session.add_assertion(
        [id,
         ontology.fs.path,
         path],
        meta_key,
        True)

#    meta_inf = os.stat(str(root)+"/"+str(file_in))
    meta_inf = os.stat(str(root) + "/" + dir_in)
    tmp_size = meta_inf.st_size
    if tmp_size:
        rdf_session.add_assertion(
            [id,
             ontology.fs.size,
             tmp_size],
            meta_key,
            True)
    tmp_inode = meta_inf.st_ino
    if tmp_inode:
        rdf_session.add_assertion(
            [id,
             ontology.fs.inode,
             tmp_inode],
            meta_key,
            True)
    tmp_mtime = meta_inf.st_mtime
    if tmp_mtime:
        rdf_session.add_assertion(
            [id,
             ontology.fs.mtime,
             tmp_mtime],
            meta_key,
            True)
    tmp_atime = meta_inf.st_atime
    if tmp_atime:
        rdf_session.add_assertion(
            [id,
             ontology.fs.atime,
             tmp_atime],
            meta_key,
            True)
    tmp_ctime = meta_inf.st_ctime
    if tmp_ctime:
        rdf_session.add_assertion(
            [id,
             ontology.fs.ctime,
             tmp_ctime],
            meta_key,
            True)
    tmp_uid = meta_inf.st_uid
    if tmp_uid:
        rdf_session.add_assertion(
            [id,
             ontology.fs.ownerAccount,
             tmp_uid],
            meta_key,
            True)
    tmp_gid = meta_inf.st_gid
    if tmp_gid:
        rdf_session.add_assertion(
            [id,
             ontology.fs.ownerGroup,
             tmp_gid],
            meta_key,
            True)
    if dir_in_name[0] == ".":
        rdf_session.add_assertion(
            [id,
             ontology.fsdetail.isInvisible,
             True],
            meta_key,
            True)

#    else:
#        rdf_session.add_assertion (
#                                   [id,
#                                    ontology.fs.visible,
#                                    False],
#                                   meta_key,
#                                   True)


    tmp_contains = find_dir(file_in_folderpath, onto_base)
    if not tmp_contains:
        tmp_contains = onto_base
    else:
        tmp_contains = tmp_contains["s"]
        tmp_contains = tmp_contains["value"]

    rdf_session.add_assertion(
        [tmp_contains,
         ontology.fs.contains,
         id],
        meta_key,
        False)

    rdf_session.add_assertion(
        [onto_base,
         ontology.fs.contains,
         id],
        meta_key,
        False)

    rdf_session.commit()


def process_file_system(basedirectory, onto_name):

    filesOut = []
    directoriesOut = []
    global object_counter
    global maxobject_counter

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # process root directory
    for root, dirs, files in os.walk(basedirectory):
        for dir in dirs:
            proc_dir = process_dir(root,
                                   basedirectory,
                                   dir,
                                   onto_name)
            object_counter = object_counter + 1
#            if object_counter > maxobject_counter:
#                session.commit()
#                object_counter = 0
            rdf_session.commit()

    rdf_session.commit()

    for root, dirs, files in os.walk(basedirectory):

        for file in files:
            processedObj = process_file(root,
                                        basedirectory,
                                        file,
                                        onto_name)
            object_counter = object_counter + 1
#            if Config.DEBUG >0:
#                filesOut = filesOut+processedObj

            if object_counter > maxobject_counter:
                rdf_session.commit()
                object_counter = 0
    rdf_session.commit()

    if Config.DEBUG > 0:
        print "##############################"
        print(basedirectory)
        print(filesOut)

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
    return reasoner_id

#    fil = open( fileInput, "r")
#    FIL_TEXT = fil.read()
#    process_input_file (FIL_TEXT)
    rdf_session.commit()



if __name__ == "__main__":

    INPUTOBJURI = get_reasoner(INPUTOBJNAME)
    rdf_session.set_metadata_properties(INPUTOBJNAME, INPUTOBJURI, 0, "date")

    uningested_part_q = """
    select ?s ?m ?g {graph ?g {
    ?s rdf:type fs:Partition .
    ?s base:mountPoint ?m .
    MINUS {?s fs:contains ?y .
    ?y rdf:type fs:File .
    }
    }
    }    
    """

    partition_resp = rdf_session.sparql_query(uningested_part_q)
    partition_list = []

    for ta in partition_resp:
        if len(ta) > 0:
            sub = None
            mount = None
            if "s" in ta:
                sub = ta["s"]["value"]
            if "m" in ta:
                mount = ta["m"]["value"]
            if sub and mount:
                print sub + "***" + mount
                partition_list.append([sub, mount])
#    print partition_list

    for partition in partition_list:
        process_file_system(partition[1], partition[0])
