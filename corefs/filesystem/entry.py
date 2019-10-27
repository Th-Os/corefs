import os
from enum import Enum

from corefs.utils._fs_utils import LinkTypes, Encodings


class Entry():

    def __init__(self, inode, name, path, parent=None, link_type=None):
        self.inode = inode
        self.name = name
        self.path = path
        self.parent = parent
        self.link_type = link_type

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = os.fsencode(name)

    def get_name(self, encoding=Encodings.BYTE_ENCODING):
        if encoding == Encodings.BYTE_ENCODING:
            return self._name
        else:
            return os.fsdecode(self._name)

    def get_full_path(self):
        if self.path == os.sep:
            return self.path + self.get_name(encoding=Encodings.UTF_8_ENCODING)
        return os.path.join(self.path, self.get_name(encoding=Encodings.UTF_8_ENCODING))

    def __repr__(self):
        return "Entry(name: {0}, path: {1})".format(self.name, self.path)


class SymbolicEntry(Entry):

    def __init__(self, inode, name, path, parent=None, link_path=None):
        super().__init__(inode, name, path, parent=parent, link_type=LinkTypes.SYMBOLIC)
        self.link_path = link_path

    def __repr__(self):
        return "SymbolicEntry(name: {0}, path: {1}, link path: {2})".format(self.name, self.path, self.link_path)


class HardlinkEntry(Entry):

    def __init__(self, inode, name, path, parent=None):
        super().__init__(inode, name, path, parent=parent, link_type=LinkTypes.HARDLINK)

    def __repr__(self):
        return "HardlinkEntry(name: {0}, path: {1})".format(self.name, self.path)