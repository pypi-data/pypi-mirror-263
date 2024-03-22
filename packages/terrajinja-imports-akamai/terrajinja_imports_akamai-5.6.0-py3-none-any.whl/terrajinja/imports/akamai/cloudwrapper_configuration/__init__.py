'''
# `akamai_cloudwrapper_configuration`

Refer to the Terraform Registry for docs: [`akamai_cloudwrapper_configuration`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration).
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


class CloudwrapperConfiguration(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.cloudwrapperConfiguration.CloudwrapperConfiguration",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration akamai_cloudwrapper_configuration}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        comments: builtins.str,
        config_name: builtins.str,
        contract_id: builtins.str,
        property_ids: typing.Sequence[builtins.str],
        capacity_alerts_threshold: typing.Optional[jsii.Number] = None,
        location: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudwrapperConfigurationLocation", typing.Dict[builtins.str, typing.Any]]]]] = None,
        notification_emails: typing.Optional[typing.Sequence[builtins.str]] = None,
        retain_idle_objects: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["CloudwrapperConfigurationTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration akamai_cloudwrapper_configuration} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param comments: Additional information you provide to differentiate or track changes of the configuration. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#comments CloudwrapperConfiguration#comments}
        :param config_name: Name of the configuration. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#config_name CloudwrapperConfiguration#config_name}
        :param contract_id: Contract ID having Cloud Wrapper entitlement. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#contract_id CloudwrapperConfiguration#contract_id}
        :param property_ids: List of properties belonging to eligible products. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#property_ids CloudwrapperConfiguration#property_ids}
        :param capacity_alerts_threshold: Capacity Alerts enablement information for the configuration. The Alert Threshold should be between 50 and 100. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#capacity_alerts_threshold CloudwrapperConfiguration#capacity_alerts_threshold}
        :param location: location block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#location CloudwrapperConfiguration#location}
        :param notification_emails: Email addresses to use for notifications. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#notification_emails CloudwrapperConfiguration#notification_emails}
        :param retain_idle_objects: Retain idle objects beyond their max idle lifetime. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#retain_idle_objects CloudwrapperConfiguration#retain_idle_objects}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#timeouts CloudwrapperConfiguration#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__762adff78f848593d3ab0b57d276e2e6388564c6440c567ece1d405634c249e1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = CloudwrapperConfigurationConfig(
            comments=comments,
            config_name=config_name,
            contract_id=contract_id,
            property_ids=property_ids,
            capacity_alerts_threshold=capacity_alerts_threshold,
            location=location,
            notification_emails=notification_emails,
            retain_idle_objects=retain_idle_objects,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="generateConfigForImport")
    @builtins.classmethod
    def generate_config_for_import(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        import_to_id: builtins.str,
        import_from_id: builtins.str,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    ) -> _cdktf_9a9027ec.ImportableResource:
        '''Generates CDKTF code for importing a CloudwrapperConfiguration resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the CloudwrapperConfiguration to import.
        :param import_from_id: The id of the existing CloudwrapperConfiguration that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the CloudwrapperConfiguration to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8130bc92734957f239cef9669f0641688d019b0b9ea170566cdc50960477cd8f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putLocation")
    def put_location(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudwrapperConfigurationLocation", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fa57b4a699790b76c53d24e59982abd793c65867da3935d1bd28f1254ab30e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLocation", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self, *, delete: typing.Optional[builtins.str] = None) -> None:
        '''
        :param delete: A string that can be `parsed as a duration <https://pkg.go.dev/time#ParseDuration>`_ consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours). Setting a timeout for a Delete operation is only applicable if changes are saved into state before the destroy operation occurs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#delete CloudwrapperConfiguration#delete}
        '''
        value = CloudwrapperConfigurationTimeouts(delete=delete)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCapacityAlertsThreshold")
    def reset_capacity_alerts_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacityAlertsThreshold", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetNotificationEmails")
    def reset_notification_emails(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationEmails", []))

    @jsii.member(jsii_name="resetRetainIdleObjects")
    def reset_retain_idle_objects(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetainIdleObjects", []))

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
    @jsii.member(jsii_name="id")
    def id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> "CloudwrapperConfigurationLocationList":
        return typing.cast("CloudwrapperConfigurationLocationList", jsii.get(self, "location"))

    @builtins.property
    @jsii.member(jsii_name="revision")
    def revision(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "revision"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "CloudwrapperConfigurationTimeoutsOutputReference":
        return typing.cast("CloudwrapperConfigurationTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="capacityAlertsThresholdInput")
    def capacity_alerts_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "capacityAlertsThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="commentsInput")
    def comments_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentsInput"))

    @builtins.property
    @jsii.member(jsii_name="configNameInput")
    def config_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configNameInput"))

    @builtins.property
    @jsii.member(jsii_name="contractIdInput")
    def contract_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contractIdInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudwrapperConfigurationLocation"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudwrapperConfigurationLocation"]]], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationEmailsInput")
    def notification_emails_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "notificationEmailsInput"))

    @builtins.property
    @jsii.member(jsii_name="propertyIdsInput")
    def property_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "propertyIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="retainIdleObjectsInput")
    def retain_idle_objects_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "retainIdleObjectsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "CloudwrapperConfigurationTimeouts"]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "CloudwrapperConfigurationTimeouts"]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="capacityAlertsThreshold")
    def capacity_alerts_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "capacityAlertsThreshold"))

    @capacity_alerts_threshold.setter
    def capacity_alerts_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c15c8193bf621005bdaf8b61230fd643b64725b5508e3ea241fe9f6a3acefc4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacityAlertsThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="comments")
    def comments(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comments"))

    @comments.setter
    def comments(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16b57a9823bbc393a4eecc6ef98e227280956748c91c3fdb5ec950b8e59f2ff9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comments", value)

    @builtins.property
    @jsii.member(jsii_name="configName")
    def config_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configName"))

    @config_name.setter
    def config_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b81b5e3f2338a88a5f8f56c25acc44454a7c61e2534735723c7cc181c960eb1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configName", value)

    @builtins.property
    @jsii.member(jsii_name="contractId")
    def contract_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contractId"))

    @contract_id.setter
    def contract_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__417185f20ec8281858a8d0ce71af7e74c0f42ba3b9e9bf0af407e5efe6d29acb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contractId", value)

    @builtins.property
    @jsii.member(jsii_name="notificationEmails")
    def notification_emails(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "notificationEmails"))

    @notification_emails.setter
    def notification_emails(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47ddf6937dee3eb6aaa2bbf69372d050b6fbccf84fa7da2059fd06d909ba6733)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationEmails", value)

    @builtins.property
    @jsii.member(jsii_name="propertyIds")
    def property_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "propertyIds"))

    @property_ids.setter
    def property_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57b6479ad2073964fbaab2037754ee6910168ab728dfca481370ecf98fc1a95c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "propertyIds", value)

    @builtins.property
    @jsii.member(jsii_name="retainIdleObjects")
    def retain_idle_objects(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "retainIdleObjects"))

    @retain_idle_objects.setter
    def retain_idle_objects(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35d2911f2e8b2a04c34379ccd448e7b5f311d3c7f663ef2dd5070767567bcf3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retainIdleObjects", value)


@jsii.data_type(
    jsii_type="akamai.cloudwrapperConfiguration.CloudwrapperConfigurationConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "comments": "comments",
        "config_name": "configName",
        "contract_id": "contractId",
        "property_ids": "propertyIds",
        "capacity_alerts_threshold": "capacityAlertsThreshold",
        "location": "location",
        "notification_emails": "notificationEmails",
        "retain_idle_objects": "retainIdleObjects",
        "timeouts": "timeouts",
    },
)
class CloudwrapperConfigurationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        comments: builtins.str,
        config_name: builtins.str,
        contract_id: builtins.str,
        property_ids: typing.Sequence[builtins.str],
        capacity_alerts_threshold: typing.Optional[jsii.Number] = None,
        location: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudwrapperConfigurationLocation", typing.Dict[builtins.str, typing.Any]]]]] = None,
        notification_emails: typing.Optional[typing.Sequence[builtins.str]] = None,
        retain_idle_objects: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["CloudwrapperConfigurationTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param comments: Additional information you provide to differentiate or track changes of the configuration. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#comments CloudwrapperConfiguration#comments}
        :param config_name: Name of the configuration. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#config_name CloudwrapperConfiguration#config_name}
        :param contract_id: Contract ID having Cloud Wrapper entitlement. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#contract_id CloudwrapperConfiguration#contract_id}
        :param property_ids: List of properties belonging to eligible products. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#property_ids CloudwrapperConfiguration#property_ids}
        :param capacity_alerts_threshold: Capacity Alerts enablement information for the configuration. The Alert Threshold should be between 50 and 100. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#capacity_alerts_threshold CloudwrapperConfiguration#capacity_alerts_threshold}
        :param location: location block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#location CloudwrapperConfiguration#location}
        :param notification_emails: Email addresses to use for notifications. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#notification_emails CloudwrapperConfiguration#notification_emails}
        :param retain_idle_objects: Retain idle objects beyond their max idle lifetime. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#retain_idle_objects CloudwrapperConfiguration#retain_idle_objects}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#timeouts CloudwrapperConfiguration#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = CloudwrapperConfigurationTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cfe30e7e5286f5d3acbf95504fd4f5754cdc945216a4fae5ef64a2872ba4f52)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument comments", value=comments, expected_type=type_hints["comments"])
            check_type(argname="argument config_name", value=config_name, expected_type=type_hints["config_name"])
            check_type(argname="argument contract_id", value=contract_id, expected_type=type_hints["contract_id"])
            check_type(argname="argument property_ids", value=property_ids, expected_type=type_hints["property_ids"])
            check_type(argname="argument capacity_alerts_threshold", value=capacity_alerts_threshold, expected_type=type_hints["capacity_alerts_threshold"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument notification_emails", value=notification_emails, expected_type=type_hints["notification_emails"])
            check_type(argname="argument retain_idle_objects", value=retain_idle_objects, expected_type=type_hints["retain_idle_objects"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "comments": comments,
            "config_name": config_name,
            "contract_id": contract_id,
            "property_ids": property_ids,
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
        if capacity_alerts_threshold is not None:
            self._values["capacity_alerts_threshold"] = capacity_alerts_threshold
        if location is not None:
            self._values["location"] = location
        if notification_emails is not None:
            self._values["notification_emails"] = notification_emails
        if retain_idle_objects is not None:
            self._values["retain_idle_objects"] = retain_idle_objects
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
    def comments(self) -> builtins.str:
        '''Additional information you provide to differentiate or track changes of the configuration.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#comments CloudwrapperConfiguration#comments}
        '''
        result = self._values.get("comments")
        assert result is not None, "Required property 'comments' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def config_name(self) -> builtins.str:
        '''Name of the configuration.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#config_name CloudwrapperConfiguration#config_name}
        '''
        result = self._values.get("config_name")
        assert result is not None, "Required property 'config_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def contract_id(self) -> builtins.str:
        '''Contract ID having Cloud Wrapper entitlement.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#contract_id CloudwrapperConfiguration#contract_id}
        '''
        result = self._values.get("contract_id")
        assert result is not None, "Required property 'contract_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def property_ids(self) -> typing.List[builtins.str]:
        '''List of properties belonging to eligible products.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#property_ids CloudwrapperConfiguration#property_ids}
        '''
        result = self._values.get("property_ids")
        assert result is not None, "Required property 'property_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def capacity_alerts_threshold(self) -> typing.Optional[jsii.Number]:
        '''Capacity Alerts enablement information for the configuration. The Alert Threshold should be between 50 and 100.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#capacity_alerts_threshold CloudwrapperConfiguration#capacity_alerts_threshold}
        '''
        result = self._values.get("capacity_alerts_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def location(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudwrapperConfigurationLocation"]]]:
        '''location block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#location CloudwrapperConfiguration#location}
        '''
        result = self._values.get("location")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudwrapperConfigurationLocation"]]], result)

    @builtins.property
    def notification_emails(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Email addresses to use for notifications.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#notification_emails CloudwrapperConfiguration#notification_emails}
        '''
        result = self._values.get("notification_emails")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def retain_idle_objects(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Retain idle objects beyond their max idle lifetime.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#retain_idle_objects CloudwrapperConfiguration#retain_idle_objects}
        '''
        result = self._values.get("retain_idle_objects")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["CloudwrapperConfigurationTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#timeouts CloudwrapperConfiguration#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["CloudwrapperConfigurationTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwrapperConfigurationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.cloudwrapperConfiguration.CloudwrapperConfigurationLocation",
    jsii_struct_bases=[],
    name_mapping={
        "capacity": "capacity",
        "comments": "comments",
        "traffic_type_id": "trafficTypeId",
    },
)
class CloudwrapperConfigurationLocation:
    def __init__(
        self,
        *,
        capacity: typing.Union["CloudwrapperConfigurationLocationCapacity", typing.Dict[builtins.str, typing.Any]],
        comments: builtins.str,
        traffic_type_id: jsii.Number,
    ) -> None:
        '''
        :param capacity: capacity block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#capacity CloudwrapperConfiguration#capacity}
        :param comments: Additional comments provided by the user. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#comments CloudwrapperConfiguration#comments}
        :param traffic_type_id: Unique identifier for the location and traffic type combination. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#traffic_type_id CloudwrapperConfiguration#traffic_type_id}
        '''
        if isinstance(capacity, dict):
            capacity = CloudwrapperConfigurationLocationCapacity(**capacity)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea42a474cd2914e06821049b4f3092b5e9066983936823869a634b4737a017bd)
            check_type(argname="argument capacity", value=capacity, expected_type=type_hints["capacity"])
            check_type(argname="argument comments", value=comments, expected_type=type_hints["comments"])
            check_type(argname="argument traffic_type_id", value=traffic_type_id, expected_type=type_hints["traffic_type_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "capacity": capacity,
            "comments": comments,
            "traffic_type_id": traffic_type_id,
        }

    @builtins.property
    def capacity(self) -> "CloudwrapperConfigurationLocationCapacity":
        '''capacity block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#capacity CloudwrapperConfiguration#capacity}
        '''
        result = self._values.get("capacity")
        assert result is not None, "Required property 'capacity' is missing"
        return typing.cast("CloudwrapperConfigurationLocationCapacity", result)

    @builtins.property
    def comments(self) -> builtins.str:
        '''Additional comments provided by the user.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#comments CloudwrapperConfiguration#comments}
        '''
        result = self._values.get("comments")
        assert result is not None, "Required property 'comments' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def traffic_type_id(self) -> jsii.Number:
        '''Unique identifier for the location and traffic type combination.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#traffic_type_id CloudwrapperConfiguration#traffic_type_id}
        '''
        result = self._values.get("traffic_type_id")
        assert result is not None, "Required property 'traffic_type_id' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwrapperConfigurationLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.cloudwrapperConfiguration.CloudwrapperConfigurationLocationCapacity",
    jsii_struct_bases=[],
    name_mapping={"unit": "unit", "value": "value"},
)
class CloudwrapperConfigurationLocationCapacity:
    def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Unit of capacity. Can be either 'GB' or 'TB'. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#unit CloudwrapperConfiguration#unit}
        :param value: Value of capacity. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#value CloudwrapperConfiguration#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c82dcfc0480d945503949d1b12b3de693a81f68f8d5288103d1f01af59d9155)
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "unit": unit,
            "value": value,
        }

    @builtins.property
    def unit(self) -> builtins.str:
        '''Unit of capacity. Can be either 'GB' or 'TB'.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#unit CloudwrapperConfiguration#unit}
        '''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Value of capacity.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#value CloudwrapperConfiguration#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwrapperConfigurationLocationCapacity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwrapperConfigurationLocationCapacityOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.cloudwrapperConfiguration.CloudwrapperConfigurationLocationCapacityOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0738b021ce424934421bc83bae48b1f1cf20bb6823c673469c3e564e85608161)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aca1acee734ffd9056bbdd550f8be8dfa9630578cd2603deaa3ca10940351b22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae375c414078bb18f573e7926e03b7ffec1925f2f3cfd19a366063c194c60b9a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CloudwrapperConfigurationLocationCapacity]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CloudwrapperConfigurationLocationCapacity]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CloudwrapperConfigurationLocationCapacity]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7148b6727a3358ec183851bb7676d9502428eb9196f57558e97d0b42cc2a931c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudwrapperConfigurationLocationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.cloudwrapperConfiguration.CloudwrapperConfigurationLocationList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fcf108103a015a12ff771d93ffe22ebd6d6af411fe844286e85a0f575498500a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CloudwrapperConfigurationLocationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c980528694c7e1d023d749ca9bb501a3ef539de435c751f653d4a8b53f9c97f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudwrapperConfigurationLocationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c40ac9ff85122b23f746d23b93a9ee0316c67fb77d1d68e27e0b94818264452e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cc6c8b547cc64177215b52b600b6238d79760f58853f6e6b362e7f167bef15fa)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ded795d77874ea0d4b51ad4ff4fdab0fa9e2bab54d8233e124f08f523ad956fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudwrapperConfigurationLocation]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudwrapperConfigurationLocation]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudwrapperConfigurationLocation]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f8590e9e539a17dea4c8d06191e9173b6bd9b41ed1ca6342950d355f07604dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudwrapperConfigurationLocationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.cloudwrapperConfiguration.CloudwrapperConfigurationLocationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1611f90d647826ab8e54fa1182437e2d6848b5f65178e647d68e7e5a8e5c6f41)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCapacity")
    def put_capacity(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Unit of capacity. Can be either 'GB' or 'TB'. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#unit CloudwrapperConfiguration#unit}
        :param value: Value of capacity. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#value CloudwrapperConfiguration#value}
        '''
        value_ = CloudwrapperConfigurationLocationCapacity(unit=unit, value=value)

        return typing.cast(None, jsii.invoke(self, "putCapacity", [value_]))

    @builtins.property
    @jsii.member(jsii_name="capacity")
    def capacity(self) -> CloudwrapperConfigurationLocationCapacityOutputReference:
        return typing.cast(CloudwrapperConfigurationLocationCapacityOutputReference, jsii.get(self, "capacity"))

    @builtins.property
    @jsii.member(jsii_name="capacityInput")
    def capacity_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CloudwrapperConfigurationLocationCapacity]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CloudwrapperConfigurationLocationCapacity]], jsii.get(self, "capacityInput"))

    @builtins.property
    @jsii.member(jsii_name="commentsInput")
    def comments_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentsInput"))

    @builtins.property
    @jsii.member(jsii_name="trafficTypeIdInput")
    def traffic_type_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "trafficTypeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="comments")
    def comments(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comments"))

    @comments.setter
    def comments(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6dea1727e6f098bd3bce15b583a073b288a6425e0afcc4adb19c4ed243384663)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comments", value)

    @builtins.property
    @jsii.member(jsii_name="trafficTypeId")
    def traffic_type_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "trafficTypeId"))

    @traffic_type_id.setter
    def traffic_type_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06ab84408578e412d9531fc1e20d93f8f7db40919731d93ca4a9a797fc4836be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trafficTypeId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CloudwrapperConfigurationLocation]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CloudwrapperConfigurationLocation]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CloudwrapperConfigurationLocation]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a558c1773a7c25a6989c35073851fb9722372ea31b69f3ce02b672880fee5ccb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.cloudwrapperConfiguration.CloudwrapperConfigurationTimeouts",
    jsii_struct_bases=[],
    name_mapping={"delete": "delete"},
)
class CloudwrapperConfigurationTimeouts:
    def __init__(self, *, delete: typing.Optional[builtins.str] = None) -> None:
        '''
        :param delete: A string that can be `parsed as a duration <https://pkg.go.dev/time#ParseDuration>`_ consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours). Setting a timeout for a Delete operation is only applicable if changes are saved into state before the destroy operation occurs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#delete CloudwrapperConfiguration#delete}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23d87a1d28af2657272d3cda693260410b28554bdb24afd49a206844d2baac9e)
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''A string that can be `parsed as a duration <https://pkg.go.dev/time#ParseDuration>`_ consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours). Setting a timeout for a Delete operation is only applicable if changes are saved into state before the destroy operation occurs.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudwrapper_configuration#delete CloudwrapperConfiguration#delete}
        '''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudwrapperConfigurationTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudwrapperConfigurationTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.cloudwrapperConfiguration.CloudwrapperConfigurationTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__520bb306c8ef73f19b5149e3efbdad72c4b1bbb61e7e972f8c7ee92fdf525a22)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afecd57a15eec14a856c3c70151a390b39b97e19ab3124d8dc0f85c71495b5db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CloudwrapperConfigurationTimeouts]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CloudwrapperConfigurationTimeouts]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CloudwrapperConfigurationTimeouts]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fdcc66029940d091f060918d908898e9d6f82a04ad5518c1f98b686d6b68222a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CloudwrapperConfiguration",
    "CloudwrapperConfigurationConfig",
    "CloudwrapperConfigurationLocation",
    "CloudwrapperConfigurationLocationCapacity",
    "CloudwrapperConfigurationLocationCapacityOutputReference",
    "CloudwrapperConfigurationLocationList",
    "CloudwrapperConfigurationLocationOutputReference",
    "CloudwrapperConfigurationTimeouts",
    "CloudwrapperConfigurationTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__762adff78f848593d3ab0b57d276e2e6388564c6440c567ece1d405634c249e1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    comments: builtins.str,
    config_name: builtins.str,
    contract_id: builtins.str,
    property_ids: typing.Sequence[builtins.str],
    capacity_alerts_threshold: typing.Optional[jsii.Number] = None,
    location: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudwrapperConfigurationLocation, typing.Dict[builtins.str, typing.Any]]]]] = None,
    notification_emails: typing.Optional[typing.Sequence[builtins.str]] = None,
    retain_idle_objects: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    timeouts: typing.Optional[typing.Union[CloudwrapperConfigurationTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__8130bc92734957f239cef9669f0641688d019b0b9ea170566cdc50960477cd8f(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fa57b4a699790b76c53d24e59982abd793c65867da3935d1bd28f1254ab30e9(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudwrapperConfigurationLocation, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c15c8193bf621005bdaf8b61230fd643b64725b5508e3ea241fe9f6a3acefc4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16b57a9823bbc393a4eecc6ef98e227280956748c91c3fdb5ec950b8e59f2ff9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b81b5e3f2338a88a5f8f56c25acc44454a7c61e2534735723c7cc181c960eb1a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__417185f20ec8281858a8d0ce71af7e74c0f42ba3b9e9bf0af407e5efe6d29acb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47ddf6937dee3eb6aaa2bbf69372d050b6fbccf84fa7da2059fd06d909ba6733(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57b6479ad2073964fbaab2037754ee6910168ab728dfca481370ecf98fc1a95c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35d2911f2e8b2a04c34379ccd448e7b5f311d3c7f663ef2dd5070767567bcf3a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cfe30e7e5286f5d3acbf95504fd4f5754cdc945216a4fae5ef64a2872ba4f52(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    comments: builtins.str,
    config_name: builtins.str,
    contract_id: builtins.str,
    property_ids: typing.Sequence[builtins.str],
    capacity_alerts_threshold: typing.Optional[jsii.Number] = None,
    location: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudwrapperConfigurationLocation, typing.Dict[builtins.str, typing.Any]]]]] = None,
    notification_emails: typing.Optional[typing.Sequence[builtins.str]] = None,
    retain_idle_objects: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    timeouts: typing.Optional[typing.Union[CloudwrapperConfigurationTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea42a474cd2914e06821049b4f3092b5e9066983936823869a634b4737a017bd(
    *,
    capacity: typing.Union[CloudwrapperConfigurationLocationCapacity, typing.Dict[builtins.str, typing.Any]],
    comments: builtins.str,
    traffic_type_id: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c82dcfc0480d945503949d1b12b3de693a81f68f8d5288103d1f01af59d9155(
    *,
    unit: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0738b021ce424934421bc83bae48b1f1cf20bb6823c673469c3e564e85608161(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aca1acee734ffd9056bbdd550f8be8dfa9630578cd2603deaa3ca10940351b22(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae375c414078bb18f573e7926e03b7ffec1925f2f3cfd19a366063c194c60b9a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7148b6727a3358ec183851bb7676d9502428eb9196f57558e97d0b42cc2a931c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CloudwrapperConfigurationLocationCapacity]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcf108103a015a12ff771d93ffe22ebd6d6af411fe844286e85a0f575498500a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c980528694c7e1d023d749ca9bb501a3ef539de435c751f653d4a8b53f9c97f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c40ac9ff85122b23f746d23b93a9ee0316c67fb77d1d68e27e0b94818264452e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc6c8b547cc64177215b52b600b6238d79760f58853f6e6b362e7f167bef15fa(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ded795d77874ea0d4b51ad4ff4fdab0fa9e2bab54d8233e124f08f523ad956fe(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f8590e9e539a17dea4c8d06191e9173b6bd9b41ed1ca6342950d355f07604dc(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudwrapperConfigurationLocation]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1611f90d647826ab8e54fa1182437e2d6848b5f65178e647d68e7e5a8e5c6f41(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6dea1727e6f098bd3bce15b583a073b288a6425e0afcc4adb19c4ed243384663(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06ab84408578e412d9531fc1e20d93f8f7db40919731d93ca4a9a797fc4836be(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a558c1773a7c25a6989c35073851fb9722372ea31b69f3ce02b672880fee5ccb(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CloudwrapperConfigurationLocation]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23d87a1d28af2657272d3cda693260410b28554bdb24afd49a206844d2baac9e(
    *,
    delete: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__520bb306c8ef73f19b5149e3efbdad72c4b1bbb61e7e972f8c7ee92fdf525a22(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afecd57a15eec14a856c3c70151a390b39b97e19ab3124d8dc0f85c71495b5db(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdcc66029940d091f060918d908898e9d6f82a04ad5518c1f98b686d6b68222a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CloudwrapperConfigurationTimeouts]],
) -> None:
    """Type checking stubs"""
    pass
