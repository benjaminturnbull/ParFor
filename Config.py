# CONFIG
#
# Config provides configuration details used throughout the
# program.
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
#
# Set up two repositories in AllegroGraph
# (or whatever Triple store you use):
#  - one for the main connection
#  - one for the metadata
# In most cases, these will be different
# repositories in the same server, but
# we split these out in case you have multiple
# servers.
#
# Set up a federation of the two for the
# query server.
#
# Replace the TODOs with your own data.
#
#


# data connection. The main connection used. Used
# for making new assertions.
conn_server = ''    # TODO - add server address here
conn_port = 10035   # this is the default port
conn_username = ''  # TODO - add connection username here.
conn_password = ''  # TODO - add connection password here.
conn_catalog = ''   # TODO - add catalog if you use one.
conn_repository = ''  # TODO - add repo name.

# query server connection. The query server.
# We currently don't go into this in detail
# but Allegro allows you to federate connections
# for querying.
query_server = ''      # TODO - add server address here
query_port = 10035     # this is the default port
query_username = ''    # TODO - add username
query_password = ''    # TODO - add password
query_catalog = ''     # TODO - add catagloe if you use one
query_repository = ''  # TODO - add repo name
query_reasoning = True  # Leave this if possible

# The metadata store. Used to assert metadata
# and query if you require only metadata.
metadata_server = ''      # TODO - add server address here
metadata_port = 10035     # this is the default port
metadata_username = ''    # TODO - add username
metadata_password = ''    # TODO - add password
metadata_catalog = ''     # TODO - add catalogue if you use one
metadata_repository = ''  # TODO - add repo name
metadata_reasoning = True  # Leave this if possible


DEBUG = 1
SPARQLER_RULES = "./SPARQLerRules/"
SPARQLER_PLUGINS = "./SPARQLerPlugins/"
CALLABLE_COMMAND_LIST = ["mount(.*)", ""]
