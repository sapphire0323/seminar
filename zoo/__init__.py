# Copyright 2020 InterDigital Communications, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from src.models import Factorized, \
                    Hyperprior, \
                    JointAutoregressive, \
                    ELIC, \
                    Channel_AR

models = {
    'factorized': Factorized,
    'hyperprior': Hyperprior,
    'joint_autogressive': JointAutoregressive, 
    'elic': ELIC,
    'channel_ar': Channel_AR, 
}
