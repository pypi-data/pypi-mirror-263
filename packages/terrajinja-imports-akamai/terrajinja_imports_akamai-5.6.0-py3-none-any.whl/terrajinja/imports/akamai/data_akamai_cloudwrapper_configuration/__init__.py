'''
# `data_akamai_cloudwrapper_configuration`

Refer to the Terraform Registry for docs: [`data_akamai_cloudwrapper_configuration`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_configuration).
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


class DataAkamaiCloudwrapperConfiguration(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudwrapperConfiguration.DataAkamaiCloudwrapperConfiguration",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_configuration akamai_cloudwrapper_configuration}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        id: jsii.Number,
        locations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudwrapperConfigurationLocations", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_configuration akamai_cloudwrapper_configuration} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param id: Unique identifier of a Cloud Wrapper configuration. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_configuration#id DataAkamaiCloudwrapperConfiguration#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param locations: locations block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_configuration#locations DataAkamaiCloudwrapperConfiguration#locations}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__908f013e7a40173c924269f02e2a7c102a35a1b27278741167474682da7928ab)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAkamaiCloudwrapperConfigurationConfig(
            id=id,
            locations=locations,
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
        '''Generates CDKTF code for importing a DataAkamaiCloudwrapperConfiguration resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the DataAkamaiCloudwrapperConfiguration to import.
        :param import_from_id: The id of the existing DataAkamaiCloudwrapperConfiguration that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_configuration#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the DataAkamaiCloudwrapperConfiguration to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53821edf12773d891f745feae10b7f5ffd580fd40ee0237de20b53df894adc7e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putLocations")
    def put_locations(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudwrapperConfigurationLocations", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b38fc0208a27f9149d3c2f0b4a1e857a640362d3282370489add51af3155a64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLocations", [value]))

    @jsii.member(jsii_name="resetLocations")
    def reset_locations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocations", []))

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
    def locations(self) -> "DataAkamaiCloudwrapperConfigurationLocationsList":
        return typing.cast("DataAkamaiCloudwrapperConfigurationLocationsList", jsii.get(self, "locations"))

    @builtins.property
    @jsii.member(jsii_name="multiCdnSettings")
    def multi_cdn_settings(
        self,
    ) -> "DataAkamaiCloudwrapperConfigurationMultiCdnSettingsOutputReference":
        return typing.cast("DataAkamaiCloudwrapperConfigurationMultiCdnSettingsOutputReference", jsii.get(self, "multiCdnSettings"))

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
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationsInput")
    def locations_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudwrapperConfigurationLocations"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudwrapperConfigurationLocations"]]], jsii.get(self, "locationsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "id"))

    @id.setter
    def id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cefc335190542ee252449063c5fa6b59e6dac10d8f291602e9866a3fb861273)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudwrapperConfiguration.DataAkamaiCloudwrapperConfigurationConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "id": "id",
        "locations": "locations",
    },
)
class DataAkamaiCloudwrapperConfigurationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        id: jsii.Number,
        locations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudwrapperConfigurationLocations", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param id: Unique identifier of a Cloud Wrapper configuration. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_configuration#id DataAkamaiCloudwrapperConfiguration#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param locations: locations block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_configuration#locations DataAkamaiCloudwrapperConfiguration#locations}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55ce752f4c7265d2b1239dbebcc9564e06033592a3fb09583bc3d0e7b1c4e43e)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument locations", value=locations, expected_type=type_hints["locations"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
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
        if locations is not None:
            self._values["locations"] = locations

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
    def id(self) -> jsii.Number:
        '''Unique identifier of a Cloud Wrapper configuration.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_configuration#id DataAkamaiCloudwrapperConfiguration#id}

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def locations(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudwrapperConfigurationLocations"]]]:
        '''locations block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_configuration#locations DataAkamaiCloudwrapperConfiguration#locations}
        '''
        result = self._values.get("locations")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudwrapperConfigurationLocations"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudwrapperConfigurationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudwrapperConfiguration.DataAkamaiCloudwrapperConfigurationLocations",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiCloudwrapperConfigurationLocations:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudwrapperConfigurationLocations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudwrapperConfiguration.DataAkamaiCloudwrapperConfigurationLocationsCapacity",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiCloudwrapperConfigurationLocationsCapacity:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudwrapperConfigurationLocationsCapacity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudwrapperConfigurationLocationsCapacityOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudwrapperConfiguration.DataAkamaiCloudwrapperConfigurationLocationsCapacityOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__80c47b597a2608b643dec06478331311d3ed060b070ce9ef5dfd48063b6d60b2)
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
    ) -> typing.Optional[DataAkamaiCloudwrapperConfigurationLocationsCapacity]:
        return typing.cast(typing.Optional[DataAkamaiCloudwrapperConfigurationLocationsCapacity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAkamaiCloudwrapperConfigurationLocationsCapacity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cbe4244081e0f226d504f0d216736be2c2cfafeffed21c56639c8dbf5f65787)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudwrapperConfigurationLocationsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudwrapperConfiguration.DataAkamaiCloudwrapperConfigurationLocationsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c2893412ba3085305cd53db1106649bb6d3c0b27eb3a332effdab721d64bae01)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiCloudwrapperConfigurationLocationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e99336942c28b3706a56953984c4adb83e2833da761f1e4d33bc4d64be02336)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiCloudwrapperConfigurationLocationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89eec2309f2f387867a8f3e41ccd4a563c57269e77b9263b694d11f483bdacc3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ef572f2f76cf9c362f031eebe46127c283d9113655c59395868f0afdf49d9da3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a02743c98117c97882bbee9899c4ea8349aa4437c17cda70b2e6dc8077ed8469)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationLocations]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationLocations]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationLocations]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2d220196a621e1fb43d4b01132b46131e587ebcd004c8d20b88b30f7f6a5d56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudwrapperConfigurationLocationsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudwrapperConfiguration.DataAkamaiCloudwrapperConfigurationLocationsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__af6488537e7a259aaaa6ee1f4f0bb8c4b1eea38768b230093e8c9f771754e7ca)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="capacity")
    def capacity(
        self,
    ) -> DataAkamaiCloudwrapperConfigurationLocationsCapacityOutputReference:
        return typing.cast(DataAkamaiCloudwrapperConfigurationLocationsCapacityOutputReference, jsii.get(self, "capacity"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationLocations]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationLocations]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationLocations]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d91a49146525afba24ea97b705c88327a2bdc99a469cc4a664711abe82cac70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudwrapperConfiguration.DataAkamaiCloudwrapperConfigurationMultiCdnSettings",
    jsii_struct_bases=[],
    name_mapping={"cdns": "cdns", "origins": "origins"},
)
class DataAkamaiCloudwrapperConfigurationMultiCdnSettings:
    def __init__(
        self,
        *,
        cdns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdns", typing.Dict[builtins.str, typing.Any]]]]] = None,
        origins: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudwrapperConfigurationMultiCdnSettingsOrigins", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param cdns: cdns block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_configuration#cdns DataAkamaiCloudwrapperConfiguration#cdns}
        :param origins: origins block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_configuration#origins DataAkamaiCloudwrapperConfiguration#origins}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d43f6700f95078170c6ba3e3a33fca5e09bb83c1a83037ef23a1dce8334c8eb1)
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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdns"]]]:
        '''cdns block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_configuration#cdns DataAkamaiCloudwrapperConfiguration#cdns}
        '''
        result = self._values.get("cdns")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdns"]]], result)

    @builtins.property
    def origins(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudwrapperConfigurationMultiCdnSettingsOrigins"]]]:
        '''origins block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_configuration#origins DataAkamaiCloudwrapperConfiguration#origins}
        '''
        result = self._values.get("origins")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudwrapperConfigurationMultiCdnSettingsOrigins"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudwrapperConfigurationMultiCdnSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudwrapperConfiguration.DataAkamaiCloudwrapperConfigurationMultiCdnSettingsBocc",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiCloudwrapperConfigurationMultiCdnSettingsBocc:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudwrapperConfigurationMultiCdnSettingsBocc(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudwrapperConfigurationMultiCdnSettingsBoccOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudwrapperConfiguration.DataAkamaiCloudwrapperConfigurationMultiCdnSettingsBoccOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__171eb354e30cf4a94bf308637f14bba1de914c528486e63fedbc101f0ac36c2f)
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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationMultiCdnSettingsBocc]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationMultiCdnSettingsBocc]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationMultiCdnSettingsBocc]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af94f57f33d80604cea257f521cc10a9b3a22df50efe6c0eb95ec967de2f6266)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudwrapperConfiguration.DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdns",
    jsii_struct_bases=[],
    name_mapping={"cdn_auth_keys": "cdnAuthKeys"},
)
class DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdns:
    def __init__(
        self,
        *,
        cdn_auth_keys: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsCdnAuthKeys", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param cdn_auth_keys: cdn_auth_keys block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_configuration#cdn_auth_keys DataAkamaiCloudwrapperConfiguration#cdn_auth_keys}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f30b2a554f806cf9b49f5f9cd4c382192fd1b53f5626242aef2be491b43bfc3a)
            check_type(argname="argument cdn_auth_keys", value=cdn_auth_keys, expected_type=type_hints["cdn_auth_keys"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cdn_auth_keys is not None:
            self._values["cdn_auth_keys"] = cdn_auth_keys

    @builtins.property
    def cdn_auth_keys(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsCdnAuthKeys"]]]:
        '''cdn_auth_keys block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudwrapper_configuration#cdn_auth_keys DataAkamaiCloudwrapperConfiguration#cdn_auth_keys}
        '''
        result = self._values.get("cdn_auth_keys")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsCdnAuthKeys"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudwrapperConfiguration.DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsCdnAuthKeys",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsCdnAuthKeys:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsCdnAuthKeys(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsCdnAuthKeysList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudwrapperConfiguration.DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsCdnAuthKeysList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f47e20f74dd303d9a62ca9769994af96e970ccead10995e00ace76da40edf803)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsCdnAuthKeysOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b2923a77461b93ed2fd242af874aff6722d46275ba8b705ba1e308fe2d4434c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsCdnAuthKeysOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e12ce768dd41c354c5e34bde21cc5ccbe9a5e8a873ca20d5add0e09e53afc51f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c50c995aeb576f558f999d122f812eafea96f36fa0433e69aa77175a1becec68)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d61807b0c82b8595730d6e01e52d6aa3d718db7b0edd38917f794179117c7eb7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsCdnAuthKeys]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsCdnAuthKeys]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsCdnAuthKeys]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86b51a6969c3152375a6887bd24f8cac3e784c0024ca163c1c7e628f7851256b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsCdnAuthKeysOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudwrapperConfiguration.DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsCdnAuthKeysOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d802aa4d154588b0b87315f15a9a0e58da20e3d03eb09020b55cb49e2edbc8ec)
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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsCdnAuthKeys]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsCdnAuthKeys]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsCdnAuthKeys]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85b10c106fd6ab0e6ab4fed3b5b4799d3ae77aff2f266cdf634ecc7a10dd38aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudwrapperConfiguration.DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__eb1710afc1583aec041d6754a16fad7b23762b6936a1156dc1628d4a1141abdb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__999be8931f63b0d174a2df9884494fa6599918d365de7e646085267003240795)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b8ccdf79f8728967e03f86f4be65f093535e71eebfb57a30dc152d6d8fa49a3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7fbddcf8a57cde288abc2914132191f90ba555a1083f1276798a0db1e23364a0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__28791dbf3d0555b5ec8471df974760e1076d3d54531ff1b16c2c8e1d15250dd0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdns]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdns]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f698dcafdb4307862ce63794e16b7d5eccde30232e7a0063f685af249e45834)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudwrapperConfiguration.DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9100929047a4b8c8e036fe3f88e52bcb06f7760c1a858eff378c0e4a940866ee)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCdnAuthKeys")
    def put_cdn_auth_keys(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsCdnAuthKeys, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3339b66db3ca8d8be9a3efebd080c31a208af2d1de945e5e9a00405ab5c6a512)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCdnAuthKeys", [value]))

    @jsii.member(jsii_name="resetCdnAuthKeys")
    def reset_cdn_auth_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCdnAuthKeys", []))

    @builtins.property
    @jsii.member(jsii_name="cdnAuthKeys")
    def cdn_auth_keys(
        self,
    ) -> DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsCdnAuthKeysList:
        return typing.cast(DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsCdnAuthKeysList, jsii.get(self, "cdnAuthKeys"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsCdnAuthKeys]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsCdnAuthKeys]]], jsii.get(self, "cdnAuthKeysInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdns]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdns]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdns]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__901a83302162bfbfd8586a9b86b232d67ec07cf832b30ac854fbfdf265786854)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudwrapperConfiguration.DataAkamaiCloudwrapperConfigurationMultiCdnSettingsDataStreams",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiCloudwrapperConfigurationMultiCdnSettingsDataStreams:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudwrapperConfigurationMultiCdnSettingsDataStreams(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudwrapperConfigurationMultiCdnSettingsDataStreamsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudwrapperConfiguration.DataAkamaiCloudwrapperConfigurationMultiCdnSettingsDataStreamsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3698705c5b7a2e7ec14263810dd54d8f0ce54d45feade1700d5526b86308db58)
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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationMultiCdnSettingsDataStreams]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationMultiCdnSettingsDataStreams]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationMultiCdnSettingsDataStreams]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__523ba8ab4df5af3d25ea06d58f27bbb6a67c139485dbe181888eee9504e447a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudwrapperConfiguration.DataAkamaiCloudwrapperConfigurationMultiCdnSettingsOrigins",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiCloudwrapperConfigurationMultiCdnSettingsOrigins:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudwrapperConfigurationMultiCdnSettingsOrigins(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudwrapperConfigurationMultiCdnSettingsOriginsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudwrapperConfiguration.DataAkamaiCloudwrapperConfigurationMultiCdnSettingsOriginsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__23835bcabcb9fd6b55af9c3c2d4e08e9daad873f2d7d80f95eda7dcffa84bf03)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiCloudwrapperConfigurationMultiCdnSettingsOriginsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5cd77d9a665124283ab214f31727ce46b1eabdce891df9b02402ad8cb4061da)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiCloudwrapperConfigurationMultiCdnSettingsOriginsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3843b95c682b0954f3847b33215e8c932332a20e59c0aef26bd5674cc75b1bd7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cc86512d71f175775933135c49f0a92da1c52c4eb6bbe76c4a575f065126e52d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7acdf56752ac0d8dd330048bfea02aea2df8f925053918343ea9607bf4ae2d26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationMultiCdnSettingsOrigins]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationMultiCdnSettingsOrigins]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationMultiCdnSettingsOrigins]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff48c48bce7ec6f045de272b083090579b8e3377cb38dad2fd3289325ac7297b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudwrapperConfigurationMultiCdnSettingsOriginsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudwrapperConfiguration.DataAkamaiCloudwrapperConfigurationMultiCdnSettingsOriginsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__04f7ec8f2f34da95a717fb44ac0b180d06f2ea3d82dc45dbaaccebfc2249f433)
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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationMultiCdnSettingsOrigins]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationMultiCdnSettingsOrigins]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationMultiCdnSettingsOrigins]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02ae87cca61e1f0b89630b4f1d4f6b16a42b0425ee9bfa5898d164dc481a5d52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudwrapperConfigurationMultiCdnSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudwrapperConfiguration.DataAkamaiCloudwrapperConfigurationMultiCdnSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8323c091eb7b25e72f1ea0b6b69f348f1dd2d574e68937a828efa383e9b82588)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCdns")
    def put_cdns(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdns, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ba2be19094cedbb49bfaf534cf4f9e8b01a00277f8e6a408717390220ec0631)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCdns", [value]))

    @jsii.member(jsii_name="putOrigins")
    def put_origins(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudwrapperConfigurationMultiCdnSettingsOrigins, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6d28324256cfcddf6b5de00536a116e2e51a2b72f184e025afb2192e8ad1e4d)
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
    ) -> DataAkamaiCloudwrapperConfigurationMultiCdnSettingsBoccOutputReference:
        return typing.cast(DataAkamaiCloudwrapperConfigurationMultiCdnSettingsBoccOutputReference, jsii.get(self, "bocc"))

    @builtins.property
    @jsii.member(jsii_name="cdns")
    def cdns(self) -> DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsList:
        return typing.cast(DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsList, jsii.get(self, "cdns"))

    @builtins.property
    @jsii.member(jsii_name="dataStreams")
    def data_streams(
        self,
    ) -> DataAkamaiCloudwrapperConfigurationMultiCdnSettingsDataStreamsOutputReference:
        return typing.cast(DataAkamaiCloudwrapperConfigurationMultiCdnSettingsDataStreamsOutputReference, jsii.get(self, "dataStreams"))

    @builtins.property
    @jsii.member(jsii_name="enableSoftAlerts")
    def enable_soft_alerts(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "enableSoftAlerts"))

    @builtins.property
    @jsii.member(jsii_name="origins")
    def origins(self) -> DataAkamaiCloudwrapperConfigurationMultiCdnSettingsOriginsList:
        return typing.cast(DataAkamaiCloudwrapperConfigurationMultiCdnSettingsOriginsList, jsii.get(self, "origins"))

    @builtins.property
    @jsii.member(jsii_name="cdnsInput")
    def cdns_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdns]]], jsii.get(self, "cdnsInput"))

    @builtins.property
    @jsii.member(jsii_name="originsInput")
    def origins_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationMultiCdnSettingsOrigins]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationMultiCdnSettingsOrigins]]], jsii.get(self, "originsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationMultiCdnSettings]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationMultiCdnSettings]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationMultiCdnSettings]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2a7374bcce343ca651527249930624454b8cc1d4f3414c8a823a3c87c947ecd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataAkamaiCloudwrapperConfiguration",
    "DataAkamaiCloudwrapperConfigurationConfig",
    "DataAkamaiCloudwrapperConfigurationLocations",
    "DataAkamaiCloudwrapperConfigurationLocationsCapacity",
    "DataAkamaiCloudwrapperConfigurationLocationsCapacityOutputReference",
    "DataAkamaiCloudwrapperConfigurationLocationsList",
    "DataAkamaiCloudwrapperConfigurationLocationsOutputReference",
    "DataAkamaiCloudwrapperConfigurationMultiCdnSettings",
    "DataAkamaiCloudwrapperConfigurationMultiCdnSettingsBocc",
    "DataAkamaiCloudwrapperConfigurationMultiCdnSettingsBoccOutputReference",
    "DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdns",
    "DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsCdnAuthKeys",
    "DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsCdnAuthKeysList",
    "DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsCdnAuthKeysOutputReference",
    "DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsList",
    "DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsOutputReference",
    "DataAkamaiCloudwrapperConfigurationMultiCdnSettingsDataStreams",
    "DataAkamaiCloudwrapperConfigurationMultiCdnSettingsDataStreamsOutputReference",
    "DataAkamaiCloudwrapperConfigurationMultiCdnSettingsOrigins",
    "DataAkamaiCloudwrapperConfigurationMultiCdnSettingsOriginsList",
    "DataAkamaiCloudwrapperConfigurationMultiCdnSettingsOriginsOutputReference",
    "DataAkamaiCloudwrapperConfigurationMultiCdnSettingsOutputReference",
]

publication.publish()

def _typecheckingstub__908f013e7a40173c924269f02e2a7c102a35a1b27278741167474682da7928ab(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    id: jsii.Number,
    locations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudwrapperConfigurationLocations, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__53821edf12773d891f745feae10b7f5ffd580fd40ee0237de20b53df894adc7e(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b38fc0208a27f9149d3c2f0b4a1e857a640362d3282370489add51af3155a64(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudwrapperConfigurationLocations, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cefc335190542ee252449063c5fa6b59e6dac10d8f291602e9866a3fb861273(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55ce752f4c7265d2b1239dbebcc9564e06033592a3fb09583bc3d0e7b1c4e43e(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: jsii.Number,
    locations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudwrapperConfigurationLocations, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80c47b597a2608b643dec06478331311d3ed060b070ce9ef5dfd48063b6d60b2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cbe4244081e0f226d504f0d216736be2c2cfafeffed21c56639c8dbf5f65787(
    value: typing.Optional[DataAkamaiCloudwrapperConfigurationLocationsCapacity],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2893412ba3085305cd53db1106649bb6d3c0b27eb3a332effdab721d64bae01(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e99336942c28b3706a56953984c4adb83e2833da761f1e4d33bc4d64be02336(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89eec2309f2f387867a8f3e41ccd4a563c57269e77b9263b694d11f483bdacc3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef572f2f76cf9c362f031eebe46127c283d9113655c59395868f0afdf49d9da3(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a02743c98117c97882bbee9899c4ea8349aa4437c17cda70b2e6dc8077ed8469(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2d220196a621e1fb43d4b01132b46131e587ebcd004c8d20b88b30f7f6a5d56(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationLocations]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af6488537e7a259aaaa6ee1f4f0bb8c4b1eea38768b230093e8c9f771754e7ca(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d91a49146525afba24ea97b705c88327a2bdc99a469cc4a664711abe82cac70(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationLocations]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d43f6700f95078170c6ba3e3a33fca5e09bb83c1a83037ef23a1dce8334c8eb1(
    *,
    cdns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdns, typing.Dict[builtins.str, typing.Any]]]]] = None,
    origins: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudwrapperConfigurationMultiCdnSettingsOrigins, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__171eb354e30cf4a94bf308637f14bba1de914c528486e63fedbc101f0ac36c2f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af94f57f33d80604cea257f521cc10a9b3a22df50efe6c0eb95ec967de2f6266(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationMultiCdnSettingsBocc]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f30b2a554f806cf9b49f5f9cd4c382192fd1b53f5626242aef2be491b43bfc3a(
    *,
    cdn_auth_keys: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsCdnAuthKeys, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f47e20f74dd303d9a62ca9769994af96e970ccead10995e00ace76da40edf803(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b2923a77461b93ed2fd242af874aff6722d46275ba8b705ba1e308fe2d4434c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e12ce768dd41c354c5e34bde21cc5ccbe9a5e8a873ca20d5add0e09e53afc51f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c50c995aeb576f558f999d122f812eafea96f36fa0433e69aa77175a1becec68(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d61807b0c82b8595730d6e01e52d6aa3d718db7b0edd38917f794179117c7eb7(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86b51a6969c3152375a6887bd24f8cac3e784c0024ca163c1c7e628f7851256b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsCdnAuthKeys]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d802aa4d154588b0b87315f15a9a0e58da20e3d03eb09020b55cb49e2edbc8ec(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85b10c106fd6ab0e6ab4fed3b5b4799d3ae77aff2f266cdf634ecc7a10dd38aa(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsCdnAuthKeys]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb1710afc1583aec041d6754a16fad7b23762b6936a1156dc1628d4a1141abdb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__999be8931f63b0d174a2df9884494fa6599918d365de7e646085267003240795(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b8ccdf79f8728967e03f86f4be65f093535e71eebfb57a30dc152d6d8fa49a3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fbddcf8a57cde288abc2914132191f90ba555a1083f1276798a0db1e23364a0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28791dbf3d0555b5ec8471df974760e1076d3d54531ff1b16c2c8e1d15250dd0(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f698dcafdb4307862ce63794e16b7d5eccde30232e7a0063f685af249e45834(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdns]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9100929047a4b8c8e036fe3f88e52bcb06f7760c1a858eff378c0e4a940866ee(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3339b66db3ca8d8be9a3efebd080c31a208af2d1de945e5e9a00405ab5c6a512(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdnsCdnAuthKeys, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__901a83302162bfbfd8586a9b86b232d67ec07cf832b30ac854fbfdf265786854(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdns]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3698705c5b7a2e7ec14263810dd54d8f0ce54d45feade1700d5526b86308db58(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__523ba8ab4df5af3d25ea06d58f27bbb6a67c139485dbe181888eee9504e447a2(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationMultiCdnSettingsDataStreams]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23835bcabcb9fd6b55af9c3c2d4e08e9daad873f2d7d80f95eda7dcffa84bf03(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5cd77d9a665124283ab214f31727ce46b1eabdce891df9b02402ad8cb4061da(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3843b95c682b0954f3847b33215e8c932332a20e59c0aef26bd5674cc75b1bd7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc86512d71f175775933135c49f0a92da1c52c4eb6bbe76c4a575f065126e52d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7acdf56752ac0d8dd330048bfea02aea2df8f925053918343ea9607bf4ae2d26(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff48c48bce7ec6f045de272b083090579b8e3377cb38dad2fd3289325ac7297b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudwrapperConfigurationMultiCdnSettingsOrigins]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04f7ec8f2f34da95a717fb44ac0b180d06f2ea3d82dc45dbaaccebfc2249f433(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02ae87cca61e1f0b89630b4f1d4f6b16a42b0425ee9bfa5898d164dc481a5d52(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationMultiCdnSettingsOrigins]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8323c091eb7b25e72f1ea0b6b69f348f1dd2d574e68937a828efa383e9b82588(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ba2be19094cedbb49bfaf534cf4f9e8b01a00277f8e6a408717390220ec0631(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudwrapperConfigurationMultiCdnSettingsCdns, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6d28324256cfcddf6b5de00536a116e2e51a2b72f184e025afb2192e8ad1e4d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudwrapperConfigurationMultiCdnSettingsOrigins, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2a7374bcce343ca651527249930624454b8cc1d4f3414c8a823a3c87c947ecd(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudwrapperConfigurationMultiCdnSettings]],
) -> None:
    """Type checking stubs"""
    pass
