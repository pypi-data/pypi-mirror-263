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

"""Json schema for Patient model."""

from marshmallow import fields

from wsidicom.metadata.patient import Patient, PatientDeIdentification, PatientSex
from wsidicom.metadata.schema.common import LoadingSchema
from wsidicom.metadata.schema.json.fields import StringOrCodeJsonField


class PatientDeIdentificationJsonSchema(LoadingSchema[PatientDeIdentification]):
    identity_removed = fields.Boolean(load_default=False)
    methods = fields.List(StringOrCodeJsonField(), allow_none=True)

    @property
    def load_type(self):
        return PatientDeIdentification


class PatientJsonSchema(LoadingSchema[Patient]):
    name = fields.String(allow_none=True)
    identifier = fields.String(allow_none=True)
    birth_date = fields.Date(allow_none=True)
    sex = fields.Enum(PatientSex, by_value=True, allow_none=True)
    species_description = StringOrCodeJsonField(allow_none=True)
    de_identification = fields.Nested(
        PatientDeIdentificationJsonSchema(), allow_none=True
    )

    @property
    def load_type(self):
        return Patient
