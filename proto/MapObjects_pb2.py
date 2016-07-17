# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MapObjects.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Map import MapCell_pb2 as Map_dot_MapCell__pb2
Map_dot_SpawnPoint__pb2 = Map_dot_MapCell__pb2.Map_dot_SpawnPoint__pb2
Map_dot_Fort_dot_FortData__pb2 = Map_dot_MapCell__pb2.Map_dot_Fort_dot_FortData__pb2
Enums_dot_PokemonType__pb2 = Map_dot_MapCell__pb2.Enums_dot_PokemonType__pb2
Enums_dot_TeamColor__pb2 = Map_dot_MapCell__pb2.Enums_dot_TeamColor__pb2
Map_dot_Fort_dot_FortType__pb2 = Map_dot_MapCell__pb2.Map_dot_Fort_dot_FortType__pb2
Map_dot_Fort_dot_FortSponsor__pb2 = Map_dot_MapCell__pb2.Map_dot_Fort_dot_FortSponsor__pb2
Map_dot_Fort_dot_FortRenderingType__pb2 = Map_dot_MapCell__pb2.Map_dot_Fort_dot_FortRenderingType__pb2
Map_dot_Fort_dot_FortLureInfo__pb2 = Map_dot_MapCell__pb2.Map_dot_Fort_dot_FortLureInfo__pb2
Enums_dot_PokemonType__pb2 = Map_dot_MapCell__pb2.Enums_dot_PokemonType__pb2
Map_dot_Fort_dot_FortSummary__pb2 = Map_dot_MapCell__pb2.Map_dot_Fort_dot_FortSummary__pb2
Map_dot_Pokemon_dot_NearbyPokemon__pb2 = Map_dot_MapCell__pb2.Map_dot_Pokemon_dot_NearbyPokemon__pb2
Enums_dot_PokemonType__pb2 = Map_dot_MapCell__pb2.Enums_dot_PokemonType__pb2
Map_dot_Pokemon_dot_WildPokemon__pb2 = Map_dot_MapCell__pb2.Map_dot_Pokemon_dot_WildPokemon__pb2
Data_dot_Pokemon__pb2 = Map_dot_MapCell__pb2.Data_dot_Pokemon__pb2
Map_dot_Pokemon_dot_MapPokemon__pb2 = Map_dot_MapCell__pb2.Map_dot_Pokemon_dot_MapPokemon__pb2
Enums_dot_PokemonType__pb2 = Map_dot_MapCell__pb2.Enums_dot_PokemonType__pb2
from Map import MapObjectsStatus_pb2 as Map_dot_MapObjectsStatus__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='MapObjects.proto',
  package='POGOProtos',
  syntax='proto3',
  serialized_pb=_b('\n\x10MapObjects.proto\x12\nPOGOProtos\x1a\x11Map/MapCell.proto\x1a\x1aMap/MapObjectsStatus.proto\"j\n\nMapObjects\x12*\n\tmap_cells\x18\x01 \x03(\x0b\x32\x17.POGOProtos.Map.MapCell\x12\x30\n\x06status\x18\x02 \x01(\x0e\x32 .POGOProtos.Map.MapObjectsStatusb\x06proto3')
  ,
  dependencies=[Map_dot_MapCell__pb2.DESCRIPTOR,Map_dot_MapObjectsStatus__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MAPOBJECTS = _descriptor.Descriptor(
  name='MapObjects',
  full_name='POGOProtos.MapObjects',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='map_cells', full_name='POGOProtos.MapObjects.map_cells', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='POGOProtos.MapObjects.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=185,
)

_MAPOBJECTS.fields_by_name['map_cells'].message_type = Map_dot_MapCell__pb2._MAPCELL
_MAPOBJECTS.fields_by_name['status'].enum_type = Map_dot_MapObjectsStatus__pb2._MAPOBJECTSSTATUS
DESCRIPTOR.message_types_by_name['MapObjects'] = _MAPOBJECTS

MapObjects = _reflection.GeneratedProtocolMessageType('MapObjects', (_message.Message,), dict(
  DESCRIPTOR = _MAPOBJECTS,
  __module__ = 'MapObjects_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.MapObjects)
  ))
_sym_db.RegisterMessage(MapObjects)


# @@protoc_insertion_point(module_scope)