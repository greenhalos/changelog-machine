from unittest import TestCase

from src.versions.VersionUtil import VersionNumber


class TestVersionNumber(TestCase):
    def testAdd(self):
        version_less_then("", "1.1.1", self)
        version_less_then("1.1", "1.1.1", self)
        version_less_then("1.1.1", "1.2.1", self)
        version_less_then("1.1.1", "1.20.1", self)
        version_less_then("1.1.1", "1.1rc.1", self)


def version_less_then(v1, v2, self):
    self.assertEqual(VersionNumber(v1).__lt__(VersionNumber(v2)), True)
    self.assertEqual(VersionNumber(v2).__lt__(VersionNumber(v1)), False)
