'''
# `data_akamai_property_rules`

Refer to the Terraform Registry for docs: [`data_akamai_property_rules`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules).
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


class DataAkamaiPropertyRules(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiPropertyRules.DataAkamaiPropertyRules",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules akamai_property_rules}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        property_id: builtins.str,
        contract_id: typing.Optional[builtins.str] = None,
        group_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        rule_format: typing.Optional[builtins.str] = None,
        version: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules akamai_property_rules} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param property_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules#property_id DataAkamaiPropertyRules#property_id}.
        :param contract_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules#contract_id DataAkamaiPropertyRules#contract_id}.
        :param group_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules#group_id DataAkamaiPropertyRules#group_id}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules#id DataAkamaiPropertyRules#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param rule_format: Rule format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules#rule_format DataAkamaiPropertyRules#rule_format}
        :param version: This is a computed value - provider will always use 'latest' version, providing own version number is not supported. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules#version DataAkamaiPropertyRules#version}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01428b319beca11948b6429726cbc24581bc9a1e2f3faddd044297b9aaf3389f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAkamaiPropertyRulesConfig(
            property_id=property_id,
            contract_id=contract_id,
            group_id=group_id,
            id=id,
            rule_format=rule_format,
            version=version,
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
        '''Generates CDKTF code for importing a DataAkamaiPropertyRules resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the DataAkamaiPropertyRules to import.
        :param import_from_id: The id of the existing DataAkamaiPropertyRules that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the DataAkamaiPropertyRules to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc636d0d7c95a14e0e5d72da042bf2969ed342f7c939f695436ed728cb91e6a4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetContractId")
    def reset_contract_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContractId", []))

    @jsii.member(jsii_name="resetGroupId")
    def reset_group_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRuleFormat")
    def reset_rule_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuleFormat", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

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
    @jsii.member(jsii_name="errors")
    def errors(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "errors"))

    @builtins.property
    @jsii.member(jsii_name="rules")
    def rules(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rules"))

    @builtins.property
    @jsii.member(jsii_name="contractIdInput")
    def contract_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contractIdInput"))

    @builtins.property
    @jsii.member(jsii_name="groupIdInput")
    def group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="propertyIdInput")
    def property_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "propertyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleFormatInput")
    def rule_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="contractId")
    def contract_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contractId"))

    @contract_id.setter
    def contract_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9264eba103b34ddc1c2ae49de8b0cfe6392faabac42978b73e6a376f16dbb3ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contractId", value)

    @builtins.property
    @jsii.member(jsii_name="groupId")
    def group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupId"))

    @group_id.setter
    def group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__284bd8c1c05c1adec68a717523777ce3aaa827ca77a05a774917335b33172cc8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e492061912c962a87529c069ed43c9642ad091b83c9e9ec37140b3504c1b199)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="propertyId")
    def property_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "propertyId"))

    @property_id.setter
    def property_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fd2cb75d5c43e552ad37b0df5474be75e326cfba8d9a824ace9e85972e3c3ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "propertyId", value)

    @builtins.property
    @jsii.member(jsii_name="ruleFormat")
    def rule_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleFormat"))

    @rule_format.setter
    def rule_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d83e173832c3efbc227ebcdea974881f6652abe4243597d8ba4b734344e64b81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleFormat", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "version"))

    @version.setter
    def version(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02f0e9074798da01707eb0ca57822c6a532529bca08c7eba9f3db5665365aa7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiPropertyRules.DataAkamaiPropertyRulesConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "property_id": "propertyId",
        "contract_id": "contractId",
        "group_id": "groupId",
        "id": "id",
        "rule_format": "ruleFormat",
        "version": "version",
    },
)
class DataAkamaiPropertyRulesConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        property_id: builtins.str,
        contract_id: typing.Optional[builtins.str] = None,
        group_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        rule_format: typing.Optional[builtins.str] = None,
        version: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param property_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules#property_id DataAkamaiPropertyRules#property_id}.
        :param contract_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules#contract_id DataAkamaiPropertyRules#contract_id}.
        :param group_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules#group_id DataAkamaiPropertyRules#group_id}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules#id DataAkamaiPropertyRules#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param rule_format: Rule format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules#rule_format DataAkamaiPropertyRules#rule_format}
        :param version: This is a computed value - provider will always use 'latest' version, providing own version number is not supported. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules#version DataAkamaiPropertyRules#version}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aaf487149aece8ecbd5febbf023339e08a08ec465887cd213953db51dc68d215)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument property_id", value=property_id, expected_type=type_hints["property_id"])
            check_type(argname="argument contract_id", value=contract_id, expected_type=type_hints["contract_id"])
            check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument rule_format", value=rule_format, expected_type=type_hints["rule_format"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "property_id": property_id,
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
        if contract_id is not None:
            self._values["contract_id"] = contract_id
        if group_id is not None:
            self._values["group_id"] = group_id
        if id is not None:
            self._values["id"] = id
        if rule_format is not None:
            self._values["rule_format"] = rule_format
        if version is not None:
            self._values["version"] = version

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
    def property_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules#property_id DataAkamaiPropertyRules#property_id}.'''
        result = self._values.get("property_id")
        assert result is not None, "Required property 'property_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def contract_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules#contract_id DataAkamaiPropertyRules#contract_id}.'''
        result = self._values.get("contract_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def group_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules#group_id DataAkamaiPropertyRules#group_id}.'''
        result = self._values.get("group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules#id DataAkamaiPropertyRules#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rule_format(self) -> typing.Optional[builtins.str]:
        '''Rule format.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules#rule_format DataAkamaiPropertyRules#rule_format}
        '''
        result = self._values.get("rule_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[jsii.Number]:
        '''This is a computed value - provider will always use 'latest' version, providing own version number is not supported.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules#version DataAkamaiPropertyRules#version}
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiPropertyRulesConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DataAkamaiPropertyRules",
    "DataAkamaiPropertyRulesConfig",
]

publication.publish()

def _typecheckingstub__01428b319beca11948b6429726cbc24581bc9a1e2f3faddd044297b9aaf3389f(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    property_id: builtins.str,
    contract_id: typing.Optional[builtins.str] = None,
    group_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    rule_format: typing.Optional[builtins.str] = None,
    version: typing.Optional[jsii.Number] = None,
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

def _typecheckingstub__fc636d0d7c95a14e0e5d72da042bf2969ed342f7c939f695436ed728cb91e6a4(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9264eba103b34ddc1c2ae49de8b0cfe6392faabac42978b73e6a376f16dbb3ef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__284bd8c1c05c1adec68a717523777ce3aaa827ca77a05a774917335b33172cc8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e492061912c962a87529c069ed43c9642ad091b83c9e9ec37140b3504c1b199(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fd2cb75d5c43e552ad37b0df5474be75e326cfba8d9a824ace9e85972e3c3ff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d83e173832c3efbc227ebcdea974881f6652abe4243597d8ba4b734344e64b81(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02f0e9074798da01707eb0ca57822c6a532529bca08c7eba9f3db5665365aa7d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aaf487149aece8ecbd5febbf023339e08a08ec465887cd213953db51dc68d215(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    property_id: builtins.str,
    contract_id: typing.Optional[builtins.str] = None,
    group_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    rule_format: typing.Optional[builtins.str] = None,
    version: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass
