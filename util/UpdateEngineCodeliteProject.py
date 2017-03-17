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

import xml.etree.ElementTree as ET
import os

sourcePath = '../src/pegr/'
sourceList = []
includeDirList = []
allowedFileExts = ['.cpp', '.hpp']
blacklistedDirs = ['deprecated/']
projectFilename = '../src/pegr/Codelite.project'

def addSource(filename):
    if not any(filename.startswith(dir) for dir in blacklistedDirs) \
            and any(filename.endswith(ext) for ext in allowedFileExts):
        sourceList.append(filename)
        fileParentName = str(os.path.dirname(filename))
        if fileParentName and fileParentName not in includeDirList:
            includeDirList.append(fileParentName)

def recursiveSearch(prefixStr, location):
    for node in os.listdir(location):
        nodeLocation = os.path.join(location, node)
    
        if os.path.isfile(nodeLocation):
            addSource(prefixStr + str(node))
        else:
            recursiveSearch(prefixStr + str(node) + '/', nodeLocation)

recursiveSearch('', sourcePath)
sourceList = sorted(sourceList)
includeDirList = sorted(includeDirList)

projectEtree = ET.parse(projectFilename)

projectRoot = projectEtree.getroot()

virtualDirs = projectRoot.findall('VirtualDirectory')

pegrVirtualDir = None
for virtualDir in virtualDirs:
    if virtualDir.get('Name') == 'pegr':
        pegrVirtualDir = virtualDir
        break
if not pegrVirtualDir:
    pegrVirtualDir = ET.SubElement(projectRoot, 'VirtualDirectory')

pegrVirtualDir.clear()
pegrVirtualDir.set('Name', 'pegr')

for source in sourceList:
    sourceElem = ET.SubElement(pegrVirtualDir, 'File')
    sourceElem.set('Name', source)

projectEtree.write(projectFilename)