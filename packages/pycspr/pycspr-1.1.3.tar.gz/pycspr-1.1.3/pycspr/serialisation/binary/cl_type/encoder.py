from pycspr.serialisation.binary.cl_value import encode as encode_cl_value
from pycspr.types import cl_types
from pycspr.types import cl_values
from pycspr.types import CL_TypeKey


def encode(entity: cl_types.CL_Type) -> bytes:
    """Encoder: CL type -> an array of bytes.

    :param entity: A CL type to be encoded.
    :returns: An array of bytes.

    """
    if entity.type_key in _ENCODERS["simple"]:
        return bytes([entity.type_key.value]) + bytes([])
    elif entity.type_key in _ENCODERS["complex"]:
        return bytes([entity.type_key.value]) + _ENCODERS["complex"][entity.type_key](entity)
    else:
        raise ValueError("Unrecognized cl type")


def _encode_byte_array(entity: cl_types.CL_Type_ByteArray):
    return encode_cl_value(cl_values.CL_U32(entity.size))


def _encode_list(entity: cl_types.CL_Type_List):
    return encode(entity.inner_type)


def _encode_map(entity: cl_types.CL_Type_Map):
    return encode(entity.key_type) + encode(entity.value_type)


def _encode_option(entity: cl_types.CL_Type_Option):
    return encode(entity.inner_type)


def _encode_tuple_1(entity: cl_types.CL_Type_Tuple1):
    return encode(entity.t0_type)


def _encode_tuple_2(entity: cl_types.CL_Type_Tuple1):
    return encode(entity.t0_type) + encode(entity.t1_type)


def _encode_tuple_3(entity: cl_types.CL_Type_Tuple1):
    return encode(entity.t0_type) + encode(entity.t1_type) + encode(entity.t2_type)


_ENCODERS: dict = {
    "complex": {
        CL_TypeKey.BYTE_ARRAY: _encode_byte_array,
        CL_TypeKey.LIST: _encode_list,
        CL_TypeKey.MAP: _encode_map,
        CL_TypeKey.OPTION: _encode_option,
        CL_TypeKey.TUPLE_1: _encode_tuple_1,
        CL_TypeKey.TUPLE_2: _encode_tuple_2,
        CL_TypeKey.TUPLE_3: _encode_tuple_3,
    },
    "simple": {
        CL_TypeKey.ANY,
        CL_TypeKey.BOOL,
        CL_TypeKey.I32,
        CL_TypeKey.I64,
        CL_TypeKey.KEY,
        CL_TypeKey.PUBLIC_KEY,
        CL_TypeKey.RESULT,
        CL_TypeKey.STRING,
        CL_TypeKey.U8,
        CL_TypeKey.U32,
        CL_TypeKey.U64,
        CL_TypeKey.U128,
        CL_TypeKey.U256,
        CL_TypeKey.U512,
        CL_TypeKey.UNIT,
        CL_TypeKey.UREF,
    }
}
