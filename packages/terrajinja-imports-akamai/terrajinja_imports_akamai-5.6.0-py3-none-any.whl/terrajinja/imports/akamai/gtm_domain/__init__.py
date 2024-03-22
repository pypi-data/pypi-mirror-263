'''
# `akamai_gtm_domain`

Refer to the Terraform Registry for docs: [`akamai_gtm_domain`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain).
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


class GtmDomain(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.gtmDomain.GtmDomain",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain akamai_gtm_domain}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        type: builtins.str,
        cname_coalescing_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        comment: typing.Optional[builtins.str] = None,
        contract: typing.Optional[builtins.str] = None,
        default_error_penalty: typing.Optional[jsii.Number] = None,
        default_ssl_client_certificate: typing.Optional[builtins.str] = None,
        default_ssl_client_private_key: typing.Optional[builtins.str] = None,
        default_timeout_penalty: typing.Optional[jsii.Number] = None,
        email_notification_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        end_user_mapping_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        group: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        load_feedback: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        load_imbalance_percentage: typing.Optional[jsii.Number] = None,
        wait_on_complete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain akamai_gtm_domain} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#name GtmDomain#name}.
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#type GtmDomain#type}.
        :param cname_coalescing_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#cname_coalescing_enabled GtmDomain#cname_coalescing_enabled}.
        :param comment: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#comment GtmDomain#comment}.
        :param contract: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#contract GtmDomain#contract}.
        :param default_error_penalty: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#default_error_penalty GtmDomain#default_error_penalty}.
        :param default_ssl_client_certificate: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#default_ssl_client_certificate GtmDomain#default_ssl_client_certificate}.
        :param default_ssl_client_private_key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#default_ssl_client_private_key GtmDomain#default_ssl_client_private_key}.
        :param default_timeout_penalty: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#default_timeout_penalty GtmDomain#default_timeout_penalty}.
        :param email_notification_list: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#email_notification_list GtmDomain#email_notification_list}.
        :param end_user_mapping_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#end_user_mapping_enabled GtmDomain#end_user_mapping_enabled}.
        :param group: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#group GtmDomain#group}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#id GtmDomain#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param load_feedback: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#load_feedback GtmDomain#load_feedback}.
        :param load_imbalance_percentage: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#load_imbalance_percentage GtmDomain#load_imbalance_percentage}.
        :param wait_on_complete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#wait_on_complete GtmDomain#wait_on_complete}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ea9fd0f398d4344f7a1fca2762602add0adebb29f40ddcad5b5253c46b1e528)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GtmDomainConfig(
            name=name,
            type=type,
            cname_coalescing_enabled=cname_coalescing_enabled,
            comment=comment,
            contract=contract,
            default_error_penalty=default_error_penalty,
            default_ssl_client_certificate=default_ssl_client_certificate,
            default_ssl_client_private_key=default_ssl_client_private_key,
            default_timeout_penalty=default_timeout_penalty,
            email_notification_list=email_notification_list,
            end_user_mapping_enabled=end_user_mapping_enabled,
            group=group,
            id=id,
            load_feedback=load_feedback,
            load_imbalance_percentage=load_imbalance_percentage,
            wait_on_complete=wait_on_complete,
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
        '''Generates CDKTF code for importing a GtmDomain resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the GtmDomain to import.
        :param import_from_id: The id of the existing GtmDomain that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the GtmDomain to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1633cdfa0700f84058b0ec0c5190b71e01b249f2ab665602994c251cf59293dc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetCnameCoalescingEnabled")
    def reset_cname_coalescing_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCnameCoalescingEnabled", []))

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

    @jsii.member(jsii_name="resetContract")
    def reset_contract(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContract", []))

    @jsii.member(jsii_name="resetDefaultErrorPenalty")
    def reset_default_error_penalty(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultErrorPenalty", []))

    @jsii.member(jsii_name="resetDefaultSslClientCertificate")
    def reset_default_ssl_client_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultSslClientCertificate", []))

    @jsii.member(jsii_name="resetDefaultSslClientPrivateKey")
    def reset_default_ssl_client_private_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultSslClientPrivateKey", []))

    @jsii.member(jsii_name="resetDefaultTimeoutPenalty")
    def reset_default_timeout_penalty(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultTimeoutPenalty", []))

    @jsii.member(jsii_name="resetEmailNotificationList")
    def reset_email_notification_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailNotificationList", []))

    @jsii.member(jsii_name="resetEndUserMappingEnabled")
    def reset_end_user_mapping_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndUserMappingEnabled", []))

    @jsii.member(jsii_name="resetGroup")
    def reset_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroup", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLoadFeedback")
    def reset_load_feedback(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadFeedback", []))

    @jsii.member(jsii_name="resetLoadImbalancePercentage")
    def reset_load_imbalance_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadImbalancePercentage", []))

    @jsii.member(jsii_name="resetWaitOnComplete")
    def reset_wait_on_complete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitOnComplete", []))

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
    @jsii.member(jsii_name="defaultHealthMax")
    def default_health_max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultHealthMax"))

    @builtins.property
    @jsii.member(jsii_name="defaultHealthMultiplier")
    def default_health_multiplier(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultHealthMultiplier"))

    @builtins.property
    @jsii.member(jsii_name="defaultHealthThreshold")
    def default_health_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultHealthThreshold"))

    @builtins.property
    @jsii.member(jsii_name="defaultMaxUnreachablePenalty")
    def default_max_unreachable_penalty(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultMaxUnreachablePenalty"))

    @builtins.property
    @jsii.member(jsii_name="defaultUnreachableThreshold")
    def default_unreachable_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultUnreachableThreshold"))

    @builtins.property
    @jsii.member(jsii_name="mapUpdateInterval")
    def map_update_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "mapUpdateInterval"))

    @builtins.property
    @jsii.member(jsii_name="maxProperties")
    def max_properties(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxProperties"))

    @builtins.property
    @jsii.member(jsii_name="maxResources")
    def max_resources(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxResources"))

    @builtins.property
    @jsii.member(jsii_name="maxTestTimeout")
    def max_test_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxTestTimeout"))

    @builtins.property
    @jsii.member(jsii_name="maxTtl")
    def max_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxTtl"))

    @builtins.property
    @jsii.member(jsii_name="minPingableRegionFraction")
    def min_pingable_region_fraction(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minPingableRegionFraction"))

    @builtins.property
    @jsii.member(jsii_name="minTestInterval")
    def min_test_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minTestInterval"))

    @builtins.property
    @jsii.member(jsii_name="minTtl")
    def min_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minTtl"))

    @builtins.property
    @jsii.member(jsii_name="pingInterval")
    def ping_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "pingInterval"))

    @builtins.property
    @jsii.member(jsii_name="pingPacketSize")
    def ping_packet_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "pingPacketSize"))

    @builtins.property
    @jsii.member(jsii_name="roundRobinPrefix")
    def round_robin_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roundRobinPrefix"))

    @builtins.property
    @jsii.member(jsii_name="servermonitorLivenessCount")
    def servermonitor_liveness_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "servermonitorLivenessCount"))

    @builtins.property
    @jsii.member(jsii_name="servermonitorLoadCount")
    def servermonitor_load_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "servermonitorLoadCount"))

    @builtins.property
    @jsii.member(jsii_name="servermonitorPool")
    def servermonitor_pool(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "servermonitorPool"))

    @builtins.property
    @jsii.member(jsii_name="cnameCoalescingEnabledInput")
    def cname_coalescing_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "cnameCoalescingEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="contractInput")
    def contract_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contractInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultErrorPenaltyInput")
    def default_error_penalty_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultErrorPenaltyInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultSslClientCertificateInput")
    def default_ssl_client_certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultSslClientCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultSslClientPrivateKeyInput")
    def default_ssl_client_private_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultSslClientPrivateKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultTimeoutPenaltyInput")
    def default_timeout_penalty_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultTimeoutPenaltyInput"))

    @builtins.property
    @jsii.member(jsii_name="emailNotificationListInput")
    def email_notification_list_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "emailNotificationListInput"))

    @builtins.property
    @jsii.member(jsii_name="endUserMappingEnabledInput")
    def end_user_mapping_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "endUserMappingEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="groupInput")
    def group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="loadFeedbackInput")
    def load_feedback_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "loadFeedbackInput"))

    @builtins.property
    @jsii.member(jsii_name="loadImbalancePercentageInput")
    def load_imbalance_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "loadImbalancePercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="waitOnCompleteInput")
    def wait_on_complete_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "waitOnCompleteInput"))

    @builtins.property
    @jsii.member(jsii_name="cnameCoalescingEnabled")
    def cname_coalescing_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "cnameCoalescingEnabled"))

    @cname_coalescing_enabled.setter
    def cname_coalescing_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__652166c94b6b8128cfe9606db386be6aa88b3ffbd1f5fabde3dc0f4eccbbf5c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cnameCoalescingEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d69953a390cf411cdb1abfc7478ae40a8c1c2b67caac2c59e93edcce434839c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="contract")
    def contract(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contract"))

    @contract.setter
    def contract(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9101de365f3b722a0e61a9d0a8bf364f7ee79b21a43a8c9be545469cc59818bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contract", value)

    @builtins.property
    @jsii.member(jsii_name="defaultErrorPenalty")
    def default_error_penalty(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultErrorPenalty"))

    @default_error_penalty.setter
    def default_error_penalty(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__198c0fc990b7504d29b1e0b7d401ad4bf9bd425492db202b4a85e46d86033f0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultErrorPenalty", value)

    @builtins.property
    @jsii.member(jsii_name="defaultSslClientCertificate")
    def default_ssl_client_certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultSslClientCertificate"))

    @default_ssl_client_certificate.setter
    def default_ssl_client_certificate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d41a0aaa7a846db025045b8b0a48f455a1af62f94261e2ff2c4b001b612e8adb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultSslClientCertificate", value)

    @builtins.property
    @jsii.member(jsii_name="defaultSslClientPrivateKey")
    def default_ssl_client_private_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultSslClientPrivateKey"))

    @default_ssl_client_private_key.setter
    def default_ssl_client_private_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__526f08786301f962350eb5858b6cf0769b4968b53aba0cd47aff56474993ba92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultSslClientPrivateKey", value)

    @builtins.property
    @jsii.member(jsii_name="defaultTimeoutPenalty")
    def default_timeout_penalty(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultTimeoutPenalty"))

    @default_timeout_penalty.setter
    def default_timeout_penalty(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__699c1ad3f73cc3b662574880f7a6aee2bc0a4384ad97371129d8899acad5654f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultTimeoutPenalty", value)

    @builtins.property
    @jsii.member(jsii_name="emailNotificationList")
    def email_notification_list(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "emailNotificationList"))

    @email_notification_list.setter
    def email_notification_list(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__469d38205424bd6afd09d938e78b8688948524dc09b00e13eb63752045e119a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailNotificationList", value)

    @builtins.property
    @jsii.member(jsii_name="endUserMappingEnabled")
    def end_user_mapping_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "endUserMappingEnabled"))

    @end_user_mapping_enabled.setter
    def end_user_mapping_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6e659121c3b67db3a3b2c5d44058e4800cd97bbac6620b4bbd47356484211a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endUserMappingEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="group")
    def group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "group"))

    @group.setter
    def group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aeb59dc1229725495eff2b072f9a994fed48d2a5896c8f5083b11e86ed316e3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "group", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd62e92e73f0c652384343c7b1739f454fc0439e9186c09028a70a767c9a4e9d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="loadFeedback")
    def load_feedback(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "loadFeedback"))

    @load_feedback.setter
    def load_feedback(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dae435d58b77563828d49edd53db2e9ea4810dbf0324fa731b1b72f9bb99ea4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadFeedback", value)

    @builtins.property
    @jsii.member(jsii_name="loadImbalancePercentage")
    def load_imbalance_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "loadImbalancePercentage"))

    @load_imbalance_percentage.setter
    def load_imbalance_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5e49ca1ef7328d96338969045bef348126904c11f84b6817a299980ca33647e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadImbalancePercentage", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecb7afa9516f6e020db575cd2b439af8a60c2f23205478beefddefa21ab379bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c754dfc7f6b494e8017d3a6a0c6a28487e427ab3a75bfb1bb81dcf19bcda3e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="waitOnComplete")
    def wait_on_complete(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "waitOnComplete"))

    @wait_on_complete.setter
    def wait_on_complete(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__321d4021a22e7ae47c314e51805494b11558677abb9f30e2ef297a4285418ec8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitOnComplete", value)


@jsii.data_type(
    jsii_type="akamai.gtmDomain.GtmDomainConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "type": "type",
        "cname_coalescing_enabled": "cnameCoalescingEnabled",
        "comment": "comment",
        "contract": "contract",
        "default_error_penalty": "defaultErrorPenalty",
        "default_ssl_client_certificate": "defaultSslClientCertificate",
        "default_ssl_client_private_key": "defaultSslClientPrivateKey",
        "default_timeout_penalty": "defaultTimeoutPenalty",
        "email_notification_list": "emailNotificationList",
        "end_user_mapping_enabled": "endUserMappingEnabled",
        "group": "group",
        "id": "id",
        "load_feedback": "loadFeedback",
        "load_imbalance_percentage": "loadImbalancePercentage",
        "wait_on_complete": "waitOnComplete",
    },
)
class GtmDomainConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        name: builtins.str,
        type: builtins.str,
        cname_coalescing_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        comment: typing.Optional[builtins.str] = None,
        contract: typing.Optional[builtins.str] = None,
        default_error_penalty: typing.Optional[jsii.Number] = None,
        default_ssl_client_certificate: typing.Optional[builtins.str] = None,
        default_ssl_client_private_key: typing.Optional[builtins.str] = None,
        default_timeout_penalty: typing.Optional[jsii.Number] = None,
        email_notification_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        end_user_mapping_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        group: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        load_feedback: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        load_imbalance_percentage: typing.Optional[jsii.Number] = None,
        wait_on_complete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#name GtmDomain#name}.
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#type GtmDomain#type}.
        :param cname_coalescing_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#cname_coalescing_enabled GtmDomain#cname_coalescing_enabled}.
        :param comment: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#comment GtmDomain#comment}.
        :param contract: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#contract GtmDomain#contract}.
        :param default_error_penalty: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#default_error_penalty GtmDomain#default_error_penalty}.
        :param default_ssl_client_certificate: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#default_ssl_client_certificate GtmDomain#default_ssl_client_certificate}.
        :param default_ssl_client_private_key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#default_ssl_client_private_key GtmDomain#default_ssl_client_private_key}.
        :param default_timeout_penalty: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#default_timeout_penalty GtmDomain#default_timeout_penalty}.
        :param email_notification_list: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#email_notification_list GtmDomain#email_notification_list}.
        :param end_user_mapping_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#end_user_mapping_enabled GtmDomain#end_user_mapping_enabled}.
        :param group: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#group GtmDomain#group}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#id GtmDomain#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param load_feedback: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#load_feedback GtmDomain#load_feedback}.
        :param load_imbalance_percentage: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#load_imbalance_percentage GtmDomain#load_imbalance_percentage}.
        :param wait_on_complete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#wait_on_complete GtmDomain#wait_on_complete}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b5e38fd63e5d022f60a03f47b2a19129ee899af45ce5ed573c55a02a0b6581e)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument cname_coalescing_enabled", value=cname_coalescing_enabled, expected_type=type_hints["cname_coalescing_enabled"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument contract", value=contract, expected_type=type_hints["contract"])
            check_type(argname="argument default_error_penalty", value=default_error_penalty, expected_type=type_hints["default_error_penalty"])
            check_type(argname="argument default_ssl_client_certificate", value=default_ssl_client_certificate, expected_type=type_hints["default_ssl_client_certificate"])
            check_type(argname="argument default_ssl_client_private_key", value=default_ssl_client_private_key, expected_type=type_hints["default_ssl_client_private_key"])
            check_type(argname="argument default_timeout_penalty", value=default_timeout_penalty, expected_type=type_hints["default_timeout_penalty"])
            check_type(argname="argument email_notification_list", value=email_notification_list, expected_type=type_hints["email_notification_list"])
            check_type(argname="argument end_user_mapping_enabled", value=end_user_mapping_enabled, expected_type=type_hints["end_user_mapping_enabled"])
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument load_feedback", value=load_feedback, expected_type=type_hints["load_feedback"])
            check_type(argname="argument load_imbalance_percentage", value=load_imbalance_percentage, expected_type=type_hints["load_imbalance_percentage"])
            check_type(argname="argument wait_on_complete", value=wait_on_complete, expected_type=type_hints["wait_on_complete"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
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
        if cname_coalescing_enabled is not None:
            self._values["cname_coalescing_enabled"] = cname_coalescing_enabled
        if comment is not None:
            self._values["comment"] = comment
        if contract is not None:
            self._values["contract"] = contract
        if default_error_penalty is not None:
            self._values["default_error_penalty"] = default_error_penalty
        if default_ssl_client_certificate is not None:
            self._values["default_ssl_client_certificate"] = default_ssl_client_certificate
        if default_ssl_client_private_key is not None:
            self._values["default_ssl_client_private_key"] = default_ssl_client_private_key
        if default_timeout_penalty is not None:
            self._values["default_timeout_penalty"] = default_timeout_penalty
        if email_notification_list is not None:
            self._values["email_notification_list"] = email_notification_list
        if end_user_mapping_enabled is not None:
            self._values["end_user_mapping_enabled"] = end_user_mapping_enabled
        if group is not None:
            self._values["group"] = group
        if id is not None:
            self._values["id"] = id
        if load_feedback is not None:
            self._values["load_feedback"] = load_feedback
        if load_imbalance_percentage is not None:
            self._values["load_imbalance_percentage"] = load_imbalance_percentage
        if wait_on_complete is not None:
            self._values["wait_on_complete"] = wait_on_complete

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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#name GtmDomain#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#type GtmDomain#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cname_coalescing_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#cname_coalescing_enabled GtmDomain#cname_coalescing_enabled}.'''
        result = self._values.get("cname_coalescing_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#comment GtmDomain#comment}.'''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def contract(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#contract GtmDomain#contract}.'''
        result = self._values.get("contract")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_error_penalty(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#default_error_penalty GtmDomain#default_error_penalty}.'''
        result = self._values.get("default_error_penalty")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def default_ssl_client_certificate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#default_ssl_client_certificate GtmDomain#default_ssl_client_certificate}.'''
        result = self._values.get("default_ssl_client_certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_ssl_client_private_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#default_ssl_client_private_key GtmDomain#default_ssl_client_private_key}.'''
        result = self._values.get("default_ssl_client_private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_timeout_penalty(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#default_timeout_penalty GtmDomain#default_timeout_penalty}.'''
        result = self._values.get("default_timeout_penalty")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def email_notification_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#email_notification_list GtmDomain#email_notification_list}.'''
        result = self._values.get("email_notification_list")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def end_user_mapping_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#end_user_mapping_enabled GtmDomain#end_user_mapping_enabled}.'''
        result = self._values.get("end_user_mapping_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def group(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#group GtmDomain#group}.'''
        result = self._values.get("group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#id GtmDomain#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def load_feedback(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#load_feedback GtmDomain#load_feedback}.'''
        result = self._values.get("load_feedback")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def load_imbalance_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#load_imbalance_percentage GtmDomain#load_imbalance_percentage}.'''
        result = self._values.get("load_imbalance_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def wait_on_complete(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_domain#wait_on_complete GtmDomain#wait_on_complete}.'''
        result = self._values.get("wait_on_complete")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GtmDomainConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "GtmDomain",
    "GtmDomainConfig",
]

publication.publish()

def _typecheckingstub__2ea9fd0f398d4344f7a1fca2762602add0adebb29f40ddcad5b5253c46b1e528(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    type: builtins.str,
    cname_coalescing_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    comment: typing.Optional[builtins.str] = None,
    contract: typing.Optional[builtins.str] = None,
    default_error_penalty: typing.Optional[jsii.Number] = None,
    default_ssl_client_certificate: typing.Optional[builtins.str] = None,
    default_ssl_client_private_key: typing.Optional[builtins.str] = None,
    default_timeout_penalty: typing.Optional[jsii.Number] = None,
    email_notification_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    end_user_mapping_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    group: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    load_feedback: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    load_imbalance_percentage: typing.Optional[jsii.Number] = None,
    wait_on_complete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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

def _typecheckingstub__1633cdfa0700f84058b0ec0c5190b71e01b249f2ab665602994c251cf59293dc(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__652166c94b6b8128cfe9606db386be6aa88b3ffbd1f5fabde3dc0f4eccbbf5c9(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d69953a390cf411cdb1abfc7478ae40a8c1c2b67caac2c59e93edcce434839c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9101de365f3b722a0e61a9d0a8bf364f7ee79b21a43a8c9be545469cc59818bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__198c0fc990b7504d29b1e0b7d401ad4bf9bd425492db202b4a85e46d86033f0d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d41a0aaa7a846db025045b8b0a48f455a1af62f94261e2ff2c4b001b612e8adb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__526f08786301f962350eb5858b6cf0769b4968b53aba0cd47aff56474993ba92(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__699c1ad3f73cc3b662574880f7a6aee2bc0a4384ad97371129d8899acad5654f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__469d38205424bd6afd09d938e78b8688948524dc09b00e13eb63752045e119a0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6e659121c3b67db3a3b2c5d44058e4800cd97bbac6620b4bbd47356484211a2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aeb59dc1229725495eff2b072f9a994fed48d2a5896c8f5083b11e86ed316e3e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd62e92e73f0c652384343c7b1739f454fc0439e9186c09028a70a767c9a4e9d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dae435d58b77563828d49edd53db2e9ea4810dbf0324fa731b1b72f9bb99ea4e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5e49ca1ef7328d96338969045bef348126904c11f84b6817a299980ca33647e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecb7afa9516f6e020db575cd2b439af8a60c2f23205478beefddefa21ab379bb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c754dfc7f6b494e8017d3a6a0c6a28487e427ab3a75bfb1bb81dcf19bcda3e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__321d4021a22e7ae47c314e51805494b11558677abb9f30e2ef297a4285418ec8(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b5e38fd63e5d022f60a03f47b2a19129ee899af45ce5ed573c55a02a0b6581e(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    type: builtins.str,
    cname_coalescing_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    comment: typing.Optional[builtins.str] = None,
    contract: typing.Optional[builtins.str] = None,
    default_error_penalty: typing.Optional[jsii.Number] = None,
    default_ssl_client_certificate: typing.Optional[builtins.str] = None,
    default_ssl_client_private_key: typing.Optional[builtins.str] = None,
    default_timeout_penalty: typing.Optional[jsii.Number] = None,
    email_notification_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    end_user_mapping_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    group: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    load_feedback: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    load_imbalance_percentage: typing.Optional[jsii.Number] = None,
    wait_on_complete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass
