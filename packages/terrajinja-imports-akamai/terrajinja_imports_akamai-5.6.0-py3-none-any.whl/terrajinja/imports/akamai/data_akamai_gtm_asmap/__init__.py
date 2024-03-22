'''
# `data_akamai_gtm_asmap`

Refer to the Terraform Registry for docs: [`data_akamai_gtm_asmap`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_asmap).
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


class DataAkamaiGtmAsmap(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmAsmap.DataAkamaiGtmAsmap",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_asmap akamai_gtm_asmap}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        domain: builtins.str,
        map_name: builtins.str,
        assignments: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmAsmapAssignments", typing.Dict[builtins.str, typing.Any]]]]] = None,
        links: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmAsmapLinks", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_asmap akamai_gtm_asmap} Data Source.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param domain: A descriptive label for the AS map. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_asmap#domain DataAkamaiGtmAsmap#domain}
        :param map_name: A descriptive label for the AS map. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_asmap#map_name DataAkamaiGtmAsmap#map_name}
        :param assignments: assignments block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_asmap#assignments DataAkamaiGtmAsmap#assignments}
        :param links: links block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_asmap#links DataAkamaiGtmAsmap#links}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc4972725a6d1b4bb8f8cbc9d5570c7fa155d3c4e813f3cf87b5192c3a44ef07)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = DataAkamaiGtmAsmapConfig(
            domain=domain,
            map_name=map_name,
            assignments=assignments,
            links=links,
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
        '''Generates CDKTF code for importing a DataAkamaiGtmAsmap resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the DataAkamaiGtmAsmap to import.
        :param import_from_id: The id of the existing DataAkamaiGtmAsmap that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_asmap#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the DataAkamaiGtmAsmap to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe408a9cfb46aae4f31554d0dd433c3ef665b6c7ee174e94c723712b797b6799)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putAssignments")
    def put_assignments(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmAsmapAssignments", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1145706d7a80c5484efde62d5413b0f0ac38bd7f36a2ed3c11d009c7b8b31786)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAssignments", [value]))

    @jsii.member(jsii_name="putLinks")
    def put_links(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmAsmapLinks", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__053efd29c31a0a2e06fe11f5bf639a579feb273364f665d58e5f962724078c9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLinks", [value]))

    @jsii.member(jsii_name="resetAssignments")
    def reset_assignments(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssignments", []))

    @jsii.member(jsii_name="resetLinks")
    def reset_links(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinks", []))

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
    @jsii.member(jsii_name="assignments")
    def assignments(self) -> "DataAkamaiGtmAsmapAssignmentsList":
        return typing.cast("DataAkamaiGtmAsmapAssignmentsList", jsii.get(self, "assignments"))

    @builtins.property
    @jsii.member(jsii_name="defaultDatacenter")
    def default_datacenter(
        self,
    ) -> "DataAkamaiGtmAsmapDefaultDatacenterOutputReference":
        return typing.cast("DataAkamaiGtmAsmapDefaultDatacenterOutputReference", jsii.get(self, "defaultDatacenter"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="links")
    def links(self) -> "DataAkamaiGtmAsmapLinksList":
        return typing.cast("DataAkamaiGtmAsmapLinksList", jsii.get(self, "links"))

    @builtins.property
    @jsii.member(jsii_name="assignmentsInput")
    def assignments_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmAsmapAssignments"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmAsmapAssignments"]]], jsii.get(self, "assignmentsInput"))

    @builtins.property
    @jsii.member(jsii_name="domainInput")
    def domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainInput"))

    @builtins.property
    @jsii.member(jsii_name="linksInput")
    def links_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmAsmapLinks"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmAsmapLinks"]]], jsii.get(self, "linksInput"))

    @builtins.property
    @jsii.member(jsii_name="mapNameInput")
    def map_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mapNameInput"))

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01199e44efd7f3c3ab9a856618f8095d2dd715985534f5fab27d12c9b085db72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)

    @builtins.property
    @jsii.member(jsii_name="mapName")
    def map_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mapName"))

    @map_name.setter
    def map_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f24300fcd4b27266c8703028c4a0cac739ee0c1ae53bc3cd19cf61c0bebbe996)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mapName", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiGtmAsmap.DataAkamaiGtmAsmapAssignments",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiGtmAsmapAssignments:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiGtmAsmapAssignments(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiGtmAsmapAssignmentsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmAsmap.DataAkamaiGtmAsmapAssignmentsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f71a8b9e2d980c6cf0d900fab4fa501b4900b4a3dfb5db5a1258f4f3b04a81d2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DataAkamaiGtmAsmapAssignmentsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__106192c490d89a3fd2c4f586afb3b9f1c3e4710e8348ee211bc58bc9f586a9a2)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiGtmAsmapAssignmentsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c57d4dc9dce9fe2187d57d52d6fac0e05e68604ed00d12249d68312d9a698282)
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
            type_hints = typing.get_type_hints(_typecheckingstub__af465d594efed23e153bbd36bcf7b6b69df163fe4479afa45d39abd811e3d750)
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
            type_hints = typing.get_type_hints(_typecheckingstub__538b4d6c7b2e5e39027895659fd020c662101b6523f438de7e32bfa0367ab965)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmAsmapAssignments]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmAsmapAssignments]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmAsmapAssignments]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26332ef0ca22ee18453b45faea9d30a7aa56a5dbf42752bbef7ceb5e2fd9cd4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiGtmAsmapAssignmentsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmAsmap.DataAkamaiGtmAsmapAssignmentsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c815cf9087cbf5db50a7985558e0cc8cb06caaff1f746fb086ce73930049a790)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="asNumbers")
    def as_numbers(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "asNumbers"))

    @builtins.property
    @jsii.member(jsii_name="datacenterId")
    def datacenter_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "datacenterId"))

    @builtins.property
    @jsii.member(jsii_name="nickname")
    def nickname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nickname"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmAsmapAssignments]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmAsmapAssignments]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmAsmapAssignments]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a309d78732fd552f1bca436977746c043b053eba4fd8f67bda5b19311854fb9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiGtmAsmap.DataAkamaiGtmAsmapConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "domain": "domain",
        "map_name": "mapName",
        "assignments": "assignments",
        "links": "links",
    },
)
class DataAkamaiGtmAsmapConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        domain: builtins.str,
        map_name: builtins.str,
        assignments: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmAsmapAssignments, typing.Dict[builtins.str, typing.Any]]]]] = None,
        links: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmAsmapLinks", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param domain: A descriptive label for the AS map. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_asmap#domain DataAkamaiGtmAsmap#domain}
        :param map_name: A descriptive label for the AS map. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_asmap#map_name DataAkamaiGtmAsmap#map_name}
        :param assignments: assignments block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_asmap#assignments DataAkamaiGtmAsmap#assignments}
        :param links: links block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_asmap#links DataAkamaiGtmAsmap#links}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3139cb4492c0901efcf9a8d27a027993f6a1920ae343db8341151a0e27c525c4)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            check_type(argname="argument map_name", value=map_name, expected_type=type_hints["map_name"])
            check_type(argname="argument assignments", value=assignments, expected_type=type_hints["assignments"])
            check_type(argname="argument links", value=links, expected_type=type_hints["links"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain": domain,
            "map_name": map_name,
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
        if assignments is not None:
            self._values["assignments"] = assignments
        if links is not None:
            self._values["links"] = links

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
    def domain(self) -> builtins.str:
        '''A descriptive label for the AS map.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_asmap#domain DataAkamaiGtmAsmap#domain}
        '''
        result = self._values.get("domain")
        assert result is not None, "Required property 'domain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def map_name(self) -> builtins.str:
        '''A descriptive label for the AS map.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_asmap#map_name DataAkamaiGtmAsmap#map_name}
        '''
        result = self._values.get("map_name")
        assert result is not None, "Required property 'map_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assignments(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmAsmapAssignments]]]:
        '''assignments block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_asmap#assignments DataAkamaiGtmAsmap#assignments}
        '''
        result = self._values.get("assignments")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmAsmapAssignments]]], result)

    @builtins.property
    def links(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmAsmapLinks"]]]:
        '''links block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_asmap#links DataAkamaiGtmAsmap#links}
        '''
        result = self._values.get("links")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmAsmapLinks"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiGtmAsmapConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dataAkamaiGtmAsmap.DataAkamaiGtmAsmapDefaultDatacenter",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiGtmAsmapDefaultDatacenter:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiGtmAsmapDefaultDatacenter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiGtmAsmapDefaultDatacenterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmAsmap.DataAkamaiGtmAsmapDefaultDatacenterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__077d223cea948b904a17058fe7c5077ef0cdd68acfad87d1cbe77ce8ef3758c4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="datacenterId")
    def datacenter_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "datacenterId"))

    @builtins.property
    @jsii.member(jsii_name="nickname")
    def nickname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nickname"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmAsmapDefaultDatacenter]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmAsmapDefaultDatacenter]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmAsmapDefaultDatacenter]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e96cd7642e95451ac102aac82724abe5150da5a3adf3112405d45b7770da34c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiGtmAsmap.DataAkamaiGtmAsmapLinks",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiGtmAsmapLinks:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiGtmAsmapLinks(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiGtmAsmapLinksList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmAsmap.DataAkamaiGtmAsmapLinksList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d57b1f9f066598b19c2bb900b1b6d90885fc195744d7c8573bef28b8073cb8ce)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DataAkamaiGtmAsmapLinksOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__087d492f2f522e7e1ebdbb83a4c80c259ca43c75a00b14c1376d93876bd3bf3d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiGtmAsmapLinksOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2eb7b4299cec04f6d033e9cc53e7a4446d4087f08973e301db98196eb3b43b21)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8098da75938b22f3e786552bb994fe2903a3377480c1fd183ac2f186f39d1fac)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4275a89ac49a2ba117a5266000f1ae668ce4be31c7983934e741b65bae08a594)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmAsmapLinks]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmAsmapLinks]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmAsmapLinks]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7611b521f65ca8e8f6db25f8da2227f41e679e653286b7d41cd572d3a6a622b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiGtmAsmapLinksOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmAsmap.DataAkamaiGtmAsmapLinksOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6712fc63cb2643b86e444c08d2ecdf8d512fb6a6b64804d8bb65d167f5f7b64a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="href")
    def href(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "href"))

    @builtins.property
    @jsii.member(jsii_name="rel")
    def rel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rel"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmAsmapLinks]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmAsmapLinks]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmAsmapLinks]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b446701ac6aabba839ffc4cb103a352a5b4aa384285d9f852de43409f4d12fff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataAkamaiGtmAsmap",
    "DataAkamaiGtmAsmapAssignments",
    "DataAkamaiGtmAsmapAssignmentsList",
    "DataAkamaiGtmAsmapAssignmentsOutputReference",
    "DataAkamaiGtmAsmapConfig",
    "DataAkamaiGtmAsmapDefaultDatacenter",
    "DataAkamaiGtmAsmapDefaultDatacenterOutputReference",
    "DataAkamaiGtmAsmapLinks",
    "DataAkamaiGtmAsmapLinksList",
    "DataAkamaiGtmAsmapLinksOutputReference",
]

publication.publish()

def _typecheckingstub__bc4972725a6d1b4bb8f8cbc9d5570c7fa155d3c4e813f3cf87b5192c3a44ef07(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain: builtins.str,
    map_name: builtins.str,
    assignments: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmAsmapAssignments, typing.Dict[builtins.str, typing.Any]]]]] = None,
    links: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmAsmapLinks, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__fe408a9cfb46aae4f31554d0dd433c3ef665b6c7ee174e94c723712b797b6799(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1145706d7a80c5484efde62d5413b0f0ac38bd7f36a2ed3c11d009c7b8b31786(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmAsmapAssignments, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__053efd29c31a0a2e06fe11f5bf639a579feb273364f665d58e5f962724078c9f(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmAsmapLinks, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01199e44efd7f3c3ab9a856618f8095d2dd715985534f5fab27d12c9b085db72(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f24300fcd4b27266c8703028c4a0cac739ee0c1ae53bc3cd19cf61c0bebbe996(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f71a8b9e2d980c6cf0d900fab4fa501b4900b4a3dfb5db5a1258f4f3b04a81d2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__106192c490d89a3fd2c4f586afb3b9f1c3e4710e8348ee211bc58bc9f586a9a2(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c57d4dc9dce9fe2187d57d52d6fac0e05e68604ed00d12249d68312d9a698282(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af465d594efed23e153bbd36bcf7b6b69df163fe4479afa45d39abd811e3d750(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__538b4d6c7b2e5e39027895659fd020c662101b6523f438de7e32bfa0367ab965(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26332ef0ca22ee18453b45faea9d30a7aa56a5dbf42752bbef7ceb5e2fd9cd4a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmAsmapAssignments]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c815cf9087cbf5db50a7985558e0cc8cb06caaff1f746fb086ce73930049a790(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a309d78732fd552f1bca436977746c043b053eba4fd8f67bda5b19311854fb9b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmAsmapAssignments]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3139cb4492c0901efcf9a8d27a027993f6a1920ae343db8341151a0e27c525c4(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    domain: builtins.str,
    map_name: builtins.str,
    assignments: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmAsmapAssignments, typing.Dict[builtins.str, typing.Any]]]]] = None,
    links: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmAsmapLinks, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__077d223cea948b904a17058fe7c5077ef0cdd68acfad87d1cbe77ce8ef3758c4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e96cd7642e95451ac102aac82724abe5150da5a3adf3112405d45b7770da34c6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmAsmapDefaultDatacenter]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d57b1f9f066598b19c2bb900b1b6d90885fc195744d7c8573bef28b8073cb8ce(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__087d492f2f522e7e1ebdbb83a4c80c259ca43c75a00b14c1376d93876bd3bf3d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2eb7b4299cec04f6d033e9cc53e7a4446d4087f08973e301db98196eb3b43b21(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8098da75938b22f3e786552bb994fe2903a3377480c1fd183ac2f186f39d1fac(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4275a89ac49a2ba117a5266000f1ae668ce4be31c7983934e741b65bae08a594(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7611b521f65ca8e8f6db25f8da2227f41e679e653286b7d41cd572d3a6a622b6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmAsmapLinks]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6712fc63cb2643b86e444c08d2ecdf8d512fb6a6b64804d8bb65d167f5f7b64a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b446701ac6aabba839ffc4cb103a352a5b4aa384285d9f852de43409f4d12fff(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmAsmapLinks]],
) -> None:
    """Type checking stubs"""
    pass
