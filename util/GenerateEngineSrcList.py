#   Copyright 2017 James Fong
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import os

replacementLine = '### GENERATE ###'
sourcePath = '../src/pegr/'
sourceList = []
outputFilename = '../cmake/EngineSrcList.cmake'
boilerplateFilename = 'EngineSrcListBoilerplate.cmake'

def addSource(filename):
    if not filename.startswith('deprecated/') and filename.endswith('.cpp'):
        sourceList.append(filename)

def recursiveSearch(prefixStr, location):
    for node in os.listdir(location):
        nodeLocation = os.path.join(location, node)
    
        if os.path.isfile(nodeLocation):
            addSource(prefixStr + str(node))
        else:
            recursiveSearch(prefixStr + str(node) + '/', nodeLocation)

recursiveSearch('', sourcePath)
sourceList = sorted(sourceList)

with open(outputFilename, 'w+') as outputFile:
    with open(boilerplateFilename, 'r+') as boilerplateFile:
        for line in boilerplateFile:
            if line.startswith(replacementLine):
                for sourceEntry in sourceList:
                    outputFile.write('\"' + sourceEntry + '\"\n')
            else:
                outputFile.write(line)
