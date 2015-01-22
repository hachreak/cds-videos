# -*- coding: utf-8 -*-
#
## This file is part of CDS.
## Copyright (C) 2015 CERN.
##
## CDS is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## CDS is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with CDS. If not, see <http://www.gnu.org/licenses/>.
##
## In applying this licence, CERN does not waive the privileges and immunities
## granted to it by virtue of its status as an Intergovernmental Organization
## or submit itself to any jurisdiction.

from __future__ import absolute_import

from .receivers import post_handler_demosite_populate, \
    post_handler_database_create, clean_data_files
from .manage import populate

from invenio.base.scripts.database import create, recreate, drop, init
from invenio.base.signals import post_command

post_command.connect(post_handler_demosite_populate, sender=populate)
post_command.connect(post_handler_database_create, sender=create)
post_command.connect(post_handler_database_create, sender=recreate)
post_command.connect(clean_data_files, sender=init)
post_command.connect(clean_data_files, sender=drop)
