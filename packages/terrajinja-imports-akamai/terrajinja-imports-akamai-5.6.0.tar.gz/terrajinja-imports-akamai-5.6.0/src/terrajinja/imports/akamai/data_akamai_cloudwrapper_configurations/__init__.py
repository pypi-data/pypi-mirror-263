'''
# `data_akamai_cloudwrapper_configurations`

Refer to the Terraform Registry for docs: [`data_akamai_cloudwrapper_configurations`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_configurations).
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


class DataAkamaiCloudwrapperConfigurations(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudwrapperConfigurations.DataAkamaiCloudwrapperConfigurations",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_configurations akamai_cloudwrapper_configurations}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        configurations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudwrapperConfigurationsConfigurations", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_configurations akamai_cloudwrapper_configurations} Data Source.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param configurations: configurations block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_configurations#configurations DataAkamaiCloudwrapperConfigurations#configurations}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7f759bc757ad69bccc90d8cc5b95e196a80c3da05b621843750b0b60d5dfd98)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = DataAkamaiCloudwrapperConfigurationsConfig(
            configurations=configurations,
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
        '''Generates CDKTF code for importing a DataAkamaiCloudwrapperConfigurations resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the DataAkamaiCloudwrapperConfigurations to import.
        :param import_from_id: The id of the existing DataAkamaiCloudwrapperConfigurations that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_configurations#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the DataAkamaiCloudwrapperConfigurations to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af422891fcc0878287b5ba1a1f0cec3f33ce0a11d5664f2fd66c01aa72cb680e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putConfigurations")
    def put_configurations(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudwrapperConfigurationsConfigurations", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7b5f2a5b3ab8eb1c0fc8d77c6cd3adb2a6c4584c6072a15aca454c8efe216df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putConfigurations", [value]))

    @jsii.member(jsii_name="resetConfigurations")
    def reset_configurations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigurations", []))

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
    @jsii.member(jsii_name="configurations")
    def configurations(
        self,
    ) -> "DataAkamaiCloudwrapperConfigurationsConfigurationsList":
        return typing.cast("DataAkamaiCloudwrapperConfigurationsConfigurationsList", jsii.get(self, "configurations"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="configurationsInput")
    def configurations_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudwrapperConfigurationsConfigurations"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudwrapperConfigurationsConfigurations"]]], jsii.get(self, "configurationsInput"))


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudwrapperConfigurations.DataAkamaiCloudwrapperConfigurationsConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "configurations": "configurations",
    },
)
class DataAkamaiCloudwrapperConfigurationsConfig(
    _cdktf_9a9027ec.TerraformMetaArguments,
):
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
        configurations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudwrapperConfigurationsConfigurations", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param configurations: configurations block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_configurations#configurations DataAkamaiCloudwrapperConfigurations#configurations}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4a5550436229cde8aeed1c6b4b743cf26ce02b12685060bca2945c8b45cb999)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument configurations", value=configurations, expected_type=type_hints["configurations"])
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
        if configurations is not None:
            self._values["configurations"] = configurations

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
    def configurations(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudwrapperConfigurationsConfigurations"]]]:
        '''configurations block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_configurations#configurations DataAkamaiCloudwrapperConfigurations#configurations}
        '''
        result = self._values.get("configurations")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudwrapperConfigurationsConfigurations"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudwrapperConfigurationsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudwrapperConfigurations.DataAkamaiCloudwrapperConfigurationsConfigurations",
    jsii_struct_bases=[],
    name_mapping={"locations": "locations"},
)
class DataAkamaiCloudwrapperConfigurationsConfigurations:
    def __init__(
        self,
        *,
        locations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudwrapperConfigurationsConfigurationsLocations", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param locations: locations block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_configurations#locations DataAkamaiCloudwrapperConfigurations#locations}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b4710f054c692037fd7955627f6f892c6cf7c6d9939f0371250e3ed34656db9)
            check_type(argname="argument locations", value=locations, expected_type=type_hints["locations"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if locations is not None:
            self._values["locations"] = locations

    @builtins.property
    def locations(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudwrapperConfigurationsConfigurationsLocations"]]]:
        '''locations block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_configurations#locations DataAkamaiCloudwrapperConfigurations#locations}
        '''
        result = self._values.get("locations")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudwrapperConfigurationsConfigurationsLocations"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudwrapperConfigurationsConfigurations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudwrapperConfigurationsConfigurationsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudwrapperConfigurations.DataAkamaiCloudwrapperConfigurationsConfigurationsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b060543d87c541facad70b6ae8a3dda003a5abeee648d3a2fc6ce70c50eb4751)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiCloudwrapperConfigurationsConfigurationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52cd52af2ed53f8376342eeaf1f05bdf41c62a309066ed240872f22d57928fd5)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiCloudwrapperConfigurationsConfigurationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__386bf3e31f0aa28c5c91a609f0ddbb35c74fe622b48c52bed9cb0a4b6150aabd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9751f82a9b6b0098107d40f88e04208b69b2b4cc2d24b740acd78dfdd069c0f5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6ae1d9f65705e8863af787aca0492e04cdc31f57b61d9eae19db0fd278b90a36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationsConfigurations]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationsConfigurations]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationsConfigurations]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf03ea1fc575aedf64e1030444253ed578cf61cc065ed68561aa3bb44c325eb7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudwrapperConfigurations.DataAkamaiCloudwrapperConfigurationsConfigurationsLocations",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiCloudwrapperConfigurationsConfigurationsLocations:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudwrapperConfigurationsConfigurationsLocations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudwrapperConfigurations.DataAkamaiCloudwrapperConfigurationsConfigurationsLocationsCapacity",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiCloudwrapperConfigurationsConfigurationsLocationsCapacity:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudwrapperConfigurationsConfigurationsLocationsCapacity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudwrapperConfigurationsConfigurationsLocationsCapacityOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudwrapperConfigurations.DataAkamaiCloudwrapperConfigurationsConfigurationsLocationsCapacityOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2e28d17f548e3516d0469922821b18b8cd9f22c0516f3ac94cb229eb8f1d2fc3)
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
    ) -> typing.Optional[DataAkamaiCloudwrapperConfigurationsConfigurationsLocationsCapacity]:
        return typing.cast(typing.Optional[DataAkamaiCloudwrapperConfigurationsConfigurationsLocationsCapacity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAkamaiCloudwrapperConfigurationsConfigurationsLocationsCapacity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__327c42347c9fe0f4b27ea54471886d1df1126fab09a1229706c1368a6007b082)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudwrapperConfigurationsConfigurationsLocationsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudwrapperConfigurations.DataAkamaiCloudwrapperConfigurationsConfigurationsLocationsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__02f90f5a47844936ae382a106fc5649629b7c1824cfb2ff927d757ac53e8f059)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiCloudwrapperConfigurationsConfigurationsLocationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec06e376f0575af3552b2c7ad80e263726ccd474ba74a745de1f32e07a97c1c8)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiCloudwrapperConfigurationsConfigurationsLocationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__951ce9cdc258968cdbcdcc37e68b0f976c57cc16e02fe89063c7f061c6378572)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ddbff0aa748ae05836914fc69869e23467272e84c439ece2670633b4bb7ab48a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1562cdf991a6f27be3e639ac53b0e2a99719164b5d0fa9e378c5d865a0dd8609)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationsConfigurationsLocations]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationsConfigurationsLocations]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationsConfigurationsLocations]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ed4815ff96a45edcb32bc93b09de0ccc19b1f82e20793d3e6f51a249f73a2fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudwrapperConfigurationsConfigurationsLocationsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudwrapperConfigurations.DataAkamaiCloudwrapperConfigurationsConfigurationsLocationsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__35fd1eec6a6888766b400575ee34741c923be8e8fd2acfec385c34d592695b95)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="capacity")
    def capacity(
        self,
    ) -> DataAkamaiCloudwrapperConfigurationsConfigurationsLocationsCapacityOutputReference:
        return typing.cast(DataAkamaiCloudwrapperConfigurationsConfigurationsLocationsCapacityOutputReference, jsii.get(self, "capacity"))

    @builtins.property
    @jsii.member(jsii_name="comments")
    def comments(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comments"))

    @builtins.property
    @jsii.member(jsii_name="mapName")
    def map_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mapName"))

    @builtins.property
    @jsii.member(jsii_name="trafficTypeId")
    def traffic_type_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "trafficTypeId"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationsConfigurationsLocations]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationsConfigurationsLocations]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationsConfigurationsLocations]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77c2e959d6fc194b0a391de7f617e4fe681c1e5a10067febc1f20b45e309a77c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudwrapperConfigurations.DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettings",
    jsii_struct_bases=[],
    name_mapping={"cdns": "cdns", "origins": "origins"},
)
class DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettings:
    def __init__(
        self,
        *,
        cdns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdns", typing.Dict[builtins.str, typing.Any]]]]] = None,
        origins: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsOrigins", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param cdns: cdns block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_configurations#cdns DataAkamaiCloudwrapperConfigurations#cdns}
        :param origins: origins block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_configurations#origins DataAkamaiCloudwrapperConfigurations#origins}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__191be6913c165ec50f3479fd03e894478749bf02450d5ef6c7b8bd51bdf1f999)
            check_type(argname="argument cdns", value=cdns, expected_type=type_hints["cdns"])
            check_type(argname="argument origins", value=origins, expected_type=type_hints["origins"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cdns is not None:
            self._values["cdns"] = cdns
        if origins is not None:
            self._values["origins"] = origins

    @builtins.property
    def cdns(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdns"]]]:
        '''cdns block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_configurations#cdns DataAkamaiCloudwrapperConfigurations#cdns}
        '''
        result = self._values.get("cdns")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdns"]]], result)

    @builtins.property
    def origins(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsOrigins"]]]:
        '''origins block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_configurations#origins DataAkamaiCloudwrapperConfigurations#origins}
        '''
        result = self._values.get("origins")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsOrigins"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudwrapperConfigurations.DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsBocc",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsBocc:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsBocc(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsBoccOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudwrapperConfigurations.DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsBoccOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__846a8b2fe4e72b6d5f6cb8916d4b2d623911f275c773a174a3d34ac1847348cf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="conditionalSamplingFrequency")
    def conditional_sampling_frequency(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "conditionalSamplingFrequency"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "enabled"))

    @builtins.property
    @jsii.member(jsii_name="forwardType")
    def forward_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "forwardType"))

    @builtins.property
    @jsii.member(jsii_name="requestType")
    def request_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "requestType"))

    @builtins.property
    @jsii.member(jsii_name="samplingFrequency")
    def sampling_frequency(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "samplingFrequency"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsBocc]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsBocc]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsBocc]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__844449d8568700a27233a0d0d8f897aa1d4c85c06400092b4ab0366fce9bf8b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudwrapperConfigurations.DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdns",
    jsii_struct_bases=[],
    name_mapping={"cdn_auth_keys": "cdnAuthKeys"},
)
class DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdns:
    def __init__(
        self,
        *,
        cdn_auth_keys: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsCdnAuthKeys", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param cdn_auth_keys: cdn_auth_keys block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_configurations#cdn_auth_keys DataAkamaiCloudwrapperConfigurations#cdn_auth_keys}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4735bfc82a7356ee1a372cf70312702428e3b88b081b69b421c325407838d15)
            check_type(argname="argument cdn_auth_keys", value=cdn_auth_keys, expected_type=type_hints["cdn_auth_keys"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cdn_auth_keys is not None:
            self._values["cdn_auth_keys"] = cdn_auth_keys

    @builtins.property
    def cdn_auth_keys(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsCdnAuthKeys"]]]:
        '''cdn_auth_keys block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_configurations#cdn_auth_keys DataAkamaiCloudwrapperConfigurations#cdn_auth_keys}
        '''
        result = self._values.get("cdn_auth_keys")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsCdnAuthKeys"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudwrapperConfigurations.DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsCdnAuthKeys",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsCdnAuthKeys:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsCdnAuthKeys(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsCdnAuthKeysList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudwrapperConfigurations.DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsCdnAuthKeysList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2b07a6570e2facc07c49dce4e4e6aec04f72535ac1ce86e44a29c8b035e074b3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsCdnAuthKeysOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5b6534175e6e01b98a4217404c2ef87a337993904c1f1177de2f2946553d2b5)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsCdnAuthKeysOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2c8c983213bc8364a08a16d9fe21c3bb075e1d33261b6dee102b457091e968e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__916acac431ccc2c9609bbd90a2e393252205512e8d391e2a7d59a7801479757a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a53c87fc819fc0f0bc5df6706d4e3fee05adbe593e37dd1f5704b83c9b8866c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsCdnAuthKeys]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsCdnAuthKeys]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsCdnAuthKeys]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44e0be5fbd9f9798e6a06cfb687617decd8d9650dd4ecdc08b5561f59e184a6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsCdnAuthKeysOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudwrapperConfigurations.DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsCdnAuthKeysOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__27e02039e970bcb7c515e5885da53a8bc1e08792a2c241371e9607700ea9eb83)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="authKeyName")
    def auth_key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authKeyName"))

    @builtins.property
    @jsii.member(jsii_name="expiryDate")
    def expiry_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expiryDate"))

    @builtins.property
    @jsii.member(jsii_name="headerName")
    def header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerName"))

    @builtins.property
    @jsii.member(jsii_name="secret")
    def secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secret"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsCdnAuthKeys]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsCdnAuthKeys]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsCdnAuthKeys]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f4131bfb0ecb27f523a19bfb5f6bf1ee05912d09aaf75d777e968f7ed24ba8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudwrapperConfigurations.DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__16e1c4b3e59eb8d36a0d15e7e551687ec1b3beb9e86aae2578b823b8cc3c1c0e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__046690ea32bff5b1f201304d855e13c1424b0b0ea435fbcafbee91a46b876be8)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__414019e2ee7ea8280e0d89e8dc53e2c83304ac3322cee271ab1d9cf80bbf2107)
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
            type_hints = typing.get_type_hints(_typecheckingstub__552f711293e06abc347265ba40bfd64d71005a0f834c21daabf4095b6ffb4fba)
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
            type_hints = typing.get_type_hints(_typecheckingstub__119587644c7c359ec95ddede404cc528d8c7320a862ef4e4dd6387cdbc0b0843)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdns]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdns]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b180afc1140414dda3156afd3d2b0bd8c93e60e7573f5211093a52f02a6f750a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudwrapperConfigurations.DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1001a394dbc03bc781fed9da3325cb489333460d99e25f3ec3845f115de42b6e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCdnAuthKeys")
    def put_cdn_auth_keys(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsCdnAuthKeys, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cdac9fc0c7231704ae6f06602c67882b71f9c980436718c6dc0c4514f0c7d0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCdnAuthKeys", [value]))

    @jsii.member(jsii_name="resetCdnAuthKeys")
    def reset_cdn_auth_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCdnAuthKeys", []))

    @builtins.property
    @jsii.member(jsii_name="cdnAuthKeys")
    def cdn_auth_keys(
        self,
    ) -> DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsCdnAuthKeysList:
        return typing.cast(DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsCdnAuthKeysList, jsii.get(self, "cdnAuthKeys"))

    @builtins.property
    @jsii.member(jsii_name="cdnCode")
    def cdn_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cdnCode"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "enabled"))

    @builtins.property
    @jsii.member(jsii_name="httpsOnly")
    def https_only(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "httpsOnly"))

    @builtins.property
    @jsii.member(jsii_name="ipAclCidrs")
    def ip_acl_cidrs(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipAclCidrs"))

    @builtins.property
    @jsii.member(jsii_name="cdnAuthKeysInput")
    def cdn_auth_keys_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsCdnAuthKeys]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsCdnAuthKeys]]], jsii.get(self, "cdnAuthKeysInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdns]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdns]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdns]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c32b9657eb85adab16b200deb3740c0842ac22f6f4cabe5664d6278bdb63663a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudwrapperConfigurations.DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsDataStreams",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsDataStreams:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsDataStreams(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsDataStreamsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudwrapperConfigurations.DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsDataStreamsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__86961abad4cc832c0e3e8d54be03dcd6a3fcc1a8e0ade981f9bdfa881670d58f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="dataStreamIds")
    def data_stream_ids(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "dataStreamIds"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "enabled"))

    @builtins.property
    @jsii.member(jsii_name="samplingRate")
    def sampling_rate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "samplingRate"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsDataStreams]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsDataStreams]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsDataStreams]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61aaaac835c9d3bc721cd8fe6ff22e46b9ede66a670ba6f0b45b12bd2579bc4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudwrapperConfigurations.DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsOrigins",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsOrigins:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsOrigins(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsOriginsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudwrapperConfigurations.DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsOriginsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__44043aaae21fd14fb6480d1aa9b112c834e4ad2555821dfe35d8dff74d5a986b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsOriginsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfa021fc3afe52a4c3852af46dd71be64b55e98a56a2a667d150c9392f3471ef)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsOriginsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__997246540192f6806aba577a9285c7a75be2e909d841a0970266cacab68d80be)
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
            type_hints = typing.get_type_hints(_typecheckingstub__015a17860175898a4e80fa781b272c1a6f5093d71f87f51634cfdd69cccc8139)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6fe934303bcd978ad2e011e9e03252d3fee6ebf88576bfbe2107638225fb0035)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsOrigins]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsOrigins]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsOrigins]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9294b0b3d64658fce8af6099d5164556219570269fb423eaf7c83e5a978a5c49)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsOriginsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudwrapperConfigurations.DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsOriginsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5672bedc3921f762b103d97cf80b46638ee01437333ecdaac8fb127cf75e5f7b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostname"))

    @builtins.property
    @jsii.member(jsii_name="originId")
    def origin_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "originId"))

    @builtins.property
    @jsii.member(jsii_name="propertyId")
    def property_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "propertyId"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsOrigins]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsOrigins]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsOrigins]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f5868ee733de0c02e2aa20fe890748e6fc473a78da32c61b34b6b547fed227a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudwrapperConfigurations.DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cc9e5ba81c4e7b3bc8f63035cf98b0397e4c1b5004a237baa8de15889db30d9f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCdns")
    def put_cdns(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdns, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55ac8d8bf7444a796cc6c20d4ec014e440fd646e966804731c54dcf0c3fcce83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCdns", [value]))

    @jsii.member(jsii_name="putOrigins")
    def put_origins(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsOrigins, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9db12d3ebe74fd58dd32a4b6979a8a15f1aeb6f7826a3c8ac670309d3ce5974e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOrigins", [value]))

    @jsii.member(jsii_name="resetCdns")
    def reset_cdns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCdns", []))

    @jsii.member(jsii_name="resetOrigins")
    def reset_origins(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrigins", []))

    @builtins.property
    @jsii.member(jsii_name="bocc")
    def bocc(
        self,
    ) -> DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsBoccOutputReference:
        return typing.cast(DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsBoccOutputReference, jsii.get(self, "bocc"))

    @builtins.property
    @jsii.member(jsii_name="cdns")
    def cdns(
        self,
    ) -> DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsList:
        return typing.cast(DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsList, jsii.get(self, "cdns"))

    @builtins.property
    @jsii.member(jsii_name="dataStreams")
    def data_streams(
        self,
    ) -> DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsDataStreamsOutputReference:
        return typing.cast(DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsDataStreamsOutputReference, jsii.get(self, "dataStreams"))

    @builtins.property
    @jsii.member(jsii_name="enableSoftAlerts")
    def enable_soft_alerts(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "enableSoftAlerts"))

    @builtins.property
    @jsii.member(jsii_name="origins")
    def origins(
        self,
    ) -> DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsOriginsList:
        return typing.cast(DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsOriginsList, jsii.get(self, "origins"))

    @builtins.property
    @jsii.member(jsii_name="cdnsInput")
    def cdns_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdns]]], jsii.get(self, "cdnsInput"))

    @builtins.property
    @jsii.member(jsii_name="originsInput")
    def origins_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsOrigins]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsOrigins]]], jsii.get(self, "originsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettings]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettings]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettings]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cf28612a1e67b001839997c14707b58c4d622788bd9f4e21326a05a8f0f72be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudwrapperConfigurationsConfigurationsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudwrapperConfigurations.DataAkamaiCloudwrapperConfigurationsConfigurationsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1e2fe6e16876c63168dc11fc3ca73417fe57f74f063fbec10200c42d4f24dd86)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putLocations")
    def put_locations(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudwrapperConfigurationsConfigurationsLocations, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c4c6bc5d95f6ffe6f20f0c18330dd657e88983df83a3e1fea91dcec5033415a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLocations", [value]))

    @jsii.member(jsii_name="resetLocations")
    def reset_locations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocations", []))

    @builtins.property
    @jsii.member(jsii_name="capacityAlertsThreshold")
    def capacity_alerts_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "capacityAlertsThreshold"))

    @builtins.property
    @jsii.member(jsii_name="comments")
    def comments(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comments"))

    @builtins.property
    @jsii.member(jsii_name="configName")
    def config_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configName"))

    @builtins.property
    @jsii.member(jsii_name="contractId")
    def contract_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contractId"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="lastActivatedBy")
    def last_activated_by(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastActivatedBy"))

    @builtins.property
    @jsii.member(jsii_name="lastActivatedDate")
    def last_activated_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastActivatedDate"))

    @builtins.property
    @jsii.member(jsii_name="lastUpdatedBy")
    def last_updated_by(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastUpdatedBy"))

    @builtins.property
    @jsii.member(jsii_name="lastUpdatedDate")
    def last_updated_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastUpdatedDate"))

    @builtins.property
    @jsii.member(jsii_name="locations")
    def locations(
        self,
    ) -> DataAkamaiCloudwrapperConfigurationsConfigurationsLocationsList:
        return typing.cast(DataAkamaiCloudwrapperConfigurationsConfigurationsLocationsList, jsii.get(self, "locations"))

    @builtins.property
    @jsii.member(jsii_name="multiCdnSettings")
    def multi_cdn_settings(
        self,
    ) -> DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsOutputReference:
        return typing.cast(DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsOutputReference, jsii.get(self, "multiCdnSettings"))

    @builtins.property
    @jsii.member(jsii_name="notificationEmails")
    def notification_emails(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "notificationEmails"))

    @builtins.property
    @jsii.member(jsii_name="propertyIds")
    def property_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "propertyIds"))

    @builtins.property
    @jsii.member(jsii_name="retainIdleObjects")
    def retain_idle_objects(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "retainIdleObjects"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="locationsInput")
    def locations_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationsConfigurationsLocations]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationsConfigurationsLocations]]], jsii.get(self, "locationsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationsConfigurations]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationsConfigurations]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationsConfigurations]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e0897cc24d3cc2d17c6770b891994e74d7c223530f6926ebf4bacbe852580fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataAkamaiCloudwrapperConfigurations",
    "DataAkamaiCloudwrapperConfigurationsConfig",
    "DataAkamaiCloudwrapperConfigurationsConfigurations",
    "DataAkamaiCloudwrapperConfigurationsConfigurationsList",
    "DataAkamaiCloudwrapperConfigurationsConfigurationsLocations",
    "DataAkamaiCloudwrapperConfigurationsConfigurationsLocationsCapacity",
    "DataAkamaiCloudwrapperConfigurationsConfigurationsLocationsCapacityOutputReference",
    "DataAkamaiCloudwrapperConfigurationsConfigurationsLocationsList",
    "DataAkamaiCloudwrapperConfigurationsConfigurationsLocationsOutputReference",
    "DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettings",
    "DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsBocc",
    "DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsBoccOutputReference",
    "DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdns",
    "DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsCdnAuthKeys",
    "DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsCdnAuthKeysList",
    "DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsCdnAuthKeysOutputReference",
    "DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsList",
    "DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsOutputReference",
    "DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsDataStreams",
    "DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsDataStreamsOutputReference",
    "DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsOrigins",
    "DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsOriginsList",
    "DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsOriginsOutputReference",
    "DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsOutputReference",
    "DataAkamaiCloudwrapperConfigurationsConfigurationsOutputReference",
]

publication.publish()

def _typecheckingstub__d7f759bc757ad69bccc90d8cc5b95e196a80c3da05b621843750b0b60d5dfd98(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    configurations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudwrapperConfigurationsConfigurations, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__af422891fcc0878287b5ba1a1f0cec3f33ce0a11d5664f2fd66c01aa72cb680e(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7b5f2a5b3ab8eb1c0fc8d77c6cd3adb2a6c4584c6072a15aca454c8efe216df(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudwrapperConfigurationsConfigurations, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4a5550436229cde8aeed1c6b4b743cf26ce02b12685060bca2945c8b45cb999(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    configurations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudwrapperConfigurationsConfigurations, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b4710f054c692037fd7955627f6f892c6cf7c6d9939f0371250e3ed34656db9(
    *,
    locations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudwrapperConfigurationsConfigurationsLocations, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b060543d87c541facad70b6ae8a3dda003a5abeee648d3a2fc6ce70c50eb4751(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52cd52af2ed53f8376342eeaf1f05bdf41c62a309066ed240872f22d57928fd5(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__386bf3e31f0aa28c5c91a609f0ddbb35c74fe622b48c52bed9cb0a4b6150aabd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9751f82a9b6b0098107d40f88e04208b69b2b4cc2d24b740acd78dfdd069c0f5(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ae1d9f65705e8863af787aca0492e04cdc31f57b61d9eae19db0fd278b90a36(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf03ea1fc575aedf64e1030444253ed578cf61cc065ed68561aa3bb44c325eb7(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationsConfigurations]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e28d17f548e3516d0469922821b18b8cd9f22c0516f3ac94cb229eb8f1d2fc3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__327c42347c9fe0f4b27ea54471886d1df1126fab09a1229706c1368a6007b082(
    value: typing.Optional[DataAkamaiCloudwrapperConfigurationsConfigurationsLocationsCapacity],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02f90f5a47844936ae382a106fc5649629b7c1824cfb2ff927d757ac53e8f059(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec06e376f0575af3552b2c7ad80e263726ccd474ba74a745de1f32e07a97c1c8(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__951ce9cdc258968cdbcdcc37e68b0f976c57cc16e02fe89063c7f061c6378572(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddbff0aa748ae05836914fc69869e23467272e84c439ece2670633b4bb7ab48a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1562cdf991a6f27be3e639ac53b0e2a99719164b5d0fa9e378c5d865a0dd8609(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ed4815ff96a45edcb32bc93b09de0ccc19b1f82e20793d3e6f51a249f73a2fe(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationsConfigurationsLocations]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35fd1eec6a6888766b400575ee34741c923be8e8fd2acfec385c34d592695b95(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77c2e959d6fc194b0a391de7f617e4fe681c1e5a10067febc1f20b45e309a77c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationsConfigurationsLocations]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__191be6913c165ec50f3479fd03e894478749bf02450d5ef6c7b8bd51bdf1f999(
    *,
    cdns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdns, typing.Dict[builtins.str, typing.Any]]]]] = None,
    origins: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsOrigins, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__846a8b2fe4e72b6d5f6cb8916d4b2d623911f275c773a174a3d34ac1847348cf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__844449d8568700a27233a0d0d8f897aa1d4c85c06400092b4ab0366fce9bf8b2(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsBocc]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4735bfc82a7356ee1a372cf70312702428e3b88b081b69b421c325407838d15(
    *,
    cdn_auth_keys: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsCdnAuthKeys, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b07a6570e2facc07c49dce4e4e6aec04f72535ac1ce86e44a29c8b035e074b3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5b6534175e6e01b98a4217404c2ef87a337993904c1f1177de2f2946553d2b5(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2c8c983213bc8364a08a16d9fe21c3bb075e1d33261b6dee102b457091e968e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__916acac431ccc2c9609bbd90a2e393252205512e8d391e2a7d59a7801479757a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a53c87fc819fc0f0bc5df6706d4e3fee05adbe593e37dd1f5704b83c9b8866c6(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44e0be5fbd9f9798e6a06cfb687617decd8d9650dd4ecdc08b5561f59e184a6b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsCdnAuthKeys]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27e02039e970bcb7c515e5885da53a8bc1e08792a2c241371e9607700ea9eb83(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f4131bfb0ecb27f523a19bfb5f6bf1ee05912d09aaf75d777e968f7ed24ba8d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsCdnAuthKeys]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16e1c4b3e59eb8d36a0d15e7e551687ec1b3beb9e86aae2578b823b8cc3c1c0e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__046690ea32bff5b1f201304d855e13c1424b0b0ea435fbcafbee91a46b876be8(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__414019e2ee7ea8280e0d89e8dc53e2c83304ac3322cee271ab1d9cf80bbf2107(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__552f711293e06abc347265ba40bfd64d71005a0f834c21daabf4095b6ffb4fba(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__119587644c7c359ec95ddede404cc528d8c7320a862ef4e4dd6387cdbc0b0843(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b180afc1140414dda3156afd3d2b0bd8c93e60e7573f5211093a52f02a6f750a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdns]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1001a394dbc03bc781fed9da3325cb489333460d99e25f3ec3845f115de42b6e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cdac9fc0c7231704ae6f06602c67882b71f9c980436718c6dc0c4514f0c7d0c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdnsCdnAuthKeys, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c32b9657eb85adab16b200deb3740c0842ac22f6f4cabe5664d6278bdb63663a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdns]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86961abad4cc832c0e3e8d54be03dcd6a3fcc1a8e0ade981f9bdfa881670d58f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61aaaac835c9d3bc721cd8fe6ff22e46b9ede66a670ba6f0b45b12bd2579bc4a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsDataStreams]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44043aaae21fd14fb6480d1aa9b112c834e4ad2555821dfe35d8dff74d5a986b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfa021fc3afe52a4c3852af46dd71be64b55e98a56a2a667d150c9392f3471ef(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__997246540192f6806aba577a9285c7a75be2e909d841a0970266cacab68d80be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__015a17860175898a4e80fa781b272c1a6f5093d71f87f51634cfdd69cccc8139(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fe934303bcd978ad2e011e9e03252d3fee6ebf88576bfbe2107638225fb0035(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9294b0b3d64658fce8af6099d5164556219570269fb423eaf7c83e5a978a5c49(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsOrigins]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5672bedc3921f762b103d97cf80b46638ee01437333ecdaac8fb127cf75e5f7b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f5868ee733de0c02e2aa20fe890748e6fc473a78da32c61b34b6b547fed227a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsOrigins]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc9e5ba81c4e7b3bc8f63035cf98b0397e4c1b5004a237baa8de15889db30d9f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55ac8d8bf7444a796cc6c20d4ec014e440fd646e966804731c54dcf0c3fcce83(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsCdns, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9db12d3ebe74fd58dd32a4b6979a8a15f1aeb6f7826a3c8ac670309d3ce5974e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettingsOrigins, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cf28612a1e67b001839997c14707b58c4d622788bd9f4e21326a05a8f0f72be(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationsConfigurationsMultiCdnSettings]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e2fe6e16876c63168dc11fc3ca73417fe57f74f063fbec10200c42d4f24dd86(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c4c6bc5d95f6ffe6f20f0c18330dd657e88983df83a3e1fea91dcec5033415a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudwrapperConfigurationsConfigurationsLocations, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e0897cc24d3cc2d17c6770b891994e74d7c223530f6926ebf4bacbe852580fe(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationsConfigurations]],
) -> None:
    """Type checking stubs"""
    pass
