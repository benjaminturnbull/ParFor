# PARFOR Session:
#
# Session maintains the session to the rdf store.
# It opens two rdfsurf sessions, one for the main
# store and another for the meta repository.
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

import surf
from Ontology import Ontology
ontology = Ontology()
import Config
import Utils


class Session:

    """
    Session maintains the session to the rdf store. 
    It opens two rdfsurf sessions, one for the main
    store and another for the meta repository.
    """

    store = None
    main_session = None
    metadatastore = None
    meta_session = None

    inputobjuri = ""
    inputobjname = "DataIngestor"
    inputobjdate = ""
    inference = 0

    def commit(self):
        """
        Commit all stores. 
        """
        self.main_session.commit()
        self.meta_session.commit()

    def store_sizes(self):
        """
        Returns store sizes in a list [main, meta]
        """
        return [self.main_session.default_store.size(),
                self.meta_session.default_store.size()]

#
#
    def single_resp_query(self, query, meta_repo=False):
        """
        Quick method for a sparql query with only a single response.
        """

        session = self.main_session

        if meta_repo:
            session = self.meta_session

        res = session.default_store.execute_sparql(query)
        res2 = res['results']["bindings"]
        if len(res2) > 0:
            return res2[0]
        else:
            return None

#
#
    def set_metadata_properties(self, name, uri, inference, date=None):
        """
        On initialisation, it's a good idea to run this to set the 
        correct properties. 
        """
        self.inputobjuri = uri
        self.inputobjname = name
        self.inputobjdate = ""
        self.inference = inference

#
    def make_triple(self,
                    spo,
                    graph=None,
                    literal=False,
                    meta_repo=False):
        """
        does the actual insertion. Unless you know what you are doing,
        use the add_assertion()
        """

        session = self.main_session

        if meta_repo:
            session = self.meta_session

        if literal == False:
            session.default_store.add_triple(surf.rdf.URIRef(spo[0]),
                                             surf.rdf.URIRef(spo[1]),
                                             surf.rdf.URIRef(spo[2]),
                                             surf.rdf.URIRef(graph))
        else:
            session.default_store.add_triple(surf.rdf.URIRef(spo[0]),
                                             surf.rdf.URIRef(spo[1]),
                                             spo[2],
                                             surf.rdf.URIRef(graph))

#
#
    def add_assertion(self, spo,  graph=None, literal=False):
        """
        adds assertion and associated metadata.
        spo is list of s,p,o and if o is a literal, literal = True
        """

        meta_repo = False
        key = self.do_metadata(graph)
        if not graph:
            self.make_triple(spo, key, literal, meta_repo)
        else:
            self.make_triple(spo, graph, literal, meta_repo)

    #
    #
    def do_metadata(self, key=None, description=None):
        """
        makes metadata triple and returns the graph 
        id.
        """

        if not key:
            key = ontology.instance.ns + Utils.get_uuid("metadata_")

        self.make_triple(
            [key,
             ontology.metadata.ns + "inputBy",
             self.inputobjuri],
            meta_repo=True)
        self.make_triple([key,
                          ontology.metadata.ns + "inference",
                          self.inference],
                         literal=True, meta_repo=True)
        self.make_triple([key,
                          ontology.metadata.ns + "inputTime",
                          self.inputobjdate],
                         literal=True, meta_repo=True)
        if description:
            self.make_triple([key,
                              ontology.metadata.ns + "description",
                              description],
                             literal=True, meta_repo=True)

        return key

    def sparql_query(self, query, meta_repo=False):
        """
        takes a query string and runs a query with it. 
        if meta_repo is true it runs the query against
        the metadata repository
        """

        # query = """
        #    select ?s where {
        #    ?s <"""+ ontology.base.name+"""> \""""+ reasoner_name +"""\" .
        #    ?s rdf:type <"""+ontology.metadata.Reasoner +"""> .
        #}"""
        session = self.main_session

        if meta_repo:
            session = self.meta_session

        res = session.default_store.execute_sparql(query)

# print "###" + str(res)
        if "results" in res:
            if "bindings" in res["results"]:
                res2 = res['results']["bindings"]
            elif "boolean" in res:
                res2 = res["boolean"]
            else:
                res2 = None
        else:
            res2 = None

        return res2

    def __init__(self):

        self.store = surf.Store(
            reader='allegro_franz',
            writer='allegro_franz',
            server=Config.query_server,
            port=Config.query_port,
            username=Config.query_username,
            password=Config.query_password,
            catalog=Config.query_catalog,
            repository=Config.query_repository,
            reasoning=True)
        self.main_session = surf.Session(self.store, {})

        self.metadatastore = surf.Store(
            reader='allegro_franz',
            writer='allegro_franz',
            server=Config.metadata_server,
            port=Config.metadata_port,
            username=Config.metadata_username,
            password=Config.metadata_password,
            catalog=Config.metadata_catalog,
            repository=Config.metadata_repository,
            reasoning=True)
        self.meta_session = surf.Session(self.metadatastore, {})
