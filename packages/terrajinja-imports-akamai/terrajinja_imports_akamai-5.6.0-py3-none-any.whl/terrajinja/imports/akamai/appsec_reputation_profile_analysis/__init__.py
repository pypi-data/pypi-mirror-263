'''
# `akamai_appsec_reputation_profile_analysis`

Refer to the Terraform Registry for docs: [`akamai_appsec_reputation_profile_analysis`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_reputation_profile_analysis).
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


class AppsecReputationProfileAnalysis(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.appsecReputationProfileAnalysis.AppsecReputationProfileAnalysis",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_reputation_profile_analysis akamai_appsec_reputation_profile_analysis}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        config_id: jsii.Number,
        forward_shared_ip_to_http_header_siem: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        forward_to_http_header: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        security_policy_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_reputation_profile_analysis akamai_appsec_reputation_profile_analysis} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param config_id: Unique identifier of the security configuration. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_reputation_profile_analysis#config_id AppsecReputationProfileAnalysis#config_id}
        :param forward_shared_ip_to_http_header_siem: Whether to add a value indicating that shared IPs are included in HTTP header and SIEM integration. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_reputation_profile_analysis#forward_shared_ip_to_http_header_siem AppsecReputationProfileAnalysis#forward_shared_ip_to_http_header_siem}
        :param forward_to_http_header: Whether to add client reputation details to requests forwarded to the origin server. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_reputation_profile_analysis#forward_to_http_header AppsecReputationProfileAnalysis#forward_to_http_header}
        :param security_policy_id: Unique identifier of the security policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_reputation_profile_analysis#security_policy_id AppsecReputationProfileAnalysis#security_policy_id}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_reputation_profile_analysis#id AppsecReputationProfileAnalysis#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9894ecc8589c97acade9a56fb6afe2c5602ddb08f1c0cc20953641d36aa57ec)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AppsecReputationProfileAnalysisConfig(
            config_id=config_id,
            forward_shared_ip_to_http_header_siem=forward_shared_ip_to_http_header_siem,
            forward_to_http_header=forward_to_http_header,
            security_policy_id=security_policy_id,
            id=id,
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
        '''Generates CDKTF code for importing a AppsecReputationProfileAnalysis resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the AppsecReputationProfileAnalysis to import.
        :param import_from_id: The id of the existing AppsecReputationProfileAnalysis that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_reputation_profile_analysis#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the AppsecReputationProfileAnalysis to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68f21c53f3f839725d93065e3b18eaa6682145a4b1336f6f255b887274b0324b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    @jsii.member(jsii_name="configIdInput")
    def config_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "configIdInput"))

    @builtins.property
    @jsii.member(jsii_name="forwardSharedIpToHttpHeaderSiemInput")
    def forward_shared_ip_to_http_header_siem_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "forwardSharedIpToHttpHeaderSiemInput"))

    @builtins.property
    @jsii.member(jsii_name="forwardToHttpHeaderInput")
    def forward_to_http_header_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "forwardToHttpHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="securityPolicyIdInput")
    def security_policy_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityPolicyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="configId")
    def config_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "configId"))

    @config_id.setter
    def config_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3fa7a51522517bd29e0ac063b6066f805cf679df2c7bacbe9dfb6dc2769a3d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configId", value)

    @builtins.property
    @jsii.member(jsii_name="forwardSharedIpToHttpHeaderSiem")
    def forward_shared_ip_to_http_header_siem(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "forwardSharedIpToHttpHeaderSiem"))

    @forward_shared_ip_to_http_header_siem.setter
    def forward_shared_ip_to_http_header_siem(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f40478bf016fd05295f6dc4801fa5d0a87195573a37e9d43fb045f23ed898b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forwardSharedIpToHttpHeaderSiem", value)

    @builtins.property
    @jsii.member(jsii_name="forwardToHttpHeader")
    def forward_to_http_header(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "forwardToHttpHeader"))

    @forward_to_http_header.setter
    def forward_to_http_header(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__504430e0f5ae502ad01aad2c02149330c206cba8af44a669fcfb63d26ab73d8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forwardToHttpHeader", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__572de77bc2f58a6b895719bf3f76605ec1a7df353bc9d9a3b14f6f2d8a5d98be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="securityPolicyId")
    def security_policy_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityPolicyId"))

    @security_policy_id.setter
    def security_policy_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a222e0c5b21f1cb495512beb08c3dca17df47920322e51eb29aee774c489bdd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityPolicyId", value)


@jsii.data_type(
    jsii_type="akamai.appsecReputationProfileAnalysis.AppsecReputationProfileAnalysisConfig",
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
        "forward_shared_ip_to_http_header_siem": "forwardSharedIpToHttpHeaderSiem",
        "forward_to_http_header": "forwardToHttpHeader",
        "security_policy_id": "securityPolicyId",
        "id": "id",
    },
)
class AppsecReputationProfileAnalysisConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        forward_shared_ip_to_http_header_siem: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        forward_to_http_header: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        security_policy_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param config_id: Unique identifier of the security configuration. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_reputation_profile_analysis#config_id AppsecReputationProfileAnalysis#config_id}
        :param forward_shared_ip_to_http_header_siem: Whether to add a value indicating that shared IPs are included in HTTP header and SIEM integration. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_reputation_profile_analysis#forward_shared_ip_to_http_header_siem AppsecReputationProfileAnalysis#forward_shared_ip_to_http_header_siem}
        :param forward_to_http_header: Whether to add client reputation details to requests forwarded to the origin server. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_reputation_profile_analysis#forward_to_http_header AppsecReputationProfileAnalysis#forward_to_http_header}
        :param security_policy_id: Unique identifier of the security policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_reputation_profile_analysis#security_policy_id AppsecReputationProfileAnalysis#security_policy_id}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_reputation_profile_analysis#id AppsecReputationProfileAnalysis#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97813b7deb088291844ec727a04398a4bc245ab84f92cd716617af0a91673de0)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument config_id", value=config_id, expected_type=type_hints["config_id"])
            check_type(argname="argument forward_shared_ip_to_http_header_siem", value=forward_shared_ip_to_http_header_siem, expected_type=type_hints["forward_shared_ip_to_http_header_siem"])
            check_type(argname="argument forward_to_http_header", value=forward_to_http_header, expected_type=type_hints["forward_to_http_header"])
            check_type(argname="argument security_policy_id", value=security_policy_id, expected_type=type_hints["security_policy_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "config_id": config_id,
            "forward_shared_ip_to_http_header_siem": forward_shared_ip_to_http_header_siem,
            "forward_to_http_header": forward_to_http_header,
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
        if id is not None:
            self._values["id"] = id

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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_reputation_profile_analysis#config_id AppsecReputationProfileAnalysis#config_id}
        '''
        result = self._values.get("config_id")
        assert result is not None, "Required property 'config_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def forward_shared_ip_to_http_header_siem(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Whether to add a value indicating that shared IPs are included in HTTP header and SIEM integration.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_reputation_profile_analysis#forward_shared_ip_to_http_header_siem AppsecReputationProfileAnalysis#forward_shared_ip_to_http_header_siem}
        '''
        result = self._values.get("forward_shared_ip_to_http_header_siem")
        assert result is not None, "Required property 'forward_shared_ip_to_http_header_siem' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def forward_to_http_header(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Whether to add client reputation details to requests forwarded to the origin server.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_reputation_profile_analysis#forward_to_http_header AppsecReputationProfileAnalysis#forward_to_http_header}
        '''
        result = self._values.get("forward_to_http_header")
        assert result is not None, "Required property 'forward_to_http_header' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def security_policy_id(self) -> builtins.str:
        '''Unique identifier of the security policy.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_reputation_profile_analysis#security_policy_id AppsecReputationProfileAnalysis#security_policy_id}
        '''
        result = self._values.get("security_policy_id")
        assert result is not None, "Required property 'security_policy_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_reputation_profile_analysis#id AppsecReputationProfileAnalysis#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsecReputationProfileAnalysisConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AppsecReputationProfileAnalysis",
    "AppsecReputationProfileAnalysisConfig",
]

publication.publish()

def _typecheckingstub__e9894ecc8589c97acade9a56fb6afe2c5602ddb08f1c0cc20953641d36aa57ec(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    config_id: jsii.Number,
    forward_shared_ip_to_http_header_siem: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    forward_to_http_header: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    security_policy_id: builtins.str,
    id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__68f21c53f3f839725d93065e3b18eaa6682145a4b1336f6f255b887274b0324b(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3fa7a51522517bd29e0ac063b6066f805cf679df2c7bacbe9dfb6dc2769a3d7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f40478bf016fd05295f6dc4801fa5d0a87195573a37e9d43fb045f23ed898b9(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__504430e0f5ae502ad01aad2c02149330c206cba8af44a669fcfb63d26ab73d8d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__572de77bc2f58a6b895719bf3f76605ec1a7df353bc9d9a3b14f6f2d8a5d98be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a222e0c5b21f1cb495512beb08c3dca17df47920322e51eb29aee774c489bdd4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97813b7deb088291844ec727a04398a4bc245ab84f92cd716617af0a91673de0(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    config_id: jsii.Number,
    forward_shared_ip_to_http_header_siem: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    forward_to_http_header: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    security_policy_id: builtins.str,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
