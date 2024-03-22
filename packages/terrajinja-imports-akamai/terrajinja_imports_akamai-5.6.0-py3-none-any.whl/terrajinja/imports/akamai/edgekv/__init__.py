'''
# `akamai_edgekv`

Refer to the Terraform Registry for docs: [`akamai_edgekv`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv).
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


class Edgekv(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.edgekv.Edgekv",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv akamai_edgekv}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        group_id: jsii.Number,
        namespace_name: builtins.str,
        network: builtins.str,
        retention_in_seconds: jsii.Number,
        geo_location: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        initial_data: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EdgekvInitialData", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv akamai_edgekv} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param group_id: Namespace ACC group ID. It will be used in EdgeKV API v2. Not updatable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv#group_id Edgekv#group_id}
        :param namespace_name: Name for the EKV namespace. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv#namespace_name Edgekv#namespace_name}
        :param network: The network on which the namespace will be activated. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv#network Edgekv#network}
        :param retention_in_seconds: Retention period for data in this namespace. An update of this value will just affect new EKV items. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv#retention_in_seconds Edgekv#retention_in_seconds}
        :param geo_location: Storage location for data. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv#geo_location Edgekv#geo_location}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv#id Edgekv#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param initial_data: initial_data block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv#initial_data Edgekv#initial_data}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21f87f613d5d080263fbfcd1be172e51277f009d097e252c00594face85b060e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = EdgekvConfig(
            group_id=group_id,
            namespace_name=namespace_name,
            network=network,
            retention_in_seconds=retention_in_seconds,
            geo_location=geo_location,
            id=id,
            initial_data=initial_data,
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
        '''Generates CDKTF code for importing a Edgekv resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the Edgekv to import.
        :param import_from_id: The id of the existing Edgekv that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the Edgekv to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3378cd6a1504fe2bf7a4dc48bf809648203faf2bc0f289ee0adb17966a061931)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putInitialData")
    def put_initial_data(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EdgekvInitialData", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84498f6c17a94a8d19fccd9ff24c0eb1dfd790d8811c4a9f254693d1cbbd757d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInitialData", [value]))

    @jsii.member(jsii_name="resetGeoLocation")
    def reset_geo_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGeoLocation", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInitialData")
    def reset_initial_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitialData", []))

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
    @jsii.member(jsii_name="initialData")
    def initial_data(self) -> "EdgekvInitialDataList":
        return typing.cast("EdgekvInitialDataList", jsii.get(self, "initialData"))

    @builtins.property
    @jsii.member(jsii_name="geoLocationInput")
    def geo_location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "geoLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="groupIdInput")
    def group_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "groupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="initialDataInput")
    def initial_data_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EdgekvInitialData"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EdgekvInitialData"]]], jsii.get(self, "initialDataInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceNameInput")
    def namespace_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInput")
    def network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionInSecondsInput")
    def retention_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="geoLocation")
    def geo_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "geoLocation"))

    @geo_location.setter
    def geo_location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c97e74803f601c43eae305221f80e9fc36e48bcd3e61511e8fe04500c89f35ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "geoLocation", value)

    @builtins.property
    @jsii.member(jsii_name="groupId")
    def group_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "groupId"))

    @group_id.setter
    def group_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2cc3cfe4eb37602d72975d29f11fd915c9dbbca61174efe3987923835e5511c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34395e2516f1017640a3ee7e610863a798760ac8fb36256fc215fab7ca2d220a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="namespaceName")
    def namespace_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespaceName"))

    @namespace_name.setter
    def namespace_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c747bfada262429faa9117559eb338f09427acdb7c44e2375972059ecae06334)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespaceName", value)

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "network"))

    @network.setter
    def network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5d391c13a7d4e90929d16611b4eedb90231177acc4d096a7ace15bc7c3df9a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "network", value)

    @builtins.property
    @jsii.member(jsii_name="retentionInSeconds")
    def retention_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionInSeconds"))

    @retention_in_seconds.setter
    def retention_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__622e1bc588db96b79f28e702ee152b9064df9a0d9e1d4824a533ad912cfc2ae8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionInSeconds", value)


@jsii.data_type(
    jsii_type="akamai.edgekv.EdgekvConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "group_id": "groupId",
        "namespace_name": "namespaceName",
        "network": "network",
        "retention_in_seconds": "retentionInSeconds",
        "geo_location": "geoLocation",
        "id": "id",
        "initial_data": "initialData",
    },
)
class EdgekvConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        group_id: jsii.Number,
        namespace_name: builtins.str,
        network: builtins.str,
        retention_in_seconds: jsii.Number,
        geo_location: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        initial_data: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EdgekvInitialData", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param group_id: Namespace ACC group ID. It will be used in EdgeKV API v2. Not updatable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv#group_id Edgekv#group_id}
        :param namespace_name: Name for the EKV namespace. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv#namespace_name Edgekv#namespace_name}
        :param network: The network on which the namespace will be activated. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv#network Edgekv#network}
        :param retention_in_seconds: Retention period for data in this namespace. An update of this value will just affect new EKV items. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv#retention_in_seconds Edgekv#retention_in_seconds}
        :param geo_location: Storage location for data. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv#geo_location Edgekv#geo_location}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv#id Edgekv#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param initial_data: initial_data block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv#initial_data Edgekv#initial_data}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93cc7387a7f72d6f54d01bb85795f29b022611f0d91a66caa278adc4806f4ac6)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
            check_type(argname="argument namespace_name", value=namespace_name, expected_type=type_hints["namespace_name"])
            check_type(argname="argument network", value=network, expected_type=type_hints["network"])
            check_type(argname="argument retention_in_seconds", value=retention_in_seconds, expected_type=type_hints["retention_in_seconds"])
            check_type(argname="argument geo_location", value=geo_location, expected_type=type_hints["geo_location"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument initial_data", value=initial_data, expected_type=type_hints["initial_data"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "group_id": group_id,
            "namespace_name": namespace_name,
            "network": network,
            "retention_in_seconds": retention_in_seconds,
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
        if geo_location is not None:
            self._values["geo_location"] = geo_location
        if id is not None:
            self._values["id"] = id
        if initial_data is not None:
            self._values["initial_data"] = initial_data

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
    def group_id(self) -> jsii.Number:
        '''Namespace ACC group ID. It will be used in EdgeKV API v2. Not updatable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv#group_id Edgekv#group_id}
        '''
        result = self._values.get("group_id")
        assert result is not None, "Required property 'group_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def namespace_name(self) -> builtins.str:
        '''Name for the EKV namespace.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv#namespace_name Edgekv#namespace_name}
        '''
        result = self._values.get("namespace_name")
        assert result is not None, "Required property 'namespace_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network(self) -> builtins.str:
        '''The network on which the namespace will be activated.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv#network Edgekv#network}
        '''
        result = self._values.get("network")
        assert result is not None, "Required property 'network' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def retention_in_seconds(self) -> jsii.Number:
        '''Retention period for data in this namespace. An update of this value will just affect new EKV items.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv#retention_in_seconds Edgekv#retention_in_seconds}
        '''
        result = self._values.get("retention_in_seconds")
        assert result is not None, "Required property 'retention_in_seconds' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def geo_location(self) -> typing.Optional[builtins.str]:
        '''Storage location for data.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv#geo_location Edgekv#geo_location}
        '''
        result = self._values.get("geo_location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv#id Edgekv#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initial_data(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EdgekvInitialData"]]]:
        '''initial_data block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv#initial_data Edgekv#initial_data}
        '''
        result = self._values.get("initial_data")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EdgekvInitialData"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EdgekvConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.edgekv.EdgekvInitialData",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value", "group": "group"},
)
class EdgekvInitialData:
    def __init__(
        self,
        *,
        key: builtins.str,
        value: builtins.str,
        group: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv#key Edgekv#key}.
        :param value: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv#value Edgekv#value}.
        :param group: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv#group Edgekv#group}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33d73040e9ac9f72ccbfa03305315d38e11d3745fc93c3ca10b8d9ca88fa94e4)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "value": value,
        }
        if group is not None:
            self._values["group"] = group

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv#key Edgekv#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv#value Edgekv#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv#group Edgekv#group}.'''
        result = self._values.get("group")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EdgekvInitialData(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EdgekvInitialDataList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.edgekv.EdgekvInitialDataList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fc93b0d4b50b4d3c0d114daf6d46ca8f826f8aea5947547e874452497612a638)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "EdgekvInitialDataOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__247df0d33e2e43288c07dfa0653d839178cee41984f2be61a7f91683cdf5a6ed)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EdgekvInitialDataOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f3ce4fac416b36e973ccd330bc677ac1d9c8378bf050475bcf26bc202c03eb3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1af725aa71a36437357079fa1b6b9f458212fc5719bd825c8908e1151e4c0212)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e3c0dbd79dbb8abafd79adc1060c3c1d70cb883bf990f497c7396a1148e82f40)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EdgekvInitialData]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EdgekvInitialData]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EdgekvInitialData]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79515e4d1ff498369a40084f5c2fc3fad8e3ba8a72af486d085b9e0bc812127a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EdgekvInitialDataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.edgekv.EdgekvInitialDataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__84677fef9867a640ed061a83d54ddcf00b68b43e3d638b219d2e5e687a6a83b4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetGroup")
    def reset_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroup", []))

    @builtins.property
    @jsii.member(jsii_name="groupInput")
    def group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="group")
    def group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "group"))

    @group.setter
    def group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7162cd8706c396be190348347d6a40e671a864460917cef85be0371c0f64b66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "group", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7683738a3cdd1a06c1cb4df76440433653312590269ce3f846ec35f34eefa5bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd2fab3787eaa21191ee804ff1c2a6480c16ba29f797f74f3fb57060e912e71e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EdgekvInitialData]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EdgekvInitialData]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EdgekvInitialData]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11afd66b0ff12e4e6689b93239b84556ac62b4487a1f0aaabe8d8b861028ea4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Edgekv",
    "EdgekvConfig",
    "EdgekvInitialData",
    "EdgekvInitialDataList",
    "EdgekvInitialDataOutputReference",
]

publication.publish()

def _typecheckingstub__21f87f613d5d080263fbfcd1be172e51277f009d097e252c00594face85b060e(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    group_id: jsii.Number,
    namespace_name: builtins.str,
    network: builtins.str,
    retention_in_seconds: jsii.Number,
    geo_location: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    initial_data: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EdgekvInitialData, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__3378cd6a1504fe2bf7a4dc48bf809648203faf2bc0f289ee0adb17966a061931(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84498f6c17a94a8d19fccd9ff24c0eb1dfd790d8811c4a9f254693d1cbbd757d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EdgekvInitialData, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c97e74803f601c43eae305221f80e9fc36e48bcd3e61511e8fe04500c89f35ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2cc3cfe4eb37602d72975d29f11fd915c9dbbca61174efe3987923835e5511c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34395e2516f1017640a3ee7e610863a798760ac8fb36256fc215fab7ca2d220a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c747bfada262429faa9117559eb338f09427acdb7c44e2375972059ecae06334(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5d391c13a7d4e90929d16611b4eedb90231177acc4d096a7ace15bc7c3df9a4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__622e1bc588db96b79f28e702ee152b9064df9a0d9e1d4824a533ad912cfc2ae8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93cc7387a7f72d6f54d01bb85795f29b022611f0d91a66caa278adc4806f4ac6(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    group_id: jsii.Number,
    namespace_name: builtins.str,
    network: builtins.str,
    retention_in_seconds: jsii.Number,
    geo_location: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    initial_data: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EdgekvInitialData, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33d73040e9ac9f72ccbfa03305315d38e11d3745fc93c3ca10b8d9ca88fa94e4(
    *,
    key: builtins.str,
    value: builtins.str,
    group: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc93b0d4b50b4d3c0d114daf6d46ca8f826f8aea5947547e874452497612a638(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__247df0d33e2e43288c07dfa0653d839178cee41984f2be61a7f91683cdf5a6ed(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f3ce4fac416b36e973ccd330bc677ac1d9c8378bf050475bcf26bc202c03eb3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1af725aa71a36437357079fa1b6b9f458212fc5719bd825c8908e1151e4c0212(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3c0dbd79dbb8abafd79adc1060c3c1d70cb883bf990f497c7396a1148e82f40(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79515e4d1ff498369a40084f5c2fc3fad8e3ba8a72af486d085b9e0bc812127a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EdgekvInitialData]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84677fef9867a640ed061a83d54ddcf00b68b43e3d638b219d2e5e687a6a83b4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7162cd8706c396be190348347d6a40e671a864460917cef85be0371c0f64b66(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7683738a3cdd1a06c1cb4df76440433653312590269ce3f846ec35f34eefa5bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd2fab3787eaa21191ee804ff1c2a6480c16ba29f797f74f3fb57060e912e71e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11afd66b0ff12e4e6689b93239b84556ac62b4487a1f0aaabe8d8b861028ea4a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EdgekvInitialData]],
) -> None:
    """Type checking stubs"""
    pass
