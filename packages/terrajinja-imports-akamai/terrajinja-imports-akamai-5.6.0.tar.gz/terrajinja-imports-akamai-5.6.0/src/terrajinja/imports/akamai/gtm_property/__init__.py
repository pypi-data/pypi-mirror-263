'''
# `akamai_gtm_property`

Refer to the Terraform Registry for docs: [`akamai_gtm_property`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property).
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


class GtmProperty(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.gtmProperty.GtmProperty",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property akamai_gtm_property}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        domain: builtins.str,
        handout_limit: jsii.Number,
        handout_mode: builtins.str,
        name: builtins.str,
        score_aggregation_type: builtins.str,
        type: builtins.str,
        backup_cname: typing.Optional[builtins.str] = None,
        backup_ip: typing.Optional[builtins.str] = None,
        balance_by_download_score: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        cname: typing.Optional[builtins.str] = None,
        comments: typing.Optional[builtins.str] = None,
        dynamic_ttl: typing.Optional[jsii.Number] = None,
        failback_delay: typing.Optional[jsii.Number] = None,
        failover_delay: typing.Optional[jsii.Number] = None,
        ghost_demand_reporting: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        health_max: typing.Optional[jsii.Number] = None,
        health_multiplier: typing.Optional[jsii.Number] = None,
        health_threshold: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        ipv6: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        liveness_test: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GtmPropertyLivenessTest", typing.Dict[builtins.str, typing.Any]]]]] = None,
        load_imbalance_percentage: typing.Optional[jsii.Number] = None,
        map_name: typing.Optional[builtins.str] = None,
        max_unreachable_penalty: typing.Optional[jsii.Number] = None,
        min_live_fraction: typing.Optional[jsii.Number] = None,
        static_rr_set: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GtmPropertyStaticRrSet", typing.Dict[builtins.str, typing.Any]]]]] = None,
        static_ttl: typing.Optional[jsii.Number] = None,
        stickiness_bonus_constant: typing.Optional[jsii.Number] = None,
        stickiness_bonus_percentage: typing.Optional[jsii.Number] = None,
        traffic_target: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GtmPropertyTrafficTarget", typing.Dict[builtins.str, typing.Any]]]]] = None,
        unreachable_threshold: typing.Optional[jsii.Number] = None,
        use_computed_targets: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        wait_on_complete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property akamai_gtm_property} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param domain: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#domain GtmProperty#domain}.
        :param handout_limit: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#handout_limit GtmProperty#handout_limit}.
        :param handout_mode: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#handout_mode GtmProperty#handout_mode}.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#name GtmProperty#name}.
        :param score_aggregation_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#score_aggregation_type GtmProperty#score_aggregation_type}.
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#type GtmProperty#type}.
        :param backup_cname: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#backup_cname GtmProperty#backup_cname}.
        :param backup_ip: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#backup_ip GtmProperty#backup_ip}.
        :param balance_by_download_score: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#balance_by_download_score GtmProperty#balance_by_download_score}.
        :param cname: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#cname GtmProperty#cname}.
        :param comments: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#comments GtmProperty#comments}.
        :param dynamic_ttl: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#dynamic_ttl GtmProperty#dynamic_ttl}.
        :param failback_delay: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#failback_delay GtmProperty#failback_delay}.
        :param failover_delay: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#failover_delay GtmProperty#failover_delay}.
        :param ghost_demand_reporting: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#ghost_demand_reporting GtmProperty#ghost_demand_reporting}.
        :param health_max: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#health_max GtmProperty#health_max}.
        :param health_multiplier: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#health_multiplier GtmProperty#health_multiplier}.
        :param health_threshold: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#health_threshold GtmProperty#health_threshold}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#id GtmProperty#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ipv6: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#ipv6 GtmProperty#ipv6}.
        :param liveness_test: liveness_test block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#liveness_test GtmProperty#liveness_test}
        :param load_imbalance_percentage: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#load_imbalance_percentage GtmProperty#load_imbalance_percentage}.
        :param map_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#map_name GtmProperty#map_name}.
        :param max_unreachable_penalty: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#max_unreachable_penalty GtmProperty#max_unreachable_penalty}.
        :param min_live_fraction: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#min_live_fraction GtmProperty#min_live_fraction}.
        :param static_rr_set: static_rr_set block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#static_rr_set GtmProperty#static_rr_set}
        :param static_ttl: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#static_ttl GtmProperty#static_ttl}.
        :param stickiness_bonus_constant: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#stickiness_bonus_constant GtmProperty#stickiness_bonus_constant}.
        :param stickiness_bonus_percentage: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#stickiness_bonus_percentage GtmProperty#stickiness_bonus_percentage}.
        :param traffic_target: traffic_target block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#traffic_target GtmProperty#traffic_target}
        :param unreachable_threshold: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#unreachable_threshold GtmProperty#unreachable_threshold}.
        :param use_computed_targets: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#use_computed_targets GtmProperty#use_computed_targets}.
        :param wait_on_complete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#wait_on_complete GtmProperty#wait_on_complete}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b643d89ce032e7f4318c6e8a9a1e954c654e8778af5edfadfed7beb88a0f470d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GtmPropertyConfig(
            domain=domain,
            handout_limit=handout_limit,
            handout_mode=handout_mode,
            name=name,
            score_aggregation_type=score_aggregation_type,
            type=type,
            backup_cname=backup_cname,
            backup_ip=backup_ip,
            balance_by_download_score=balance_by_download_score,
            cname=cname,
            comments=comments,
            dynamic_ttl=dynamic_ttl,
            failback_delay=failback_delay,
            failover_delay=failover_delay,
            ghost_demand_reporting=ghost_demand_reporting,
            health_max=health_max,
            health_multiplier=health_multiplier,
            health_threshold=health_threshold,
            id=id,
            ipv6=ipv6,
            liveness_test=liveness_test,
            load_imbalance_percentage=load_imbalance_percentage,
            map_name=map_name,
            max_unreachable_penalty=max_unreachable_penalty,
            min_live_fraction=min_live_fraction,
            static_rr_set=static_rr_set,
            static_ttl=static_ttl,
            stickiness_bonus_constant=stickiness_bonus_constant,
            stickiness_bonus_percentage=stickiness_bonus_percentage,
            traffic_target=traffic_target,
            unreachable_threshold=unreachable_threshold,
            use_computed_targets=use_computed_targets,
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
        '''Generates CDKTF code for importing a GtmProperty resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the GtmProperty to import.
        :param import_from_id: The id of the existing GtmProperty that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the GtmProperty to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bea20c66b55ec00b31d88ed3b52980d468db29c084435dadd3546ad535f774e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putLivenessTest")
    def put_liveness_test(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GtmPropertyLivenessTest", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99310899b2cb014f0d736ba45d897ba30c46efae6b69a4e3e76269cbb0629460)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLivenessTest", [value]))

    @jsii.member(jsii_name="putStaticRrSet")
    def put_static_rr_set(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GtmPropertyStaticRrSet", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9bbc148c0ed52d87d0036fb933e513dc23230a066204cdf08a5e266fcf653a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStaticRrSet", [value]))

    @jsii.member(jsii_name="putTrafficTarget")
    def put_traffic_target(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GtmPropertyTrafficTarget", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac10351d66927524a557f68101973011083133ba00cc0c87dea7cbecad75a33d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTrafficTarget", [value]))

    @jsii.member(jsii_name="resetBackupCname")
    def reset_backup_cname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupCname", []))

    @jsii.member(jsii_name="resetBackupIp")
    def reset_backup_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupIp", []))

    @jsii.member(jsii_name="resetBalanceByDownloadScore")
    def reset_balance_by_download_score(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBalanceByDownloadScore", []))

    @jsii.member(jsii_name="resetCname")
    def reset_cname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCname", []))

    @jsii.member(jsii_name="resetComments")
    def reset_comments(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComments", []))

    @jsii.member(jsii_name="resetDynamicTtl")
    def reset_dynamic_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDynamicTtl", []))

    @jsii.member(jsii_name="resetFailbackDelay")
    def reset_failback_delay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailbackDelay", []))

    @jsii.member(jsii_name="resetFailoverDelay")
    def reset_failover_delay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailoverDelay", []))

    @jsii.member(jsii_name="resetGhostDemandReporting")
    def reset_ghost_demand_reporting(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGhostDemandReporting", []))

    @jsii.member(jsii_name="resetHealthMax")
    def reset_health_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthMax", []))

    @jsii.member(jsii_name="resetHealthMultiplier")
    def reset_health_multiplier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthMultiplier", []))

    @jsii.member(jsii_name="resetHealthThreshold")
    def reset_health_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthThreshold", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIpv6")
    def reset_ipv6(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv6", []))

    @jsii.member(jsii_name="resetLivenessTest")
    def reset_liveness_test(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLivenessTest", []))

    @jsii.member(jsii_name="resetLoadImbalancePercentage")
    def reset_load_imbalance_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadImbalancePercentage", []))

    @jsii.member(jsii_name="resetMapName")
    def reset_map_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMapName", []))

    @jsii.member(jsii_name="resetMaxUnreachablePenalty")
    def reset_max_unreachable_penalty(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxUnreachablePenalty", []))

    @jsii.member(jsii_name="resetMinLiveFraction")
    def reset_min_live_fraction(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinLiveFraction", []))

    @jsii.member(jsii_name="resetStaticRrSet")
    def reset_static_rr_set(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStaticRrSet", []))

    @jsii.member(jsii_name="resetStaticTtl")
    def reset_static_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStaticTtl", []))

    @jsii.member(jsii_name="resetStickinessBonusConstant")
    def reset_stickiness_bonus_constant(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStickinessBonusConstant", []))

    @jsii.member(jsii_name="resetStickinessBonusPercentage")
    def reset_stickiness_bonus_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStickinessBonusPercentage", []))

    @jsii.member(jsii_name="resetTrafficTarget")
    def reset_traffic_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrafficTarget", []))

    @jsii.member(jsii_name="resetUnreachableThreshold")
    def reset_unreachable_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnreachableThreshold", []))

    @jsii.member(jsii_name="resetUseComputedTargets")
    def reset_use_computed_targets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseComputedTargets", []))

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
    @jsii.member(jsii_name="livenessTest")
    def liveness_test(self) -> "GtmPropertyLivenessTestList":
        return typing.cast("GtmPropertyLivenessTestList", jsii.get(self, "livenessTest"))

    @builtins.property
    @jsii.member(jsii_name="staticRrSet")
    def static_rr_set(self) -> "GtmPropertyStaticRrSetList":
        return typing.cast("GtmPropertyStaticRrSetList", jsii.get(self, "staticRrSet"))

    @builtins.property
    @jsii.member(jsii_name="trafficTarget")
    def traffic_target(self) -> "GtmPropertyTrafficTargetList":
        return typing.cast("GtmPropertyTrafficTargetList", jsii.get(self, "trafficTarget"))

    @builtins.property
    @jsii.member(jsii_name="weightedHashBitsForIpv4")
    def weighted_hash_bits_for_ipv4(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weightedHashBitsForIpv4"))

    @builtins.property
    @jsii.member(jsii_name="weightedHashBitsForIpv6")
    def weighted_hash_bits_for_ipv6(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weightedHashBitsForIpv6"))

    @builtins.property
    @jsii.member(jsii_name="backupCnameInput")
    def backup_cname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backupCnameInput"))

    @builtins.property
    @jsii.member(jsii_name="backupIpInput")
    def backup_ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backupIpInput"))

    @builtins.property
    @jsii.member(jsii_name="balanceByDownloadScoreInput")
    def balance_by_download_score_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "balanceByDownloadScoreInput"))

    @builtins.property
    @jsii.member(jsii_name="cnameInput")
    def cname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cnameInput"))

    @builtins.property
    @jsii.member(jsii_name="commentsInput")
    def comments_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentsInput"))

    @builtins.property
    @jsii.member(jsii_name="domainInput")
    def domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainInput"))

    @builtins.property
    @jsii.member(jsii_name="dynamicTtlInput")
    def dynamic_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dynamicTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="failbackDelayInput")
    def failback_delay_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "failbackDelayInput"))

    @builtins.property
    @jsii.member(jsii_name="failoverDelayInput")
    def failover_delay_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "failoverDelayInput"))

    @builtins.property
    @jsii.member(jsii_name="ghostDemandReportingInput")
    def ghost_demand_reporting_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "ghostDemandReportingInput"))

    @builtins.property
    @jsii.member(jsii_name="handoutLimitInput")
    def handout_limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "handoutLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="handoutModeInput")
    def handout_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "handoutModeInput"))

    @builtins.property
    @jsii.member(jsii_name="healthMaxInput")
    def health_max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "healthMaxInput"))

    @builtins.property
    @jsii.member(jsii_name="healthMultiplierInput")
    def health_multiplier_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "healthMultiplierInput"))

    @builtins.property
    @jsii.member(jsii_name="healthThresholdInput")
    def health_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "healthThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv6Input")
    def ipv6_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "ipv6Input"))

    @builtins.property
    @jsii.member(jsii_name="livenessTestInput")
    def liveness_test_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GtmPropertyLivenessTest"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GtmPropertyLivenessTest"]]], jsii.get(self, "livenessTestInput"))

    @builtins.property
    @jsii.member(jsii_name="loadImbalancePercentageInput")
    def load_imbalance_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "loadImbalancePercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="mapNameInput")
    def map_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mapNameInput"))

    @builtins.property
    @jsii.member(jsii_name="maxUnreachablePenaltyInput")
    def max_unreachable_penalty_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxUnreachablePenaltyInput"))

    @builtins.property
    @jsii.member(jsii_name="minLiveFractionInput")
    def min_live_fraction_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minLiveFractionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="scoreAggregationTypeInput")
    def score_aggregation_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scoreAggregationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="staticRrSetInput")
    def static_rr_set_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GtmPropertyStaticRrSet"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GtmPropertyStaticRrSet"]]], jsii.get(self, "staticRrSetInput"))

    @builtins.property
    @jsii.member(jsii_name="staticTtlInput")
    def static_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "staticTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="stickinessBonusConstantInput")
    def stickiness_bonus_constant_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "stickinessBonusConstantInput"))

    @builtins.property
    @jsii.member(jsii_name="stickinessBonusPercentageInput")
    def stickiness_bonus_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "stickinessBonusPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="trafficTargetInput")
    def traffic_target_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GtmPropertyTrafficTarget"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GtmPropertyTrafficTarget"]]], jsii.get(self, "trafficTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="unreachableThresholdInput")
    def unreachable_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "unreachableThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="useComputedTargetsInput")
    def use_computed_targets_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "useComputedTargetsInput"))

    @builtins.property
    @jsii.member(jsii_name="waitOnCompleteInput")
    def wait_on_complete_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "waitOnCompleteInput"))

    @builtins.property
    @jsii.member(jsii_name="backupCname")
    def backup_cname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backupCname"))

    @backup_cname.setter
    def backup_cname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f10f255084ef040f2591521ca6f292f9680b2d69dae8df8893ffae2ed7410edc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupCname", value)

    @builtins.property
    @jsii.member(jsii_name="backupIp")
    def backup_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backupIp"))

    @backup_ip.setter
    def backup_ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9f2ff883dd90427730c50a52ded511f2d7f1b0360794d94a36c53bf8e3e1fb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupIp", value)

    @builtins.property
    @jsii.member(jsii_name="balanceByDownloadScore")
    def balance_by_download_score(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "balanceByDownloadScore"))

    @balance_by_download_score.setter
    def balance_by_download_score(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25a7ac189be8fd790e35a9c92a77b0406c89217d80cee10ea0a8cf0f22c3586d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "balanceByDownloadScore", value)

    @builtins.property
    @jsii.member(jsii_name="cname")
    def cname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cname"))

    @cname.setter
    def cname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7951255fc3a92d63e7ef3809a8c119cf513a2d2ed33a20931a9a8b6289e3ad5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cname", value)

    @builtins.property
    @jsii.member(jsii_name="comments")
    def comments(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comments"))

    @comments.setter
    def comments(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5cfeb377033c2543ef974153e64db0bc70d494ea843d3dd13cab03f619db3720)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comments", value)

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81874216486e0f0571a1c75f70acf04202f591d0196a6d51fcca92acbf1b18e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)

    @builtins.property
    @jsii.member(jsii_name="dynamicTtl")
    def dynamic_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dynamicTtl"))

    @dynamic_ttl.setter
    def dynamic_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00b7f07ca5520fdd582eb9fc264c469bc36d8d430e5e1e5dbb005388972a170b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dynamicTtl", value)

    @builtins.property
    @jsii.member(jsii_name="failbackDelay")
    def failback_delay(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "failbackDelay"))

    @failback_delay.setter
    def failback_delay(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5db5b1aaa8becd3df7e74fab881dee5714b06e7685cbe9b206cdd085f06f4be8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failbackDelay", value)

    @builtins.property
    @jsii.member(jsii_name="failoverDelay")
    def failover_delay(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "failoverDelay"))

    @failover_delay.setter
    def failover_delay(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__665d3fdfc9dc493bc63edcac3c419c15360b4acc68a7efe2f5a6451621d047c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failoverDelay", value)

    @builtins.property
    @jsii.member(jsii_name="ghostDemandReporting")
    def ghost_demand_reporting(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "ghostDemandReporting"))

    @ghost_demand_reporting.setter
    def ghost_demand_reporting(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bde30a917cb99eef3c70ec8bdc7da7b570bdcee6bb53d351f733fdbf7e7bb1d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ghostDemandReporting", value)

    @builtins.property
    @jsii.member(jsii_name="handoutLimit")
    def handout_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "handoutLimit"))

    @handout_limit.setter
    def handout_limit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75f6dfd981971d995deac7e992b63c7e524cb686195a41fc19bacbe51056e180)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "handoutLimit", value)

    @builtins.property
    @jsii.member(jsii_name="handoutMode")
    def handout_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "handoutMode"))

    @handout_mode.setter
    def handout_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02f4ed340d84a40548a27d2800b476466d8879783650908b526f85180f0da86d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "handoutMode", value)

    @builtins.property
    @jsii.member(jsii_name="healthMax")
    def health_max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "healthMax"))

    @health_max.setter
    def health_max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fe528ff281e256ff566fababbcef8991792ff0511d9ba958afc0aa1721008c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthMax", value)

    @builtins.property
    @jsii.member(jsii_name="healthMultiplier")
    def health_multiplier(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "healthMultiplier"))

    @health_multiplier.setter
    def health_multiplier(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50456c7b86074ce67a7765bd1b04fadb749f8f8e67720253972bd475c3ad164e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthMultiplier", value)

    @builtins.property
    @jsii.member(jsii_name="healthThreshold")
    def health_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "healthThreshold"))

    @health_threshold.setter
    def health_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f5bdf7ab8dc5512538d887cd7cfff5cd9075bb189e1f8bb28c38989890a73c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01c8607b960fea7846d5b88bc6313f74cd155ea6687fdf85f9412ed5e07c7a1f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ipv6")
    def ipv6(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "ipv6"))

    @ipv6.setter
    def ipv6(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c22a9799a40278cf8275b2535aa29ef65e1e7f68a9ef18da6d84e1f42060eea4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv6", value)

    @builtins.property
    @jsii.member(jsii_name="loadImbalancePercentage")
    def load_imbalance_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "loadImbalancePercentage"))

    @load_imbalance_percentage.setter
    def load_imbalance_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__707cf77fe47cab98c4dd9a65a6c19d070f58ca486c3d15a1c06b517ff6b95f0f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadImbalancePercentage", value)

    @builtins.property
    @jsii.member(jsii_name="mapName")
    def map_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mapName"))

    @map_name.setter
    def map_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6809629e030216c2045306ce7565be661aeb0747a0d39612441bed106a966b7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mapName", value)

    @builtins.property
    @jsii.member(jsii_name="maxUnreachablePenalty")
    def max_unreachable_penalty(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxUnreachablePenalty"))

    @max_unreachable_penalty.setter
    def max_unreachable_penalty(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05f06b54ebc166b42e0d6ace8c063b390aa34c7580cb8624700b568e8b84c963)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxUnreachablePenalty", value)

    @builtins.property
    @jsii.member(jsii_name="minLiveFraction")
    def min_live_fraction(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minLiveFraction"))

    @min_live_fraction.setter
    def min_live_fraction(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__831cade067ac64a29f3fd9cb4381378dd8ac21e563a3223f9f4feb8b677ccff2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minLiveFraction", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70ec45ac70f82f8bbf2293e33accb2b97b8d4eae83ba1c4c75db573264ed4fd9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="scoreAggregationType")
    def score_aggregation_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scoreAggregationType"))

    @score_aggregation_type.setter
    def score_aggregation_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fea78e110232f5281e81edb2af1ce916c8a44c5fafa9116482dce05bec19e1a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scoreAggregationType", value)

    @builtins.property
    @jsii.member(jsii_name="staticTtl")
    def static_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "staticTtl"))

    @static_ttl.setter
    def static_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2348067efe4b66ce6952f873f6e5d853b2358bdd36ed697ab82d7adc9e8e81aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "staticTtl", value)

    @builtins.property
    @jsii.member(jsii_name="stickinessBonusConstant")
    def stickiness_bonus_constant(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "stickinessBonusConstant"))

    @stickiness_bonus_constant.setter
    def stickiness_bonus_constant(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc91363a70a649321ae63164b0753123c3e65cf43af58bb59ea8aab20d67b254)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stickinessBonusConstant", value)

    @builtins.property
    @jsii.member(jsii_name="stickinessBonusPercentage")
    def stickiness_bonus_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "stickinessBonusPercentage"))

    @stickiness_bonus_percentage.setter
    def stickiness_bonus_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b055c56ae0ad6bdc46f660787da92183d0eff8ea81e61e7132c2e91f2563498)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stickinessBonusPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__114e6f319f3bacc6641c244bee89cdd1e2fd1385b9cc4ce8fc59b4f59d424c4b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="unreachableThreshold")
    def unreachable_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "unreachableThreshold"))

    @unreachable_threshold.setter
    def unreachable_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f571cc6902c4f0a36f2fc0ed4307cb6fba92e5180a1c0377e479ad6927592204)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unreachableThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="useComputedTargets")
    def use_computed_targets(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "useComputedTargets"))

    @use_computed_targets.setter
    def use_computed_targets(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04663718af1001fe96404b8ec913be5d9fe3f97200d63bdc991df0136f174c00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useComputedTargets", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__ef0ccb24781c9d548e3b337d6ff6f8727f2958511aee934e542292e3dc3a8f66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitOnComplete", value)


@jsii.data_type(
    jsii_type="akamai.gtmProperty.GtmPropertyConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "domain": "domain",
        "handout_limit": "handoutLimit",
        "handout_mode": "handoutMode",
        "name": "name",
        "score_aggregation_type": "scoreAggregationType",
        "type": "type",
        "backup_cname": "backupCname",
        "backup_ip": "backupIp",
        "balance_by_download_score": "balanceByDownloadScore",
        "cname": "cname",
        "comments": "comments",
        "dynamic_ttl": "dynamicTtl",
        "failback_delay": "failbackDelay",
        "failover_delay": "failoverDelay",
        "ghost_demand_reporting": "ghostDemandReporting",
        "health_max": "healthMax",
        "health_multiplier": "healthMultiplier",
        "health_threshold": "healthThreshold",
        "id": "id",
        "ipv6": "ipv6",
        "liveness_test": "livenessTest",
        "load_imbalance_percentage": "loadImbalancePercentage",
        "map_name": "mapName",
        "max_unreachable_penalty": "maxUnreachablePenalty",
        "min_live_fraction": "minLiveFraction",
        "static_rr_set": "staticRrSet",
        "static_ttl": "staticTtl",
        "stickiness_bonus_constant": "stickinessBonusConstant",
        "stickiness_bonus_percentage": "stickinessBonusPercentage",
        "traffic_target": "trafficTarget",
        "unreachable_threshold": "unreachableThreshold",
        "use_computed_targets": "useComputedTargets",
        "wait_on_complete": "waitOnComplete",
    },
)
class GtmPropertyConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        domain: builtins.str,
        handout_limit: jsii.Number,
        handout_mode: builtins.str,
        name: builtins.str,
        score_aggregation_type: builtins.str,
        type: builtins.str,
        backup_cname: typing.Optional[builtins.str] = None,
        backup_ip: typing.Optional[builtins.str] = None,
        balance_by_download_score: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        cname: typing.Optional[builtins.str] = None,
        comments: typing.Optional[builtins.str] = None,
        dynamic_ttl: typing.Optional[jsii.Number] = None,
        failback_delay: typing.Optional[jsii.Number] = None,
        failover_delay: typing.Optional[jsii.Number] = None,
        ghost_demand_reporting: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        health_max: typing.Optional[jsii.Number] = None,
        health_multiplier: typing.Optional[jsii.Number] = None,
        health_threshold: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        ipv6: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        liveness_test: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GtmPropertyLivenessTest", typing.Dict[builtins.str, typing.Any]]]]] = None,
        load_imbalance_percentage: typing.Optional[jsii.Number] = None,
        map_name: typing.Optional[builtins.str] = None,
        max_unreachable_penalty: typing.Optional[jsii.Number] = None,
        min_live_fraction: typing.Optional[jsii.Number] = None,
        static_rr_set: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GtmPropertyStaticRrSet", typing.Dict[builtins.str, typing.Any]]]]] = None,
        static_ttl: typing.Optional[jsii.Number] = None,
        stickiness_bonus_constant: typing.Optional[jsii.Number] = None,
        stickiness_bonus_percentage: typing.Optional[jsii.Number] = None,
        traffic_target: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GtmPropertyTrafficTarget", typing.Dict[builtins.str, typing.Any]]]]] = None,
        unreachable_threshold: typing.Optional[jsii.Number] = None,
        use_computed_targets: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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
        :param domain: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#domain GtmProperty#domain}.
        :param handout_limit: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#handout_limit GtmProperty#handout_limit}.
        :param handout_mode: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#handout_mode GtmProperty#handout_mode}.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#name GtmProperty#name}.
        :param score_aggregation_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#score_aggregation_type GtmProperty#score_aggregation_type}.
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#type GtmProperty#type}.
        :param backup_cname: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#backup_cname GtmProperty#backup_cname}.
        :param backup_ip: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#backup_ip GtmProperty#backup_ip}.
        :param balance_by_download_score: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#balance_by_download_score GtmProperty#balance_by_download_score}.
        :param cname: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#cname GtmProperty#cname}.
        :param comments: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#comments GtmProperty#comments}.
        :param dynamic_ttl: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#dynamic_ttl GtmProperty#dynamic_ttl}.
        :param failback_delay: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#failback_delay GtmProperty#failback_delay}.
        :param failover_delay: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#failover_delay GtmProperty#failover_delay}.
        :param ghost_demand_reporting: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#ghost_demand_reporting GtmProperty#ghost_demand_reporting}.
        :param health_max: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#health_max GtmProperty#health_max}.
        :param health_multiplier: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#health_multiplier GtmProperty#health_multiplier}.
        :param health_threshold: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#health_threshold GtmProperty#health_threshold}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#id GtmProperty#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ipv6: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#ipv6 GtmProperty#ipv6}.
        :param liveness_test: liveness_test block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#liveness_test GtmProperty#liveness_test}
        :param load_imbalance_percentage: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#load_imbalance_percentage GtmProperty#load_imbalance_percentage}.
        :param map_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#map_name GtmProperty#map_name}.
        :param max_unreachable_penalty: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#max_unreachable_penalty GtmProperty#max_unreachable_penalty}.
        :param min_live_fraction: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#min_live_fraction GtmProperty#min_live_fraction}.
        :param static_rr_set: static_rr_set block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#static_rr_set GtmProperty#static_rr_set}
        :param static_ttl: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#static_ttl GtmProperty#static_ttl}.
        :param stickiness_bonus_constant: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#stickiness_bonus_constant GtmProperty#stickiness_bonus_constant}.
        :param stickiness_bonus_percentage: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#stickiness_bonus_percentage GtmProperty#stickiness_bonus_percentage}.
        :param traffic_target: traffic_target block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#traffic_target GtmProperty#traffic_target}
        :param unreachable_threshold: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#unreachable_threshold GtmProperty#unreachable_threshold}.
        :param use_computed_targets: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#use_computed_targets GtmProperty#use_computed_targets}.
        :param wait_on_complete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#wait_on_complete GtmProperty#wait_on_complete}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcfb710470d47a2163bd8c268679fa46a16587c132f9d355094424efe943d017)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            check_type(argname="argument handout_limit", value=handout_limit, expected_type=type_hints["handout_limit"])
            check_type(argname="argument handout_mode", value=handout_mode, expected_type=type_hints["handout_mode"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument score_aggregation_type", value=score_aggregation_type, expected_type=type_hints["score_aggregation_type"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument backup_cname", value=backup_cname, expected_type=type_hints["backup_cname"])
            check_type(argname="argument backup_ip", value=backup_ip, expected_type=type_hints["backup_ip"])
            check_type(argname="argument balance_by_download_score", value=balance_by_download_score, expected_type=type_hints["balance_by_download_score"])
            check_type(argname="argument cname", value=cname, expected_type=type_hints["cname"])
            check_type(argname="argument comments", value=comments, expected_type=type_hints["comments"])
            check_type(argname="argument dynamic_ttl", value=dynamic_ttl, expected_type=type_hints["dynamic_ttl"])
            check_type(argname="argument failback_delay", value=failback_delay, expected_type=type_hints["failback_delay"])
            check_type(argname="argument failover_delay", value=failover_delay, expected_type=type_hints["failover_delay"])
            check_type(argname="argument ghost_demand_reporting", value=ghost_demand_reporting, expected_type=type_hints["ghost_demand_reporting"])
            check_type(argname="argument health_max", value=health_max, expected_type=type_hints["health_max"])
            check_type(argname="argument health_multiplier", value=health_multiplier, expected_type=type_hints["health_multiplier"])
            check_type(argname="argument health_threshold", value=health_threshold, expected_type=type_hints["health_threshold"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ipv6", value=ipv6, expected_type=type_hints["ipv6"])
            check_type(argname="argument liveness_test", value=liveness_test, expected_type=type_hints["liveness_test"])
            check_type(argname="argument load_imbalance_percentage", value=load_imbalance_percentage, expected_type=type_hints["load_imbalance_percentage"])
            check_type(argname="argument map_name", value=map_name, expected_type=type_hints["map_name"])
            check_type(argname="argument max_unreachable_penalty", value=max_unreachable_penalty, expected_type=type_hints["max_unreachable_penalty"])
            check_type(argname="argument min_live_fraction", value=min_live_fraction, expected_type=type_hints["min_live_fraction"])
            check_type(argname="argument static_rr_set", value=static_rr_set, expected_type=type_hints["static_rr_set"])
            check_type(argname="argument static_ttl", value=static_ttl, expected_type=type_hints["static_ttl"])
            check_type(argname="argument stickiness_bonus_constant", value=stickiness_bonus_constant, expected_type=type_hints["stickiness_bonus_constant"])
            check_type(argname="argument stickiness_bonus_percentage", value=stickiness_bonus_percentage, expected_type=type_hints["stickiness_bonus_percentage"])
            check_type(argname="argument traffic_target", value=traffic_target, expected_type=type_hints["traffic_target"])
            check_type(argname="argument unreachable_threshold", value=unreachable_threshold, expected_type=type_hints["unreachable_threshold"])
            check_type(argname="argument use_computed_targets", value=use_computed_targets, expected_type=type_hints["use_computed_targets"])
            check_type(argname="argument wait_on_complete", value=wait_on_complete, expected_type=type_hints["wait_on_complete"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain": domain,
            "handout_limit": handout_limit,
            "handout_mode": handout_mode,
            "name": name,
            "score_aggregation_type": score_aggregation_type,
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
        if backup_cname is not None:
            self._values["backup_cname"] = backup_cname
        if backup_ip is not None:
            self._values["backup_ip"] = backup_ip
        if balance_by_download_score is not None:
            self._values["balance_by_download_score"] = balance_by_download_score
        if cname is not None:
            self._values["cname"] = cname
        if comments is not None:
            self._values["comments"] = comments
        if dynamic_ttl is not None:
            self._values["dynamic_ttl"] = dynamic_ttl
        if failback_delay is not None:
            self._values["failback_delay"] = failback_delay
        if failover_delay is not None:
            self._values["failover_delay"] = failover_delay
        if ghost_demand_reporting is not None:
            self._values["ghost_demand_reporting"] = ghost_demand_reporting
        if health_max is not None:
            self._values["health_max"] = health_max
        if health_multiplier is not None:
            self._values["health_multiplier"] = health_multiplier
        if health_threshold is not None:
            self._values["health_threshold"] = health_threshold
        if id is not None:
            self._values["id"] = id
        if ipv6 is not None:
            self._values["ipv6"] = ipv6
        if liveness_test is not None:
            self._values["liveness_test"] = liveness_test
        if load_imbalance_percentage is not None:
            self._values["load_imbalance_percentage"] = load_imbalance_percentage
        if map_name is not None:
            self._values["map_name"] = map_name
        if max_unreachable_penalty is not None:
            self._values["max_unreachable_penalty"] = max_unreachable_penalty
        if min_live_fraction is not None:
            self._values["min_live_fraction"] = min_live_fraction
        if static_rr_set is not None:
            self._values["static_rr_set"] = static_rr_set
        if static_ttl is not None:
            self._values["static_ttl"] = static_ttl
        if stickiness_bonus_constant is not None:
            self._values["stickiness_bonus_constant"] = stickiness_bonus_constant
        if stickiness_bonus_percentage is not None:
            self._values["stickiness_bonus_percentage"] = stickiness_bonus_percentage
        if traffic_target is not None:
            self._values["traffic_target"] = traffic_target
        if unreachable_threshold is not None:
            self._values["unreachable_threshold"] = unreachable_threshold
        if use_computed_targets is not None:
            self._values["use_computed_targets"] = use_computed_targets
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
    def domain(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#domain GtmProperty#domain}.'''
        result = self._values.get("domain")
        assert result is not None, "Required property 'domain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def handout_limit(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#handout_limit GtmProperty#handout_limit}.'''
        result = self._values.get("handout_limit")
        assert result is not None, "Required property 'handout_limit' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def handout_mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#handout_mode GtmProperty#handout_mode}.'''
        result = self._values.get("handout_mode")
        assert result is not None, "Required property 'handout_mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#name GtmProperty#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def score_aggregation_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#score_aggregation_type GtmProperty#score_aggregation_type}.'''
        result = self._values.get("score_aggregation_type")
        assert result is not None, "Required property 'score_aggregation_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#type GtmProperty#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def backup_cname(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#backup_cname GtmProperty#backup_cname}.'''
        result = self._values.get("backup_cname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def backup_ip(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#backup_ip GtmProperty#backup_ip}.'''
        result = self._values.get("backup_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def balance_by_download_score(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#balance_by_download_score GtmProperty#balance_by_download_score}.'''
        result = self._values.get("balance_by_download_score")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def cname(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#cname GtmProperty#cname}.'''
        result = self._values.get("cname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def comments(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#comments GtmProperty#comments}.'''
        result = self._values.get("comments")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dynamic_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#dynamic_ttl GtmProperty#dynamic_ttl}.'''
        result = self._values.get("dynamic_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def failback_delay(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#failback_delay GtmProperty#failback_delay}.'''
        result = self._values.get("failback_delay")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def failover_delay(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#failover_delay GtmProperty#failover_delay}.'''
        result = self._values.get("failover_delay")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ghost_demand_reporting(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#ghost_demand_reporting GtmProperty#ghost_demand_reporting}.'''
        result = self._values.get("ghost_demand_reporting")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def health_max(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#health_max GtmProperty#health_max}.'''
        result = self._values.get("health_max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def health_multiplier(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#health_multiplier GtmProperty#health_multiplier}.'''
        result = self._values.get("health_multiplier")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def health_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#health_threshold GtmProperty#health_threshold}.'''
        result = self._values.get("health_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#id GtmProperty#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ipv6(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#ipv6 GtmProperty#ipv6}.'''
        result = self._values.get("ipv6")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def liveness_test(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GtmPropertyLivenessTest"]]]:
        '''liveness_test block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#liveness_test GtmProperty#liveness_test}
        '''
        result = self._values.get("liveness_test")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GtmPropertyLivenessTest"]]], result)

    @builtins.property
    def load_imbalance_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#load_imbalance_percentage GtmProperty#load_imbalance_percentage}.'''
        result = self._values.get("load_imbalance_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def map_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#map_name GtmProperty#map_name}.'''
        result = self._values.get("map_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_unreachable_penalty(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#max_unreachable_penalty GtmProperty#max_unreachable_penalty}.'''
        result = self._values.get("max_unreachable_penalty")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_live_fraction(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#min_live_fraction GtmProperty#min_live_fraction}.'''
        result = self._values.get("min_live_fraction")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def static_rr_set(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GtmPropertyStaticRrSet"]]]:
        '''static_rr_set block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#static_rr_set GtmProperty#static_rr_set}
        '''
        result = self._values.get("static_rr_set")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GtmPropertyStaticRrSet"]]], result)

    @builtins.property
    def static_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#static_ttl GtmProperty#static_ttl}.'''
        result = self._values.get("static_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def stickiness_bonus_constant(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#stickiness_bonus_constant GtmProperty#stickiness_bonus_constant}.'''
        result = self._values.get("stickiness_bonus_constant")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def stickiness_bonus_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#stickiness_bonus_percentage GtmProperty#stickiness_bonus_percentage}.'''
        result = self._values.get("stickiness_bonus_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def traffic_target(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GtmPropertyTrafficTarget"]]]:
        '''traffic_target block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#traffic_target GtmProperty#traffic_target}
        '''
        result = self._values.get("traffic_target")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GtmPropertyTrafficTarget"]]], result)

    @builtins.property
    def unreachable_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#unreachable_threshold GtmProperty#unreachable_threshold}.'''
        result = self._values.get("unreachable_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def use_computed_targets(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#use_computed_targets GtmProperty#use_computed_targets}.'''
        result = self._values.get("use_computed_targets")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def wait_on_complete(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#wait_on_complete GtmProperty#wait_on_complete}.'''
        result = self._values.get("wait_on_complete")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GtmPropertyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.gtmProperty.GtmPropertyLivenessTest",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "test_interval": "testInterval",
        "test_object_protocol": "testObjectProtocol",
        "test_timeout": "testTimeout",
        "answers_required": "answersRequired",
        "disabled": "disabled",
        "disable_nonstandard_port_warning": "disableNonstandardPortWarning",
        "error_penalty": "errorPenalty",
        "http_error3_xx": "httpError3Xx",
        "http_error4_xx": "httpError4Xx",
        "http_error5_xx": "httpError5Xx",
        "http_header": "httpHeader",
        "peer_certificate_verification": "peerCertificateVerification",
        "recursion_requested": "recursionRequested",
        "request_string": "requestString",
        "resource_type": "resourceType",
        "response_string": "responseString",
        "ssl_client_certificate": "sslClientCertificate",
        "ssl_client_private_key": "sslClientPrivateKey",
        "test_object": "testObject",
        "test_object_password": "testObjectPassword",
        "test_object_port": "testObjectPort",
        "test_object_username": "testObjectUsername",
        "timeout_penalty": "timeoutPenalty",
    },
)
class GtmPropertyLivenessTest:
    def __init__(
        self,
        *,
        name: builtins.str,
        test_interval: jsii.Number,
        test_object_protocol: builtins.str,
        test_timeout: jsii.Number,
        answers_required: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        disable_nonstandard_port_warning: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        error_penalty: typing.Optional[jsii.Number] = None,
        http_error3_xx: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        http_error4_xx: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        http_error5_xx: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        http_header: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GtmPropertyLivenessTestHttpHeader", typing.Dict[builtins.str, typing.Any]]]]] = None,
        peer_certificate_verification: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        recursion_requested: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        request_string: typing.Optional[builtins.str] = None,
        resource_type: typing.Optional[builtins.str] = None,
        response_string: typing.Optional[builtins.str] = None,
        ssl_client_certificate: typing.Optional[builtins.str] = None,
        ssl_client_private_key: typing.Optional[builtins.str] = None,
        test_object: typing.Optional[builtins.str] = None,
        test_object_password: typing.Optional[builtins.str] = None,
        test_object_port: typing.Optional[jsii.Number] = None,
        test_object_username: typing.Optional[builtins.str] = None,
        timeout_penalty: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#name GtmProperty#name}.
        :param test_interval: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#test_interval GtmProperty#test_interval}.
        :param test_object_protocol: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#test_object_protocol GtmProperty#test_object_protocol}.
        :param test_timeout: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#test_timeout GtmProperty#test_timeout}.
        :param answers_required: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#answers_required GtmProperty#answers_required}.
        :param disabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#disabled GtmProperty#disabled}.
        :param disable_nonstandard_port_warning: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#disable_nonstandard_port_warning GtmProperty#disable_nonstandard_port_warning}.
        :param error_penalty: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#error_penalty GtmProperty#error_penalty}.
        :param http_error3_xx: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#http_error3xx GtmProperty#http_error3xx}.
        :param http_error4_xx: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#http_error4xx GtmProperty#http_error4xx}.
        :param http_error5_xx: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#http_error5xx GtmProperty#http_error5xx}.
        :param http_header: http_header block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#http_header GtmProperty#http_header}
        :param peer_certificate_verification: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#peer_certificate_verification GtmProperty#peer_certificate_verification}.
        :param recursion_requested: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#recursion_requested GtmProperty#recursion_requested}.
        :param request_string: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#request_string GtmProperty#request_string}.
        :param resource_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#resource_type GtmProperty#resource_type}.
        :param response_string: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#response_string GtmProperty#response_string}.
        :param ssl_client_certificate: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#ssl_client_certificate GtmProperty#ssl_client_certificate}.
        :param ssl_client_private_key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#ssl_client_private_key GtmProperty#ssl_client_private_key}.
        :param test_object: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#test_object GtmProperty#test_object}.
        :param test_object_password: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#test_object_password GtmProperty#test_object_password}.
        :param test_object_port: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#test_object_port GtmProperty#test_object_port}.
        :param test_object_username: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#test_object_username GtmProperty#test_object_username}.
        :param timeout_penalty: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#timeout_penalty GtmProperty#timeout_penalty}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e50d1387d34384167da4d9096bd77af2bc19561f3764335768293dce8272443c)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument test_interval", value=test_interval, expected_type=type_hints["test_interval"])
            check_type(argname="argument test_object_protocol", value=test_object_protocol, expected_type=type_hints["test_object_protocol"])
            check_type(argname="argument test_timeout", value=test_timeout, expected_type=type_hints["test_timeout"])
            check_type(argname="argument answers_required", value=answers_required, expected_type=type_hints["answers_required"])
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
            check_type(argname="argument disable_nonstandard_port_warning", value=disable_nonstandard_port_warning, expected_type=type_hints["disable_nonstandard_port_warning"])
            check_type(argname="argument error_penalty", value=error_penalty, expected_type=type_hints["error_penalty"])
            check_type(argname="argument http_error3_xx", value=http_error3_xx, expected_type=type_hints["http_error3_xx"])
            check_type(argname="argument http_error4_xx", value=http_error4_xx, expected_type=type_hints["http_error4_xx"])
            check_type(argname="argument http_error5_xx", value=http_error5_xx, expected_type=type_hints["http_error5_xx"])
            check_type(argname="argument http_header", value=http_header, expected_type=type_hints["http_header"])
            check_type(argname="argument peer_certificate_verification", value=peer_certificate_verification, expected_type=type_hints["peer_certificate_verification"])
            check_type(argname="argument recursion_requested", value=recursion_requested, expected_type=type_hints["recursion_requested"])
            check_type(argname="argument request_string", value=request_string, expected_type=type_hints["request_string"])
            check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
            check_type(argname="argument response_string", value=response_string, expected_type=type_hints["response_string"])
            check_type(argname="argument ssl_client_certificate", value=ssl_client_certificate, expected_type=type_hints["ssl_client_certificate"])
            check_type(argname="argument ssl_client_private_key", value=ssl_client_private_key, expected_type=type_hints["ssl_client_private_key"])
            check_type(argname="argument test_object", value=test_object, expected_type=type_hints["test_object"])
            check_type(argname="argument test_object_password", value=test_object_password, expected_type=type_hints["test_object_password"])
            check_type(argname="argument test_object_port", value=test_object_port, expected_type=type_hints["test_object_port"])
            check_type(argname="argument test_object_username", value=test_object_username, expected_type=type_hints["test_object_username"])
            check_type(argname="argument timeout_penalty", value=timeout_penalty, expected_type=type_hints["timeout_penalty"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "test_interval": test_interval,
            "test_object_protocol": test_object_protocol,
            "test_timeout": test_timeout,
        }
        if answers_required is not None:
            self._values["answers_required"] = answers_required
        if disabled is not None:
            self._values["disabled"] = disabled
        if disable_nonstandard_port_warning is not None:
            self._values["disable_nonstandard_port_warning"] = disable_nonstandard_port_warning
        if error_penalty is not None:
            self._values["error_penalty"] = error_penalty
        if http_error3_xx is not None:
            self._values["http_error3_xx"] = http_error3_xx
        if http_error4_xx is not None:
            self._values["http_error4_xx"] = http_error4_xx
        if http_error5_xx is not None:
            self._values["http_error5_xx"] = http_error5_xx
        if http_header is not None:
            self._values["http_header"] = http_header
        if peer_certificate_verification is not None:
            self._values["peer_certificate_verification"] = peer_certificate_verification
        if recursion_requested is not None:
            self._values["recursion_requested"] = recursion_requested
        if request_string is not None:
            self._values["request_string"] = request_string
        if resource_type is not None:
            self._values["resource_type"] = resource_type
        if response_string is not None:
            self._values["response_string"] = response_string
        if ssl_client_certificate is not None:
            self._values["ssl_client_certificate"] = ssl_client_certificate
        if ssl_client_private_key is not None:
            self._values["ssl_client_private_key"] = ssl_client_private_key
        if test_object is not None:
            self._values["test_object"] = test_object
        if test_object_password is not None:
            self._values["test_object_password"] = test_object_password
        if test_object_port is not None:
            self._values["test_object_port"] = test_object_port
        if test_object_username is not None:
            self._values["test_object_username"] = test_object_username
        if timeout_penalty is not None:
            self._values["timeout_penalty"] = timeout_penalty

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#name GtmProperty#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def test_interval(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#test_interval GtmProperty#test_interval}.'''
        result = self._values.get("test_interval")
        assert result is not None, "Required property 'test_interval' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def test_object_protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#test_object_protocol GtmProperty#test_object_protocol}.'''
        result = self._values.get("test_object_protocol")
        assert result is not None, "Required property 'test_object_protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def test_timeout(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#test_timeout GtmProperty#test_timeout}.'''
        result = self._values.get("test_timeout")
        assert result is not None, "Required property 'test_timeout' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def answers_required(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#answers_required GtmProperty#answers_required}.'''
        result = self._values.get("answers_required")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#disabled GtmProperty#disabled}.'''
        result = self._values.get("disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def disable_nonstandard_port_warning(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#disable_nonstandard_port_warning GtmProperty#disable_nonstandard_port_warning}.'''
        result = self._values.get("disable_nonstandard_port_warning")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def error_penalty(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#error_penalty GtmProperty#error_penalty}.'''
        result = self._values.get("error_penalty")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def http_error3_xx(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#http_error3xx GtmProperty#http_error3xx}.'''
        result = self._values.get("http_error3_xx")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def http_error4_xx(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#http_error4xx GtmProperty#http_error4xx}.'''
        result = self._values.get("http_error4_xx")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def http_error5_xx(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#http_error5xx GtmProperty#http_error5xx}.'''
        result = self._values.get("http_error5_xx")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def http_header(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GtmPropertyLivenessTestHttpHeader"]]]:
        '''http_header block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#http_header GtmProperty#http_header}
        '''
        result = self._values.get("http_header")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GtmPropertyLivenessTestHttpHeader"]]], result)

    @builtins.property
    def peer_certificate_verification(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#peer_certificate_verification GtmProperty#peer_certificate_verification}.'''
        result = self._values.get("peer_certificate_verification")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def recursion_requested(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#recursion_requested GtmProperty#recursion_requested}.'''
        result = self._values.get("recursion_requested")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def request_string(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#request_string GtmProperty#request_string}.'''
        result = self._values.get("request_string")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#resource_type GtmProperty#resource_type}.'''
        result = self._values.get("resource_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def response_string(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#response_string GtmProperty#response_string}.'''
        result = self._values.get("response_string")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssl_client_certificate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#ssl_client_certificate GtmProperty#ssl_client_certificate}.'''
        result = self._values.get("ssl_client_certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssl_client_private_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#ssl_client_private_key GtmProperty#ssl_client_private_key}.'''
        result = self._values.get("ssl_client_private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def test_object(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#test_object GtmProperty#test_object}.'''
        result = self._values.get("test_object")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def test_object_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#test_object_password GtmProperty#test_object_password}.'''
        result = self._values.get("test_object_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def test_object_port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#test_object_port GtmProperty#test_object_port}.'''
        result = self._values.get("test_object_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def test_object_username(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#test_object_username GtmProperty#test_object_username}.'''
        result = self._values.get("test_object_username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeout_penalty(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#timeout_penalty GtmProperty#timeout_penalty}.'''
        result = self._values.get("timeout_penalty")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GtmPropertyLivenessTest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.gtmProperty.GtmPropertyLivenessTestHttpHeader",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class GtmPropertyLivenessTestHttpHeader:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#name GtmProperty#name}.
        :param value: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#value GtmProperty#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bd04adc01bbbf0417f990c58bc784d4470d7f0beae3ade0ff625c38480c8deb)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#name GtmProperty#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#value GtmProperty#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GtmPropertyLivenessTestHttpHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GtmPropertyLivenessTestHttpHeaderList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.gtmProperty.GtmPropertyLivenessTestHttpHeaderList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1da67a72c2cb7107d46efd3809f39bec1ef9161fc210d8f6ae7a4653dfe69e15)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GtmPropertyLivenessTestHttpHeaderOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54d8b62e70a04574987193105d56b5efdfa8830044b03107cc4e69aef54d7eb2)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GtmPropertyLivenessTestHttpHeaderOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed44cb67c56d72ccff6451625f2ff82fa681f420865e7a4d4066c579479cb146)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6f5a7fd33d5e2b6d271544792ad0f91be0eaf45d16c79e742b49c65681a3925c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5e7569324db821419016670e6603976433bb76304000a422c61fe040a3fc1355)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmPropertyLivenessTestHttpHeader]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmPropertyLivenessTestHttpHeader]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmPropertyLivenessTestHttpHeader]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c53f14a86c9ebcf418ea4d29d347e93a2f3113c453c8bead9661c78eca9d0f5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GtmPropertyLivenessTestHttpHeaderOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.gtmProperty.GtmPropertyLivenessTestHttpHeaderOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__79a378373e62ffb3725eecff82e35052424a668c5cc18c57e6c79e84afe48997)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95391d2c65cb523f1d10cc843d60728e1044c523d02b45afbb60557a49730497)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a53e0e9830dc9857f4b5323c19021dd1854bd707f3a2c5b5386a614fa4655718)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GtmPropertyLivenessTestHttpHeader]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GtmPropertyLivenessTestHttpHeader]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GtmPropertyLivenessTestHttpHeader]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4036654edfc6d6a3102a1c6b94ea608877491ece5ebc95f0d868105295de596)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GtmPropertyLivenessTestList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.gtmProperty.GtmPropertyLivenessTestList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3131ab6b4a2dd20d0e7cdbeae4ab796f80cce69ad79bc4d12ff98339ac9546fc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GtmPropertyLivenessTestOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6508df68661cd06409e57669e9861e2715cc290eee1fffdefb4f935376e0b9f1)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GtmPropertyLivenessTestOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e76138bbe88cbe89d5ded61290489360b2bb1585fe0160f42af2cb9d1067f48)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b9380c85820411629aea2d921c2058d2afa26b64fc63af4a14409056270f892e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9913a58bb530073498915d56391226b4e25682d8418bce86ea085c530467f8cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmPropertyLivenessTest]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmPropertyLivenessTest]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmPropertyLivenessTest]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5211b578046c3c46a246c0b9ba3583dca40ef8c97744203924be9899be73d011)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GtmPropertyLivenessTestOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.gtmProperty.GtmPropertyLivenessTestOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__21c00f59a7af297663b6527a7dffbde012f4cc8fc1626a14aa5e3562d1a05bbd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putHttpHeader")
    def put_http_header(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GtmPropertyLivenessTestHttpHeader, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c90d00b9f4992b213a8ab700f5d729bbd9fa00483abe2cebb45f9052e9fe643)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHttpHeader", [value]))

    @jsii.member(jsii_name="resetAnswersRequired")
    def reset_answers_required(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnswersRequired", []))

    @jsii.member(jsii_name="resetDisabled")
    def reset_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisabled", []))

    @jsii.member(jsii_name="resetDisableNonstandardPortWarning")
    def reset_disable_nonstandard_port_warning(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableNonstandardPortWarning", []))

    @jsii.member(jsii_name="resetErrorPenalty")
    def reset_error_penalty(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorPenalty", []))

    @jsii.member(jsii_name="resetHttpError3Xx")
    def reset_http_error3_xx(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpError3Xx", []))

    @jsii.member(jsii_name="resetHttpError4Xx")
    def reset_http_error4_xx(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpError4Xx", []))

    @jsii.member(jsii_name="resetHttpError5Xx")
    def reset_http_error5_xx(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpError5Xx", []))

    @jsii.member(jsii_name="resetHttpHeader")
    def reset_http_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpHeader", []))

    @jsii.member(jsii_name="resetPeerCertificateVerification")
    def reset_peer_certificate_verification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeerCertificateVerification", []))

    @jsii.member(jsii_name="resetRecursionRequested")
    def reset_recursion_requested(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecursionRequested", []))

    @jsii.member(jsii_name="resetRequestString")
    def reset_request_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestString", []))

    @jsii.member(jsii_name="resetResourceType")
    def reset_resource_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceType", []))

    @jsii.member(jsii_name="resetResponseString")
    def reset_response_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseString", []))

    @jsii.member(jsii_name="resetSslClientCertificate")
    def reset_ssl_client_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslClientCertificate", []))

    @jsii.member(jsii_name="resetSslClientPrivateKey")
    def reset_ssl_client_private_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslClientPrivateKey", []))

    @jsii.member(jsii_name="resetTestObject")
    def reset_test_object(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTestObject", []))

    @jsii.member(jsii_name="resetTestObjectPassword")
    def reset_test_object_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTestObjectPassword", []))

    @jsii.member(jsii_name="resetTestObjectPort")
    def reset_test_object_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTestObjectPort", []))

    @jsii.member(jsii_name="resetTestObjectUsername")
    def reset_test_object_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTestObjectUsername", []))

    @jsii.member(jsii_name="resetTimeoutPenalty")
    def reset_timeout_penalty(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeoutPenalty", []))

    @builtins.property
    @jsii.member(jsii_name="httpHeader")
    def http_header(self) -> GtmPropertyLivenessTestHttpHeaderList:
        return typing.cast(GtmPropertyLivenessTestHttpHeaderList, jsii.get(self, "httpHeader"))

    @builtins.property
    @jsii.member(jsii_name="answersRequiredInput")
    def answers_required_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "answersRequiredInput"))

    @builtins.property
    @jsii.member(jsii_name="disabledInput")
    def disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disabledInput"))

    @builtins.property
    @jsii.member(jsii_name="disableNonstandardPortWarningInput")
    def disable_nonstandard_port_warning_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableNonstandardPortWarningInput"))

    @builtins.property
    @jsii.member(jsii_name="errorPenaltyInput")
    def error_penalty_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "errorPenaltyInput"))

    @builtins.property
    @jsii.member(jsii_name="httpError3XxInput")
    def http_error3_xx_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "httpError3XxInput"))

    @builtins.property
    @jsii.member(jsii_name="httpError4XxInput")
    def http_error4_xx_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "httpError4XxInput"))

    @builtins.property
    @jsii.member(jsii_name="httpError5XxInput")
    def http_error5_xx_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "httpError5XxInput"))

    @builtins.property
    @jsii.member(jsii_name="httpHeaderInput")
    def http_header_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmPropertyLivenessTestHttpHeader]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmPropertyLivenessTestHttpHeader]]], jsii.get(self, "httpHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="peerCertificateVerificationInput")
    def peer_certificate_verification_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "peerCertificateVerificationInput"))

    @builtins.property
    @jsii.member(jsii_name="recursionRequestedInput")
    def recursion_requested_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "recursionRequestedInput"))

    @builtins.property
    @jsii.member(jsii_name="requestStringInput")
    def request_string_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "requestStringInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceTypeInput")
    def resource_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="responseStringInput")
    def response_string_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseStringInput"))

    @builtins.property
    @jsii.member(jsii_name="sslClientCertificateInput")
    def ssl_client_certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslClientCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="sslClientPrivateKeyInput")
    def ssl_client_private_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslClientPrivateKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="testIntervalInput")
    def test_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "testIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="testObjectInput")
    def test_object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "testObjectInput"))

    @builtins.property
    @jsii.member(jsii_name="testObjectPasswordInput")
    def test_object_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "testObjectPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="testObjectPortInput")
    def test_object_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "testObjectPortInput"))

    @builtins.property
    @jsii.member(jsii_name="testObjectProtocolInput")
    def test_object_protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "testObjectProtocolInput"))

    @builtins.property
    @jsii.member(jsii_name="testObjectUsernameInput")
    def test_object_username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "testObjectUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="testTimeoutInput")
    def test_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "testTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutPenaltyInput")
    def timeout_penalty_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutPenaltyInput"))

    @builtins.property
    @jsii.member(jsii_name="answersRequired")
    def answers_required(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "answersRequired"))

    @answers_required.setter
    def answers_required(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d13972e7656361e59fefcc86566b272cc0fc640dd83db0b471959eef7fadd9d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "answersRequired", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__7793ad7319b386a6cebd8e9281eb3381ddf80e021da72cbcf027d9e11aa93275)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabled", value)

    @builtins.property
    @jsii.member(jsii_name="disableNonstandardPortWarning")
    def disable_nonstandard_port_warning(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disableNonstandardPortWarning"))

    @disable_nonstandard_port_warning.setter
    def disable_nonstandard_port_warning(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58942a55e4ef8df4f7cb5e5084b72308921789ac551f84d413ffb3f6312685dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableNonstandardPortWarning", value)

    @builtins.property
    @jsii.member(jsii_name="errorPenalty")
    def error_penalty(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "errorPenalty"))

    @error_penalty.setter
    def error_penalty(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0178a29058797d3b79f40f49758026fb2d9c44e4f7253ee671c9b939ae641fbb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "errorPenalty", value)

    @builtins.property
    @jsii.member(jsii_name="httpError3Xx")
    def http_error3_xx(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "httpError3Xx"))

    @http_error3_xx.setter
    def http_error3_xx(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c98e058905522741cc5c12766adb2fff743507fc24c27b40c096066e8fe07a25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpError3Xx", value)

    @builtins.property
    @jsii.member(jsii_name="httpError4Xx")
    def http_error4_xx(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "httpError4Xx"))

    @http_error4_xx.setter
    def http_error4_xx(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__242c3d56ae2fa5afc6196299dcf986ed4a19d50ad84c09f23e6cb94878ec57f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpError4Xx", value)

    @builtins.property
    @jsii.member(jsii_name="httpError5Xx")
    def http_error5_xx(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "httpError5Xx"))

    @http_error5_xx.setter
    def http_error5_xx(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70f38ad5f2c1516518549faed3999834be24760bd18b0cb107dc92e6733f4cec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpError5Xx", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c7c93f06b23f73f377a3322e13d16e17f55efd5d81e60a6f01b1bb880517d08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="peerCertificateVerification")
    def peer_certificate_verification(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "peerCertificateVerification"))

    @peer_certificate_verification.setter
    def peer_certificate_verification(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f77d4da3c2681505614dbe7752eec74064b363e4e6e8d40f1a7612026dd52e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "peerCertificateVerification", value)

    @builtins.property
    @jsii.member(jsii_name="recursionRequested")
    def recursion_requested(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "recursionRequested"))

    @recursion_requested.setter
    def recursion_requested(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20476ea372b7bc138887b6dd746f537e19302ad21ca5bc190135163981623673)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recursionRequested", value)

    @builtins.property
    @jsii.member(jsii_name="requestString")
    def request_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "requestString"))

    @request_string.setter
    def request_string(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd60993e637e371c91fb6dbc71a378418f4722a16c89879072570172d53d69d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestString", value)

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @resource_type.setter
    def resource_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43923861971f02cf4e77a903800f15cd14730f06740043f138ba9d2457d74a83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceType", value)

    @builtins.property
    @jsii.member(jsii_name="responseString")
    def response_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseString"))

    @response_string.setter
    def response_string(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57291780c16dd254595c73a814c5505c5922846d20dcfa41fd458f61aa031c1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseString", value)

    @builtins.property
    @jsii.member(jsii_name="sslClientCertificate")
    def ssl_client_certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslClientCertificate"))

    @ssl_client_certificate.setter
    def ssl_client_certificate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__575b6ef25626c125238fb31847320224a261dd609fb7af386cbf076c3ed0f840)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslClientCertificate", value)

    @builtins.property
    @jsii.member(jsii_name="sslClientPrivateKey")
    def ssl_client_private_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslClientPrivateKey"))

    @ssl_client_private_key.setter
    def ssl_client_private_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05c5954f0d0a1519690f27c62bfb8803ac88bdab7eafce29555199a96fb2524d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslClientPrivateKey", value)

    @builtins.property
    @jsii.member(jsii_name="testInterval")
    def test_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "testInterval"))

    @test_interval.setter
    def test_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0af021edf1273624a9d54b0db421579ed6c782db8312b9e06728c2611c44b6d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "testInterval", value)

    @builtins.property
    @jsii.member(jsii_name="testObject")
    def test_object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "testObject"))

    @test_object.setter
    def test_object(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a57041842e3cc1830fab0e8ba32c0e642b0c7c1fc071d60df14e0810e4184cad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "testObject", value)

    @builtins.property
    @jsii.member(jsii_name="testObjectPassword")
    def test_object_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "testObjectPassword"))

    @test_object_password.setter
    def test_object_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69876db4fb838039a6ef394f7720af5b5ed6759ade60b6258492183b91a60e4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "testObjectPassword", value)

    @builtins.property
    @jsii.member(jsii_name="testObjectPort")
    def test_object_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "testObjectPort"))

    @test_object_port.setter
    def test_object_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddcbf32321bd8f5320fd9d5dcbc118fe454275d10eb0ae117ccfa151e97d3a79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "testObjectPort", value)

    @builtins.property
    @jsii.member(jsii_name="testObjectProtocol")
    def test_object_protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "testObjectProtocol"))

    @test_object_protocol.setter
    def test_object_protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__040eebad5ba9ba6375f1326060816458372be3adc33ac32d45e71f050d3b6776)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "testObjectProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="testObjectUsername")
    def test_object_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "testObjectUsername"))

    @test_object_username.setter
    def test_object_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9eb016a4b7829968ce5bab0244bb351ba0c2156d27825a6d9c512313599f79f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "testObjectUsername", value)

    @builtins.property
    @jsii.member(jsii_name="testTimeout")
    def test_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "testTimeout"))

    @test_timeout.setter
    def test_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d7232ced42c9a8183d58cd3ebff5cf406db78c45c0b9dc5c416d72bf10c1a80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "testTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutPenalty")
    def timeout_penalty(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutPenalty"))

    @timeout_penalty.setter
    def timeout_penalty(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e355001749b61502f900827090101077af80d921764fb166fe8bb70145815be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutPenalty", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GtmPropertyLivenessTest]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GtmPropertyLivenessTest]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GtmPropertyLivenessTest]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9651077956553f06df96400cbc41e6ceeb8a108234025ebba8765ad9c1b21b3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.gtmProperty.GtmPropertyStaticRrSet",
    jsii_struct_bases=[],
    name_mapping={"rdata": "rdata", "ttl": "ttl", "type": "type"},
)
class GtmPropertyStaticRrSet:
    def __init__(
        self,
        *,
        rdata: typing.Optional[typing.Sequence[builtins.str]] = None,
        ttl: typing.Optional[jsii.Number] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param rdata: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#rdata GtmProperty#rdata}.
        :param ttl: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#ttl GtmProperty#ttl}.
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#type GtmProperty#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e2a7342f26ab60172459e19d407b6fd92ad8905e3386d556f6451dfa6d41d6e)
            check_type(argname="argument rdata", value=rdata, expected_type=type_hints["rdata"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if rdata is not None:
            self._values["rdata"] = rdata
        if ttl is not None:
            self._values["ttl"] = ttl
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def rdata(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#rdata GtmProperty#rdata}.'''
        result = self._values.get("rdata")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#ttl GtmProperty#ttl}.'''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#type GtmProperty#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GtmPropertyStaticRrSet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GtmPropertyStaticRrSetList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.gtmProperty.GtmPropertyStaticRrSetList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__24ad64bead3e614d91446ffda28dcefbc27e2cb6dc1bcdffd62e848415fc71c1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GtmPropertyStaticRrSetOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63491881aba7883764a05660bf02a9249a2fd6782b692cb5b51521c56bb9e58e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GtmPropertyStaticRrSetOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__224a0b4ad5f7983099a369ae602c5692abdbf05dd517a0b859c91637054198ad)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b78760e78c2c03c22431dcaa46ee99be758d11a41c60f5620fb2ff61d7a7d028)
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
            type_hints = typing.get_type_hints(_typecheckingstub__98a2ea7e6eb61624c87043517ce4b592c234e683dd8d1b9ef6080e65f4934196)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmPropertyStaticRrSet]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmPropertyStaticRrSet]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmPropertyStaticRrSet]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d6dccc4c2e2d7344a518a7bba700230340f585515c408bcedd54400264ed0bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GtmPropertyStaticRrSetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.gtmProperty.GtmPropertyStaticRrSetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a704f7fc91cad1fcbd50b85f106d7a8cf7e2b893bb962e89b52d2c4b58a95485)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetRdata")
    def reset_rdata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRdata", []))

    @jsii.member(jsii_name="resetTtl")
    def reset_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTtl", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="rdataInput")
    def rdata_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rdataInput"))

    @builtins.property
    @jsii.member(jsii_name="ttlInput")
    def ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ttlInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="rdata")
    def rdata(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "rdata"))

    @rdata.setter
    def rdata(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e347f0b5e8d8c79e9fca37666d80be55ffab655157ec20aca3316422724388f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rdata", value)

    @builtins.property
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ttl"))

    @ttl.setter
    def ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afbf61c813e30ab4f2f6c01754c2394942a88233a0443d5b636392dd11ca6933)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ttl", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f75155bd01731b4ac6054c4df6226770e0b5393ba8bbabea128bcd0821820b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GtmPropertyStaticRrSet]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GtmPropertyStaticRrSet]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GtmPropertyStaticRrSet]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0371f2ff2e714b1fbe4231d34f850db15667aabdc76cebaf790f94ed9ce0453e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.gtmProperty.GtmPropertyTrafficTarget",
    jsii_struct_bases=[],
    name_mapping={
        "datacenter_id": "datacenterId",
        "enabled": "enabled",
        "handout_cname": "handoutCname",
        "name": "name",
        "servers": "servers",
        "weight": "weight",
    },
)
class GtmPropertyTrafficTarget:
    def __init__(
        self,
        *,
        datacenter_id: typing.Optional[jsii.Number] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        handout_cname: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        servers: typing.Optional[typing.Sequence[builtins.str]] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param datacenter_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#datacenter_id GtmProperty#datacenter_id}.
        :param enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#enabled GtmProperty#enabled}.
        :param handout_cname: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#handout_cname GtmProperty#handout_cname}.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#name GtmProperty#name}.
        :param servers: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#servers GtmProperty#servers}.
        :param weight: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#weight GtmProperty#weight}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7eaf66862220b121a73f353fddbfa4b8fef4eaf6fc92b94523b369d4b03f0c4)
            check_type(argname="argument datacenter_id", value=datacenter_id, expected_type=type_hints["datacenter_id"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument handout_cname", value=handout_cname, expected_type=type_hints["handout_cname"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument servers", value=servers, expected_type=type_hints["servers"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if datacenter_id is not None:
            self._values["datacenter_id"] = datacenter_id
        if enabled is not None:
            self._values["enabled"] = enabled
        if handout_cname is not None:
            self._values["handout_cname"] = handout_cname
        if name is not None:
            self._values["name"] = name
        if servers is not None:
            self._values["servers"] = servers
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def datacenter_id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#datacenter_id GtmProperty#datacenter_id}.'''
        result = self._values.get("datacenter_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#enabled GtmProperty#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def handout_cname(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#handout_cname GtmProperty#handout_cname}.'''
        result = self._values.get("handout_cname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#name GtmProperty#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def servers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#servers GtmProperty#servers}.'''
        result = self._values.get("servers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_property#weight GtmProperty#weight}.'''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GtmPropertyTrafficTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GtmPropertyTrafficTargetList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.gtmProperty.GtmPropertyTrafficTargetList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b2364ca0f61cfb4070882b7ab27ea82706275317bc2028abf345d65bae3fd215)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GtmPropertyTrafficTargetOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19de98f30db7464014d5aaf5e7ec0c43e425dc25454e663a1f058e21f9fe0a15)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GtmPropertyTrafficTargetOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae45e0724ea71ee99f6110723fc84b083e3eefb8f6039fc8ca4418e38d63f422)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f3fc3099e7c0e545e1dcc61627dbb1ad0e14cc2491be60f28707ac9dd810cd3c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__11376cc53b1181fff76e2b2d53ae86e9e95f121669b71297ef0a40674b57c794)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmPropertyTrafficTarget]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmPropertyTrafficTarget]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmPropertyTrafficTarget]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f386e27c88408894005645ae244206f8b6f38e60a1059c544be6783adf16c02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GtmPropertyTrafficTargetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.gtmProperty.GtmPropertyTrafficTargetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c29c2c9e6f1f6bd341af4392cf85bf441cae900d39c559fb0819a5df835f187b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDatacenterId")
    def reset_datacenter_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatacenterId", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetHandoutCname")
    def reset_handout_cname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHandoutCname", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetServers")
    def reset_servers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServers", []))

    @jsii.member(jsii_name="resetWeight")
    def reset_weight(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeight", []))

    @builtins.property
    @jsii.member(jsii_name="datacenterIdInput")
    def datacenter_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "datacenterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="handoutCnameInput")
    def handout_cname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "handoutCnameInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="serversInput")
    def servers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "serversInput"))

    @builtins.property
    @jsii.member(jsii_name="weightInput")
    def weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightInput"))

    @builtins.property
    @jsii.member(jsii_name="datacenterId")
    def datacenter_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "datacenterId"))

    @datacenter_id.setter
    def datacenter_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cca2425dee09c9a310deca14e644e3325e62aea3f30511e30b53c290dffbdbd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datacenterId", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96875d5ce8423211cd3259023fc3d5dbacb4209bc95e1daee6f2514e87b1fea9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="handoutCname")
    def handout_cname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "handoutCname"))

    @handout_cname.setter
    def handout_cname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfe8e6bb273f373b7e70864b24afe136d1d3ac0180665191e39a854a013391fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "handoutCname", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5efa987252714276b9e967431c9c73e78bef821d3f6f7607daaa1709133b7cc2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="servers")
    def servers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "servers"))

    @servers.setter
    def servers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cc9df50c05fd033bc2c458a07cb0dc4f1f9c91b284635bb6857264de70afe6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "servers", value)

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weight"))

    @weight.setter
    def weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8ab08a41fb143fccd8c6736f2a46655a0941cdaec9c961b061622d4705f7d46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weight", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GtmPropertyTrafficTarget]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GtmPropertyTrafficTarget]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GtmPropertyTrafficTarget]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11530b9e902e6bc9763c547bf8cdc99833e29f8e9b2d7448e789ed78de4c7c28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GtmProperty",
    "GtmPropertyConfig",
    "GtmPropertyLivenessTest",
    "GtmPropertyLivenessTestHttpHeader",
    "GtmPropertyLivenessTestHttpHeaderList",
    "GtmPropertyLivenessTestHttpHeaderOutputReference",
    "GtmPropertyLivenessTestList",
    "GtmPropertyLivenessTestOutputReference",
    "GtmPropertyStaticRrSet",
    "GtmPropertyStaticRrSetList",
    "GtmPropertyStaticRrSetOutputReference",
    "GtmPropertyTrafficTarget",
    "GtmPropertyTrafficTargetList",
    "GtmPropertyTrafficTargetOutputReference",
]

publication.publish()

def _typecheckingstub__b643d89ce032e7f4318c6e8a9a1e954c654e8778af5edfadfed7beb88a0f470d(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    domain: builtins.str,
    handout_limit: jsii.Number,
    handout_mode: builtins.str,
    name: builtins.str,
    score_aggregation_type: builtins.str,
    type: builtins.str,
    backup_cname: typing.Optional[builtins.str] = None,
    backup_ip: typing.Optional[builtins.str] = None,
    balance_by_download_score: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    cname: typing.Optional[builtins.str] = None,
    comments: typing.Optional[builtins.str] = None,
    dynamic_ttl: typing.Optional[jsii.Number] = None,
    failback_delay: typing.Optional[jsii.Number] = None,
    failover_delay: typing.Optional[jsii.Number] = None,
    ghost_demand_reporting: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    health_max: typing.Optional[jsii.Number] = None,
    health_multiplier: typing.Optional[jsii.Number] = None,
    health_threshold: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    ipv6: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    liveness_test: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GtmPropertyLivenessTest, typing.Dict[builtins.str, typing.Any]]]]] = None,
    load_imbalance_percentage: typing.Optional[jsii.Number] = None,
    map_name: typing.Optional[builtins.str] = None,
    max_unreachable_penalty: typing.Optional[jsii.Number] = None,
    min_live_fraction: typing.Optional[jsii.Number] = None,
    static_rr_set: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GtmPropertyStaticRrSet, typing.Dict[builtins.str, typing.Any]]]]] = None,
    static_ttl: typing.Optional[jsii.Number] = None,
    stickiness_bonus_constant: typing.Optional[jsii.Number] = None,
    stickiness_bonus_percentage: typing.Optional[jsii.Number] = None,
    traffic_target: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GtmPropertyTrafficTarget, typing.Dict[builtins.str, typing.Any]]]]] = None,
    unreachable_threshold: typing.Optional[jsii.Number] = None,
    use_computed_targets: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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

def _typecheckingstub__9bea20c66b55ec00b31d88ed3b52980d468db29c084435dadd3546ad535f774e(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99310899b2cb014f0d736ba45d897ba30c46efae6b69a4e3e76269cbb0629460(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GtmPropertyLivenessTest, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9bbc148c0ed52d87d0036fb933e513dc23230a066204cdf08a5e266fcf653a5(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GtmPropertyStaticRrSet, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac10351d66927524a557f68101973011083133ba00cc0c87dea7cbecad75a33d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GtmPropertyTrafficTarget, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f10f255084ef040f2591521ca6f292f9680b2d69dae8df8893ffae2ed7410edc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9f2ff883dd90427730c50a52ded511f2d7f1b0360794d94a36c53bf8e3e1fb5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25a7ac189be8fd790e35a9c92a77b0406c89217d80cee10ea0a8cf0f22c3586d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7951255fc3a92d63e7ef3809a8c119cf513a2d2ed33a20931a9a8b6289e3ad5a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cfeb377033c2543ef974153e64db0bc70d494ea843d3dd13cab03f619db3720(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81874216486e0f0571a1c75f70acf04202f591d0196a6d51fcca92acbf1b18e2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00b7f07ca5520fdd582eb9fc264c469bc36d8d430e5e1e5dbb005388972a170b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5db5b1aaa8becd3df7e74fab881dee5714b06e7685cbe9b206cdd085f06f4be8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__665d3fdfc9dc493bc63edcac3c419c15360b4acc68a7efe2f5a6451621d047c7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bde30a917cb99eef3c70ec8bdc7da7b570bdcee6bb53d351f733fdbf7e7bb1d2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75f6dfd981971d995deac7e992b63c7e524cb686195a41fc19bacbe51056e180(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02f4ed340d84a40548a27d2800b476466d8879783650908b526f85180f0da86d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fe528ff281e256ff566fababbcef8991792ff0511d9ba958afc0aa1721008c7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50456c7b86074ce67a7765bd1b04fadb749f8f8e67720253972bd475c3ad164e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f5bdf7ab8dc5512538d887cd7cfff5cd9075bb189e1f8bb28c38989890a73c2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01c8607b960fea7846d5b88bc6313f74cd155ea6687fdf85f9412ed5e07c7a1f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c22a9799a40278cf8275b2535aa29ef65e1e7f68a9ef18da6d84e1f42060eea4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__707cf77fe47cab98c4dd9a65a6c19d070f58ca486c3d15a1c06b517ff6b95f0f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6809629e030216c2045306ce7565be661aeb0747a0d39612441bed106a966b7b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05f06b54ebc166b42e0d6ace8c063b390aa34c7580cb8624700b568e8b84c963(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__831cade067ac64a29f3fd9cb4381378dd8ac21e563a3223f9f4feb8b677ccff2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70ec45ac70f82f8bbf2293e33accb2b97b8d4eae83ba1c4c75db573264ed4fd9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fea78e110232f5281e81edb2af1ce916c8a44c5fafa9116482dce05bec19e1a9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2348067efe4b66ce6952f873f6e5d853b2358bdd36ed697ab82d7adc9e8e81aa(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc91363a70a649321ae63164b0753123c3e65cf43af58bb59ea8aab20d67b254(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b055c56ae0ad6bdc46f660787da92183d0eff8ea81e61e7132c2e91f2563498(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__114e6f319f3bacc6641c244bee89cdd1e2fd1385b9cc4ce8fc59b4f59d424c4b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f571cc6902c4f0a36f2fc0ed4307cb6fba92e5180a1c0377e479ad6927592204(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04663718af1001fe96404b8ec913be5d9fe3f97200d63bdc991df0136f174c00(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef0ccb24781c9d548e3b337d6ff6f8727f2958511aee934e542292e3dc3a8f66(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcfb710470d47a2163bd8c268679fa46a16587c132f9d355094424efe943d017(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    domain: builtins.str,
    handout_limit: jsii.Number,
    handout_mode: builtins.str,
    name: builtins.str,
    score_aggregation_type: builtins.str,
    type: builtins.str,
    backup_cname: typing.Optional[builtins.str] = None,
    backup_ip: typing.Optional[builtins.str] = None,
    balance_by_download_score: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    cname: typing.Optional[builtins.str] = None,
    comments: typing.Optional[builtins.str] = None,
    dynamic_ttl: typing.Optional[jsii.Number] = None,
    failback_delay: typing.Optional[jsii.Number] = None,
    failover_delay: typing.Optional[jsii.Number] = None,
    ghost_demand_reporting: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    health_max: typing.Optional[jsii.Number] = None,
    health_multiplier: typing.Optional[jsii.Number] = None,
    health_threshold: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    ipv6: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    liveness_test: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GtmPropertyLivenessTest, typing.Dict[builtins.str, typing.Any]]]]] = None,
    load_imbalance_percentage: typing.Optional[jsii.Number] = None,
    map_name: typing.Optional[builtins.str] = None,
    max_unreachable_penalty: typing.Optional[jsii.Number] = None,
    min_live_fraction: typing.Optional[jsii.Number] = None,
    static_rr_set: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GtmPropertyStaticRrSet, typing.Dict[builtins.str, typing.Any]]]]] = None,
    static_ttl: typing.Optional[jsii.Number] = None,
    stickiness_bonus_constant: typing.Optional[jsii.Number] = None,
    stickiness_bonus_percentage: typing.Optional[jsii.Number] = None,
    traffic_target: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GtmPropertyTrafficTarget, typing.Dict[builtins.str, typing.Any]]]]] = None,
    unreachable_threshold: typing.Optional[jsii.Number] = None,
    use_computed_targets: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    wait_on_complete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e50d1387d34384167da4d9096bd77af2bc19561f3764335768293dce8272443c(
    *,
    name: builtins.str,
    test_interval: jsii.Number,
    test_object_protocol: builtins.str,
    test_timeout: jsii.Number,
    answers_required: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    disable_nonstandard_port_warning: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    error_penalty: typing.Optional[jsii.Number] = None,
    http_error3_xx: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    http_error4_xx: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    http_error5_xx: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    http_header: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GtmPropertyLivenessTestHttpHeader, typing.Dict[builtins.str, typing.Any]]]]] = None,
    peer_certificate_verification: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    recursion_requested: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    request_string: typing.Optional[builtins.str] = None,
    resource_type: typing.Optional[builtins.str] = None,
    response_string: typing.Optional[builtins.str] = None,
    ssl_client_certificate: typing.Optional[builtins.str] = None,
    ssl_client_private_key: typing.Optional[builtins.str] = None,
    test_object: typing.Optional[builtins.str] = None,
    test_object_password: typing.Optional[builtins.str] = None,
    test_object_port: typing.Optional[jsii.Number] = None,
    test_object_username: typing.Optional[builtins.str] = None,
    timeout_penalty: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bd04adc01bbbf0417f990c58bc784d4470d7f0beae3ade0ff625c38480c8deb(
    *,
    name: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1da67a72c2cb7107d46efd3809f39bec1ef9161fc210d8f6ae7a4653dfe69e15(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54d8b62e70a04574987193105d56b5efdfa8830044b03107cc4e69aef54d7eb2(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed44cb67c56d72ccff6451625f2ff82fa681f420865e7a4d4066c579479cb146(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f5a7fd33d5e2b6d271544792ad0f91be0eaf45d16c79e742b49c65681a3925c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e7569324db821419016670e6603976433bb76304000a422c61fe040a3fc1355(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c53f14a86c9ebcf418ea4d29d347e93a2f3113c453c8bead9661c78eca9d0f5c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmPropertyLivenessTestHttpHeader]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79a378373e62ffb3725eecff82e35052424a668c5cc18c57e6c79e84afe48997(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95391d2c65cb523f1d10cc843d60728e1044c523d02b45afbb60557a49730497(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a53e0e9830dc9857f4b5323c19021dd1854bd707f3a2c5b5386a614fa4655718(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4036654edfc6d6a3102a1c6b94ea608877491ece5ebc95f0d868105295de596(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GtmPropertyLivenessTestHttpHeader]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3131ab6b4a2dd20d0e7cdbeae4ab796f80cce69ad79bc4d12ff98339ac9546fc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6508df68661cd06409e57669e9861e2715cc290eee1fffdefb4f935376e0b9f1(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e76138bbe88cbe89d5ded61290489360b2bb1585fe0160f42af2cb9d1067f48(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9380c85820411629aea2d921c2058d2afa26b64fc63af4a14409056270f892e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9913a58bb530073498915d56391226b4e25682d8418bce86ea085c530467f8cc(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5211b578046c3c46a246c0b9ba3583dca40ef8c97744203924be9899be73d011(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmPropertyLivenessTest]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21c00f59a7af297663b6527a7dffbde012f4cc8fc1626a14aa5e3562d1a05bbd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c90d00b9f4992b213a8ab700f5d729bbd9fa00483abe2cebb45f9052e9fe643(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GtmPropertyLivenessTestHttpHeader, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d13972e7656361e59fefcc86566b272cc0fc640dd83db0b471959eef7fadd9d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7793ad7319b386a6cebd8e9281eb3381ddf80e021da72cbcf027d9e11aa93275(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58942a55e4ef8df4f7cb5e5084b72308921789ac551f84d413ffb3f6312685dd(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0178a29058797d3b79f40f49758026fb2d9c44e4f7253ee671c9b939ae641fbb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c98e058905522741cc5c12766adb2fff743507fc24c27b40c096066e8fe07a25(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__242c3d56ae2fa5afc6196299dcf986ed4a19d50ad84c09f23e6cb94878ec57f7(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70f38ad5f2c1516518549faed3999834be24760bd18b0cb107dc92e6733f4cec(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c7c93f06b23f73f377a3322e13d16e17f55efd5d81e60a6f01b1bb880517d08(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f77d4da3c2681505614dbe7752eec74064b363e4e6e8d40f1a7612026dd52e7(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20476ea372b7bc138887b6dd746f537e19302ad21ca5bc190135163981623673(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd60993e637e371c91fb6dbc71a378418f4722a16c89879072570172d53d69d0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43923861971f02cf4e77a903800f15cd14730f06740043f138ba9d2457d74a83(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57291780c16dd254595c73a814c5505c5922846d20dcfa41fd458f61aa031c1b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__575b6ef25626c125238fb31847320224a261dd609fb7af386cbf076c3ed0f840(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05c5954f0d0a1519690f27c62bfb8803ac88bdab7eafce29555199a96fb2524d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0af021edf1273624a9d54b0db421579ed6c782db8312b9e06728c2611c44b6d2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a57041842e3cc1830fab0e8ba32c0e642b0c7c1fc071d60df14e0810e4184cad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69876db4fb838039a6ef394f7720af5b5ed6759ade60b6258492183b91a60e4f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddcbf32321bd8f5320fd9d5dcbc118fe454275d10eb0ae117ccfa151e97d3a79(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__040eebad5ba9ba6375f1326060816458372be3adc33ac32d45e71f050d3b6776(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9eb016a4b7829968ce5bab0244bb351ba0c2156d27825a6d9c512313599f79f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d7232ced42c9a8183d58cd3ebff5cf406db78c45c0b9dc5c416d72bf10c1a80(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e355001749b61502f900827090101077af80d921764fb166fe8bb70145815be(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9651077956553f06df96400cbc41e6ceeb8a108234025ebba8765ad9c1b21b3c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GtmPropertyLivenessTest]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e2a7342f26ab60172459e19d407b6fd92ad8905e3386d556f6451dfa6d41d6e(
    *,
    rdata: typing.Optional[typing.Sequence[builtins.str]] = None,
    ttl: typing.Optional[jsii.Number] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24ad64bead3e614d91446ffda28dcefbc27e2cb6dc1bcdffd62e848415fc71c1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63491881aba7883764a05660bf02a9249a2fd6782b692cb5b51521c56bb9e58e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__224a0b4ad5f7983099a369ae602c5692abdbf05dd517a0b859c91637054198ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b78760e78c2c03c22431dcaa46ee99be758d11a41c60f5620fb2ff61d7a7d028(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98a2ea7e6eb61624c87043517ce4b592c234e683dd8d1b9ef6080e65f4934196(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d6dccc4c2e2d7344a518a7bba700230340f585515c408bcedd54400264ed0bf(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmPropertyStaticRrSet]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a704f7fc91cad1fcbd50b85f106d7a8cf7e2b893bb962e89b52d2c4b58a95485(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e347f0b5e8d8c79e9fca37666d80be55ffab655157ec20aca3316422724388f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afbf61c813e30ab4f2f6c01754c2394942a88233a0443d5b636392dd11ca6933(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f75155bd01731b4ac6054c4df6226770e0b5393ba8bbabea128bcd0821820b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0371f2ff2e714b1fbe4231d34f850db15667aabdc76cebaf790f94ed9ce0453e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GtmPropertyStaticRrSet]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7eaf66862220b121a73f353fddbfa4b8fef4eaf6fc92b94523b369d4b03f0c4(
    *,
    datacenter_id: typing.Optional[jsii.Number] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    handout_cname: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    servers: typing.Optional[typing.Sequence[builtins.str]] = None,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2364ca0f61cfb4070882b7ab27ea82706275317bc2028abf345d65bae3fd215(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19de98f30db7464014d5aaf5e7ec0c43e425dc25454e663a1f058e21f9fe0a15(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae45e0724ea71ee99f6110723fc84b083e3eefb8f6039fc8ca4418e38d63f422(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3fc3099e7c0e545e1dcc61627dbb1ad0e14cc2491be60f28707ac9dd810cd3c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11376cc53b1181fff76e2b2d53ae86e9e95f121669b71297ef0a40674b57c794(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f386e27c88408894005645ae244206f8b6f38e60a1059c544be6783adf16c02(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmPropertyTrafficTarget]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c29c2c9e6f1f6bd341af4392cf85bf441cae900d39c559fb0819a5df835f187b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cca2425dee09c9a310deca14e644e3325e62aea3f30511e30b53c290dffbdbd6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96875d5ce8423211cd3259023fc3d5dbacb4209bc95e1daee6f2514e87b1fea9(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfe8e6bb273f373b7e70864b24afe136d1d3ac0180665191e39a854a013391fe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5efa987252714276b9e967431c9c73e78bef821d3f6f7607daaa1709133b7cc2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cc9df50c05fd033bc2c458a07cb0dc4f1f9c91b284635bb6857264de70afe6b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8ab08a41fb143fccd8c6736f2a46655a0941cdaec9c961b061622d4705f7d46(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11530b9e902e6bc9763c547bf8cdc99833e29f8e9b2d7448e789ed78de4c7c28(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GtmPropertyTrafficTarget]],
) -> None:
    """Type checking stubs"""
    pass
