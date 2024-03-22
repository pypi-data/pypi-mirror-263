'''
# `data_akamai_cloudlets_forward_rewrite_match_rule`

Refer to the Terraform Registry for docs: [`data_akamai_cloudlets_forward_rewrite_match_rule`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule).
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


class DataAkamaiCloudletsForwardRewriteMatchRule(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsForwardRewriteMatchRule.DataAkamaiCloudletsForwardRewriteMatchRule",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule akamai_cloudlets_forward_rewrite_match_rule}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        id: typing.Optional[builtins.str] = None,
        match_rules: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudletsForwardRewriteMatchRuleMatchRules", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule akamai_cloudlets_forward_rewrite_match_rule} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#id DataAkamaiCloudletsForwardRewriteMatchRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param match_rules: match_rules block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#match_rules DataAkamaiCloudletsForwardRewriteMatchRule#match_rules}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f9841ce1c0edd9fb17a2cbd0341dade6387ccbc7020cf66cdb78b53a8d0f4d0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAkamaiCloudletsForwardRewriteMatchRuleConfig(
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
        '''Generates CDKTF code for importing a DataAkamaiCloudletsForwardRewriteMatchRule resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the DataAkamaiCloudletsForwardRewriteMatchRule to import.
        :param import_from_id: The id of the existing DataAkamaiCloudletsForwardRewriteMatchRule that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the DataAkamaiCloudletsForwardRewriteMatchRule to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__591d89211afc13973e75930f90ee9cda2ce88cebdf575a368562aa357726c65a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putMatchRules")
    def put_match_rules(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudletsForwardRewriteMatchRuleMatchRules", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2405c80b485fe06c0a5908ea6a8562b66683f4480b4556cde2665f8470ca1b6a)
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
    def match_rules(self) -> "DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesList":
        return typing.cast("DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesList", jsii.get(self, "matchRules"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="matchRulesInput")
    def match_rules_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsForwardRewriteMatchRuleMatchRules"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsForwardRewriteMatchRuleMatchRules"]]], jsii.get(self, "matchRulesInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2151acd73a87efe6eda444ef9ae55af0487e6465d7ba3b762f48724d50d46db9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsForwardRewriteMatchRule.DataAkamaiCloudletsForwardRewriteMatchRuleConfig",
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
class DataAkamaiCloudletsForwardRewriteMatchRuleConfig(
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
        match_rules: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudletsForwardRewriteMatchRuleMatchRules", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#id DataAkamaiCloudletsForwardRewriteMatchRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param match_rules: match_rules block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#match_rules DataAkamaiCloudletsForwardRewriteMatchRule#match_rules}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee10ea8f3a2a5a425f5b8210763b2f01f1dc6707821602db3b5630cf43ec7d1c)
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
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#id DataAkamaiCloudletsForwardRewriteMatchRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_rules(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsForwardRewriteMatchRuleMatchRules"]]]:
        '''match_rules block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#match_rules DataAkamaiCloudletsForwardRewriteMatchRule#match_rules}
        '''
        result = self._values.get("match_rules")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsForwardRewriteMatchRuleMatchRules"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsForwardRewriteMatchRuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsForwardRewriteMatchRule.DataAkamaiCloudletsForwardRewriteMatchRuleMatchRules",
    jsii_struct_bases=[],
    name_mapping={
        "forward_settings": "forwardSettings",
        "disabled": "disabled",
        "end": "end",
        "matches": "matches",
        "match_url": "matchUrl",
        "name": "name",
        "start": "start",
    },
)
class DataAkamaiCloudletsForwardRewriteMatchRuleMatchRules:
    def __init__(
        self,
        *,
        forward_settings: typing.Union["DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesForwardSettings", typing.Dict[builtins.str, typing.Any]],
        disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        end: typing.Optional[jsii.Number] = None,
        matches: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatches", typing.Dict[builtins.str, typing.Any]]]]] = None,
        match_url: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        start: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param forward_settings: forward_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#forward_settings DataAkamaiCloudletsForwardRewriteMatchRule#forward_settings}
        :param disabled: If set to true, disables a rule so it is not evaluated against incoming requests. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#disabled DataAkamaiCloudletsForwardRewriteMatchRule#disabled}
        :param end: The end time for this match (in seconds since the epoch). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#end DataAkamaiCloudletsForwardRewriteMatchRule#end}
        :param matches: matches block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#matches DataAkamaiCloudletsForwardRewriteMatchRule#matches}
        :param match_url: If using a URL match, this property is the URL that the Cloudlet uses to match the incoming request. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#match_url DataAkamaiCloudletsForwardRewriteMatchRule#match_url}
        :param name: The name of the rule. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#name DataAkamaiCloudletsForwardRewriteMatchRule#name}
        :param start: The start time for this match (in seconds since the epoch). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#start DataAkamaiCloudletsForwardRewriteMatchRule#start}
        '''
        if isinstance(forward_settings, dict):
            forward_settings = DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesForwardSettings(**forward_settings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b754f394489b2e8d855b4a9d5b1435b429983d2c85740226446c66ad2c707f47)
            check_type(argname="argument forward_settings", value=forward_settings, expected_type=type_hints["forward_settings"])
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
            check_type(argname="argument end", value=end, expected_type=type_hints["end"])
            check_type(argname="argument matches", value=matches, expected_type=type_hints["matches"])
            check_type(argname="argument match_url", value=match_url, expected_type=type_hints["match_url"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument start", value=start, expected_type=type_hints["start"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "forward_settings": forward_settings,
        }
        if disabled is not None:
            self._values["disabled"] = disabled
        if end is not None:
            self._values["end"] = end
        if matches is not None:
            self._values["matches"] = matches
        if match_url is not None:
            self._values["match_url"] = match_url
        if name is not None:
            self._values["name"] = name
        if start is not None:
            self._values["start"] = start

    @builtins.property
    def forward_settings(
        self,
    ) -> "DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesForwardSettings":
        '''forward_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#forward_settings DataAkamaiCloudletsForwardRewriteMatchRule#forward_settings}
        '''
        result = self._values.get("forward_settings")
        assert result is not None, "Required property 'forward_settings' is missing"
        return typing.cast("DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesForwardSettings", result)

    @builtins.property
    def disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If set to true, disables a rule so it is not evaluated against incoming requests.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#disabled DataAkamaiCloudletsForwardRewriteMatchRule#disabled}
        '''
        result = self._values.get("disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def end(self) -> typing.Optional[jsii.Number]:
        '''The end time for this match (in seconds since the epoch).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#end DataAkamaiCloudletsForwardRewriteMatchRule#end}
        '''
        result = self._values.get("end")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def matches(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatches"]]]:
        '''matches block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#matches DataAkamaiCloudletsForwardRewriteMatchRule#matches}
        '''
        result = self._values.get("matches")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatches"]]], result)

    @builtins.property
    def match_url(self) -> typing.Optional[builtins.str]:
        '''If using a URL match, this property is the URL that the Cloudlet uses to match the incoming request.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#match_url DataAkamaiCloudletsForwardRewriteMatchRule#match_url}
        '''
        result = self._values.get("match_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the rule.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#name DataAkamaiCloudletsForwardRewriteMatchRule#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start(self) -> typing.Optional[jsii.Number]:
        '''The start time for this match (in seconds since the epoch).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#start DataAkamaiCloudletsForwardRewriteMatchRule#start}
        '''
        result = self._values.get("start")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsForwardRewriteMatchRuleMatchRules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsForwardRewriteMatchRule.DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesForwardSettings",
    jsii_struct_bases=[],
    name_mapping={
        "origin_id": "originId",
        "path_and_qs": "pathAndQs",
        "use_incoming_query_string": "useIncomingQueryString",
    },
)
class DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesForwardSettings:
    def __init__(
        self,
        *,
        origin_id: typing.Optional[builtins.str] = None,
        path_and_qs: typing.Optional[builtins.str] = None,
        use_incoming_query_string: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param origin_id: The ID of the Conditional Origin requests are forwarded to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#origin_id DataAkamaiCloudletsForwardRewriteMatchRule#origin_id}
        :param path_and_qs: If a value is provided and match conditions are met, this property defines the path/resource/query string to rewrite URL for the incoming request. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#path_and_qs DataAkamaiCloudletsForwardRewriteMatchRule#path_and_qs}
        :param use_incoming_query_string: If set to true, the Cloudlet includes the query string from the request in the rewritten or forwarded URL. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#use_incoming_query_string DataAkamaiCloudletsForwardRewriteMatchRule#use_incoming_query_string}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06e59514dbbb143905aaedd3cd3e7ec3d84a38e418ce4985c361d12806730ec7)
            check_type(argname="argument origin_id", value=origin_id, expected_type=type_hints["origin_id"])
            check_type(argname="argument path_and_qs", value=path_and_qs, expected_type=type_hints["path_and_qs"])
            check_type(argname="argument use_incoming_query_string", value=use_incoming_query_string, expected_type=type_hints["use_incoming_query_string"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if origin_id is not None:
            self._values["origin_id"] = origin_id
        if path_and_qs is not None:
            self._values["path_and_qs"] = path_and_qs
        if use_incoming_query_string is not None:
            self._values["use_incoming_query_string"] = use_incoming_query_string

    @builtins.property
    def origin_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the Conditional Origin requests are forwarded to.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#origin_id DataAkamaiCloudletsForwardRewriteMatchRule#origin_id}
        '''
        result = self._values.get("origin_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path_and_qs(self) -> typing.Optional[builtins.str]:
        '''If a value is provided and match conditions are met, this property defines the path/resource/query string to rewrite URL for the incoming request.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#path_and_qs DataAkamaiCloudletsForwardRewriteMatchRule#path_and_qs}
        '''
        result = self._values.get("path_and_qs")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_incoming_query_string(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If set to true, the Cloudlet includes the query string from the request in the rewritten or forwarded URL.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#use_incoming_query_string DataAkamaiCloudletsForwardRewriteMatchRule#use_incoming_query_string}
        '''
        result = self._values.get("use_incoming_query_string")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesForwardSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesForwardSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsForwardRewriteMatchRule.DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesForwardSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__30f7532f997986877abd6bfd60e802c366f130ad53fca0dc9c9d303afcf10f93)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetOriginId")
    def reset_origin_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOriginId", []))

    @jsii.member(jsii_name="resetPathAndQs")
    def reset_path_and_qs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPathAndQs", []))

    @jsii.member(jsii_name="resetUseIncomingQueryString")
    def reset_use_incoming_query_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseIncomingQueryString", []))

    @builtins.property
    @jsii.member(jsii_name="originIdInput")
    def origin_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "originIdInput"))

    @builtins.property
    @jsii.member(jsii_name="pathAndQsInput")
    def path_and_qs_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathAndQsInput"))

    @builtins.property
    @jsii.member(jsii_name="useIncomingQueryStringInput")
    def use_incoming_query_string_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "useIncomingQueryStringInput"))

    @builtins.property
    @jsii.member(jsii_name="originId")
    def origin_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "originId"))

    @origin_id.setter
    def origin_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4bd12f4faec4c6bd4e2d94708258f1aeb389f1319a95e19d553870f2a1792c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originId", value)

    @builtins.property
    @jsii.member(jsii_name="pathAndQs")
    def path_and_qs(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pathAndQs"))

    @path_and_qs.setter
    def path_and_qs(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa6a6b93aae680fe88a975416365a46380024757bb67dfa7ca6045cb4bed5d27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pathAndQs", value)

    @builtins.property
    @jsii.member(jsii_name="useIncomingQueryString")
    def use_incoming_query_string(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "useIncomingQueryString"))

    @use_incoming_query_string.setter
    def use_incoming_query_string(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74bc8cd4990d46963e9b52861e691064ed72fe49e3ecd0abaaa49f0f95c6e0b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useIncomingQueryString", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesForwardSettings]:
        return typing.cast(typing.Optional[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesForwardSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesForwardSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a2e4a9061aa004ef2309315b221d4baa35520f545fa9623123575c75327a6f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsForwardRewriteMatchRule.DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__56da81bb9e87e68e8e3154044fe496b54da036481a4a6558cf7958eecb445011)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__caade0bf67c0b29f9e8be6b067289fc4255c3ec9c29c599b4713416951771e7a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2d916838a1136507c9d72c19ce4c54c6c672351d0eaab3200d0346cea2f48b9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0e7b4fd17e43f7713e0eae974dcc95360ab9b45819df1cac6fce9aa17285e4c2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__adec8806f83cd132c9c973f636f6edd8df755105c869a038146292ad6401b9b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRules]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRules]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRules]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2161840ba7b0e871f64b438c2321538b74c62e3915cc0ad9fa50d938c06cee1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsForwardRewriteMatchRule.DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatches",
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
class DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatches:
    def __init__(
        self,
        *,
        case_sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        check_ips: typing.Optional[builtins.str] = None,
        match_operator: typing.Optional[builtins.str] = None,
        match_type: typing.Optional[builtins.str] = None,
        match_value: typing.Optional[builtins.str] = None,
        negate: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        object_match_value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValue", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param case_sensitive: If true, the match is case sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#case_sensitive DataAkamaiCloudletsForwardRewriteMatchRule#case_sensitive}
        :param check_ips: For clientip, continent, countrycode, proxy, and regioncode match types, the part of the request that determines the IP address to use. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#check_ips DataAkamaiCloudletsForwardRewriteMatchRule#check_ips}
        :param match_operator: Valid entries for this property: contains, exists, and equals. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#match_operator DataAkamaiCloudletsForwardRewriteMatchRule#match_operator}
        :param match_type: The type of match used. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#match_type DataAkamaiCloudletsForwardRewriteMatchRule#match_type}
        :param match_value: Depends on the matchType. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#match_value DataAkamaiCloudletsForwardRewriteMatchRule#match_value}
        :param negate: If true, negates the match. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#negate DataAkamaiCloudletsForwardRewriteMatchRule#negate}
        :param object_match_value: object_match_value block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#object_match_value DataAkamaiCloudletsForwardRewriteMatchRule#object_match_value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80b2e319681b52bc0e5825e43d499852d7da27f84f5fa535f7b65aa1e065c574)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#case_sensitive DataAkamaiCloudletsForwardRewriteMatchRule#case_sensitive}
        '''
        result = self._values.get("case_sensitive")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def check_ips(self) -> typing.Optional[builtins.str]:
        '''For clientip, continent, countrycode, proxy, and regioncode match types, the part of the request that determines the IP address to use.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#check_ips DataAkamaiCloudletsForwardRewriteMatchRule#check_ips}
        '''
        result = self._values.get("check_ips")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_operator(self) -> typing.Optional[builtins.str]:
        '''Valid entries for this property: contains, exists, and equals.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#match_operator DataAkamaiCloudletsForwardRewriteMatchRule#match_operator}
        '''
        result = self._values.get("match_operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_type(self) -> typing.Optional[builtins.str]:
        '''The type of match used.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#match_type DataAkamaiCloudletsForwardRewriteMatchRule#match_type}
        '''
        result = self._values.get("match_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_value(self) -> typing.Optional[builtins.str]:
        '''Depends on the matchType.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#match_value DataAkamaiCloudletsForwardRewriteMatchRule#match_value}
        '''
        result = self._values.get("match_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def negate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If true, negates the match.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#negate DataAkamaiCloudletsForwardRewriteMatchRule#negate}
        '''
        result = self._values.get("negate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def object_match_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValue"]]]:
        '''object_match_value block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#object_match_value DataAkamaiCloudletsForwardRewriteMatchRule#object_match_value}
        '''
        result = self._values.get("object_match_value")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValue"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatches(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsForwardRewriteMatchRule.DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__29e00427c294c8e07aa5f996fb8d5f287473fc4d86790c5bd66457be8538d199)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9dcc40d99c268f9c255f8dda9adaadcdde2ecee3688a7878bf0a48b0594e7ed8)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fcdefea05d59232fcae24792a780c5dc2c6044e2c13af1c8b9ba64f56d4ffbf)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b35194d93c7653bbd7d99cb8c395cee0b09a1eccefa11790bcd4b6a7842d31df)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e02e451669e1290bac22e1f37b7a55967e1cd81e21562cf8000270cb8b420a65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatches]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatches]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatches]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f038e2eef3ce97a60143d62868f54e5543e61a73996df646c361265efd4cda2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsForwardRewriteMatchRule.DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValue",
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
class DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValue:
    def __init__(
        self,
        *,
        type: builtins.str,
        name: typing.Optional[builtins.str] = None,
        name_case_sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        name_has_wildcard: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        options: typing.Optional[typing.Union["DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValueOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        value: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: The array type, which can be one of the following: object or simple. Use the simple option when adding only an array of string-based values Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#type DataAkamaiCloudletsForwardRewriteMatchRule#type}
        :param name: If using a match type that supports name attributes, enter the value in the incoming request to match on. The following match types support this property: cookie, header, parameter, and query Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#name DataAkamaiCloudletsForwardRewriteMatchRule#name}
        :param name_case_sensitive: Set to true if the entry for the name property should be evaluated based on case sensitivity. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#name_case_sensitive DataAkamaiCloudletsForwardRewriteMatchRule#name_case_sensitive}
        :param name_has_wildcard: Set to true if the entry for the name property includes wildcards. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#name_has_wildcard DataAkamaiCloudletsForwardRewriteMatchRule#name_has_wildcard}
        :param options: options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#options DataAkamaiCloudletsForwardRewriteMatchRule#options}
        :param value: The value attributes in the incoming request to match on (use only with simple or range type). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#value DataAkamaiCloudletsForwardRewriteMatchRule#value}
        '''
        if isinstance(options, dict):
            options = DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValueOptions(**options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e67a8d3af6e4a47ee38e53cd92bad435b665ec01408f30dabd83d771c8614f11)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#type DataAkamaiCloudletsForwardRewriteMatchRule#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''If using a match type that supports name attributes, enter the value in the incoming request to match on.

        The following match types support this property: cookie, header, parameter, and query

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#name DataAkamaiCloudletsForwardRewriteMatchRule#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name_case_sensitive(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set to true if the entry for the name property should be evaluated based on case sensitivity.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#name_case_sensitive DataAkamaiCloudletsForwardRewriteMatchRule#name_case_sensitive}
        '''
        result = self._values.get("name_case_sensitive")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def name_has_wildcard(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set to true if the entry for the name property includes wildcards.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#name_has_wildcard DataAkamaiCloudletsForwardRewriteMatchRule#name_has_wildcard}
        '''
        result = self._values.get("name_has_wildcard")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def options(
        self,
    ) -> typing.Optional["DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValueOptions"]:
        '''options block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#options DataAkamaiCloudletsForwardRewriteMatchRule#options}
        '''
        result = self._values.get("options")
        return typing.cast(typing.Optional["DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValueOptions"], result)

    @builtins.property
    def value(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The value attributes in the incoming request to match on (use only with simple or range type).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#value DataAkamaiCloudletsForwardRewriteMatchRule#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValueList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsForwardRewriteMatchRule.DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValueList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__49b64bbdae8ff80622583d354bec80c3597b3a8510d14bb4e64882232aa9c5ac)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValueOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53423fc12e0cbf27f717cf556b1a7a2106f7f871824e76e2b5a3dee6075a4334)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValueOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c4663b407b88ea5be7ee8d6348e89738372fcbee60b49c2695e69e766883e6a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__51110a4cf5668b9343692daa8017111f814494c7019a6f58f2e88433daddfc7e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__35ba39ef005a0bb9748df84c0e7765bda86959400f4b4902b0ba6dd9058dcd42)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValue]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValue]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValue]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__978e1281d1637f239822883b5a130550896c58400e8fe9371a7eb45cadadb18c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsForwardRewriteMatchRule.DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValueOptions",
    jsii_struct_bases=[],
    name_mapping={
        "value": "value",
        "value_case_sensitive": "valueCaseSensitive",
        "value_escaped": "valueEscaped",
        "value_has_wildcard": "valueHasWildcard",
    },
)
class DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValueOptions:
    def __init__(
        self,
        *,
        value: typing.Optional[typing.Sequence[builtins.str]] = None,
        value_case_sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        value_escaped: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        value_has_wildcard: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param value: The value attributes in the incoming request to match on. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#value DataAkamaiCloudletsForwardRewriteMatchRule#value}
        :param value_case_sensitive: Set to true if the entries for the value property should be evaluated based on case sensitivity. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#value_case_sensitive DataAkamaiCloudletsForwardRewriteMatchRule#value_case_sensitive}
        :param value_escaped: Set to true if provided value should be compared in escaped form. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#value_escaped DataAkamaiCloudletsForwardRewriteMatchRule#value_escaped}
        :param value_has_wildcard: Set to true if the entries for the value property include wildcards. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#value_has_wildcard DataAkamaiCloudletsForwardRewriteMatchRule#value_has_wildcard}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37b81cdbb0893588bffa6bdc66f6e93b4ecdc4140d60052214082dc9aaad15a7)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#value DataAkamaiCloudletsForwardRewriteMatchRule#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def value_case_sensitive(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set to true if the entries for the value property should be evaluated based on case sensitivity.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#value_case_sensitive DataAkamaiCloudletsForwardRewriteMatchRule#value_case_sensitive}
        '''
        result = self._values.get("value_case_sensitive")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def value_escaped(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set to true if provided value should be compared in escaped form.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#value_escaped DataAkamaiCloudletsForwardRewriteMatchRule#value_escaped}
        '''
        result = self._values.get("value_escaped")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def value_has_wildcard(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set to true if the entries for the value property include wildcards.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#value_has_wildcard DataAkamaiCloudletsForwardRewriteMatchRule#value_has_wildcard}
        '''
        result = self._values.get("value_has_wildcard")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValueOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValueOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsForwardRewriteMatchRule.DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValueOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bfa808504a474ab6955b79e53cc11fb2dd9844ae52a7e86d00cc6fcfc0149748)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6911010ed66553dbbf08c37578a7bf725a27e61784f6b0b032a425d2b90b6fe2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5f8999352c3284540e7b66c96419acada17bb3dabc4ca8b54653a2ac03b98f25)
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
            type_hints = typing.get_type_hints(_typecheckingstub__161dc3879a00407726ca8f84014fd766fee8f8764c722b1aca62c0f3f338e44f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a70ace2ec893109bf63b23b58b441f5906d58597c2e7c028052d13a14ed2b9a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "valueHasWildcard", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValueOptions]:
        return typing.cast(typing.Optional[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValueOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValueOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab5f2a3426910a9e44ff256f0d8997f4317c93a0546f34215415b4f50fcce43a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValueOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsForwardRewriteMatchRule.DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValueOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__193568b15ccdb54a0f097b90758eab3ce7106deea8ecfae220f7df6b8a2f6237)
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
        :param value: The value attributes in the incoming request to match on. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#value DataAkamaiCloudletsForwardRewriteMatchRule#value}
        :param value_case_sensitive: Set to true if the entries for the value property should be evaluated based on case sensitivity. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#value_case_sensitive DataAkamaiCloudletsForwardRewriteMatchRule#value_case_sensitive}
        :param value_escaped: Set to true if provided value should be compared in escaped form. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#value_escaped DataAkamaiCloudletsForwardRewriteMatchRule#value_escaped}
        :param value_has_wildcard: Set to true if the entries for the value property include wildcards. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#value_has_wildcard DataAkamaiCloudletsForwardRewriteMatchRule#value_has_wildcard}
        '''
        value_ = DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValueOptions(
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
    ) -> DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValueOptionsOutputReference:
        return typing.cast(DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValueOptionsOutputReference, jsii.get(self, "options"))

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
    ) -> typing.Optional[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValueOptions]:
        return typing.cast(typing.Optional[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValueOptions], jsii.get(self, "optionsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__03bbc08cad82be5b2d993f3ac94f10fa37e725f64c6b29c7b8c49454f2e026d3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5761b7e390360d3c0ceda2cf00bc0c6f20fdcebbae6296d4dc010b580604c10c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9846d204cb554a692a8688306ca36a844bad6e17fb601b4d40dd31fea7b32e98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nameHasWildcard", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34b20c51933c2aa4e622566d582ba1aa6d0d3d060138ecc304995bb87f3e8076)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "value"))

    @value.setter
    def value(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c25cb7db3f7b90f93da6b3ebf89dcfe8fcb6fc0836ba202946c250d470aea8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValue]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValue]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValue]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__480036fe32c3e24afbc83087418d82c71ea01820adb82be670a5e54ccdae681d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsForwardRewriteMatchRule.DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6fa9c4a250c133fdca87e9463a9619a4693db52c8115f30a91813ad0246b7e59)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putObjectMatchValue")
    def put_object_match_value(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValue, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5582182d01dd433f6b5ff9f1e253cfb96867d74b413eaf844305095a61e7b446)
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
    ) -> DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValueList:
        return typing.cast(DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValueList, jsii.get(self, "objectMatchValue"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValue]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValue]]], jsii.get(self, "objectMatchValueInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__5018acee884618e0ab959cd44b957a42b48267ed89fa73dfcff97d4cccfd6473)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caseSensitive", value)

    @builtins.property
    @jsii.member(jsii_name="checkIps")
    def check_ips(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "checkIps"))

    @check_ips.setter
    def check_ips(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fea46591be8d77b51a0be74fdd7aa1ac904eb10f68e21beab50d7084d423b73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "checkIps", value)

    @builtins.property
    @jsii.member(jsii_name="matchOperator")
    def match_operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchOperator"))

    @match_operator.setter
    def match_operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b27748b765115b62f7eab300c67151228a298363d5b397ac365d8144469f3256)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOperator", value)

    @builtins.property
    @jsii.member(jsii_name="matchType")
    def match_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchType"))

    @match_type.setter
    def match_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79e4d683ce7d2bf9a921ad80de99aa8c5b5406f1b37951ed27ac336b87601c2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchType", value)

    @builtins.property
    @jsii.member(jsii_name="matchValue")
    def match_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchValue"))

    @match_value.setter
    def match_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e7bd110bfe6f520a338e0a99c8523ca2ef3874867c3a11e98d67723152e9add)
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
            type_hints = typing.get_type_hints(_typecheckingstub__509225cc8669c0b7bab97be5adbc93370b910d943286f1784ae359fddf4f514e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatches]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatches]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatches]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad33ca873cf1d77c44ebd5d2df32f5b32d5694e1f3a874355507ebc590cf90c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsForwardRewriteMatchRule.DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2e9d93648c7b4e9ffd9eddf434bca05bd858ad6e5f6a79113467c75d3d9e7fce)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putForwardSettings")
    def put_forward_settings(
        self,
        *,
        origin_id: typing.Optional[builtins.str] = None,
        path_and_qs: typing.Optional[builtins.str] = None,
        use_incoming_query_string: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param origin_id: The ID of the Conditional Origin requests are forwarded to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#origin_id DataAkamaiCloudletsForwardRewriteMatchRule#origin_id}
        :param path_and_qs: If a value is provided and match conditions are met, this property defines the path/resource/query string to rewrite URL for the incoming request. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#path_and_qs DataAkamaiCloudletsForwardRewriteMatchRule#path_and_qs}
        :param use_incoming_query_string: If set to true, the Cloudlet includes the query string from the request in the rewritten or forwarded URL. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_forward_rewrite_match_rule#use_incoming_query_string DataAkamaiCloudletsForwardRewriteMatchRule#use_incoming_query_string}
        '''
        value = DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesForwardSettings(
            origin_id=origin_id,
            path_and_qs=path_and_qs,
            use_incoming_query_string=use_incoming_query_string,
        )

        return typing.cast(None, jsii.invoke(self, "putForwardSettings", [value]))

    @jsii.member(jsii_name="putMatches")
    def put_matches(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatches, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__572e67d472a4706ef904b8caf72582f34211077862b8f0cf9e9f35b9be23e3db)
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

    @jsii.member(jsii_name="resetMatchUrl")
    def reset_match_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchUrl", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetStart")
    def reset_start(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStart", []))

    @builtins.property
    @jsii.member(jsii_name="forwardSettings")
    def forward_settings(
        self,
    ) -> DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesForwardSettingsOutputReference:
        return typing.cast(DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesForwardSettingsOutputReference, jsii.get(self, "forwardSettings"))

    @builtins.property
    @jsii.member(jsii_name="matches")
    def matches(
        self,
    ) -> DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesList:
        return typing.cast(DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesList, jsii.get(self, "matches"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

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
    @jsii.member(jsii_name="forwardSettingsInput")
    def forward_settings_input(
        self,
    ) -> typing.Optional[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesForwardSettings]:
        return typing.cast(typing.Optional[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesForwardSettings], jsii.get(self, "forwardSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchesInput")
    def matches_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatches]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatches]]], jsii.get(self, "matchesInput"))

    @builtins.property
    @jsii.member(jsii_name="matchUrlInput")
    def match_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "matchUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="startInput")
    def start_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "startInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__0c02a3d800732f0d99b133e7d872fd27d97051291adb7ca57e583215335d60af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabled", value)

    @builtins.property
    @jsii.member(jsii_name="end")
    def end(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "end"))

    @end.setter
    def end(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__881ac70a1367b7672b18b014b8e374560b9e4da4b4ff78bf557d4fb996b29c77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "end", value)

    @builtins.property
    @jsii.member(jsii_name="matchUrl")
    def match_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchUrl"))

    @match_url.setter
    def match_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1daa86a161dd9e8e3611810cccddafbcfd574c4304c98bd6f762f0b53d4822ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchUrl", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a74325edfe74e3376808b89718ad94b926b67bc2c2a2a7b7306b20e57d28b4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="start")
    def start(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "start"))

    @start.setter
    def start(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6ebbeb25cc5b65f300ac2bee5e5674039a47e7ece3441fdff60c566ff0fdc4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "start", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsForwardRewriteMatchRuleMatchRules]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsForwardRewriteMatchRuleMatchRules]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsForwardRewriteMatchRuleMatchRules]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__faa34de1e4c900b661d24727c7dc6017f2dc55b88fc13e78aa5bfc06837281ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataAkamaiCloudletsForwardRewriteMatchRule",
    "DataAkamaiCloudletsForwardRewriteMatchRuleConfig",
    "DataAkamaiCloudletsForwardRewriteMatchRuleMatchRules",
    "DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesForwardSettings",
    "DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesForwardSettingsOutputReference",
    "DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesList",
    "DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatches",
    "DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesList",
    "DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValue",
    "DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValueList",
    "DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValueOptions",
    "DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValueOptionsOutputReference",
    "DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValueOutputReference",
    "DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesOutputReference",
    "DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesOutputReference",
]

publication.publish()

def _typecheckingstub__7f9841ce1c0edd9fb17a2cbd0341dade6387ccbc7020cf66cdb78b53a8d0f4d0(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    id: typing.Optional[builtins.str] = None,
    match_rules: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRules, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__591d89211afc13973e75930f90ee9cda2ce88cebdf575a368562aa357726c65a(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2405c80b485fe06c0a5908ea6a8562b66683f4480b4556cde2665f8470ca1b6a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRules, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2151acd73a87efe6eda444ef9ae55af0487e6465d7ba3b762f48724d50d46db9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee10ea8f3a2a5a425f5b8210763b2f01f1dc6707821602db3b5630cf43ec7d1c(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    match_rules: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRules, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b754f394489b2e8d855b4a9d5b1435b429983d2c85740226446c66ad2c707f47(
    *,
    forward_settings: typing.Union[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesForwardSettings, typing.Dict[builtins.str, typing.Any]],
    disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    end: typing.Optional[jsii.Number] = None,
    matches: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatches, typing.Dict[builtins.str, typing.Any]]]]] = None,
    match_url: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    start: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06e59514dbbb143905aaedd3cd3e7ec3d84a38e418ce4985c361d12806730ec7(
    *,
    origin_id: typing.Optional[builtins.str] = None,
    path_and_qs: typing.Optional[builtins.str] = None,
    use_incoming_query_string: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30f7532f997986877abd6bfd60e802c366f130ad53fca0dc9c9d303afcf10f93(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4bd12f4faec4c6bd4e2d94708258f1aeb389f1319a95e19d553870f2a1792c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa6a6b93aae680fe88a975416365a46380024757bb67dfa7ca6045cb4bed5d27(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74bc8cd4990d46963e9b52861e691064ed72fe49e3ecd0abaaa49f0f95c6e0b5(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a2e4a9061aa004ef2309315b221d4baa35520f545fa9623123575c75327a6f7(
    value: typing.Optional[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesForwardSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56da81bb9e87e68e8e3154044fe496b54da036481a4a6558cf7958eecb445011(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__caade0bf67c0b29f9e8be6b067289fc4255c3ec9c29c599b4713416951771e7a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2d916838a1136507c9d72c19ce4c54c6c672351d0eaab3200d0346cea2f48b9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e7b4fd17e43f7713e0eae974dcc95360ab9b45819df1cac6fce9aa17285e4c2(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adec8806f83cd132c9c973f636f6edd8df755105c869a038146292ad6401b9b1(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2161840ba7b0e871f64b438c2321538b74c62e3915cc0ad9fa50d938c06cee1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRules]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80b2e319681b52bc0e5825e43d499852d7da27f84f5fa535f7b65aa1e065c574(
    *,
    case_sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    check_ips: typing.Optional[builtins.str] = None,
    match_operator: typing.Optional[builtins.str] = None,
    match_type: typing.Optional[builtins.str] = None,
    match_value: typing.Optional[builtins.str] = None,
    negate: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    object_match_value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValue, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29e00427c294c8e07aa5f996fb8d5f287473fc4d86790c5bd66457be8538d199(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9dcc40d99c268f9c255f8dda9adaadcdde2ecee3688a7878bf0a48b0594e7ed8(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fcdefea05d59232fcae24792a780c5dc2c6044e2c13af1c8b9ba64f56d4ffbf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b35194d93c7653bbd7d99cb8c395cee0b09a1eccefa11790bcd4b6a7842d31df(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e02e451669e1290bac22e1f37b7a55967e1cd81e21562cf8000270cb8b420a65(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f038e2eef3ce97a60143d62868f54e5543e61a73996df646c361265efd4cda2e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatches]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e67a8d3af6e4a47ee38e53cd92bad435b665ec01408f30dabd83d771c8614f11(
    *,
    type: builtins.str,
    name: typing.Optional[builtins.str] = None,
    name_case_sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    name_has_wildcard: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    options: typing.Optional[typing.Union[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValueOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    value: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49b64bbdae8ff80622583d354bec80c3597b3a8510d14bb4e64882232aa9c5ac(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53423fc12e0cbf27f717cf556b1a7a2106f7f871824e76e2b5a3dee6075a4334(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c4663b407b88ea5be7ee8d6348e89738372fcbee60b49c2695e69e766883e6a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51110a4cf5668b9343692daa8017111f814494c7019a6f58f2e88433daddfc7e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35ba39ef005a0bb9748df84c0e7765bda86959400f4b4902b0ba6dd9058dcd42(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__978e1281d1637f239822883b5a130550896c58400e8fe9371a7eb45cadadb18c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValue]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37b81cdbb0893588bffa6bdc66f6e93b4ecdc4140d60052214082dc9aaad15a7(
    *,
    value: typing.Optional[typing.Sequence[builtins.str]] = None,
    value_case_sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    value_escaped: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    value_has_wildcard: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfa808504a474ab6955b79e53cc11fb2dd9844ae52a7e86d00cc6fcfc0149748(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6911010ed66553dbbf08c37578a7bf725a27e61784f6b0b032a425d2b90b6fe2(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f8999352c3284540e7b66c96419acada17bb3dabc4ca8b54653a2ac03b98f25(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__161dc3879a00407726ca8f84014fd766fee8f8764c722b1aca62c0f3f338e44f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a70ace2ec893109bf63b23b58b441f5906d58597c2e7c028052d13a14ed2b9a7(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab5f2a3426910a9e44ff256f0d8997f4317c93a0546f34215415b4f50fcce43a(
    value: typing.Optional[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValueOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__193568b15ccdb54a0f097b90758eab3ce7106deea8ecfae220f7df6b8a2f6237(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03bbc08cad82be5b2d993f3ac94f10fa37e725f64c6b29c7b8c49454f2e026d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5761b7e390360d3c0ceda2cf00bc0c6f20fdcebbae6296d4dc010b580604c10c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9846d204cb554a692a8688306ca36a844bad6e17fb601b4d40dd31fea7b32e98(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34b20c51933c2aa4e622566d582ba1aa6d0d3d060138ecc304995bb87f3e8076(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c25cb7db3f7b90f93da6b3ebf89dcfe8fcb6fc0836ba202946c250d470aea8d(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__480036fe32c3e24afbc83087418d82c71ea01820adb82be670a5e54ccdae681d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValue]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fa9c4a250c133fdca87e9463a9619a4693db52c8115f30a91813ad0246b7e59(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5582182d01dd433f6b5ff9f1e253cfb96867d74b413eaf844305095a61e7b446(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatchesObjectMatchValue, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5018acee884618e0ab959cd44b957a42b48267ed89fa73dfcff97d4cccfd6473(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fea46591be8d77b51a0be74fdd7aa1ac904eb10f68e21beab50d7084d423b73(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b27748b765115b62f7eab300c67151228a298363d5b397ac365d8144469f3256(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79e4d683ce7d2bf9a921ad80de99aa8c5b5406f1b37951ed27ac336b87601c2b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e7bd110bfe6f520a338e0a99c8523ca2ef3874867c3a11e98d67723152e9add(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__509225cc8669c0b7bab97be5adbc93370b910d943286f1784ae359fddf4f514e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad33ca873cf1d77c44ebd5d2df32f5b32d5694e1f3a874355507ebc590cf90c6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatches]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e9d93648c7b4e9ffd9eddf434bca05bd858ad6e5f6a79113467c75d3d9e7fce(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__572e67d472a4706ef904b8caf72582f34211077862b8f0cf9e9f35b9be23e3db(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsForwardRewriteMatchRuleMatchRulesMatches, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c02a3d800732f0d99b133e7d872fd27d97051291adb7ca57e583215335d60af(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__881ac70a1367b7672b18b014b8e374560b9e4da4b4ff78bf557d4fb996b29c77(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1daa86a161dd9e8e3611810cccddafbcfd574c4304c98bd6f762f0b53d4822ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a74325edfe74e3376808b89718ad94b926b67bc2c2a2a7b7306b20e57d28b4a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6ebbeb25cc5b65f300ac2bee5e5674039a47e7ece3441fdff60c566ff0fdc4c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__faa34de1e4c900b661d24727c7dc6017f2dc55b88fc13e78aa5bfc06837281ff(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsForwardRewriteMatchRuleMatchRules]],
) -> None:
    """Type checking stubs"""
    pass
