#
# Requirement Management Toolset
#
# Common setup for RDep test cases
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.digraph.Digraph import Digraph
from rmtoo.lib.MemLogStore import MemLogStore

class ReqSet(Digraph, MemLogStore):

    def __init__(self, d=None):
        Digraph.__init__(self, d)
        MemLogStore.__init__(self)

class TestConfig:
    pass

# Create a set of parameters for the test-cases
def create_parameters(d=None):
    return {}, TestConfig(), ReqSet(d)

# This is a test (minimalistic) requirement
class TestReq(Digraph.Node):

    def __init__(self, name, tags, req=None):
        Digraph.Node.__init__(self, name)
        self.id = name
        self.tags = tags
        self.req = req
