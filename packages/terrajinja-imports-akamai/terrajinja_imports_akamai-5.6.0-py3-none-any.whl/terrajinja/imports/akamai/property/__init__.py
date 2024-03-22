'''
# `akamai_property`

Refer to the Terraform Registry for docs: [`akamai_property`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property).
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


class Property(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.property.Property",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property akamai_property}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        contract_id: builtins.str,
        group_id: builtins.str,
        name: builtins.str,
        product_id: builtins.str,
        hostnames: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PropertyHostnames", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        property_id: typing.Optional[builtins.str] = None,
        rule_format: typing.Optional[builtins.str] = None,
        rules: typing.Optional[builtins.str] = None,
        version_notes: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property akamai_property} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param contract_id: Contract ID to be assigned to the Property. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#contract_id Property#contract_id}
        :param group_id: Group ID to be assigned to the Property. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#group_id Property#group_id}
        :param name: Name to give to the Property (must be unique). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#name Property#name}
        :param product_id: Product ID to be assigned to the Property. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#product_id Property#product_id}
        :param hostnames: hostnames block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#hostnames Property#hostnames}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#id Property#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param property_id: Property ID. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#property_id Property#property_id}
        :param rule_format: Specify the rule format version (defaults to latest version available when created). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#rule_format Property#rule_format}
        :param rules: Property Rules as JSON. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#rules Property#rules}
        :param version_notes: Property version notes. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#version_notes Property#version_notes}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1783e18cf8778db0c1f5c6e4edd3627e7116012ab338f723a9626e9e21dec183)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = PropertyConfig(
            contract_id=contract_id,
            group_id=group_id,
            name=name,
            product_id=product_id,
            hostnames=hostnames,
            id=id,
            property_id=property_id,
            rule_format=rule_format,
            rules=rules,
            version_notes=version_notes,
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
        '''Generates CDKTF code for importing a Property resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the Property to import.
        :param import_from_id: The id of the existing Property that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the Property to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e245dabd2ac73071c62a8470a04ddc795afa2b7ab51cd480f532c1483faacfdb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putHostnames")
    def put_hostnames(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PropertyHostnames", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a77edf2cfa37bceafc224501518bf00a2dd88feacbe0179f9f4b2fe3abdb38a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHostnames", [value]))

    @jsii.member(jsii_name="resetHostnames")
    def reset_hostnames(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostnames", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPropertyId")
    def reset_property_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPropertyId", []))

    @jsii.member(jsii_name="resetRuleFormat")
    def reset_rule_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuleFormat", []))

    @jsii.member(jsii_name="resetRules")
    def reset_rules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRules", []))

    @jsii.member(jsii_name="resetVersionNotes")
    def reset_version_notes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersionNotes", []))

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
    @jsii.member(jsii_name="hostnames")
    def hostnames(self) -> "PropertyHostnamesList":
        return typing.cast("PropertyHostnamesList", jsii.get(self, "hostnames"))

    @builtins.property
    @jsii.member(jsii_name="latestVersion")
    def latest_version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "latestVersion"))

    @builtins.property
    @jsii.member(jsii_name="productionVersion")
    def production_version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "productionVersion"))

    @builtins.property
    @jsii.member(jsii_name="readVersion")
    def read_version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "readVersion"))

    @builtins.property
    @jsii.member(jsii_name="ruleErrors")
    def rule_errors(self) -> "PropertyRuleErrorsList":
        return typing.cast("PropertyRuleErrorsList", jsii.get(self, "ruleErrors"))

    @builtins.property
    @jsii.member(jsii_name="ruleWarnings")
    def rule_warnings(self) -> "PropertyRuleWarningsList":
        return typing.cast("PropertyRuleWarningsList", jsii.get(self, "ruleWarnings"))

    @builtins.property
    @jsii.member(jsii_name="stagingVersion")
    def staging_version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "stagingVersion"))

    @builtins.property
    @jsii.member(jsii_name="contractIdInput")
    def contract_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contractIdInput"))

    @builtins.property
    @jsii.member(jsii_name="groupIdInput")
    def group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="hostnamesInput")
    def hostnames_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PropertyHostnames"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PropertyHostnames"]]], jsii.get(self, "hostnamesInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="productIdInput")
    def product_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "productIdInput"))

    @builtins.property
    @jsii.member(jsii_name="propertyIdInput")
    def property_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "propertyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleFormatInput")
    def rule_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="rulesInput")
    def rules_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rulesInput"))

    @builtins.property
    @jsii.member(jsii_name="versionNotesInput")
    def version_notes_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionNotesInput"))

    @builtins.property
    @jsii.member(jsii_name="contractId")
    def contract_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contractId"))

    @contract_id.setter
    def contract_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bbeb2485f078e88cfbdabae3cb3898ba7b6f29d894f064e6d6090fb1cb33e36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contractId", value)

    @builtins.property
    @jsii.member(jsii_name="groupId")
    def group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupId"))

    @group_id.setter
    def group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b271808477fb8e25371d880bb822128ac900c65d2a88bce8d58acf03d98961db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b27dd7468b532c3d3f8f82892f54d20fe62f76a4139c993aa73d8a5e58f20695)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36f13fbba8d1cb35cd5e3e7bb84b4e1c5f7c8b3d06b8fd494f956a5b6f282d98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="productId")
    def product_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "productId"))

    @product_id.setter
    def product_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ec49a059afc347e87e6ae2d492f2e5b49d35fc268e6caaa15595e3be696a547)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "productId", value)

    @builtins.property
    @jsii.member(jsii_name="propertyId")
    def property_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "propertyId"))

    @property_id.setter
    def property_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2770adb717103f60e84975a2e3a85df122e590f58a427b7eeb6807564ba677a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "propertyId", value)

    @builtins.property
    @jsii.member(jsii_name="ruleFormat")
    def rule_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleFormat"))

    @rule_format.setter
    def rule_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acf8d24efcdede318f0b8d4ead85c2d22156dd0b06123ae488f07ee675a7d6b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleFormat", value)

    @builtins.property
    @jsii.member(jsii_name="rules")
    def rules(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rules"))

    @rules.setter
    def rules(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8799001c4813671c3461280e3af1341c447c6a9ec73a76ae8e7f942a51cb55ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rules", value)

    @builtins.property
    @jsii.member(jsii_name="versionNotes")
    def version_notes(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "versionNotes"))

    @version_notes.setter
    def version_notes(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2432d381e0df62cebfde8609a68fab5f00e29ada62144b6bd25c5f22b95fccf1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versionNotes", value)


@jsii.data_type(
    jsii_type="akamai.property.PropertyConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "contract_id": "contractId",
        "group_id": "groupId",
        "name": "name",
        "product_id": "productId",
        "hostnames": "hostnames",
        "id": "id",
        "property_id": "propertyId",
        "rule_format": "ruleFormat",
        "rules": "rules",
        "version_notes": "versionNotes",
    },
)
class PropertyConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        contract_id: builtins.str,
        group_id: builtins.str,
        name: builtins.str,
        product_id: builtins.str,
        hostnames: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PropertyHostnames", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        property_id: typing.Optional[builtins.str] = None,
        rule_format: typing.Optional[builtins.str] = None,
        rules: typing.Optional[builtins.str] = None,
        version_notes: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param contract_id: Contract ID to be assigned to the Property. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#contract_id Property#contract_id}
        :param group_id: Group ID to be assigned to the Property. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#group_id Property#group_id}
        :param name: Name to give to the Property (must be unique). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#name Property#name}
        :param product_id: Product ID to be assigned to the Property. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#product_id Property#product_id}
        :param hostnames: hostnames block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#hostnames Property#hostnames}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#id Property#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param property_id: Property ID. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#property_id Property#property_id}
        :param rule_format: Specify the rule format version (defaults to latest version available when created). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#rule_format Property#rule_format}
        :param rules: Property Rules as JSON. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#rules Property#rules}
        :param version_notes: Property version notes. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#version_notes Property#version_notes}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d69fcb8e9b9174c3c160a7a9efda793ab955544064857c16ccb74b51ae97eb9)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument contract_id", value=contract_id, expected_type=type_hints["contract_id"])
            check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument product_id", value=product_id, expected_type=type_hints["product_id"])
            check_type(argname="argument hostnames", value=hostnames, expected_type=type_hints["hostnames"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument property_id", value=property_id, expected_type=type_hints["property_id"])
            check_type(argname="argument rule_format", value=rule_format, expected_type=type_hints["rule_format"])
            check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
            check_type(argname="argument version_notes", value=version_notes, expected_type=type_hints["version_notes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "contract_id": contract_id,
            "group_id": group_id,
            "name": name,
            "product_id": product_id,
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
        if hostnames is not None:
            self._values["hostnames"] = hostnames
        if id is not None:
            self._values["id"] = id
        if property_id is not None:
            self._values["property_id"] = property_id
        if rule_format is not None:
            self._values["rule_format"] = rule_format
        if rules is not None:
            self._values["rules"] = rules
        if version_notes is not None:
            self._values["version_notes"] = version_notes

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
    def contract_id(self) -> builtins.str:
        '''Contract ID to be assigned to the Property.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#contract_id Property#contract_id}
        '''
        result = self._values.get("contract_id")
        assert result is not None, "Required property 'contract_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_id(self) -> builtins.str:
        '''Group ID to be assigned to the Property.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#group_id Property#group_id}
        '''
        result = self._values.get("group_id")
        assert result is not None, "Required property 'group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name to give to the Property (must be unique).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#name Property#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def product_id(self) -> builtins.str:
        '''Product ID to be assigned to the Property.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#product_id Property#product_id}
        '''
        result = self._values.get("product_id")
        assert result is not None, "Required property 'product_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def hostnames(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PropertyHostnames"]]]:
        '''hostnames block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#hostnames Property#hostnames}
        '''
        result = self._values.get("hostnames")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PropertyHostnames"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#id Property#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def property_id(self) -> typing.Optional[builtins.str]:
        '''Property ID.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#property_id Property#property_id}
        '''
        result = self._values.get("property_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rule_format(self) -> typing.Optional[builtins.str]:
        '''Specify the rule format version (defaults to latest version available when created).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#rule_format Property#rule_format}
        '''
        result = self._values.get("rule_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rules(self) -> typing.Optional[builtins.str]:
        '''Property Rules as JSON.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#rules Property#rules}
        '''
        result = self._values.get("rules")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_notes(self) -> typing.Optional[builtins.str]:
        '''Property version notes.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#version_notes Property#version_notes}
        '''
        result = self._values.get("version_notes")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PropertyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.property.PropertyHostnames",
    jsii_struct_bases=[],
    name_mapping={
        "cert_provisioning_type": "certProvisioningType",
        "cname_from": "cnameFrom",
        "cname_to": "cnameTo",
        "cert_status": "certStatus",
        "cname_type": "cnameType",
    },
)
class PropertyHostnames:
    def __init__(
        self,
        *,
        cert_provisioning_type: builtins.str,
        cname_from: builtins.str,
        cname_to: builtins.str,
        cert_status: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PropertyHostnamesCertStatus", typing.Dict[builtins.str, typing.Any]]]]] = None,
        cname_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cert_provisioning_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#cert_provisioning_type Property#cert_provisioning_type}.
        :param cname_from: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#cname_from Property#cname_from}.
        :param cname_to: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#cname_to Property#cname_to}.
        :param cert_status: cert_status block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#cert_status Property#cert_status}
        :param cname_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#cname_type Property#cname_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e37b3a3de0083c806fb0447a441c50be5c56983dd434a79f7a0ea39e4540bff3)
            check_type(argname="argument cert_provisioning_type", value=cert_provisioning_type, expected_type=type_hints["cert_provisioning_type"])
            check_type(argname="argument cname_from", value=cname_from, expected_type=type_hints["cname_from"])
            check_type(argname="argument cname_to", value=cname_to, expected_type=type_hints["cname_to"])
            check_type(argname="argument cert_status", value=cert_status, expected_type=type_hints["cert_status"])
            check_type(argname="argument cname_type", value=cname_type, expected_type=type_hints["cname_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cert_provisioning_type": cert_provisioning_type,
            "cname_from": cname_from,
            "cname_to": cname_to,
        }
        if cert_status is not None:
            self._values["cert_status"] = cert_status
        if cname_type is not None:
            self._values["cname_type"] = cname_type

    @builtins.property
    def cert_provisioning_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#cert_provisioning_type Property#cert_provisioning_type}.'''
        result = self._values.get("cert_provisioning_type")
        assert result is not None, "Required property 'cert_provisioning_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cname_from(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#cname_from Property#cname_from}.'''
        result = self._values.get("cname_from")
        assert result is not None, "Required property 'cname_from' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cname_to(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#cname_to Property#cname_to}.'''
        result = self._values.get("cname_to")
        assert result is not None, "Required property 'cname_to' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cert_status(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PropertyHostnamesCertStatus"]]]:
        '''cert_status block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#cert_status Property#cert_status}
        '''
        result = self._values.get("cert_status")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PropertyHostnamesCertStatus"]]], result)

    @builtins.property
    def cname_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property#cname_type Property#cname_type}.'''
        result = self._values.get("cname_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PropertyHostnames(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.property.PropertyHostnamesCertStatus",
    jsii_struct_bases=[],
    name_mapping={},
)
class PropertyHostnamesCertStatus:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PropertyHostnamesCertStatus(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PropertyHostnamesCertStatusList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.property.PropertyHostnamesCertStatusList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d13805072aac3d3dd8db4fd775a40730a32f36938e43367064ab41205812c1aa)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "PropertyHostnamesCertStatusOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78890842f0e16d2bd29b9e33074438d92b768b33b14caea29349c1e7a00ea732)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PropertyHostnamesCertStatusOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3922601eb4a55c8c00261854c2925a166752c75fc478c93e7a72bb18dbbaa026)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6186d7707e3d414e66a3d9a3e4342c88b69a99d86e88b82e242b22b89e5f8ef3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2889a8c4c3df20b9496473e84a859d76981a8d69640385d1392bbe61575ea252)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PropertyHostnamesCertStatus]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PropertyHostnamesCertStatus]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PropertyHostnamesCertStatus]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52e4d8c2cae6fb753fd44efa92007b5397946a3f856f9ce8f080b96358fa29a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PropertyHostnamesCertStatusOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.property.PropertyHostnamesCertStatusOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__382c6fcd1768e41b88edb189639ad5300b6a80f87637f6bdcd93ec811a96d2d6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostname"))

    @builtins.property
    @jsii.member(jsii_name="productionStatus")
    def production_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "productionStatus"))

    @builtins.property
    @jsii.member(jsii_name="stagingStatus")
    def staging_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stagingStatus"))

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PropertyHostnamesCertStatus]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PropertyHostnamesCertStatus]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PropertyHostnamesCertStatus]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c40369b881bc4d3af73c437a6b367d07b75177c882a3f9f7cc374cc9d3128a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PropertyHostnamesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.property.PropertyHostnamesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2ebb77aa093863450b2aeba0f480a384bc72eb229a23b6c2f702a115557e0b69)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "PropertyHostnamesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cadb350e20caa3d77a072b14a8cba525693ae1bc824a3f03441f24c7ecaeb878)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PropertyHostnamesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3661daad1d4580addf95f634a4230a067942d8e430f53648a8d705910e39eff3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__aaee7eef595b8b2700f76f8d6944840249f117286d8f65284890058ef274c525)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3baa96870b714518e6447fb27a9ef7e69e5929f98fa8d484c248c85e6cab37f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PropertyHostnames]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PropertyHostnames]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PropertyHostnames]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9dbad80278fa27a8d125029d8e97abd862ef03827d3ea9ee7f3b9193785b5879)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PropertyHostnamesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.property.PropertyHostnamesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__94dd5bdfc3a123ba7b0f8d9d6b39c7dc54bd837c5e06a70c29b470ac589c8f65)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCertStatus")
    def put_cert_status(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PropertyHostnamesCertStatus, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69f50a68b0ce16d22c20c8f1f44a6f30e1bf806c05ee647303d786deea1968d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCertStatus", [value]))

    @jsii.member(jsii_name="resetCertStatus")
    def reset_cert_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertStatus", []))

    @jsii.member(jsii_name="resetCnameType")
    def reset_cname_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCnameType", []))

    @builtins.property
    @jsii.member(jsii_name="certStatus")
    def cert_status(self) -> PropertyHostnamesCertStatusList:
        return typing.cast(PropertyHostnamesCertStatusList, jsii.get(self, "certStatus"))

    @builtins.property
    @jsii.member(jsii_name="edgeHostnameId")
    def edge_hostname_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "edgeHostnameId"))

    @builtins.property
    @jsii.member(jsii_name="certProvisioningTypeInput")
    def cert_provisioning_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certProvisioningTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="certStatusInput")
    def cert_status_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PropertyHostnamesCertStatus]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PropertyHostnamesCertStatus]]], jsii.get(self, "certStatusInput"))

    @builtins.property
    @jsii.member(jsii_name="cnameFromInput")
    def cname_from_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cnameFromInput"))

    @builtins.property
    @jsii.member(jsii_name="cnameToInput")
    def cname_to_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cnameToInput"))

    @builtins.property
    @jsii.member(jsii_name="cnameTypeInput")
    def cname_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cnameTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="certProvisioningType")
    def cert_provisioning_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certProvisioningType"))

    @cert_provisioning_type.setter
    def cert_provisioning_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfeb4252139ac7f3f898cf6c52c8fd666a2c5f89d6d6b057928dc8a1ea31a399)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certProvisioningType", value)

    @builtins.property
    @jsii.member(jsii_name="cnameFrom")
    def cname_from(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cnameFrom"))

    @cname_from.setter
    def cname_from(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8bb909b56d9ed20449a299cb997e633ef58b9cd371f7e51652b7aad4e95e6c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cnameFrom", value)

    @builtins.property
    @jsii.member(jsii_name="cnameTo")
    def cname_to(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cnameTo"))

    @cname_to.setter
    def cname_to(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91b3d979b0a8ed187586339598d14d213cb405e728b09aa7305be082279a1bb9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cnameTo", value)

    @builtins.property
    @jsii.member(jsii_name="cnameType")
    def cname_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cnameType"))

    @cname_type.setter
    def cname_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ce02462453e43325e3c49b1fbfcf37e6af365809924cf59572bc5c12b89e4d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cnameType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PropertyHostnames]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PropertyHostnames]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PropertyHostnames]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d06bdadeb769c5e5642b841758337e7623292217ec542b3b065895e738fc259)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.property.PropertyRuleErrors",
    jsii_struct_bases=[],
    name_mapping={},
)
class PropertyRuleErrors:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PropertyRuleErrors(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PropertyRuleErrorsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.property.PropertyRuleErrorsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e0b849de9c2120424b96107c6f4d4fd3d42c8cb8b1579d435112e253bced2f23)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "PropertyRuleErrorsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__806b0f8b777944850e935882484567479a689d8fab041c60bd5bf0e87866eac3)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PropertyRuleErrorsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__834e0eeae08fa3c129cf132af4bc03d4f603e7edc3cc7a50cf9d94defec9ab25)
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
            type_hints = typing.get_type_hints(_typecheckingstub__959f8100e9bfc02a6fd5d7abe48b991b1f5c078966adb50ce5f76dfc89edcd9a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7a0ca299a2da809df00bea7ed463ae976c025f49666f119788b48b99f21b6f3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class PropertyRuleErrorsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.property.PropertyRuleErrorsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e26eca286026b9557375005081a3bc5617465d95a18dda64dbad3a4b918909bf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="behaviorName")
    def behavior_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "behaviorName"))

    @builtins.property
    @jsii.member(jsii_name="detail")
    def detail(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "detail"))

    @builtins.property
    @jsii.member(jsii_name="errorLocation")
    def error_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "errorLocation"))

    @builtins.property
    @jsii.member(jsii_name="instance")
    def instance(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instance"))

    @builtins.property
    @jsii.member(jsii_name="statusCode")
    def status_code(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "statusCode"))

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PropertyRuleErrors]:
        return typing.cast(typing.Optional[PropertyRuleErrors], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[PropertyRuleErrors]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__796da2b19f2ecf0efd957a56c187518ea4736a38171acf35f6e95ed881dfe032)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.property.PropertyRuleWarnings",
    jsii_struct_bases=[],
    name_mapping={},
)
class PropertyRuleWarnings:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PropertyRuleWarnings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PropertyRuleWarningsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.property.PropertyRuleWarningsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__400325fa19884f36d12e6c2b20c579497e8dd6ce2d35d90585831b9a0120443e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "PropertyRuleWarningsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e5d6a6d4adae721cd026b33b4e8a4259bfab295e037d168230267e2e207c43b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PropertyRuleWarningsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28994eb4ac260b2f8f61e81320e7c6168766a75ca331ec669b0b98bfee3ecc29)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b343062ef14a28f3368b960b38a37949ce0e1cf4e11fe68fb9ffff600276197b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7ea90c6f4788c7e31a36475d958a856e5d0afc0bc63ac7bb85f21655f202f030)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class PropertyRuleWarningsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.property.PropertyRuleWarningsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__178c7220545867c0ea0de4688a193f8063de6e4e379c445f34fef74dccfad93c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="behaviorName")
    def behavior_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "behaviorName"))

    @builtins.property
    @jsii.member(jsii_name="detail")
    def detail(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "detail"))

    @builtins.property
    @jsii.member(jsii_name="errorLocation")
    def error_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "errorLocation"))

    @builtins.property
    @jsii.member(jsii_name="instance")
    def instance(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instance"))

    @builtins.property
    @jsii.member(jsii_name="statusCode")
    def status_code(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "statusCode"))

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PropertyRuleWarnings]:
        return typing.cast(typing.Optional[PropertyRuleWarnings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[PropertyRuleWarnings]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d79eea2080507ac837482f1be6a32a35171787772fa95c512cf1e994eb1ca376)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Property",
    "PropertyConfig",
    "PropertyHostnames",
    "PropertyHostnamesCertStatus",
    "PropertyHostnamesCertStatusList",
    "PropertyHostnamesCertStatusOutputReference",
    "PropertyHostnamesList",
    "PropertyHostnamesOutputReference",
    "PropertyRuleErrors",
    "PropertyRuleErrorsList",
    "PropertyRuleErrorsOutputReference",
    "PropertyRuleWarnings",
    "PropertyRuleWarningsList",
    "PropertyRuleWarningsOutputReference",
]

publication.publish()

def _typecheckingstub__1783e18cf8778db0c1f5c6e4edd3627e7116012ab338f723a9626e9e21dec183(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    contract_id: builtins.str,
    group_id: builtins.str,
    name: builtins.str,
    product_id: builtins.str,
    hostnames: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PropertyHostnames, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    property_id: typing.Optional[builtins.str] = None,
    rule_format: typing.Optional[builtins.str] = None,
    rules: typing.Optional[builtins.str] = None,
    version_notes: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__e245dabd2ac73071c62a8470a04ddc795afa2b7ab51cd480f532c1483faacfdb(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a77edf2cfa37bceafc224501518bf00a2dd88feacbe0179f9f4b2fe3abdb38a4(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PropertyHostnames, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bbeb2485f078e88cfbdabae3cb3898ba7b6f29d894f064e6d6090fb1cb33e36(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b271808477fb8e25371d880bb822128ac900c65d2a88bce8d58acf03d98961db(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b27dd7468b532c3d3f8f82892f54d20fe62f76a4139c993aa73d8a5e58f20695(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36f13fbba8d1cb35cd5e3e7bb84b4e1c5f7c8b3d06b8fd494f956a5b6f282d98(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ec49a059afc347e87e6ae2d492f2e5b49d35fc268e6caaa15595e3be696a547(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2770adb717103f60e84975a2e3a85df122e590f58a427b7eeb6807564ba677a3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acf8d24efcdede318f0b8d4ead85c2d22156dd0b06123ae488f07ee675a7d6b9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8799001c4813671c3461280e3af1341c447c6a9ec73a76ae8e7f942a51cb55ed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2432d381e0df62cebfde8609a68fab5f00e29ada62144b6bd25c5f22b95fccf1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d69fcb8e9b9174c3c160a7a9efda793ab955544064857c16ccb74b51ae97eb9(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    contract_id: builtins.str,
    group_id: builtins.str,
    name: builtins.str,
    product_id: builtins.str,
    hostnames: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PropertyHostnames, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    property_id: typing.Optional[builtins.str] = None,
    rule_format: typing.Optional[builtins.str] = None,
    rules: typing.Optional[builtins.str] = None,
    version_notes: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e37b3a3de0083c806fb0447a441c50be5c56983dd434a79f7a0ea39e4540bff3(
    *,
    cert_provisioning_type: builtins.str,
    cname_from: builtins.str,
    cname_to: builtins.str,
    cert_status: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PropertyHostnamesCertStatus, typing.Dict[builtins.str, typing.Any]]]]] = None,
    cname_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d13805072aac3d3dd8db4fd775a40730a32f36938e43367064ab41205812c1aa(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78890842f0e16d2bd29b9e33074438d92b768b33b14caea29349c1e7a00ea732(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3922601eb4a55c8c00261854c2925a166752c75fc478c93e7a72bb18dbbaa026(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6186d7707e3d414e66a3d9a3e4342c88b69a99d86e88b82e242b22b89e5f8ef3(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2889a8c4c3df20b9496473e84a859d76981a8d69640385d1392bbe61575ea252(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52e4d8c2cae6fb753fd44efa92007b5397946a3f856f9ce8f080b96358fa29a2(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PropertyHostnamesCertStatus]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__382c6fcd1768e41b88edb189639ad5300b6a80f87637f6bdcd93ec811a96d2d6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c40369b881bc4d3af73c437a6b367d07b75177c882a3f9f7cc374cc9d3128a9(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PropertyHostnamesCertStatus]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ebb77aa093863450b2aeba0f480a384bc72eb229a23b6c2f702a115557e0b69(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cadb350e20caa3d77a072b14a8cba525693ae1bc824a3f03441f24c7ecaeb878(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3661daad1d4580addf95f634a4230a067942d8e430f53648a8d705910e39eff3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aaee7eef595b8b2700f76f8d6944840249f117286d8f65284890058ef274c525(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3baa96870b714518e6447fb27a9ef7e69e5929f98fa8d484c248c85e6cab37f3(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9dbad80278fa27a8d125029d8e97abd862ef03827d3ea9ee7f3b9193785b5879(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PropertyHostnames]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94dd5bdfc3a123ba7b0f8d9d6b39c7dc54bd837c5e06a70c29b470ac589c8f65(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69f50a68b0ce16d22c20c8f1f44a6f30e1bf806c05ee647303d786deea1968d7(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PropertyHostnamesCertStatus, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfeb4252139ac7f3f898cf6c52c8fd666a2c5f89d6d6b057928dc8a1ea31a399(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8bb909b56d9ed20449a299cb997e633ef58b9cd371f7e51652b7aad4e95e6c0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91b3d979b0a8ed187586339598d14d213cb405e728b09aa7305be082279a1bb9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ce02462453e43325e3c49b1fbfcf37e6af365809924cf59572bc5c12b89e4d1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d06bdadeb769c5e5642b841758337e7623292217ec542b3b065895e738fc259(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PropertyHostnames]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0b849de9c2120424b96107c6f4d4fd3d42c8cb8b1579d435112e253bced2f23(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__806b0f8b777944850e935882484567479a689d8fab041c60bd5bf0e87866eac3(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__834e0eeae08fa3c129cf132af4bc03d4f603e7edc3cc7a50cf9d94defec9ab25(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__959f8100e9bfc02a6fd5d7abe48b991b1f5c078966adb50ce5f76dfc89edcd9a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a0ca299a2da809df00bea7ed463ae976c025f49666f119788b48b99f21b6f3e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e26eca286026b9557375005081a3bc5617465d95a18dda64dbad3a4b918909bf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__796da2b19f2ecf0efd957a56c187518ea4736a38171acf35f6e95ed881dfe032(
    value: typing.Optional[PropertyRuleErrors],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__400325fa19884f36d12e6c2b20c579497e8dd6ce2d35d90585831b9a0120443e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e5d6a6d4adae721cd026b33b4e8a4259bfab295e037d168230267e2e207c43b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28994eb4ac260b2f8f61e81320e7c6168766a75ca331ec669b0b98bfee3ecc29(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b343062ef14a28f3368b960b38a37949ce0e1cf4e11fe68fb9ffff600276197b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ea90c6f4788c7e31a36475d958a856e5d0afc0bc63ac7bb85f21655f202f030(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__178c7220545867c0ea0de4688a193f8063de6e4e379c445f34fef74dccfad93c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d79eea2080507ac837482f1be6a32a35171787772fa95c512cf1e994eb1ca376(
    value: typing.Optional[PropertyRuleWarnings],
) -> None:
    """Type checking stubs"""
    pass
