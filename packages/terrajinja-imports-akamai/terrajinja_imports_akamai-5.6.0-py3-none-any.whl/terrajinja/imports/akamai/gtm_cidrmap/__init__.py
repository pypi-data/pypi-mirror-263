'''
# `akamai_gtm_cidrmap`

Refer to the Terraform Registry for docs: [`akamai_gtm_cidrmap`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_cidrmap).
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


class GtmCidrmap(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.gtmCidrmap.GtmCidrmap",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_cidrmap akamai_gtm_cidrmap}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        default_datacenter: typing.Union["GtmCidrmapDefaultDatacenter", typing.Dict[builtins.str, typing.Any]],
        domain: builtins.str,
        name: builtins.str,
        assignment: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GtmCidrmapAssignment", typing.Dict[builtins.str, typing.Any]]]]] = None,
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
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_cidrmap akamai_gtm_cidrmap} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param default_datacenter: default_datacenter block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_cidrmap#default_datacenter GtmCidrmap#default_datacenter}
        :param domain: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_cidrmap#domain GtmCidrmap#domain}.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_cidrmap#name GtmCidrmap#name}.
        :param assignment: assignment block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_cidrmap#assignment GtmCidrmap#assignment}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_cidrmap#id GtmCidrmap#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param wait_on_complete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_cidrmap#wait_on_complete GtmCidrmap#wait_on_complete}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb66088d6aa12640873c09c7aaedf8e359c6870e1093534dc2c5fdbfe86a6e1b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GtmCidrmapConfig(
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
        '''Generates CDKTF code for importing a GtmCidrmap resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the GtmCidrmap to import.
        :param import_from_id: The id of the existing GtmCidrmap that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_cidrmap#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the GtmCidrmap to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5db3b8e51894c44a243a7e099b3d64284075cfccc249150c7e716e49cecb045c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putAssignment")
    def put_assignment(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GtmCidrmapAssignment", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c6f38f22e8e6889bd67633adbd1471af184e2fc189d1a3c1f9916303a47db1e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAssignment", [value]))

    @jsii.member(jsii_name="putDefaultDatacenter")
    def put_default_datacenter(
        self,
        *,
        datacenter_id: jsii.Number,
        nickname: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param datacenter_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_cidrmap#datacenter_id GtmCidrmap#datacenter_id}.
        :param nickname: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_cidrmap#nickname GtmCidrmap#nickname}.
        '''
        value = GtmCidrmapDefaultDatacenter(
            datacenter_id=datacenter_id, nickname=nickname
        )

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
    def assignment(self) -> "GtmCidrmapAssignmentList":
        return typing.cast("GtmCidrmapAssignmentList", jsii.get(self, "assignment"))

    @builtins.property
    @jsii.member(jsii_name="defaultDatacenter")
    def default_datacenter(self) -> "GtmCidrmapDefaultDatacenterOutputReference":
        return typing.cast("GtmCidrmapDefaultDatacenterOutputReference", jsii.get(self, "defaultDatacenter"))

    @builtins.property
    @jsii.member(jsii_name="assignmentInput")
    def assignment_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GtmCidrmapAssignment"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GtmCidrmapAssignment"]]], jsii.get(self, "assignmentInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultDatacenterInput")
    def default_datacenter_input(
        self,
    ) -> typing.Optional["GtmCidrmapDefaultDatacenter"]:
        return typing.cast(typing.Optional["GtmCidrmapDefaultDatacenter"], jsii.get(self, "defaultDatacenterInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__38a87bc556d8d3c9157bf210289afe7a15531a8573cb208af2ccb95d10086e22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f83eec7da026042bc240adf0f7053f6f6b356142226b8dbd9ffa5de337d94e10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8854381a67c47e3db6cb4b94e2cd53e4a062dcc8dbaae5eb14b10de991b3adf)
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
            type_hints = typing.get_type_hints(_typecheckingstub__daa2aff1e3685848f464eaca2b6bcc001fe8250b7e8989994ff84cf0a095bc5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitOnComplete", value)


@jsii.data_type(
    jsii_type="akamai.gtmCidrmap.GtmCidrmapAssignment",
    jsii_struct_bases=[],
    name_mapping={
        "datacenter_id": "datacenterId",
        "nickname": "nickname",
        "blocks": "blocks",
    },
)
class GtmCidrmapAssignment:
    def __init__(
        self,
        *,
        datacenter_id: jsii.Number,
        nickname: builtins.str,
        blocks: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param datacenter_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_cidrmap#datacenter_id GtmCidrmap#datacenter_id}.
        :param nickname: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_cidrmap#nickname GtmCidrmap#nickname}.
        :param blocks: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_cidrmap#blocks GtmCidrmap#blocks}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fed6fb69937e9eaaf2e71652982a8b95555a399874dd17e96770366e139163b9)
            check_type(argname="argument datacenter_id", value=datacenter_id, expected_type=type_hints["datacenter_id"])
            check_type(argname="argument nickname", value=nickname, expected_type=type_hints["nickname"])
            check_type(argname="argument blocks", value=blocks, expected_type=type_hints["blocks"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "datacenter_id": datacenter_id,
            "nickname": nickname,
        }
        if blocks is not None:
            self._values["blocks"] = blocks

    @builtins.property
    def datacenter_id(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_cidrmap#datacenter_id GtmCidrmap#datacenter_id}.'''
        result = self._values.get("datacenter_id")
        assert result is not None, "Required property 'datacenter_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def nickname(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_cidrmap#nickname GtmCidrmap#nickname}.'''
        result = self._values.get("nickname")
        assert result is not None, "Required property 'nickname' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def blocks(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_cidrmap#blocks GtmCidrmap#blocks}.'''
        result = self._values.get("blocks")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GtmCidrmapAssignment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GtmCidrmapAssignmentList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.gtmCidrmap.GtmCidrmapAssignmentList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8a0593e8ec39b6a32430cb9ae689227c708016d716c179b942f5fbc30df89a0e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GtmCidrmapAssignmentOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a474d735e235d448534254cd0fcaa6a086696fd4dfa95741fe5ac9db919d0e94)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GtmCidrmapAssignmentOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d43adfd88c2abe651fe96228542f19c466109a655adbf3076cfc0602e1b20d8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d7a7eae5bb8f24044bf09f1eb2c9f3547d745764742012da5ec058e45881443a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6afa37a1bf289927127b3a78f666c58d83261c8633d9260cbfda76848fe266ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmCidrmapAssignment]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmCidrmapAssignment]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmCidrmapAssignment]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b05091c32a8497761fc39585185f256dbebdd43cda91029d85ff80081b132488)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GtmCidrmapAssignmentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.gtmCidrmap.GtmCidrmapAssignmentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5a71600485babeec3a11db6e37498ca125e9e040eb544ace62ed6e3d4cfb6210)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetBlocks")
    def reset_blocks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlocks", []))

    @builtins.property
    @jsii.member(jsii_name="blocksInput")
    def blocks_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "blocksInput"))

    @builtins.property
    @jsii.member(jsii_name="datacenterIdInput")
    def datacenter_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "datacenterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nicknameInput")
    def nickname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nicknameInput"))

    @builtins.property
    @jsii.member(jsii_name="blocks")
    def blocks(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "blocks"))

    @blocks.setter
    def blocks(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88675ea5a6dc0d8bc136efcb46ba85c7a1f9f4e47217aa8d29d26a024649a327)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blocks", value)

    @builtins.property
    @jsii.member(jsii_name="datacenterId")
    def datacenter_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "datacenterId"))

    @datacenter_id.setter
    def datacenter_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__979f6757aace9fc82c5fa7c8db5ec03917c5f0f35812fec7f728ec76370ca1c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datacenterId", value)

    @builtins.property
    @jsii.member(jsii_name="nickname")
    def nickname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nickname"))

    @nickname.setter
    def nickname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__daa108039e2799d8d6070b1820ea9245af677e32efa9d847ed7b1ac0092fb560)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nickname", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GtmCidrmapAssignment]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GtmCidrmapAssignment]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GtmCidrmapAssignment]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed7a81d2aac30f6557731e747e73b00a464d9baa28be81fc75c9033672e37b10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.gtmCidrmap.GtmCidrmapConfig",
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
class GtmCidrmapConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        default_datacenter: typing.Union["GtmCidrmapDefaultDatacenter", typing.Dict[builtins.str, typing.Any]],
        domain: builtins.str,
        name: builtins.str,
        assignment: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GtmCidrmapAssignment, typing.Dict[builtins.str, typing.Any]]]]] = None,
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
        :param default_datacenter: default_datacenter block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_cidrmap#default_datacenter GtmCidrmap#default_datacenter}
        :param domain: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_cidrmap#domain GtmCidrmap#domain}.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_cidrmap#name GtmCidrmap#name}.
        :param assignment: assignment block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_cidrmap#assignment GtmCidrmap#assignment}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_cidrmap#id GtmCidrmap#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param wait_on_complete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_cidrmap#wait_on_complete GtmCidrmap#wait_on_complete}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(default_datacenter, dict):
            default_datacenter = GtmCidrmapDefaultDatacenter(**default_datacenter)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__402782dbf666d557a32851a2cca8d580f0dce14f5cfbda295e76156c7d11f9cd)
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
    def default_datacenter(self) -> "GtmCidrmapDefaultDatacenter":
        '''default_datacenter block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_cidrmap#default_datacenter GtmCidrmap#default_datacenter}
        '''
        result = self._values.get("default_datacenter")
        assert result is not None, "Required property 'default_datacenter' is missing"
        return typing.cast("GtmCidrmapDefaultDatacenter", result)

    @builtins.property
    def domain(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_cidrmap#domain GtmCidrmap#domain}.'''
        result = self._values.get("domain")
        assert result is not None, "Required property 'domain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_cidrmap#name GtmCidrmap#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assignment(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmCidrmapAssignment]]]:
        '''assignment block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_cidrmap#assignment GtmCidrmap#assignment}
        '''
        result = self._values.get("assignment")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmCidrmapAssignment]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_cidrmap#id GtmCidrmap#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wait_on_complete(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_cidrmap#wait_on_complete GtmCidrmap#wait_on_complete}.'''
        result = self._values.get("wait_on_complete")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GtmCidrmapConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.gtmCidrmap.GtmCidrmapDefaultDatacenter",
    jsii_struct_bases=[],
    name_mapping={"datacenter_id": "datacenterId", "nickname": "nickname"},
)
class GtmCidrmapDefaultDatacenter:
    def __init__(
        self,
        *,
        datacenter_id: jsii.Number,
        nickname: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param datacenter_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_cidrmap#datacenter_id GtmCidrmap#datacenter_id}.
        :param nickname: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_cidrmap#nickname GtmCidrmap#nickname}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be6336eec42a47359dc763ba3a8de80f62554fb6b5e8162320889e9f60ea5f85)
            check_type(argname="argument datacenter_id", value=datacenter_id, expected_type=type_hints["datacenter_id"])
            check_type(argname="argument nickname", value=nickname, expected_type=type_hints["nickname"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "datacenter_id": datacenter_id,
        }
        if nickname is not None:
            self._values["nickname"] = nickname

    @builtins.property
    def datacenter_id(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_cidrmap#datacenter_id GtmCidrmap#datacenter_id}.'''
        result = self._values.get("datacenter_id")
        assert result is not None, "Required property 'datacenter_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def nickname(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_cidrmap#nickname GtmCidrmap#nickname}.'''
        result = self._values.get("nickname")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GtmCidrmapDefaultDatacenter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GtmCidrmapDefaultDatacenterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.gtmCidrmap.GtmCidrmapDefaultDatacenterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bc5e1e7651739a604a3018420b52009815539f2da9707eb66e108877833ec776)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNickname")
    def reset_nickname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNickname", []))

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
            type_hints = typing.get_type_hints(_typecheckingstub__4c6d2d85331cfc77b1d13e7feef92e612244259d03a478cd2e3479a4d65b1e2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datacenterId", value)

    @builtins.property
    @jsii.member(jsii_name="nickname")
    def nickname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nickname"))

    @nickname.setter
    def nickname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22d21c177ea855ccedb7261e2abc16bde90d18ba3b3df4cedb1711d4922a8245)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nickname", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GtmCidrmapDefaultDatacenter]:
        return typing.cast(typing.Optional[GtmCidrmapDefaultDatacenter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GtmCidrmapDefaultDatacenter],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc011527b6ebd3ea9bb525e816827bf12f9f7cd3d64a2178bce2fe8659fc58d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GtmCidrmap",
    "GtmCidrmapAssignment",
    "GtmCidrmapAssignmentList",
    "GtmCidrmapAssignmentOutputReference",
    "GtmCidrmapConfig",
    "GtmCidrmapDefaultDatacenter",
    "GtmCidrmapDefaultDatacenterOutputReference",
]

publication.publish()

def _typecheckingstub__cb66088d6aa12640873c09c7aaedf8e359c6870e1093534dc2c5fdbfe86a6e1b(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    default_datacenter: typing.Union[GtmCidrmapDefaultDatacenter, typing.Dict[builtins.str, typing.Any]],
    domain: builtins.str,
    name: builtins.str,
    assignment: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GtmCidrmapAssignment, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__5db3b8e51894c44a243a7e099b3d64284075cfccc249150c7e716e49cecb045c(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c6f38f22e8e6889bd67633adbd1471af184e2fc189d1a3c1f9916303a47db1e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GtmCidrmapAssignment, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38a87bc556d8d3c9157bf210289afe7a15531a8573cb208af2ccb95d10086e22(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f83eec7da026042bc240adf0f7053f6f6b356142226b8dbd9ffa5de337d94e10(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8854381a67c47e3db6cb4b94e2cd53e4a062dcc8dbaae5eb14b10de991b3adf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daa2aff1e3685848f464eaca2b6bcc001fe8250b7e8989994ff84cf0a095bc5e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fed6fb69937e9eaaf2e71652982a8b95555a399874dd17e96770366e139163b9(
    *,
    datacenter_id: jsii.Number,
    nickname: builtins.str,
    blocks: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a0593e8ec39b6a32430cb9ae689227c708016d716c179b942f5fbc30df89a0e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a474d735e235d448534254cd0fcaa6a086696fd4dfa95741fe5ac9db919d0e94(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d43adfd88c2abe651fe96228542f19c466109a655adbf3076cfc0602e1b20d8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7a7eae5bb8f24044bf09f1eb2c9f3547d745764742012da5ec058e45881443a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6afa37a1bf289927127b3a78f666c58d83261c8633d9260cbfda76848fe266ff(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b05091c32a8497761fc39585185f256dbebdd43cda91029d85ff80081b132488(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmCidrmapAssignment]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a71600485babeec3a11db6e37498ca125e9e040eb544ace62ed6e3d4cfb6210(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88675ea5a6dc0d8bc136efcb46ba85c7a1f9f4e47217aa8d29d26a024649a327(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__979f6757aace9fc82c5fa7c8db5ec03917c5f0f35812fec7f728ec76370ca1c9(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daa108039e2799d8d6070b1820ea9245af677e32efa9d847ed7b1ac0092fb560(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed7a81d2aac30f6557731e747e73b00a464d9baa28be81fc75c9033672e37b10(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GtmCidrmapAssignment]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__402782dbf666d557a32851a2cca8d580f0dce14f5cfbda295e76156c7d11f9cd(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    default_datacenter: typing.Union[GtmCidrmapDefaultDatacenter, typing.Dict[builtins.str, typing.Any]],
    domain: builtins.str,
    name: builtins.str,
    assignment: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GtmCidrmapAssignment, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    wait_on_complete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be6336eec42a47359dc763ba3a8de80f62554fb6b5e8162320889e9f60ea5f85(
    *,
    datacenter_id: jsii.Number,
    nickname: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc5e1e7651739a604a3018420b52009815539f2da9707eb66e108877833ec776(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c6d2d85331cfc77b1d13e7feef92e612244259d03a478cd2e3479a4d65b1e2a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22d21c177ea855ccedb7261e2abc16bde90d18ba3b3df4cedb1711d4922a8245(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc011527b6ebd3ea9bb525e816827bf12f9f7cd3d64a2178bce2fe8659fc58d7(
    value: typing.Optional[GtmCidrmapDefaultDatacenter],
) -> None:
    """Type checking stubs"""
    pass
