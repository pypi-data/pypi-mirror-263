'''
# `akamai_appsec_rule`

Refer to the Terraform Registry for docs: [`akamai_appsec_rule`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_rule).
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


class AppsecRule(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.appsecRule.AppsecRule",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_rule akamai_appsec_rule}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        config_id: jsii.Number,
        rule_id: jsii.Number,
        security_policy_id: builtins.str,
        condition_exception: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        rule_action: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_rule akamai_appsec_rule} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param config_id: Unique identifier of the security configuration. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_rule#config_id AppsecRule#config_id}
        :param rule_id: Unique identifier of the rule. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_rule#rule_id AppsecRule#rule_id}
        :param security_policy_id: Unique identifier of the security policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_rule#security_policy_id AppsecRule#security_policy_id}
        :param condition_exception: JSON-formatted condition and exception information for the rule. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_rule#condition_exception AppsecRule#condition_exception}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_rule#id AppsecRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param rule_action: Action to be taken when the rule is triggered. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_rule#rule_action AppsecRule#rule_action}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aafeef48c2b7f805405db59c056a983eb008cce73b15b82794ada859e2756065)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AppsecRuleConfig(
            config_id=config_id,
            rule_id=rule_id,
            security_policy_id=security_policy_id,
            condition_exception=condition_exception,
            id=id,
            rule_action=rule_action,
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
        '''Generates CDKTF code for importing a AppsecRule resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the AppsecRule to import.
        :param import_from_id: The id of the existing AppsecRule that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_rule#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the AppsecRule to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb1ee70a2c981102df69a695d16283c7ba0769661da8f64d23985b728472183e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetConditionException")
    def reset_condition_exception(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConditionException", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRuleAction")
    def reset_rule_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuleAction", []))

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
    @jsii.member(jsii_name="conditionExceptionInput")
    def condition_exception_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "conditionExceptionInput"))

    @builtins.property
    @jsii.member(jsii_name="configIdInput")
    def config_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "configIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleActionInput")
    def rule_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleActionInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleIdInput")
    def rule_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ruleIdInput"))

    @builtins.property
    @jsii.member(jsii_name="securityPolicyIdInput")
    def security_policy_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityPolicyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionException")
    def condition_exception(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "conditionException"))

    @condition_exception.setter
    def condition_exception(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02f58011dd9ed6d45c64dcb37f42272233bb33988bf2df1867940168e4fd2b31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "conditionException", value)

    @builtins.property
    @jsii.member(jsii_name="configId")
    def config_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "configId"))

    @config_id.setter
    def config_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26e714a39f38946de9ae4904090d0fa41e158376204bf25d1dd08493f3b69882)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16a0d22b2c3eec6e1e3fb6609046d510c8002786783aff9635680158b21d7020)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ruleAction")
    def rule_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleAction"))

    @rule_action.setter
    def rule_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c4a15302618231f6df2f7e84c2830d6c1c50d837b563c0bb71e73bbde7862a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleAction", value)

    @builtins.property
    @jsii.member(jsii_name="ruleId")
    def rule_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ruleId"))

    @rule_id.setter
    def rule_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ec4f67d2c695c49cdb1f9d96bd68504cc039fc966eb1dbceb076bde05078af4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleId", value)

    @builtins.property
    @jsii.member(jsii_name="securityPolicyId")
    def security_policy_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityPolicyId"))

    @security_policy_id.setter
    def security_policy_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59b5bb050790be1064530e53d275625edb1f639b6551b9c823e7d5670a457970)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityPolicyId", value)


@jsii.data_type(
    jsii_type="akamai.appsecRule.AppsecRuleConfig",
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
        "rule_id": "ruleId",
        "security_policy_id": "securityPolicyId",
        "condition_exception": "conditionException",
        "id": "id",
        "rule_action": "ruleAction",
    },
)
class AppsecRuleConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        rule_id: jsii.Number,
        security_policy_id: builtins.str,
        condition_exception: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        rule_action: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param config_id: Unique identifier of the security configuration. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_rule#config_id AppsecRule#config_id}
        :param rule_id: Unique identifier of the rule. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_rule#rule_id AppsecRule#rule_id}
        :param security_policy_id: Unique identifier of the security policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_rule#security_policy_id AppsecRule#security_policy_id}
        :param condition_exception: JSON-formatted condition and exception information for the rule. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_rule#condition_exception AppsecRule#condition_exception}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_rule#id AppsecRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param rule_action: Action to be taken when the rule is triggered. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_rule#rule_action AppsecRule#rule_action}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62340f6997a80e8d30936e09ea7c71f2c7095125578b47b33c39f74d19bba1d6)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument config_id", value=config_id, expected_type=type_hints["config_id"])
            check_type(argname="argument rule_id", value=rule_id, expected_type=type_hints["rule_id"])
            check_type(argname="argument security_policy_id", value=security_policy_id, expected_type=type_hints["security_policy_id"])
            check_type(argname="argument condition_exception", value=condition_exception, expected_type=type_hints["condition_exception"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument rule_action", value=rule_action, expected_type=type_hints["rule_action"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "config_id": config_id,
            "rule_id": rule_id,
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
        if condition_exception is not None:
            self._values["condition_exception"] = condition_exception
        if id is not None:
            self._values["id"] = id
        if rule_action is not None:
            self._values["rule_action"] = rule_action

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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_rule#config_id AppsecRule#config_id}
        '''
        result = self._values.get("config_id")
        assert result is not None, "Required property 'config_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def rule_id(self) -> jsii.Number:
        '''Unique identifier of the rule.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_rule#rule_id AppsecRule#rule_id}
        '''
        result = self._values.get("rule_id")
        assert result is not None, "Required property 'rule_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def security_policy_id(self) -> builtins.str:
        '''Unique identifier of the security policy.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_rule#security_policy_id AppsecRule#security_policy_id}
        '''
        result = self._values.get("security_policy_id")
        assert result is not None, "Required property 'security_policy_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def condition_exception(self) -> typing.Optional[builtins.str]:
        '''JSON-formatted condition and exception information for the rule.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_rule#condition_exception AppsecRule#condition_exception}
        '''
        result = self._values.get("condition_exception")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_rule#id AppsecRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rule_action(self) -> typing.Optional[builtins.str]:
        '''Action to be taken when the rule is triggered.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_rule#rule_action AppsecRule#rule_action}
        '''
        result = self._values.get("rule_action")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsecRuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AppsecRule",
    "AppsecRuleConfig",
]

publication.publish()

def _typecheckingstub__aafeef48c2b7f805405db59c056a983eb008cce73b15b82794ada859e2756065(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    config_id: jsii.Number,
    rule_id: jsii.Number,
    security_policy_id: builtins.str,
    condition_exception: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    rule_action: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__fb1ee70a2c981102df69a695d16283c7ba0769661da8f64d23985b728472183e(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02f58011dd9ed6d45c64dcb37f42272233bb33988bf2df1867940168e4fd2b31(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26e714a39f38946de9ae4904090d0fa41e158376204bf25d1dd08493f3b69882(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16a0d22b2c3eec6e1e3fb6609046d510c8002786783aff9635680158b21d7020(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c4a15302618231f6df2f7e84c2830d6c1c50d837b563c0bb71e73bbde7862a9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ec4f67d2c695c49cdb1f9d96bd68504cc039fc966eb1dbceb076bde05078af4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59b5bb050790be1064530e53d275625edb1f639b6551b9c823e7d5670a457970(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62340f6997a80e8d30936e09ea7c71f2c7095125578b47b33c39f74d19bba1d6(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    config_id: jsii.Number,
    rule_id: jsii.Number,
    security_policy_id: builtins.str,
    condition_exception: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    rule_action: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
