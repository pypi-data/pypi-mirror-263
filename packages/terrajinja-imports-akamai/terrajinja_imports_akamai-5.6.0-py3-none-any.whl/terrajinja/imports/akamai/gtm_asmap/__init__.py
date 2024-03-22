'''
# `akamai_gtm_asmap`

Refer to the Terraform Registry for docs: [`akamai_gtm_asmap`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_asmap).
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


class GtmAsmap(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.gtmAsmap.GtmAsmap",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_asmap akamai_gtm_asmap}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        default_datacenter: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GtmAsmapDefaultDatacenter", typing.Dict[builtins.str, typing.Any]]]],
        domain: builtins.str,
        name: builtins.str,
        assignment: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GtmAsmapAssignment", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        wait_on_complete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_asmap akamai_gtm_asmap} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param default_datacenter: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_asmap#default_datacenter GtmAsmap#default_datacenter}.
        :param domain: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_asmap#domain GtmAsmap#domain}.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_asmap#name GtmAsmap#name}.
        :param assignment: assignment block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_asmap#assignment GtmAsmap#assignment}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_asmap#id GtmAsmap#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param wait_on_complete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_asmap#wait_on_complete GtmAsmap#wait_on_complete}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b67f3574eb22a72c48b06f1b257c3582a9074bf4f1e81d5f17a7a000e04701d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GtmAsmapConfig(
            default_datacenter=default_datacenter,
            domain=domain,
            name=name,
            assignment=assignment,
            id=id,
            wait_on_complete=wait_on_complete,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="generateConfigForImport")
    @builtins.classmethod
    def generate_config_for_import(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        import_to_id: builtins.str,
        import_from_id: builtins.str,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    ) -> _cdktf_9a9027ec.ImportableResource:
        '''Generates CDKTF code for importing a GtmAsmap resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the GtmAsmap to import.
        :param import_from_id: The id of the existing GtmAsmap that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_asmap#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the GtmAsmap to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39dc705b8705b5d68ccc845d0e71f4d54a535336e7f512937f164a1b25a4702c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putAssignment")
    def put_assignment(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GtmAsmapAssignment", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7357645f2af71a885ca866c6f17a1bae3237c9a67f66a832d0d450bb239866d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAssignment", [value]))

    @jsii.member(jsii_name="putDefaultDatacenter")
    def put_default_datacenter(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GtmAsmapDefaultDatacenter", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b8c59dc9f1db5d2fc25ed85c8630645cebd711126592bb4038357ab461277ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDefaultDatacenter", [value]))

    @jsii.member(jsii_name="resetAssignment")
    def reset_assignment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssignment", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetWaitOnComplete")
    def reset_wait_on_complete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitOnComplete", []))

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
    @jsii.member(jsii_name="assignment")
    def assignment(self) -> "GtmAsmapAssignmentList":
        return typing.cast("GtmAsmapAssignmentList", jsii.get(self, "assignment"))

    @builtins.property
    @jsii.member(jsii_name="defaultDatacenter")
    def default_datacenter(self) -> "GtmAsmapDefaultDatacenterList":
        return typing.cast("GtmAsmapDefaultDatacenterList", jsii.get(self, "defaultDatacenter"))

    @builtins.property
    @jsii.member(jsii_name="assignmentInput")
    def assignment_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GtmAsmapAssignment"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GtmAsmapAssignment"]]], jsii.get(self, "assignmentInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultDatacenterInput")
    def default_datacenter_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GtmAsmapDefaultDatacenter"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GtmAsmapDefaultDatacenter"]]], jsii.get(self, "defaultDatacenterInput"))

    @builtins.property
    @jsii.member(jsii_name="domainInput")
    def domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="waitOnCompleteInput")
    def wait_on_complete_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "waitOnCompleteInput"))

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__300ff800fe76d3cadb99008a2b7c8cf9e859697818fb8aa6e513a52b582d6bfd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0ae4d922a751463b06011df70738596cda51052b5b2e30e0c4bbbc009c19ff8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__940bf52ffe707870b3d6a9401f7ab32202be043c971f6b27189574c20f3c2de9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="waitOnComplete")
    def wait_on_complete(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "waitOnComplete"))

    @wait_on_complete.setter
    def wait_on_complete(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd103806fdcb38a2844044c1f4b7f44c062e07dc49c4654638ac1382a2759852)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitOnComplete", value)


@jsii.data_type(
    jsii_type="akamai.gtmAsmap.GtmAsmapAssignment",
    jsii_struct_bases=[],
    name_mapping={
        "as_numbers": "asNumbers",
        "datacenter_id": "datacenterId",
        "nickname": "nickname",
    },
)
class GtmAsmapAssignment:
    def __init__(
        self,
        *,
        as_numbers: typing.Sequence[jsii.Number],
        datacenter_id: jsii.Number,
        nickname: builtins.str,
    ) -> None:
        '''
        :param as_numbers: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_asmap#as_numbers GtmAsmap#as_numbers}.
        :param datacenter_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_asmap#datacenter_id GtmAsmap#datacenter_id}.
        :param nickname: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_asmap#nickname GtmAsmap#nickname}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88b64305466cbcff022a4c81af2545d3a83f356481fd8235fe75a745a569a155)
            check_type(argname="argument as_numbers", value=as_numbers, expected_type=type_hints["as_numbers"])
            check_type(argname="argument datacenter_id", value=datacenter_id, expected_type=type_hints["datacenter_id"])
            check_type(argname="argument nickname", value=nickname, expected_type=type_hints["nickname"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "as_numbers": as_numbers,
            "datacenter_id": datacenter_id,
            "nickname": nickname,
        }

    @builtins.property
    def as_numbers(self) -> typing.List[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_asmap#as_numbers GtmAsmap#as_numbers}.'''
        result = self._values.get("as_numbers")
        assert result is not None, "Required property 'as_numbers' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    @builtins.property
    def datacenter_id(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_asmap#datacenter_id GtmAsmap#datacenter_id}.'''
        result = self._values.get("datacenter_id")
        assert result is not None, "Required property 'datacenter_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def nickname(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_asmap#nickname GtmAsmap#nickname}.'''
        result = self._values.get("nickname")
        assert result is not None, "Required property 'nickname' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GtmAsmapAssignment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GtmAsmapAssignmentList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.gtmAsmap.GtmAsmapAssignmentList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e5cb8b0f1b8d5183fd50e3cd0c250e52554a8a62ad1798a0001a8aa37212678b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GtmAsmapAssignmentOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64e7e6464e3184c7dbffbaffa61c4706aff0ec596933893b5e439648b0da4117)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GtmAsmapAssignmentOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b67cab0c0ce0fe173bd924462832198b8d59511c08b562cac50ad58d30cf1c6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__eebccc636f9d339984480017de3735d89243c96c7c86d1c51add5ce1a8a0a632)
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
            type_hints = typing.get_type_hints(_typecheckingstub__af5c4b760327c5bac91d03910f41d8a43c031551a3a61fd22c1177fec05e5776)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmAsmapAssignment]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmAsmapAssignment]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmAsmapAssignment]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c21c8b654cfc84f596a8de9266a18e3092581e633762f01cea76c5abbcb5567f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GtmAsmapAssignmentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.gtmAsmap.GtmAsmapAssignmentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dc089f83cc7dd947c94daf30813ccd937f833fab9ba4dbfad32d7e2b27e4e85c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="asNumbersInput")
    def as_numbers_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "asNumbersInput"))

    @builtins.property
    @jsii.member(jsii_name="datacenterIdInput")
    def datacenter_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "datacenterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nicknameInput")
    def nickname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nicknameInput"))

    @builtins.property
    @jsii.member(jsii_name="asNumbers")
    def as_numbers(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "asNumbers"))

    @as_numbers.setter
    def as_numbers(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bca071a4d3b1a210432ba45786c725c8581e17b2941c2f9fecb9c8a98420d004)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "asNumbers", value)

    @builtins.property
    @jsii.member(jsii_name="datacenterId")
    def datacenter_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "datacenterId"))

    @datacenter_id.setter
    def datacenter_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8839796093d7a8b6a2a56c15b198102fd86dc8787d6a759b2ebda3d84a12e881)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datacenterId", value)

    @builtins.property
    @jsii.member(jsii_name="nickname")
    def nickname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nickname"))

    @nickname.setter
    def nickname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e133584fa1caa2edd56940819660fd41796f8811e4cbd9e6eb2c6ec74801550)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nickname", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GtmAsmapAssignment]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GtmAsmapAssignment]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GtmAsmapAssignment]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50f73b2fc2a2e866b591f58203e796a4d6386e4322cc979cd9c35e7fa5954186)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.gtmAsmap.GtmAsmapConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "default_datacenter": "defaultDatacenter",
        "domain": "domain",
        "name": "name",
        "assignment": "assignment",
        "id": "id",
        "wait_on_complete": "waitOnComplete",
    },
)
class GtmAsmapConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        default_datacenter: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GtmAsmapDefaultDatacenter", typing.Dict[builtins.str, typing.Any]]]],
        domain: builtins.str,
        name: builtins.str,
        assignment: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GtmAsmapAssignment, typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        wait_on_complete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param default_datacenter: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_asmap#default_datacenter GtmAsmap#default_datacenter}.
        :param domain: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_asmap#domain GtmAsmap#domain}.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_asmap#name GtmAsmap#name}.
        :param assignment: assignment block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_asmap#assignment GtmAsmap#assignment}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_asmap#id GtmAsmap#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param wait_on_complete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_asmap#wait_on_complete GtmAsmap#wait_on_complete}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb408ca24af384f9fc26a79a014387020c1ef886c1ea65539e4beb556580ddf0)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument default_datacenter", value=default_datacenter, expected_type=type_hints["default_datacenter"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument assignment", value=assignment, expected_type=type_hints["assignment"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument wait_on_complete", value=wait_on_complete, expected_type=type_hints["wait_on_complete"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "default_datacenter": default_datacenter,
            "domain": domain,
            "name": name,
        }
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
        if assignment is not None:
            self._values["assignment"] = assignment
        if id is not None:
            self._values["id"] = id
        if wait_on_complete is not None:
            self._values["wait_on_complete"] = wait_on_complete

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
    def default_datacenter(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GtmAsmapDefaultDatacenter"]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_asmap#default_datacenter GtmAsmap#default_datacenter}.'''
        result = self._values.get("default_datacenter")
        assert result is not None, "Required property 'default_datacenter' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GtmAsmapDefaultDatacenter"]], result)

    @builtins.property
    def domain(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_asmap#domain GtmAsmap#domain}.'''
        result = self._values.get("domain")
        assert result is not None, "Required property 'domain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_asmap#name GtmAsmap#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assignment(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmAsmapAssignment]]]:
        '''assignment block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_asmap#assignment GtmAsmap#assignment}
        '''
        result = self._values.get("assignment")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmAsmapAssignment]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_asmap#id GtmAsmap#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wait_on_complete(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_asmap#wait_on_complete GtmAsmap#wait_on_complete}.'''
        result = self._values.get("wait_on_complete")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GtmAsmapConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.gtmAsmap.GtmAsmapDefaultDatacenter",
    jsii_struct_bases=[],
    name_mapping={"datacenter_id": "datacenterId", "nickname": "nickname"},
)
class GtmAsmapDefaultDatacenter:
    def __init__(self, *, datacenter_id: jsii.Number, nickname: builtins.str) -> None:
        '''
        :param datacenter_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_asmap#datacenter_id GtmAsmap#datacenter_id}.
        :param nickname: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_asmap#nickname GtmAsmap#nickname}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42e5c5ccc7d91925930fc6fd26b8d1ebf20352680f48421e325b08eed01ed894)
            check_type(argname="argument datacenter_id", value=datacenter_id, expected_type=type_hints["datacenter_id"])
            check_type(argname="argument nickname", value=nickname, expected_type=type_hints["nickname"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "datacenter_id": datacenter_id,
            "nickname": nickname,
        }

    @builtins.property
    def datacenter_id(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_asmap#datacenter_id GtmAsmap#datacenter_id}.'''
        result = self._values.get("datacenter_id")
        assert result is not None, "Required property 'datacenter_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def nickname(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_asmap#nickname GtmAsmap#nickname}.'''
        result = self._values.get("nickname")
        assert result is not None, "Required property 'nickname' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GtmAsmapDefaultDatacenter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GtmAsmapDefaultDatacenterList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.gtmAsmap.GtmAsmapDefaultDatacenterList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c77cedf9afb0f4564607f4171063f2ca68fd84988a2cbcc6c3f79b59f8771573)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GtmAsmapDefaultDatacenterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65ce8a63ada493884f41244c76c6bd48c70b3ae01b5d324d3048a8e4245ad2cf)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GtmAsmapDefaultDatacenterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3847bc804b8998fc37a2b86d4c30ff39afe1ef66ee04bdd89ef8e03ee7ed5ee6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fe0a7588afcbda9465e7b759849fe3b4cf53f05965428df3de33358e9f6abd44)
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
            type_hints = typing.get_type_hints(_typecheckingstub__09e398dc345f0f1550a36c5f0d77f89149a72f5357937195ce4c353b087e8a95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmAsmapDefaultDatacenter]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmAsmapDefaultDatacenter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmAsmapDefaultDatacenter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8cdc7ab15dd82c8e2bf85e4c645792d69ecf84d57cf845b0e3e79f408a7c505)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GtmAsmapDefaultDatacenterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.gtmAsmap.GtmAsmapDefaultDatacenterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c8b265249b630d7278b0a376b70405fefa5e5c9f1a96ab81ee8fc95a6586cbf2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="datacenterIdInput")
    def datacenter_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "datacenterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nicknameInput")
    def nickname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nicknameInput"))

    @builtins.property
    @jsii.member(jsii_name="datacenterId")
    def datacenter_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "datacenterId"))

    @datacenter_id.setter
    def datacenter_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60e95170e319e54430dd198e74d8a794b864cf70809171fa0c38e514aceeb78f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datacenterId", value)

    @builtins.property
    @jsii.member(jsii_name="nickname")
    def nickname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nickname"))

    @nickname.setter
    def nickname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdf85526577a6da240f9df165e98d54b7f92f7abd2400e54d8c7252992401a5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nickname", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GtmAsmapDefaultDatacenter]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GtmAsmapDefaultDatacenter]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GtmAsmapDefaultDatacenter]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32415a04c89db7074a8a3419880e784d8574ffc43195506b4d72f7cb3da27986)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GtmAsmap",
    "GtmAsmapAssignment",
    "GtmAsmapAssignmentList",
    "GtmAsmapAssignmentOutputReference",
    "GtmAsmapConfig",
    "GtmAsmapDefaultDatacenter",
    "GtmAsmapDefaultDatacenterList",
    "GtmAsmapDefaultDatacenterOutputReference",
]

publication.publish()

def _typecheckingstub__5b67f3574eb22a72c48b06f1b257c3582a9074bf4f1e81d5f17a7a000e04701d(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    default_datacenter: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GtmAsmapDefaultDatacenter, typing.Dict[builtins.str, typing.Any]]]],
    domain: builtins.str,
    name: builtins.str,
    assignment: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GtmAsmapAssignment, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    wait_on_complete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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

def _typecheckingstub__39dc705b8705b5d68ccc845d0e71f4d54a535336e7f512937f164a1b25a4702c(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7357645f2af71a885ca866c6f17a1bae3237c9a67f66a832d0d450bb239866d0(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GtmAsmapAssignment, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b8c59dc9f1db5d2fc25ed85c8630645cebd711126592bb4038357ab461277ed(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GtmAsmapDefaultDatacenter, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__300ff800fe76d3cadb99008a2b7c8cf9e859697818fb8aa6e513a52b582d6bfd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0ae4d922a751463b06011df70738596cda51052b5b2e30e0c4bbbc009c19ff8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__940bf52ffe707870b3d6a9401f7ab32202be043c971f6b27189574c20f3c2de9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd103806fdcb38a2844044c1f4b7f44c062e07dc49c4654638ac1382a2759852(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88b64305466cbcff022a4c81af2545d3a83f356481fd8235fe75a745a569a155(
    *,
    as_numbers: typing.Sequence[jsii.Number],
    datacenter_id: jsii.Number,
    nickname: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5cb8b0f1b8d5183fd50e3cd0c250e52554a8a62ad1798a0001a8aa37212678b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64e7e6464e3184c7dbffbaffa61c4706aff0ec596933893b5e439648b0da4117(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b67cab0c0ce0fe173bd924462832198b8d59511c08b562cac50ad58d30cf1c6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eebccc636f9d339984480017de3735d89243c96c7c86d1c51add5ce1a8a0a632(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af5c4b760327c5bac91d03910f41d8a43c031551a3a61fd22c1177fec05e5776(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c21c8b654cfc84f596a8de9266a18e3092581e633762f01cea76c5abbcb5567f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmAsmapAssignment]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc089f83cc7dd947c94daf30813ccd937f833fab9ba4dbfad32d7e2b27e4e85c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bca071a4d3b1a210432ba45786c725c8581e17b2941c2f9fecb9c8a98420d004(
    value: typing.List[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8839796093d7a8b6a2a56c15b198102fd86dc8787d6a759b2ebda3d84a12e881(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e133584fa1caa2edd56940819660fd41796f8811e4cbd9e6eb2c6ec74801550(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50f73b2fc2a2e866b591f58203e796a4d6386e4322cc979cd9c35e7fa5954186(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GtmAsmapAssignment]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb408ca24af384f9fc26a79a014387020c1ef886c1ea65539e4beb556580ddf0(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    default_datacenter: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GtmAsmapDefaultDatacenter, typing.Dict[builtins.str, typing.Any]]]],
    domain: builtins.str,
    name: builtins.str,
    assignment: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GtmAsmapAssignment, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    wait_on_complete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42e5c5ccc7d91925930fc6fd26b8d1ebf20352680f48421e325b08eed01ed894(
    *,
    datacenter_id: jsii.Number,
    nickname: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c77cedf9afb0f4564607f4171063f2ca68fd84988a2cbcc6c3f79b59f8771573(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65ce8a63ada493884f41244c76c6bd48c70b3ae01b5d324d3048a8e4245ad2cf(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3847bc804b8998fc37a2b86d4c30ff39afe1ef66ee04bdd89ef8e03ee7ed5ee6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe0a7588afcbda9465e7b759849fe3b4cf53f05965428df3de33358e9f6abd44(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09e398dc345f0f1550a36c5f0d77f89149a72f5357937195ce4c353b087e8a95(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8cdc7ab15dd82c8e2bf85e4c645792d69ecf84d57cf845b0e3e79f408a7c505(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmAsmapDefaultDatacenter]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8b265249b630d7278b0a376b70405fefa5e5c9f1a96ab81ee8fc95a6586cbf2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60e95170e319e54430dd198e74d8a794b864cf70809171fa0c38e514aceeb78f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdf85526577a6da240f9df165e98d54b7f92f7abd2400e54d8c7252992401a5e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32415a04c89db7074a8a3419880e784d8574ffc43195506b4d72f7cb3da27986(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GtmAsmapDefaultDatacenter]],
) -> None:
    """Type checking stubs"""
    pass
