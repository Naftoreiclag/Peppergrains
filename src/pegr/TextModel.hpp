/*
   Copyright 2015-2017 James Fong

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

#ifndef PGG_TEXTMODEL_HPP
#define PGG_TEXTMODEL_HPP

#include <string>

#include "ShaderProgramResource.hpp"
#include "FontResource.hpp"
#include "Model.hpp"

namespace pegr {

class TextModel : public Model {
private:
    FontResource* mFont;
    std::string mText;
    uint32_t mNumGlyphs;

    GLuint mVertexArrayObject;
    GLuint mVertexBufferObject;
    GLuint mIndexBufferObject;
    ShaderProgramResource* mShaderProg;
public:
    TextModel(FontResource* font, std::string text);
    virtual ~TextModel();

    void load();
    void unload();

    void render(Renderable::Pass rendPass, const glm::mat4& modelMat);

};

}

#endif // PGG_TEXTMODEL_HPP
