'''
# `data_akamai_cloudlets_audience_segmentation_match_rule`

Refer to the Terraform Registry for docs: [`data_akamai_cloudlets_audience_segmentation_match_rule`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule).
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


class DataAkamaiCloudletsAudienceSegmentationMatchRule(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsAudienceSegmentationMatchRule.DataAkamaiCloudletsAudienceSegmentationMatchRule",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule akamai_cloudlets_audience_segmentation_match_rule}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        id: typing.Optional[builtins.str] = None,
        match_rules: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRules", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule akamai_cloudlets_audience_segmentation_match_rule} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#id DataAkamaiCloudletsAudienceSegmentationMatchRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param match_rules: match_rules block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#match_rules DataAkamaiCloudletsAudienceSegmentationMatchRule#match_rules}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eda019cddb44f3975a16f10b1e7951fcea874b7529e19c059fa1297f3f1acff2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAkamaiCloudletsAudienceSegmentationMatchRuleConfig(
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
        '''Generates CDKTF code for importing a DataAkamaiCloudletsAudienceSegmentationMatchRule resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the DataAkamaiCloudletsAudienceSegmentationMatchRule to import.
        :param import_from_id: The id of the existing DataAkamaiCloudletsAudienceSegmentationMatchRule that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the DataAkamaiCloudletsAudienceSegmentationMatchRule to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aaff018869fefe947c30498a0ec45e3a264e4111ec41edebecc038f551e69ad3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putMatchRules")
    def put_match_rules(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRules", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3328235ef0ea082a588db222405fc5e77ea3bfbc01fbc84ad591a914cfa0228b)
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
    ) -> "DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesList":
        return typing.cast("DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesList", jsii.get(self, "matchRules"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="matchRulesInput")
    def match_rules_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRules"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRules"]]], jsii.get(self, "matchRulesInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fac3ca4dcfc9a5c54d075d68c92fc8ea6ab8f5e1e0dacda46da16db0dd5a7b63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsAudienceSegmentationMatchRule.DataAkamaiCloudletsAudienceSegmentationMatchRuleConfig",
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
class DataAkamaiCloudletsAudienceSegmentationMatchRuleConfig(
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
        match_rules: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRules", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#id DataAkamaiCloudletsAudienceSegmentationMatchRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param match_rules: match_rules block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#match_rules DataAkamaiCloudletsAudienceSegmentationMatchRule#match_rules}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e26b411686e85f6ac096f8210b7fd652f60b31ae49a0b5cfcc539c7e85432faf)
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
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#id DataAkamaiCloudletsAudienceSegmentationMatchRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_rules(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRules"]]]:
        '''match_rules block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#match_rules DataAkamaiCloudletsAudienceSegmentationMatchRule#match_rules}
        '''
        result = self._values.get("match_rules")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRules"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsAudienceSegmentationMatchRuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsAudienceSegmentationMatchRule.DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRules",
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
class DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRules:
    def __init__(
        self,
        *,
        forward_settings: typing.Union["DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesForwardSettings", typing.Dict[builtins.str, typing.Any]],
        disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        end: typing.Optional[jsii.Number] = None,
        matches: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatches", typing.Dict[builtins.str, typing.Any]]]]] = None,
        match_url: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        start: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param forward_settings: forward_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#forward_settings DataAkamaiCloudletsAudienceSegmentationMatchRule#forward_settings}
        :param disabled: If set to true, disables a rule so it is not evaluated against incoming requests. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#disabled DataAkamaiCloudletsAudienceSegmentationMatchRule#disabled}
        :param end: The end time for this match (in seconds since the epoch). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#end DataAkamaiCloudletsAudienceSegmentationMatchRule#end}
        :param matches: matches block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#matches DataAkamaiCloudletsAudienceSegmentationMatchRule#matches}
        :param match_url: If using a URL match, this property is the URL that the Cloudlet uses to match the incoming request. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#match_url DataAkamaiCloudletsAudienceSegmentationMatchRule#match_url}
        :param name: The name of the rule. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#name DataAkamaiCloudletsAudienceSegmentationMatchRule#name}
        :param start: The start time for this match (in seconds since the epoch). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#start DataAkamaiCloudletsAudienceSegmentationMatchRule#start}
        '''
        if isinstance(forward_settings, dict):
            forward_settings = DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesForwardSettings(**forward_settings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e6a5a4a538ef2bd31d781ec7e8c8d7993dbe5dcc47fccacde89317796fa561a)
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
    ) -> "DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesForwardSettings":
        '''forward_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#forward_settings DataAkamaiCloudletsAudienceSegmentationMatchRule#forward_settings}
        '''
        result = self._values.get("forward_settings")
        assert result is not None, "Required property 'forward_settings' is missing"
        return typing.cast("DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesForwardSettings", result)

    @builtins.property
    def disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If set to true, disables a rule so it is not evaluated against incoming requests.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#disabled DataAkamaiCloudletsAudienceSegmentationMatchRule#disabled}
        '''
        result = self._values.get("disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def end(self) -> typing.Optional[jsii.Number]:
        '''The end time for this match (in seconds since the epoch).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#end DataAkamaiCloudletsAudienceSegmentationMatchRule#end}
        '''
        result = self._values.get("end")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def matches(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatches"]]]:
        '''matches block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#matches DataAkamaiCloudletsAudienceSegmentationMatchRule#matches}
        '''
        result = self._values.get("matches")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatches"]]], result)

    @builtins.property
    def match_url(self) -> typing.Optional[builtins.str]:
        '''If using a URL match, this property is the URL that the Cloudlet uses to match the incoming request.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#match_url DataAkamaiCloudletsAudienceSegmentationMatchRule#match_url}
        '''
        result = self._values.get("match_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the rule.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#name DataAkamaiCloudletsAudienceSegmentationMatchRule#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start(self) -> typing.Optional[jsii.Number]:
        '''The start time for this match (in seconds since the epoch).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#start DataAkamaiCloudletsAudienceSegmentationMatchRule#start}
        '''
        result = self._values.get("start")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsAudienceSegmentationMatchRule.DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesForwardSettings",
    jsii_struct_bases=[],
    name_mapping={
        "origin_id": "originId",
        "path_and_qs": "pathAndQs",
        "use_incoming_query_string": "useIncomingQueryString",
    },
)
class DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesForwardSettings:
    def __init__(
        self,
        *,
        origin_id: typing.Optional[builtins.str] = None,
        path_and_qs: typing.Optional[builtins.str] = None,
        use_incoming_query_string: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param origin_id: The ID of the Conditional Origin requests are forwarded to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#origin_id DataAkamaiCloudletsAudienceSegmentationMatchRule#origin_id}
        :param path_and_qs: If a value is provided and match conditions are met, this property defines the path/resource/query string to rewrite URL for the incoming request. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#path_and_qs DataAkamaiCloudletsAudienceSegmentationMatchRule#path_and_qs}
        :param use_incoming_query_string: If set to true, the Cloudlet includes the query string from the request in the rewritten or forwarded URL. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#use_incoming_query_string DataAkamaiCloudletsAudienceSegmentationMatchRule#use_incoming_query_string}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec18aefda4bd081fb30668dfc9a60adc1690932024321bb19a46aee7081ed818)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#origin_id DataAkamaiCloudletsAudienceSegmentationMatchRule#origin_id}
        '''
        result = self._values.get("origin_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path_and_qs(self) -> typing.Optional[builtins.str]:
        '''If a value is provided and match conditions are met, this property defines the path/resource/query string to rewrite URL for the incoming request.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#path_and_qs DataAkamaiCloudletsAudienceSegmentationMatchRule#path_and_qs}
        '''
        result = self._values.get("path_and_qs")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_incoming_query_string(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If set to true, the Cloudlet includes the query string from the request in the rewritten or forwarded URL.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#use_incoming_query_string DataAkamaiCloudletsAudienceSegmentationMatchRule#use_incoming_query_string}
        '''
        result = self._values.get("use_incoming_query_string")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesForwardSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesForwardSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsAudienceSegmentationMatchRule.DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesForwardSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cc974f09bd63948355c40429e70ec7b9aead8dc54847aefd882a92d06e9b1226)
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
            type_hints = typing.get_type_hints(_typecheckingstub__35ffda61d97030ee2fb83badd809a8ca8e2d87e319d69af9087f95dac97c7cc1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originId", value)

    @builtins.property
    @jsii.member(jsii_name="pathAndQs")
    def path_and_qs(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pathAndQs"))

    @path_and_qs.setter
    def path_and_qs(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ed22ef9fb01e48d4ed15daa955b4f273a06bf074027f9ed42573eed7f7add50)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9525bb12e2733efe6a81b92ae87f8d8581bfd1ac9ca85588f39404ff523b5312)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useIncomingQueryString", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesForwardSettings]:
        return typing.cast(typing.Optional[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesForwardSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesForwardSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__166dcea6ace97de9dace2c2e81f68e32792d81e3feee8ab748e9306746a719ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsAudienceSegmentationMatchRule.DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e70eea68d3088300d6634ed1a9a9c096afac1499a4ac4047fc38e30e66de37a9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc04c9c4fa6cc351738b2d8fc9c804ec573aaf3781bd0d41bb7e4fb3946babae)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__792b289d63fff275b78cbb11e13f97265f58b4483094121563ac58424f344c7c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b9aa6b8fdd0e95e04c92cc685027bc8f31df6a59f30d5bb3e6393f283f24efe7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a904169b4cbc919366e6555868fab8ba8cb614b53c5cf6281ce4b6fc4bc57b19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRules]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRules]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRules]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26a751d79b06923679ab28947c390dfd7d88a5887b46555298085ea9d0404c67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsAudienceSegmentationMatchRule.DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatches",
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
class DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatches:
    def __init__(
        self,
        *,
        case_sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        check_ips: typing.Optional[builtins.str] = None,
        match_operator: typing.Optional[builtins.str] = None,
        match_type: typing.Optional[builtins.str] = None,
        match_value: typing.Optional[builtins.str] = None,
        negate: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        object_match_value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValue", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param case_sensitive: If true, the match is case sensitive. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#case_sensitive DataAkamaiCloudletsAudienceSegmentationMatchRule#case_sensitive}
        :param check_ips: For clientip, continent, countrycode, proxy, and regioncode match types, the part of the request that determines the IP address to use. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#check_ips DataAkamaiCloudletsAudienceSegmentationMatchRule#check_ips}
        :param match_operator: Valid entries for this property: contains, exists, and equals. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#match_operator DataAkamaiCloudletsAudienceSegmentationMatchRule#match_operator}
        :param match_type: The type of match used. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#match_type DataAkamaiCloudletsAudienceSegmentationMatchRule#match_type}
        :param match_value: Depends on the matchType. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#match_value DataAkamaiCloudletsAudienceSegmentationMatchRule#match_value}
        :param negate: If true, negates the match. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#negate DataAkamaiCloudletsAudienceSegmentationMatchRule#negate}
        :param object_match_value: object_match_value block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#object_match_value DataAkamaiCloudletsAudienceSegmentationMatchRule#object_match_value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9575e11ba6bd8158a60206918820e05cec46c82a0dba25002c7f4663869c77b7)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#case_sensitive DataAkamaiCloudletsAudienceSegmentationMatchRule#case_sensitive}
        '''
        result = self._values.get("case_sensitive")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def check_ips(self) -> typing.Optional[builtins.str]:
        '''For clientip, continent, countrycode, proxy, and regioncode match types, the part of the request that determines the IP address to use.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#check_ips DataAkamaiCloudletsAudienceSegmentationMatchRule#check_ips}
        '''
        result = self._values.get("check_ips")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_operator(self) -> typing.Optional[builtins.str]:
        '''Valid entries for this property: contains, exists, and equals.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#match_operator DataAkamaiCloudletsAudienceSegmentationMatchRule#match_operator}
        '''
        result = self._values.get("match_operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_type(self) -> typing.Optional[builtins.str]:
        '''The type of match used.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#match_type DataAkamaiCloudletsAudienceSegmentationMatchRule#match_type}
        '''
        result = self._values.get("match_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_value(self) -> typing.Optional[builtins.str]:
        '''Depends on the matchType.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#match_value DataAkamaiCloudletsAudienceSegmentationMatchRule#match_value}
        '''
        result = self._values.get("match_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def negate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If true, negates the match.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#negate DataAkamaiCloudletsAudienceSegmentationMatchRule#negate}
        '''
        result = self._values.get("negate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def object_match_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValue"]]]:
        '''object_match_value block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#object_match_value DataAkamaiCloudletsAudienceSegmentationMatchRule#object_match_value}
        '''
        result = self._values.get("object_match_value")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValue"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatches(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsAudienceSegmentationMatchRule.DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1e9739527b7cc5156d6a2ea97ec0237c8271e6e7235f5a757e9c37000006e01e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3796023ae1f2cdc5d6e87288ce76ed7068e66d78352e67ca6232fd9007538eea)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3092f82d2820adc16b34c76074746f7b7d0b9a213cbc8c155700e25b8dc73ff)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3fd69438ea26b74efd3acdeec027d3576af322d7a0a95130cf586a05b497f73e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__171e7c57e84ff8d650aa6903423cbbe287800666fb88a42d6d0f704730075df8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatches]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatches]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatches]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f5b0f2e925888efa21c662624f01f5d9e5f26642522f3ed89eb0614bb976a08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsAudienceSegmentationMatchRule.DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValue",
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
class DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValue:
    def __init__(
        self,
        *,
        type: builtins.str,
        name: typing.Optional[builtins.str] = None,
        name_case_sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        name_has_wildcard: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        options: typing.Optional[typing.Union["DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValueOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        value: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: The array type, which can be one of the following: object or simple or range. Use the simple option when adding only an array of string-based values Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#type DataAkamaiCloudletsAudienceSegmentationMatchRule#type}
        :param name: If using a match type that supports name attributes, enter the value in the incoming request to match on. The following match types support this property: cookie, header, parameter, and query Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#name DataAkamaiCloudletsAudienceSegmentationMatchRule#name}
        :param name_case_sensitive: Set to true if the entry for the name property should be evaluated based on case sensitivity. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#name_case_sensitive DataAkamaiCloudletsAudienceSegmentationMatchRule#name_case_sensitive}
        :param name_has_wildcard: Set to true if the entry for the name property includes wildcards. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#name_has_wildcard DataAkamaiCloudletsAudienceSegmentationMatchRule#name_has_wildcard}
        :param options: options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#options DataAkamaiCloudletsAudienceSegmentationMatchRule#options}
        :param value: The value attributes in the incoming request to match on (use only with simple or range type). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#value DataAkamaiCloudletsAudienceSegmentationMatchRule#value}
        '''
        if isinstance(options, dict):
            options = DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValueOptions(**options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a523b26253900b0a9ffe176c7542a13df88b8336a9d8cfe3b29c5401cfbf7c9a)
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
        '''The array type, which can be one of the following: object or simple or range.

        Use the simple option when adding only an array of string-based values

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#type DataAkamaiCloudletsAudienceSegmentationMatchRule#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''If using a match type that supports name attributes, enter the value in the incoming request to match on.

        The following match types support this property: cookie, header, parameter, and query

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#name DataAkamaiCloudletsAudienceSegmentationMatchRule#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name_case_sensitive(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set to true if the entry for the name property should be evaluated based on case sensitivity.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#name_case_sensitive DataAkamaiCloudletsAudienceSegmentationMatchRule#name_case_sensitive}
        '''
        result = self._values.get("name_case_sensitive")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def name_has_wildcard(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set to true if the entry for the name property includes wildcards.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#name_has_wildcard DataAkamaiCloudletsAudienceSegmentationMatchRule#name_has_wildcard}
        '''
        result = self._values.get("name_has_wildcard")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def options(
        self,
    ) -> typing.Optional["DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValueOptions"]:
        '''options block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#options DataAkamaiCloudletsAudienceSegmentationMatchRule#options}
        '''
        result = self._values.get("options")
        return typing.cast(typing.Optional["DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValueOptions"], result)

    @builtins.property
    def value(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The value attributes in the incoming request to match on (use only with simple or range type).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#value DataAkamaiCloudletsAudienceSegmentationMatchRule#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValueList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsAudienceSegmentationMatchRule.DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValueList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dd5c40ab6f1d94e413a4ea2e97609a0500b9c68e60cf1475273e8923a634cb2c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValueOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a4d1d9dfcc48539e2c2b399c65c847f7e7aa3a99fa89c6799fdb6e21dc4ab33)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValueOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbc2c61d9745f064c03b5b1b0ab57599a7f42a4a73243cca9ad7217a44c4acc7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0feab8da2ac1499e33c4c0d07d571ce6505d91a08511903bca9553a5ed3cff65)
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
            type_hints = typing.get_type_hints(_typecheckingstub__07ce656bb7e3f891ce5dd1845745115beb50302cfbb061cc0f8e0cddecfa3e9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValue]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValue]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValue]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06674babb9148beed9394a0ca0557c2b98e56da4ee0ffae54da11ef7d9c79f36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsAudienceSegmentationMatchRule.DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValueOptions",
    jsii_struct_bases=[],
    name_mapping={
        "value": "value",
        "value_case_sensitive": "valueCaseSensitive",
        "value_escaped": "valueEscaped",
        "value_has_wildcard": "valueHasWildcard",
    },
)
class DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValueOptions:
    def __init__(
        self,
        *,
        value: typing.Optional[typing.Sequence[builtins.str]] = None,
        value_case_sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        value_escaped: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        value_has_wildcard: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param value: The value attributes in the incoming request to match on. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#value DataAkamaiCloudletsAudienceSegmentationMatchRule#value}
        :param value_case_sensitive: Set to true if the entries for the value property should be evaluated based on case sensitivity. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#value_case_sensitive DataAkamaiCloudletsAudienceSegmentationMatchRule#value_case_sensitive}
        :param value_escaped: Set to true if provided value should be compared in escaped form. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#value_escaped DataAkamaiCloudletsAudienceSegmentationMatchRule#value_escaped}
        :param value_has_wildcard: Set to true if the entries for the value property include wildcards. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#value_has_wildcard DataAkamaiCloudletsAudienceSegmentationMatchRule#value_has_wildcard}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb36f4d1cb2f9946eb3d37c20c517a025ae4e9816ddb2527f1ecd69e2eedc480)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#value DataAkamaiCloudletsAudienceSegmentationMatchRule#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def value_case_sensitive(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set to true if the entries for the value property should be evaluated based on case sensitivity.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#value_case_sensitive DataAkamaiCloudletsAudienceSegmentationMatchRule#value_case_sensitive}
        '''
        result = self._values.get("value_case_sensitive")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def value_escaped(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set to true if provided value should be compared in escaped form.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#value_escaped DataAkamaiCloudletsAudienceSegmentationMatchRule#value_escaped}
        '''
        result = self._values.get("value_escaped")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def value_has_wildcard(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set to true if the entries for the value property include wildcards.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#value_has_wildcard DataAkamaiCloudletsAudienceSegmentationMatchRule#value_has_wildcard}
        '''
        result = self._values.get("value_has_wildcard")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValueOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValueOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsAudienceSegmentationMatchRule.DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValueOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f581c707ed3c26322e6fb0a3bd8635a708c3244c9da4bdab02838564a6cebbff)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2ce307f1010d3750e073d84bbbf9af07669c8a8f663b6be610643d68e1f6824c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5f2f7f92efa32cac6b1afb6855d5681cb89447f1487dda0b7d29399319f838ac)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5220edddaa1c3a4bed2ef4226e7e2a9ec252e385f38ab329a54b7238b5ac9e62)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5cdd0dcc251ce7cb1f125db1f249ad6b27288c2367b7ba2c9223a3888154a477)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "valueHasWildcard", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValueOptions]:
        return typing.cast(typing.Optional[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValueOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValueOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9cb06e2ddf10760d8fcd8fd2539a9f361f96f73cac54ec8597bca0e89d801d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValueOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsAudienceSegmentationMatchRule.DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValueOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0fb6ad8d0ce404a0e47814cb2b62c401ebdf4806f2a0b41f823f0f8223fff85b)
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
        :param value: The value attributes in the incoming request to match on. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#value DataAkamaiCloudletsAudienceSegmentationMatchRule#value}
        :param value_case_sensitive: Set to true if the entries for the value property should be evaluated based on case sensitivity. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#value_case_sensitive DataAkamaiCloudletsAudienceSegmentationMatchRule#value_case_sensitive}
        :param value_escaped: Set to true if provided value should be compared in escaped form. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#value_escaped DataAkamaiCloudletsAudienceSegmentationMatchRule#value_escaped}
        :param value_has_wildcard: Set to true if the entries for the value property include wildcards. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#value_has_wildcard DataAkamaiCloudletsAudienceSegmentationMatchRule#value_has_wildcard}
        '''
        value_ = DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValueOptions(
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
    ) -> DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValueOptionsOutputReference:
        return typing.cast(DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValueOptionsOutputReference, jsii.get(self, "options"))

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
    ) -> typing.Optional[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValueOptions]:
        return typing.cast(typing.Optional[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValueOptions], jsii.get(self, "optionsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__252a20a1765388ffb9bee8ac11ea1fee3a22799146f7cc2589df63a32ff65b09)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d8cde5c954546aca068adf61f7f9d53257b4ca37c93a1244c95897e153a6270e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__527874d3d46b6dc831b6d854d585ae8743fa64a8bc4fd024d564c515dc5484b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nameHasWildcard", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9889c7252790c1c848c3149b0fee030c4f1344cee0eeced7061aed5b6f546143)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "value"))

    @value.setter
    def value(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31969871721779653e4b3ddf506eed9f82fbad2a4527264dc6054defde5a037d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValue]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValue]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValue]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffe98d98cc8335f4e7afc29905997bbdc28248a5bd4227eba44c4ab688508c30)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsAudienceSegmentationMatchRule.DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__70fa1b56362e10847c87b505e49cb875cab93693b519617b1ec0b170f6b260d3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putObjectMatchValue")
    def put_object_match_value(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValue, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05e04263e3ee01eedf8f809d545356ad8e9e05f36d5ecec197f44f3ab373d4b3)
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
    ) -> DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValueList:
        return typing.cast(DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValueList, jsii.get(self, "objectMatchValue"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValue]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValue]]], jsii.get(self, "objectMatchValueInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__245097e61875f190990592803e3a8d5776910acc379930803538d5f6bbe8fd24)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caseSensitive", value)

    @builtins.property
    @jsii.member(jsii_name="checkIps")
    def check_ips(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "checkIps"))

    @check_ips.setter
    def check_ips(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bef32b6ee1a567d3ee6dc19950d726910886140af8b37e01c6ffa763fda8be72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "checkIps", value)

    @builtins.property
    @jsii.member(jsii_name="matchOperator")
    def match_operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchOperator"))

    @match_operator.setter
    def match_operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__beea036738fb2529cf7d856ee45bf6ad1f4b2c1dd6a80f2c0b514910045ec5af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOperator", value)

    @builtins.property
    @jsii.member(jsii_name="matchType")
    def match_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchType"))

    @match_type.setter
    def match_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__508b4db046284ccdecf20b530b6b302d173249cb12e7026016c0edddf51b8a10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchType", value)

    @builtins.property
    @jsii.member(jsii_name="matchValue")
    def match_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchValue"))

    @match_value.setter
    def match_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7c6e9420cfcaf0ac451becb51d433a2b45890c2d12c09dadccb0b61d96463b5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6ac58e6e6b951d14cbdb4c12b9cd66bca1fa922ec46ecd949be77ae5082d0eec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatches]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatches]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatches]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__049a1c09d3137ea3d55c3dea88dd13a5ea39dba2baac8f801442bd5c32ab0306)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsAudienceSegmentationMatchRule.DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__98a6db725bd1dbf5f3d60a5776bde0a1a18ac577a04908301db6c62b015cdc91)
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
        :param origin_id: The ID of the Conditional Origin requests are forwarded to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#origin_id DataAkamaiCloudletsAudienceSegmentationMatchRule#origin_id}
        :param path_and_qs: If a value is provided and match conditions are met, this property defines the path/resource/query string to rewrite URL for the incoming request. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#path_and_qs DataAkamaiCloudletsAudienceSegmentationMatchRule#path_and_qs}
        :param use_incoming_query_string: If set to true, the Cloudlet includes the query string from the request in the rewritten or forwarded URL. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_audience_segmentation_match_rule#use_incoming_query_string DataAkamaiCloudletsAudienceSegmentationMatchRule#use_incoming_query_string}
        '''
        value = DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesForwardSettings(
            origin_id=origin_id,
            path_and_qs=path_and_qs,
            use_incoming_query_string=use_incoming_query_string,
        )

        return typing.cast(None, jsii.invoke(self, "putForwardSettings", [value]))

    @jsii.member(jsii_name="putMatches")
    def put_matches(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatches, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dddf4481b445ce20558db040d0e0776cf7c57061a9714fc6bed41d7ef9978fcb)
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
    ) -> DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesForwardSettingsOutputReference:
        return typing.cast(DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesForwardSettingsOutputReference, jsii.get(self, "forwardSettings"))

    @builtins.property
    @jsii.member(jsii_name="matches")
    def matches(
        self,
    ) -> DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesList:
        return typing.cast(DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesList, jsii.get(self, "matches"))

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
    ) -> typing.Optional[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesForwardSettings]:
        return typing.cast(typing.Optional[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesForwardSettings], jsii.get(self, "forwardSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchesInput")
    def matches_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatches]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatches]]], jsii.get(self, "matchesInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__d6a34571f32ae0abb17a222746b6ccbcdab1da816e916c216c97d3aaabff31ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabled", value)

    @builtins.property
    @jsii.member(jsii_name="end")
    def end(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "end"))

    @end.setter
    def end(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c957ad9c2389838857d48fcbff4cf65b3c707374a730955097eddae40fa86a06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "end", value)

    @builtins.property
    @jsii.member(jsii_name="matchUrl")
    def match_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchUrl"))

    @match_url.setter
    def match_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d94cf225a78c151effd1f880c4a4f5ea05feafd2ea972ba9c8fb3b3afc08c5be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchUrl", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__657bd9ff5b51d934ec286e8c8624d2fe87c940159d9d49953ff0785ff1be170c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="start")
    def start(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "start"))

    @start.setter
    def start(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee67ed5890b69505cb9fc3909e3e60b136f7387447a1e8924d4a3c3bcacd2f22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "start", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRules]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRules]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRules]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89ac31305115ce4c2057f5ccd24cf5e394facc0dafe882098413b281c0831179)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataAkamaiCloudletsAudienceSegmentationMatchRule",
    "DataAkamaiCloudletsAudienceSegmentationMatchRuleConfig",
    "DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRules",
    "DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesForwardSettings",
    "DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesForwardSettingsOutputReference",
    "DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesList",
    "DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatches",
    "DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesList",
    "DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValue",
    "DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValueList",
    "DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValueOptions",
    "DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValueOptionsOutputReference",
    "DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValueOutputReference",
    "DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesOutputReference",
    "DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesOutputReference",
]

publication.publish()

def _typecheckingstub__eda019cddb44f3975a16f10b1e7951fcea874b7529e19c059fa1297f3f1acff2(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    id: typing.Optional[builtins.str] = None,
    match_rules: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRules, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__aaff018869fefe947c30498a0ec45e3a264e4111ec41edebecc038f551e69ad3(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3328235ef0ea082a588db222405fc5e77ea3bfbc01fbc84ad591a914cfa0228b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRules, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fac3ca4dcfc9a5c54d075d68c92fc8ea6ab8f5e1e0dacda46da16db0dd5a7b63(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e26b411686e85f6ac096f8210b7fd652f60b31ae49a0b5cfcc539c7e85432faf(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    match_rules: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRules, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e6a5a4a538ef2bd31d781ec7e8c8d7993dbe5dcc47fccacde89317796fa561a(
    *,
    forward_settings: typing.Union[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesForwardSettings, typing.Dict[builtins.str, typing.Any]],
    disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    end: typing.Optional[jsii.Number] = None,
    matches: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatches, typing.Dict[builtins.str, typing.Any]]]]] = None,
    match_url: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    start: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec18aefda4bd081fb30668dfc9a60adc1690932024321bb19a46aee7081ed818(
    *,
    origin_id: typing.Optional[builtins.str] = None,
    path_and_qs: typing.Optional[builtins.str] = None,
    use_incoming_query_string: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc974f09bd63948355c40429e70ec7b9aead8dc54847aefd882a92d06e9b1226(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35ffda61d97030ee2fb83badd809a8ca8e2d87e319d69af9087f95dac97c7cc1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ed22ef9fb01e48d4ed15daa955b4f273a06bf074027f9ed42573eed7f7add50(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9525bb12e2733efe6a81b92ae87f8d8581bfd1ac9ca85588f39404ff523b5312(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__166dcea6ace97de9dace2c2e81f68e32792d81e3feee8ab748e9306746a719ba(
    value: typing.Optional[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesForwardSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e70eea68d3088300d6634ed1a9a9c096afac1499a4ac4047fc38e30e66de37a9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc04c9c4fa6cc351738b2d8fc9c804ec573aaf3781bd0d41bb7e4fb3946babae(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__792b289d63fff275b78cbb11e13f97265f58b4483094121563ac58424f344c7c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9aa6b8fdd0e95e04c92cc685027bc8f31df6a59f30d5bb3e6393f283f24efe7(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a904169b4cbc919366e6555868fab8ba8cb614b53c5cf6281ce4b6fc4bc57b19(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26a751d79b06923679ab28947c390dfd7d88a5887b46555298085ea9d0404c67(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRules]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9575e11ba6bd8158a60206918820e05cec46c82a0dba25002c7f4663869c77b7(
    *,
    case_sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    check_ips: typing.Optional[builtins.str] = None,
    match_operator: typing.Optional[builtins.str] = None,
    match_type: typing.Optional[builtins.str] = None,
    match_value: typing.Optional[builtins.str] = None,
    negate: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    object_match_value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValue, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e9739527b7cc5156d6a2ea97ec0237c8271e6e7235f5a757e9c37000006e01e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3796023ae1f2cdc5d6e87288ce76ed7068e66d78352e67ca6232fd9007538eea(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3092f82d2820adc16b34c76074746f7b7d0b9a213cbc8c155700e25b8dc73ff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fd69438ea26b74efd3acdeec027d3576af322d7a0a95130cf586a05b497f73e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__171e7c57e84ff8d650aa6903423cbbe287800666fb88a42d6d0f704730075df8(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f5b0f2e925888efa21c662624f01f5d9e5f26642522f3ed89eb0614bb976a08(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatches]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a523b26253900b0a9ffe176c7542a13df88b8336a9d8cfe3b29c5401cfbf7c9a(
    *,
    type: builtins.str,
    name: typing.Optional[builtins.str] = None,
    name_case_sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    name_has_wildcard: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    options: typing.Optional[typing.Union[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValueOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    value: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd5c40ab6f1d94e413a4ea2e97609a0500b9c68e60cf1475273e8923a634cb2c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a4d1d9dfcc48539e2c2b399c65c847f7e7aa3a99fa89c6799fdb6e21dc4ab33(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbc2c61d9745f064c03b5b1b0ab57599a7f42a4a73243cca9ad7217a44c4acc7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0feab8da2ac1499e33c4c0d07d571ce6505d91a08511903bca9553a5ed3cff65(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07ce656bb7e3f891ce5dd1845745115beb50302cfbb061cc0f8e0cddecfa3e9c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06674babb9148beed9394a0ca0557c2b98e56da4ee0ffae54da11ef7d9c79f36(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValue]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb36f4d1cb2f9946eb3d37c20c517a025ae4e9816ddb2527f1ecd69e2eedc480(
    *,
    value: typing.Optional[typing.Sequence[builtins.str]] = None,
    value_case_sensitive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    value_escaped: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    value_has_wildcard: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f581c707ed3c26322e6fb0a3bd8635a708c3244c9da4bdab02838564a6cebbff(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ce307f1010d3750e073d84bbbf9af07669c8a8f663b6be610643d68e1f6824c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f2f7f92efa32cac6b1afb6855d5681cb89447f1487dda0b7d29399319f838ac(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5220edddaa1c3a4bed2ef4226e7e2a9ec252e385f38ab329a54b7238b5ac9e62(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cdd0dcc251ce7cb1f125db1f249ad6b27288c2367b7ba2c9223a3888154a477(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9cb06e2ddf10760d8fcd8fd2539a9f361f96f73cac54ec8597bca0e89d801d5(
    value: typing.Optional[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValueOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fb6ad8d0ce404a0e47814cb2b62c401ebdf4806f2a0b41f823f0f8223fff85b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__252a20a1765388ffb9bee8ac11ea1fee3a22799146f7cc2589df63a32ff65b09(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8cde5c954546aca068adf61f7f9d53257b4ca37c93a1244c95897e153a6270e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__527874d3d46b6dc831b6d854d585ae8743fa64a8bc4fd024d564c515dc5484b0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9889c7252790c1c848c3149b0fee030c4f1344cee0eeced7061aed5b6f546143(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31969871721779653e4b3ddf506eed9f82fbad2a4527264dc6054defde5a037d(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffe98d98cc8335f4e7afc29905997bbdc28248a5bd4227eba44c4ab688508c30(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValue]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70fa1b56362e10847c87b505e49cb875cab93693b519617b1ec0b170f6b260d3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05e04263e3ee01eedf8f809d545356ad8e9e05f36d5ecec197f44f3ab373d4b3(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatchesObjectMatchValue, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__245097e61875f190990592803e3a8d5776910acc379930803538d5f6bbe8fd24(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bef32b6ee1a567d3ee6dc19950d726910886140af8b37e01c6ffa763fda8be72(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__beea036738fb2529cf7d856ee45bf6ad1f4b2c1dd6a80f2c0b514910045ec5af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__508b4db046284ccdecf20b530b6b302d173249cb12e7026016c0edddf51b8a10(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7c6e9420cfcaf0ac451becb51d433a2b45890c2d12c09dadccb0b61d96463b5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ac58e6e6b951d14cbdb4c12b9cd66bca1fa922ec46ecd949be77ae5082d0eec(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__049a1c09d3137ea3d55c3dea88dd13a5ea39dba2baac8f801442bd5c32ab0306(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatches]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98a6db725bd1dbf5f3d60a5776bde0a1a18ac577a04908301db6c62b015cdc91(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dddf4481b445ce20558db040d0e0776cf7c57061a9714fc6bed41d7ef9978fcb(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRulesMatches, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6a34571f32ae0abb17a222746b6ccbcdab1da816e916c216c97d3aaabff31ec(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c957ad9c2389838857d48fcbff4cf65b3c707374a730955097eddae40fa86a06(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d94cf225a78c151effd1f880c4a4f5ea05feafd2ea972ba9c8fb3b3afc08c5be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__657bd9ff5b51d934ec286e8c8624d2fe87c940159d9d49953ff0785ff1be170c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee67ed5890b69505cb9fc3909e3e60b136f7387447a1e8924d4a3c3bcacd2f22(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89ac31305115ce4c2057f5ccd24cf5e394facc0dafe882098413b281c0831179(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsAudienceSegmentationMatchRuleMatchRules]],
) -> None:
    """Type checking stubs"""
    pass
