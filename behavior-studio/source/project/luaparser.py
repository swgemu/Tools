# coding=utf-8
# -----------------
# file      : luaparser.py
# date      : 2017/08/01
# author    : Dustin Niehoff
# contact   : dannuic@gmail.com
# copyright : Copyright (C) 2012  Victor Zarubkin
# license   : This file is part of BehaviorStudio.
#           :
#           : BehaviorStudio is free software: you can redistribute it and/or modify
#           : it under the terms of the GNU General Public License as published by
#           : the Free Software Foundation, either version 3 of the License, or
#           : (at your option) any later version.
#           :
#           : BehaviorStudio is distributed in the hope that it will be useful,
#           : but WITHOUT ANY WARRANTY; without even the implied warranty of
#           : MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#           : GNU General Public License for more details.
#           :
#           : You should have received a copy of the GNU General Public License
#           : along with BehaviorStudio. If not, see <http://www.gnu.org/licenses/>.
#           :
#           : A copy of the GNU General Public License can be found in file COPYING.
############################################################################

"""

"""

from __future__ import unicode_literals

__author__ = 'Dustin Niehoff'
__copyright__ = 'Copyright (C) 2012  Victor Zarubkin'
__credits__ = ['Victor Zarubkin','Dustin Niehoff']
__license__ = ['GPLv3']
__version__ = '1.3.0'  # this is last application version when this script file was changed
__email__ = 'dannuic@gmail.com'
############################################################################

import os
import regex as re

def matchNamedBrackets(matchString):
    # interestingly, this could also work but apparently returns 3 empty
    # strings at the beginning of the tuple -- I guess the ?DEFINE is
    # "capturing"?
    #reg = '(?(DEFINE)(?P<b>({((?>[^{}]|(?P>b))*)})))(\w+)\s*=\s*{((?>[^{}]|(?P>b))*)}'

    reg = '(\w+)\s*=\s*({((?>[^{}]|(?2))*)})'
    # There are 3 captures in this regex, so ensure that we get all 3 before
    # returning the list. This guarantees that we get a list of size 2 tuples
    # as a return (which could be empty)
    return [(r[0], re.sub('[\s]+', '', r[2])) for r in re.findall(reg, matchString, re.S) if len(r) == 3]

def matchBrackets(matchString):
    reg = '({(?>[^{}]|(?R))*})'
    return re.findall(reg, matchString)

###########################################################################
###########################################################################

class LuaTree(object):
    def __init__(self, name, nodes):
        self.name = name
        self.nodes = nodes

class LuaNode(object):
    def __init__(self, ident, name, pid, **kwargs):
        self.id = ident
        self.name = name
        self.pid = pid
        self.args = []
        for key, val in kwargs.items():
            self.args.append(str(key) + '=' + str(val))

    def mkString(self):
        l = ['id="' + str(self.id) + '"',
             'name="' + str(self.name) + '"',
             'pid="' + str(self.pid) + '"']

        if self.args:
            l.append('args={' + ', '.join(map(str, self.args)) + '}')

        return '\t{' + ',\t'.join(l) + '}'

class LuaParser(object):
    __debug_str = ('debug', 'Debug', 'DEBUG')

    def __init__(self):
        pass

    # Parse a lua file and return an object filled with a list of data trees
    def parse(self, filename):
        # Loop through file until I find an opening block (^(\w+)\s*=\s*\{.*$)
        # where the first capture is the name of the tree. Then grab all the
        # lines until the close of the block (^\}.*). The next parseable line
        # should verify that my block has closed. We can then pass the block
        # into the tree parser to get a tree object.
        if filename is None:
            print('error: No filename for lua parser')
            print('')
            return []

        try:
            with open(filename) as f:
                return [(b[0], self.__parseTree(b[1])) for b in matchNamedBrackets(f.read()) if len(b) == 2]
        except EnvironmentError as error:
            print('error: Cannot open filename {0} with error {1}'.format(filename, error))
            print('')
            return []

    def __parseTree(self, text):
        l = matchBrackets(text)
        return l

    def write(self, trees, filename, suffix):
        try:
            with open(filename, 'w') as f:
                for tree in trees:
                    className = tree.name + suffix
                    f.write(className + ' = {\n')
                    print(tree.nodes)
                    f.write(',\n'.join([node.mkString() for node in tree.nodes]))
                    f.write('}\naddAiTemplate("' + className + '", ' +
                            className + ')\n\n')
        except EnvironmentError as error:
            print('error: Cannot open filename {0} with error {1}'.format(filename, error))
            print('')
        pass
