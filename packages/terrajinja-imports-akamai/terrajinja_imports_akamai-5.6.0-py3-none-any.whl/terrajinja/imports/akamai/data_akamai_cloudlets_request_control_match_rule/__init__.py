'''
# `data_akamai_cloudlets_request_control_match_rule`

Refer to the Terraform Registry for docs: [`data_akamai_cloudlets_request_control_match_rule`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule).
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


class DataAkamaiCloudletsRequestControlMatchRule(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsRequestControlMatchRule.DataAkamaiCloudletsRequestControlMatchRule",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule akamai_cloudlets_request_control_match_rule}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        id: typing.Optional[builtins.str] = None,
        match_rules: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudletsRequestControlMatchRuleMatchRules", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule akamai_cloudlets_request_control_match_rule} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#id DataAkamaiCloudletsRequestControlMatchRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param match_rules: match_rules block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#match_rules DataAkamaiCloudletsRequestControlMatchRule#match_rules}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e23b597445057b7b50212416e592c49af5b64295e4c8f7c2caa82580fb935f57)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAkamaiCloudletsRequestControlMatchRuleConfig(
            id=id,
            match_rules=match_rules,
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
        '''Generates CDKTF code for importing a DataAkamaiCloudletsRequestControlMatchRule resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the DataAkamaiCloudletsRequestControlMatchRule to import.
        :param import_from_id: The id of the existing DataAkamaiCloudletsRequestControlMatchRule that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the DataAkamaiCloudletsRequestControlMatchRule to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__327a6775f32dfe56e7455d623fd567b144c47234ec6c6e21d55b7cb8e44e7ecd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putMatchRules")
    def put_match_rules(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudletsRequestControlMatchRuleMatchRules", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee74d898c532ab5e907666fc2126d71f29e8c3fed8c24dada5550f063af57a36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchRules", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMatchRules")
    def reset_match_rules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchRules", []))

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
    @jsii.member(jsii_name="json")
    def json(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "json"))

    @builtins.property
    @jsii.member(jsii_name="matchRules")
    def match_rules(self) -> "DataAkamaiCloudletsRequestControlMatchRuleMatchRulesList":
        return typing.cast("DataAkamaiCloudletsRequestControlMatchRuleMatchRulesList", jsii.get(self, "matchRules"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="matchRulesInput")
    def match_rules_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsRequestControlMatchRuleMatchRules"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsRequestControlMatchRuleMatchRules"]]], jsii.get(self, "matchRulesInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__883973703e6deb7fa1ae75aca78f35c489a7321d11f5be2e5eb6812718c2d5b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsRequestControlMatchRule.DataAkamaiCloudletsRequestControlMatchRuleConfig",
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
        "match_rules": "matchRules",
    },
)
class DataAkamaiCloudletsRequestControlMatchRuleConfig(
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
        id: typing.Optional[builtins.str] = None,
        match_rules: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudletsRequestControlMatchRuleMatchRules", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#id DataAkamaiCloudletsRequestControlMatchRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param match_rules: match_rules block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#match_rules DataAkamaiCloudletsRequestControlMatchRule#match_rules}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2339e9c008917c5ca5a708d09d04a2b14414fcf18260025b2f1f56f5eea424e0)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument match_rules", value=match_rules, expected_type=type_hints["match_rules"])
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
        if id is not None:
            self._values["id"] = id
        if match_rules is not None:
            self._values["match_rules"] = match_rules

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
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#id DataAkamaiCloudletsRequestControlMatchRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_rules(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsRequestControlMatchRuleMatchRules"]]]:
        '''match_rules block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#match_rules DataAkamaiCloudletsRequestControlMatchRule#match_rules}
        '''
        result = self._values.get("match_rules")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsRequestControlMatchRuleMatchRules"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsRequestControlMatchRuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsRequestControlMatchRule.DataAkamaiCloudletsRequestControlMatchRuleMatchRules",
    jsii_struct_bases=[],
    name_mapping={
        "allow_deny": "allowDeny",
        "disabled": "disabled",
        "end": "end",
        "matches": "matches",
        "matches_always": "matchesAlways",
        "name": "name",
        "start": "start",
    },
)
class DataAkamaiCloudletsRequestControlMatchRuleMatchRules:
    def __init__(
        self,
        *,
        allow_deny: builtins.str,
        disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        end: typing.Optional[jsii.Number] = None,
        matches: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatches", typing.Dict[builtins.str, typing.Any]]]]] = None,
        matches_always: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
        start: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param allow_deny: If set to allow, the request is sent to origin when all conditions are true. If deny, the request is denied when all conditions are true. If denybranded, the request is denied and rerouted according to the configuration of the Request Control behavior Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#allow_deny DataAkamaiCloudletsRequestControlMatchRule#allow_deny}
        :param disabled: If set to true, disables a rule so it is not evaluated against incoming requests. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#disabled DataAkamaiCloudletsRequestControlMatchRule#disabled}
        :param end: The end time for this match (in seconds since the epoch). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#end DataAkamaiCloudletsRequestControlMatchRule#end}
        :param matches: matches block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#matches DataAkamaiCloudletsRequestControlMatchRule#matches}
        :param matches_always: Is used in some cloudlets to support default rules (rule that is always matched). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#matches_always DataAkamaiCloudletsRequestControlMatchRule#matches_always}
        :param name: The name of the rule. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#name DataAkamaiCloudletsRequestControlMatchRule#name}
        :param start: The start time for this match (in seconds since the epoch). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#start DataAkamaiCloudletsRequestControlMatchRule#start}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97f59f17895bf0b3e6eb340f22f36c89c5e31bfb55dccd8062d3d6d3139e2b0d)
            check_type(argname="argument allow_deny", value=allow_deny, expected_type=type_hints["allow_deny"])
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
            check_type(argname="argument end", value=end, expected_type=type_hints["end"])
            check_type(argname="argument matches", value=matches, expected_type=type_hints["matches"])
            check_type(argname="argument matches_always", value=matches_always, expected_type=type_hints["matches_always"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument start", value=start, expected_type=type_hints["start"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "allow_deny": allow_deny,
        }
        if disabled is not None:
            self._values["disabled"] = disabled
        if end is not None:
            self._values["end"] = end
        if matches is not None:
            self._values["matches"] = matches
        if matches_always is not None:
            self._values["matches_always"] = matches_always
        if name is not None:
            self._values["name"] = name
        if start is not None:
            self._values["start"] = start

    @builtins.property
    def allow_deny(self) -> builtins.str:
        '''If set to allow, the request is sent to origin when all conditions are true.

        If deny, the request is denied when all conditions are true. If denybranded, the request is denied and rerouted according to the configuration of the Request Control behavior

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#allow_deny DataAkamaiCloudletsRequestControlMatchRule#allow_deny}
        '''
        result = self._values.get("allow_deny")
        assert result is not None, "Required property 'allow_deny' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If set to true, disables a rule so it is not evaluated against incoming requests.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#disabled DataAkamaiCloudletsRequestControlMatchRule#disabled}
        '''
        result = self._values.get("disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def end(self) -> typing.Optional[jsii.Number]:
        '''The end time for this match (in seconds since the epoch).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#end DataAkamaiCloudletsRequestControlMatchRule#end}
        '''
        result = self._values.get("end")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def matches(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatches"]]]:
        '''matches block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#matches DataAkamaiCloudletsRequestControlMatchRule#matches}
        '''
        result = self._values.get("matches")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatches"]]], result)

    @builtins.property
    def matches_always(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Is used in some cloudlets to support default rules (rule that is always matched).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#matches_always DataAkamaiCloudletsRequestControlMatchRule#matches_always}
        '''
        result = self._values.get("matches_always")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the rule.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#name DataAkamaiCloudletsRequestControlMatchRule#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start(self) -> typing.Optional[jsii.Number]:
        '''The start time for this match (in seconds since the epoch).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#start DataAkamaiCloudletsRequestControlMatchRule#start}
        '''
        result = self._values.get("start")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsRequestControlMatchRuleMatchRules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudletsRequestControlMatchRuleMatchRulesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsRequestControlMatchRule.DataAkamaiCloudletsRequestControlMatchRuleMatchRulesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dcbf41856fbf451590b81c59b343d6516bc11e8d6bfe2b6fea9213875a88b0c0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiCloudletsRequestControlMatchRuleMatchRulesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7551fd8357f83045b493700599741e4cb20382c3aaa5acfe5ce61f7da2ccfa5)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiCloudletsRequestControlMatchRuleMatchRulesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5154183626ecfdb47be61f581fa90718136257cd22482f4fadaa0255ae068bf1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__51cc31782b07f394df6d59a3493d837fca0191d2216f55ec5cc4f3d544f2ebe2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7da616d6025561e7f8f31b90c6cebc7dfd4a52ee498a3e48e30a3bc51945ac75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsRequestControlMatchRuleMatchRules]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsRequestControlMatchRuleMatchRules]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsRequestControlMatchRuleMatchRules]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__649bcd13eac4c6aa3385e16990acee3c05b0696de42096334abf5c0066db900e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsRequestControlMatchRule.DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatches",
    jsii_struct_bases=[],
    name_mapping={
        "case_sensitive": "caseSensitive",
        "check_ips": "checkIps",
        "match_operator": "matchOperator",
        "match_type": "matchType",
        "match_value": "matchValue",
        "negate": "negate",
        "object_match_value": "objectMatchValue",
    },
)
class DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatches:
    def __init__(
        self,
        *,
        case_sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        check_ips: typing.Optional[builtins.str] = None,
        match_operator: typing.Optional[builtins.str] = None,
        match_type: typing.Optional[builtins.str] = None,
        match_value: typing.Optional[builtins.str] = None,
        negate: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        object_match_value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValue", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param case_sensitive: If true, the match is case sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#case_sensitive DataAkamaiCloudletsRequestControlMatchRule#case_sensitive}
        :param check_ips: For clientip, continent, countrycode, proxy, and regioncode match types, the part of the request that determines the IP address to use. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#check_ips DataAkamaiCloudletsRequestControlMatchRule#check_ips}
        :param match_operator: Valid entries for this property: contains, exists, and equals. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#match_operator DataAkamaiCloudletsRequestControlMatchRule#match_operator}
        :param match_type: The type of match used. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#match_type DataAkamaiCloudletsRequestControlMatchRule#match_type}
        :param match_value: Depends on the matchType. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#match_value DataAkamaiCloudletsRequestControlMatchRule#match_value}
        :param negate: If true, negates the match. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#negate DataAkamaiCloudletsRequestControlMatchRule#negate}
        :param object_match_value: object_match_value block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#object_match_value DataAkamaiCloudletsRequestControlMatchRule#object_match_value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f387bd4ed5cf82c767258c296f7078eeba0310554380cdc70bd7c2cb2ffebb0)
            check_type(argname="argument case_sensitive", value=case_sensitive, expected_type=type_hints["case_sensitive"])
            check_type(argname="argument check_ips", value=check_ips, expected_type=type_hints["check_ips"])
            check_type(argname="argument match_operator", value=match_operator, expected_type=type_hints["match_operator"])
            check_type(argname="argument match_type", value=match_type, expected_type=type_hints["match_type"])
            check_type(argname="argument match_value", value=match_value, expected_type=type_hints["match_value"])
            check_type(argname="argument negate", value=negate, expected_type=type_hints["negate"])
            check_type(argname="argument object_match_value", value=object_match_value, expected_type=type_hints["object_match_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if case_sensitive is not None:
            self._values["case_sensitive"] = case_sensitive
        if check_ips is not None:
            self._values["check_ips"] = check_ips
        if match_operator is not None:
            self._values["match_operator"] = match_operator
        if match_type is not None:
            self._values["match_type"] = match_type
        if match_value is not None:
            self._values["match_value"] = match_value
        if negate is not None:
            self._values["negate"] = negate
        if object_match_value is not None:
            self._values["object_match_value"] = object_match_value

    @builtins.property
    def case_sensitive(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If true, the match is case sensitive.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#case_sensitive DataAkamaiCloudletsRequestControlMatchRule#case_sensitive}
        '''
        result = self._values.get("case_sensitive")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def check_ips(self) -> typing.Optional[builtins.str]:
        '''For clientip, continent, countrycode, proxy, and regioncode match types, the part of the request that determines the IP address to use.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#check_ips DataAkamaiCloudletsRequestControlMatchRule#check_ips}
        '''
        result = self._values.get("check_ips")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_operator(self) -> typing.Optional[builtins.str]:
        '''Valid entries for this property: contains, exists, and equals.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#match_operator DataAkamaiCloudletsRequestControlMatchRule#match_operator}
        '''
        result = self._values.get("match_operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_type(self) -> typing.Optional[builtins.str]:
        '''The type of match used.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#match_type DataAkamaiCloudletsRequestControlMatchRule#match_type}
        '''
        result = self._values.get("match_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_value(self) -> typing.Optional[builtins.str]:
        '''Depends on the matchType.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#match_value DataAkamaiCloudletsRequestControlMatchRule#match_value}
        '''
        result = self._values.get("match_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def negate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If true, negates the match.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#negate DataAkamaiCloudletsRequestControlMatchRule#negate}
        '''
        result = self._values.get("negate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def object_match_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValue"]]]:
        '''object_match_value block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#object_match_value DataAkamaiCloudletsRequestControlMatchRule#object_match_value}
        '''
        result = self._values.get("object_match_value")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValue"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatches(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsRequestControlMatchRule.DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__60e16e1cbf69f073b2e596220ad952bb5fc1301406f275e0e56c139e7243e3e4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__931ce7fd9dc1f93dfa0be7736b4ecac462ee61ed4554fcfb7af64616b289e217)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3999a79f88792149a92071dfa1eab068174ce1b2f1b08c2c0df47e2b16ae1ef3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f1ec2d60c40a3b20a4169c6d298a010173efe7ed044bef2b7d29da5ba5d6ad30)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fcbb0eb59ad19f02fc656e69e58a07512d41ff7031842cba3f5554ad0b17e5a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatches]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatches]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatches]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1eb1558c7967ba18a515f76bd93d2303d902f3d8244e4df633457078ba0ee200)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsRequestControlMatchRule.DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValue",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "name": "name",
        "name_case_sensitive": "nameCaseSensitive",
        "name_has_wildcard": "nameHasWildcard",
        "options": "options",
        "value": "value",
    },
)
class DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValue:
    def __init__(
        self,
        *,
        type: builtins.str,
        name: typing.Optional[builtins.str] = None,
        name_case_sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        name_has_wildcard: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        options: typing.Optional[typing.Union["DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValueOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        value: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: The array type, which can be one of the following: object or simple. Use the simple option when adding only an array of string-based values Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#type DataAkamaiCloudletsRequestControlMatchRule#type}
        :param name: If using a match type that supports name attributes, enter the value in the incoming request to match on. The following match types support this property: cookie, header, parameter, and query Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#name DataAkamaiCloudletsRequestControlMatchRule#name}
        :param name_case_sensitive: Set to true if the entry for the name property should be evaluated based on case sensitivity. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#name_case_sensitive DataAkamaiCloudletsRequestControlMatchRule#name_case_sensitive}
        :param name_has_wildcard: Set to true if the entry for the name property includes wildcards. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#name_has_wildcard DataAkamaiCloudletsRequestControlMatchRule#name_has_wildcard}
        :param options: options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#options DataAkamaiCloudletsRequestControlMatchRule#options}
        :param value: The value attributes in the incoming request to match on (use only with simple type). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#value DataAkamaiCloudletsRequestControlMatchRule#value}
        '''
        if isinstance(options, dict):
            options = DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValueOptions(**options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aced90d6a9e32373d8d18f6595f35ba52027fb037e862b23afca003a5eefac19)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument name_case_sensitive", value=name_case_sensitive, expected_type=type_hints["name_case_sensitive"])
            check_type(argname="argument name_has_wildcard", value=name_has_wildcard, expected_type=type_hints["name_has_wildcard"])
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if name is not None:
            self._values["name"] = name
        if name_case_sensitive is not None:
            self._values["name_case_sensitive"] = name_case_sensitive
        if name_has_wildcard is not None:
            self._values["name_has_wildcard"] = name_has_wildcard
        if options is not None:
            self._values["options"] = options
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def type(self) -> builtins.str:
        '''The array type, which can be one of the following: object or simple.

        Use the simple option when adding only an array of string-based values

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#type DataAkamaiCloudletsRequestControlMatchRule#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''If using a match type that supports name attributes, enter the value in the incoming request to match on.

        The following match types support this property: cookie, header, parameter, and query

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#name DataAkamaiCloudletsRequestControlMatchRule#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name_case_sensitive(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set to true if the entry for the name property should be evaluated based on case sensitivity.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#name_case_sensitive DataAkamaiCloudletsRequestControlMatchRule#name_case_sensitive}
        '''
        result = self._values.get("name_case_sensitive")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def name_has_wildcard(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set to true if the entry for the name property includes wildcards.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#name_has_wildcard DataAkamaiCloudletsRequestControlMatchRule#name_has_wildcard}
        '''
        result = self._values.get("name_has_wildcard")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def options(
        self,
    ) -> typing.Optional["DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValueOptions"]:
        '''options block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#options DataAkamaiCloudletsRequestControlMatchRule#options}
        '''
        result = self._values.get("options")
        return typing.cast(typing.Optional["DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValueOptions"], result)

    @builtins.property
    def value(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The value attributes in the incoming request to match on (use only with simple type).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#value DataAkamaiCloudletsRequestControlMatchRule#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValueList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsRequestControlMatchRule.DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValueList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e2303631b758bae0014c605b4d9a0f3bf6304745c3c6a9b2bca9be521704a4c2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValueOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d485260c6a3ef825d330d5fb2d494e271059ba58bd9dfad81d69626eac7932d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValueOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d119735be1b47ff19bcc2b231a473ab74f60c46a491b7fc4e05775f8bcbf35c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5e4c9f3091a4f3a03e4c6ae7536a2731bf354f713608e48d75689b3fe72b6e3f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__944d3e4802dd9c3d23ef4a75404e853aa7a4f7c525533e906ba9c1f4f403f9b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValue]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValue]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValue]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a3e7e037f462a30fa640f857e2879fc5933e29e8903c4c6c5d735edc387f42e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsRequestControlMatchRule.DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValueOptions",
    jsii_struct_bases=[],
    name_mapping={
        "value": "value",
        "value_case_sensitive": "valueCaseSensitive",
        "value_escaped": "valueEscaped",
        "value_has_wildcard": "valueHasWildcard",
    },
)
class DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValueOptions:
    def __init__(
        self,
        *,
        value: typing.Optional[typing.Sequence[builtins.str]] = None,
        value_case_sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        value_escaped: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        value_has_wildcard: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param value: The value attributes in the incoming request to match on. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#value DataAkamaiCloudletsRequestControlMatchRule#value}
        :param value_case_sensitive: Set to true if the entries for the value property should be evaluated based on case sensitivity. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#value_case_sensitive DataAkamaiCloudletsRequestControlMatchRule#value_case_sensitive}
        :param value_escaped: Set to true if provided value should be compared in escaped form. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#value_escaped DataAkamaiCloudletsRequestControlMatchRule#value_escaped}
        :param value_has_wildcard: Set to true if the entries for the value property include wildcards. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#value_has_wildcard DataAkamaiCloudletsRequestControlMatchRule#value_has_wildcard}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e0f6ce5d2cfe854aa0957814d7068bb6e9a8ba6759de6109a591c139dc4fcc1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument value_case_sensitive", value=value_case_sensitive, expected_type=type_hints["value_case_sensitive"])
            check_type(argname="argument value_escaped", value=value_escaped, expected_type=type_hints["value_escaped"])
            check_type(argname="argument value_has_wildcard", value=value_has_wildcard, expected_type=type_hints["value_has_wildcard"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if value is not None:
            self._values["value"] = value
        if value_case_sensitive is not None:
            self._values["value_case_sensitive"] = value_case_sensitive
        if value_escaped is not None:
            self._values["value_escaped"] = value_escaped
        if value_has_wildcard is not None:
            self._values["value_has_wildcard"] = value_has_wildcard

    @builtins.property
    def value(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The value attributes in the incoming request to match on.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#value DataAkamaiCloudletsRequestControlMatchRule#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def value_case_sensitive(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set to true if the entries for the value property should be evaluated based on case sensitivity.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#value_case_sensitive DataAkamaiCloudletsRequestControlMatchRule#value_case_sensitive}
        '''
        result = self._values.get("value_case_sensitive")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def value_escaped(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set to true if provided value should be compared in escaped form.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#value_escaped DataAkamaiCloudletsRequestControlMatchRule#value_escaped}
        '''
        result = self._values.get("value_escaped")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def value_has_wildcard(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set to true if the entries for the value property include wildcards.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#value_has_wildcard DataAkamaiCloudletsRequestControlMatchRule#value_has_wildcard}
        '''
        result = self._values.get("value_has_wildcard")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValueOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValueOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsRequestControlMatchRule.DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValueOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__657e06d3bfbd0e2a9a672eadbf7416a3629a425c49f7eeddff0c0e283f5cef86)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @jsii.member(jsii_name="resetValueCaseSensitive")
    def reset_value_case_sensitive(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValueCaseSensitive", []))

    @jsii.member(jsii_name="resetValueEscaped")
    def reset_value_escaped(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValueEscaped", []))

    @jsii.member(jsii_name="resetValueHasWildcard")
    def reset_value_has_wildcard(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValueHasWildcard", []))

    @builtins.property
    @jsii.member(jsii_name="valueCaseSensitiveInput")
    def value_case_sensitive_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "valueCaseSensitiveInput"))

    @builtins.property
    @jsii.member(jsii_name="valueEscapedInput")
    def value_escaped_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "valueEscapedInput"))

    @builtins.property
    @jsii.member(jsii_name="valueHasWildcardInput")
    def value_has_wildcard_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "valueHasWildcardInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "value"))

    @value.setter
    def value(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c853af69236c8a488a8c15ef14ce9d3b5847c2f1aeadaf59ada79eb635a457fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="valueCaseSensitive")
    def value_case_sensitive(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "valueCaseSensitive"))

    @value_case_sensitive.setter
    def value_case_sensitive(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc5e77a999c4dde8547f995e8d247680a6c8d94457f223cab76eab0ae6353ec0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "valueCaseSensitive", value)

    @builtins.property
    @jsii.member(jsii_name="valueEscaped")
    def value_escaped(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "valueEscaped"))

    @value_escaped.setter
    def value_escaped(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7eaaa06a3a72c4add50e4fa536b8d1d3a3b4c40b001b3ac53bbac849b2610d23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "valueEscaped", value)

    @builtins.property
    @jsii.member(jsii_name="valueHasWildcard")
    def value_has_wildcard(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "valueHasWildcard"))

    @value_has_wildcard.setter
    def value_has_wildcard(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d105ae87cc83fd1029d3a89508a8041958df18d43df5f7b9a4790626fc0cc74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "valueHasWildcard", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValueOptions]:
        return typing.cast(typing.Optional[DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValueOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValueOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8635dd8ebdb8d70c352e0583306f1ee19e4850b31d3230f1f16b955caa9daf6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValueOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsRequestControlMatchRule.DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValueOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__35ffe4c6c8b299a29eb77971a68a46e9d684d479d9f3a9b2492e75c47474f28a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putOptions")
    def put_options(
        self,
        *,
        value: typing.Optional[typing.Sequence[builtins.str]] = None,
        value_case_sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        value_escaped: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        value_has_wildcard: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param value: The value attributes in the incoming request to match on. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#value DataAkamaiCloudletsRequestControlMatchRule#value}
        :param value_case_sensitive: Set to true if the entries for the value property should be evaluated based on case sensitivity. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#value_case_sensitive DataAkamaiCloudletsRequestControlMatchRule#value_case_sensitive}
        :param value_escaped: Set to true if provided value should be compared in escaped form. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#value_escaped DataAkamaiCloudletsRequestControlMatchRule#value_escaped}
        :param value_has_wildcard: Set to true if the entries for the value property include wildcards. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_request_control_match_rule#value_has_wildcard DataAkamaiCloudletsRequestControlMatchRule#value_has_wildcard}
        '''
        value_ = DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValueOptions(
            value=value,
            value_case_sensitive=value_case_sensitive,
            value_escaped=value_escaped,
            value_has_wildcard=value_has_wildcard,
        )

        return typing.cast(None, jsii.invoke(self, "putOptions", [value_]))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNameCaseSensitive")
    def reset_name_case_sensitive(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNameCaseSensitive", []))

    @jsii.member(jsii_name="resetNameHasWildcard")
    def reset_name_has_wildcard(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNameHasWildcard", []))

    @jsii.member(jsii_name="resetOptions")
    def reset_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptions", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="options")
    def options(
        self,
    ) -> DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValueOptionsOutputReference:
        return typing.cast(DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValueOptionsOutputReference, jsii.get(self, "options"))

    @builtins.property
    @jsii.member(jsii_name="nameCaseSensitiveInput")
    def name_case_sensitive_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "nameCaseSensitiveInput"))

    @builtins.property
    @jsii.member(jsii_name="nameHasWildcardInput")
    def name_has_wildcard_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "nameHasWildcardInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="optionsInput")
    def options_input(
        self,
    ) -> typing.Optional[DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValueOptions]:
        return typing.cast(typing.Optional[DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValueOptions], jsii.get(self, "optionsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fddf888eb14cfd8f3ba318ef731523925910dc2e7657165aedd8a654ab1119f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="nameCaseSensitive")
    def name_case_sensitive(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "nameCaseSensitive"))

    @name_case_sensitive.setter
    def name_case_sensitive(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12c0c6453a15acaa265a74e4854f4f77ed482e8276ce6507a9bcb16817980ba4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nameCaseSensitive", value)

    @builtins.property
    @jsii.member(jsii_name="nameHasWildcard")
    def name_has_wildcard(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "nameHasWildcard"))

    @name_has_wildcard.setter
    def name_has_wildcard(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__416da2631ce85582d3760b9f846dceae592235d0b3817208adea096819b36ca6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nameHasWildcard", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f71f2932011536c92610c79b366cf39122e68309073dab14ef1f5551ce8164f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "value"))

    @value.setter
    def value(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fd99d7d7a1c428ca597d5b93098c6761f7e958b208b2b7e438c858e8432dbbc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValue]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValue]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValue]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02dfb5c398c5b24c4eeef3ef2defa30ba7ef4a0cec86607c2419be35860cea7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsRequestControlMatchRule.DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c86e337441ec2f9ec9ad74cd198d2097dd5e383512f5490821810e8125676d0e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putObjectMatchValue")
    def put_object_match_value(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValue, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3972f64e599523b56cf889ef97fd98870eb1e93b27351e79788d7fba486b8c65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putObjectMatchValue", [value]))

    @jsii.member(jsii_name="resetCaseSensitive")
    def reset_case_sensitive(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaseSensitive", []))

    @jsii.member(jsii_name="resetCheckIps")
    def reset_check_ips(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCheckIps", []))

    @jsii.member(jsii_name="resetMatchOperator")
    def reset_match_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOperator", []))

    @jsii.member(jsii_name="resetMatchType")
    def reset_match_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchType", []))

    @jsii.member(jsii_name="resetMatchValue")
    def reset_match_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchValue", []))

    @jsii.member(jsii_name="resetNegate")
    def reset_negate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegate", []))

    @jsii.member(jsii_name="resetObjectMatchValue")
    def reset_object_match_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObjectMatchValue", []))

    @builtins.property
    @jsii.member(jsii_name="objectMatchValue")
    def object_match_value(
        self,
    ) -> DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValueList:
        return typing.cast(DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValueList, jsii.get(self, "objectMatchValue"))

    @builtins.property
    @jsii.member(jsii_name="caseSensitiveInput")
    def case_sensitive_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "caseSensitiveInput"))

    @builtins.property
    @jsii.member(jsii_name="checkIpsInput")
    def check_ips_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "checkIpsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOperatorInput")
    def match_operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "matchOperatorInput"))

    @builtins.property
    @jsii.member(jsii_name="matchTypeInput")
    def match_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "matchTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="matchValueInput")
    def match_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "matchValueInput"))

    @builtins.property
    @jsii.member(jsii_name="negateInput")
    def negate_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "negateInput"))

    @builtins.property
    @jsii.member(jsii_name="objectMatchValueInput")
    def object_match_value_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValue]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValue]]], jsii.get(self, "objectMatchValueInput"))

    @builtins.property
    @jsii.member(jsii_name="caseSensitive")
    def case_sensitive(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "caseSensitive"))

    @case_sensitive.setter
    def case_sensitive(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4af599c23f5de03d3bd115a8602ccad4913523c59fa7ba76d4669ebb14ce63ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caseSensitive", value)

    @builtins.property
    @jsii.member(jsii_name="checkIps")
    def check_ips(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "checkIps"))

    @check_ips.setter
    def check_ips(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aedd83d84afd8e7ff54f3cdb9d9eeeb242efb5a4376e449eb25e2b48ef36dbd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "checkIps", value)

    @builtins.property
    @jsii.member(jsii_name="matchOperator")
    def match_operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchOperator"))

    @match_operator.setter
    def match_operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c16b59f357aafbd88d9f6006459c9c3b38c04dec9e30ffa10f238f43ccec11f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOperator", value)

    @builtins.property
    @jsii.member(jsii_name="matchType")
    def match_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchType"))

    @match_type.setter
    def match_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec9344ad02a9f49f822d06d7a2688c191f7e89410f38b15fafc5337a93056607)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchType", value)

    @builtins.property
    @jsii.member(jsii_name="matchValue")
    def match_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchValue"))

    @match_value.setter
    def match_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84a602adf054e340bfe5084e8113918653daa4fc231e5a52a5688f34688a3f46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchValue", value)

    @builtins.property
    @jsii.member(jsii_name="negate")
    def negate(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "negate"))

    @negate.setter
    def negate(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cd4719ca0f4e9f3d5a06522b1f9fd006c03587524be91eda6d62e79d298cb26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatches]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatches]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatches]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8532e0814801f4cd8cc9bd597e519a6df366f0aa2bc9d53a753d6510c7cf55b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudletsRequestControlMatchRuleMatchRulesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsRequestControlMatchRule.DataAkamaiCloudletsRequestControlMatchRuleMatchRulesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6033576dbd0832f18dd6e11b306464f7db22067f6ecba214953b963b66d81432)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMatches")
    def put_matches(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatches, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14fa9cb8730e390264385eeafdfd8406b18b2299cc54c3bf04bde79fdafda93a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatches", [value]))

    @jsii.member(jsii_name="resetDisabled")
    def reset_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisabled", []))

    @jsii.member(jsii_name="resetEnd")
    def reset_end(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnd", []))

    @jsii.member(jsii_name="resetMatches")
    def reset_matches(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatches", []))

    @jsii.member(jsii_name="resetMatchesAlways")
    def reset_matches_always(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchesAlways", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetStart")
    def reset_start(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStart", []))

    @builtins.property
    @jsii.member(jsii_name="matches")
    def matches(
        self,
    ) -> DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesList:
        return typing.cast(DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesList, jsii.get(self, "matches"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="allowDenyInput")
    def allow_deny_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allowDenyInput"))

    @builtins.property
    @jsii.member(jsii_name="disabledInput")
    def disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disabledInput"))

    @builtins.property
    @jsii.member(jsii_name="endInput")
    def end_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "endInput"))

    @builtins.property
    @jsii.member(jsii_name="matchesAlwaysInput")
    def matches_always_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "matchesAlwaysInput"))

    @builtins.property
    @jsii.member(jsii_name="matchesInput")
    def matches_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatches]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatches]]], jsii.get(self, "matchesInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="startInput")
    def start_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "startInput"))

    @builtins.property
    @jsii.member(jsii_name="allowDeny")
    def allow_deny(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "allowDeny"))

    @allow_deny.setter
    def allow_deny(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__564b806c268774a1242ec978c7dd7fe916501762a981e9c514dfa1d61f5959f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowDeny", value)

    @builtins.property
    @jsii.member(jsii_name="disabled")
    def disabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disabled"))

    @disabled.setter
    def disabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd798f21013681334b97e2b33550d4c22faf063753d87e891a607de3ab75d2ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabled", value)

    @builtins.property
    @jsii.member(jsii_name="end")
    def end(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "end"))

    @end.setter
    def end(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a1ed9fbe8586ee32464b8e86891ca5827370e76f175d8ac1fd143ed0a6e5c48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "end", value)

    @builtins.property
    @jsii.member(jsii_name="matchesAlways")
    def matches_always(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "matchesAlways"))

    @matches_always.setter
    def matches_always(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe5bd9d4066e4fd1874d0caabdbc8d5a41b91d3e1538bf3372891eef48fa3014)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchesAlways", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4e306a640bec3e06a59c3236228324a69eaecff6eeb2cac9e38e437891bfced)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="start")
    def start(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "start"))

    @start.setter
    def start(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d756aa08a148695b449d6f4a19d7cc0ac27ff42f4f85074044fb0a700431cb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "start", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsRequestControlMatchRuleMatchRules]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsRequestControlMatchRuleMatchRules]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsRequestControlMatchRuleMatchRules]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c508beab4ce8df4d70e0ff0816a84443418c6aad8759cabc0b0f4dd89352e13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataAkamaiCloudletsRequestControlMatchRule",
    "DataAkamaiCloudletsRequestControlMatchRuleConfig",
    "DataAkamaiCloudletsRequestControlMatchRuleMatchRules",
    "DataAkamaiCloudletsRequestControlMatchRuleMatchRulesList",
    "DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatches",
    "DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesList",
    "DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValue",
    "DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValueList",
    "DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValueOptions",
    "DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValueOptionsOutputReference",
    "DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValueOutputReference",
    "DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesOutputReference",
    "DataAkamaiCloudletsRequestControlMatchRuleMatchRulesOutputReference",
]

publication.publish()

def _typecheckingstub__e23b597445057b7b50212416e592c49af5b64295e4c8f7c2caa82580fb935f57(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    id: typing.Optional[builtins.str] = None,
    match_rules: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsRequestControlMatchRuleMatchRules, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__327a6775f32dfe56e7455d623fd567b144c47234ec6c6e21d55b7cb8e44e7ecd(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee74d898c532ab5e907666fc2126d71f29e8c3fed8c24dada5550f063af57a36(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsRequestControlMatchRuleMatchRules, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__883973703e6deb7fa1ae75aca78f35c489a7321d11f5be2e5eb6812718c2d5b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2339e9c008917c5ca5a708d09d04a2b14414fcf18260025b2f1f56f5eea424e0(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    match_rules: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsRequestControlMatchRuleMatchRules, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97f59f17895bf0b3e6eb340f22f36c89c5e31bfb55dccd8062d3d6d3139e2b0d(
    *,
    allow_deny: builtins.str,
    disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    end: typing.Optional[jsii.Number] = None,
    matches: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatches, typing.Dict[builtins.str, typing.Any]]]]] = None,
    matches_always: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    name: typing.Optional[builtins.str] = None,
    start: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcbf41856fbf451590b81c59b343d6516bc11e8d6bfe2b6fea9213875a88b0c0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7551fd8357f83045b493700599741e4cb20382c3aaa5acfe5ce61f7da2ccfa5(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5154183626ecfdb47be61f581fa90718136257cd22482f4fadaa0255ae068bf1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51cc31782b07f394df6d59a3493d837fca0191d2216f55ec5cc4f3d544f2ebe2(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7da616d6025561e7f8f31b90c6cebc7dfd4a52ee498a3e48e30a3bc51945ac75(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__649bcd13eac4c6aa3385e16990acee3c05b0696de42096334abf5c0066db900e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsRequestControlMatchRuleMatchRules]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f387bd4ed5cf82c767258c296f7078eeba0310554380cdc70bd7c2cb2ffebb0(
    *,
    case_sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    check_ips: typing.Optional[builtins.str] = None,
    match_operator: typing.Optional[builtins.str] = None,
    match_type: typing.Optional[builtins.str] = None,
    match_value: typing.Optional[builtins.str] = None,
    negate: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    object_match_value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValue, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60e16e1cbf69f073b2e596220ad952bb5fc1301406f275e0e56c139e7243e3e4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__931ce7fd9dc1f93dfa0be7736b4ecac462ee61ed4554fcfb7af64616b289e217(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3999a79f88792149a92071dfa1eab068174ce1b2f1b08c2c0df47e2b16ae1ef3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1ec2d60c40a3b20a4169c6d298a010173efe7ed044bef2b7d29da5ba5d6ad30(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcbb0eb59ad19f02fc656e69e58a07512d41ff7031842cba3f5554ad0b17e5a0(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1eb1558c7967ba18a515f76bd93d2303d902f3d8244e4df633457078ba0ee200(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatches]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aced90d6a9e32373d8d18f6595f35ba52027fb037e862b23afca003a5eefac19(
    *,
    type: builtins.str,
    name: typing.Optional[builtins.str] = None,
    name_case_sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    name_has_wildcard: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    options: typing.Optional[typing.Union[DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValueOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    value: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2303631b758bae0014c605b4d9a0f3bf6304745c3c6a9b2bca9be521704a4c2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d485260c6a3ef825d330d5fb2d494e271059ba58bd9dfad81d69626eac7932d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d119735be1b47ff19bcc2b231a473ab74f60c46a491b7fc4e05775f8bcbf35c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e4c9f3091a4f3a03e4c6ae7536a2731bf354f713608e48d75689b3fe72b6e3f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__944d3e4802dd9c3d23ef4a75404e853aa7a4f7c525533e906ba9c1f4f403f9b1(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a3e7e037f462a30fa640f857e2879fc5933e29e8903c4c6c5d735edc387f42e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValue]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e0f6ce5d2cfe854aa0957814d7068bb6e9a8ba6759de6109a591c139dc4fcc1(
    *,
    value: typing.Optional[typing.Sequence[builtins.str]] = None,
    value_case_sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    value_escaped: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    value_has_wildcard: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__657e06d3bfbd0e2a9a672eadbf7416a3629a425c49f7eeddff0c0e283f5cef86(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c853af69236c8a488a8c15ef14ce9d3b5847c2f1aeadaf59ada79eb635a457fc(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc5e77a999c4dde8547f995e8d247680a6c8d94457f223cab76eab0ae6353ec0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7eaaa06a3a72c4add50e4fa536b8d1d3a3b4c40b001b3ac53bbac849b2610d23(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d105ae87cc83fd1029d3a89508a8041958df18d43df5f7b9a4790626fc0cc74(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8635dd8ebdb8d70c352e0583306f1ee19e4850b31d3230f1f16b955caa9daf6(
    value: typing.Optional[DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValueOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35ffe4c6c8b299a29eb77971a68a46e9d684d479d9f3a9b2492e75c47474f28a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fddf888eb14cfd8f3ba318ef731523925910dc2e7657165aedd8a654ab1119f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12c0c6453a15acaa265a74e4854f4f77ed482e8276ce6507a9bcb16817980ba4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__416da2631ce85582d3760b9f846dceae592235d0b3817208adea096819b36ca6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f71f2932011536c92610c79b366cf39122e68309073dab14ef1f5551ce8164f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fd99d7d7a1c428ca597d5b93098c6761f7e958b208b2b7e438c858e8432dbbc(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02dfb5c398c5b24c4eeef3ef2defa30ba7ef4a0cec86607c2419be35860cea7d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValue]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c86e337441ec2f9ec9ad74cd198d2097dd5e383512f5490821810e8125676d0e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3972f64e599523b56cf889ef97fd98870eb1e93b27351e79788d7fba486b8c65(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatchesObjectMatchValue, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4af599c23f5de03d3bd115a8602ccad4913523c59fa7ba76d4669ebb14ce63ae(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aedd83d84afd8e7ff54f3cdb9d9eeeb242efb5a4376e449eb25e2b48ef36dbd6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c16b59f357aafbd88d9f6006459c9c3b38c04dec9e30ffa10f238f43ccec11f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec9344ad02a9f49f822d06d7a2688c191f7e89410f38b15fafc5337a93056607(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84a602adf054e340bfe5084e8113918653daa4fc231e5a52a5688f34688a3f46(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cd4719ca0f4e9f3d5a06522b1f9fd006c03587524be91eda6d62e79d298cb26(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8532e0814801f4cd8cc9bd597e519a6df366f0aa2bc9d53a753d6510c7cf55b6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatches]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6033576dbd0832f18dd6e11b306464f7db22067f6ecba214953b963b66d81432(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14fa9cb8730e390264385eeafdfd8406b18b2299cc54c3bf04bde79fdafda93a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsRequestControlMatchRuleMatchRulesMatches, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__564b806c268774a1242ec978c7dd7fe916501762a981e9c514dfa1d61f5959f0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd798f21013681334b97e2b33550d4c22faf063753d87e891a607de3ab75d2ee(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a1ed9fbe8586ee32464b8e86891ca5827370e76f175d8ac1fd143ed0a6e5c48(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe5bd9d4066e4fd1874d0caabdbc8d5a41b91d3e1538bf3372891eef48fa3014(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4e306a640bec3e06a59c3236228324a69eaecff6eeb2cac9e38e437891bfced(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d756aa08a148695b449d6f4a19d7cc0ac27ff42f4f85074044fb0a700431cb5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c508beab4ce8df4d70e0ff0816a84443418c6aad8759cabc0b0f4dd89352e13(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsRequestControlMatchRuleMatchRules]],
) -> None:
    """Type checking stubs"""
    pass
