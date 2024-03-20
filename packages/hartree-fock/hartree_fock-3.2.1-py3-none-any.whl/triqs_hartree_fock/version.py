# Copyright (c) 2022 Simons Foundation
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
# You may obtain a copy of the License at
#     https:#www.gnu.org/licenses/gpl-3.0.txt
#
# Authors: Jonathan Karp, Alexander Hampel, Nils Wentzell, Hugo U. R. Strand, Olivier Parcollet

version = "3.2.1"
triqs_hash = "40768343b393dbacaf535adc72e140d6dc316b65"
triqs_hartree_fock_hash = "680288f7e8a8ec85e44982fa7dd5047bdd3128f7"

def show_version():
  print("\nYou are using triqs_hartree_fock version %s\n"%version)

def show_git_hash():
  print("\nYou are using triqs_hartree_fock git hash %s based on triqs git hash %s\n"%("680288f7e8a8ec85e44982fa7dd5047bdd3128f7", triqs_hash))
