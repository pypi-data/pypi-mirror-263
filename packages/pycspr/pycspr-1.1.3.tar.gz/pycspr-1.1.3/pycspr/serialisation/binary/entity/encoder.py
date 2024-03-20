import typing

from pycspr.serialisation.binary.cl_type import encode as encode_cl_type
from pycspr.serialisation.binary.cl_value import encode as encode_cl_value
from pycspr.serialisation.utils import cl_value_to_cl_type
from pycspr.types import cl_values
from pycspr.types.deploys import Deploy
from pycspr.types.deploys import DeployApproval
from pycspr.types.deploys import DeployArgument
from pycspr.types.deploys import DeployBody
from pycspr.types.deploys import DeployHeader
from pycspr.types.deploys import ModuleBytes
from pycspr.types.deploys import StoredContractByHash
from pycspr.types.deploys import StoredContractByHashVersioned
from pycspr.types.deploys import StoredContractByName
from pycspr.types.deploys import StoredContractByNameVersioned
from pycspr.types.deploys import Transfer


def encode(entity: object) -> bytes:
    """Encoder: Domain entity -> an array of bytes.

    :param entity: A deploy related type instance to be encoded.
    :returns: An array of bytes.

    """
    try:
        encoder = _ENCODERS[type(entity)]
    except KeyError:
        raise ValueError(f"Unknown deploy type: {entity}")
    else:
        return encoder(entity)


def _encode_deploy(entity: Deploy) -> bytes:
    return \
        encode(entity.header) + \
        entity.hash + \
        encode(entity.payment) + \
        encode(entity.session) + \
        _encode_deploy_approval_set(entity.approvals)


def _encode_deploy_approval(entity: DeployApproval) -> bytes:
    # TODO: check why this logic is required
    if isinstance(entity.signer, bytes):
        return entity.signer + entity.signature
    else:
        return entity.signer.account_key + entity.signature


def _encode_deploy_approval_set(entities: typing.List[DeployApproval]) -> bytes:
    return \
        encode_cl_value(cl_values.CL_U32(len(entities))) + \
        bytes([i for j in map(encode, entities) for i in j])


def _encode_deploy_argument(entity: DeployArgument) -> bytes:
    return \
        encode_cl_value(cl_values.CL_String(entity.name)) + \
        _u8_array_to_bytes(encode_cl_value(entity.value)) + \
        encode_cl_type(cl_value_to_cl_type(entity.value))


def _encode_deploy_body(entity: DeployBody) -> bytes:
    return encode(entity.payment) + encode(entity.session) + entity.hash


def _encode_deploy_header(entity: DeployHeader) -> bytes:
    result = bytes([])
    result += encode_cl_value(
        cl_values.CL_PublicKey.from_public_key(entity.account_public_key)
    )
    result += encode_cl_value(
        cl_values.CL_U64(int(entity.timestamp.value * 1000))
    )
    result += encode_cl_value(
        cl_values.CL_U64(entity.ttl.as_milliseconds)
    )
    result += encode_cl_value(
        cl_values.CL_U64(entity.gas_price)
    )
    result += encode_cl_value(
        cl_values.CL_ByteArray(entity.body_hash)
    )
    result += encode_cl_value(
        cl_values.CL_List(entity.dependencies)
    )
    result += encode_cl_value(
        cl_values.CL_String(entity.chain_name)
    )

    return result


def _encode_module_bytes(entity: ModuleBytes) -> bytes:
    return \
        bytes([0]) + \
        _u8_array_to_bytes(list(entity.module_bytes)) + \
        _vector_to_bytes(list(map(encode, entity.arguments)))


def _encode_stored_contract_by_hash(entity: StoredContractByHash) -> bytes:
    return \
        bytes([1]) + \
        encode_cl_value(cl_values.CL_ByteArray(entity.hash)) + \
        encode_cl_value(cl_values.CL_String(entity.entry_point)) + \
        _vector_to_bytes(list(map(encode, entity.arguments)))


def _encode_stored_contract_by_hash_versioned(entity: StoredContractByHashVersioned) -> bytes:
    return \
        bytes([2]) + \
        encode_cl_value(cl_values.CL_ByteArray(entity.hash)) + \
        encode_cl_value(cl_values.CL_U32(entity.version)) + \
        encode_cl_value(cl_values.CL_String(entity.entry_point)) + \
        _vector_to_bytes(list(map(encode, entity.arguments)))


def _encode_stored_contract_by_name(entity: StoredContractByName) -> bytes:
    return \
        bytes([3]) + \
        encode_cl_value(cl_values.CL_String(entity.name)) + \
        encode_cl_value(cl_values.CL_String(entity.entry_point)) + \
        _vector_to_bytes(list(map(encode, entity.arguments)))


def _encode_stored_contract_by_name_versioned(entity: StoredContractByNameVersioned) -> bytes:
    return \
        bytes([4]) + \
        encode_cl_value(cl_values.CL_String(entity.name)) + \
        encode_cl_value(cl_values.CL_U32(entity.version)) + \
        encode_cl_value(cl_values.CL_String(entity.entry_point)) + \
        _vector_to_bytes(list(map(encode, entity.arguments)))


def _encode_transfer(entity: Transfer) -> bytes:
    return \
        bytes([5]) + \
        _vector_to_bytes(list(map(encode, entity.arguments)))


def _u8_array_to_bytes(value: typing.List[int]) -> bytes:
    return encode_cl_value(cl_values.CL_U32(len(value))) + bytes(value)


def _vector_to_bytes(value: typing.List) -> bytes:
    return \
        encode_cl_value(cl_values.CL_U32(len(value))) + \
        bytes([i for j in value for i in j])


_ENCODERS = {
    Deploy: _encode_deploy,
    DeployApproval: _encode_deploy_approval,
    DeployArgument: _encode_deploy_argument,
    DeployBody: _encode_deploy_body,
    DeployHeader: _encode_deploy_header,
    ModuleBytes: _encode_module_bytes,
    StoredContractByHash: _encode_stored_contract_by_hash,
    StoredContractByHashVersioned: _encode_stored_contract_by_hash_versioned,
    StoredContractByName: _encode_stored_contract_by_name,
    StoredContractByNameVersioned: _encode_stored_contract_by_name_versioned,
    Transfer: _encode_transfer,
}
