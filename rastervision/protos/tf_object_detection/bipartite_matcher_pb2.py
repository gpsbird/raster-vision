# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rastervision/protos/tf_object_detection/bipartite_matcher.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='rastervision/protos/tf_object_detection/bipartite_matcher.proto',
  package='rastervision.protos.tf_object_detection',
  syntax='proto2',
  serialized_pb=_b('\n?rastervision/protos/tf_object_detection/bipartite_matcher.proto\x12\'rastervision.protos.tf_object_detection\"4\n\x10\x42ipartiteMatcher\x12 \n\x11use_matmul_gather\x18\x06 \x01(\x08:\x05\x66\x61lse')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_BIPARTITEMATCHER = _descriptor.Descriptor(
  name='BipartiteMatcher',
  full_name='rastervision.protos.tf_object_detection.BipartiteMatcher',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='use_matmul_gather', full_name='rastervision.protos.tf_object_detection.BipartiteMatcher.use_matmul_gather', index=0,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=108,
  serialized_end=160,
)

DESCRIPTOR.message_types_by_name['BipartiteMatcher'] = _BIPARTITEMATCHER

BipartiteMatcher = _reflection.GeneratedProtocolMessageType('BipartiteMatcher', (_message.Message,), dict(
  DESCRIPTOR = _BIPARTITEMATCHER,
  __module__ = 'rastervision.protos.tf_object_detection.bipartite_matcher_pb2'
  # @@protoc_insertion_point(class_scope:rastervision.protos.tf_object_detection.BipartiteMatcher)
  ))
_sym_db.RegisterMessage(BipartiteMatcher)


# @@protoc_insertion_point(module_scope)