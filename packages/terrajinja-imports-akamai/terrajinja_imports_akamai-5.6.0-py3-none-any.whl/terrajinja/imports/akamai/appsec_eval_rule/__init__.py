'''
# `akamai_appsec_eval_rule`

Refer to the Terraform Registry for docs: [`akamai_appsec_eval_rule`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_eval_rule).
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


class AppsecEvalRule(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.appsecEvalRule.AppsecEvalRule",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_eval_rule akamai_appsec_eval_rule}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        config_id: jsii.Number,
        rule_action: builtins.str,
        rule_id: jsii.Number,
        security_policy_id: builtins.str,
        condition_exception: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_eval_rule akamai_appsec_eval_rule} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param config_id: Unique identifier of the security configuration. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_eval_rule#config_id AppsecEvalRule#config_id}
        :param rule_action: Action to be taken when the evaluation rule is triggered. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_eval_rule#rule_action AppsecEvalRule#rule_action}
        :param rule_id: Unique identifier of the evaluation rule being modified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_eval_rule#rule_id AppsecEvalRule#rule_id}
        :param security_policy_id: Unique identifier of the security policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_eval_rule#security_policy_id AppsecEvalRule#security_policy_id}
        :param condition_exception: JSON-formatted condition and exception information for the evaluation rule. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_eval_rule#condition_exception AppsecEvalRule#condition_exception}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_eval_rule#id AppsecEvalRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f68a8fd4a9f45050c3c9f797a3a6d8211191262e56da7a4cb70457c494aea34b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AppsecEvalRuleConfig(
            config_id=config_id,
            rule_action=rule_action,
            rule_id=rule_id,
            security_policy_id=security_policy_id,
            condition_exception=condition_exception,
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
        '''Generates CDKTF code for importing a AppsecEvalRule resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the AppsecEvalRule to import.
        :param import_from_id: The id of the existing AppsecEvalRule that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_eval_rule#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the AppsecEvalRule to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2eb3a6378b8c5d0725c8104c43e13f3e1f34ad8640ed379185baf3d1506137ae)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1fcffaec202ca61aadd8878d831c1ed97eb08d320c6420a9fae9fa1a50b5323c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "conditionException", value)

    @builtins.property
    @jsii.member(jsii_name="configId")
    def config_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "configId"))

    @config_id.setter
    def config_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a891e6c02b9fe6026890ef42d1e0d12405f085db8c0ed9087e80bcdccd1ef51e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__552e7c0e01ff7ac7bbb4ba3edb130701c962a2df98e3f009a98459e8457a2be9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ruleAction")
    def rule_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleAction"))

    @rule_action.setter
    def rule_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f6bf7d1db44021d7e063bee2b20c9d052cfeb2cd27f9c3c55471b70772caaca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleAction", value)

    @builtins.property
    @jsii.member(jsii_name="ruleId")
    def rule_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ruleId"))

    @rule_id.setter
    def rule_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7049b2bc287e331651cefb9cb04b7d1213f361fcf3b2f7e078b01d2feeebc77b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleId", value)

    @builtins.property
    @jsii.member(jsii_name="securityPolicyId")
    def security_policy_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityPolicyId"))

    @security_policy_id.setter
    def security_policy_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77803d48c71a5f818e86a6881e23c34b88fcb5832411508ba41c27d4784db872)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityPolicyId", value)


@jsii.data_type(
    jsii_type="akamai.appsecEvalRule.AppsecEvalRuleConfig",
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
        "rule_action": "ruleAction",
        "rule_id": "ruleId",
        "security_policy_id": "securityPolicyId",
        "condition_exception": "conditionException",
        "id": "id",
    },
)
class AppsecEvalRuleConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        rule_action: builtins.str,
        rule_id: jsii.Number,
        security_policy_id: builtins.str,
        condition_exception: typing.Optional[builtins.str] = None,
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
        :param config_id: Unique identifier of the security configuration. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_eval_rule#config_id AppsecEvalRule#config_id}
        :param rule_action: Action to be taken when the evaluation rule is triggered. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_eval_rule#rule_action AppsecEvalRule#rule_action}
        :param rule_id: Unique identifier of the evaluation rule being modified. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_eval_rule#rule_id AppsecEvalRule#rule_id}
        :param security_policy_id: Unique identifier of the security policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_eval_rule#security_policy_id AppsecEvalRule#security_policy_id}
        :param condition_exception: JSON-formatted condition and exception information for the evaluation rule. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_eval_rule#condition_exception AppsecEvalRule#condition_exception}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_eval_rule#id AppsecEvalRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bdfdd5e2d949e4f929baa22d528f42160f692733a3ab50ea23f8fa48baef717)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument config_id", value=config_id, expected_type=type_hints["config_id"])
            check_type(argname="argument rule_action", value=rule_action, expected_type=type_hints["rule_action"])
            check_type(argname="argument rule_id", value=rule_id, expected_type=type_hints["rule_id"])
            check_type(argname="argument security_policy_id", value=security_policy_id, expected_type=type_hints["security_policy_id"])
            check_type(argname="argument condition_exception", value=condition_exception, expected_type=type_hints["condition_exception"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "config_id": config_id,
            "rule_action": rule_action,
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_eval_rule#config_id AppsecEvalRule#config_id}
        '''
        result = self._values.get("config_id")
        assert result is not None, "Required property 'config_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def rule_action(self) -> builtins.str:
        '''Action to be taken when the evaluation rule is triggered.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_eval_rule#rule_action AppsecEvalRule#rule_action}
        '''
        result = self._values.get("rule_action")
        assert result is not None, "Required property 'rule_action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_id(self) -> jsii.Number:
        '''Unique identifier of the evaluation rule being modified.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_eval_rule#rule_id AppsecEvalRule#rule_id}
        '''
        result = self._values.get("rule_id")
        assert result is not None, "Required property 'rule_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def security_policy_id(self) -> builtins.str:
        '''Unique identifier of the security policy.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_eval_rule#security_policy_id AppsecEvalRule#security_policy_id}
        '''
        result = self._values.get("security_policy_id")
        assert result is not None, "Required property 'security_policy_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def condition_exception(self) -> typing.Optional[builtins.str]:
        '''JSON-formatted condition and exception information for the evaluation rule.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_eval_rule#condition_exception AppsecEvalRule#condition_exception}
        '''
        result = self._values.get("condition_exception")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/appsec_eval_rule#id AppsecEvalRule#id}.

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
        return "AppsecEvalRuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AppsecEvalRule",
    "AppsecEvalRuleConfig",
]

publication.publish()

def _typecheckingstub__f68a8fd4a9f45050c3c9f797a3a6d8211191262e56da7a4cb70457c494aea34b(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    config_id: jsii.Number,
    rule_action: builtins.str,
    rule_id: jsii.Number,
    security_policy_id: builtins.str,
    condition_exception: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__2eb3a6378b8c5d0725c8104c43e13f3e1f34ad8640ed379185baf3d1506137ae(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fcffaec202ca61aadd8878d831c1ed97eb08d320c6420a9fae9fa1a50b5323c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a891e6c02b9fe6026890ef42d1e0d12405f085db8c0ed9087e80bcdccd1ef51e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__552e7c0e01ff7ac7bbb4ba3edb130701c962a2df98e3f009a98459e8457a2be9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f6bf7d1db44021d7e063bee2b20c9d052cfeb2cd27f9c3c55471b70772caaca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7049b2bc287e331651cefb9cb04b7d1213f361fcf3b2f7e078b01d2feeebc77b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77803d48c71a5f818e86a6881e23c34b88fcb5832411508ba41c27d4784db872(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bdfdd5e2d949e4f929baa22d528f42160f692733a3ab50ea23f8fa48baef717(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    config_id: jsii.Number,
    rule_action: builtins.str,
    rule_id: jsii.Number,
    security_policy_id: builtins.str,
    condition_exception: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
