'''
# `data_akamai_cloudwrapper_capacities`

Refer to the Terraform Registry for docs: [`data_akamai_cloudwrapper_capacities`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_capacities).
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8


class DataAkamaiCloudwrapperCapacities(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudwrapperCapacities.DataAkamaiCloudwrapperCapacities",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_capacities akamai_cloudwrapper_capacities}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        capacities: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudwrapperCapacitiesCapacities", typing.Dict[builtins.str, typing.Any]]]]] = None,
        contract_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_capacities akamai_cloudwrapper_capacities} Data Source.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param capacities: capacities block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_capacities#capacities DataAkamaiCloudwrapperCapacities#capacities}
        :param contract_ids: List of contract IDs with Cloud Wrapper entitlement. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_capacities#contract_ids DataAkamaiCloudwrapperCapacities#contract_ids}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a599809d465fbbdd9b50b5e95bae529dd303d7e2f7cf0f12e1f8db158f2ee20)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = DataAkamaiCloudwrapperCapacitiesConfig(
            capacities=capacities,
            contract_ids=contract_ids,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="generateConfigForImport")
    @builtins.classmethod
    def generate_config_for_import(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        import_to_id: builtins.str,
        import_from_id: builtins.str,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    ) -> _cdktf_9a9027ec.ImportableResource:
        '''Generates CDKTF code for importing a DataAkamaiCloudwrapperCapacities resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the DataAkamaiCloudwrapperCapacities to import.
        :param import_from_id: The id of the existing DataAkamaiCloudwrapperCapacities that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_capacities#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the DataAkamaiCloudwrapperCapacities to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bee65a2ae42f9072bbc26d622d1234e78bda534455f84fbc1ff11368464752a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putCapacities")
    def put_capacities(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudwrapperCapacitiesCapacities", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8ddcfbdeef5847f3cd5305869078e8c8ec4f49f569af6b0cf4b94a3c21e727f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCapacities", [value]))

    @jsii.member(jsii_name="resetCapacities")
    def reset_capacities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacities", []))

    @jsii.member(jsii_name="resetContractIds")
    def reset_contract_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContractIds", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.member(jsii_name="synthesizeHclAttributes")
    def _synthesize_hcl_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeHclAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="capacities")
    def capacities(self) -> "DataAkamaiCloudwrapperCapacitiesCapacitiesList":
        return typing.cast("DataAkamaiCloudwrapperCapacitiesCapacitiesList", jsii.get(self, "capacities"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="capacitiesInput")
    def capacities_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudwrapperCapacitiesCapacities"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudwrapperCapacitiesCapacities"]]], jsii.get(self, "capacitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="contractIdsInput")
    def contract_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "contractIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="contractIds")
    def contract_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "contractIds"))

    @contract_ids.setter
    def contract_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cb9267ba0562ecad46a1848013128f42804a0cfd2d45b24cc51ea2fb986c4a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contractIds", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudwrapperCapacities.DataAkamaiCloudwrapperCapacitiesCapacities",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiCloudwrapperCapacitiesCapacities:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudwrapperCapacitiesCapacities(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudwrapperCapacities.DataAkamaiCloudwrapperCapacitiesCapacitiesApproved",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiCloudwrapperCapacitiesCapacitiesApproved:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudwrapperCapacitiesCapacitiesApproved(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudwrapperCapacitiesCapacitiesApprovedOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudwrapperCapacities.DataAkamaiCloudwrapperCapacitiesCapacitiesApprovedOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b25a624ba91bd43737c03e59c107696e7d37287ba4145377777140e12edd2601)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAkamaiCloudwrapperCapacitiesCapacitiesApproved]:
        return typing.cast(typing.Optional[DataAkamaiCloudwrapperCapacitiesCapacitiesApproved], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAkamaiCloudwrapperCapacitiesCapacitiesApproved],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a9ea02e17e4775d53f964c5475a080cc2beb1399de490e8c2c5a90ea24bcde6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudwrapperCapacities.DataAkamaiCloudwrapperCapacitiesCapacitiesAssigned",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiCloudwrapperCapacitiesCapacitiesAssigned:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudwrapperCapacitiesCapacitiesAssigned(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudwrapperCapacitiesCapacitiesAssignedOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudwrapperCapacities.DataAkamaiCloudwrapperCapacitiesCapacitiesAssignedOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dac5ad6de5c1c245905613c34add6d678d5a900940c6d6798c3c75f15f7a363d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAkamaiCloudwrapperCapacitiesCapacitiesAssigned]:
        return typing.cast(typing.Optional[DataAkamaiCloudwrapperCapacitiesCapacitiesAssigned], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAkamaiCloudwrapperCapacitiesCapacitiesAssigned],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db9368ba94d9665762d94a47b6609c5048e664c4230424dcf8c04c8bab672b5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudwrapperCapacitiesCapacitiesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudwrapperCapacities.DataAkamaiCloudwrapperCapacitiesCapacitiesList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__212752f61ae6bfc67edc8f9e09d0469cc08163588f016bb008db80c49f55cc90)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiCloudwrapperCapacitiesCapacitiesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9c418394edc1f1576f0dd8a4cc2769dc5846beae39b0c78172b9f43a81ded2e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiCloudwrapperCapacitiesCapacitiesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cd6b7b27c039c89b8308dc2782d61ad6635cb52b02371cde06b2b05ac4bc598)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__822de5a75b95f53db444aa12b8be08852f9a34d790165470c5683aaac59a794a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6c3a2e802e5b39df116e77251420e2d0bf6ffe3835b8bd9f5a99fb1454bcafd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperCapacitiesCapacities]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperCapacitiesCapacities]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperCapacitiesCapacities]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6454289f542f26751b9e144c5f2d99afa944533084ba9e457cd5a1dcadd037bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudwrapperCapacitiesCapacitiesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudwrapperCapacities.DataAkamaiCloudwrapperCapacitiesCapacitiesOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6dfd93c7eb0190dcbbe0be8903a33b825ca7581e94100175a35600d132dfa46c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="approved")
    def approved(
        self,
    ) -> DataAkamaiCloudwrapperCapacitiesCapacitiesApprovedOutputReference:
        return typing.cast(DataAkamaiCloudwrapperCapacitiesCapacitiesApprovedOutputReference, jsii.get(self, "approved"))

    @builtins.property
    @jsii.member(jsii_name="assigned")
    def assigned(
        self,
    ) -> DataAkamaiCloudwrapperCapacitiesCapacitiesAssignedOutputReference:
        return typing.cast(DataAkamaiCloudwrapperCapacitiesCapacitiesAssignedOutputReference, jsii.get(self, "assigned"))

    @builtins.property
    @jsii.member(jsii_name="contractId")
    def contract_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contractId"))

    @builtins.property
    @jsii.member(jsii_name="locationId")
    def location_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "locationId"))

    @builtins.property
    @jsii.member(jsii_name="locationName")
    def location_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "locationName"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="unassigned")
    def unassigned(
        self,
    ) -> "DataAkamaiCloudwrapperCapacitiesCapacitiesUnassignedOutputReference":
        return typing.cast("DataAkamaiCloudwrapperCapacitiesCapacitiesUnassignedOutputReference", jsii.get(self, "unassigned"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperCapacitiesCapacities]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperCapacitiesCapacities]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperCapacitiesCapacities]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51d9cbf42d7b3a6651f78b335a0b955e790909b66731de526f138dff537c97e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudwrapperCapacities.DataAkamaiCloudwrapperCapacitiesCapacitiesUnassigned",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiCloudwrapperCapacitiesCapacitiesUnassigned:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudwrapperCapacitiesCapacitiesUnassigned(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudwrapperCapacitiesCapacitiesUnassignedOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudwrapperCapacities.DataAkamaiCloudwrapperCapacitiesCapacitiesUnassignedOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e35ac1b8ae4903b274dfd652c18cfe28905f948501c73e1374de6fcaa91d14ed)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAkamaiCloudwrapperCapacitiesCapacitiesUnassigned]:
        return typing.cast(typing.Optional[DataAkamaiCloudwrapperCapacitiesCapacitiesUnassigned], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAkamaiCloudwrapperCapacitiesCapacitiesUnassigned],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf677ab6f9936154d7a6618e50846f7edeecb72ace1976b37b998222c2164cf8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudwrapperCapacities.DataAkamaiCloudwrapperCapacitiesConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "capacities": "capacities",
        "contract_ids": "contractIds",
    },
)
class DataAkamaiCloudwrapperCapacitiesConfig(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
        capacities: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudwrapperCapacitiesCapacities, typing.Dict[builtins.str, typing.Any]]]]] = None,
        contract_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param capacities: capacities block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_capacities#capacities DataAkamaiCloudwrapperCapacities#capacities}
        :param contract_ids: List of contract IDs with Cloud Wrapper entitlement. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_capacities#contract_ids DataAkamaiCloudwrapperCapacities#contract_ids}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9166fb189a2befe79f28250ebce51b394770cac851fd1ee42fd6c64d592ebde)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument capacities", value=capacities, expected_type=type_hints["capacities"])
            check_type(argname="argument contract_ids", value=contract_ids, expected_type=type_hints["contract_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if capacities is not None:
            self._values["capacities"] = capacities
        if contract_ids is not None:
            self._values["contract_ids"] = contract_ids

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(
        self,
    ) -> typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]], result)

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]], result)

    @builtins.property
    def capacities(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperCapacitiesCapacities]]]:
        '''capacities block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_capacities#capacities DataAkamaiCloudwrapperCapacities#capacities}
        '''
        result = self._values.get("capacities")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperCapacitiesCapacities]]], result)

    @builtins.property
    def contract_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of contract IDs with Cloud Wrapper entitlement.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_capacities#contract_ids DataAkamaiCloudwrapperCapacities#contract_ids}
        '''
        result = self._values.get("contract_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudwrapperCapacitiesConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DataAkamaiCloudwrapperCapacities",
    "DataAkamaiCloudwrapperCapacitiesCapacities",
    "DataAkamaiCloudwrapperCapacitiesCapacitiesApproved",
    "DataAkamaiCloudwrapperCapacitiesCapacitiesApprovedOutputReference",
    "DataAkamaiCloudwrapperCapacitiesCapacitiesAssigned",
    "DataAkamaiCloudwrapperCapacitiesCapacitiesAssignedOutputReference",
    "DataAkamaiCloudwrapperCapacitiesCapacitiesList",
    "DataAkamaiCloudwrapperCapacitiesCapacitiesOutputReference",
    "DataAkamaiCloudwrapperCapacitiesCapacitiesUnassigned",
    "DataAkamaiCloudwrapperCapacitiesCapacitiesUnassignedOutputReference",
    "DataAkamaiCloudwrapperCapacitiesConfig",
]

publication.publish()

def _typecheckingstub__1a599809d465fbbdd9b50b5e95bae529dd303d7e2f7cf0f12e1f8db158f2ee20(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    capacities: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudwrapperCapacitiesCapacities, typing.Dict[builtins.str, typing.Any]]]]] = None,
    contract_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bee65a2ae42f9072bbc26d622d1234e78bda534455f84fbc1ff11368464752a(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8ddcfbdeef5847f3cd5305869078e8c8ec4f49f569af6b0cf4b94a3c21e727f(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudwrapperCapacitiesCapacities, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cb9267ba0562ecad46a1848013128f42804a0cfd2d45b24cc51ea2fb986c4a2(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b25a624ba91bd43737c03e59c107696e7d37287ba4145377777140e12edd2601(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a9ea02e17e4775d53f964c5475a080cc2beb1399de490e8c2c5a90ea24bcde6(
    value: typing.Optional[DataAkamaiCloudwrapperCapacitiesCapacitiesApproved],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dac5ad6de5c1c245905613c34add6d678d5a900940c6d6798c3c75f15f7a363d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db9368ba94d9665762d94a47b6609c5048e664c4230424dcf8c04c8bab672b5b(
    value: typing.Optional[DataAkamaiCloudwrapperCapacitiesCapacitiesAssigned],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__212752f61ae6bfc67edc8f9e09d0469cc08163588f016bb008db80c49f55cc90(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9c418394edc1f1576f0dd8a4cc2769dc5846beae39b0c78172b9f43a81ded2e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cd6b7b27c039c89b8308dc2782d61ad6635cb52b02371cde06b2b05ac4bc598(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__822de5a75b95f53db444aa12b8be08852f9a34d790165470c5683aaac59a794a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6c3a2e802e5b39df116e77251420e2d0bf6ffe3835b8bd9f5a99fb1454bcafd(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6454289f542f26751b9e144c5f2d99afa944533084ba9e457cd5a1dcadd037bf(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperCapacitiesCapacities]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6dfd93c7eb0190dcbbe0be8903a33b825ca7581e94100175a35600d132dfa46c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51d9cbf42d7b3a6651f78b335a0b955e790909b66731de526f138dff537c97e0(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperCapacitiesCapacities]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e35ac1b8ae4903b274dfd652c18cfe28905f948501c73e1374de6fcaa91d14ed(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf677ab6f9936154d7a6618e50846f7edeecb72ace1976b37b998222c2164cf8(
    value: typing.Optional[DataAkamaiCloudwrapperCapacitiesCapacitiesUnassigned],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9166fb189a2befe79f28250ebce51b394770cac851fd1ee42fd6c64d592ebde(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    capacities: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudwrapperCapacitiesCapacities, typing.Dict[builtins.str, typing.Any]]]]] = None,
    contract_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
