#    Copyright 2023 SECTRA AB
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

"""Module for handling tile indexing (full or sparse)."""

from wsidicom.instance.tile_index.full_tile_index import FullTileIndex
from wsidicom.instance.tile_index.sparse_tile_index import SparseTileIndex

__all__ = ["FullTileIndex", "SparseTileIndex"]
