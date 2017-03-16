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

#ifndef PEGR_SOUNDRESOURCE_HPP
#define PEGR_SOUNDRESOURCE_HPP

#include "SoundWaveform.hpp"
#include "Resource.hpp"

namespace pegr {

class SoundResource : public Resource, public Sound::Waveform {
public:
    SoundResource();
    ~SoundResource();
    
    void mix(
        SoundIoChannelArea* channels, uint32_t channelCount, 
        uint32_t frameCount, 
        double startPhase,
        double endPhase,
        double startAmplitude,
        double endAmplitude) const;
        
    void load();
    void unload();
};

} // namespace pegr

#endif // PEGR_SOUNDRESOURCE_HPP
