'''
# `akamai_appsec_slow_post`

Refer to the Terraform Registry for docs: [`akamai_appsec_slow_post`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_slow_post).
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


class AppsecSlowPost(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.appsecSlowPost.AppsecSlowPost",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_slow_post akamai_appsec_slow_post}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        config_id: jsii.Number,
        security_policy_id: builtins.str,
        slow_rate_action: builtins.str,
        duration_threshold_timeout: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        slow_rate_threshold_period: typing.Optional[jsii.Number] = None,
        slow_rate_threshold_rate: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_slow_post akamai_appsec_slow_post} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param config_id: Unique identifier of the security configuration. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_slow_post#config_id AppsecSlowPost#config_id}
        :param security_policy_id: Unique identifier of the security policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_slow_post#security_policy_id AppsecSlowPost#security_policy_id}
        :param slow_rate_action: Action to be taken when slow POST protection is triggered. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_slow_post#slow_rate_action AppsecSlowPost#slow_rate_action}
        :param duration_threshold_timeout: Maximum amount of time (in seconds) within which the first 8KB of the POST body must be received to avoid triggering the specified action. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_slow_post#duration_threshold_timeout AppsecSlowPost#duration_threshold_timeout}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_slow_post#id AppsecSlowPost#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param slow_rate_threshold_period: Amount of time (in seconds) that the server should allow a request before marking the request as being too slow. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_slow_post#slow_rate_threshold_period AppsecSlowPost#slow_rate_threshold_period}
        :param slow_rate_threshold_rate: Average rate (in bytes per second over the specified time period) allowed before the specified action is triggered. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_slow_post#slow_rate_threshold_rate AppsecSlowPost#slow_rate_threshold_rate}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6831e791a4c439468f03f1af1676c961e1f4e57e46ecb1375319044ee8a98185)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AppsecSlowPostConfig(
            config_id=config_id,
            security_policy_id=security_policy_id,
            slow_rate_action=slow_rate_action,
            duration_threshold_timeout=duration_threshold_timeout,
            id=id,
            slow_rate_threshold_period=slow_rate_threshold_period,
            slow_rate_threshold_rate=slow_rate_threshold_rate,
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
        '''Generates CDKTF code for importing a AppsecSlowPost resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the AppsecSlowPost to import.
        :param import_from_id: The id of the existing AppsecSlowPost that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_slow_post#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the AppsecSlowPost to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fefb3428e005834b20498eb35baf14bd61a45f13fcf5918d064cf859d1159489)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetDurationThresholdTimeout")
    def reset_duration_threshold_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDurationThresholdTimeout", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSlowRateThresholdPeriod")
    def reset_slow_rate_threshold_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSlowRateThresholdPeriod", []))

    @jsii.member(jsii_name="resetSlowRateThresholdRate")
    def reset_slow_rate_threshold_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSlowRateThresholdRate", []))

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
    @jsii.member(jsii_name="durationThresholdTimeoutInput")
    def duration_threshold_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "durationThresholdTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="securityPolicyIdInput")
    def security_policy_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityPolicyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="slowRateActionInput")
    def slow_rate_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "slowRateActionInput"))

    @builtins.property
    @jsii.member(jsii_name="slowRateThresholdPeriodInput")
    def slow_rate_threshold_period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "slowRateThresholdPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="slowRateThresholdRateInput")
    def slow_rate_threshold_rate_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "slowRateThresholdRateInput"))

    @builtins.property
    @jsii.member(jsii_name="configId")
    def config_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "configId"))

    @config_id.setter
    def config_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2fce89d1dd56c3989def2e117b6acc6125c6f2c134b98529324b44f33e08c1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configId", value)

    @builtins.property
    @jsii.member(jsii_name="durationThresholdTimeout")
    def duration_threshold_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "durationThresholdTimeout"))

    @duration_threshold_timeout.setter
    def duration_threshold_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf5c18b522949daa4896a02826997c35602d2d9bb84ebbe58b542e2f73fcecc5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "durationThresholdTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__881df8c21de49a2f3f9540ad123c6c4ab9f357a0c1e685dd393847772a2e8f0e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="securityPolicyId")
    def security_policy_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityPolicyId"))

    @security_policy_id.setter
    def security_policy_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b56bcaf477751fe989da50bdfadbc0f0de4b5c2bc50cfdb1eec354bc862b576c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityPolicyId", value)

    @builtins.property
    @jsii.member(jsii_name="slowRateAction")
    def slow_rate_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "slowRateAction"))

    @slow_rate_action.setter
    def slow_rate_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34df176da12bfd43d12fb46f9cf4320ff23f16df1123bf38ff128361b62ff4c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "slowRateAction", value)

    @builtins.property
    @jsii.member(jsii_name="slowRateThresholdPeriod")
    def slow_rate_threshold_period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "slowRateThresholdPeriod"))

    @slow_rate_threshold_period.setter
    def slow_rate_threshold_period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03717f65b0fe5d78345a8f3ff9ef342087507f31b05642088a8386950ba8b399)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "slowRateThresholdPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="slowRateThresholdRate")
    def slow_rate_threshold_rate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "slowRateThresholdRate"))

    @slow_rate_threshold_rate.setter
    def slow_rate_threshold_rate(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__092b787884198aae4fefcfa534e99d9068de20b3dbfc779e7c15c4cc5a6f856f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "slowRateThresholdRate", value)


@jsii.data_type(
    jsii_type="akamai.appsecSlowPost.AppsecSlowPostConfig",
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
        "security_policy_id": "securityPolicyId",
        "slow_rate_action": "slowRateAction",
        "duration_threshold_timeout": "durationThresholdTimeout",
        "id": "id",
        "slow_rate_threshold_period": "slowRateThresholdPeriod",
        "slow_rate_threshold_rate": "slowRateThresholdRate",
    },
)
class AppsecSlowPostConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        security_policy_id: builtins.str,
        slow_rate_action: builtins.str,
        duration_threshold_timeout: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        slow_rate_threshold_period: typing.Optional[jsii.Number] = None,
        slow_rate_threshold_rate: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param config_id: Unique identifier of the security configuration. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_slow_post#config_id AppsecSlowPost#config_id}
        :param security_policy_id: Unique identifier of the security policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_slow_post#security_policy_id AppsecSlowPost#security_policy_id}
        :param slow_rate_action: Action to be taken when slow POST protection is triggered. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_slow_post#slow_rate_action AppsecSlowPost#slow_rate_action}
        :param duration_threshold_timeout: Maximum amount of time (in seconds) within which the first 8KB of the POST body must be received to avoid triggering the specified action. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_slow_post#duration_threshold_timeout AppsecSlowPost#duration_threshold_timeout}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_slow_post#id AppsecSlowPost#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param slow_rate_threshold_period: Amount of time (in seconds) that the server should allow a request before marking the request as being too slow. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_slow_post#slow_rate_threshold_period AppsecSlowPost#slow_rate_threshold_period}
        :param slow_rate_threshold_rate: Average rate (in bytes per second over the specified time period) allowed before the specified action is triggered. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_slow_post#slow_rate_threshold_rate AppsecSlowPost#slow_rate_threshold_rate}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17f5e1bc8371ab2f8c9be6969a2ddf7544f1238ab928a8286793b776ef44dd66)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument config_id", value=config_id, expected_type=type_hints["config_id"])
            check_type(argname="argument security_policy_id", value=security_policy_id, expected_type=type_hints["security_policy_id"])
            check_type(argname="argument slow_rate_action", value=slow_rate_action, expected_type=type_hints["slow_rate_action"])
            check_type(argname="argument duration_threshold_timeout", value=duration_threshold_timeout, expected_type=type_hints["duration_threshold_timeout"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument slow_rate_threshold_period", value=slow_rate_threshold_period, expected_type=type_hints["slow_rate_threshold_period"])
            check_type(argname="argument slow_rate_threshold_rate", value=slow_rate_threshold_rate, expected_type=type_hints["slow_rate_threshold_rate"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "config_id": config_id,
            "security_policy_id": security_policy_id,
            "slow_rate_action": slow_rate_action,
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
        if duration_threshold_timeout is not None:
            self._values["duration_threshold_timeout"] = duration_threshold_timeout
        if id is not None:
            self._values["id"] = id
        if slow_rate_threshold_period is not None:
            self._values["slow_rate_threshold_period"] = slow_rate_threshold_period
        if slow_rate_threshold_rate is not None:
            self._values["slow_rate_threshold_rate"] = slow_rate_threshold_rate

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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_slow_post#config_id AppsecSlowPost#config_id}
        '''
        result = self._values.get("config_id")
        assert result is not None, "Required property 'config_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def security_policy_id(self) -> builtins.str:
        '''Unique identifier of the security policy.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_slow_post#security_policy_id AppsecSlowPost#security_policy_id}
        '''
        result = self._values.get("security_policy_id")
        assert result is not None, "Required property 'security_policy_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def slow_rate_action(self) -> builtins.str:
        '''Action to be taken when slow POST protection is triggered.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_slow_post#slow_rate_action AppsecSlowPost#slow_rate_action}
        '''
        result = self._values.get("slow_rate_action")
        assert result is not None, "Required property 'slow_rate_action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def duration_threshold_timeout(self) -> typing.Optional[jsii.Number]:
        '''Maximum amount of time (in seconds) within which the first 8KB of the POST body must be received to avoid triggering the specified action.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_slow_post#duration_threshold_timeout AppsecSlowPost#duration_threshold_timeout}
        '''
        result = self._values.get("duration_threshold_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_slow_post#id AppsecSlowPost#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def slow_rate_threshold_period(self) -> typing.Optional[jsii.Number]:
        '''Amount of time (in seconds) that the server should allow a request before marking the request as being too slow.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_slow_post#slow_rate_threshold_period AppsecSlowPost#slow_rate_threshold_period}
        '''
        result = self._values.get("slow_rate_threshold_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def slow_rate_threshold_rate(self) -> typing.Optional[jsii.Number]:
        '''Average rate (in bytes per second over the specified time period) allowed before the specified action is triggered.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_slow_post#slow_rate_threshold_rate AppsecSlowPost#slow_rate_threshold_rate}
        '''
        result = self._values.get("slow_rate_threshold_rate")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsecSlowPostConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AppsecSlowPost",
    "AppsecSlowPostConfig",
]

publication.publish()

def _typecheckingstub__6831e791a4c439468f03f1af1676c961e1f4e57e46ecb1375319044ee8a98185(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    config_id: jsii.Number,
    security_policy_id: builtins.str,
    slow_rate_action: builtins.str,
    duration_threshold_timeout: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    slow_rate_threshold_period: typing.Optional[jsii.Number] = None,
    slow_rate_threshold_rate: typing.Optional[jsii.Number] = None,
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

def _typecheckingstub__fefb3428e005834b20498eb35baf14bd61a45f13fcf5918d064cf859d1159489(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2fce89d1dd56c3989def2e117b6acc6125c6f2c134b98529324b44f33e08c1c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf5c18b522949daa4896a02826997c35602d2d9bb84ebbe58b542e2f73fcecc5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__881df8c21de49a2f3f9540ad123c6c4ab9f357a0c1e685dd393847772a2e8f0e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b56bcaf477751fe989da50bdfadbc0f0de4b5c2bc50cfdb1eec354bc862b576c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34df176da12bfd43d12fb46f9cf4320ff23f16df1123bf38ff128361b62ff4c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03717f65b0fe5d78345a8f3ff9ef342087507f31b05642088a8386950ba8b399(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__092b787884198aae4fefcfa534e99d9068de20b3dbfc779e7c15c4cc5a6f856f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17f5e1bc8371ab2f8c9be6969a2ddf7544f1238ab928a8286793b776ef44dd66(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    config_id: jsii.Number,
    security_policy_id: builtins.str,
    slow_rate_action: builtins.str,
    duration_threshold_timeout: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    slow_rate_threshold_period: typing.Optional[jsii.Number] = None,
    slow_rate_threshold_rate: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass
