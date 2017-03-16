/*
   Copyright 2016-2017 James Fong

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
*/

#ifndef PGG_SCENENODECOMPONENT_HPP
#define PGG_SCENENODECOMPONENT_HPP

#include "NRES.hpp" // Base class: nres::Component

#include "SceneNode.hpp"

namespace pegr {

class SceneNodeEComp : public nres::Component {
public:
    static const nres::ComponentID sComponentID;

    SceneNodeEComp(Model* model = nullptr);
    Model* const mArgModel;
    
    ~SceneNodeEComp();

    SceneNode* mSceneNode;

    const nres::ComponentID& getID() const;
};

}

#endif // PGG_SCENENODECOMPONENT_HPP
