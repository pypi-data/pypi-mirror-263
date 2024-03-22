'''
# `akamai_property_include_activation`

Refer to the Terraform Registry for docs: [`akamai_property_include_activation`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation).
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


class PropertyIncludeActivation(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.propertyIncludeActivation.PropertyIncludeActivation",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation akamai_property_include_activation}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        contract_id: builtins.str,
        group_id: builtins.str,
        include_id: builtins.str,
        network: builtins.str,
        notify_emails: typing.Sequence[builtins.str],
        version: jsii.Number,
        auto_acknowledge_rule_warnings: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        compliance_record: typing.Optional[typing.Union["PropertyIncludeActivationComplianceRecord", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        note: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["PropertyIncludeActivationTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation akamai_property_include_activation} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param contract_id: The contract under which the include is activated. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#contract_id PropertyIncludeActivation#contract_id}
        :param group_id: The group under which the include is activated. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#group_id PropertyIncludeActivation#group_id}
        :param include_id: The unique identifier of the include. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#include_id PropertyIncludeActivation#include_id}
        :param network: The network for which the activation will be performed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#network PropertyIncludeActivation#network}
        :param notify_emails: The list of email addresses to notify about an activation status. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#notify_emails PropertyIncludeActivation#notify_emails}
        :param version: The unique identifier of the include. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#version PropertyIncludeActivation#version}
        :param auto_acknowledge_rule_warnings: Automatically acknowledge all rule warnings for activation and continue. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#auto_acknowledge_rule_warnings PropertyIncludeActivation#auto_acknowledge_rule_warnings}
        :param compliance_record: compliance_record block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#compliance_record PropertyIncludeActivation#compliance_record}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#id PropertyIncludeActivation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param note: The note to assign to a log message of the activation request. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#note PropertyIncludeActivation#note}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#timeouts PropertyIncludeActivation#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b369e9cad307216989a2601b3ebe57f3ce94b8810ffe17dc2229727f942563c3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = PropertyIncludeActivationConfig(
            contract_id=contract_id,
            group_id=group_id,
            include_id=include_id,
            network=network,
            notify_emails=notify_emails,
            version=version,
            auto_acknowledge_rule_warnings=auto_acknowledge_rule_warnings,
            compliance_record=compliance_record,
            id=id,
            note=note,
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
        '''Generates CDKTF code for importing a PropertyIncludeActivation resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the PropertyIncludeActivation to import.
        :param import_from_id: The id of the existing PropertyIncludeActivation that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the PropertyIncludeActivation to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a3575d8bdd88b5e698d5bb47ad0f143bbb2eb621387a1b99ed3b1251b657c39)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putComplianceRecord")
    def put_compliance_record(
        self,
        *,
        noncompliance_reason_emergency: typing.Optional[typing.Union["PropertyIncludeActivationComplianceRecordNoncomplianceReasonEmergency", typing.Dict[builtins.str, typing.Any]]] = None,
        noncompliance_reason_none: typing.Optional[typing.Union["PropertyIncludeActivationComplianceRecordNoncomplianceReasonNone", typing.Dict[builtins.str, typing.Any]]] = None,
        noncompliance_reason_no_production_traffic: typing.Optional[typing.Union["PropertyIncludeActivationComplianceRecordNoncomplianceReasonNoProductionTraffic", typing.Dict[builtins.str, typing.Any]]] = None,
        noncompliance_reason_other: typing.Optional[typing.Union["PropertyIncludeActivationComplianceRecordNoncomplianceReasonOther", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param noncompliance_reason_emergency: noncompliance_reason_emergency block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#noncompliance_reason_emergency PropertyIncludeActivation#noncompliance_reason_emergency}
        :param noncompliance_reason_none: noncompliance_reason_none block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#noncompliance_reason_none PropertyIncludeActivation#noncompliance_reason_none}
        :param noncompliance_reason_no_production_traffic: noncompliance_reason_no_production_traffic block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#noncompliance_reason_no_production_traffic PropertyIncludeActivation#noncompliance_reason_no_production_traffic}
        :param noncompliance_reason_other: noncompliance_reason_other block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#noncompliance_reason_other PropertyIncludeActivation#noncompliance_reason_other}
        '''
        value = PropertyIncludeActivationComplianceRecord(
            noncompliance_reason_emergency=noncompliance_reason_emergency,
            noncompliance_reason_none=noncompliance_reason_none,
            noncompliance_reason_no_production_traffic=noncompliance_reason_no_production_traffic,
            noncompliance_reason_other=noncompliance_reason_other,
        )

        return typing.cast(None, jsii.invoke(self, "putComplianceRecord", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self, *, default: typing.Optional[builtins.str] = None) -> None:
        '''
        :param default: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#default PropertyIncludeActivation#default}.
        '''
        value = PropertyIncludeActivationTimeouts(default=default)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAutoAcknowledgeRuleWarnings")
    def reset_auto_acknowledge_rule_warnings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoAcknowledgeRuleWarnings", []))

    @jsii.member(jsii_name="resetComplianceRecord")
    def reset_compliance_record(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComplianceRecord", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNote")
    def reset_note(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNote", []))

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
    def compliance_record(
        self,
    ) -> "PropertyIncludeActivationComplianceRecordOutputReference":
        return typing.cast("PropertyIncludeActivationComplianceRecordOutputReference", jsii.get(self, "complianceRecord"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "PropertyIncludeActivationTimeoutsOutputReference":
        return typing.cast("PropertyIncludeActivationTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="validations")
    def validations(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "validations"))

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
    ) -> typing.Optional["PropertyIncludeActivationComplianceRecord"]:
        return typing.cast(typing.Optional["PropertyIncludeActivationComplianceRecord"], jsii.get(self, "complianceRecordInput"))

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
    @jsii.member(jsii_name="includeIdInput")
    def include_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "includeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInput")
    def network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkInput"))

    @builtins.property
    @jsii.member(jsii_name="noteInput")
    def note_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "noteInput"))

    @builtins.property
    @jsii.member(jsii_name="notifyEmailsInput")
    def notify_emails_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "notifyEmailsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(self) -> typing.Optional["PropertyIncludeActivationTimeouts"]:
        return typing.cast(typing.Optional["PropertyIncludeActivationTimeouts"], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "versionInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__6465edba9b0dbb514539e48f9c749ea8cd9ba91113f34c5fdec252272b5437db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoAcknowledgeRuleWarnings", value)

    @builtins.property
    @jsii.member(jsii_name="contractId")
    def contract_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contractId"))

    @contract_id.setter
    def contract_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__363854128813ebbd6e7592fa0d39672e3b71aff8c1feef49cf51b0b64efa6091)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contractId", value)

    @builtins.property
    @jsii.member(jsii_name="groupId")
    def group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupId"))

    @group_id.setter
    def group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99ae78abee3d6caee53f7748f7e530e817acec7b161c6b9b079f5f24ac8dc071)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__818003c173aa9fca615b90fda8224f3449afa01d25419d844e0535852cb8d746)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="includeId")
    def include_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "includeId"))

    @include_id.setter
    def include_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac446c014fcafaf349de79807ae7100f708701949f9dd30b46e04a0e248d8d54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeId", value)

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "network"))

    @network.setter
    def network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3a8134d5b592464f1d7789b17923d667ca97bd38c05523ce8e022326ea99906)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "network", value)

    @builtins.property
    @jsii.member(jsii_name="note")
    def note(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "note"))

    @note.setter
    def note(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2deb61cb5e7ff94374e1735c5be02968d22ac8599bc5c81051a0a52ecb579697)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "note", value)

    @builtins.property
    @jsii.member(jsii_name="notifyEmails")
    def notify_emails(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "notifyEmails"))

    @notify_emails.setter
    def notify_emails(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbba224b9284aa89e03f464a8a9bacf4789d8a7e713a43099d2c5e62d2a7d0be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notifyEmails", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "version"))

    @version.setter
    def version(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2f2e7556c9c035a9635d76278cb31362bc88d75ed5cecb2c7ada670f20cdead)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)


@jsii.data_type(
    jsii_type="akamai.propertyIncludeActivation.PropertyIncludeActivationComplianceRecord",
    jsii_struct_bases=[],
    name_mapping={
        "noncompliance_reason_emergency": "noncomplianceReasonEmergency",
        "noncompliance_reason_none": "noncomplianceReasonNone",
        "noncompliance_reason_no_production_traffic": "noncomplianceReasonNoProductionTraffic",
        "noncompliance_reason_other": "noncomplianceReasonOther",
    },
)
class PropertyIncludeActivationComplianceRecord:
    def __init__(
        self,
        *,
        noncompliance_reason_emergency: typing.Optional[typing.Union["PropertyIncludeActivationComplianceRecordNoncomplianceReasonEmergency", typing.Dict[builtins.str, typing.Any]]] = None,
        noncompliance_reason_none: typing.Optional[typing.Union["PropertyIncludeActivationComplianceRecordNoncomplianceReasonNone", typing.Dict[builtins.str, typing.Any]]] = None,
        noncompliance_reason_no_production_traffic: typing.Optional[typing.Union["PropertyIncludeActivationComplianceRecordNoncomplianceReasonNoProductionTraffic", typing.Dict[builtins.str, typing.Any]]] = None,
        noncompliance_reason_other: typing.Optional[typing.Union["PropertyIncludeActivationComplianceRecordNoncomplianceReasonOther", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param noncompliance_reason_emergency: noncompliance_reason_emergency block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#noncompliance_reason_emergency PropertyIncludeActivation#noncompliance_reason_emergency}
        :param noncompliance_reason_none: noncompliance_reason_none block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#noncompliance_reason_none PropertyIncludeActivation#noncompliance_reason_none}
        :param noncompliance_reason_no_production_traffic: noncompliance_reason_no_production_traffic block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#noncompliance_reason_no_production_traffic PropertyIncludeActivation#noncompliance_reason_no_production_traffic}
        :param noncompliance_reason_other: noncompliance_reason_other block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#noncompliance_reason_other PropertyIncludeActivation#noncompliance_reason_other}
        '''
        if isinstance(noncompliance_reason_emergency, dict):
            noncompliance_reason_emergency = PropertyIncludeActivationComplianceRecordNoncomplianceReasonEmergency(**noncompliance_reason_emergency)
        if isinstance(noncompliance_reason_none, dict):
            noncompliance_reason_none = PropertyIncludeActivationComplianceRecordNoncomplianceReasonNone(**noncompliance_reason_none)
        if isinstance(noncompliance_reason_no_production_traffic, dict):
            noncompliance_reason_no_production_traffic = PropertyIncludeActivationComplianceRecordNoncomplianceReasonNoProductionTraffic(**noncompliance_reason_no_production_traffic)
        if isinstance(noncompliance_reason_other, dict):
            noncompliance_reason_other = PropertyIncludeActivationComplianceRecordNoncomplianceReasonOther(**noncompliance_reason_other)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92a8012a3c00c4350095bc4ad4674886bc6841b3f5dd8f15a182507fbfb97d34)
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
    ) -> typing.Optional["PropertyIncludeActivationComplianceRecordNoncomplianceReasonEmergency"]:
        '''noncompliance_reason_emergency block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#noncompliance_reason_emergency PropertyIncludeActivation#noncompliance_reason_emergency}
        '''
        result = self._values.get("noncompliance_reason_emergency")
        return typing.cast(typing.Optional["PropertyIncludeActivationComplianceRecordNoncomplianceReasonEmergency"], result)

    @builtins.property
    def noncompliance_reason_none(
        self,
    ) -> typing.Optional["PropertyIncludeActivationComplianceRecordNoncomplianceReasonNone"]:
        '''noncompliance_reason_none block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#noncompliance_reason_none PropertyIncludeActivation#noncompliance_reason_none}
        '''
        result = self._values.get("noncompliance_reason_none")
        return typing.cast(typing.Optional["PropertyIncludeActivationComplianceRecordNoncomplianceReasonNone"], result)

    @builtins.property
    def noncompliance_reason_no_production_traffic(
        self,
    ) -> typing.Optional["PropertyIncludeActivationComplianceRecordNoncomplianceReasonNoProductionTraffic"]:
        '''noncompliance_reason_no_production_traffic block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#noncompliance_reason_no_production_traffic PropertyIncludeActivation#noncompliance_reason_no_production_traffic}
        '''
        result = self._values.get("noncompliance_reason_no_production_traffic")
        return typing.cast(typing.Optional["PropertyIncludeActivationComplianceRecordNoncomplianceReasonNoProductionTraffic"], result)

    @builtins.property
    def noncompliance_reason_other(
        self,
    ) -> typing.Optional["PropertyIncludeActivationComplianceRecordNoncomplianceReasonOther"]:
        '''noncompliance_reason_other block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#noncompliance_reason_other PropertyIncludeActivation#noncompliance_reason_other}
        '''
        result = self._values.get("noncompliance_reason_other")
        return typing.cast(typing.Optional["PropertyIncludeActivationComplianceRecordNoncomplianceReasonOther"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PropertyIncludeActivationComplianceRecord(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.propertyIncludeActivation.PropertyIncludeActivationComplianceRecordNoncomplianceReasonEmergency",
    jsii_struct_bases=[],
    name_mapping={"ticket_id": "ticketId"},
)
class PropertyIncludeActivationComplianceRecordNoncomplianceReasonEmergency:
    def __init__(self, *, ticket_id: typing.Optional[builtins.str] = None) -> None:
        '''
        :param ticket_id: Identifies the ticket that describes the need for the activation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#ticket_id PropertyIncludeActivation#ticket_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc5ca3d9282594654dd655e3bd3de57760bde0c45f7b707283942490e6070875)
            check_type(argname="argument ticket_id", value=ticket_id, expected_type=type_hints["ticket_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ticket_id is not None:
            self._values["ticket_id"] = ticket_id

    @builtins.property
    def ticket_id(self) -> typing.Optional[builtins.str]:
        '''Identifies the ticket that describes the need for the activation.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#ticket_id PropertyIncludeActivation#ticket_id}
        '''
        result = self._values.get("ticket_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PropertyIncludeActivationComplianceRecordNoncomplianceReasonEmergency(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PropertyIncludeActivationComplianceRecordNoncomplianceReasonEmergencyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.propertyIncludeActivation.PropertyIncludeActivationComplianceRecordNoncomplianceReasonEmergencyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4c465093aad3bf35e75d9ea884dca15bc9e5b16274fb60f8b681e02adb5d4249)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2e7c9301e35c89d5dada15a9465477ec25ed2e7f074a04bf305695c59ba6af73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ticketId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PropertyIncludeActivationComplianceRecordNoncomplianceReasonEmergency]:
        return typing.cast(typing.Optional[PropertyIncludeActivationComplianceRecordNoncomplianceReasonEmergency], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PropertyIncludeActivationComplianceRecordNoncomplianceReasonEmergency],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__692431355ff8db08ba7555be848da2a25f005ef5a0189ce323b995245d37daa1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.propertyIncludeActivation.PropertyIncludeActivationComplianceRecordNoncomplianceReasonNoProductionTraffic",
    jsii_struct_bases=[],
    name_mapping={"ticket_id": "ticketId"},
)
class PropertyIncludeActivationComplianceRecordNoncomplianceReasonNoProductionTraffic:
    def __init__(self, *, ticket_id: typing.Optional[builtins.str] = None) -> None:
        '''
        :param ticket_id: Identifies the ticket that describes the need for the activation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#ticket_id PropertyIncludeActivation#ticket_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7feb886481bd9390ad2fbeafdca9ecd61ed905a366fa1af81ddb11d0bbebbe7e)
            check_type(argname="argument ticket_id", value=ticket_id, expected_type=type_hints["ticket_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ticket_id is not None:
            self._values["ticket_id"] = ticket_id

    @builtins.property
    def ticket_id(self) -> typing.Optional[builtins.str]:
        '''Identifies the ticket that describes the need for the activation.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#ticket_id PropertyIncludeActivation#ticket_id}
        '''
        result = self._values.get("ticket_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PropertyIncludeActivationComplianceRecordNoncomplianceReasonNoProductionTraffic(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PropertyIncludeActivationComplianceRecordNoncomplianceReasonNoProductionTrafficOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.propertyIncludeActivation.PropertyIncludeActivationComplianceRecordNoncomplianceReasonNoProductionTrafficOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__89ca58c63f4ba675d2f43a633e68c8318da873df7ea4c2826c28e17903b6f998)
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
            type_hints = typing.get_type_hints(_typecheckingstub__442bb06cc0359e5ca0dd06cf9b46c08cb8075144de2531c36008b1db25fc20b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ticketId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PropertyIncludeActivationComplianceRecordNoncomplianceReasonNoProductionTraffic]:
        return typing.cast(typing.Optional[PropertyIncludeActivationComplianceRecordNoncomplianceReasonNoProductionTraffic], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PropertyIncludeActivationComplianceRecordNoncomplianceReasonNoProductionTraffic],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2dd93c51e570f929007a160483bd50654f6dcbfa008341836b8ede00bdd1814b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.propertyIncludeActivation.PropertyIncludeActivationComplianceRecordNoncomplianceReasonNone",
    jsii_struct_bases=[],
    name_mapping={
        "customer_email": "customerEmail",
        "peer_reviewed_by": "peerReviewedBy",
        "ticket_id": "ticketId",
        "unit_tested": "unitTested",
    },
)
class PropertyIncludeActivationComplianceRecordNoncomplianceReasonNone:
    def __init__(
        self,
        *,
        customer_email: typing.Optional[builtins.str] = None,
        peer_reviewed_by: typing.Optional[builtins.str] = None,
        ticket_id: typing.Optional[builtins.str] = None,
        unit_tested: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param customer_email: Identifies the customer. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#customer_email PropertyIncludeActivation#customer_email}
        :param peer_reviewed_by: Identifies person who has independently approved the activation request. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#peer_reviewed_by PropertyIncludeActivation#peer_reviewed_by}
        :param ticket_id: Identifies the ticket that describes the need for the activation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#ticket_id PropertyIncludeActivation#ticket_id}
        :param unit_tested: Whether the metadata to activate has been fully tested. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#unit_tested PropertyIncludeActivation#unit_tested}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f4d8b341a72f2b7570234ac2c333f29ec795f4e3d66607f423d7d2ae10aec6e)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#customer_email PropertyIncludeActivation#customer_email}
        '''
        result = self._values.get("customer_email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def peer_reviewed_by(self) -> typing.Optional[builtins.str]:
        '''Identifies person who has independently approved the activation request.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#peer_reviewed_by PropertyIncludeActivation#peer_reviewed_by}
        '''
        result = self._values.get("peer_reviewed_by")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ticket_id(self) -> typing.Optional[builtins.str]:
        '''Identifies the ticket that describes the need for the activation.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#ticket_id PropertyIncludeActivation#ticket_id}
        '''
        result = self._values.get("ticket_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def unit_tested(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether the metadata to activate has been fully tested.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#unit_tested PropertyIncludeActivation#unit_tested}
        '''
        result = self._values.get("unit_tested")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PropertyIncludeActivationComplianceRecordNoncomplianceReasonNone(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PropertyIncludeActivationComplianceRecordNoncomplianceReasonNoneOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.propertyIncludeActivation.PropertyIncludeActivationComplianceRecordNoncomplianceReasonNoneOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e1fbf8db33cf91b89f541cf2950d8007f3f2679001ad49477c5d38eef4fb3940)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5ed06e8c4c43b339c63cbd6d3e971bdb9fdfe6060c8b5db8f08c741edb3815a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customerEmail", value)

    @builtins.property
    @jsii.member(jsii_name="peerReviewedBy")
    def peer_reviewed_by(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "peerReviewedBy"))

    @peer_reviewed_by.setter
    def peer_reviewed_by(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e2bd620068b7fc4d74244fb374c66ee08e710dbba03feb033c59dfebc040740)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "peerReviewedBy", value)

    @builtins.property
    @jsii.member(jsii_name="ticketId")
    def ticket_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ticketId"))

    @ticket_id.setter
    def ticket_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc85176d6ab41897f15fc734d25a0573d3ab30b0e44a1023e7201d4e23273ab5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5b9f2ffbbb117a105ce2212589d9a97d1cc80e7d1d1ff3e3a3d7d3681f1ab1fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unitTested", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PropertyIncludeActivationComplianceRecordNoncomplianceReasonNone]:
        return typing.cast(typing.Optional[PropertyIncludeActivationComplianceRecordNoncomplianceReasonNone], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PropertyIncludeActivationComplianceRecordNoncomplianceReasonNone],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3532109b1317557630c9229c8a03d3ef08038fded2d1460218bcfe762cdd709)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.propertyIncludeActivation.PropertyIncludeActivationComplianceRecordNoncomplianceReasonOther",
    jsii_struct_bases=[],
    name_mapping={
        "other_noncompliance_reason": "otherNoncomplianceReason",
        "ticket_id": "ticketId",
    },
)
class PropertyIncludeActivationComplianceRecordNoncomplianceReasonOther:
    def __init__(
        self,
        *,
        other_noncompliance_reason: typing.Optional[builtins.str] = None,
        ticket_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param other_noncompliance_reason: Describes the reason why the activation must occur immediately, out of compliance with the standard procedure. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#other_noncompliance_reason PropertyIncludeActivation#other_noncompliance_reason}
        :param ticket_id: Identifies the ticket that describes the need for the activation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#ticket_id PropertyIncludeActivation#ticket_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6571989beca2ff63808125f6b7a09d19491d17e8f989eb881510377dc2da0df)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#other_noncompliance_reason PropertyIncludeActivation#other_noncompliance_reason}
        '''
        result = self._values.get("other_noncompliance_reason")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ticket_id(self) -> typing.Optional[builtins.str]:
        '''Identifies the ticket that describes the need for the activation.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#ticket_id PropertyIncludeActivation#ticket_id}
        '''
        result = self._values.get("ticket_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PropertyIncludeActivationComplianceRecordNoncomplianceReasonOther(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PropertyIncludeActivationComplianceRecordNoncomplianceReasonOtherOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.propertyIncludeActivation.PropertyIncludeActivationComplianceRecordNoncomplianceReasonOtherOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cc86aa1394a0580f4a348a9049708daa8866efcf907f58cae93b3b6edc9ed3c9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1e25cd70213bf92c6dad0672ef4481cefbffea7b11e8d854887266f2de5692a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "otherNoncomplianceReason", value)

    @builtins.property
    @jsii.member(jsii_name="ticketId")
    def ticket_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ticketId"))

    @ticket_id.setter
    def ticket_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0e365c804c97925d4593994d94476bd610e65f3bb949d79121c1863b5063569)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ticketId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PropertyIncludeActivationComplianceRecordNoncomplianceReasonOther]:
        return typing.cast(typing.Optional[PropertyIncludeActivationComplianceRecordNoncomplianceReasonOther], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PropertyIncludeActivationComplianceRecordNoncomplianceReasonOther],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__895225627bb708e5054ec04b6122d765e239dcb5b78e6e42c99557e9cd5f5f23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PropertyIncludeActivationComplianceRecordOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.propertyIncludeActivation.PropertyIncludeActivationComplianceRecordOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4d5809e383738ed93ebea3ea858da52851059ad60a9a93adb095309bd2e0ce5e)
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
        :param ticket_id: Identifies the ticket that describes the need for the activation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#ticket_id PropertyIncludeActivation#ticket_id}
        '''
        value = PropertyIncludeActivationComplianceRecordNoncomplianceReasonEmergency(
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
        :param customer_email: Identifies the customer. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#customer_email PropertyIncludeActivation#customer_email}
        :param peer_reviewed_by: Identifies person who has independently approved the activation request. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#peer_reviewed_by PropertyIncludeActivation#peer_reviewed_by}
        :param ticket_id: Identifies the ticket that describes the need for the activation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#ticket_id PropertyIncludeActivation#ticket_id}
        :param unit_tested: Whether the metadata to activate has been fully tested. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#unit_tested PropertyIncludeActivation#unit_tested}
        '''
        value = PropertyIncludeActivationComplianceRecordNoncomplianceReasonNone(
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
        :param ticket_id: Identifies the ticket that describes the need for the activation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#ticket_id PropertyIncludeActivation#ticket_id}
        '''
        value = PropertyIncludeActivationComplianceRecordNoncomplianceReasonNoProductionTraffic(
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
        :param other_noncompliance_reason: Describes the reason why the activation must occur immediately, out of compliance with the standard procedure. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#other_noncompliance_reason PropertyIncludeActivation#other_noncompliance_reason}
        :param ticket_id: Identifies the ticket that describes the need for the activation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#ticket_id PropertyIncludeActivation#ticket_id}
        '''
        value = PropertyIncludeActivationComplianceRecordNoncomplianceReasonOther(
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
    ) -> PropertyIncludeActivationComplianceRecordNoncomplianceReasonEmergencyOutputReference:
        return typing.cast(PropertyIncludeActivationComplianceRecordNoncomplianceReasonEmergencyOutputReference, jsii.get(self, "noncomplianceReasonEmergency"))

    @builtins.property
    @jsii.member(jsii_name="noncomplianceReasonNone")
    def noncompliance_reason_none(
        self,
    ) -> PropertyIncludeActivationComplianceRecordNoncomplianceReasonNoneOutputReference:
        return typing.cast(PropertyIncludeActivationComplianceRecordNoncomplianceReasonNoneOutputReference, jsii.get(self, "noncomplianceReasonNone"))

    @builtins.property
    @jsii.member(jsii_name="noncomplianceReasonNoProductionTraffic")
    def noncompliance_reason_no_production_traffic(
        self,
    ) -> PropertyIncludeActivationComplianceRecordNoncomplianceReasonNoProductionTrafficOutputReference:
        return typing.cast(PropertyIncludeActivationComplianceRecordNoncomplianceReasonNoProductionTrafficOutputReference, jsii.get(self, "noncomplianceReasonNoProductionTraffic"))

    @builtins.property
    @jsii.member(jsii_name="noncomplianceReasonOther")
    def noncompliance_reason_other(
        self,
    ) -> PropertyIncludeActivationComplianceRecordNoncomplianceReasonOtherOutputReference:
        return typing.cast(PropertyIncludeActivationComplianceRecordNoncomplianceReasonOtherOutputReference, jsii.get(self, "noncomplianceReasonOther"))

    @builtins.property
    @jsii.member(jsii_name="noncomplianceReasonEmergencyInput")
    def noncompliance_reason_emergency_input(
        self,
    ) -> typing.Optional[PropertyIncludeActivationComplianceRecordNoncomplianceReasonEmergency]:
        return typing.cast(typing.Optional[PropertyIncludeActivationComplianceRecordNoncomplianceReasonEmergency], jsii.get(self, "noncomplianceReasonEmergencyInput"))

    @builtins.property
    @jsii.member(jsii_name="noncomplianceReasonNoneInput")
    def noncompliance_reason_none_input(
        self,
    ) -> typing.Optional[PropertyIncludeActivationComplianceRecordNoncomplianceReasonNone]:
        return typing.cast(typing.Optional[PropertyIncludeActivationComplianceRecordNoncomplianceReasonNone], jsii.get(self, "noncomplianceReasonNoneInput"))

    @builtins.property
    @jsii.member(jsii_name="noncomplianceReasonNoProductionTrafficInput")
    def noncompliance_reason_no_production_traffic_input(
        self,
    ) -> typing.Optional[PropertyIncludeActivationComplianceRecordNoncomplianceReasonNoProductionTraffic]:
        return typing.cast(typing.Optional[PropertyIncludeActivationComplianceRecordNoncomplianceReasonNoProductionTraffic], jsii.get(self, "noncomplianceReasonNoProductionTrafficInput"))

    @builtins.property
    @jsii.member(jsii_name="noncomplianceReasonOtherInput")
    def noncompliance_reason_other_input(
        self,
    ) -> typing.Optional[PropertyIncludeActivationComplianceRecordNoncomplianceReasonOther]:
        return typing.cast(typing.Optional[PropertyIncludeActivationComplianceRecordNoncomplianceReasonOther], jsii.get(self, "noncomplianceReasonOtherInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PropertyIncludeActivationComplianceRecord]:
        return typing.cast(typing.Optional[PropertyIncludeActivationComplianceRecord], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PropertyIncludeActivationComplianceRecord],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__792de28e7454649e7e9bb51a0c31b08d6c5fb0d6a121b73b0df211b95ac6fe0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.propertyIncludeActivation.PropertyIncludeActivationConfig",
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
        "include_id": "includeId",
        "network": "network",
        "notify_emails": "notifyEmails",
        "version": "version",
        "auto_acknowledge_rule_warnings": "autoAcknowledgeRuleWarnings",
        "compliance_record": "complianceRecord",
        "id": "id",
        "note": "note",
        "timeouts": "timeouts",
    },
)
class PropertyIncludeActivationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        include_id: builtins.str,
        network: builtins.str,
        notify_emails: typing.Sequence[builtins.str],
        version: jsii.Number,
        auto_acknowledge_rule_warnings: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        compliance_record: typing.Optional[typing.Union[PropertyIncludeActivationComplianceRecord, typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        note: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["PropertyIncludeActivationTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param contract_id: The contract under which the include is activated. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#contract_id PropertyIncludeActivation#contract_id}
        :param group_id: The group under which the include is activated. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#group_id PropertyIncludeActivation#group_id}
        :param include_id: The unique identifier of the include. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#include_id PropertyIncludeActivation#include_id}
        :param network: The network for which the activation will be performed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#network PropertyIncludeActivation#network}
        :param notify_emails: The list of email addresses to notify about an activation status. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#notify_emails PropertyIncludeActivation#notify_emails}
        :param version: The unique identifier of the include. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#version PropertyIncludeActivation#version}
        :param auto_acknowledge_rule_warnings: Automatically acknowledge all rule warnings for activation and continue. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#auto_acknowledge_rule_warnings PropertyIncludeActivation#auto_acknowledge_rule_warnings}
        :param compliance_record: compliance_record block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#compliance_record PropertyIncludeActivation#compliance_record}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#id PropertyIncludeActivation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param note: The note to assign to a log message of the activation request. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#note PropertyIncludeActivation#note}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#timeouts PropertyIncludeActivation#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(compliance_record, dict):
            compliance_record = PropertyIncludeActivationComplianceRecord(**compliance_record)
        if isinstance(timeouts, dict):
            timeouts = PropertyIncludeActivationTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc375cd5939d582c8a0d20e9c80c3d34829b87da35123d993917f92599ccb11f)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument contract_id", value=contract_id, expected_type=type_hints["contract_id"])
            check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
            check_type(argname="argument include_id", value=include_id, expected_type=type_hints["include_id"])
            check_type(argname="argument network", value=network, expected_type=type_hints["network"])
            check_type(argname="argument notify_emails", value=notify_emails, expected_type=type_hints["notify_emails"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument auto_acknowledge_rule_warnings", value=auto_acknowledge_rule_warnings, expected_type=type_hints["auto_acknowledge_rule_warnings"])
            check_type(argname="argument compliance_record", value=compliance_record, expected_type=type_hints["compliance_record"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument note", value=note, expected_type=type_hints["note"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "contract_id": contract_id,
            "group_id": group_id,
            "include_id": include_id,
            "network": network,
            "notify_emails": notify_emails,
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
        if auto_acknowledge_rule_warnings is not None:
            self._values["auto_acknowledge_rule_warnings"] = auto_acknowledge_rule_warnings
        if compliance_record is not None:
            self._values["compliance_record"] = compliance_record
        if id is not None:
            self._values["id"] = id
        if note is not None:
            self._values["note"] = note
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
    def contract_id(self) -> builtins.str:
        '''The contract under which the include is activated.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#contract_id PropertyIncludeActivation#contract_id}
        '''
        result = self._values.get("contract_id")
        assert result is not None, "Required property 'contract_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_id(self) -> builtins.str:
        '''The group under which the include is activated.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#group_id PropertyIncludeActivation#group_id}
        '''
        result = self._values.get("group_id")
        assert result is not None, "Required property 'group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def include_id(self) -> builtins.str:
        '''The unique identifier of the include.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#include_id PropertyIncludeActivation#include_id}
        '''
        result = self._values.get("include_id")
        assert result is not None, "Required property 'include_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network(self) -> builtins.str:
        '''The network for which the activation will be performed.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#network PropertyIncludeActivation#network}
        '''
        result = self._values.get("network")
        assert result is not None, "Required property 'network' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def notify_emails(self) -> typing.List[builtins.str]:
        '''The list of email addresses to notify about an activation status.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#notify_emails PropertyIncludeActivation#notify_emails}
        '''
        result = self._values.get("notify_emails")
        assert result is not None, "Required property 'notify_emails' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def version(self) -> jsii.Number:
        '''The unique identifier of the include.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#version PropertyIncludeActivation#version}
        '''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def auto_acknowledge_rule_warnings(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Automatically acknowledge all rule warnings for activation and continue.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#auto_acknowledge_rule_warnings PropertyIncludeActivation#auto_acknowledge_rule_warnings}
        '''
        result = self._values.get("auto_acknowledge_rule_warnings")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def compliance_record(
        self,
    ) -> typing.Optional[PropertyIncludeActivationComplianceRecord]:
        '''compliance_record block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#compliance_record PropertyIncludeActivation#compliance_record}
        '''
        result = self._values.get("compliance_record")
        return typing.cast(typing.Optional[PropertyIncludeActivationComplianceRecord], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#id PropertyIncludeActivation#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def note(self) -> typing.Optional[builtins.str]:
        '''The note to assign to a log message of the activation request.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#note PropertyIncludeActivation#note}
        '''
        result = self._values.get("note")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["PropertyIncludeActivationTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#timeouts PropertyIncludeActivation#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["PropertyIncludeActivationTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PropertyIncludeActivationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.propertyIncludeActivation.PropertyIncludeActivationTimeouts",
    jsii_struct_bases=[],
    name_mapping={"default": "default"},
)
class PropertyIncludeActivationTimeouts:
    def __init__(self, *, default: typing.Optional[builtins.str] = None) -> None:
        '''
        :param default: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#default PropertyIncludeActivation#default}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc6183f30757dd269b292348eb438116783069e3613d63b0d72912c302b273d2)
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if default is not None:
            self._values["default"] = default

    @builtins.property
    def default(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/property_include_activation#default PropertyIncludeActivation#default}.'''
        result = self._values.get("default")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PropertyIncludeActivationTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PropertyIncludeActivationTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.propertyIncludeActivation.PropertyIncludeActivationTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2bd3922668f64aae19dba49e8111369675745cafd25ac80d17824ce9188806a5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__02f48064e2cb6c90d8ea07e4893fd64c1006181023e4950a9b2baca8c57ba6be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PropertyIncludeActivationTimeouts]:
        return typing.cast(typing.Optional[PropertyIncludeActivationTimeouts], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PropertyIncludeActivationTimeouts],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13699ec7beb10e154de5d98914dbda1b7a2793e20f60953735479999b7945f3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "PropertyIncludeActivation",
    "PropertyIncludeActivationComplianceRecord",
    "PropertyIncludeActivationComplianceRecordNoncomplianceReasonEmergency",
    "PropertyIncludeActivationComplianceRecordNoncomplianceReasonEmergencyOutputReference",
    "PropertyIncludeActivationComplianceRecordNoncomplianceReasonNoProductionTraffic",
    "PropertyIncludeActivationComplianceRecordNoncomplianceReasonNoProductionTrafficOutputReference",
    "PropertyIncludeActivationComplianceRecordNoncomplianceReasonNone",
    "PropertyIncludeActivationComplianceRecordNoncomplianceReasonNoneOutputReference",
    "PropertyIncludeActivationComplianceRecordNoncomplianceReasonOther",
    "PropertyIncludeActivationComplianceRecordNoncomplianceReasonOtherOutputReference",
    "PropertyIncludeActivationComplianceRecordOutputReference",
    "PropertyIncludeActivationConfig",
    "PropertyIncludeActivationTimeouts",
    "PropertyIncludeActivationTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__b369e9cad307216989a2601b3ebe57f3ce94b8810ffe17dc2229727f942563c3(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    contract_id: builtins.str,
    group_id: builtins.str,
    include_id: builtins.str,
    network: builtins.str,
    notify_emails: typing.Sequence[builtins.str],
    version: jsii.Number,
    auto_acknowledge_rule_warnings: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    compliance_record: typing.Optional[typing.Union[PropertyIncludeActivationComplianceRecord, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    note: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[PropertyIncludeActivationTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__7a3575d8bdd88b5e698d5bb47ad0f143bbb2eb621387a1b99ed3b1251b657c39(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6465edba9b0dbb514539e48f9c749ea8cd9ba91113f34c5fdec252272b5437db(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__363854128813ebbd6e7592fa0d39672e3b71aff8c1feef49cf51b0b64efa6091(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99ae78abee3d6caee53f7748f7e530e817acec7b161c6b9b079f5f24ac8dc071(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__818003c173aa9fca615b90fda8224f3449afa01d25419d844e0535852cb8d746(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac446c014fcafaf349de79807ae7100f708701949f9dd30b46e04a0e248d8d54(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3a8134d5b592464f1d7789b17923d667ca97bd38c05523ce8e022326ea99906(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2deb61cb5e7ff94374e1735c5be02968d22ac8599bc5c81051a0a52ecb579697(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbba224b9284aa89e03f464a8a9bacf4789d8a7e713a43099d2c5e62d2a7d0be(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2f2e7556c9c035a9635d76278cb31362bc88d75ed5cecb2c7ada670f20cdead(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92a8012a3c00c4350095bc4ad4674886bc6841b3f5dd8f15a182507fbfb97d34(
    *,
    noncompliance_reason_emergency: typing.Optional[typing.Union[PropertyIncludeActivationComplianceRecordNoncomplianceReasonEmergency, typing.Dict[builtins.str, typing.Any]]] = None,
    noncompliance_reason_none: typing.Optional[typing.Union[PropertyIncludeActivationComplianceRecordNoncomplianceReasonNone, typing.Dict[builtins.str, typing.Any]]] = None,
    noncompliance_reason_no_production_traffic: typing.Optional[typing.Union[PropertyIncludeActivationComplianceRecordNoncomplianceReasonNoProductionTraffic, typing.Dict[builtins.str, typing.Any]]] = None,
    noncompliance_reason_other: typing.Optional[typing.Union[PropertyIncludeActivationComplianceRecordNoncomplianceReasonOther, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc5ca3d9282594654dd655e3bd3de57760bde0c45f7b707283942490e6070875(
    *,
    ticket_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c465093aad3bf35e75d9ea884dca15bc9e5b16274fb60f8b681e02adb5d4249(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e7c9301e35c89d5dada15a9465477ec25ed2e7f074a04bf305695c59ba6af73(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__692431355ff8db08ba7555be848da2a25f005ef5a0189ce323b995245d37daa1(
    value: typing.Optional[PropertyIncludeActivationComplianceRecordNoncomplianceReasonEmergency],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7feb886481bd9390ad2fbeafdca9ecd61ed905a366fa1af81ddb11d0bbebbe7e(
    *,
    ticket_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89ca58c63f4ba675d2f43a633e68c8318da873df7ea4c2826c28e17903b6f998(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__442bb06cc0359e5ca0dd06cf9b46c08cb8075144de2531c36008b1db25fc20b3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dd93c51e570f929007a160483bd50654f6dcbfa008341836b8ede00bdd1814b(
    value: typing.Optional[PropertyIncludeActivationComplianceRecordNoncomplianceReasonNoProductionTraffic],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f4d8b341a72f2b7570234ac2c333f29ec795f4e3d66607f423d7d2ae10aec6e(
    *,
    customer_email: typing.Optional[builtins.str] = None,
    peer_reviewed_by: typing.Optional[builtins.str] = None,
    ticket_id: typing.Optional[builtins.str] = None,
    unit_tested: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1fbf8db33cf91b89f541cf2950d8007f3f2679001ad49477c5d38eef4fb3940(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ed06e8c4c43b339c63cbd6d3e971bdb9fdfe6060c8b5db8f08c741edb3815a5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e2bd620068b7fc4d74244fb374c66ee08e710dbba03feb033c59dfebc040740(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc85176d6ab41897f15fc734d25a0573d3ab30b0e44a1023e7201d4e23273ab5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b9f2ffbbb117a105ce2212589d9a97d1cc80e7d1d1ff3e3a3d7d3681f1ab1fd(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3532109b1317557630c9229c8a03d3ef08038fded2d1460218bcfe762cdd709(
    value: typing.Optional[PropertyIncludeActivationComplianceRecordNoncomplianceReasonNone],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6571989beca2ff63808125f6b7a09d19491d17e8f989eb881510377dc2da0df(
    *,
    other_noncompliance_reason: typing.Optional[builtins.str] = None,
    ticket_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc86aa1394a0580f4a348a9049708daa8866efcf907f58cae93b3b6edc9ed3c9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e25cd70213bf92c6dad0672ef4481cefbffea7b11e8d854887266f2de5692a4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0e365c804c97925d4593994d94476bd610e65f3bb949d79121c1863b5063569(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__895225627bb708e5054ec04b6122d765e239dcb5b78e6e42c99557e9cd5f5f23(
    value: typing.Optional[PropertyIncludeActivationComplianceRecordNoncomplianceReasonOther],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d5809e383738ed93ebea3ea858da52851059ad60a9a93adb095309bd2e0ce5e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__792de28e7454649e7e9bb51a0c31b08d6c5fb0d6a121b73b0df211b95ac6fe0a(
    value: typing.Optional[PropertyIncludeActivationComplianceRecord],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc375cd5939d582c8a0d20e9c80c3d34829b87da35123d993917f92599ccb11f(
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
    include_id: builtins.str,
    network: builtins.str,
    notify_emails: typing.Sequence[builtins.str],
    version: jsii.Number,
    auto_acknowledge_rule_warnings: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    compliance_record: typing.Optional[typing.Union[PropertyIncludeActivationComplianceRecord, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    note: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[PropertyIncludeActivationTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc6183f30757dd269b292348eb438116783069e3613d63b0d72912c302b273d2(
    *,
    default: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bd3922668f64aae19dba49e8111369675745cafd25ac80d17824ce9188806a5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02f48064e2cb6c90d8ea07e4893fd64c1006181023e4950a9b2baca8c57ba6be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13699ec7beb10e154de5d98914dbda1b7a2793e20f60953735479999b7945f3a(
    value: typing.Optional[PropertyIncludeActivationTimeouts],
) -> None:
    """Type checking stubs"""
    pass
