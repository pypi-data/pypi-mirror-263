'''
# `akamai_appsec_ip_geo`

Refer to the Terraform Registry for docs: [`akamai_appsec_ip_geo`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_ip_geo).
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


class AppsecIpGeo(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.appsecIpGeo.AppsecIpGeo",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_ip_geo akamai_appsec_ip_geo}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        config_id: jsii.Number,
        mode: builtins.str,
        security_policy_id: builtins.str,
        asn_network_lists: typing.Optional[typing.Sequence[builtins.str]] = None,
        exception_ip_network_lists: typing.Optional[typing.Sequence[builtins.str]] = None,
        geo_network_lists: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        ip_network_lists: typing.Optional[typing.Sequence[builtins.str]] = None,
        ukraine_geo_control_action: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_ip_geo akamai_appsec_ip_geo} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param config_id: Unique identifier of the security configuration. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_ip_geo#config_id AppsecIpGeo#config_id}
        :param mode: Protection mode (block or allow). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_ip_geo#mode AppsecIpGeo#mode}
        :param security_policy_id: Unique identifier of the security policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_ip_geo#security_policy_id AppsecIpGeo#security_policy_id}
        :param asn_network_lists: List of IDs of ASN network list to be blocked. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_ip_geo#asn_network_lists AppsecIpGeo#asn_network_lists}
        :param exception_ip_network_lists: List of IDs of network list that are always allowed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_ip_geo#exception_ip_network_lists AppsecIpGeo#exception_ip_network_lists}
        :param geo_network_lists: List of IDs of geographic network list to be blocked. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_ip_geo#geo_network_lists AppsecIpGeo#geo_network_lists}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_ip_geo#id AppsecIpGeo#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_network_lists: List of IDs of IP network list to be blocked. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_ip_geo#ip_network_lists AppsecIpGeo#ip_network_lists}
        :param ukraine_geo_control_action: Action set for Ukraine geo control. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_ip_geo#ukraine_geo_control_action AppsecIpGeo#ukraine_geo_control_action}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3daa64d88cf460817498a0832d31c3735b59af0e6a942df11e0b8f95f3f8a428)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AppsecIpGeoConfig(
            config_id=config_id,
            mode=mode,
            security_policy_id=security_policy_id,
            asn_network_lists=asn_network_lists,
            exception_ip_network_lists=exception_ip_network_lists,
            geo_network_lists=geo_network_lists,
            id=id,
            ip_network_lists=ip_network_lists,
            ukraine_geo_control_action=ukraine_geo_control_action,
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
        '''Generates CDKTF code for importing a AppsecIpGeo resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the AppsecIpGeo to import.
        :param import_from_id: The id of the existing AppsecIpGeo that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_ip_geo#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the AppsecIpGeo to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5245cf05ab74a5bd06f43a11f83d6a8c750882964460e9606fbaa98b74c2d28f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetAsnNetworkLists")
    def reset_asn_network_lists(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAsnNetworkLists", []))

    @jsii.member(jsii_name="resetExceptionIpNetworkLists")
    def reset_exception_ip_network_lists(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExceptionIpNetworkLists", []))

    @jsii.member(jsii_name="resetGeoNetworkLists")
    def reset_geo_network_lists(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGeoNetworkLists", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIpNetworkLists")
    def reset_ip_network_lists(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpNetworkLists", []))

    @jsii.member(jsii_name="resetUkraineGeoControlAction")
    def reset_ukraine_geo_control_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUkraineGeoControlAction", []))

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
    @jsii.member(jsii_name="asnNetworkListsInput")
    def asn_network_lists_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "asnNetworkListsInput"))

    @builtins.property
    @jsii.member(jsii_name="configIdInput")
    def config_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "configIdInput"))

    @builtins.property
    @jsii.member(jsii_name="exceptionIpNetworkListsInput")
    def exception_ip_network_lists_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exceptionIpNetworkListsInput"))

    @builtins.property
    @jsii.member(jsii_name="geoNetworkListsInput")
    def geo_network_lists_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "geoNetworkListsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ipNetworkListsInput")
    def ip_network_lists_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipNetworkListsInput"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="securityPolicyIdInput")
    def security_policy_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityPolicyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="ukraineGeoControlActionInput")
    def ukraine_geo_control_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ukraineGeoControlActionInput"))

    @builtins.property
    @jsii.member(jsii_name="asnNetworkLists")
    def asn_network_lists(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "asnNetworkLists"))

    @asn_network_lists.setter
    def asn_network_lists(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__beb1dab3bc3fa9cb60f4d68b2f292d33fc9658ed3581cc351f282e894c45f5fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "asnNetworkLists", value)

    @builtins.property
    @jsii.member(jsii_name="configId")
    def config_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "configId"))

    @config_id.setter
    def config_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c762d729fd705d42ee8475700e8d37b5bcb854a997284ca86838b36428d8ddc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configId", value)

    @builtins.property
    @jsii.member(jsii_name="exceptionIpNetworkLists")
    def exception_ip_network_lists(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exceptionIpNetworkLists"))

    @exception_ip_network_lists.setter
    def exception_ip_network_lists(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac5b91b630423720b913396b6d79e54d9009f252aabe9f0701318c01e3d145e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exceptionIpNetworkLists", value)

    @builtins.property
    @jsii.member(jsii_name="geoNetworkLists")
    def geo_network_lists(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "geoNetworkLists"))

    @geo_network_lists.setter
    def geo_network_lists(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bf14be83517f43b58b12033bfcd5047a2c924f75f4a3686195a0d95e20a1f57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "geoNetworkLists", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a67fd2c6933cb6c04a4d000bbfdff88d48b0d5fc700199d5ff020d6982b7f8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ipNetworkLists")
    def ip_network_lists(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipNetworkLists"))

    @ip_network_lists.setter
    def ip_network_lists(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8855f959579dd0710b4645120377e815e509e05728b31b7a70ceb72669359ed5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipNetworkLists", value)

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e701390fdc39afb1a49ebbbd783272dded8117b30b96020c76ba8aabcd9bb4a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="securityPolicyId")
    def security_policy_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityPolicyId"))

    @security_policy_id.setter
    def security_policy_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebebc42408ac78a8a441ed3b4ad2c2909180f228900a448b7b20e9173a8a7cdf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityPolicyId", value)

    @builtins.property
    @jsii.member(jsii_name="ukraineGeoControlAction")
    def ukraine_geo_control_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ukraineGeoControlAction"))

    @ukraine_geo_control_action.setter
    def ukraine_geo_control_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d27997a2b3e25c9c4ef42a095020e40fc5c26310a80ee61b944d8c4cb18c5b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ukraineGeoControlAction", value)


@jsii.data_type(
    jsii_type="akamai.appsecIpGeo.AppsecIpGeoConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "config_id": "configId",
        "mode": "mode",
        "security_policy_id": "securityPolicyId",
        "asn_network_lists": "asnNetworkLists",
        "exception_ip_network_lists": "exceptionIpNetworkLists",
        "geo_network_lists": "geoNetworkLists",
        "id": "id",
        "ip_network_lists": "ipNetworkLists",
        "ukraine_geo_control_action": "ukraineGeoControlAction",
    },
)
class AppsecIpGeoConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        config_id: jsii.Number,
        mode: builtins.str,
        security_policy_id: builtins.str,
        asn_network_lists: typing.Optional[typing.Sequence[builtins.str]] = None,
        exception_ip_network_lists: typing.Optional[typing.Sequence[builtins.str]] = None,
        geo_network_lists: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        ip_network_lists: typing.Optional[typing.Sequence[builtins.str]] = None,
        ukraine_geo_control_action: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param config_id: Unique identifier of the security configuration. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_ip_geo#config_id AppsecIpGeo#config_id}
        :param mode: Protection mode (block or allow). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_ip_geo#mode AppsecIpGeo#mode}
        :param security_policy_id: Unique identifier of the security policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_ip_geo#security_policy_id AppsecIpGeo#security_policy_id}
        :param asn_network_lists: List of IDs of ASN network list to be blocked. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_ip_geo#asn_network_lists AppsecIpGeo#asn_network_lists}
        :param exception_ip_network_lists: List of IDs of network list that are always allowed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_ip_geo#exception_ip_network_lists AppsecIpGeo#exception_ip_network_lists}
        :param geo_network_lists: List of IDs of geographic network list to be blocked. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_ip_geo#geo_network_lists AppsecIpGeo#geo_network_lists}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_ip_geo#id AppsecIpGeo#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_network_lists: List of IDs of IP network list to be blocked. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_ip_geo#ip_network_lists AppsecIpGeo#ip_network_lists}
        :param ukraine_geo_control_action: Action set for Ukraine geo control. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_ip_geo#ukraine_geo_control_action AppsecIpGeo#ukraine_geo_control_action}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf6d8963945469ac84524ef69b8172da36ae0c6d20997b22b8737e72c12d64df)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument config_id", value=config_id, expected_type=type_hints["config_id"])
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument security_policy_id", value=security_policy_id, expected_type=type_hints["security_policy_id"])
            check_type(argname="argument asn_network_lists", value=asn_network_lists, expected_type=type_hints["asn_network_lists"])
            check_type(argname="argument exception_ip_network_lists", value=exception_ip_network_lists, expected_type=type_hints["exception_ip_network_lists"])
            check_type(argname="argument geo_network_lists", value=geo_network_lists, expected_type=type_hints["geo_network_lists"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ip_network_lists", value=ip_network_lists, expected_type=type_hints["ip_network_lists"])
            check_type(argname="argument ukraine_geo_control_action", value=ukraine_geo_control_action, expected_type=type_hints["ukraine_geo_control_action"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "config_id": config_id,
            "mode": mode,
            "security_policy_id": security_policy_id,
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
        if asn_network_lists is not None:
            self._values["asn_network_lists"] = asn_network_lists
        if exception_ip_network_lists is not None:
            self._values["exception_ip_network_lists"] = exception_ip_network_lists
        if geo_network_lists is not None:
            self._values["geo_network_lists"] = geo_network_lists
        if id is not None:
            self._values["id"] = id
        if ip_network_lists is not None:
            self._values["ip_network_lists"] = ip_network_lists
        if ukraine_geo_control_action is not None:
            self._values["ukraine_geo_control_action"] = ukraine_geo_control_action

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
    def config_id(self) -> jsii.Number:
        '''Unique identifier of the security configuration.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_ip_geo#config_id AppsecIpGeo#config_id}
        '''
        result = self._values.get("config_id")
        assert result is not None, "Required property 'config_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def mode(self) -> builtins.str:
        '''Protection mode (block or allow).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_ip_geo#mode AppsecIpGeo#mode}
        '''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_policy_id(self) -> builtins.str:
        '''Unique identifier of the security policy.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_ip_geo#security_policy_id AppsecIpGeo#security_policy_id}
        '''
        result = self._values.get("security_policy_id")
        assert result is not None, "Required property 'security_policy_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def asn_network_lists(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of IDs of ASN network list to be blocked.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_ip_geo#asn_network_lists AppsecIpGeo#asn_network_lists}
        '''
        result = self._values.get("asn_network_lists")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def exception_ip_network_lists(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of IDs of network list that are always allowed.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_ip_geo#exception_ip_network_lists AppsecIpGeo#exception_ip_network_lists}
        '''
        result = self._values.get("exception_ip_network_lists")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def geo_network_lists(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of IDs of geographic network list to be blocked.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_ip_geo#geo_network_lists AppsecIpGeo#geo_network_lists}
        '''
        result = self._values.get("geo_network_lists")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_ip_geo#id AppsecIpGeo#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_network_lists(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of IDs of IP network list to be blocked.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_ip_geo#ip_network_lists AppsecIpGeo#ip_network_lists}
        '''
        result = self._values.get("ip_network_lists")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ukraine_geo_control_action(self) -> typing.Optional[builtins.str]:
        '''Action set for Ukraine geo control.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_ip_geo#ukraine_geo_control_action AppsecIpGeo#ukraine_geo_control_action}
        '''
        result = self._values.get("ukraine_geo_control_action")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsecIpGeoConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AppsecIpGeo",
    "AppsecIpGeoConfig",
]

publication.publish()

def _typecheckingstub__3daa64d88cf460817498a0832d31c3735b59af0e6a942df11e0b8f95f3f8a428(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    config_id: jsii.Number,
    mode: builtins.str,
    security_policy_id: builtins.str,
    asn_network_lists: typing.Optional[typing.Sequence[builtins.str]] = None,
    exception_ip_network_lists: typing.Optional[typing.Sequence[builtins.str]] = None,
    geo_network_lists: typing.Optional[typing.Sequence[builtins.str]] = None,
    id: typing.Optional[builtins.str] = None,
    ip_network_lists: typing.Optional[typing.Sequence[builtins.str]] = None,
    ukraine_geo_control_action: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__5245cf05ab74a5bd06f43a11f83d6a8c750882964460e9606fbaa98b74c2d28f(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__beb1dab3bc3fa9cb60f4d68b2f292d33fc9658ed3581cc351f282e894c45f5fd(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c762d729fd705d42ee8475700e8d37b5bcb854a997284ca86838b36428d8ddc(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac5b91b630423720b913396b6d79e54d9009f252aabe9f0701318c01e3d145e2(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bf14be83517f43b58b12033bfcd5047a2c924f75f4a3686195a0d95e20a1f57(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a67fd2c6933cb6c04a4d000bbfdff88d48b0d5fc700199d5ff020d6982b7f8a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8855f959579dd0710b4645120377e815e509e05728b31b7a70ceb72669359ed5(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e701390fdc39afb1a49ebbbd783272dded8117b30b96020c76ba8aabcd9bb4a9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebebc42408ac78a8a441ed3b4ad2c2909180f228900a448b7b20e9173a8a7cdf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d27997a2b3e25c9c4ef42a095020e40fc5c26310a80ee61b944d8c4cb18c5b9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf6d8963945469ac84524ef69b8172da36ae0c6d20997b22b8737e72c12d64df(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    config_id: jsii.Number,
    mode: builtins.str,
    security_policy_id: builtins.str,
    asn_network_lists: typing.Optional[typing.Sequence[builtins.str]] = None,
    exception_ip_network_lists: typing.Optional[typing.Sequence[builtins.str]] = None,
    geo_network_lists: typing.Optional[typing.Sequence[builtins.str]] = None,
    id: typing.Optional[builtins.str] = None,
    ip_network_lists: typing.Optional[typing.Sequence[builtins.str]] = None,
    ukraine_geo_control_action: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
