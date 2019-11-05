import unittest

from xcube.util import extension
from xcube_gen_vito.plugin import init_plugin


class VitoS2PlusPluginTest(unittest.TestCase):

    # noinspection PyMethodMayBeStatic
    def test_init_plugin(self):
        ext_reg = extension.ExtensionRegistry()
        init_plugin(ext_reg)
        self.assertTrue(ext_reg.has_extension('xcube.core.gen.iproc', 'vito-s2plus-l2'))

