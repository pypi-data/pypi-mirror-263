'''
# `data_akamai_appsec_api_endpoints`

Refer to the Terraform Registry for docs: [`data_akamai_appsec_api_endpoints`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/appsec_api_endpoints).
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


class DataAkamaiAppsecApiEndpoints(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiAppsecApiEndpoints.DataAkamaiAppsecApiEndpoints",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/appsec_api_endpoints akamai_appsec_api_endpoints}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        config_id: jsii.Number,
        api_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        security_policy_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/appsec_api_endpoints akamai_appsec_api_endpoints} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param config_id: Unique identifier of the security configuration. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/appsec_api_endpoints#config_id DataAkamaiAppsecApiEndpoints#config_id}
        :param api_name: Name of the API endpoint. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/appsec_api_endpoints#api_name DataAkamaiAppsecApiEndpoints#api_name}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/appsec_api_endpoints#id DataAkamaiAppsecApiEndpoints#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param security_policy_id: Unique identifier of the security policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/appsec_api_endpoints#security_policy_id DataAkamaiAppsecApiEndpoints#security_policy_id}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7bda0e5b973f681d208c4a07a4447311a78d53732256c5e9842a38f9d227c77)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAkamaiAppsecApiEndpointsConfig(
            config_id=config_id,
            api_name=api_name,
            id=id,
            security_policy_id=security_policy_id,
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
        '''Generates CDKTF code for importing a DataAkamaiAppsecApiEndpoints resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the DataAkamaiAppsecApiEndpoints to import.
        :param import_from_id: The id of the existing DataAkamaiAppsecApiEndpoints that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/appsec_api_endpoints#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the DataAkamaiAppsecApiEndpoints to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0de61fa34a2930bd53ab5e4b6c8fca9cb0f6aa9fdffbe4b7ffc0c3cfcac498e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetApiName")
    def reset_api_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSecurityPolicyId")
    def reset_security_policy_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityPolicyId", []))

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
    @jsii.member(jsii_name="idList")
    def id_list(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "idList"))

    @builtins.property
    @jsii.member(jsii_name="json")
    def json(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "json"))

    @builtins.property
    @jsii.member(jsii_name="outputText")
    def output_text(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outputText"))

    @builtins.property
    @jsii.member(jsii_name="apiNameInput")
    def api_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiNameInput"))

    @builtins.property
    @jsii.member(jsii_name="configIdInput")
    def config_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "configIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="securityPolicyIdInput")
    def security_policy_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityPolicyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="apiName")
    def api_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiName"))

    @api_name.setter
    def api_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb5c89d943e15b067913d59738f9353fddfd4ab1104acb76866ce41aee253584)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiName", value)

    @builtins.property
    @jsii.member(jsii_name="configId")
    def config_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "configId"))

    @config_id.setter
    def config_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__730360069e1f261c9961ded0e2c2751f4c04f81ad9364b622e313f12783d025f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b93b6dc200d481a521c8269fad180330b76e8b0c8983b15fcf69ef446d2b1c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="securityPolicyId")
    def security_policy_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityPolicyId"))

    @security_policy_id.setter
    def security_policy_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03475ff566afe0e9aaa7f830b53d1007533ed2d0bdc7c6b2345b1c40be65bcb1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityPolicyId", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiAppsecApiEndpoints.DataAkamaiAppsecApiEndpointsConfig",
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
        "api_name": "apiName",
        "id": "id",
        "security_policy_id": "securityPolicyId",
    },
)
class DataAkamaiAppsecApiEndpointsConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        api_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        security_policy_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param config_id: Unique identifier of the security configuration. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/appsec_api_endpoints#config_id DataAkamaiAppsecApiEndpoints#config_id}
        :param api_name: Name of the API endpoint. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/appsec_api_endpoints#api_name DataAkamaiAppsecApiEndpoints#api_name}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/appsec_api_endpoints#id DataAkamaiAppsecApiEndpoints#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param security_policy_id: Unique identifier of the security policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/appsec_api_endpoints#security_policy_id DataAkamaiAppsecApiEndpoints#security_policy_id}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a33577a7f70c934134fab68496081825c78da8157b257e747c0b256f11f3f6e8)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument config_id", value=config_id, expected_type=type_hints["config_id"])
            check_type(argname="argument api_name", value=api_name, expected_type=type_hints["api_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument security_policy_id", value=security_policy_id, expected_type=type_hints["security_policy_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "config_id": config_id,
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
        if api_name is not None:
            self._values["api_name"] = api_name
        if id is not None:
            self._values["id"] = id
        if security_policy_id is not None:
            self._values["security_policy_id"] = security_policy_id

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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/appsec_api_endpoints#config_id DataAkamaiAppsecApiEndpoints#config_id}
        '''
        result = self._values.get("config_id")
        assert result is not None, "Required property 'config_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def api_name(self) -> typing.Optional[builtins.str]:
        '''Name of the API endpoint.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/appsec_api_endpoints#api_name DataAkamaiAppsecApiEndpoints#api_name}
        '''
        result = self._values.get("api_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/appsec_api_endpoints#id DataAkamaiAppsecApiEndpoints#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_policy_id(self) -> typing.Optional[builtins.str]:
        '''Unique identifier of the security policy.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/appsec_api_endpoints#security_policy_id DataAkamaiAppsecApiEndpoints#security_policy_id}
        '''
        result = self._values.get("security_policy_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiAppsecApiEndpointsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DataAkamaiAppsecApiEndpoints",
    "DataAkamaiAppsecApiEndpointsConfig",
]

publication.publish()

def _typecheckingstub__f7bda0e5b973f681d208c4a07a4447311a78d53732256c5e9842a38f9d227c77(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    config_id: jsii.Number,
    api_name: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    security_policy_id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__e0de61fa34a2930bd53ab5e4b6c8fca9cb0f6aa9fdffbe4b7ffc0c3cfcac498e(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb5c89d943e15b067913d59738f9353fddfd4ab1104acb76866ce41aee253584(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__730360069e1f261c9961ded0e2c2751f4c04f81ad9364b622e313f12783d025f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b93b6dc200d481a521c8269fad180330b76e8b0c8983b15fcf69ef446d2b1c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03475ff566afe0e9aaa7f830b53d1007533ed2d0bdc7c6b2345b1c40be65bcb1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a33577a7f70c934134fab68496081825c78da8157b257e747c0b256f11f3f6e8(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    config_id: jsii.Number,
    api_name: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    security_policy_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
