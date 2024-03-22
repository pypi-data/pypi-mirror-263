'''
# `data_akamai_cloudlets_visitor_prioritization_match_rule`

Refer to the Terraform Registry for docs: [`data_akamai_cloudlets_visitor_prioritization_match_rule`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule).
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


class DataAkamaiCloudletsVisitorPrioritizationMatchRule(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsVisitorPrioritizationMatchRule.DataAkamaiCloudletsVisitorPrioritizationMatchRule",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule akamai_cloudlets_visitor_prioritization_match_rule}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        id: typing.Optional[builtins.str] = None,
        match_rules: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRules", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule akamai_cloudlets_visitor_prioritization_match_rule} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#id DataAkamaiCloudletsVisitorPrioritizationMatchRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param match_rules: match_rules block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#match_rules DataAkamaiCloudletsVisitorPrioritizationMatchRule#match_rules}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bad489b608c37e3642acf2e45c0bc4a64f6cbd68f08df56d9b8759e3b08b80c4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAkamaiCloudletsVisitorPrioritizationMatchRuleConfig(
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
        '''Generates CDKTF code for importing a DataAkamaiCloudletsVisitorPrioritizationMatchRule resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the DataAkamaiCloudletsVisitorPrioritizationMatchRule to import.
        :param import_from_id: The id of the existing DataAkamaiCloudletsVisitorPrioritizationMatchRule that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the DataAkamaiCloudletsVisitorPrioritizationMatchRule to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0fb421eef000053631abea5113d58f724c1fac743bfe98789ca249951c6fc5b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putMatchRules")
    def put_match_rules(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRules", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0a1bc7db39f3954c0811b1063c5fcb6e79189b77e8d99a1ba126d7a0041e484)
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
    def match_rules(
        self,
    ) -> "DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesList":
        return typing.cast("DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesList", jsii.get(self, "matchRules"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="matchRulesInput")
    def match_rules_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRules"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRules"]]], jsii.get(self, "matchRulesInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76704d48efa6b1cb0e19cfdab40179671bd8431a047e084be1cdfaa5021f64df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsVisitorPrioritizationMatchRule.DataAkamaiCloudletsVisitorPrioritizationMatchRuleConfig",
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
class DataAkamaiCloudletsVisitorPrioritizationMatchRuleConfig(
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
        match_rules: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRules", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#id DataAkamaiCloudletsVisitorPrioritizationMatchRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param match_rules: match_rules block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#match_rules DataAkamaiCloudletsVisitorPrioritizationMatchRule#match_rules}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c7dd8944a287b555d4cd2485fa2bc081923ca55ce109f159190c11bcdece6d3)
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
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#id DataAkamaiCloudletsVisitorPrioritizationMatchRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_rules(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRules"]]]:
        '''match_rules block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#match_rules DataAkamaiCloudletsVisitorPrioritizationMatchRule#match_rules}
        '''
        result = self._values.get("match_rules")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRules"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsVisitorPrioritizationMatchRuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsVisitorPrioritizationMatchRule.DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRules",
    jsii_struct_bases=[],
    name_mapping={
        "pass_through_percent": "passThroughPercent",
        "disabled": "disabled",
        "end": "end",
        "matches": "matches",
        "match_url": "matchUrl",
        "name": "name",
        "start": "start",
    },
)
class DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRules:
    def __init__(
        self,
        *,
        pass_through_percent: jsii.Number,
        disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        end: typing.Optional[jsii.Number] = None,
        matches: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatches", typing.Dict[builtins.str, typing.Any]]]]] = None,
        match_url: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        start: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param pass_through_percent: The range 0.0: 99.0 specifies the percentage of requests that pass through to the origin. The value of 100 means the request always passes through to the origin. A value of -1 means send everyone to the waiting room. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#pass_through_percent DataAkamaiCloudletsVisitorPrioritizationMatchRule#pass_through_percent}
        :param disabled: If set to true, disables a rule so it is not evaluated against incoming requests. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#disabled DataAkamaiCloudletsVisitorPrioritizationMatchRule#disabled}
        :param end: The end time for this match (in seconds since the epoch). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#end DataAkamaiCloudletsVisitorPrioritizationMatchRule#end}
        :param matches: matches block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#matches DataAkamaiCloudletsVisitorPrioritizationMatchRule#matches}
        :param match_url: If using a URL match, this property is the URL that the Cloudlet uses to match the incoming request. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#match_url DataAkamaiCloudletsVisitorPrioritizationMatchRule#match_url}
        :param name: The name of the rule. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#name DataAkamaiCloudletsVisitorPrioritizationMatchRule#name}
        :param start: The start time for this match (in seconds since the epoch). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#start DataAkamaiCloudletsVisitorPrioritizationMatchRule#start}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69dc53709db83cd1c4d79276b4fe69688f5756d97aee294cba91dd15fc0c6a35)
            check_type(argname="argument pass_through_percent", value=pass_through_percent, expected_type=type_hints["pass_through_percent"])
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
            check_type(argname="argument end", value=end, expected_type=type_hints["end"])
            check_type(argname="argument matches", value=matches, expected_type=type_hints["matches"])
            check_type(argname="argument match_url", value=match_url, expected_type=type_hints["match_url"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument start", value=start, expected_type=type_hints["start"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "pass_through_percent": pass_through_percent,
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
    def pass_through_percent(self) -> jsii.Number:
        '''The range 0.0: 99.0 specifies the percentage of requests that pass through to the origin. The value of 100 means the request always passes through to the origin. A value of -1 means send everyone to the waiting room.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#pass_through_percent DataAkamaiCloudletsVisitorPrioritizationMatchRule#pass_through_percent}
        '''
        result = self._values.get("pass_through_percent")
        assert result is not None, "Required property 'pass_through_percent' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If set to true, disables a rule so it is not evaluated against incoming requests.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#disabled DataAkamaiCloudletsVisitorPrioritizationMatchRule#disabled}
        '''
        result = self._values.get("disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def end(self) -> typing.Optional[jsii.Number]:
        '''The end time for this match (in seconds since the epoch).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#end DataAkamaiCloudletsVisitorPrioritizationMatchRule#end}
        '''
        result = self._values.get("end")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def matches(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatches"]]]:
        '''matches block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#matches DataAkamaiCloudletsVisitorPrioritizationMatchRule#matches}
        '''
        result = self._values.get("matches")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatches"]]], result)

    @builtins.property
    def match_url(self) -> typing.Optional[builtins.str]:
        '''If using a URL match, this property is the URL that the Cloudlet uses to match the incoming request.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#match_url DataAkamaiCloudletsVisitorPrioritizationMatchRule#match_url}
        '''
        result = self._values.get("match_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the rule.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#name DataAkamaiCloudletsVisitorPrioritizationMatchRule#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start(self) -> typing.Optional[jsii.Number]:
        '''The start time for this match (in seconds since the epoch).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#start DataAkamaiCloudletsVisitorPrioritizationMatchRule#start}
        '''
        result = self._values.get("start")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsVisitorPrioritizationMatchRule.DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e2c8fec231230c5cb13d5a38fa0cac1f630fa693d72613f80d3922083cb81952)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97b8264642033655a7b6c52342f6e76d5f6e7d7f1c8eb79b92112b2f8e6b84e9)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd3fdd3be3d0cda4a5f77cd17dc2cbdf2325c59e17ce86d764e2926fe0372832)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5f68f6b8350675365f77cbefdb66fb47543a2fc7bc19df949fd4e00376af5e1b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1605094691634807f850a95406130fe7c7cdc6dbd523fc19d4e9fa9c71e34f07)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRules]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRules]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRules]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9436dd460b1bcc596f5e3199b41ea416ed665bc0cbbc4b26a5492b9ae7a9dc59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsVisitorPrioritizationMatchRule.DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatches",
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
class DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatches:
    def __init__(
        self,
        *,
        case_sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        check_ips: typing.Optional[builtins.str] = None,
        match_operator: typing.Optional[builtins.str] = None,
        match_type: typing.Optional[builtins.str] = None,
        match_value: typing.Optional[builtins.str] = None,
        negate: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        object_match_value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValue", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param case_sensitive: If true, the match is case sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#case_sensitive DataAkamaiCloudletsVisitorPrioritizationMatchRule#case_sensitive}
        :param check_ips: For clientip, continent, countrycode, proxy, and regioncode match types, the part of the request that determines the IP address to use. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#check_ips DataAkamaiCloudletsVisitorPrioritizationMatchRule#check_ips}
        :param match_operator: Valid entries for this property: contains, exists, and equals. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#match_operator DataAkamaiCloudletsVisitorPrioritizationMatchRule#match_operator}
        :param match_type: The type of match used. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#match_type DataAkamaiCloudletsVisitorPrioritizationMatchRule#match_type}
        :param match_value: Depends on the matchType. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#match_value DataAkamaiCloudletsVisitorPrioritizationMatchRule#match_value}
        :param negate: If true, negates the match. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#negate DataAkamaiCloudletsVisitorPrioritizationMatchRule#negate}
        :param object_match_value: object_match_value block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#object_match_value DataAkamaiCloudletsVisitorPrioritizationMatchRule#object_match_value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66145912e8b1dcff8085d4c49d489a0bff9c8d4feb90fa1b05ce4b815d267a3a)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#case_sensitive DataAkamaiCloudletsVisitorPrioritizationMatchRule#case_sensitive}
        '''
        result = self._values.get("case_sensitive")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def check_ips(self) -> typing.Optional[builtins.str]:
        '''For clientip, continent, countrycode, proxy, and regioncode match types, the part of the request that determines the IP address to use.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#check_ips DataAkamaiCloudletsVisitorPrioritizationMatchRule#check_ips}
        '''
        result = self._values.get("check_ips")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_operator(self) -> typing.Optional[builtins.str]:
        '''Valid entries for this property: contains, exists, and equals.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#match_operator DataAkamaiCloudletsVisitorPrioritizationMatchRule#match_operator}
        '''
        result = self._values.get("match_operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_type(self) -> typing.Optional[builtins.str]:
        '''The type of match used.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#match_type DataAkamaiCloudletsVisitorPrioritizationMatchRule#match_type}
        '''
        result = self._values.get("match_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_value(self) -> typing.Optional[builtins.str]:
        '''Depends on the matchType.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#match_value DataAkamaiCloudletsVisitorPrioritizationMatchRule#match_value}
        '''
        result = self._values.get("match_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def negate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If true, negates the match.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#negate DataAkamaiCloudletsVisitorPrioritizationMatchRule#negate}
        '''
        result = self._values.get("negate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def object_match_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValue"]]]:
        '''object_match_value block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#object_match_value DataAkamaiCloudletsVisitorPrioritizationMatchRule#object_match_value}
        '''
        result = self._values.get("object_match_value")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValue"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatches(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsVisitorPrioritizationMatchRule.DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d11006f916a8b11e9f330f071c80469adc091f8d77ab359cb1efecddf0381035)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9554d3bed31d0016c9d048526d95ab657ea4be04bec847af008a2a16a337bf9f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0188b511d7b411a451f3363798b105264c9536003238368aee538f7393eb7690)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8567608be7ad44ce55aa68104542485cc5baf5a84486250a7a44e64951095ba4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__81a2a367ded0709f23cadfb1e3afa660cb633f28e5281ee2a0ec1e84e46a038d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatches]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatches]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatches]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73b896cf567e016b608a81aeab661ce57d1b163c374293cf17980e079f579a18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsVisitorPrioritizationMatchRule.DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValue",
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
class DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValue:
    def __init__(
        self,
        *,
        type: builtins.str,
        name: typing.Optional[builtins.str] = None,
        name_case_sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        name_has_wildcard: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        options: typing.Optional[typing.Union["DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValueOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        value: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: The array type, which can be one of the following: object or simple. Use the simple option when adding only an array of string-based values Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#type DataAkamaiCloudletsVisitorPrioritizationMatchRule#type}
        :param name: If using a match type that supports name attributes, enter the value in the incoming request to match on. The following match types support this property: cookie, header, parameter, and query Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#name DataAkamaiCloudletsVisitorPrioritizationMatchRule#name}
        :param name_case_sensitive: Set to true if the entry for the name property should be evaluated based on case sensitivity. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#name_case_sensitive DataAkamaiCloudletsVisitorPrioritizationMatchRule#name_case_sensitive}
        :param name_has_wildcard: Set to true if the entry for the name property includes wildcards. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#name_has_wildcard DataAkamaiCloudletsVisitorPrioritizationMatchRule#name_has_wildcard}
        :param options: options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#options DataAkamaiCloudletsVisitorPrioritizationMatchRule#options}
        :param value: The value attributes in the incoming request to match on (use only with simple type). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#value DataAkamaiCloudletsVisitorPrioritizationMatchRule#value}
        '''
        if isinstance(options, dict):
            options = DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValueOptions(**options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcee2020e4876f450dd86775539d932bacab0c4f5b4b352e85a72cb0400e3bcc)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#type DataAkamaiCloudletsVisitorPrioritizationMatchRule#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''If using a match type that supports name attributes, enter the value in the incoming request to match on.

        The following match types support this property: cookie, header, parameter, and query

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#name DataAkamaiCloudletsVisitorPrioritizationMatchRule#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name_case_sensitive(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set to true if the entry for the name property should be evaluated based on case sensitivity.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#name_case_sensitive DataAkamaiCloudletsVisitorPrioritizationMatchRule#name_case_sensitive}
        '''
        result = self._values.get("name_case_sensitive")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def name_has_wildcard(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set to true if the entry for the name property includes wildcards.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#name_has_wildcard DataAkamaiCloudletsVisitorPrioritizationMatchRule#name_has_wildcard}
        '''
        result = self._values.get("name_has_wildcard")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def options(
        self,
    ) -> typing.Optional["DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValueOptions"]:
        '''options block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#options DataAkamaiCloudletsVisitorPrioritizationMatchRule#options}
        '''
        result = self._values.get("options")
        return typing.cast(typing.Optional["DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValueOptions"], result)

    @builtins.property
    def value(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The value attributes in the incoming request to match on (use only with simple type).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#value DataAkamaiCloudletsVisitorPrioritizationMatchRule#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValueList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsVisitorPrioritizationMatchRule.DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValueList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cbfb19d0d1962bedff50d9a08b5a681b6f199fe8b3943f0eb4ea4f1af5251322)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValueOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f3c4ed1022e80053a392bda6754a7c05510bd11321254121daab079731c32cb)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValueOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80d540993700a62680b27a16e20fc7e35f00f05822d8674d314263b0c4414b43)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b5ce79f512038fc51b7d4d74fcd695e0d6268dba0da7b5711eefe5add07ac903)
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
            type_hints = typing.get_type_hints(_typecheckingstub__214920aa0ca7c80b18c651c65d6dc46fec70a19622584abdb2e26ebae47f1646)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValue]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValue]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValue]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34ef70f844aa0408c7e9b55e071152a662e8a6dacd97bd054d82995ea253abe2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsVisitorPrioritizationMatchRule.DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValueOptions",
    jsii_struct_bases=[],
    name_mapping={
        "value": "value",
        "value_case_sensitive": "valueCaseSensitive",
        "value_escaped": "valueEscaped",
        "value_has_wildcard": "valueHasWildcard",
    },
)
class DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValueOptions:
    def __init__(
        self,
        *,
        value: typing.Optional[typing.Sequence[builtins.str]] = None,
        value_case_sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        value_escaped: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        value_has_wildcard: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param value: The value attributes in the incoming request to match on. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#value DataAkamaiCloudletsVisitorPrioritizationMatchRule#value}
        :param value_case_sensitive: Set to true if the entries for the value property should be evaluated based on case sensitivity. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#value_case_sensitive DataAkamaiCloudletsVisitorPrioritizationMatchRule#value_case_sensitive}
        :param value_escaped: Set to true if provided value should be compared in escaped form. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#value_escaped DataAkamaiCloudletsVisitorPrioritizationMatchRule#value_escaped}
        :param value_has_wildcard: Set to true if the entries for the value property include wildcards. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#value_has_wildcard DataAkamaiCloudletsVisitorPrioritizationMatchRule#value_has_wildcard}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1ffd54dbbceb18539f0e15f9d02f9b637b7f96e3362e06656c5a7b7e7676e4f)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#value DataAkamaiCloudletsVisitorPrioritizationMatchRule#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def value_case_sensitive(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set to true if the entries for the value property should be evaluated based on case sensitivity.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#value_case_sensitive DataAkamaiCloudletsVisitorPrioritizationMatchRule#value_case_sensitive}
        '''
        result = self._values.get("value_case_sensitive")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def value_escaped(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set to true if provided value should be compared in escaped form.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#value_escaped DataAkamaiCloudletsVisitorPrioritizationMatchRule#value_escaped}
        '''
        result = self._values.get("value_escaped")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def value_has_wildcard(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set to true if the entries for the value property include wildcards.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#value_has_wildcard DataAkamaiCloudletsVisitorPrioritizationMatchRule#value_has_wildcard}
        '''
        result = self._values.get("value_has_wildcard")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValueOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValueOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsVisitorPrioritizationMatchRule.DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValueOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4b137c0b24c3913cbe3530ff832763d619e8d6dc77b0ad71e14297aab3e6ffdb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ca28292343c11c75787fe2bdab79d82c4bcbd6cd8f5c0c32a2144ef1f9c31fbe)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5748941583a2458d22965d03b25d5433b45a77c6454a0ffd9c70a4f2e03f02d4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__41d5ec1e7acad8724d0c8c2d921c61a23deaff0997ad0df0c46cf53ac7a3e4fe)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0c04248cf556883a1757fcca64f1d3018811ec6c21b2924a80f7a3eb3587ad55)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "valueHasWildcard", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValueOptions]:
        return typing.cast(typing.Optional[DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValueOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValueOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50bccc105122833ba2964f5d6bcdc88af72f7cd936950f60f78239fb1c5689f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValueOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsVisitorPrioritizationMatchRule.DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValueOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2c08c8d1087364dd6bec25b7e581f81d87101103739fdeff3a22dfc34f7d7fd1)
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
        :param value: The value attributes in the incoming request to match on. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#value DataAkamaiCloudletsVisitorPrioritizationMatchRule#value}
        :param value_case_sensitive: Set to true if the entries for the value property should be evaluated based on case sensitivity. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#value_case_sensitive DataAkamaiCloudletsVisitorPrioritizationMatchRule#value_case_sensitive}
        :param value_escaped: Set to true if provided value should be compared in escaped form. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#value_escaped DataAkamaiCloudletsVisitorPrioritizationMatchRule#value_escaped}
        :param value_has_wildcard: Set to true if the entries for the value property include wildcards. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_visitor_prioritization_match_rule#value_has_wildcard DataAkamaiCloudletsVisitorPrioritizationMatchRule#value_has_wildcard}
        '''
        value_ = DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValueOptions(
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
    ) -> DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValueOptionsOutputReference:
        return typing.cast(DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValueOptionsOutputReference, jsii.get(self, "options"))

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
    ) -> typing.Optional[DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValueOptions]:
        return typing.cast(typing.Optional[DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValueOptions], jsii.get(self, "optionsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__b296a45792693986a7cc533e2ed4481559bd08c7c5417e528647ee694c8f246f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ecb323d17f180c9f3ab944887587501ca6f52dc98224124a5ac964d605dafccb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__493427bf75ebeeb9fac40502dd528badfefa82b062b14aa4d69a4b5af35a7de3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nameHasWildcard", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f7e95b7d5ca65f37174377702191740c722638b57f3104354639bd6f1c78881)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "value"))

    @value.setter
    def value(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dccdae8663fb42fbe262bb1c85abcb0784c55c32ea1167844425bb1ee8937777)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValue]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValue]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValue]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21fcc1fad56b099c1efd5bb808b96a74dee71db6bec2b04ad61614192e1b300a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsVisitorPrioritizationMatchRule.DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__392bac50139c654db9ae0db2403f63d31fe901d37bad3af582f39b2af9a044a4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putObjectMatchValue")
    def put_object_match_value(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValue, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b027be3076cd663a7da7d05bf468cfda0ad904f1fb0ef4febbd653aacd4203d)
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
    ) -> DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValueList:
        return typing.cast(DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValueList, jsii.get(self, "objectMatchValue"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValue]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValue]]], jsii.get(self, "objectMatchValueInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__0c43e9e52dc9c1e8a17f19f6d498a7a00751dddf3eb13423b7a7e121cfa0aa0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caseSensitive", value)

    @builtins.property
    @jsii.member(jsii_name="checkIps")
    def check_ips(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "checkIps"))

    @check_ips.setter
    def check_ips(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e55a5f4bcbef291516912fd85faccb4b7457fb1a8a4e6765e54b796e912791d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "checkIps", value)

    @builtins.property
    @jsii.member(jsii_name="matchOperator")
    def match_operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchOperator"))

    @match_operator.setter
    def match_operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b9d715c761583d41c586095c5dc3838a41a514f523b8185d96fcc42cab02b2f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOperator", value)

    @builtins.property
    @jsii.member(jsii_name="matchType")
    def match_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchType"))

    @match_type.setter
    def match_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eed0de5a039841c0664d8b7ef74d2380beadf99fc337edf1de30a3e4761df311)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchType", value)

    @builtins.property
    @jsii.member(jsii_name="matchValue")
    def match_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchValue"))

    @match_value.setter
    def match_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8b5ceec23303216293fb5674c4bdbe54c4454c8d26deb3f3fa60dbad1ef1812)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bd64dfc68169078042db10c09d97ac97fadec32df9326f3dfba5e523065ac8a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatches]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatches]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatches]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3cc209847c8774b30883233cb866d7473b6d914288c698ea5941fe4f5c184d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsVisitorPrioritizationMatchRule.DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c2e2816222a5a755c9c003c2f901b40ff55d74212568b7e25974a4857b05cd43)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMatches")
    def put_matches(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatches, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0339f51cf2349cdc7055227ab4314996c9c486ebf19f153404e60641b78158a1)
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
    @jsii.member(jsii_name="matches")
    def matches(
        self,
    ) -> DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesList:
        return typing.cast(DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesList, jsii.get(self, "matches"))

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
    @jsii.member(jsii_name="matchesInput")
    def matches_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatches]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatches]]], jsii.get(self, "matchesInput"))

    @builtins.property
    @jsii.member(jsii_name="matchUrlInput")
    def match_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "matchUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="passThroughPercentInput")
    def pass_through_percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "passThroughPercentInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__500ee4d8cdd409f8e0b1027a1472301aea435493c630807b26a81b1e31dd791a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabled", value)

    @builtins.property
    @jsii.member(jsii_name="end")
    def end(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "end"))

    @end.setter
    def end(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b6d45ab42aed1c9440e534e9baff95a56b84d62c18c9ea071e5790143c203cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "end", value)

    @builtins.property
    @jsii.member(jsii_name="matchUrl")
    def match_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchUrl"))

    @match_url.setter
    def match_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3a971dc54aba9e18dfe8943e7b052dc6302db3cecff7647477f5f3c1cab7f54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchUrl", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__431a8e1ff3b9a40be2098e59474b8390ada3fde70de661b5614d4feec19ac522)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="passThroughPercent")
    def pass_through_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "passThroughPercent"))

    @pass_through_percent.setter
    def pass_through_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07611f9968221c51a4e3442ce44614a6f160a0fb11669f19dad66bd23683e0bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passThroughPercent", value)

    @builtins.property
    @jsii.member(jsii_name="start")
    def start(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "start"))

    @start.setter
    def start(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ed18728dfa16bdf5754fa5e12e31f8939845f0fa16a43504ab7023097829867)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "start", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRules]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRules]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRules]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0532140180774be883e40fc90b5d5e25e3504e699c91f26389388b5f26e34320)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataAkamaiCloudletsVisitorPrioritizationMatchRule",
    "DataAkamaiCloudletsVisitorPrioritizationMatchRuleConfig",
    "DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRules",
    "DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesList",
    "DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatches",
    "DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesList",
    "DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValue",
    "DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValueList",
    "DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValueOptions",
    "DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValueOptionsOutputReference",
    "DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValueOutputReference",
    "DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesOutputReference",
    "DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesOutputReference",
]

publication.publish()

def _typecheckingstub__bad489b608c37e3642acf2e45c0bc4a64f6cbd68f08df56d9b8759e3b08b80c4(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    id: typing.Optional[builtins.str] = None,
    match_rules: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRules, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__d0fb421eef000053631abea5113d58f724c1fac743bfe98789ca249951c6fc5b(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0a1bc7db39f3954c0811b1063c5fcb6e79189b77e8d99a1ba126d7a0041e484(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRules, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76704d48efa6b1cb0e19cfdab40179671bd8431a047e084be1cdfaa5021f64df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c7dd8944a287b555d4cd2485fa2bc081923ca55ce109f159190c11bcdece6d3(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    match_rules: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRules, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69dc53709db83cd1c4d79276b4fe69688f5756d97aee294cba91dd15fc0c6a35(
    *,
    pass_through_percent: jsii.Number,
    disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    end: typing.Optional[jsii.Number] = None,
    matches: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatches, typing.Dict[builtins.str, typing.Any]]]]] = None,
    match_url: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    start: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2c8fec231230c5cb13d5a38fa0cac1f630fa693d72613f80d3922083cb81952(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97b8264642033655a7b6c52342f6e76d5f6e7d7f1c8eb79b92112b2f8e6b84e9(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd3fdd3be3d0cda4a5f77cd17dc2cbdf2325c59e17ce86d764e2926fe0372832(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f68f6b8350675365f77cbefdb66fb47543a2fc7bc19df949fd4e00376af5e1b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1605094691634807f850a95406130fe7c7cdc6dbd523fc19d4e9fa9c71e34f07(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9436dd460b1bcc596f5e3199b41ea416ed665bc0cbbc4b26a5492b9ae7a9dc59(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRules]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66145912e8b1dcff8085d4c49d489a0bff9c8d4feb90fa1b05ce4b815d267a3a(
    *,
    case_sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    check_ips: typing.Optional[builtins.str] = None,
    match_operator: typing.Optional[builtins.str] = None,
    match_type: typing.Optional[builtins.str] = None,
    match_value: typing.Optional[builtins.str] = None,
    negate: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    object_match_value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValue, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d11006f916a8b11e9f330f071c80469adc091f8d77ab359cb1efecddf0381035(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9554d3bed31d0016c9d048526d95ab657ea4be04bec847af008a2a16a337bf9f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0188b511d7b411a451f3363798b105264c9536003238368aee538f7393eb7690(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8567608be7ad44ce55aa68104542485cc5baf5a84486250a7a44e64951095ba4(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81a2a367ded0709f23cadfb1e3afa660cb633f28e5281ee2a0ec1e84e46a038d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73b896cf567e016b608a81aeab661ce57d1b163c374293cf17980e079f579a18(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatches]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcee2020e4876f450dd86775539d932bacab0c4f5b4b352e85a72cb0400e3bcc(
    *,
    type: builtins.str,
    name: typing.Optional[builtins.str] = None,
    name_case_sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    name_has_wildcard: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    options: typing.Optional[typing.Union[DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValueOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    value: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbfb19d0d1962bedff50d9a08b5a681b6f199fe8b3943f0eb4ea4f1af5251322(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f3c4ed1022e80053a392bda6754a7c05510bd11321254121daab079731c32cb(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80d540993700a62680b27a16e20fc7e35f00f05822d8674d314263b0c4414b43(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5ce79f512038fc51b7d4d74fcd695e0d6268dba0da7b5711eefe5add07ac903(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__214920aa0ca7c80b18c651c65d6dc46fec70a19622584abdb2e26ebae47f1646(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34ef70f844aa0408c7e9b55e071152a662e8a6dacd97bd054d82995ea253abe2(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValue]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1ffd54dbbceb18539f0e15f9d02f9b637b7f96e3362e06656c5a7b7e7676e4f(
    *,
    value: typing.Optional[typing.Sequence[builtins.str]] = None,
    value_case_sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    value_escaped: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    value_has_wildcard: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b137c0b24c3913cbe3530ff832763d619e8d6dc77b0ad71e14297aab3e6ffdb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca28292343c11c75787fe2bdab79d82c4bcbd6cd8f5c0c32a2144ef1f9c31fbe(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5748941583a2458d22965d03b25d5433b45a77c6454a0ffd9c70a4f2e03f02d4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41d5ec1e7acad8724d0c8c2d921c61a23deaff0997ad0df0c46cf53ac7a3e4fe(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c04248cf556883a1757fcca64f1d3018811ec6c21b2924a80f7a3eb3587ad55(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50bccc105122833ba2964f5d6bcdc88af72f7cd936950f60f78239fb1c5689f2(
    value: typing.Optional[DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValueOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c08c8d1087364dd6bec25b7e581f81d87101103739fdeff3a22dfc34f7d7fd1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b296a45792693986a7cc533e2ed4481559bd08c7c5417e528647ee694c8f246f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecb323d17f180c9f3ab944887587501ca6f52dc98224124a5ac964d605dafccb(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__493427bf75ebeeb9fac40502dd528badfefa82b062b14aa4d69a4b5af35a7de3(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f7e95b7d5ca65f37174377702191740c722638b57f3104354639bd6f1c78881(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dccdae8663fb42fbe262bb1c85abcb0784c55c32ea1167844425bb1ee8937777(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21fcc1fad56b099c1efd5bb808b96a74dee71db6bec2b04ad61614192e1b300a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValue]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__392bac50139c654db9ae0db2403f63d31fe901d37bad3af582f39b2af9a044a4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b027be3076cd663a7da7d05bf468cfda0ad904f1fb0ef4febbd653aacd4203d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatchesObjectMatchValue, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c43e9e52dc9c1e8a17f19f6d498a7a00751dddf3eb13423b7a7e121cfa0aa0d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e55a5f4bcbef291516912fd85faccb4b7457fb1a8a4e6765e54b796e912791d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b9d715c761583d41c586095c5dc3838a41a514f523b8185d96fcc42cab02b2f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eed0de5a039841c0664d8b7ef74d2380beadf99fc337edf1de30a3e4761df311(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8b5ceec23303216293fb5674c4bdbe54c4454c8d26deb3f3fa60dbad1ef1812(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd64dfc68169078042db10c09d97ac97fadec32df9326f3dfba5e523065ac8a7(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3cc209847c8774b30883233cb866d7473b6d914288c698ea5941fe4f5c184d3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatches]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2e2816222a5a755c9c003c2f901b40ff55d74212568b7e25974a4857b05cd43(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0339f51cf2349cdc7055227ab4314996c9c486ebf19f153404e60641b78158a1(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRulesMatches, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__500ee4d8cdd409f8e0b1027a1472301aea435493c630807b26a81b1e31dd791a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b6d45ab42aed1c9440e534e9baff95a56b84d62c18c9ea071e5790143c203cb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3a971dc54aba9e18dfe8943e7b052dc6302db3cecff7647477f5f3c1cab7f54(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__431a8e1ff3b9a40be2098e59474b8390ada3fde70de661b5614d4feec19ac522(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07611f9968221c51a4e3442ce44614a6f160a0fb11669f19dad66bd23683e0bd(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ed18728dfa16bdf5754fa5e12e31f8939845f0fa16a43504ab7023097829867(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0532140180774be883e40fc90b5d5e25e3504e699c91f26389388b5f26e34320(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsVisitorPrioritizationMatchRuleMatchRules]],
) -> None:
    """Type checking stubs"""
    pass
