'''
# `akamai_property_include`

Refer to the Terraform Registry for docs: [`akamai_property_include`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include).
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


class PropertyInclude(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.propertyInclude.PropertyInclude",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include akamai_property_include}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        contract_id: builtins.str,
        group_id: builtins.str,
        name: builtins.str,
        rule_format: builtins.str,
        type: builtins.str,
        id: typing.Optional[builtins.str] = None,
        product_id: typing.Optional[builtins.str] = None,
        rules: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include akamai_property_include} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param contract_id: Identifies the contract to which the include is assigned. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include#contract_id PropertyInclude#contract_id}
        :param group_id: Identifies the group to which the include is assigned. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include#group_id PropertyInclude#group_id}
        :param name: A descriptive name for the include. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include#name PropertyInclude#name}
        :param rule_format: Indicates the versioned set of features and criteria. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include#rule_format PropertyInclude#rule_format}
        :param type: Specifies the type of the include, either 'MICROSERVICES' or 'COMMON_SETTINGS'. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include#type PropertyInclude#type}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include#id PropertyInclude#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param product_id: The product assigned to the include. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include#product_id PropertyInclude#product_id}
        :param rules: Property Rules as JSON. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include#rules PropertyInclude#rules}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56857270342cfc448354804452e205cc53de2f9b112dba67914edfcc0be6af50)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = PropertyIncludeConfig(
            contract_id=contract_id,
            group_id=group_id,
            name=name,
            rule_format=rule_format,
            type=type,
            id=id,
            product_id=product_id,
            rules=rules,
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
        '''Generates CDKTF code for importing a PropertyInclude resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the PropertyInclude to import.
        :param import_from_id: The id of the existing PropertyInclude that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the PropertyInclude to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__422489099c01fae6cab942b20a4f030a313c5db4b1d2c74e7093bfc6e6cde14b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetProductId")
    def reset_product_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProductId", []))

    @jsii.member(jsii_name="resetRules")
    def reset_rules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRules", []))

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
    @jsii.member(jsii_name="latestVersion")
    def latest_version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "latestVersion"))

    @builtins.property
    @jsii.member(jsii_name="productionVersion")
    def production_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "productionVersion"))

    @builtins.property
    @jsii.member(jsii_name="ruleErrors")
    def rule_errors(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleErrors"))

    @builtins.property
    @jsii.member(jsii_name="ruleWarnings")
    def rule_warnings(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleWarnings"))

    @builtins.property
    @jsii.member(jsii_name="stagingVersion")
    def staging_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stagingVersion"))

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
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="productIdInput")
    def product_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "productIdInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleFormatInput")
    def rule_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="rulesInput")
    def rules_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rulesInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="contractId")
    def contract_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contractId"))

    @contract_id.setter
    def contract_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a68bc3fd00ffed84bb160e042eb0be3c54b2cacf9335548ba8f8abb0a558b5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contractId", value)

    @builtins.property
    @jsii.member(jsii_name="groupId")
    def group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupId"))

    @group_id.setter
    def group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2786c0afd8c426804ef415788e7d7636263062c52cdea2075824672a8a0b3d39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b3d252905b731ac790f9fd89e49fdc02481780188f91834ac0652192e40426c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebaf17d4ba7483659ee70b92f40a151ab6036336f2302f7c3c5b6737a518833d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="productId")
    def product_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "productId"))

    @product_id.setter
    def product_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fdc24338939ce2f38568e875e7862403990a717daa10b184b123c2fe274fcb2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "productId", value)

    @builtins.property
    @jsii.member(jsii_name="ruleFormat")
    def rule_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleFormat"))

    @rule_format.setter
    def rule_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31e09db82f0b502ca1de3e581e22031ebc6a44343c42bc831a85aff86be2f395)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleFormat", value)

    @builtins.property
    @jsii.member(jsii_name="rules")
    def rules(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rules"))

    @rules.setter
    def rules(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ca1d629df30e9b80ea351b0efd29b2212b9aeba217ec44caf94d171c86f1cc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rules", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f08f78e79c6006633432b3dbceb364a9fba0aa6102f1e7c44029e21c6f611d32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="akamai.propertyInclude.PropertyIncludeConfig",
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
        "rule_format": "ruleFormat",
        "type": "type",
        "id": "id",
        "product_id": "productId",
        "rules": "rules",
    },
)
class PropertyIncludeConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        rule_format: builtins.str,
        type: builtins.str,
        id: typing.Optional[builtins.str] = None,
        product_id: typing.Optional[builtins.str] = None,
        rules: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param contract_id: Identifies the contract to which the include is assigned. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include#contract_id PropertyInclude#contract_id}
        :param group_id: Identifies the group to which the include is assigned. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include#group_id PropertyInclude#group_id}
        :param name: A descriptive name for the include. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include#name PropertyInclude#name}
        :param rule_format: Indicates the versioned set of features and criteria. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include#rule_format PropertyInclude#rule_format}
        :param type: Specifies the type of the include, either 'MICROSERVICES' or 'COMMON_SETTINGS'. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include#type PropertyInclude#type}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include#id PropertyInclude#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param product_id: The product assigned to the include. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include#product_id PropertyInclude#product_id}
        :param rules: Property Rules as JSON. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include#rules PropertyInclude#rules}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cdbb5b466d3a8d5314e7d4974114e4b44ca72372aac6f2ef5ba6bed00f34bc3)
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
            check_type(argname="argument rule_format", value=rule_format, expected_type=type_hints["rule_format"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument product_id", value=product_id, expected_type=type_hints["product_id"])
            check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "contract_id": contract_id,
            "group_id": group_id,
            "name": name,
            "rule_format": rule_format,
            "type": type,
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
        if id is not None:
            self._values["id"] = id
        if product_id is not None:
            self._values["product_id"] = product_id
        if rules is not None:
            self._values["rules"] = rules

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
        '''Identifies the contract to which the include is assigned.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include#contract_id PropertyInclude#contract_id}
        '''
        result = self._values.get("contract_id")
        assert result is not None, "Required property 'contract_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_id(self) -> builtins.str:
        '''Identifies the group to which the include is assigned.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include#group_id PropertyInclude#group_id}
        '''
        result = self._values.get("group_id")
        assert result is not None, "Required property 'group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A descriptive name for the include.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include#name PropertyInclude#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_format(self) -> builtins.str:
        '''Indicates the versioned set of features and criteria.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include#rule_format PropertyInclude#rule_format}
        '''
        result = self._values.get("rule_format")
        assert result is not None, "Required property 'rule_format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Specifies the type of the include, either 'MICROSERVICES' or 'COMMON_SETTINGS'.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include#type PropertyInclude#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include#id PropertyInclude#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def product_id(self) -> typing.Optional[builtins.str]:
        '''The product assigned to the include.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include#product_id PropertyInclude#product_id}
        '''
        result = self._values.get("product_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rules(self) -> typing.Optional[builtins.str]:
        '''Property Rules as JSON.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include#rules PropertyInclude#rules}
        '''
        result = self._values.get("rules")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PropertyIncludeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "PropertyInclude",
    "PropertyIncludeConfig",
]

publication.publish()

def _typecheckingstub__56857270342cfc448354804452e205cc53de2f9b112dba67914edfcc0be6af50(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    contract_id: builtins.str,
    group_id: builtins.str,
    name: builtins.str,
    rule_format: builtins.str,
    type: builtins.str,
    id: typing.Optional[builtins.str] = None,
    product_id: typing.Optional[builtins.str] = None,
    rules: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__422489099c01fae6cab942b20a4f030a313c5db4b1d2c74e7093bfc6e6cde14b(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a68bc3fd00ffed84bb160e042eb0be3c54b2cacf9335548ba8f8abb0a558b5f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2786c0afd8c426804ef415788e7d7636263062c52cdea2075824672a8a0b3d39(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b3d252905b731ac790f9fd89e49fdc02481780188f91834ac0652192e40426c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebaf17d4ba7483659ee70b92f40a151ab6036336f2302f7c3c5b6737a518833d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fdc24338939ce2f38568e875e7862403990a717daa10b184b123c2fe274fcb2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31e09db82f0b502ca1de3e581e22031ebc6a44343c42bc831a85aff86be2f395(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ca1d629df30e9b80ea351b0efd29b2212b9aeba217ec44caf94d171c86f1cc0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f08f78e79c6006633432b3dbceb364a9fba0aa6102f1e7c44029e21c6f611d32(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cdbb5b466d3a8d5314e7d4974114e4b44ca72372aac6f2ef5ba6bed00f34bc3(
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
    rule_format: builtins.str,
    type: builtins.str,
    id: typing.Optional[builtins.str] = None,
    product_id: typing.Optional[builtins.str] = None,
    rules: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
