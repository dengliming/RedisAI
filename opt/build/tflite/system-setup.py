#!/usr/bin/env python3

import sys
import os
import argparse

READIES = "/build/readies"
sys.path.insert(0, READIES)
import paella

#----------------------------------------------------------------------------------------------

class RediSearchSetup(paella.Setup):
    def __init__(self, nop=False):
        paella.Setup.__init__(self, nop)

    def common_first(self):
        self.install_downloaders()
        self.install("git")

    def debian_compat(self):
        self.install("unzip build-essential zlib1g-dev libegl1-mesa-dev libgles2-mesa-dev python3-distutils python3-numpy")

    def macos(self):
        self.install_gnu_utils()

    def common_last(self):
        self.run("{PYTHON} {READIES}/bin/getcmake --no-repo".format(PYTHON=self.python, READIES=READIES))
        self.run("USE_BAZEL_VERSION=3.5.0 {PYTHON} {READIES}/bin/getbazel".format(PYTHON=self.python, READIES=READIES))

#----------------------------------------------------------------------------------------------

parser = argparse.ArgumentParser(description='Set up system for build.')
parser.add_argument('-n', '--nop', action="store_true", help='no operation')
args = parser.parse_args()

RediSearchSetup(nop = args.nop).setup()
