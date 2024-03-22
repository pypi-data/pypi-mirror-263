'''
# `data_akamai_cloudlets_application_load_balancer_match_rule`

Refer to the Terraform Registry for docs: [`data_akamai_cloudlets_application_load_balancer_match_rule`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule).
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


class DataAkamaiCloudletsApplicationLoadBalancerMatchRule(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsApplicationLoadBalancerMatchRule.DataAkamaiCloudletsApplicationLoadBalancerMatchRule",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule akamai_cloudlets_application_load_balancer_match_rule}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        id: typing.Optional[builtins.str] = None,
        match_rules: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRules", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule akamai_cloudlets_application_load_balancer_match_rule} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#id DataAkamaiCloudletsApplicationLoadBalancerMatchRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param match_rules: match_rules block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#match_rules DataAkamaiCloudletsApplicationLoadBalancerMatchRule#match_rules}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1772c11a86aae8a0485884f54f5d2a9447f7171f588e574db9ed291514a2c399)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAkamaiCloudletsApplicationLoadBalancerMatchRuleConfig(
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
        '''Generates CDKTF code for importing a DataAkamaiCloudletsApplicationLoadBalancerMatchRule resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the DataAkamaiCloudletsApplicationLoadBalancerMatchRule to import.
        :param import_from_id: The id of the existing DataAkamaiCloudletsApplicationLoadBalancerMatchRule that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the DataAkamaiCloudletsApplicationLoadBalancerMatchRule to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c47c5db7f777c6d0884e9dc9dec32b87d7d28bc120723c53412faf844249450c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putMatchRules")
    def put_match_rules(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRules", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__445105dade110916e45d87429ce10616698e696c83ca8e9b12930831a588f8d7)
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
    ) -> "DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesList":
        return typing.cast("DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesList", jsii.get(self, "matchRules"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="matchRulesInput")
    def match_rules_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRules"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRules"]]], jsii.get(self, "matchRulesInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf28c77404a00a1907e8c589b9a5b5ff1b9772f285c4f0c1d8593077cde370e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsApplicationLoadBalancerMatchRule.DataAkamaiCloudletsApplicationLoadBalancerMatchRuleConfig",
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
class DataAkamaiCloudletsApplicationLoadBalancerMatchRuleConfig(
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
        match_rules: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRules", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#id DataAkamaiCloudletsApplicationLoadBalancerMatchRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param match_rules: match_rules block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#match_rules DataAkamaiCloudletsApplicationLoadBalancerMatchRule#match_rules}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4cda175ee9f7087f1a03edbff3cca49450d1b63d05b20b9b1771f423ef2446a)
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
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#id DataAkamaiCloudletsApplicationLoadBalancerMatchRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_rules(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRules"]]]:
        '''match_rules block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#match_rules DataAkamaiCloudletsApplicationLoadBalancerMatchRule#match_rules}
        '''
        result = self._values.get("match_rules")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRules"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsApplicationLoadBalancerMatchRuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsApplicationLoadBalancerMatchRule.DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRules",
    jsii_struct_bases=[],
    name_mapping={
        "forward_settings": "forwardSettings",
        "disabled": "disabled",
        "end": "end",
        "id": "id",
        "matches": "matches",
        "matches_always": "matchesAlways",
        "match_url": "matchUrl",
        "name": "name",
        "start": "start",
    },
)
class DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRules:
    def __init__(
        self,
        *,
        forward_settings: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesForwardSettings", typing.Dict[builtins.str, typing.Any]]]],
        disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        end: typing.Optional[jsii.Number] = None,
        id: typing.Optional[jsii.Number] = None,
        matches: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatches", typing.Dict[builtins.str, typing.Any]]]]] = None,
        matches_always: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        match_url: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        start: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param forward_settings: forward_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#forward_settings DataAkamaiCloudletsApplicationLoadBalancerMatchRule#forward_settings}
        :param disabled: If set to true, disables a rule so it is not evaluated against incoming requests. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#disabled DataAkamaiCloudletsApplicationLoadBalancerMatchRule#disabled}
        :param end: The end time for this match (in seconds since the epoch). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#end DataAkamaiCloudletsApplicationLoadBalancerMatchRule#end}
        :param id: Akamai internal use only. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#id DataAkamaiCloudletsApplicationLoadBalancerMatchRule#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param matches: matches block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#matches DataAkamaiCloudletsApplicationLoadBalancerMatchRule#matches}
        :param matches_always: Is used in some cloudlets to support default rules (rule that is always matched). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#matches_always DataAkamaiCloudletsApplicationLoadBalancerMatchRule#matches_always}
        :param match_url: If using a URL match, this property is the URL that the Cloudlet uses to match the incoming request. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#match_url DataAkamaiCloudletsApplicationLoadBalancerMatchRule#match_url}
        :param name: The name of the rule. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#name DataAkamaiCloudletsApplicationLoadBalancerMatchRule#name}
        :param start: The start time for this match (in seconds since the epoch). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#start DataAkamaiCloudletsApplicationLoadBalancerMatchRule#start}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07e08f624dad9e1a1ab379da6ec5bf77de9d3e3f49131e0f98e32f20b9f2adbe)
            check_type(argname="argument forward_settings", value=forward_settings, expected_type=type_hints["forward_settings"])
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
            check_type(argname="argument end", value=end, expected_type=type_hints["end"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument matches", value=matches, expected_type=type_hints["matches"])
            check_type(argname="argument matches_always", value=matches_always, expected_type=type_hints["matches_always"])
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
        if id is not None:
            self._values["id"] = id
        if matches is not None:
            self._values["matches"] = matches
        if matches_always is not None:
            self._values["matches_always"] = matches_always
        if match_url is not None:
            self._values["match_url"] = match_url
        if name is not None:
            self._values["name"] = name
        if start is not None:
            self._values["start"] = start

    @builtins.property
    def forward_settings(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesForwardSettings"]]:
        '''forward_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#forward_settings DataAkamaiCloudletsApplicationLoadBalancerMatchRule#forward_settings}
        '''
        result = self._values.get("forward_settings")
        assert result is not None, "Required property 'forward_settings' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesForwardSettings"]], result)

    @builtins.property
    def disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If set to true, disables a rule so it is not evaluated against incoming requests.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#disabled DataAkamaiCloudletsApplicationLoadBalancerMatchRule#disabled}
        '''
        result = self._values.get("disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def end(self) -> typing.Optional[jsii.Number]:
        '''The end time for this match (in seconds since the epoch).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#end DataAkamaiCloudletsApplicationLoadBalancerMatchRule#end}
        '''
        result = self._values.get("end")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Akamai internal use only.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#id DataAkamaiCloudletsApplicationLoadBalancerMatchRule#id}

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def matches(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatches"]]]:
        '''matches block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#matches DataAkamaiCloudletsApplicationLoadBalancerMatchRule#matches}
        '''
        result = self._values.get("matches")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatches"]]], result)

    @builtins.property
    def matches_always(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Is used in some cloudlets to support default rules (rule that is always matched).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#matches_always DataAkamaiCloudletsApplicationLoadBalancerMatchRule#matches_always}
        '''
        result = self._values.get("matches_always")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def match_url(self) -> typing.Optional[builtins.str]:
        '''If using a URL match, this property is the URL that the Cloudlet uses to match the incoming request.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#match_url DataAkamaiCloudletsApplicationLoadBalancerMatchRule#match_url}
        '''
        result = self._values.get("match_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the rule.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#name DataAkamaiCloudletsApplicationLoadBalancerMatchRule#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start(self) -> typing.Optional[jsii.Number]:
        '''The start time for this match (in seconds since the epoch).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#start DataAkamaiCloudletsApplicationLoadBalancerMatchRule#start}
        '''
        result = self._values.get("start")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsApplicationLoadBalancerMatchRule.DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesForwardSettings",
    jsii_struct_bases=[],
    name_mapping={"origin_id": "originId"},
)
class DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesForwardSettings:
    def __init__(self, *, origin_id: builtins.str) -> None:
        '''
        :param origin_id: The ID of the Conditional Origin requests are forwarded to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#origin_id DataAkamaiCloudletsApplicationLoadBalancerMatchRule#origin_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56cf88fd8ddb8dc952be8d705b9ba6df3cae520175eb50ba3e1f1ec622b5f4b1)
            check_type(argname="argument origin_id", value=origin_id, expected_type=type_hints["origin_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "origin_id": origin_id,
        }

    @builtins.property
    def origin_id(self) -> builtins.str:
        '''The ID of the Conditional Origin requests are forwarded to.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#origin_id DataAkamaiCloudletsApplicationLoadBalancerMatchRule#origin_id}
        '''
        result = self._values.get("origin_id")
        assert result is not None, "Required property 'origin_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesForwardSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesForwardSettingsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsApplicationLoadBalancerMatchRule.DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesForwardSettingsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5375a3c60b9b6f9991e90d0a4ae84edacb9c5424110376839e7c1da2731fd020)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesForwardSettingsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__851949610f68266ad92f13f82b683905a9c0974a2855915566165fd568c258fb)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesForwardSettingsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb18433643ed31b4dfb069df9e65b48cb3a02d650a468ad6b87bc325bccc2de8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__eeabf945fd16ef6c7d75e6c3823e0e9d20071142d12b0674966671d651c4f631)
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
            type_hints = typing.get_type_hints(_typecheckingstub__10ceb3c171484e96755848ccfde03a2e9ad396b1b1d9635f9980881559c7ada7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesForwardSettings]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesForwardSettings]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesForwardSettings]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__866f7cdd01682424ca69c3afb7fd5c0fb67716ad89ff31bab08f73061786fb15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesForwardSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsApplicationLoadBalancerMatchRule.DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesForwardSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c8b4df9e47ff1f1e6dbdfc0b1dc01a54292e7f2ffe5f31144795f87392404ebe)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="originIdInput")
    def origin_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "originIdInput"))

    @builtins.property
    @jsii.member(jsii_name="originId")
    def origin_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "originId"))

    @origin_id.setter
    def origin_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08ccee5e8a32835775c4ac1b6604a9635f55dea0cde60cf1b45d87f4ecb0734e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesForwardSettings]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesForwardSettings]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesForwardSettings]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fa2008e0ce3d645a143881348c4da16e13ef06016a9eac6ed7595735a662b85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsApplicationLoadBalancerMatchRule.DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4b39be2437b8d85e59b68dbbc480592506d602fe2e3dfc65dcda49727472dcf6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d827b04aeb450822bbd0cb2cf190835abca361dde1dc29b26e8c472795706be)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b80b6fab1d243b2e87130fa00ba34e930d2b8fb6ffe45961f69f75bc118edcfe)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1d53840c35d7abeca6d3c2a082ab8067ac7fcf3d019d1c3001437bb8859e90d2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__edc368e626f445a0e761236bf3874b190ed45a49867f23217d4d862b976eb1ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRules]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRules]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRules]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8239020a29c9f31c0e939a888f79286ca8a37709b41c11d0f4ab38c31c431110)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsApplicationLoadBalancerMatchRule.DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatches",
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
class DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatches:
    def __init__(
        self,
        *,
        case_sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        check_ips: typing.Optional[builtins.str] = None,
        match_operator: typing.Optional[builtins.str] = None,
        match_type: typing.Optional[builtins.str] = None,
        match_value: typing.Optional[builtins.str] = None,
        negate: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        object_match_value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValue", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param case_sensitive: If true, the match is case sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#case_sensitive DataAkamaiCloudletsApplicationLoadBalancerMatchRule#case_sensitive}
        :param check_ips: For clientip, continent, countrycode, proxy, and regioncode match types, the part of the request that determines the IP address to use. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#check_ips DataAkamaiCloudletsApplicationLoadBalancerMatchRule#check_ips}
        :param match_operator: Valid entries for this property: contains, exists, and equals. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#match_operator DataAkamaiCloudletsApplicationLoadBalancerMatchRule#match_operator}
        :param match_type: The type of match used. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#match_type DataAkamaiCloudletsApplicationLoadBalancerMatchRule#match_type}
        :param match_value: Depends on the matchType. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#match_value DataAkamaiCloudletsApplicationLoadBalancerMatchRule#match_value}
        :param negate: If true, negates the match. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#negate DataAkamaiCloudletsApplicationLoadBalancerMatchRule#negate}
        :param object_match_value: object_match_value block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#object_match_value DataAkamaiCloudletsApplicationLoadBalancerMatchRule#object_match_value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6242ee49d5af4e67e8237526f1569ac6a7831ff1b4c595934c32592fa217ed99)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#case_sensitive DataAkamaiCloudletsApplicationLoadBalancerMatchRule#case_sensitive}
        '''
        result = self._values.get("case_sensitive")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def check_ips(self) -> typing.Optional[builtins.str]:
        '''For clientip, continent, countrycode, proxy, and regioncode match types, the part of the request that determines the IP address to use.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#check_ips DataAkamaiCloudletsApplicationLoadBalancerMatchRule#check_ips}
        '''
        result = self._values.get("check_ips")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_operator(self) -> typing.Optional[builtins.str]:
        '''Valid entries for this property: contains, exists, and equals.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#match_operator DataAkamaiCloudletsApplicationLoadBalancerMatchRule#match_operator}
        '''
        result = self._values.get("match_operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_type(self) -> typing.Optional[builtins.str]:
        '''The type of match used.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#match_type DataAkamaiCloudletsApplicationLoadBalancerMatchRule#match_type}
        '''
        result = self._values.get("match_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_value(self) -> typing.Optional[builtins.str]:
        '''Depends on the matchType.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#match_value DataAkamaiCloudletsApplicationLoadBalancerMatchRule#match_value}
        '''
        result = self._values.get("match_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def negate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If true, negates the match.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#negate DataAkamaiCloudletsApplicationLoadBalancerMatchRule#negate}
        '''
        result = self._values.get("negate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def object_match_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValue"]]]:
        '''object_match_value block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#object_match_value DataAkamaiCloudletsApplicationLoadBalancerMatchRule#object_match_value}
        '''
        result = self._values.get("object_match_value")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValue"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatches(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsApplicationLoadBalancerMatchRule.DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__168f8b8b5a0de8410926a7c3392c26af466e2f7ed32095920b95d53e6a884fb6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4aaf55078d547ca1cb48b2231ddc60e7765487a6fca152b79494ec4259f7b435)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fcff4abbad8ba06c2e0f1b6aa6bea2b778ad25a21ba046684b193db67ec78e9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5a2eb4af8ae44b669e8a680caa4d775607533426bbdb0f0875be711f640d5549)
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
            type_hints = typing.get_type_hints(_typecheckingstub__60217103ce8397b1642662edd517a02785fabad24e11076d826cc40c5089ca41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatches]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatches]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatches]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb63c99b227ccb7d997dc21d13741c4b714f6872cb8ae0f70837656e5458be62)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsApplicationLoadBalancerMatchRule.DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValue",
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
class DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValue:
    def __init__(
        self,
        *,
        type: builtins.str,
        name: typing.Optional[builtins.str] = None,
        name_case_sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        name_has_wildcard: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        options: typing.Optional[typing.Union["DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValueOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        value: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: The array type, which can be one of the following: object, range, or simple. Use the simple option when adding only an array of string-based values Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#type DataAkamaiCloudletsApplicationLoadBalancerMatchRule#type}
        :param name: If using a match type that supports name attributes, enter the value in the incoming request to match on. The following match types support this property: cookie, header, parameter, and query Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#name DataAkamaiCloudletsApplicationLoadBalancerMatchRule#name}
        :param name_case_sensitive: Set to true if the entry for the name property should be evaluated based on case sensitivity. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#name_case_sensitive DataAkamaiCloudletsApplicationLoadBalancerMatchRule#name_case_sensitive}
        :param name_has_wildcard: Set to true if the entry for the name property includes wildcards. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#name_has_wildcard DataAkamaiCloudletsApplicationLoadBalancerMatchRule#name_has_wildcard}
        :param options: options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#options DataAkamaiCloudletsApplicationLoadBalancerMatchRule#options}
        :param value: The value attributes in the incoming request to match on (use only with simple or range type). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#value DataAkamaiCloudletsApplicationLoadBalancerMatchRule#value}
        '''
        if isinstance(options, dict):
            options = DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValueOptions(**options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b234087a17f79d216e1a36c6aafc6dc662da937719f68a89a029f682e0f5e5a9)
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
        '''The array type, which can be one of the following: object, range, or simple.

        Use the simple option when adding only an array of string-based values

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#type DataAkamaiCloudletsApplicationLoadBalancerMatchRule#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''If using a match type that supports name attributes, enter the value in the incoming request to match on.

        The following match types support this property: cookie, header, parameter, and query

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#name DataAkamaiCloudletsApplicationLoadBalancerMatchRule#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name_case_sensitive(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set to true if the entry for the name property should be evaluated based on case sensitivity.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#name_case_sensitive DataAkamaiCloudletsApplicationLoadBalancerMatchRule#name_case_sensitive}
        '''
        result = self._values.get("name_case_sensitive")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def name_has_wildcard(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set to true if the entry for the name property includes wildcards.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#name_has_wildcard DataAkamaiCloudletsApplicationLoadBalancerMatchRule#name_has_wildcard}
        '''
        result = self._values.get("name_has_wildcard")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def options(
        self,
    ) -> typing.Optional["DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValueOptions"]:
        '''options block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#options DataAkamaiCloudletsApplicationLoadBalancerMatchRule#options}
        '''
        result = self._values.get("options")
        return typing.cast(typing.Optional["DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValueOptions"], result)

    @builtins.property
    def value(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The value attributes in the incoming request to match on (use only with simple or range type).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#value DataAkamaiCloudletsApplicationLoadBalancerMatchRule#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValueList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsApplicationLoadBalancerMatchRule.DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValueList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3f9e55d0868abdc21a3bd1ebf06fd9a3cdc2b3e95a17d3021f1bb70bdf38895c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValueOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2bfbc8214a8e63aceef91adb5addb938a0a40e7fa0c7d5409cabe137f17ee4f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValueOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c6e819621a87d428133bcb97d8066ad4834fe3c65693066843c3e2dabecb168)
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
            type_hints = typing.get_type_hints(_typecheckingstub__befd097dec6d0f776ba0608c04ab0d7e3fd73d7ea46044eb59e94888648b6c2f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5b01c65b65f5fda817ec8e0c984dfc18f719d24e13ad7d470e4849f90a23eead)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValue]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValue]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValue]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03b2af11fd6a037a0b8e3d9a84438de6bcb1b687fc26a1daf084f86382f1959e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsApplicationLoadBalancerMatchRule.DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValueOptions",
    jsii_struct_bases=[],
    name_mapping={
        "value": "value",
        "value_case_sensitive": "valueCaseSensitive",
        "value_escaped": "valueEscaped",
        "value_has_wildcard": "valueHasWildcard",
    },
)
class DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValueOptions:
    def __init__(
        self,
        *,
        value: typing.Optional[typing.Sequence[builtins.str]] = None,
        value_case_sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        value_escaped: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        value_has_wildcard: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param value: The value attributes in the incoming request to match on. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#value DataAkamaiCloudletsApplicationLoadBalancerMatchRule#value}
        :param value_case_sensitive: Set to true if the entries for the value property should be evaluated based on case sensitivity. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#value_case_sensitive DataAkamaiCloudletsApplicationLoadBalancerMatchRule#value_case_sensitive}
        :param value_escaped: Set to true if provided value should be compared in escaped form. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#value_escaped DataAkamaiCloudletsApplicationLoadBalancerMatchRule#value_escaped}
        :param value_has_wildcard: Set to true if the entries for the value property include wildcards. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#value_has_wildcard DataAkamaiCloudletsApplicationLoadBalancerMatchRule#value_has_wildcard}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7c9b0df4234bd35425d88efd99db3f28029466d02e9e00596d78216a85d62fb)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#value DataAkamaiCloudletsApplicationLoadBalancerMatchRule#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def value_case_sensitive(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set to true if the entries for the value property should be evaluated based on case sensitivity.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#value_case_sensitive DataAkamaiCloudletsApplicationLoadBalancerMatchRule#value_case_sensitive}
        '''
        result = self._values.get("value_case_sensitive")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def value_escaped(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set to true if provided value should be compared in escaped form.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#value_escaped DataAkamaiCloudletsApplicationLoadBalancerMatchRule#value_escaped}
        '''
        result = self._values.get("value_escaped")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def value_has_wildcard(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set to true if the entries for the value property include wildcards.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#value_has_wildcard DataAkamaiCloudletsApplicationLoadBalancerMatchRule#value_has_wildcard}
        '''
        result = self._values.get("value_has_wildcard")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValueOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValueOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsApplicationLoadBalancerMatchRule.DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValueOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__05f7eb4a80560fcb99d0e660c8d18af1ba3b6b60414c45dc8483421e3d438b19)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ac1bf71e21dd87fa756822f374749466810973a2d7fdd3a0a71746fa9ed77dfe)
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
            type_hints = typing.get_type_hints(_typecheckingstub__70891f59b46e27ad49be038152270ec0baf1f72412dd41f85694aefbfb4fa55a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5dda464283f6d18d185a45d67aa404232be9aa56856cf6ad4db0e7defb82e8ae)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e303422055d4c9c5e2a12d29ffd8948e01ab6705b258dc592f79a86eb0e84abd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "valueHasWildcard", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValueOptions]:
        return typing.cast(typing.Optional[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValueOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValueOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44812387d2523cb19140c1988f234406d1372035ff5e8da20f6faa409ed71718)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValueOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsApplicationLoadBalancerMatchRule.DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValueOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__12dd7ded273f69dac4c8d566e48fa2e7adae074e5eb6739614aaffa3d05d0b1d)
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
        :param value: The value attributes in the incoming request to match on. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#value DataAkamaiCloudletsApplicationLoadBalancerMatchRule#value}
        :param value_case_sensitive: Set to true if the entries for the value property should be evaluated based on case sensitivity. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#value_case_sensitive DataAkamaiCloudletsApplicationLoadBalancerMatchRule#value_case_sensitive}
        :param value_escaped: Set to true if provided value should be compared in escaped form. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#value_escaped DataAkamaiCloudletsApplicationLoadBalancerMatchRule#value_escaped}
        :param value_has_wildcard: Set to true if the entries for the value property include wildcards. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_application_load_balancer_match_rule#value_has_wildcard DataAkamaiCloudletsApplicationLoadBalancerMatchRule#value_has_wildcard}
        '''
        value_ = DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValueOptions(
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
    ) -> DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValueOptionsOutputReference:
        return typing.cast(DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValueOptionsOutputReference, jsii.get(self, "options"))

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
    ) -> typing.Optional[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValueOptions]:
        return typing.cast(typing.Optional[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValueOptions], jsii.get(self, "optionsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__ee3cae38f1f3286b8d5c3ad5e2e0f6e62ee92e456bfbc0aef2b66c86f88c81f1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4f7cb2fa406491b7d21413f9e8f13b4dd29b4e0fb587682f4641f5100a2230c7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0285ca26c9c7dc61759cecf6552c14fa550b06aec389eeed384306565845b82b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nameHasWildcard", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0de12a91d62a99169ef004ce0278caa5e8ee0f0acbf8fab4897e494e16367a99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "value"))

    @value.setter
    def value(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9538fe8f8373616b42374f8e7eebe7a061f36ceba0a5425d4580205014ddd0f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValue]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValue]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValue]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59434da7ca825ea537dd4374b12da9725453c0b4cdbd037a0d0f11593d11c888)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsApplicationLoadBalancerMatchRule.DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ab1173ddafc99084d8671ff88e42316ce81b4bd18b853208a3849ac0fa84c54e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putObjectMatchValue")
    def put_object_match_value(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValue, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c7540ad755500f828c285e1fb7ca0f596ad772f12a658cbe160e45da469509b)
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
    ) -> DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValueList:
        return typing.cast(DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValueList, jsii.get(self, "objectMatchValue"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValue]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValue]]], jsii.get(self, "objectMatchValueInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__0907eab55624fb39da0f241db96ccea0aaea0f150f16699a9c7cbb1351c328a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caseSensitive", value)

    @builtins.property
    @jsii.member(jsii_name="checkIps")
    def check_ips(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "checkIps"))

    @check_ips.setter
    def check_ips(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9d7fd195feceafc4c4cc5f00fbffae6c156650f204679ba398c9cc0978f9628)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "checkIps", value)

    @builtins.property
    @jsii.member(jsii_name="matchOperator")
    def match_operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchOperator"))

    @match_operator.setter
    def match_operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e61388cbcd9f0b0f970c6ebbc538ebae7ae7cbe07e0f9955621c9baf956aff6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOperator", value)

    @builtins.property
    @jsii.member(jsii_name="matchType")
    def match_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchType"))

    @match_type.setter
    def match_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72d4845531a8608c8d1cab925a2a4a93e9294b617b71d73a3904edfe20aa5673)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchType", value)

    @builtins.property
    @jsii.member(jsii_name="matchValue")
    def match_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchValue"))

    @match_value.setter
    def match_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3848c7c5e1fded1fb695107b809769a8cf1bd0fbe544e03d293806c747944ac8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e473729cfbb181173cadafe1eda99ef171fd6264a8fc6988662c7bda32a5a9dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatches]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatches]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatches]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b76be01ea06d2f9447c42c3af6554427fc293eeba7c85724cc9d7b6b153eb12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsApplicationLoadBalancerMatchRule.DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a86b2c1831e01aa9a5c97fcc9dd0995bb340932a3a4c76c377389af3888807bc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putForwardSettings")
    def put_forward_settings(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesForwardSettings, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c959eeab138e1ac8c078b3c1c8c32bb56861c409dd696c6a2725a810d8fdde7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putForwardSettings", [value]))

    @jsii.member(jsii_name="putMatches")
    def put_matches(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatches, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__458fbc59abb4dcbfcb810753aa4a1d32764532f769088f830239324f7033db08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatches", [value]))

    @jsii.member(jsii_name="resetDisabled")
    def reset_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisabled", []))

    @jsii.member(jsii_name="resetEnd")
    def reset_end(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnd", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMatches")
    def reset_matches(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatches", []))

    @jsii.member(jsii_name="resetMatchesAlways")
    def reset_matches_always(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchesAlways", []))

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
    ) -> DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesForwardSettingsList:
        return typing.cast(DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesForwardSettingsList, jsii.get(self, "forwardSettings"))

    @builtins.property
    @jsii.member(jsii_name="matches")
    def matches(
        self,
    ) -> DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesList:
        return typing.cast(DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesList, jsii.get(self, "matches"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesForwardSettings]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesForwardSettings]]], jsii.get(self, "forwardSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idInput"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatches]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatches]]], jsii.get(self, "matchesInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__506aca10056846737f6de00325cae1c77c8bd4ae555891211a7470ed789e1721)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabled", value)

    @builtins.property
    @jsii.member(jsii_name="end")
    def end(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "end"))

    @end.setter
    def end(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30e16bfa76555c66c832bc027e6194db21509e1ea425a25c3a4389df2da25298)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "end", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "id"))

    @id.setter
    def id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7150c98afde1f248cdb9df2b31abe5d6373a5cba86e6c52e735bdc5a79b33dfc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__82b96748f4f74d31e9cb10875d58b932c63b2a9d318691a3d7a32e7c3469e96e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchesAlways", value)

    @builtins.property
    @jsii.member(jsii_name="matchUrl")
    def match_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchUrl"))

    @match_url.setter
    def match_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99dd40a59a785ebd4b8da161b2eebfa578aa3beaf462d1f688692e391e42fc6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchUrl", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51a94f41cf63f7d0d8932157048130960c81802b654e0bcc2f730745b6795e09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="start")
    def start(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "start"))

    @start.setter
    def start(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__455a442b542b3c7f7d92a81c5a1e9e0db98ad447b521fab6ce8d896536b1d9a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "start", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRules]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRules]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRules]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d05c269bdc4bd6c22f334ce554cd712641b43553cd6b18228ed6685b14c6888)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataAkamaiCloudletsApplicationLoadBalancerMatchRule",
    "DataAkamaiCloudletsApplicationLoadBalancerMatchRuleConfig",
    "DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRules",
    "DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesForwardSettings",
    "DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesForwardSettingsList",
    "DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesForwardSettingsOutputReference",
    "DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesList",
    "DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatches",
    "DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesList",
    "DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValue",
    "DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValueList",
    "DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValueOptions",
    "DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValueOptionsOutputReference",
    "DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValueOutputReference",
    "DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesOutputReference",
    "DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesOutputReference",
]

publication.publish()

def _typecheckingstub__1772c11a86aae8a0485884f54f5d2a9447f7171f588e574db9ed291514a2c399(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    id: typing.Optional[builtins.str] = None,
    match_rules: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRules, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__c47c5db7f777c6d0884e9dc9dec32b87d7d28bc120723c53412faf844249450c(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__445105dade110916e45d87429ce10616698e696c83ca8e9b12930831a588f8d7(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRules, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf28c77404a00a1907e8c589b9a5b5ff1b9772f285c4f0c1d8593077cde370e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4cda175ee9f7087f1a03edbff3cca49450d1b63d05b20b9b1771f423ef2446a(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    match_rules: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRules, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07e08f624dad9e1a1ab379da6ec5bf77de9d3e3f49131e0f98e32f20b9f2adbe(
    *,
    forward_settings: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesForwardSettings, typing.Dict[builtins.str, typing.Any]]]],
    disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    end: typing.Optional[jsii.Number] = None,
    id: typing.Optional[jsii.Number] = None,
    matches: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatches, typing.Dict[builtins.str, typing.Any]]]]] = None,
    matches_always: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    match_url: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    start: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56cf88fd8ddb8dc952be8d705b9ba6df3cae520175eb50ba3e1f1ec622b5f4b1(
    *,
    origin_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5375a3c60b9b6f9991e90d0a4ae84edacb9c5424110376839e7c1da2731fd020(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__851949610f68266ad92f13f82b683905a9c0974a2855915566165fd568c258fb(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb18433643ed31b4dfb069df9e65b48cb3a02d650a468ad6b87bc325bccc2de8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eeabf945fd16ef6c7d75e6c3823e0e9d20071142d12b0674966671d651c4f631(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10ceb3c171484e96755848ccfde03a2e9ad396b1b1d9635f9980881559c7ada7(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__866f7cdd01682424ca69c3afb7fd5c0fb67716ad89ff31bab08f73061786fb15(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesForwardSettings]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8b4df9e47ff1f1e6dbdfc0b1dc01a54292e7f2ffe5f31144795f87392404ebe(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08ccee5e8a32835775c4ac1b6604a9635f55dea0cde60cf1b45d87f4ecb0734e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fa2008e0ce3d645a143881348c4da16e13ef06016a9eac6ed7595735a662b85(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesForwardSettings]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b39be2437b8d85e59b68dbbc480592506d602fe2e3dfc65dcda49727472dcf6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d827b04aeb450822bbd0cb2cf190835abca361dde1dc29b26e8c472795706be(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b80b6fab1d243b2e87130fa00ba34e930d2b8fb6ffe45961f69f75bc118edcfe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d53840c35d7abeca6d3c2a082ab8067ac7fcf3d019d1c3001437bb8859e90d2(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edc368e626f445a0e761236bf3874b190ed45a49867f23217d4d862b976eb1ed(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8239020a29c9f31c0e939a888f79286ca8a37709b41c11d0f4ab38c31c431110(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRules]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6242ee49d5af4e67e8237526f1569ac6a7831ff1b4c595934c32592fa217ed99(
    *,
    case_sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    check_ips: typing.Optional[builtins.str] = None,
    match_operator: typing.Optional[builtins.str] = None,
    match_type: typing.Optional[builtins.str] = None,
    match_value: typing.Optional[builtins.str] = None,
    negate: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    object_match_value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValue, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__168f8b8b5a0de8410926a7c3392c26af466e2f7ed32095920b95d53e6a884fb6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4aaf55078d547ca1cb48b2231ddc60e7765487a6fca152b79494ec4259f7b435(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fcff4abbad8ba06c2e0f1b6aa6bea2b778ad25a21ba046684b193db67ec78e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a2eb4af8ae44b669e8a680caa4d775607533426bbdb0f0875be711f640d5549(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60217103ce8397b1642662edd517a02785fabad24e11076d826cc40c5089ca41(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb63c99b227ccb7d997dc21d13741c4b714f6872cb8ae0f70837656e5458be62(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatches]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b234087a17f79d216e1a36c6aafc6dc662da937719f68a89a029f682e0f5e5a9(
    *,
    type: builtins.str,
    name: typing.Optional[builtins.str] = None,
    name_case_sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    name_has_wildcard: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    options: typing.Optional[typing.Union[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValueOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    value: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f9e55d0868abdc21a3bd1ebf06fd9a3cdc2b3e95a17d3021f1bb70bdf38895c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2bfbc8214a8e63aceef91adb5addb938a0a40e7fa0c7d5409cabe137f17ee4f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c6e819621a87d428133bcb97d8066ad4834fe3c65693066843c3e2dabecb168(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__befd097dec6d0f776ba0608c04ab0d7e3fd73d7ea46044eb59e94888648b6c2f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b01c65b65f5fda817ec8e0c984dfc18f719d24e13ad7d470e4849f90a23eead(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03b2af11fd6a037a0b8e3d9a84438de6bcb1b687fc26a1daf084f86382f1959e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValue]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7c9b0df4234bd35425d88efd99db3f28029466d02e9e00596d78216a85d62fb(
    *,
    value: typing.Optional[typing.Sequence[builtins.str]] = None,
    value_case_sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    value_escaped: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    value_has_wildcard: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05f7eb4a80560fcb99d0e660c8d18af1ba3b6b60414c45dc8483421e3d438b19(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac1bf71e21dd87fa756822f374749466810973a2d7fdd3a0a71746fa9ed77dfe(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70891f59b46e27ad49be038152270ec0baf1f72412dd41f85694aefbfb4fa55a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dda464283f6d18d185a45d67aa404232be9aa56856cf6ad4db0e7defb82e8ae(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e303422055d4c9c5e2a12d29ffd8948e01ab6705b258dc592f79a86eb0e84abd(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44812387d2523cb19140c1988f234406d1372035ff5e8da20f6faa409ed71718(
    value: typing.Optional[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValueOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12dd7ded273f69dac4c8d566e48fa2e7adae074e5eb6739614aaffa3d05d0b1d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee3cae38f1f3286b8d5c3ad5e2e0f6e62ee92e456bfbc0aef2b66c86f88c81f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f7cb2fa406491b7d21413f9e8f13b4dd29b4e0fb587682f4641f5100a2230c7(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0285ca26c9c7dc61759cecf6552c14fa550b06aec389eeed384306565845b82b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0de12a91d62a99169ef004ce0278caa5e8ee0f0acbf8fab4897e494e16367a99(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9538fe8f8373616b42374f8e7eebe7a061f36ceba0a5425d4580205014ddd0f4(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59434da7ca825ea537dd4374b12da9725453c0b4cdbd037a0d0f11593d11c888(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValue]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab1173ddafc99084d8671ff88e42316ce81b4bd18b853208a3849ac0fa84c54e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c7540ad755500f828c285e1fb7ca0f596ad772f12a658cbe160e45da469509b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatchesObjectMatchValue, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0907eab55624fb39da0f241db96ccea0aaea0f150f16699a9c7cbb1351c328a8(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9d7fd195feceafc4c4cc5f00fbffae6c156650f204679ba398c9cc0978f9628(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e61388cbcd9f0b0f970c6ebbc538ebae7ae7cbe07e0f9955621c9baf956aff6b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72d4845531a8608c8d1cab925a2a4a93e9294b617b71d73a3904edfe20aa5673(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3848c7c5e1fded1fb695107b809769a8cf1bd0fbe544e03d293806c747944ac8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e473729cfbb181173cadafe1eda99ef171fd6264a8fc6988662c7bda32a5a9dd(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b76be01ea06d2f9447c42c3af6554427fc293eeba7c85724cc9d7b6b153eb12(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatches]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a86b2c1831e01aa9a5c97fcc9dd0995bb340932a3a4c76c377389af3888807bc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c959eeab138e1ac8c078b3c1c8c32bb56861c409dd696c6a2725a810d8fdde7(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesForwardSettings, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__458fbc59abb4dcbfcb810753aa4a1d32764532f769088f830239324f7033db08(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRulesMatches, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__506aca10056846737f6de00325cae1c77c8bd4ae555891211a7470ed789e1721(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30e16bfa76555c66c832bc027e6194db21509e1ea425a25c3a4389df2da25298(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7150c98afde1f248cdb9df2b31abe5d6373a5cba86e6c52e735bdc5a79b33dfc(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82b96748f4f74d31e9cb10875d58b932c63b2a9d318691a3d7a32e7c3469e96e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99dd40a59a785ebd4b8da161b2eebfa578aa3beaf462d1f688692e391e42fc6a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51a94f41cf63f7d0d8932157048130960c81802b654e0bcc2f730745b6795e09(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__455a442b542b3c7f7d92a81c5a1e9e0db98ad447b521fab6ce8d896536b1d9a1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d05c269bdc4bd6c22f334ce554cd712641b43553cd6b18228ed6685b14c6888(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsApplicationLoadBalancerMatchRuleMatchRules]],
) -> None:
    """Type checking stubs"""
    pass
