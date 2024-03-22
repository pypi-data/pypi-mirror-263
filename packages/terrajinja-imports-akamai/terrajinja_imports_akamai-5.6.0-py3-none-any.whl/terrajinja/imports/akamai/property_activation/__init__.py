'''
# `akamai_property_activation`

Refer to the Terraform Registry for docs: [`akamai_property_activation`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation).
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


class PropertyActivation(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.propertyActivation.PropertyActivation",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation akamai_property_activation}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        contact: typing.Sequence[builtins.str],
        property_id: builtins.str,
        version: jsii.Number,
        activation_id: typing.Optional[builtins.str] = None,
        auto_acknowledge_rule_warnings: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        compliance_record: typing.Optional[typing.Union["PropertyActivationComplianceRecord", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        network: typing.Optional[builtins.str] = None,
        note: typing.Optional[builtins.str] = None,
        rule_errors: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PropertyActivationRuleErrors", typing.Dict[builtins.str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["PropertyActivationTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation akamai_property_activation} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param contact: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#contact PropertyActivation#contact}.
        :param property_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#property_id PropertyActivation#property_id}.
        :param version: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#version PropertyActivation#version}.
        :param activation_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#activation_id PropertyActivation#activation_id}.
        :param auto_acknowledge_rule_warnings: Automatically acknowledge all rule warnings for activation to continue. Default is false. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#auto_acknowledge_rule_warnings PropertyActivation#auto_acknowledge_rule_warnings}
        :param compliance_record: compliance_record block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#compliance_record PropertyActivation#compliance_record}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#id PropertyActivation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param network: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#network PropertyActivation#network}.
        :param note: assigns a log message to the activation request. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#note PropertyActivation#note}
        :param rule_errors: rule_errors block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#rule_errors PropertyActivation#rule_errors}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#timeouts PropertyActivation#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4b65d7c112b2f637948dfa5b8d6a3b435ce3708758082b5e8e25e468e9ad945)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = PropertyActivationConfig(
            contact=contact,
            property_id=property_id,
            version=version,
            activation_id=activation_id,
            auto_acknowledge_rule_warnings=auto_acknowledge_rule_warnings,
            compliance_record=compliance_record,
            id=id,
            network=network,
            note=note,
            rule_errors=rule_errors,
            timeouts=timeouts,
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
        '''Generates CDKTF code for importing a PropertyActivation resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the PropertyActivation to import.
        :param import_from_id: The id of the existing PropertyActivation that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the PropertyActivation to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__251b0bd534a8ebb58fa806864022e2ab82b84785d513e96ce3f292f75bc7c9cf)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putComplianceRecord")
    def put_compliance_record(
        self,
        *,
        noncompliance_reason_emergency: typing.Optional[typing.Union["PropertyActivationComplianceRecordNoncomplianceReasonEmergency", typing.Dict[builtins.str, typing.Any]]] = None,
        noncompliance_reason_none: typing.Optional[typing.Union["PropertyActivationComplianceRecordNoncomplianceReasonNone", typing.Dict[builtins.str, typing.Any]]] = None,
        noncompliance_reason_no_production_traffic: typing.Optional[typing.Union["PropertyActivationComplianceRecordNoncomplianceReasonNoProductionTraffic", typing.Dict[builtins.str, typing.Any]]] = None,
        noncompliance_reason_other: typing.Optional[typing.Union["PropertyActivationComplianceRecordNoncomplianceReasonOther", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param noncompliance_reason_emergency: noncompliance_reason_emergency block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#noncompliance_reason_emergency PropertyActivation#noncompliance_reason_emergency}
        :param noncompliance_reason_none: noncompliance_reason_none block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#noncompliance_reason_none PropertyActivation#noncompliance_reason_none}
        :param noncompliance_reason_no_production_traffic: noncompliance_reason_no_production_traffic block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#noncompliance_reason_no_production_traffic PropertyActivation#noncompliance_reason_no_production_traffic}
        :param noncompliance_reason_other: noncompliance_reason_other block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#noncompliance_reason_other PropertyActivation#noncompliance_reason_other}
        '''
        value = PropertyActivationComplianceRecord(
            noncompliance_reason_emergency=noncompliance_reason_emergency,
            noncompliance_reason_none=noncompliance_reason_none,
            noncompliance_reason_no_production_traffic=noncompliance_reason_no_production_traffic,
            noncompliance_reason_other=noncompliance_reason_other,
        )

        return typing.cast(None, jsii.invoke(self, "putComplianceRecord", [value]))

    @jsii.member(jsii_name="putRuleErrors")
    def put_rule_errors(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PropertyActivationRuleErrors", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60b5f47059067316c54204b52bac07aa445918a77011bb38b6d4b89e4ce37d9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRuleErrors", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self, *, default: typing.Optional[builtins.str] = None) -> None:
        '''
        :param default: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#default PropertyActivation#default}.
        '''
        value = PropertyActivationTimeouts(default=default)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetActivationId")
    def reset_activation_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActivationId", []))

    @jsii.member(jsii_name="resetAutoAcknowledgeRuleWarnings")
    def reset_auto_acknowledge_rule_warnings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoAcknowledgeRuleWarnings", []))

    @jsii.member(jsii_name="resetComplianceRecord")
    def reset_compliance_record(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComplianceRecord", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNetwork")
    def reset_network(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetwork", []))

    @jsii.member(jsii_name="resetNote")
    def reset_note(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNote", []))

    @jsii.member(jsii_name="resetRuleErrors")
    def reset_rule_errors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuleErrors", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

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
    @jsii.member(jsii_name="complianceRecord")
    def compliance_record(self) -> "PropertyActivationComplianceRecordOutputReference":
        return typing.cast("PropertyActivationComplianceRecordOutputReference", jsii.get(self, "complianceRecord"))

    @builtins.property
    @jsii.member(jsii_name="errors")
    def errors(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "errors"))

    @builtins.property
    @jsii.member(jsii_name="ruleErrors")
    def rule_errors(self) -> "PropertyActivationRuleErrorsList":
        return typing.cast("PropertyActivationRuleErrorsList", jsii.get(self, "ruleErrors"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "PropertyActivationTimeoutsOutputReference":
        return typing.cast("PropertyActivationTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="warnings")
    def warnings(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "warnings"))

    @builtins.property
    @jsii.member(jsii_name="activationIdInput")
    def activation_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "activationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="autoAcknowledgeRuleWarningsInput")
    def auto_acknowledge_rule_warnings_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "autoAcknowledgeRuleWarningsInput"))

    @builtins.property
    @jsii.member(jsii_name="complianceRecordInput")
    def compliance_record_input(
        self,
    ) -> typing.Optional["PropertyActivationComplianceRecord"]:
        return typing.cast(typing.Optional["PropertyActivationComplianceRecord"], jsii.get(self, "complianceRecordInput"))

    @builtins.property
    @jsii.member(jsii_name="contactInput")
    def contact_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "contactInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInput")
    def network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkInput"))

    @builtins.property
    @jsii.member(jsii_name="noteInput")
    def note_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "noteInput"))

    @builtins.property
    @jsii.member(jsii_name="propertyIdInput")
    def property_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "propertyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleErrorsInput")
    def rule_errors_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PropertyActivationRuleErrors"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PropertyActivationRuleErrors"]]], jsii.get(self, "ruleErrorsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(self) -> typing.Optional["PropertyActivationTimeouts"]:
        return typing.cast(typing.Optional["PropertyActivationTimeouts"], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="activationId")
    def activation_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "activationId"))

    @activation_id.setter
    def activation_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6afefff1726c3af6e53135dd22015a0290a3d0aad0021257e221be55edab0505)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "activationId", value)

    @builtins.property
    @jsii.member(jsii_name="autoAcknowledgeRuleWarnings")
    def auto_acknowledge_rule_warnings(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "autoAcknowledgeRuleWarnings"))

    @auto_acknowledge_rule_warnings.setter
    def auto_acknowledge_rule_warnings(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d97ef7545d8cb9ecc115980925b0b48301ef38a90f025914cee1d76cb48b3a1e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoAcknowledgeRuleWarnings", value)

    @builtins.property
    @jsii.member(jsii_name="contact")
    def contact(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "contact"))

    @contact.setter
    def contact(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4269d733aec0a5a244a83b0f95180dc0b472bd30627a74b206521ad9271945ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contact", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48e9684b23e1a437767958d9b10d073648735291fe5dd80b9e23ce07f2246992)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "network"))

    @network.setter
    def network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2519ccdf9b9883b30ad67b305842c4a1c7aa05f030ce339af2f04a141cd44e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "network", value)

    @builtins.property
    @jsii.member(jsii_name="note")
    def note(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "note"))

    @note.setter
    def note(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4ff9612888834fcd6119039b662a7b99589462dcb6b1b5fc74147cbfdcc7d1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "note", value)

    @builtins.property
    @jsii.member(jsii_name="propertyId")
    def property_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "propertyId"))

    @property_id.setter
    def property_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb4d35f4772fad257539624a064b3e8df8ac3128c92bb78ca948e934ba97473c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "propertyId", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "version"))

    @version.setter
    def version(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fa9b7e343b91d44fc961edf901e7557d191f9db8407e67ec7d6cdc10d91e3fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)


@jsii.data_type(
    jsii_type="akamai.propertyActivation.PropertyActivationComplianceRecord",
    jsii_struct_bases=[],
    name_mapping={
        "noncompliance_reason_emergency": "noncomplianceReasonEmergency",
        "noncompliance_reason_none": "noncomplianceReasonNone",
        "noncompliance_reason_no_production_traffic": "noncomplianceReasonNoProductionTraffic",
        "noncompliance_reason_other": "noncomplianceReasonOther",
    },
)
class PropertyActivationComplianceRecord:
    def __init__(
        self,
        *,
        noncompliance_reason_emergency: typing.Optional[typing.Union["PropertyActivationComplianceRecordNoncomplianceReasonEmergency", typing.Dict[builtins.str, typing.Any]]] = None,
        noncompliance_reason_none: typing.Optional[typing.Union["PropertyActivationComplianceRecordNoncomplianceReasonNone", typing.Dict[builtins.str, typing.Any]]] = None,
        noncompliance_reason_no_production_traffic: typing.Optional[typing.Union["PropertyActivationComplianceRecordNoncomplianceReasonNoProductionTraffic", typing.Dict[builtins.str, typing.Any]]] = None,
        noncompliance_reason_other: typing.Optional[typing.Union["PropertyActivationComplianceRecordNoncomplianceReasonOther", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param noncompliance_reason_emergency: noncompliance_reason_emergency block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#noncompliance_reason_emergency PropertyActivation#noncompliance_reason_emergency}
        :param noncompliance_reason_none: noncompliance_reason_none block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#noncompliance_reason_none PropertyActivation#noncompliance_reason_none}
        :param noncompliance_reason_no_production_traffic: noncompliance_reason_no_production_traffic block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#noncompliance_reason_no_production_traffic PropertyActivation#noncompliance_reason_no_production_traffic}
        :param noncompliance_reason_other: noncompliance_reason_other block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#noncompliance_reason_other PropertyActivation#noncompliance_reason_other}
        '''
        if isinstance(noncompliance_reason_emergency, dict):
            noncompliance_reason_emergency = PropertyActivationComplianceRecordNoncomplianceReasonEmergency(**noncompliance_reason_emergency)
        if isinstance(noncompliance_reason_none, dict):
            noncompliance_reason_none = PropertyActivationComplianceRecordNoncomplianceReasonNone(**noncompliance_reason_none)
        if isinstance(noncompliance_reason_no_production_traffic, dict):
            noncompliance_reason_no_production_traffic = PropertyActivationComplianceRecordNoncomplianceReasonNoProductionTraffic(**noncompliance_reason_no_production_traffic)
        if isinstance(noncompliance_reason_other, dict):
            noncompliance_reason_other = PropertyActivationComplianceRecordNoncomplianceReasonOther(**noncompliance_reason_other)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c23c0509c3f03a2d8e8f104f3306601432ff2bfc825668944e66c11ae959896)
            check_type(argname="argument noncompliance_reason_emergency", value=noncompliance_reason_emergency, expected_type=type_hints["noncompliance_reason_emergency"])
            check_type(argname="argument noncompliance_reason_none", value=noncompliance_reason_none, expected_type=type_hints["noncompliance_reason_none"])
            check_type(argname="argument noncompliance_reason_no_production_traffic", value=noncompliance_reason_no_production_traffic, expected_type=type_hints["noncompliance_reason_no_production_traffic"])
            check_type(argname="argument noncompliance_reason_other", value=noncompliance_reason_other, expected_type=type_hints["noncompliance_reason_other"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if noncompliance_reason_emergency is not None:
            self._values["noncompliance_reason_emergency"] = noncompliance_reason_emergency
        if noncompliance_reason_none is not None:
            self._values["noncompliance_reason_none"] = noncompliance_reason_none
        if noncompliance_reason_no_production_traffic is not None:
            self._values["noncompliance_reason_no_production_traffic"] = noncompliance_reason_no_production_traffic
        if noncompliance_reason_other is not None:
            self._values["noncompliance_reason_other"] = noncompliance_reason_other

    @builtins.property
    def noncompliance_reason_emergency(
        self,
    ) -> typing.Optional["PropertyActivationComplianceRecordNoncomplianceReasonEmergency"]:
        '''noncompliance_reason_emergency block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#noncompliance_reason_emergency PropertyActivation#noncompliance_reason_emergency}
        '''
        result = self._values.get("noncompliance_reason_emergency")
        return typing.cast(typing.Optional["PropertyActivationComplianceRecordNoncomplianceReasonEmergency"], result)

    @builtins.property
    def noncompliance_reason_none(
        self,
    ) -> typing.Optional["PropertyActivationComplianceRecordNoncomplianceReasonNone"]:
        '''noncompliance_reason_none block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#noncompliance_reason_none PropertyActivation#noncompliance_reason_none}
        '''
        result = self._values.get("noncompliance_reason_none")
        return typing.cast(typing.Optional["PropertyActivationComplianceRecordNoncomplianceReasonNone"], result)

    @builtins.property
    def noncompliance_reason_no_production_traffic(
        self,
    ) -> typing.Optional["PropertyActivationComplianceRecordNoncomplianceReasonNoProductionTraffic"]:
        '''noncompliance_reason_no_production_traffic block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#noncompliance_reason_no_production_traffic PropertyActivation#noncompliance_reason_no_production_traffic}
        '''
        result = self._values.get("noncompliance_reason_no_production_traffic")
        return typing.cast(typing.Optional["PropertyActivationComplianceRecordNoncomplianceReasonNoProductionTraffic"], result)

    @builtins.property
    def noncompliance_reason_other(
        self,
    ) -> typing.Optional["PropertyActivationComplianceRecordNoncomplianceReasonOther"]:
        '''noncompliance_reason_other block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#noncompliance_reason_other PropertyActivation#noncompliance_reason_other}
        '''
        result = self._values.get("noncompliance_reason_other")
        return typing.cast(typing.Optional["PropertyActivationComplianceRecordNoncomplianceReasonOther"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PropertyActivationComplianceRecord(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.propertyActivation.PropertyActivationComplianceRecordNoncomplianceReasonEmergency",
    jsii_struct_bases=[],
    name_mapping={"ticket_id": "ticketId"},
)
class PropertyActivationComplianceRecordNoncomplianceReasonEmergency:
    def __init__(self, *, ticket_id: typing.Optional[builtins.str] = None) -> None:
        '''
        :param ticket_id: Identifies the ticket that describes the need for the activation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#ticket_id PropertyActivation#ticket_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccaead67a7e7528a8238c11ac3e72c110c03be97f35260b912f7fdca5c694296)
            check_type(argname="argument ticket_id", value=ticket_id, expected_type=type_hints["ticket_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ticket_id is not None:
            self._values["ticket_id"] = ticket_id

    @builtins.property
    def ticket_id(self) -> typing.Optional[builtins.str]:
        '''Identifies the ticket that describes the need for the activation.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#ticket_id PropertyActivation#ticket_id}
        '''
        result = self._values.get("ticket_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PropertyActivationComplianceRecordNoncomplianceReasonEmergency(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PropertyActivationComplianceRecordNoncomplianceReasonEmergencyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.propertyActivation.PropertyActivationComplianceRecordNoncomplianceReasonEmergencyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bd677a903d5954a4946df74429cda43a5ae54f4bdc4df9acae7d0400584e0e10)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetTicketId")
    def reset_ticket_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTicketId", []))

    @builtins.property
    @jsii.member(jsii_name="ticketIdInput")
    def ticket_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ticketIdInput"))

    @builtins.property
    @jsii.member(jsii_name="ticketId")
    def ticket_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ticketId"))

    @ticket_id.setter
    def ticket_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15a0f88b3d1c63a238e7799e676094202f3b42d72f17602ee03b9d843e1883ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ticketId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PropertyActivationComplianceRecordNoncomplianceReasonEmergency]:
        return typing.cast(typing.Optional[PropertyActivationComplianceRecordNoncomplianceReasonEmergency], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PropertyActivationComplianceRecordNoncomplianceReasonEmergency],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50442d71ef20b94943e4baf1dcd40db138b96653f1aa238a0bbddcfc754ed609)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.propertyActivation.PropertyActivationComplianceRecordNoncomplianceReasonNoProductionTraffic",
    jsii_struct_bases=[],
    name_mapping={"ticket_id": "ticketId"},
)
class PropertyActivationComplianceRecordNoncomplianceReasonNoProductionTraffic:
    def __init__(self, *, ticket_id: typing.Optional[builtins.str] = None) -> None:
        '''
        :param ticket_id: Identifies the ticket that describes the need for the activation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#ticket_id PropertyActivation#ticket_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b956c4df3519be14e1c6f819769e01d35b9bf1341d9cb437b6c257aebc15035)
            check_type(argname="argument ticket_id", value=ticket_id, expected_type=type_hints["ticket_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ticket_id is not None:
            self._values["ticket_id"] = ticket_id

    @builtins.property
    def ticket_id(self) -> typing.Optional[builtins.str]:
        '''Identifies the ticket that describes the need for the activation.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#ticket_id PropertyActivation#ticket_id}
        '''
        result = self._values.get("ticket_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PropertyActivationComplianceRecordNoncomplianceReasonNoProductionTraffic(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PropertyActivationComplianceRecordNoncomplianceReasonNoProductionTrafficOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.propertyActivation.PropertyActivationComplianceRecordNoncomplianceReasonNoProductionTrafficOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__308f022f797fc2d2281185d15bbf84919d226f9a8296166d3287137521ff8e9f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetTicketId")
    def reset_ticket_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTicketId", []))

    @builtins.property
    @jsii.member(jsii_name="ticketIdInput")
    def ticket_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ticketIdInput"))

    @builtins.property
    @jsii.member(jsii_name="ticketId")
    def ticket_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ticketId"))

    @ticket_id.setter
    def ticket_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da1f3f3d2ad81f31ce4a94b4edbb754c318bb8b2c71612f04bc7f4f0eb628bd8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ticketId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PropertyActivationComplianceRecordNoncomplianceReasonNoProductionTraffic]:
        return typing.cast(typing.Optional[PropertyActivationComplianceRecordNoncomplianceReasonNoProductionTraffic], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PropertyActivationComplianceRecordNoncomplianceReasonNoProductionTraffic],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__030bb1bd9b660767ee1a5cdef323ffcd58e78267e402bcb493e13bb2532ec82d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.propertyActivation.PropertyActivationComplianceRecordNoncomplianceReasonNone",
    jsii_struct_bases=[],
    name_mapping={
        "customer_email": "customerEmail",
        "peer_reviewed_by": "peerReviewedBy",
        "ticket_id": "ticketId",
        "unit_tested": "unitTested",
    },
)
class PropertyActivationComplianceRecordNoncomplianceReasonNone:
    def __init__(
        self,
        *,
        customer_email: typing.Optional[builtins.str] = None,
        peer_reviewed_by: typing.Optional[builtins.str] = None,
        ticket_id: typing.Optional[builtins.str] = None,
        unit_tested: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param customer_email: Identifies the customer. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#customer_email PropertyActivation#customer_email}
        :param peer_reviewed_by: Identifies person who has independently approved the activation request. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#peer_reviewed_by PropertyActivation#peer_reviewed_by}
        :param ticket_id: Identifies the ticket that describes the need for the activation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#ticket_id PropertyActivation#ticket_id}
        :param unit_tested: Whether the metadata to activate has been fully tested. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#unit_tested PropertyActivation#unit_tested}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ab1a982a4278403ee9fd22bbd94360db4bae4531757dd122216a21115b7db9d)
            check_type(argname="argument customer_email", value=customer_email, expected_type=type_hints["customer_email"])
            check_type(argname="argument peer_reviewed_by", value=peer_reviewed_by, expected_type=type_hints["peer_reviewed_by"])
            check_type(argname="argument ticket_id", value=ticket_id, expected_type=type_hints["ticket_id"])
            check_type(argname="argument unit_tested", value=unit_tested, expected_type=type_hints["unit_tested"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if customer_email is not None:
            self._values["customer_email"] = customer_email
        if peer_reviewed_by is not None:
            self._values["peer_reviewed_by"] = peer_reviewed_by
        if ticket_id is not None:
            self._values["ticket_id"] = ticket_id
        if unit_tested is not None:
            self._values["unit_tested"] = unit_tested

    @builtins.property
    def customer_email(self) -> typing.Optional[builtins.str]:
        '''Identifies the customer.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#customer_email PropertyActivation#customer_email}
        '''
        result = self._values.get("customer_email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def peer_reviewed_by(self) -> typing.Optional[builtins.str]:
        '''Identifies person who has independently approved the activation request.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#peer_reviewed_by PropertyActivation#peer_reviewed_by}
        '''
        result = self._values.get("peer_reviewed_by")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ticket_id(self) -> typing.Optional[builtins.str]:
        '''Identifies the ticket that describes the need for the activation.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#ticket_id PropertyActivation#ticket_id}
        '''
        result = self._values.get("ticket_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def unit_tested(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether the metadata to activate has been fully tested.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#unit_tested PropertyActivation#unit_tested}
        '''
        result = self._values.get("unit_tested")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PropertyActivationComplianceRecordNoncomplianceReasonNone(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PropertyActivationComplianceRecordNoncomplianceReasonNoneOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.propertyActivation.PropertyActivationComplianceRecordNoncomplianceReasonNoneOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__01fd6e94c8d4e0cdb189bef2402581c7abd58afe71e822db13898abc693b7b57)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCustomerEmail")
    def reset_customer_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomerEmail", []))

    @jsii.member(jsii_name="resetPeerReviewedBy")
    def reset_peer_reviewed_by(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeerReviewedBy", []))

    @jsii.member(jsii_name="resetTicketId")
    def reset_ticket_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTicketId", []))

    @jsii.member(jsii_name="resetUnitTested")
    def reset_unit_tested(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnitTested", []))

    @builtins.property
    @jsii.member(jsii_name="customerEmailInput")
    def customer_email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customerEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="peerReviewedByInput")
    def peer_reviewed_by_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "peerReviewedByInput"))

    @builtins.property
    @jsii.member(jsii_name="ticketIdInput")
    def ticket_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ticketIdInput"))

    @builtins.property
    @jsii.member(jsii_name="unitTestedInput")
    def unit_tested_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "unitTestedInput"))

    @builtins.property
    @jsii.member(jsii_name="customerEmail")
    def customer_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customerEmail"))

    @customer_email.setter
    def customer_email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c4d1ed872fbe8be9c56014473a54ae82f3cb8b52ace23c7da7b68e70904fc25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customerEmail", value)

    @builtins.property
    @jsii.member(jsii_name="peerReviewedBy")
    def peer_reviewed_by(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "peerReviewedBy"))

    @peer_reviewed_by.setter
    def peer_reviewed_by(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__991205fab8c665585d06065ebd2ccb7fc68935e04afd0d2a33f4771f758a5963)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "peerReviewedBy", value)

    @builtins.property
    @jsii.member(jsii_name="ticketId")
    def ticket_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ticketId"))

    @ticket_id.setter
    def ticket_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f5ddf503fb5ef02cfc7c75877d2da328e58e131abfe5e4d424e32d8c9bb000d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ticketId", value)

    @builtins.property
    @jsii.member(jsii_name="unitTested")
    def unit_tested(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "unitTested"))

    @unit_tested.setter
    def unit_tested(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6090f151649d9ac03463a14567ae5e8484f9d334361e60037b82478708a0bd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unitTested", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PropertyActivationComplianceRecordNoncomplianceReasonNone]:
        return typing.cast(typing.Optional[PropertyActivationComplianceRecordNoncomplianceReasonNone], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PropertyActivationComplianceRecordNoncomplianceReasonNone],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7383db1c03c7544d2536cd564de7220468d537e1588e0d77a4aaedab6366a644)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.propertyActivation.PropertyActivationComplianceRecordNoncomplianceReasonOther",
    jsii_struct_bases=[],
    name_mapping={
        "other_noncompliance_reason": "otherNoncomplianceReason",
        "ticket_id": "ticketId",
    },
)
class PropertyActivationComplianceRecordNoncomplianceReasonOther:
    def __init__(
        self,
        *,
        other_noncompliance_reason: typing.Optional[builtins.str] = None,
        ticket_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param other_noncompliance_reason: Describes the reason why the activation must occur immediately, out of compliance with the standard procedure. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#other_noncompliance_reason PropertyActivation#other_noncompliance_reason}
        :param ticket_id: Identifies the ticket that describes the need for the activation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#ticket_id PropertyActivation#ticket_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c6b54b29a50d322d93c5353393ad5c01a14751f56f47f23a292512f5507ebe7)
            check_type(argname="argument other_noncompliance_reason", value=other_noncompliance_reason, expected_type=type_hints["other_noncompliance_reason"])
            check_type(argname="argument ticket_id", value=ticket_id, expected_type=type_hints["ticket_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if other_noncompliance_reason is not None:
            self._values["other_noncompliance_reason"] = other_noncompliance_reason
        if ticket_id is not None:
            self._values["ticket_id"] = ticket_id

    @builtins.property
    def other_noncompliance_reason(self) -> typing.Optional[builtins.str]:
        '''Describes the reason why the activation must occur immediately, out of compliance with the standard procedure.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#other_noncompliance_reason PropertyActivation#other_noncompliance_reason}
        '''
        result = self._values.get("other_noncompliance_reason")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ticket_id(self) -> typing.Optional[builtins.str]:
        '''Identifies the ticket that describes the need for the activation.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#ticket_id PropertyActivation#ticket_id}
        '''
        result = self._values.get("ticket_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PropertyActivationComplianceRecordNoncomplianceReasonOther(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PropertyActivationComplianceRecordNoncomplianceReasonOtherOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.propertyActivation.PropertyActivationComplianceRecordNoncomplianceReasonOtherOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8f94017619834faf15580aa0bf6017c9bc27177f052ed92b60ea4a28e0e2b61c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetOtherNoncomplianceReason")
    def reset_other_noncompliance_reason(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOtherNoncomplianceReason", []))

    @jsii.member(jsii_name="resetTicketId")
    def reset_ticket_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTicketId", []))

    @builtins.property
    @jsii.member(jsii_name="otherNoncomplianceReasonInput")
    def other_noncompliance_reason_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "otherNoncomplianceReasonInput"))

    @builtins.property
    @jsii.member(jsii_name="ticketIdInput")
    def ticket_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ticketIdInput"))

    @builtins.property
    @jsii.member(jsii_name="otherNoncomplianceReason")
    def other_noncompliance_reason(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "otherNoncomplianceReason"))

    @other_noncompliance_reason.setter
    def other_noncompliance_reason(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24ebc0b3258bad166ebb4501754aad3f474397c950dabd3b0c26fb114ae05d85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "otherNoncomplianceReason", value)

    @builtins.property
    @jsii.member(jsii_name="ticketId")
    def ticket_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ticketId"))

    @ticket_id.setter
    def ticket_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db8c9c613fe2a31eae9b6c8c1be146a8dfab8a03d2d65764cb44d8ee39a241d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ticketId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PropertyActivationComplianceRecordNoncomplianceReasonOther]:
        return typing.cast(typing.Optional[PropertyActivationComplianceRecordNoncomplianceReasonOther], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PropertyActivationComplianceRecordNoncomplianceReasonOther],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__230058b406f05efc92813de52bc71ed9d02a6dbfc6e9750282e4d67601efe6b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PropertyActivationComplianceRecordOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.propertyActivation.PropertyActivationComplianceRecordOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0fcba7b86fcb5862bc0cd26eea3f5ac7af644925601b89c3b54ed932f7508cf4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putNoncomplianceReasonEmergency")
    def put_noncompliance_reason_emergency(
        self,
        *,
        ticket_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ticket_id: Identifies the ticket that describes the need for the activation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#ticket_id PropertyActivation#ticket_id}
        '''
        value = PropertyActivationComplianceRecordNoncomplianceReasonEmergency(
            ticket_id=ticket_id
        )

        return typing.cast(None, jsii.invoke(self, "putNoncomplianceReasonEmergency", [value]))

    @jsii.member(jsii_name="putNoncomplianceReasonNone")
    def put_noncompliance_reason_none(
        self,
        *,
        customer_email: typing.Optional[builtins.str] = None,
        peer_reviewed_by: typing.Optional[builtins.str] = None,
        ticket_id: typing.Optional[builtins.str] = None,
        unit_tested: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param customer_email: Identifies the customer. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#customer_email PropertyActivation#customer_email}
        :param peer_reviewed_by: Identifies person who has independently approved the activation request. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#peer_reviewed_by PropertyActivation#peer_reviewed_by}
        :param ticket_id: Identifies the ticket that describes the need for the activation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#ticket_id PropertyActivation#ticket_id}
        :param unit_tested: Whether the metadata to activate has been fully tested. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#unit_tested PropertyActivation#unit_tested}
        '''
        value = PropertyActivationComplianceRecordNoncomplianceReasonNone(
            customer_email=customer_email,
            peer_reviewed_by=peer_reviewed_by,
            ticket_id=ticket_id,
            unit_tested=unit_tested,
        )

        return typing.cast(None, jsii.invoke(self, "putNoncomplianceReasonNone", [value]))

    @jsii.member(jsii_name="putNoncomplianceReasonNoProductionTraffic")
    def put_noncompliance_reason_no_production_traffic(
        self,
        *,
        ticket_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ticket_id: Identifies the ticket that describes the need for the activation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#ticket_id PropertyActivation#ticket_id}
        '''
        value = PropertyActivationComplianceRecordNoncomplianceReasonNoProductionTraffic(
            ticket_id=ticket_id
        )

        return typing.cast(None, jsii.invoke(self, "putNoncomplianceReasonNoProductionTraffic", [value]))

    @jsii.member(jsii_name="putNoncomplianceReasonOther")
    def put_noncompliance_reason_other(
        self,
        *,
        other_noncompliance_reason: typing.Optional[builtins.str] = None,
        ticket_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param other_noncompliance_reason: Describes the reason why the activation must occur immediately, out of compliance with the standard procedure. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#other_noncompliance_reason PropertyActivation#other_noncompliance_reason}
        :param ticket_id: Identifies the ticket that describes the need for the activation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#ticket_id PropertyActivation#ticket_id}
        '''
        value = PropertyActivationComplianceRecordNoncomplianceReasonOther(
            other_noncompliance_reason=other_noncompliance_reason, ticket_id=ticket_id
        )

        return typing.cast(None, jsii.invoke(self, "putNoncomplianceReasonOther", [value]))

    @jsii.member(jsii_name="resetNoncomplianceReasonEmergency")
    def reset_noncompliance_reason_emergency(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoncomplianceReasonEmergency", []))

    @jsii.member(jsii_name="resetNoncomplianceReasonNone")
    def reset_noncompliance_reason_none(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoncomplianceReasonNone", []))

    @jsii.member(jsii_name="resetNoncomplianceReasonNoProductionTraffic")
    def reset_noncompliance_reason_no_production_traffic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoncomplianceReasonNoProductionTraffic", []))

    @jsii.member(jsii_name="resetNoncomplianceReasonOther")
    def reset_noncompliance_reason_other(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoncomplianceReasonOther", []))

    @builtins.property
    @jsii.member(jsii_name="noncomplianceReasonEmergency")
    def noncompliance_reason_emergency(
        self,
    ) -> PropertyActivationComplianceRecordNoncomplianceReasonEmergencyOutputReference:
        return typing.cast(PropertyActivationComplianceRecordNoncomplianceReasonEmergencyOutputReference, jsii.get(self, "noncomplianceReasonEmergency"))

    @builtins.property
    @jsii.member(jsii_name="noncomplianceReasonNone")
    def noncompliance_reason_none(
        self,
    ) -> PropertyActivationComplianceRecordNoncomplianceReasonNoneOutputReference:
        return typing.cast(PropertyActivationComplianceRecordNoncomplianceReasonNoneOutputReference, jsii.get(self, "noncomplianceReasonNone"))

    @builtins.property
    @jsii.member(jsii_name="noncomplianceReasonNoProductionTraffic")
    def noncompliance_reason_no_production_traffic(
        self,
    ) -> PropertyActivationComplianceRecordNoncomplianceReasonNoProductionTrafficOutputReference:
        return typing.cast(PropertyActivationComplianceRecordNoncomplianceReasonNoProductionTrafficOutputReference, jsii.get(self, "noncomplianceReasonNoProductionTraffic"))

    @builtins.property
    @jsii.member(jsii_name="noncomplianceReasonOther")
    def noncompliance_reason_other(
        self,
    ) -> PropertyActivationComplianceRecordNoncomplianceReasonOtherOutputReference:
        return typing.cast(PropertyActivationComplianceRecordNoncomplianceReasonOtherOutputReference, jsii.get(self, "noncomplianceReasonOther"))

    @builtins.property
    @jsii.member(jsii_name="noncomplianceReasonEmergencyInput")
    def noncompliance_reason_emergency_input(
        self,
    ) -> typing.Optional[PropertyActivationComplianceRecordNoncomplianceReasonEmergency]:
        return typing.cast(typing.Optional[PropertyActivationComplianceRecordNoncomplianceReasonEmergency], jsii.get(self, "noncomplianceReasonEmergencyInput"))

    @builtins.property
    @jsii.member(jsii_name="noncomplianceReasonNoneInput")
    def noncompliance_reason_none_input(
        self,
    ) -> typing.Optional[PropertyActivationComplianceRecordNoncomplianceReasonNone]:
        return typing.cast(typing.Optional[PropertyActivationComplianceRecordNoncomplianceReasonNone], jsii.get(self, "noncomplianceReasonNoneInput"))

    @builtins.property
    @jsii.member(jsii_name="noncomplianceReasonNoProductionTrafficInput")
    def noncompliance_reason_no_production_traffic_input(
        self,
    ) -> typing.Optional[PropertyActivationComplianceRecordNoncomplianceReasonNoProductionTraffic]:
        return typing.cast(typing.Optional[PropertyActivationComplianceRecordNoncomplianceReasonNoProductionTraffic], jsii.get(self, "noncomplianceReasonNoProductionTrafficInput"))

    @builtins.property
    @jsii.member(jsii_name="noncomplianceReasonOtherInput")
    def noncompliance_reason_other_input(
        self,
    ) -> typing.Optional[PropertyActivationComplianceRecordNoncomplianceReasonOther]:
        return typing.cast(typing.Optional[PropertyActivationComplianceRecordNoncomplianceReasonOther], jsii.get(self, "noncomplianceReasonOtherInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PropertyActivationComplianceRecord]:
        return typing.cast(typing.Optional[PropertyActivationComplianceRecord], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PropertyActivationComplianceRecord],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4da6e971f13d843058d9ace54916657cfcc5854191520180b2ffdae963e6a0ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.propertyActivation.PropertyActivationConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "contact": "contact",
        "property_id": "propertyId",
        "version": "version",
        "activation_id": "activationId",
        "auto_acknowledge_rule_warnings": "autoAcknowledgeRuleWarnings",
        "compliance_record": "complianceRecord",
        "id": "id",
        "network": "network",
        "note": "note",
        "rule_errors": "ruleErrors",
        "timeouts": "timeouts",
    },
)
class PropertyActivationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        contact: typing.Sequence[builtins.str],
        property_id: builtins.str,
        version: jsii.Number,
        activation_id: typing.Optional[builtins.str] = None,
        auto_acknowledge_rule_warnings: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        compliance_record: typing.Optional[typing.Union[PropertyActivationComplianceRecord, typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        network: typing.Optional[builtins.str] = None,
        note: typing.Optional[builtins.str] = None,
        rule_errors: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PropertyActivationRuleErrors", typing.Dict[builtins.str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["PropertyActivationTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param contact: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#contact PropertyActivation#contact}.
        :param property_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#property_id PropertyActivation#property_id}.
        :param version: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#version PropertyActivation#version}.
        :param activation_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#activation_id PropertyActivation#activation_id}.
        :param auto_acknowledge_rule_warnings: Automatically acknowledge all rule warnings for activation to continue. Default is false. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#auto_acknowledge_rule_warnings PropertyActivation#auto_acknowledge_rule_warnings}
        :param compliance_record: compliance_record block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#compliance_record PropertyActivation#compliance_record}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#id PropertyActivation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param network: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#network PropertyActivation#network}.
        :param note: assigns a log message to the activation request. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#note PropertyActivation#note}
        :param rule_errors: rule_errors block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#rule_errors PropertyActivation#rule_errors}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#timeouts PropertyActivation#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(compliance_record, dict):
            compliance_record = PropertyActivationComplianceRecord(**compliance_record)
        if isinstance(timeouts, dict):
            timeouts = PropertyActivationTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__baa959572e1ffc1c4fac3db6fec3bd7136055063e68b6af543969c35083fdc19)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument contact", value=contact, expected_type=type_hints["contact"])
            check_type(argname="argument property_id", value=property_id, expected_type=type_hints["property_id"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument activation_id", value=activation_id, expected_type=type_hints["activation_id"])
            check_type(argname="argument auto_acknowledge_rule_warnings", value=auto_acknowledge_rule_warnings, expected_type=type_hints["auto_acknowledge_rule_warnings"])
            check_type(argname="argument compliance_record", value=compliance_record, expected_type=type_hints["compliance_record"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument network", value=network, expected_type=type_hints["network"])
            check_type(argname="argument note", value=note, expected_type=type_hints["note"])
            check_type(argname="argument rule_errors", value=rule_errors, expected_type=type_hints["rule_errors"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "contact": contact,
            "property_id": property_id,
            "version": version,
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
        if activation_id is not None:
            self._values["activation_id"] = activation_id
        if auto_acknowledge_rule_warnings is not None:
            self._values["auto_acknowledge_rule_warnings"] = auto_acknowledge_rule_warnings
        if compliance_record is not None:
            self._values["compliance_record"] = compliance_record
        if id is not None:
            self._values["id"] = id
        if network is not None:
            self._values["network"] = network
        if note is not None:
            self._values["note"] = note
        if rule_errors is not None:
            self._values["rule_errors"] = rule_errors
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
    def contact(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#contact PropertyActivation#contact}.'''
        result = self._values.get("contact")
        assert result is not None, "Required property 'contact' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def property_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#property_id PropertyActivation#property_id}.'''
        result = self._values.get("property_id")
        assert result is not None, "Required property 'property_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#version PropertyActivation#version}.'''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def activation_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#activation_id PropertyActivation#activation_id}.'''
        result = self._values.get("activation_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auto_acknowledge_rule_warnings(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Automatically acknowledge all rule warnings for activation to continue. Default is false.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#auto_acknowledge_rule_warnings PropertyActivation#auto_acknowledge_rule_warnings}
        '''
        result = self._values.get("auto_acknowledge_rule_warnings")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def compliance_record(self) -> typing.Optional[PropertyActivationComplianceRecord]:
        '''compliance_record block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#compliance_record PropertyActivation#compliance_record}
        '''
        result = self._values.get("compliance_record")
        return typing.cast(typing.Optional[PropertyActivationComplianceRecord], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#id PropertyActivation#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#network PropertyActivation#network}.'''
        result = self._values.get("network")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def note(self) -> typing.Optional[builtins.str]:
        '''assigns a log message to the activation request.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#note PropertyActivation#note}
        '''
        result = self._values.get("note")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rule_errors(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PropertyActivationRuleErrors"]]]:
        '''rule_errors block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#rule_errors PropertyActivation#rule_errors}
        '''
        result = self._values.get("rule_errors")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PropertyActivationRuleErrors"]]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["PropertyActivationTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#timeouts PropertyActivation#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["PropertyActivationTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PropertyActivationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.propertyActivation.PropertyActivationRuleErrors",
    jsii_struct_bases=[],
    name_mapping={
        "behavior_name": "behaviorName",
        "detail": "detail",
        "error_location": "errorLocation",
        "instance": "instance",
        "status_code": "statusCode",
        "title": "title",
        "type": "type",
    },
)
class PropertyActivationRuleErrors:
    def __init__(
        self,
        *,
        behavior_name: typing.Optional[builtins.str] = None,
        detail: typing.Optional[builtins.str] = None,
        error_location: typing.Optional[builtins.str] = None,
        instance: typing.Optional[builtins.str] = None,
        status_code: typing.Optional[jsii.Number] = None,
        title: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param behavior_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#behavior_name PropertyActivation#behavior_name}.
        :param detail: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#detail PropertyActivation#detail}.
        :param error_location: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#error_location PropertyActivation#error_location}.
        :param instance: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#instance PropertyActivation#instance}.
        :param status_code: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#status_code PropertyActivation#status_code}.
        :param title: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#title PropertyActivation#title}.
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#type PropertyActivation#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6372ca3e72b5868bcc950c96a217390d87724455ee4424bf0e341877fc1b76e)
            check_type(argname="argument behavior_name", value=behavior_name, expected_type=type_hints["behavior_name"])
            check_type(argname="argument detail", value=detail, expected_type=type_hints["detail"])
            check_type(argname="argument error_location", value=error_location, expected_type=type_hints["error_location"])
            check_type(argname="argument instance", value=instance, expected_type=type_hints["instance"])
            check_type(argname="argument status_code", value=status_code, expected_type=type_hints["status_code"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if behavior_name is not None:
            self._values["behavior_name"] = behavior_name
        if detail is not None:
            self._values["detail"] = detail
        if error_location is not None:
            self._values["error_location"] = error_location
        if instance is not None:
            self._values["instance"] = instance
        if status_code is not None:
            self._values["status_code"] = status_code
        if title is not None:
            self._values["title"] = title
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def behavior_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#behavior_name PropertyActivation#behavior_name}.'''
        result = self._values.get("behavior_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def detail(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#detail PropertyActivation#detail}.'''
        result = self._values.get("detail")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def error_location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#error_location PropertyActivation#error_location}.'''
        result = self._values.get("error_location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#instance PropertyActivation#instance}.'''
        result = self._values.get("instance")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status_code(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#status_code PropertyActivation#status_code}.'''
        result = self._values.get("status_code")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#title PropertyActivation#title}.'''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#type PropertyActivation#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PropertyActivationRuleErrors(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PropertyActivationRuleErrorsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.propertyActivation.PropertyActivationRuleErrorsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4daaaa254c9304ec28a07b7bf153022ea37dc6d90548db4e2bb53c81ebbcc041)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "PropertyActivationRuleErrorsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f01caffce37e143f19ac003861badc8d3140c702642f65a303b82a330ec1bfd8)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PropertyActivationRuleErrorsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcaca601958bd149d1b8ef495e80030e93ec263de5d456196409d2e79ad2a53d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__42d384a02e6de70726a2687a3fc97aa194ef1ee88ed73b6c8bb393a16317e397)
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
            type_hints = typing.get_type_hints(_typecheckingstub__50783238ee488860ff232724bb5779791bdb33132cdc8505132ee3b5d6614b86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PropertyActivationRuleErrors]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PropertyActivationRuleErrors]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PropertyActivationRuleErrors]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c424d45baa174f43f8f618a7b272ea213aafab75c7e06f6280e92077b2a2873c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PropertyActivationRuleErrorsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.propertyActivation.PropertyActivationRuleErrorsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__140eb49c44fa0ef3a07285a8300c9609ef9ed2182caae299000645534ef64755)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetBehaviorName")
    def reset_behavior_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBehaviorName", []))

    @jsii.member(jsii_name="resetDetail")
    def reset_detail(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDetail", []))

    @jsii.member(jsii_name="resetErrorLocation")
    def reset_error_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorLocation", []))

    @jsii.member(jsii_name="resetInstance")
    def reset_instance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstance", []))

    @jsii.member(jsii_name="resetStatusCode")
    def reset_status_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatusCode", []))

    @jsii.member(jsii_name="resetTitle")
    def reset_title(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTitle", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="behaviorNameInput")
    def behavior_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "behaviorNameInput"))

    @builtins.property
    @jsii.member(jsii_name="detailInput")
    def detail_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "detailInput"))

    @builtins.property
    @jsii.member(jsii_name="errorLocationInput")
    def error_location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "errorLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceInput")
    def instance_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceInput"))

    @builtins.property
    @jsii.member(jsii_name="statusCodeInput")
    def status_code_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "statusCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="behaviorName")
    def behavior_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "behaviorName"))

    @behavior_name.setter
    def behavior_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__712642edb838474c94a918b3151ead2ec458528c967396066b2853bd42672073)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "behaviorName", value)

    @builtins.property
    @jsii.member(jsii_name="detail")
    def detail(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "detail"))

    @detail.setter
    def detail(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1490d8ed851beb0f513b3ef8b6be975cfae29bd3a2596083fe7cc04781307e7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "detail", value)

    @builtins.property
    @jsii.member(jsii_name="errorLocation")
    def error_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "errorLocation"))

    @error_location.setter
    def error_location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__773966015c77306f6cbcaa4a905446349a9e4611a8ba96e9cce14596bb40d5c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "errorLocation", value)

    @builtins.property
    @jsii.member(jsii_name="instance")
    def instance(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instance"))

    @instance.setter
    def instance(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__feb42c171191ea9bd81dfafda2304e126e0e8de735a07ecc2e410a306f9521e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instance", value)

    @builtins.property
    @jsii.member(jsii_name="statusCode")
    def status_code(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "statusCode"))

    @status_code.setter
    def status_code(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e86147fa104501476abb8de50f1fed0bd1c9401a7ca3c8c476084bee9d9e873)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statusCode", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ada89283a60b9542721730ade0f048fd27921a6d17b89678151b9030a616253)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbf0c2f3b81b830b8045dbf3d23c4b870a3b7e7e43fd4e46aa07fffd51a2872c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PropertyActivationRuleErrors]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PropertyActivationRuleErrors]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PropertyActivationRuleErrors]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a0dcd75225eb18f25b4772bbd28a9684cf1fa1c0b1f7d7b920fed36ebc39a5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.propertyActivation.PropertyActivationTimeouts",
    jsii_struct_bases=[],
    name_mapping={"default": "default"},
)
class PropertyActivationTimeouts:
    def __init__(self, *, default: typing.Optional[builtins.str] = None) -> None:
        '''
        :param default: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#default PropertyActivation#default}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cb1526d499b4acc3e77d630d6f17eed0fc465fc642a70bedffe2e6f3c35efdd)
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if default is not None:
            self._values["default"] = default

    @builtins.property
    def default(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_activation#default PropertyActivation#default}.'''
        result = self._values.get("default")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PropertyActivationTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PropertyActivationTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.propertyActivation.PropertyActivationTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__97bf96909af8f1814d2f7f9b27e4feefe3528cb3f96cbf5a4243e8eaa470ba14)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDefault")
    def reset_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefault", []))

    @builtins.property
    @jsii.member(jsii_name="defaultInput")
    def default_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultInput"))

    @builtins.property
    @jsii.member(jsii_name="default")
    def default(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "default"))

    @default.setter
    def default(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__888c4832b36d9f694ed897767f7a73d659ffceef958933a68772ced21a102bd3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PropertyActivationTimeouts]:
        return typing.cast(typing.Optional[PropertyActivationTimeouts], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PropertyActivationTimeouts],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50ad4c16b9fd29cb3b649c1972969ea67d57b3bdcf21ee46390dbe728722309f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "PropertyActivation",
    "PropertyActivationComplianceRecord",
    "PropertyActivationComplianceRecordNoncomplianceReasonEmergency",
    "PropertyActivationComplianceRecordNoncomplianceReasonEmergencyOutputReference",
    "PropertyActivationComplianceRecordNoncomplianceReasonNoProductionTraffic",
    "PropertyActivationComplianceRecordNoncomplianceReasonNoProductionTrafficOutputReference",
    "PropertyActivationComplianceRecordNoncomplianceReasonNone",
    "PropertyActivationComplianceRecordNoncomplianceReasonNoneOutputReference",
    "PropertyActivationComplianceRecordNoncomplianceReasonOther",
    "PropertyActivationComplianceRecordNoncomplianceReasonOtherOutputReference",
    "PropertyActivationComplianceRecordOutputReference",
    "PropertyActivationConfig",
    "PropertyActivationRuleErrors",
    "PropertyActivationRuleErrorsList",
    "PropertyActivationRuleErrorsOutputReference",
    "PropertyActivationTimeouts",
    "PropertyActivationTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__a4b65d7c112b2f637948dfa5b8d6a3b435ce3708758082b5e8e25e468e9ad945(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    contact: typing.Sequence[builtins.str],
    property_id: builtins.str,
    version: jsii.Number,
    activation_id: typing.Optional[builtins.str] = None,
    auto_acknowledge_rule_warnings: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    compliance_record: typing.Optional[typing.Union[PropertyActivationComplianceRecord, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    network: typing.Optional[builtins.str] = None,
    note: typing.Optional[builtins.str] = None,
    rule_errors: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PropertyActivationRuleErrors, typing.Dict[builtins.str, typing.Any]]]]] = None,
    timeouts: typing.Optional[typing.Union[PropertyActivationTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__251b0bd534a8ebb58fa806864022e2ab82b84785d513e96ce3f292f75bc7c9cf(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60b5f47059067316c54204b52bac07aa445918a77011bb38b6d4b89e4ce37d9e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PropertyActivationRuleErrors, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6afefff1726c3af6e53135dd22015a0290a3d0aad0021257e221be55edab0505(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d97ef7545d8cb9ecc115980925b0b48301ef38a90f025914cee1d76cb48b3a1e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4269d733aec0a5a244a83b0f95180dc0b472bd30627a74b206521ad9271945ef(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48e9684b23e1a437767958d9b10d073648735291fe5dd80b9e23ce07f2246992(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2519ccdf9b9883b30ad67b305842c4a1c7aa05f030ce339af2f04a141cd44e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4ff9612888834fcd6119039b662a7b99589462dcb6b1b5fc74147cbfdcc7d1a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb4d35f4772fad257539624a064b3e8df8ac3128c92bb78ca948e934ba97473c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fa9b7e343b91d44fc961edf901e7557d191f9db8407e67ec7d6cdc10d91e3fe(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c23c0509c3f03a2d8e8f104f3306601432ff2bfc825668944e66c11ae959896(
    *,
    noncompliance_reason_emergency: typing.Optional[typing.Union[PropertyActivationComplianceRecordNoncomplianceReasonEmergency, typing.Dict[builtins.str, typing.Any]]] = None,
    noncompliance_reason_none: typing.Optional[typing.Union[PropertyActivationComplianceRecordNoncomplianceReasonNone, typing.Dict[builtins.str, typing.Any]]] = None,
    noncompliance_reason_no_production_traffic: typing.Optional[typing.Union[PropertyActivationComplianceRecordNoncomplianceReasonNoProductionTraffic, typing.Dict[builtins.str, typing.Any]]] = None,
    noncompliance_reason_other: typing.Optional[typing.Union[PropertyActivationComplianceRecordNoncomplianceReasonOther, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccaead67a7e7528a8238c11ac3e72c110c03be97f35260b912f7fdca5c694296(
    *,
    ticket_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd677a903d5954a4946df74429cda43a5ae54f4bdc4df9acae7d0400584e0e10(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15a0f88b3d1c63a238e7799e676094202f3b42d72f17602ee03b9d843e1883ef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50442d71ef20b94943e4baf1dcd40db138b96653f1aa238a0bbddcfc754ed609(
    value: typing.Optional[PropertyActivationComplianceRecordNoncomplianceReasonEmergency],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b956c4df3519be14e1c6f819769e01d35b9bf1341d9cb437b6c257aebc15035(
    *,
    ticket_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__308f022f797fc2d2281185d15bbf84919d226f9a8296166d3287137521ff8e9f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da1f3f3d2ad81f31ce4a94b4edbb754c318bb8b2c71612f04bc7f4f0eb628bd8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__030bb1bd9b660767ee1a5cdef323ffcd58e78267e402bcb493e13bb2532ec82d(
    value: typing.Optional[PropertyActivationComplianceRecordNoncomplianceReasonNoProductionTraffic],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ab1a982a4278403ee9fd22bbd94360db4bae4531757dd122216a21115b7db9d(
    *,
    customer_email: typing.Optional[builtins.str] = None,
    peer_reviewed_by: typing.Optional[builtins.str] = None,
    ticket_id: typing.Optional[builtins.str] = None,
    unit_tested: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01fd6e94c8d4e0cdb189bef2402581c7abd58afe71e822db13898abc693b7b57(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c4d1ed872fbe8be9c56014473a54ae82f3cb8b52ace23c7da7b68e70904fc25(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__991205fab8c665585d06065ebd2ccb7fc68935e04afd0d2a33f4771f758a5963(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f5ddf503fb5ef02cfc7c75877d2da328e58e131abfe5e4d424e32d8c9bb000d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6090f151649d9ac03463a14567ae5e8484f9d334361e60037b82478708a0bd6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7383db1c03c7544d2536cd564de7220468d537e1588e0d77a4aaedab6366a644(
    value: typing.Optional[PropertyActivationComplianceRecordNoncomplianceReasonNone],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c6b54b29a50d322d93c5353393ad5c01a14751f56f47f23a292512f5507ebe7(
    *,
    other_noncompliance_reason: typing.Optional[builtins.str] = None,
    ticket_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f94017619834faf15580aa0bf6017c9bc27177f052ed92b60ea4a28e0e2b61c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24ebc0b3258bad166ebb4501754aad3f474397c950dabd3b0c26fb114ae05d85(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db8c9c613fe2a31eae9b6c8c1be146a8dfab8a03d2d65764cb44d8ee39a241d4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__230058b406f05efc92813de52bc71ed9d02a6dbfc6e9750282e4d67601efe6b3(
    value: typing.Optional[PropertyActivationComplianceRecordNoncomplianceReasonOther],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fcba7b86fcb5862bc0cd26eea3f5ac7af644925601b89c3b54ed932f7508cf4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4da6e971f13d843058d9ace54916657cfcc5854191520180b2ffdae963e6a0ae(
    value: typing.Optional[PropertyActivationComplianceRecord],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__baa959572e1ffc1c4fac3db6fec3bd7136055063e68b6af543969c35083fdc19(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    contact: typing.Sequence[builtins.str],
    property_id: builtins.str,
    version: jsii.Number,
    activation_id: typing.Optional[builtins.str] = None,
    auto_acknowledge_rule_warnings: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    compliance_record: typing.Optional[typing.Union[PropertyActivationComplianceRecord, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    network: typing.Optional[builtins.str] = None,
    note: typing.Optional[builtins.str] = None,
    rule_errors: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PropertyActivationRuleErrors, typing.Dict[builtins.str, typing.Any]]]]] = None,
    timeouts: typing.Optional[typing.Union[PropertyActivationTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6372ca3e72b5868bcc950c96a217390d87724455ee4424bf0e341877fc1b76e(
    *,
    behavior_name: typing.Optional[builtins.str] = None,
    detail: typing.Optional[builtins.str] = None,
    error_location: typing.Optional[builtins.str] = None,
    instance: typing.Optional[builtins.str] = None,
    status_code: typing.Optional[jsii.Number] = None,
    title: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4daaaa254c9304ec28a07b7bf153022ea37dc6d90548db4e2bb53c81ebbcc041(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f01caffce37e143f19ac003861badc8d3140c702642f65a303b82a330ec1bfd8(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcaca601958bd149d1b8ef495e80030e93ec263de5d456196409d2e79ad2a53d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42d384a02e6de70726a2687a3fc97aa194ef1ee88ed73b6c8bb393a16317e397(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50783238ee488860ff232724bb5779791bdb33132cdc8505132ee3b5d6614b86(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c424d45baa174f43f8f618a7b272ea213aafab75c7e06f6280e92077b2a2873c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PropertyActivationRuleErrors]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__140eb49c44fa0ef3a07285a8300c9609ef9ed2182caae299000645534ef64755(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__712642edb838474c94a918b3151ead2ec458528c967396066b2853bd42672073(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1490d8ed851beb0f513b3ef8b6be975cfae29bd3a2596083fe7cc04781307e7b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__773966015c77306f6cbcaa4a905446349a9e4611a8ba96e9cce14596bb40d5c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__feb42c171191ea9bd81dfafda2304e126e0e8de735a07ecc2e410a306f9521e1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e86147fa104501476abb8de50f1fed0bd1c9401a7ca3c8c476084bee9d9e873(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ada89283a60b9542721730ade0f048fd27921a6d17b89678151b9030a616253(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbf0c2f3b81b830b8045dbf3d23c4b870a3b7e7e43fd4e46aa07fffd51a2872c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a0dcd75225eb18f25b4772bbd28a9684cf1fa1c0b1f7d7b920fed36ebc39a5a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PropertyActivationRuleErrors]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cb1526d499b4acc3e77d630d6f17eed0fc465fc642a70bedffe2e6f3c35efdd(
    *,
    default: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97bf96909af8f1814d2f7f9b27e4feefe3528cb3f96cbf5a4243e8eaa470ba14(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__888c4832b36d9f694ed897767f7a73d659ffceef958933a68772ced21a102bd3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50ad4c16b9fd29cb3b649c1972969ea67d57b3bdcf21ee46390dbe728722309f(
    value: typing.Optional[PropertyActivationTimeouts],
) -> None:
    """Type checking stubs"""
    pass
