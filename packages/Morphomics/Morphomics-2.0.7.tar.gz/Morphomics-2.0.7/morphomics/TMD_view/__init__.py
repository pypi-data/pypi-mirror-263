"""Visualize neurons and plots persistence barcode, diagrams, images.

Matplotlib required.
"""

# Copyright (C) 2022  Blue Brain Project, EPFL
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

try:
    import matplotlib
except ImportError as exc:
    raise ImportError(
        "matplotlib is not installed. " + "Please install it by doing: pip install matplotlib"
    ) from exc

from morphomics.TMD_view import plot  # noqa
from morphomics.TMD_view import view  # noqa
