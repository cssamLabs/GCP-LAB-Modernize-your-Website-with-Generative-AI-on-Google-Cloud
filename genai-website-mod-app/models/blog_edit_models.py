# Copyright 2024 Google LLC
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

from pydantic import BaseModel


class BlogContentRequest(BaseModel):
    # blog_id: str = ""
    url: str = ""
    blog_content: str = ""
    state: str = ""
    edit_mode: bool = False


class BlogContentResponse(BaseModel):
    blog_id: str = ""
    public_url: str = ""
    blog_content: str = ""
    state: str = ""


class ImageResponse(BaseModel):
    url: str = ""
