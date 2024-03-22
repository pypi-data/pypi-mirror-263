'''
# `data_akamai_gtm_domain`

Refer to the Terraform Registry for docs: [`data_akamai_gtm_domain`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain).
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


class DataAkamaiGtmDomain(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomain",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain akamai_gtm_domain}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        as_maps: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainAsMaps", typing.Dict[builtins.str, typing.Any]]]]] = None,
        cidr_maps: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainCidrMaps", typing.Dict[builtins.str, typing.Any]]]]] = None,
        datacenters: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainDatacenters", typing.Dict[builtins.str, typing.Any]]]]] = None,
        geographic_maps: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainGeographicMaps", typing.Dict[builtins.str, typing.Any]]]]] = None,
        links: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainLinks", typing.Dict[builtins.str, typing.Any]]]]] = None,
        properties: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainProperties", typing.Dict[builtins.str, typing.Any]]]]] = None,
        resources: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainResources", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain akamai_gtm_domain} Data Source.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The full GTM domain name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#name DataAkamaiGtmDomain#name}
        :param as_maps: as_maps block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#as_maps DataAkamaiGtmDomain#as_maps}
        :param cidr_maps: cidr_maps block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#cidr_maps DataAkamaiGtmDomain#cidr_maps}
        :param datacenters: datacenters block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#datacenters DataAkamaiGtmDomain#datacenters}
        :param geographic_maps: geographic_maps block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#geographic_maps DataAkamaiGtmDomain#geographic_maps}
        :param links: links block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#links DataAkamaiGtmDomain#links}
        :param properties: properties block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#properties DataAkamaiGtmDomain#properties}
        :param resources: resources block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#resources DataAkamaiGtmDomain#resources}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc99b076fa668ce0302c478187128723057998556f055572f4e3c069de44c375)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = DataAkamaiGtmDomainConfig(
            name=name,
            as_maps=as_maps,
            cidr_maps=cidr_maps,
            datacenters=datacenters,
            geographic_maps=geographic_maps,
            links=links,
            properties=properties,
            resources=resources,
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
        '''Generates CDKTF code for importing a DataAkamaiGtmDomain resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the DataAkamaiGtmDomain to import.
        :param import_from_id: The id of the existing DataAkamaiGtmDomain that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the DataAkamaiGtmDomain to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a31327bc46ec10aff34f8b648337da6e9c72f763a7ffb81126890d0adf365fb7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putAsMaps")
    def put_as_maps(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainAsMaps", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7961ef7617f01a85ff53ff90dcea60ec687e19997b82226d7a8285c9d433f97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAsMaps", [value]))

    @jsii.member(jsii_name="putCidrMaps")
    def put_cidr_maps(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainCidrMaps", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a26ab55124363dbcf8374664ef345912f1e3222501d2f007577c3f9fc9d9703f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCidrMaps", [value]))

    @jsii.member(jsii_name="putDatacenters")
    def put_datacenters(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainDatacenters", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7eca313ad4bdd1a9ebb532e5f15992efa9a19fd75c1fd52b5568d9ff1121a07)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDatacenters", [value]))

    @jsii.member(jsii_name="putGeographicMaps")
    def put_geographic_maps(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainGeographicMaps", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c99ba84c69ec8a7c657806d34ab46a20bf9f9c8214b3de579e305d24b41e2389)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGeographicMaps", [value]))

    @jsii.member(jsii_name="putLinks")
    def put_links(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainLinks", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f10d1d768cde6f7bb2b032b0f7e0d4877ce1e2eb9c6d40059d31522badfd45aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLinks", [value]))

    @jsii.member(jsii_name="putProperties")
    def put_properties(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainProperties", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f62edf5cf8300402c294841fd730738557d72a1a2f8fa04c4159533cbc7f1a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putProperties", [value]))

    @jsii.member(jsii_name="putResources")
    def put_resources(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainResources", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd6849bc1768e76d8c168d649401647de6d7b06ec11ba90ffc00c74c2e125a6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putResources", [value]))

    @jsii.member(jsii_name="resetAsMaps")
    def reset_as_maps(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAsMaps", []))

    @jsii.member(jsii_name="resetCidrMaps")
    def reset_cidr_maps(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCidrMaps", []))

    @jsii.member(jsii_name="resetDatacenters")
    def reset_datacenters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatacenters", []))

    @jsii.member(jsii_name="resetGeographicMaps")
    def reset_geographic_maps(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGeographicMaps", []))

    @jsii.member(jsii_name="resetLinks")
    def reset_links(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinks", []))

    @jsii.member(jsii_name="resetProperties")
    def reset_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProperties", []))

    @jsii.member(jsii_name="resetResources")
    def reset_resources(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResources", []))

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
    @jsii.member(jsii_name="asMaps")
    def as_maps(self) -> "DataAkamaiGtmDomainAsMapsList":
        return typing.cast("DataAkamaiGtmDomainAsMapsList", jsii.get(self, "asMaps"))

    @builtins.property
    @jsii.member(jsii_name="cidrMaps")
    def cidr_maps(self) -> "DataAkamaiGtmDomainCidrMapsList":
        return typing.cast("DataAkamaiGtmDomainCidrMapsList", jsii.get(self, "cidrMaps"))

    @builtins.property
    @jsii.member(jsii_name="cnameCoalescingEnabled")
    def cname_coalescing_enabled(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "cnameCoalescingEnabled"))

    @builtins.property
    @jsii.member(jsii_name="datacenters")
    def datacenters(self) -> "DataAkamaiGtmDomainDatacentersList":
        return typing.cast("DataAkamaiGtmDomainDatacentersList", jsii.get(self, "datacenters"))

    @builtins.property
    @jsii.member(jsii_name="defaultErrorPenalty")
    def default_error_penalty(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultErrorPenalty"))

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
    @jsii.member(jsii_name="defaultSslClientCertificate")
    def default_ssl_client_certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultSslClientCertificate"))

    @builtins.property
    @jsii.member(jsii_name="defaultSslClientPrivateKey")
    def default_ssl_client_private_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultSslClientPrivateKey"))

    @builtins.property
    @jsii.member(jsii_name="defaultTimeoutPenalty")
    def default_timeout_penalty(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultTimeoutPenalty"))

    @builtins.property
    @jsii.member(jsii_name="defaultUnreachableThreshold")
    def default_unreachable_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultUnreachableThreshold"))

    @builtins.property
    @jsii.member(jsii_name="emailNotificationList")
    def email_notification_list(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "emailNotificationList"))

    @builtins.property
    @jsii.member(jsii_name="endUserMappingEnabled")
    def end_user_mapping_enabled(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "endUserMappingEnabled"))

    @builtins.property
    @jsii.member(jsii_name="geographicMaps")
    def geographic_maps(self) -> "DataAkamaiGtmDomainGeographicMapsList":
        return typing.cast("DataAkamaiGtmDomainGeographicMapsList", jsii.get(self, "geographicMaps"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="lastModified")
    def last_modified(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastModified"))

    @builtins.property
    @jsii.member(jsii_name="lastModifiedBy")
    def last_modified_by(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastModifiedBy"))

    @builtins.property
    @jsii.member(jsii_name="links")
    def links(self) -> "DataAkamaiGtmDomainLinksList":
        return typing.cast("DataAkamaiGtmDomainLinksList", jsii.get(self, "links"))

    @builtins.property
    @jsii.member(jsii_name="loadFeedback")
    def load_feedback(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "loadFeedback"))

    @builtins.property
    @jsii.member(jsii_name="loadImbalancePercentage")
    def load_imbalance_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "loadImbalancePercentage"))

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
    @jsii.member(jsii_name="modificationComments")
    def modification_comments(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "modificationComments"))

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> "DataAkamaiGtmDomainPropertiesList":
        return typing.cast("DataAkamaiGtmDomainPropertiesList", jsii.get(self, "properties"))

    @builtins.property
    @jsii.member(jsii_name="resources")
    def resources(self) -> "DataAkamaiGtmDomainResourcesList":
        return typing.cast("DataAkamaiGtmDomainResourcesList", jsii.get(self, "resources"))

    @builtins.property
    @jsii.member(jsii_name="roundRobinPrefix")
    def round_robin_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roundRobinPrefix"))

    @builtins.property
    @jsii.member(jsii_name="serverMonitorPool")
    def server_monitor_pool(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverMonitorPool"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> "DataAkamaiGtmDomainStatusOutputReference":
        return typing.cast("DataAkamaiGtmDomainStatusOutputReference", jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="asMapsInput")
    def as_maps_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainAsMaps"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainAsMaps"]]], jsii.get(self, "asMapsInput"))

    @builtins.property
    @jsii.member(jsii_name="cidrMapsInput")
    def cidr_maps_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainCidrMaps"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainCidrMaps"]]], jsii.get(self, "cidrMapsInput"))

    @builtins.property
    @jsii.member(jsii_name="datacentersInput")
    def datacenters_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainDatacenters"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainDatacenters"]]], jsii.get(self, "datacentersInput"))

    @builtins.property
    @jsii.member(jsii_name="geographicMapsInput")
    def geographic_maps_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainGeographicMaps"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainGeographicMaps"]]], jsii.get(self, "geographicMapsInput"))

    @builtins.property
    @jsii.member(jsii_name="linksInput")
    def links_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainLinks"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainLinks"]]], jsii.get(self, "linksInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="propertiesInput")
    def properties_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainProperties"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainProperties"]]], jsii.get(self, "propertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="resourcesInput")
    def resources_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainResources"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainResources"]]], jsii.get(self, "resourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af6d5339d333720882a806c2b83bd4d9aa8e74ec0418c756b0f088a80f190c53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainAsMaps",
    jsii_struct_bases=[],
    name_mapping={"assignments": "assignments", "links": "links"},
)
class DataAkamaiGtmDomainAsMaps:
    def __init__(
        self,
        *,
        assignments: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainAsMapsAssignments", typing.Dict[builtins.str, typing.Any]]]]] = None,
        links: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainAsMapsLinks", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param assignments: assignments block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#assignments DataAkamaiGtmDomain#assignments}
        :param links: links block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#links DataAkamaiGtmDomain#links}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__117dae3a40c054eefa18efd0dd88f00ad359648d01c11619db4b36e45b8b2e48)
            check_type(argname="argument assignments", value=assignments, expected_type=type_hints["assignments"])
            check_type(argname="argument links", value=links, expected_type=type_hints["links"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if assignments is not None:
            self._values["assignments"] = assignments
        if links is not None:
            self._values["links"] = links

    @builtins.property
    def assignments(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainAsMapsAssignments"]]]:
        '''assignments block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#assignments DataAkamaiGtmDomain#assignments}
        '''
        result = self._values.get("assignments")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainAsMapsAssignments"]]], result)

    @builtins.property
    def links(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainAsMapsLinks"]]]:
        '''links block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#links DataAkamaiGtmDomain#links}
        '''
        result = self._values.get("links")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainAsMapsLinks"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiGtmDomainAsMaps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainAsMapsAssignments",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiGtmDomainAsMapsAssignments:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiGtmDomainAsMapsAssignments(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiGtmDomainAsMapsAssignmentsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainAsMapsAssignmentsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5f1dcd6bcfd9b9a86da619cd0251003fad21c40586719f2dce5d8dffbd02fd30)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiGtmDomainAsMapsAssignmentsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2c31d25363903edf3e43d1fcf43086ad029cd24f774322270a81bc748eb25c7)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiGtmDomainAsMapsAssignmentsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cab25170fc30e3a97c17e256246861ef114b7b9e26b3f200a89352d6e94b652f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d4c866fffa513bb3a9294e01a772cd3c3fbfb220678e3a98a44843e80731a5b6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cb7230d2d76e13756f5a0fef84cd71157203ca3a4f500fbcd5f0454179bc3a2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainAsMapsAssignments]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainAsMapsAssignments]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainAsMapsAssignments]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c6483b68879ec38928a7d41f6213d1080f21d7d4008a93039a522142968a7f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiGtmDomainAsMapsAssignmentsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainAsMapsAssignmentsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a46d7157378d024a8efb72a59e69188408897bbb5b9806c9e280046f43de6e4f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="asNumbers")
    def as_numbers(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "asNumbers"))

    @builtins.property
    @jsii.member(jsii_name="datacenterId")
    def datacenter_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "datacenterId"))

    @builtins.property
    @jsii.member(jsii_name="nickname")
    def nickname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nickname"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainAsMapsAssignments]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainAsMapsAssignments]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainAsMapsAssignments]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfd9fad3bfedaaab8a56c70bdc7f9e4ca61ac3c5339eb2b4f97c92f1d1d515f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainAsMapsDefaultDatacenter",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiGtmDomainAsMapsDefaultDatacenter:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiGtmDomainAsMapsDefaultDatacenter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiGtmDomainAsMapsDefaultDatacenterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainAsMapsDefaultDatacenterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1ff644c1bc4ac53266f5e3c9f77a04a47c8b29ea7d93d28f4b5a66da865148ca)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="datacenterId")
    def datacenter_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "datacenterId"))

    @builtins.property
    @jsii.member(jsii_name="nickname")
    def nickname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nickname"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainAsMapsDefaultDatacenter]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainAsMapsDefaultDatacenter]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainAsMapsDefaultDatacenter]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d2cf23da11015885e9820d16133f9dba68072f415780deb77345e7ceec12d0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainAsMapsLinks",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiGtmDomainAsMapsLinks:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiGtmDomainAsMapsLinks(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiGtmDomainAsMapsLinksList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainAsMapsLinksList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e7eeb55c1766ec4994028d49b21f5c8496770cf5eba48d4fefb8d95ece8acc27)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiGtmDomainAsMapsLinksOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3a22de048bde43cb4e81ae9d13f7e061c7a958c323227571d251789e841ba21)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiGtmDomainAsMapsLinksOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15a03b6fecbc756f2dbd5ffa1179aeffca9eca052601da43945782c3d085b25f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0f94e8a3986035f6c1c50c18fbd33130c96c6e8abe8a453f2f1870d0648f5693)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b55406fcc325dbfa569afac38dc98d72e8ebbf8462346ce25278df33c3958d71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainAsMapsLinks]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainAsMapsLinks]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainAsMapsLinks]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d91391615e040ea22d1ea6c4f2aeb565f73ff18e10972c70946130a497e7c916)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiGtmDomainAsMapsLinksOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainAsMapsLinksOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7ee67eb20e32d3638733d7ae75f2e3316b13d4bf08dfeec998fd5d046229c7d6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="href")
    def href(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "href"))

    @builtins.property
    @jsii.member(jsii_name="rel")
    def rel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rel"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainAsMapsLinks]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainAsMapsLinks]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainAsMapsLinks]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__932edcc7ae400af27fed64c39f27fb06984afdcd1f9bfc4c15ba154fc9136702)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiGtmDomainAsMapsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainAsMapsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a06aca9322b9665923d8d1716abdde7ec706d729b0bcc245a4c68a0eb8c4bf2a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DataAkamaiGtmDomainAsMapsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__506c3b14246b23dbfd05342cfd3f5267121cb9f2fceb34ce6b15fa9d0ba00a88)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiGtmDomainAsMapsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c0f1fe368db5f4519d429b14e6f032e07dde47cb234fb288eb6c3b568170208)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c2da84afd3535387fed938ae3178cc43d934842392972d6478fbcc404a6a9a14)
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
            type_hints = typing.get_type_hints(_typecheckingstub__633dde1f522fc81048d14348edd4cd09eedda0a42aaca07bef8b22c664f52a79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainAsMaps]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainAsMaps]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainAsMaps]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b53e5c16e693cce125406d85cb5769d8d208513fa5cd200007fb699abc22b6db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiGtmDomainAsMapsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainAsMapsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2e0b813c9d179717290463b4585995946b592a9072f4b9d7c34f4161c68cb3a1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAssignments")
    def put_assignments(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainAsMapsAssignments, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f307c5d420b1aa3225bacabdcd10a68a0b3722bb80b04c937ec459f1035f3cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAssignments", [value]))

    @jsii.member(jsii_name="putLinks")
    def put_links(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainAsMapsLinks, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c53d538e41fde4bcdf940dd75937b9974ffb7de4f19286f8caab99cf4c30235)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLinks", [value]))

    @jsii.member(jsii_name="resetAssignments")
    def reset_assignments(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssignments", []))

    @jsii.member(jsii_name="resetLinks")
    def reset_links(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinks", []))

    @builtins.property
    @jsii.member(jsii_name="assignments")
    def assignments(self) -> DataAkamaiGtmDomainAsMapsAssignmentsList:
        return typing.cast(DataAkamaiGtmDomainAsMapsAssignmentsList, jsii.get(self, "assignments"))

    @builtins.property
    @jsii.member(jsii_name="defaultDatacenter")
    def default_datacenter(
        self,
    ) -> DataAkamaiGtmDomainAsMapsDefaultDatacenterOutputReference:
        return typing.cast(DataAkamaiGtmDomainAsMapsDefaultDatacenterOutputReference, jsii.get(self, "defaultDatacenter"))

    @builtins.property
    @jsii.member(jsii_name="links")
    def links(self) -> DataAkamaiGtmDomainAsMapsLinksList:
        return typing.cast(DataAkamaiGtmDomainAsMapsLinksList, jsii.get(self, "links"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="assignmentsInput")
    def assignments_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainAsMapsAssignments]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainAsMapsAssignments]]], jsii.get(self, "assignmentsInput"))

    @builtins.property
    @jsii.member(jsii_name="linksInput")
    def links_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainAsMapsLinks]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainAsMapsLinks]]], jsii.get(self, "linksInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainAsMaps]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainAsMaps]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainAsMaps]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d6e69afc79b9114469f100d59f91cff68f91897fc9a341ca3e87b1dc2e3f4ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainCidrMaps",
    jsii_struct_bases=[],
    name_mapping={"assignments": "assignments", "links": "links"},
)
class DataAkamaiGtmDomainCidrMaps:
    def __init__(
        self,
        *,
        assignments: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainCidrMapsAssignments", typing.Dict[builtins.str, typing.Any]]]]] = None,
        links: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainCidrMapsLinks", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param assignments: assignments block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#assignments DataAkamaiGtmDomain#assignments}
        :param links: links block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#links DataAkamaiGtmDomain#links}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c35f3cef77edb09a9d64773bae3e47f9836f5e45102d671044fd6d68f0b59711)
            check_type(argname="argument assignments", value=assignments, expected_type=type_hints["assignments"])
            check_type(argname="argument links", value=links, expected_type=type_hints["links"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if assignments is not None:
            self._values["assignments"] = assignments
        if links is not None:
            self._values["links"] = links

    @builtins.property
    def assignments(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainCidrMapsAssignments"]]]:
        '''assignments block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#assignments DataAkamaiGtmDomain#assignments}
        '''
        result = self._values.get("assignments")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainCidrMapsAssignments"]]], result)

    @builtins.property
    def links(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainCidrMapsLinks"]]]:
        '''links block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#links DataAkamaiGtmDomain#links}
        '''
        result = self._values.get("links")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainCidrMapsLinks"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiGtmDomainCidrMaps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainCidrMapsAssignments",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiGtmDomainCidrMapsAssignments:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiGtmDomainCidrMapsAssignments(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiGtmDomainCidrMapsAssignmentsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainCidrMapsAssignmentsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__660e83c0a7f9c299354d4b1a7a7423ab918a0d0dce0fad67db3b63f608056cc2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiGtmDomainCidrMapsAssignmentsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1ccfcc8cea5f706d96a1e8b3ed2c695f32b662cb7f6d507a00d50fd6ce9537c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiGtmDomainCidrMapsAssignmentsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51d3ba59610302fa2d82f3085ded03fc1a07479c9c83077ce0ee4e5eeb590c2f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b97aa01fc09980746e76086be4752091f756ac9651d467e72abab60e6a1f0a89)
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
            type_hints = typing.get_type_hints(_typecheckingstub__da5af43edbc77bf60c372c9681964271572716b0151b6c4e5919e396f89e1470)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainCidrMapsAssignments]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainCidrMapsAssignments]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainCidrMapsAssignments]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39901a5d37e182c2bb9792ea9ef2030545354c3f38b5ba90b1a1e150caea4248)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiGtmDomainCidrMapsAssignmentsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainCidrMapsAssignmentsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__471f816db77cc152e999c48034a2187ebee7aef0aab74e8287d2cee4f060bfe7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="blocks")
    def blocks(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "blocks"))

    @builtins.property
    @jsii.member(jsii_name="datacenterId")
    def datacenter_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "datacenterId"))

    @builtins.property
    @jsii.member(jsii_name="nickname")
    def nickname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nickname"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainCidrMapsAssignments]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainCidrMapsAssignments]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainCidrMapsAssignments]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da9a49f246d6db6d88a91fa6ea1a7fdc70cdbfc54217aa230cb18e21e1cd1575)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainCidrMapsDefaultDatacenter",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiGtmDomainCidrMapsDefaultDatacenter:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiGtmDomainCidrMapsDefaultDatacenter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiGtmDomainCidrMapsDefaultDatacenterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainCidrMapsDefaultDatacenterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f2202be0848a69f28b3b741bb7b4c8fac81fa93aeca9d5c4bcd50009fd24df84)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="datacenterId")
    def datacenter_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "datacenterId"))

    @builtins.property
    @jsii.member(jsii_name="nickname")
    def nickname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nickname"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainCidrMapsDefaultDatacenter]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainCidrMapsDefaultDatacenter]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainCidrMapsDefaultDatacenter]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2043831eb13861b5a77153750a3803336f95e00fe16b016c33dcb323f31385e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainCidrMapsLinks",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiGtmDomainCidrMapsLinks:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiGtmDomainCidrMapsLinks(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiGtmDomainCidrMapsLinksList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainCidrMapsLinksList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5c1115a74c4e3904e1e2d97219218d61b89ac281f8cf8ece76d5855b95c0bfa2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiGtmDomainCidrMapsLinksOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5d4834f083c414cbe0f53616b8ada7aef99f32e834c7d5095453cf5da8f6c6e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiGtmDomainCidrMapsLinksOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9375a1356441d0ba5737f0cad363726b720050acec9d01b8c3e0a9fa67506bcb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b4362e30d07b0aba0f43bd2a05a907bf20e9d262c12adee67fc968c0d0a1a885)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f46b4a3d11e136578998404cc35dce6eacf7c2e33a4971a59c3cac72e65e4659)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainCidrMapsLinks]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainCidrMapsLinks]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainCidrMapsLinks]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cb6692cdeafb1f44faec0da21294140d885f0800646a8b16833e35f3bb9d48e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiGtmDomainCidrMapsLinksOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainCidrMapsLinksOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__70f1d8923917abdc90c85223a7fdd8fd463915b696fc7c27858f7e6e144b4778)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="href")
    def href(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "href"))

    @builtins.property
    @jsii.member(jsii_name="rel")
    def rel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rel"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainCidrMapsLinks]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainCidrMapsLinks]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainCidrMapsLinks]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9676a820d90a622246364a01450039345f208503e8b39023a74c9b2285c54cef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiGtmDomainCidrMapsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainCidrMapsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__872965da83f92521ad6ff3663c69a6968ad6d7966dc418857801167ffe6cd5b6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DataAkamaiGtmDomainCidrMapsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcd7c97b0945d706eda069f12b1e964542975efa3be0384acee605220a25a875)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiGtmDomainCidrMapsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2a99532567ee594d0effa0fac0ab3eed4529345daac90f7f206ef19e0a9af8b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6461dc73ae25b1fac533ba41be0ee3bf4e3587cc1dba2adfe32766576d433e0f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6d9a8163c6b6906a5c8d446333baf80a9932ccfb3f62c41dd9a1d1f261e6454d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainCidrMaps]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainCidrMaps]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainCidrMaps]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d65e96c6114635a0fbb3aad868e7280b42ba6de9bcf4ce82ad7c54cee5bff75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiGtmDomainCidrMapsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainCidrMapsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f598a9a051eed6f11c85bc43a0b31a49265c7d92e5096299a50a13e2abd2bd90)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAssignments")
    def put_assignments(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainCidrMapsAssignments, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4ab867c8775cbd58d19a8ee7dd0710ccabdfaae7dcb8e08edf0de12f16658e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAssignments", [value]))

    @jsii.member(jsii_name="putLinks")
    def put_links(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainCidrMapsLinks, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__568bbb84a0e6b538a5385884a194565496fa6ceb01f19839237019a65590f491)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLinks", [value]))

    @jsii.member(jsii_name="resetAssignments")
    def reset_assignments(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssignments", []))

    @jsii.member(jsii_name="resetLinks")
    def reset_links(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinks", []))

    @builtins.property
    @jsii.member(jsii_name="assignments")
    def assignments(self) -> DataAkamaiGtmDomainCidrMapsAssignmentsList:
        return typing.cast(DataAkamaiGtmDomainCidrMapsAssignmentsList, jsii.get(self, "assignments"))

    @builtins.property
    @jsii.member(jsii_name="defaultDatacenter")
    def default_datacenter(
        self,
    ) -> DataAkamaiGtmDomainCidrMapsDefaultDatacenterOutputReference:
        return typing.cast(DataAkamaiGtmDomainCidrMapsDefaultDatacenterOutputReference, jsii.get(self, "defaultDatacenter"))

    @builtins.property
    @jsii.member(jsii_name="links")
    def links(self) -> DataAkamaiGtmDomainCidrMapsLinksList:
        return typing.cast(DataAkamaiGtmDomainCidrMapsLinksList, jsii.get(self, "links"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="assignmentsInput")
    def assignments_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainCidrMapsAssignments]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainCidrMapsAssignments]]], jsii.get(self, "assignmentsInput"))

    @builtins.property
    @jsii.member(jsii_name="linksInput")
    def links_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainCidrMapsLinks]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainCidrMapsLinks]]], jsii.get(self, "linksInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainCidrMaps]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainCidrMaps]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainCidrMaps]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__733aeb5d161759e22acbedbd4dda5833f7b732fc23d0895c7fcc44b1330ce99b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainConfig",
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
        "as_maps": "asMaps",
        "cidr_maps": "cidrMaps",
        "datacenters": "datacenters",
        "geographic_maps": "geographicMaps",
        "links": "links",
        "properties": "properties",
        "resources": "resources",
    },
)
class DataAkamaiGtmDomainConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        as_maps: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainAsMaps, typing.Dict[builtins.str, typing.Any]]]]] = None,
        cidr_maps: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainCidrMaps, typing.Dict[builtins.str, typing.Any]]]]] = None,
        datacenters: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainDatacenters", typing.Dict[builtins.str, typing.Any]]]]] = None,
        geographic_maps: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainGeographicMaps", typing.Dict[builtins.str, typing.Any]]]]] = None,
        links: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainLinks", typing.Dict[builtins.str, typing.Any]]]]] = None,
        properties: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainProperties", typing.Dict[builtins.str, typing.Any]]]]] = None,
        resources: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainResources", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The full GTM domain name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#name DataAkamaiGtmDomain#name}
        :param as_maps: as_maps block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#as_maps DataAkamaiGtmDomain#as_maps}
        :param cidr_maps: cidr_maps block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#cidr_maps DataAkamaiGtmDomain#cidr_maps}
        :param datacenters: datacenters block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#datacenters DataAkamaiGtmDomain#datacenters}
        :param geographic_maps: geographic_maps block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#geographic_maps DataAkamaiGtmDomain#geographic_maps}
        :param links: links block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#links DataAkamaiGtmDomain#links}
        :param properties: properties block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#properties DataAkamaiGtmDomain#properties}
        :param resources: resources block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#resources DataAkamaiGtmDomain#resources}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__999093c45980b70972e1a2556d6c34e398122c6f64dbbdf48515ee724f913f92)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument as_maps", value=as_maps, expected_type=type_hints["as_maps"])
            check_type(argname="argument cidr_maps", value=cidr_maps, expected_type=type_hints["cidr_maps"])
            check_type(argname="argument datacenters", value=datacenters, expected_type=type_hints["datacenters"])
            check_type(argname="argument geographic_maps", value=geographic_maps, expected_type=type_hints["geographic_maps"])
            check_type(argname="argument links", value=links, expected_type=type_hints["links"])
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
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
        if as_maps is not None:
            self._values["as_maps"] = as_maps
        if cidr_maps is not None:
            self._values["cidr_maps"] = cidr_maps
        if datacenters is not None:
            self._values["datacenters"] = datacenters
        if geographic_maps is not None:
            self._values["geographic_maps"] = geographic_maps
        if links is not None:
            self._values["links"] = links
        if properties is not None:
            self._values["properties"] = properties
        if resources is not None:
            self._values["resources"] = resources

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
        '''The full GTM domain name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#name DataAkamaiGtmDomain#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def as_maps(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainAsMaps]]]:
        '''as_maps block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#as_maps DataAkamaiGtmDomain#as_maps}
        '''
        result = self._values.get("as_maps")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainAsMaps]]], result)

    @builtins.property
    def cidr_maps(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainCidrMaps]]]:
        '''cidr_maps block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#cidr_maps DataAkamaiGtmDomain#cidr_maps}
        '''
        result = self._values.get("cidr_maps")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainCidrMaps]]], result)

    @builtins.property
    def datacenters(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainDatacenters"]]]:
        '''datacenters block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#datacenters DataAkamaiGtmDomain#datacenters}
        '''
        result = self._values.get("datacenters")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainDatacenters"]]], result)

    @builtins.property
    def geographic_maps(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainGeographicMaps"]]]:
        '''geographic_maps block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#geographic_maps DataAkamaiGtmDomain#geographic_maps}
        '''
        result = self._values.get("geographic_maps")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainGeographicMaps"]]], result)

    @builtins.property
    def links(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainLinks"]]]:
        '''links block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#links DataAkamaiGtmDomain#links}
        '''
        result = self._values.get("links")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainLinks"]]], result)

    @builtins.property
    def properties(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainProperties"]]]:
        '''properties block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#properties DataAkamaiGtmDomain#properties}
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainProperties"]]], result)

    @builtins.property
    def resources(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainResources"]]]:
        '''resources block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#resources DataAkamaiGtmDomain#resources}
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainResources"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiGtmDomainConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainDatacenters",
    jsii_struct_bases=[],
    name_mapping={"default_load_object": "defaultLoadObject", "links": "links"},
)
class DataAkamaiGtmDomainDatacenters:
    def __init__(
        self,
        *,
        default_load_object: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainDatacentersDefaultLoadObject", typing.Dict[builtins.str, typing.Any]]]]] = None,
        links: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainDatacentersLinks", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param default_load_object: default_load_object block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#default_load_object DataAkamaiGtmDomain#default_load_object}
        :param links: links block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#links DataAkamaiGtmDomain#links}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd872b6fa0fcc0af3910923b387e92fc3828b22efa71ae45a0c0495ca7407645)
            check_type(argname="argument default_load_object", value=default_load_object, expected_type=type_hints["default_load_object"])
            check_type(argname="argument links", value=links, expected_type=type_hints["links"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if default_load_object is not None:
            self._values["default_load_object"] = default_load_object
        if links is not None:
            self._values["links"] = links

    @builtins.property
    def default_load_object(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainDatacentersDefaultLoadObject"]]]:
        '''default_load_object block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#default_load_object DataAkamaiGtmDomain#default_load_object}
        '''
        result = self._values.get("default_load_object")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainDatacentersDefaultLoadObject"]]], result)

    @builtins.property
    def links(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainDatacentersLinks"]]]:
        '''links block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#links DataAkamaiGtmDomain#links}
        '''
        result = self._values.get("links")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainDatacentersLinks"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiGtmDomainDatacenters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainDatacentersDefaultLoadObject",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiGtmDomainDatacentersDefaultLoadObject:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiGtmDomainDatacentersDefaultLoadObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiGtmDomainDatacentersDefaultLoadObjectList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainDatacentersDefaultLoadObjectList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__48452f3d422eabafa639b426342b56dad2ee330e9a33f85c6442042779459975)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiGtmDomainDatacentersDefaultLoadObjectOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5712aed638a40cb49d5452028f48415108cb7ea4325f5771d5c94b1c628e9ed6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiGtmDomainDatacentersDefaultLoadObjectOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25428e49cd6b17c4ad5cb65ddfd3a1c9a2adc62d1c3e12f51f0b48f77ec7bd14)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b01413a6918072a40707f610b6f1d868185659138167341525f6cc18d8a9d4be)
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
            type_hints = typing.get_type_hints(_typecheckingstub__13aa6e63be8b5395a17ba5fea73a870a48811ac24ca1238df04dab12c46fe6ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainDatacentersDefaultLoadObject]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainDatacentersDefaultLoadObject]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainDatacentersDefaultLoadObject]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00910c6ded0da1a26c670e01ad8d1c572cd867a90d8e9e5074b87c9492e52605)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiGtmDomainDatacentersDefaultLoadObjectOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainDatacentersDefaultLoadObjectOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6e86d18689be4e2931e41f6d75c3017d9a1a4beeb7374a105de47dd48d7676a1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="loadObject")
    def load_object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loadObject"))

    @builtins.property
    @jsii.member(jsii_name="loadObjectPort")
    def load_object_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "loadObjectPort"))

    @builtins.property
    @jsii.member(jsii_name="loadServers")
    def load_servers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "loadServers"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainDatacentersDefaultLoadObject]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainDatacentersDefaultLoadObject]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainDatacentersDefaultLoadObject]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8aa3163988cd379b1a8029be86f4e0a268e50aa850ca4f5ceb5b8ead1f4d41df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainDatacentersLinks",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiGtmDomainDatacentersLinks:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiGtmDomainDatacentersLinks(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiGtmDomainDatacentersLinksList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainDatacentersLinksList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__16eb6dbd160ecafe1e45bd0efa6b524eaee7f555f6f597b64bcfce8f5e48fa75)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiGtmDomainDatacentersLinksOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d30346389b9cf264203028227a32efcecc95cc17900f0603381f641b30c6fdb3)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiGtmDomainDatacentersLinksOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df0491943f18b9c1e1292101c2bdde258edbf828f82d0542c6ba22a5e30494ae)
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
            type_hints = typing.get_type_hints(_typecheckingstub__92e48165b7f453bb5de1e3995d4d819f8e8ed6e328b6668ca34b24282338abe8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__42b9fd5ab646a4f45bb3b55d9008d51238d1845cfd61c9ae26ea41c31f4e7148)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainDatacentersLinks]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainDatacentersLinks]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainDatacentersLinks]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d21178e44918c8d57eb546b54edde9a87a8b6ffb15945f6923da5b8100dacd3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiGtmDomainDatacentersLinksOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainDatacentersLinksOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b0d1967c3b5975b83f7bb07ec9c7165864ed0e97889982f7617ea6b1c24c4ee4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="href")
    def href(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "href"))

    @builtins.property
    @jsii.member(jsii_name="rel")
    def rel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rel"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainDatacentersLinks]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainDatacentersLinks]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainDatacentersLinks]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9987f807c07305efe23bfb41a1e52389fb9b1cfdbca574c87faf93e5a7488946)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiGtmDomainDatacentersList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainDatacentersList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3780c73597e6addaac05f4922fe65f5d2c2184f844661c719762271da82acad2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiGtmDomainDatacentersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b2464f413a5287510cf77dc1572f86e007a0e7cadc1e5a21fb09db29c71b320)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiGtmDomainDatacentersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7ada49c5ae09b27f36577f2dc5057b0c59d0c1a6809d6d08ecf963e43f926f1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8924c1d623d3fb246d027dc108dbc2fbfb11df402691d922fd0b0805d7e04835)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8f08603530ef6e7538029ef05aeb9ccb98d38aab598ef3f04c9e471a5a46dbee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainDatacenters]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainDatacenters]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainDatacenters]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b2a6f7c9f9437e42fdb22ee79bbd7ae4bdf3aff4d703ad1bfac2c3e440ae106)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiGtmDomainDatacentersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainDatacentersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__87f2e0032ffe19fd75d30671d1e4a31ef891dc043a5ba4261202e556db4506e3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDefaultLoadObject")
    def put_default_load_object(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainDatacentersDefaultLoadObject, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__542d5f37bf01070873ec9bc0805d1f1bd1935c1cb7c344bb82d87fe39019653a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDefaultLoadObject", [value]))

    @jsii.member(jsii_name="putLinks")
    def put_links(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainDatacentersLinks, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f215c9c7a2ec567cc32ccc348ec0a347103e050966130380679acdb6cb5b0ead)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLinks", [value]))

    @jsii.member(jsii_name="resetDefaultLoadObject")
    def reset_default_load_object(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultLoadObject", []))

    @jsii.member(jsii_name="resetLinks")
    def reset_links(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinks", []))

    @builtins.property
    @jsii.member(jsii_name="city")
    def city(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "city"))

    @builtins.property
    @jsii.member(jsii_name="cloneOf")
    def clone_of(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cloneOf"))

    @builtins.property
    @jsii.member(jsii_name="cloudServerHostHeaderOverride")
    def cloud_server_host_header_override(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "cloudServerHostHeaderOverride"))

    @builtins.property
    @jsii.member(jsii_name="cloudServerTargeting")
    def cloud_server_targeting(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "cloudServerTargeting"))

    @builtins.property
    @jsii.member(jsii_name="continent")
    def continent(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "continent"))

    @builtins.property
    @jsii.member(jsii_name="country")
    def country(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "country"))

    @builtins.property
    @jsii.member(jsii_name="datacenterId")
    def datacenter_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "datacenterId"))

    @builtins.property
    @jsii.member(jsii_name="defaultLoadObject")
    def default_load_object(
        self,
    ) -> DataAkamaiGtmDomainDatacentersDefaultLoadObjectList:
        return typing.cast(DataAkamaiGtmDomainDatacentersDefaultLoadObjectList, jsii.get(self, "defaultLoadObject"))

    @builtins.property
    @jsii.member(jsii_name="latitude")
    def latitude(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "latitude"))

    @builtins.property
    @jsii.member(jsii_name="links")
    def links(self) -> DataAkamaiGtmDomainDatacentersLinksList:
        return typing.cast(DataAkamaiGtmDomainDatacentersLinksList, jsii.get(self, "links"))

    @builtins.property
    @jsii.member(jsii_name="longitude")
    def longitude(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "longitude"))

    @builtins.property
    @jsii.member(jsii_name="nickname")
    def nickname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nickname"))

    @builtins.property
    @jsii.member(jsii_name="scorePenalty")
    def score_penalty(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scorePenalty"))

    @builtins.property
    @jsii.member(jsii_name="serverMonitorPool")
    def server_monitor_pool(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverMonitorPool"))

    @builtins.property
    @jsii.member(jsii_name="stateOrProvince")
    def state_or_province(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stateOrProvince"))

    @builtins.property
    @jsii.member(jsii_name="virtual")
    def virtual(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "virtual"))

    @builtins.property
    @jsii.member(jsii_name="defaultLoadObjectInput")
    def default_load_object_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainDatacentersDefaultLoadObject]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainDatacentersDefaultLoadObject]]], jsii.get(self, "defaultLoadObjectInput"))

    @builtins.property
    @jsii.member(jsii_name="linksInput")
    def links_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainDatacentersLinks]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainDatacentersLinks]]], jsii.get(self, "linksInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainDatacenters]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainDatacenters]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainDatacenters]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4db4f9fcf4f1b89813294a1f56630347b70e21971f0ee07247dc3cc24aeae304)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainGeographicMaps",
    jsii_struct_bases=[],
    name_mapping={"assignments": "assignments", "links": "links"},
)
class DataAkamaiGtmDomainGeographicMaps:
    def __init__(
        self,
        *,
        assignments: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainGeographicMapsAssignments", typing.Dict[builtins.str, typing.Any]]]]] = None,
        links: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainGeographicMapsLinks", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param assignments: assignments block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#assignments DataAkamaiGtmDomain#assignments}
        :param links: links block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#links DataAkamaiGtmDomain#links}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c3de928e81dc71e24a9b0ae7ee3c5e67686c00a9d663fd850d8d13925271d44)
            check_type(argname="argument assignments", value=assignments, expected_type=type_hints["assignments"])
            check_type(argname="argument links", value=links, expected_type=type_hints["links"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if assignments is not None:
            self._values["assignments"] = assignments
        if links is not None:
            self._values["links"] = links

    @builtins.property
    def assignments(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainGeographicMapsAssignments"]]]:
        '''assignments block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#assignments DataAkamaiGtmDomain#assignments}
        '''
        result = self._values.get("assignments")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainGeographicMapsAssignments"]]], result)

    @builtins.property
    def links(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainGeographicMapsLinks"]]]:
        '''links block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#links DataAkamaiGtmDomain#links}
        '''
        result = self._values.get("links")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainGeographicMapsLinks"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiGtmDomainGeographicMaps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainGeographicMapsAssignments",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiGtmDomainGeographicMapsAssignments:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiGtmDomainGeographicMapsAssignments(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiGtmDomainGeographicMapsAssignmentsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainGeographicMapsAssignmentsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__76e4dae3ebc38a1490bed57c42ff2cd5a2f49d8c9afa5456445d661a80d2f44e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiGtmDomainGeographicMapsAssignmentsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c49343ecbbb643683fe49b3f8755edd6d04f8e6b641c1093615dba05c924e7d4)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiGtmDomainGeographicMapsAssignmentsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f328e14c6a1ad64431f55893cb2dda55fe3b4a5fa53a8041b2a5d27b98e63ee)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5d7eae75f8e9720439a617bcd3a2468e85e8ac94888df832084543fe91588eda)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ceb648f1edefbfb75285d125759df1b1f2bee9307be2a8331b8c467538f8060b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainGeographicMapsAssignments]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainGeographicMapsAssignments]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainGeographicMapsAssignments]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb4b258138b90533ecc2c9b1cdfb537fcc146d2a2643b6cf70d79f907db6bd61)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiGtmDomainGeographicMapsAssignmentsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainGeographicMapsAssignmentsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__432fe6c6556c6789c935c3301fccb07ed809b97368d91d016aebaec33dd8af11)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="countries")
    def countries(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "countries"))

    @builtins.property
    @jsii.member(jsii_name="datacenterId")
    def datacenter_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "datacenterId"))

    @builtins.property
    @jsii.member(jsii_name="nickname")
    def nickname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nickname"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainGeographicMapsAssignments]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainGeographicMapsAssignments]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainGeographicMapsAssignments]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__844e34aa0cfb1bc49426ed42a00e8726f61cb779e8a27f68ce025cffb8f02242)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainGeographicMapsDefaultDatacenter",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiGtmDomainGeographicMapsDefaultDatacenter:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiGtmDomainGeographicMapsDefaultDatacenter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiGtmDomainGeographicMapsDefaultDatacenterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainGeographicMapsDefaultDatacenterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__da34d0e021ca1d1126fd97245625cd1422dd22342f363e24c102bb5e2fa5493e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="datacenterId")
    def datacenter_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "datacenterId"))

    @builtins.property
    @jsii.member(jsii_name="nickname")
    def nickname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nickname"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainGeographicMapsDefaultDatacenter]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainGeographicMapsDefaultDatacenter]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainGeographicMapsDefaultDatacenter]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c28b8b246040e76d037f063b6fcea5346f4257e47fd20a3fa6dcdea55b34317)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainGeographicMapsLinks",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiGtmDomainGeographicMapsLinks:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiGtmDomainGeographicMapsLinks(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiGtmDomainGeographicMapsLinksList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainGeographicMapsLinksList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d6d997917c645740acbe19d4a950ab7c8e4867ac8855d60a6ae82d9a624cc6ec)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiGtmDomainGeographicMapsLinksOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f72cd61bec4a2a8ae76ff9818ec1644afb13e50ed930adba905f0fdad8ebcb83)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiGtmDomainGeographicMapsLinksOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0307be876d6fbab7c6b7831ae28cf6066fb1d3f0ab567c3bdbab9c8e559da05)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8303a9d8fe2a69ed69b27700f23180fc9528c58fc5c338b06ee609d3b7e147cd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9c7dfd841afc02d7baa1a9fe982eec9c62609fd2f375aedee395bcdbc8956a11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainGeographicMapsLinks]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainGeographicMapsLinks]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainGeographicMapsLinks]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2bba8e4d2b486254bda3d1af4c38e2f8a27a5604fd723f02cbbf8399506eb25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiGtmDomainGeographicMapsLinksOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainGeographicMapsLinksOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3a78363ca5cc37fb34a1c98c52a719d30ee6fff99593de259d02be92eb6b8a02)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="href")
    def href(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "href"))

    @builtins.property
    @jsii.member(jsii_name="rel")
    def rel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rel"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainGeographicMapsLinks]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainGeographicMapsLinks]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainGeographicMapsLinks]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35807f4af5ae737d900d2e293dd57b85faab264c7d27ca69f639ed8315f79a0f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiGtmDomainGeographicMapsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainGeographicMapsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__988f78bf4b52c3878b15de87209d40501f6088463d49847ca5bb617cb496c259)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiGtmDomainGeographicMapsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f84608cd2218dc507bea5ab0d58d7090c223c7362f2f6632e8e4aa829afd8394)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiGtmDomainGeographicMapsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c800bdacfca73b059a03fd82f58efc9e16336fc9ecea7eba1976d96e4fef152a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4e821d5143880b148765d655956b09da931e9207ab12bd8a6255f0ce3708edd1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d4d7aa51b5ccf675f7709cc67946df3c8dc4234b94c420197c3155b62c2e14c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainGeographicMaps]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainGeographicMaps]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainGeographicMaps]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__478622864ab4b4693885667502417d192576cb8200c28e80c959b283544b92e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiGtmDomainGeographicMapsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainGeographicMapsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c63ecf4c6087e1c9c90aa77e5a72cfbad5375bb482f9bed1d3e9e1c6253a2cbd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAssignments")
    def put_assignments(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainGeographicMapsAssignments, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a08caf62ed4dd36e6d25de847dcfaec223b111038c35cfb2ceff56b05dea0769)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAssignments", [value]))

    @jsii.member(jsii_name="putLinks")
    def put_links(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainGeographicMapsLinks, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ecdfad811262af7f38cd5b3245f2c5e7d1acd2238066da7fb5bd52013de1305)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLinks", [value]))

    @jsii.member(jsii_name="resetAssignments")
    def reset_assignments(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssignments", []))

    @jsii.member(jsii_name="resetLinks")
    def reset_links(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinks", []))

    @builtins.property
    @jsii.member(jsii_name="assignments")
    def assignments(self) -> DataAkamaiGtmDomainGeographicMapsAssignmentsList:
        return typing.cast(DataAkamaiGtmDomainGeographicMapsAssignmentsList, jsii.get(self, "assignments"))

    @builtins.property
    @jsii.member(jsii_name="defaultDatacenter")
    def default_datacenter(
        self,
    ) -> DataAkamaiGtmDomainGeographicMapsDefaultDatacenterOutputReference:
        return typing.cast(DataAkamaiGtmDomainGeographicMapsDefaultDatacenterOutputReference, jsii.get(self, "defaultDatacenter"))

    @builtins.property
    @jsii.member(jsii_name="links")
    def links(self) -> DataAkamaiGtmDomainGeographicMapsLinksList:
        return typing.cast(DataAkamaiGtmDomainGeographicMapsLinksList, jsii.get(self, "links"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="assignmentsInput")
    def assignments_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainGeographicMapsAssignments]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainGeographicMapsAssignments]]], jsii.get(self, "assignmentsInput"))

    @builtins.property
    @jsii.member(jsii_name="linksInput")
    def links_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainGeographicMapsLinks]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainGeographicMapsLinks]]], jsii.get(self, "linksInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainGeographicMaps]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainGeographicMaps]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainGeographicMaps]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da63413184520d3ea13b54e74a09794431d2b4b7d1de64c27549bde1c727f883)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainLinks",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiGtmDomainLinks:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiGtmDomainLinks(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiGtmDomainLinksList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainLinksList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c31d5cf2f0ff69210125527fb641786f570764149e2970f36863e08776247600)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DataAkamaiGtmDomainLinksOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11d546688afe77c948aec5a28d4d7d831d15dd17edc3742fa5a520f3fcf6106e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiGtmDomainLinksOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bfa75255d309e514a185855ba43f932b3900dbf9c0b7e000d7a3cd21e177c04)
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
            type_hints = typing.get_type_hints(_typecheckingstub__68a2ab3e99a74b09903af54d49577c9f33a8fad86b20c5293eaf849d9e54a7c9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9920acb7862ebb7437c5afad57cedfb0951de77b0dc933f28f9de063eb533545)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainLinks]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainLinks]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainLinks]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c28c9059a3b4a8f9505ec5ac238fbac290c97ccabdd661a0ebd9a0aad71a80d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiGtmDomainLinksOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainLinksOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__32a45a736639d7013127b3c4d62f639fd493587d2d38ee700137c91c39d81322)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="href")
    def href(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "href"))

    @builtins.property
    @jsii.member(jsii_name="rel")
    def rel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rel"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainLinks]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainLinks]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainLinks]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__deed70c4f7496ebc130300afb21af89819da440566003d9efb3bfbfa03f55739)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainProperties",
    jsii_struct_bases=[],
    name_mapping={
        "links": "links",
        "liveness_tests": "livenessTests",
        "static_rr_sets": "staticRrSets",
        "traffic_targets": "trafficTargets",
    },
)
class DataAkamaiGtmDomainProperties:
    def __init__(
        self,
        *,
        links: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainPropertiesLinks", typing.Dict[builtins.str, typing.Any]]]]] = None,
        liveness_tests: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainPropertiesLivenessTests", typing.Dict[builtins.str, typing.Any]]]]] = None,
        static_rr_sets: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainPropertiesStaticRrSets", typing.Dict[builtins.str, typing.Any]]]]] = None,
        traffic_targets: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainPropertiesTrafficTargets", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param links: links block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#links DataAkamaiGtmDomain#links}
        :param liveness_tests: liveness_tests block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#liveness_tests DataAkamaiGtmDomain#liveness_tests}
        :param static_rr_sets: static_rr_sets block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#static_rr_sets DataAkamaiGtmDomain#static_rr_sets}
        :param traffic_targets: traffic_targets block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#traffic_targets DataAkamaiGtmDomain#traffic_targets}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bbb51ba39023fb923970bbd4bc6f89498c7694b24a7ca08ba7ad55e1920107d)
            check_type(argname="argument links", value=links, expected_type=type_hints["links"])
            check_type(argname="argument liveness_tests", value=liveness_tests, expected_type=type_hints["liveness_tests"])
            check_type(argname="argument static_rr_sets", value=static_rr_sets, expected_type=type_hints["static_rr_sets"])
            check_type(argname="argument traffic_targets", value=traffic_targets, expected_type=type_hints["traffic_targets"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if links is not None:
            self._values["links"] = links
        if liveness_tests is not None:
            self._values["liveness_tests"] = liveness_tests
        if static_rr_sets is not None:
            self._values["static_rr_sets"] = static_rr_sets
        if traffic_targets is not None:
            self._values["traffic_targets"] = traffic_targets

    @builtins.property
    def links(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainPropertiesLinks"]]]:
        '''links block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#links DataAkamaiGtmDomain#links}
        '''
        result = self._values.get("links")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainPropertiesLinks"]]], result)

    @builtins.property
    def liveness_tests(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainPropertiesLivenessTests"]]]:
        '''liveness_tests block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#liveness_tests DataAkamaiGtmDomain#liveness_tests}
        '''
        result = self._values.get("liveness_tests")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainPropertiesLivenessTests"]]], result)

    @builtins.property
    def static_rr_sets(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainPropertiesStaticRrSets"]]]:
        '''static_rr_sets block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#static_rr_sets DataAkamaiGtmDomain#static_rr_sets}
        '''
        result = self._values.get("static_rr_sets")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainPropertiesStaticRrSets"]]], result)

    @builtins.property
    def traffic_targets(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainPropertiesTrafficTargets"]]]:
        '''traffic_targets block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#traffic_targets DataAkamaiGtmDomain#traffic_targets}
        '''
        result = self._values.get("traffic_targets")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainPropertiesTrafficTargets"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiGtmDomainProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainPropertiesLinks",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiGtmDomainPropertiesLinks:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiGtmDomainPropertiesLinks(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiGtmDomainPropertiesLinksList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainPropertiesLinksList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__af2ab56e72e01f58267b023f05aa62e98386ed4bc2459fa271f26ef02c1f91f2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiGtmDomainPropertiesLinksOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b14141cd964dd13d5c1ad1283edaf2e5f77b9be0c7fae217ef514137a17bedb)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiGtmDomainPropertiesLinksOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00112e045e346929b4d9f1d094cb924c6dcdbc2f8c27493f7a66a864ca4ac847)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f9626356c056db986fdc85386000508ddda4474d5e4bfcf1745bebb2a7439b78)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9277fec70a15cee9ce4105b93e35153d35dc9b7f3f80ad99993c87bd8a36829a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainPropertiesLinks]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainPropertiesLinks]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainPropertiesLinks]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05bb7f30eb6954bec6a1b64cfd9f13a65650c8c3f3bf4b0e1a5a7c5431d92cc5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiGtmDomainPropertiesLinksOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainPropertiesLinksOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c19e048a13187842c2727eb43a9a78e4e7d482be34c47d4d3e28b2bb28b39a8c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="href")
    def href(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "href"))

    @builtins.property
    @jsii.member(jsii_name="rel")
    def rel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rel"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainPropertiesLinks]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainPropertiesLinks]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainPropertiesLinks]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba41ffb48bbd0f4a5e112b30e9b8e67d4361eb64c31d7b2c6a84067912490c7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiGtmDomainPropertiesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainPropertiesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__922b0285e652b4451565b527cce994c1deff27fa7bf1ed7a5dd521545b3ee035)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DataAkamaiGtmDomainPropertiesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bc5482810fd6974a58fc2be4630056067c191499b3efae2ea5afa15bc542908)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiGtmDomainPropertiesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22cbda29728dc31e4bbd4e4dca509fde065d5a893d393e60178b52079ffd75b7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f661787c14d064b4a77ea9e6b8f22a41d332ee5a857c34c2b1fda83249083f10)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bd62f726dfaa523a3a1865f856d971dc59477f3744dca34be3db2adea843e1bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainProperties]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainProperties]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainProperties]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfa3af1318b8f164550f5391850e0b94c25738192fe6e840e555d904924f666e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainPropertiesLivenessTests",
    jsii_struct_bases=[],
    name_mapping={"http_headers": "httpHeaders"},
)
class DataAkamaiGtmDomainPropertiesLivenessTests:
    def __init__(
        self,
        *,
        http_headers: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainPropertiesLivenessTestsHttpHeaders", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param http_headers: http_headers block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#http_headers DataAkamaiGtmDomain#http_headers}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f33141af781f4637231dae9f7d7eb24a31bf8d3ee829c232fa2e8b85c8fd2836)
            check_type(argname="argument http_headers", value=http_headers, expected_type=type_hints["http_headers"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if http_headers is not None:
            self._values["http_headers"] = http_headers

    @builtins.property
    def http_headers(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainPropertiesLivenessTestsHttpHeaders"]]]:
        '''http_headers block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#http_headers DataAkamaiGtmDomain#http_headers}
        '''
        result = self._values.get("http_headers")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainPropertiesLivenessTestsHttpHeaders"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiGtmDomainPropertiesLivenessTests(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainPropertiesLivenessTestsHttpHeaders",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiGtmDomainPropertiesLivenessTestsHttpHeaders:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiGtmDomainPropertiesLivenessTestsHttpHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiGtmDomainPropertiesLivenessTestsHttpHeadersList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainPropertiesLivenessTestsHttpHeadersList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ffa50cbb8bea00907a6aabdd650195591afdc719b4f2738730a9d2c50c74afcd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiGtmDomainPropertiesLivenessTestsHttpHeadersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d07acab8ee3509015ff9d62581f654e94396c6c82aa2c8cf7aad448d26f39030)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiGtmDomainPropertiesLivenessTestsHttpHeadersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aaa289cda490d44d3aef9dc8500378410f2d7a970c5a00497b90b01178b706ce)
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
            type_hints = typing.get_type_hints(_typecheckingstub__488a7b48687246791775b362d60108129eb64618a46be4468ffac920c84ae41f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0d22ac68a6fde5f543ce063de8330bdb8b81fe1a233b7e5b6fe3eb9db430a47a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainPropertiesLivenessTestsHttpHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainPropertiesLivenessTestsHttpHeaders]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainPropertiesLivenessTestsHttpHeaders]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3d62f7d1eb2d07f4d85ad7e0a330c614214919efdd87226aa8b550959fa233d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiGtmDomainPropertiesLivenessTestsHttpHeadersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainPropertiesLivenessTestsHttpHeadersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dfa9a1c9f17a7d229f3f039d179dccbf51073eaead1b350c6ca139270acefe3d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainPropertiesLivenessTestsHttpHeaders]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainPropertiesLivenessTestsHttpHeaders]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainPropertiesLivenessTestsHttpHeaders]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9990b601e5e816e65942d7c5d0436deb822d16b3c1fd463cc2438b5c7a2ce038)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiGtmDomainPropertiesLivenessTestsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainPropertiesLivenessTestsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__42b6f65bb933609e5f89e1de22f23fef2909a008478d94fe5ef935c350163829)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiGtmDomainPropertiesLivenessTestsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8502d5c482516738f6380b7a13baa3966ae8d163b720d49b5dcecb7e434d2b52)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiGtmDomainPropertiesLivenessTestsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d801603f5fd2a2ff6cb87c1394fcbe893152359afb4c5eb58f61cf87c117ba6a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2f68dbfecfab50a4bb276dad23bc22fdb20a909919f40b62cf3ba842d8790197)
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
            type_hints = typing.get_type_hints(_typecheckingstub__93259587b0c970d8f2083cf567bdee5bf8bebd24c851ab9830d772338e811c1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainPropertiesLivenessTests]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainPropertiesLivenessTests]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainPropertiesLivenessTests]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a6b374367a94799625e9b16ba7a117c5530c22b59ab726e851fd952ffd42288)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiGtmDomainPropertiesLivenessTestsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainPropertiesLivenessTestsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b51ef33c246c2c949de5180e856205e7cfdb3b0fc80b3a8c9813c1d2e694399a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putHttpHeaders")
    def put_http_headers(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainPropertiesLivenessTestsHttpHeaders, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3adb86a2805366417b68227f707c87137e077cf2bf520087bc72fa1a54368af2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHttpHeaders", [value]))

    @jsii.member(jsii_name="resetHttpHeaders")
    def reset_http_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpHeaders", []))

    @builtins.property
    @jsii.member(jsii_name="answersRequired")
    def answers_required(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "answersRequired"))

    @builtins.property
    @jsii.member(jsii_name="disabled")
    def disabled(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "disabled"))

    @builtins.property
    @jsii.member(jsii_name="disableNonstandardPortWarning")
    def disable_nonstandard_port_warning(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "disableNonstandardPortWarning"))

    @builtins.property
    @jsii.member(jsii_name="errorPenalty")
    def error_penalty(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "errorPenalty"))

    @builtins.property
    @jsii.member(jsii_name="httpError3Xx")
    def http_error3_xx(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "httpError3Xx"))

    @builtins.property
    @jsii.member(jsii_name="httpError4Xx")
    def http_error4_xx(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "httpError4Xx"))

    @builtins.property
    @jsii.member(jsii_name="httpError5Xx")
    def http_error5_xx(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "httpError5Xx"))

    @builtins.property
    @jsii.member(jsii_name="httpHeaders")
    def http_headers(self) -> DataAkamaiGtmDomainPropertiesLivenessTestsHttpHeadersList:
        return typing.cast(DataAkamaiGtmDomainPropertiesLivenessTestsHttpHeadersList, jsii.get(self, "httpHeaders"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="peerCertificateVerification")
    def peer_certificate_verification(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "peerCertificateVerification"))

    @builtins.property
    @jsii.member(jsii_name="recursionRequested")
    def recursion_requested(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "recursionRequested"))

    @builtins.property
    @jsii.member(jsii_name="requestString")
    def request_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "requestString"))

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @builtins.property
    @jsii.member(jsii_name="responseString")
    def response_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseString"))

    @builtins.property
    @jsii.member(jsii_name="sslClientCertificate")
    def ssl_client_certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslClientCertificate"))

    @builtins.property
    @jsii.member(jsii_name="sslClientPrivateKey")
    def ssl_client_private_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslClientPrivateKey"))

    @builtins.property
    @jsii.member(jsii_name="testInterval")
    def test_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "testInterval"))

    @builtins.property
    @jsii.member(jsii_name="testObject")
    def test_object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "testObject"))

    @builtins.property
    @jsii.member(jsii_name="testObjectPassword")
    def test_object_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "testObjectPassword"))

    @builtins.property
    @jsii.member(jsii_name="testObjectPort")
    def test_object_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "testObjectPort"))

    @builtins.property
    @jsii.member(jsii_name="testObjectProtocol")
    def test_object_protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "testObjectProtocol"))

    @builtins.property
    @jsii.member(jsii_name="testObjectUsername")
    def test_object_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "testObjectUsername"))

    @builtins.property
    @jsii.member(jsii_name="testTimeout")
    def test_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "testTimeout"))

    @builtins.property
    @jsii.member(jsii_name="timeoutPenalty")
    def timeout_penalty(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutPenalty"))

    @builtins.property
    @jsii.member(jsii_name="httpHeadersInput")
    def http_headers_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainPropertiesLivenessTestsHttpHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainPropertiesLivenessTestsHttpHeaders]]], jsii.get(self, "httpHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainPropertiesLivenessTests]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainPropertiesLivenessTests]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainPropertiesLivenessTests]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18b1c9c15e478d7b63103dfc8bbc11a1b40ed87ac93296ba8f4b41f158045119)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiGtmDomainPropertiesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainPropertiesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fe2c4a6405736453b2ffccad03d07d252b35321a87bc6c330ab173b8edc02cb6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putLinks")
    def put_links(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainPropertiesLinks, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17141713ad42db431fae10f5d53e6f63353ee43364eab0446a71699f66100d73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLinks", [value]))

    @jsii.member(jsii_name="putLivenessTests")
    def put_liveness_tests(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainPropertiesLivenessTests, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f424f3043969afd40b18cfc49dc6d726d1ceff17e02f13b3178066660c7ee7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLivenessTests", [value]))

    @jsii.member(jsii_name="putStaticRrSets")
    def put_static_rr_sets(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainPropertiesStaticRrSets", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81e631d4afe20d04f47ebd2c711dbb96e6c1acc3164b7dd64acaa4c79f89596b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStaticRrSets", [value]))

    @jsii.member(jsii_name="putTrafficTargets")
    def put_traffic_targets(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainPropertiesTrafficTargets", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ed630636f51ed2d8c98b9c222a03464bef138c9ef4aacdbf08f4af39d3a30c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTrafficTargets", [value]))

    @jsii.member(jsii_name="resetLinks")
    def reset_links(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinks", []))

    @jsii.member(jsii_name="resetLivenessTests")
    def reset_liveness_tests(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLivenessTests", []))

    @jsii.member(jsii_name="resetStaticRrSets")
    def reset_static_rr_sets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStaticRrSets", []))

    @jsii.member(jsii_name="resetTrafficTargets")
    def reset_traffic_targets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrafficTargets", []))

    @builtins.property
    @jsii.member(jsii_name="backupCname")
    def backup_cname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backupCname"))

    @builtins.property
    @jsii.member(jsii_name="backupIp")
    def backup_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backupIp"))

    @builtins.property
    @jsii.member(jsii_name="balanceByDownloadScore")
    def balance_by_download_score(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "balanceByDownloadScore"))

    @builtins.property
    @jsii.member(jsii_name="cname")
    def cname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cname"))

    @builtins.property
    @jsii.member(jsii_name="comments")
    def comments(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comments"))

    @builtins.property
    @jsii.member(jsii_name="dynamicTtl")
    def dynamic_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dynamicTtl"))

    @builtins.property
    @jsii.member(jsii_name="failbackDelay")
    def failback_delay(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "failbackDelay"))

    @builtins.property
    @jsii.member(jsii_name="failoverDelay")
    def failover_delay(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "failoverDelay"))

    @builtins.property
    @jsii.member(jsii_name="ghostDemandReporting")
    def ghost_demand_reporting(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "ghostDemandReporting"))

    @builtins.property
    @jsii.member(jsii_name="handoutLimit")
    def handout_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "handoutLimit"))

    @builtins.property
    @jsii.member(jsii_name="handoutMode")
    def handout_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "handoutMode"))

    @builtins.property
    @jsii.member(jsii_name="healthMax")
    def health_max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "healthMax"))

    @builtins.property
    @jsii.member(jsii_name="healthMultiplier")
    def health_multiplier(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "healthMultiplier"))

    @builtins.property
    @jsii.member(jsii_name="healthThreshold")
    def health_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "healthThreshold"))

    @builtins.property
    @jsii.member(jsii_name="ipv6")
    def ipv6(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "ipv6"))

    @builtins.property
    @jsii.member(jsii_name="lastModified")
    def last_modified(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastModified"))

    @builtins.property
    @jsii.member(jsii_name="links")
    def links(self) -> DataAkamaiGtmDomainPropertiesLinksList:
        return typing.cast(DataAkamaiGtmDomainPropertiesLinksList, jsii.get(self, "links"))

    @builtins.property
    @jsii.member(jsii_name="livenessTests")
    def liveness_tests(self) -> DataAkamaiGtmDomainPropertiesLivenessTestsList:
        return typing.cast(DataAkamaiGtmDomainPropertiesLivenessTestsList, jsii.get(self, "livenessTests"))

    @builtins.property
    @jsii.member(jsii_name="loadImbalancePercentage")
    def load_imbalance_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "loadImbalancePercentage"))

    @builtins.property
    @jsii.member(jsii_name="mapName")
    def map_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mapName"))

    @builtins.property
    @jsii.member(jsii_name="maxUnreachablePenalty")
    def max_unreachable_penalty(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxUnreachablePenalty"))

    @builtins.property
    @jsii.member(jsii_name="minLiveFraction")
    def min_live_fraction(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minLiveFraction"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="scoreAggregationType")
    def score_aggregation_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scoreAggregationType"))

    @builtins.property
    @jsii.member(jsii_name="staticRrSets")
    def static_rr_sets(self) -> "DataAkamaiGtmDomainPropertiesStaticRrSetsList":
        return typing.cast("DataAkamaiGtmDomainPropertiesStaticRrSetsList", jsii.get(self, "staticRrSets"))

    @builtins.property
    @jsii.member(jsii_name="staticTtl")
    def static_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "staticTtl"))

    @builtins.property
    @jsii.member(jsii_name="sticknessBonusConstant")
    def stickness_bonus_constant(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sticknessBonusConstant"))

    @builtins.property
    @jsii.member(jsii_name="sticknessBonusPercentage")
    def stickness_bonus_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sticknessBonusPercentage"))

    @builtins.property
    @jsii.member(jsii_name="trafficTargets")
    def traffic_targets(self) -> "DataAkamaiGtmDomainPropertiesTrafficTargetsList":
        return typing.cast("DataAkamaiGtmDomainPropertiesTrafficTargetsList", jsii.get(self, "trafficTargets"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="unreachableThreshold")
    def unreachable_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "unreachableThreshold"))

    @builtins.property
    @jsii.member(jsii_name="useComputedTargets")
    def use_computed_targets(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "useComputedTargets"))

    @builtins.property
    @jsii.member(jsii_name="weightedHashBitsForIpv4")
    def weighted_hash_bits_for_ipv4(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weightedHashBitsForIpv4"))

    @builtins.property
    @jsii.member(jsii_name="weightedHashBitsForIpv6")
    def weighted_hash_bits_for_ipv6(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weightedHashBitsForIpv6"))

    @builtins.property
    @jsii.member(jsii_name="linksInput")
    def links_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainPropertiesLinks]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainPropertiesLinks]]], jsii.get(self, "linksInput"))

    @builtins.property
    @jsii.member(jsii_name="livenessTestsInput")
    def liveness_tests_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainPropertiesLivenessTests]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainPropertiesLivenessTests]]], jsii.get(self, "livenessTestsInput"))

    @builtins.property
    @jsii.member(jsii_name="staticRrSetsInput")
    def static_rr_sets_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainPropertiesStaticRrSets"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainPropertiesStaticRrSets"]]], jsii.get(self, "staticRrSetsInput"))

    @builtins.property
    @jsii.member(jsii_name="trafficTargetsInput")
    def traffic_targets_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainPropertiesTrafficTargets"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainPropertiesTrafficTargets"]]], jsii.get(self, "trafficTargetsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainProperties]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainProperties]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainProperties]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6950b0ef605d19748c5ab53fe236cb8aaa61ec2c2963dee7d384bfef15d0ecef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainPropertiesStaticRrSets",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiGtmDomainPropertiesStaticRrSets:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiGtmDomainPropertiesStaticRrSets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiGtmDomainPropertiesStaticRrSetsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainPropertiesStaticRrSetsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5abad77a74da6825c81c9cb016a0736515fc65543f7697b12f7863cc0f08c1f7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiGtmDomainPropertiesStaticRrSetsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7611b9549816707c57e6c0194f303725b929cdd130f9683a70b71ee6ef5ad5fc)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiGtmDomainPropertiesStaticRrSetsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d76f0a0f8be321e85501528065b5f3c3412b68707ef260cb7bd7a26012c9a88)
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
            type_hints = typing.get_type_hints(_typecheckingstub__89ace75c51bf79a76c36a4d6137efe0f03fe92c87c62cc112e94c79bf2475cf9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__78ab1fa998bc5e7538316a88a0d27e7b6f9ef88ad71dc9388ba777104789bb9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainPropertiesStaticRrSets]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainPropertiesStaticRrSets]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainPropertiesStaticRrSets]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3aa6a2919cd76d4e8650538852a406922a62fbfc0ea3dcf9135bb025adb5a96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiGtmDomainPropertiesStaticRrSetsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainPropertiesStaticRrSetsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8d51a256fbb92a00a404bd04cf2f76607d25c485de8bf2c6b8eb20f8bc261778)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="rdata")
    def rdata(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "rdata"))

    @builtins.property
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ttl"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainPropertiesStaticRrSets]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainPropertiesStaticRrSets]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainPropertiesStaticRrSets]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae34d41cfcd2b18d2175e522b88a519bc080bda1edd3e868459c32539e5930f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainPropertiesTrafficTargets",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiGtmDomainPropertiesTrafficTargets:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiGtmDomainPropertiesTrafficTargets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiGtmDomainPropertiesTrafficTargetsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainPropertiesTrafficTargetsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ebc8052c227f5b7c1f53c75519ccd20a6716979c5f0be2831b06a11098b3e108)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiGtmDomainPropertiesTrafficTargetsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f5d331af2cd33bf41266a26d8d073c79b3c040df7166d1a6313d3eec5862ef6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiGtmDomainPropertiesTrafficTargetsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a9d86090814975068cd35bfb14964dbc1b9553a2aac0d0bd9c9c71de408ea1b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__aec1099e7d73cecc275cf6447ef11a40e68fbd45f2e0bba22b70eb6946446481)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0d9d38dead3397121f6d1102ea6a562036f7ab96706dbfac1f18ca55f092e09f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainPropertiesTrafficTargets]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainPropertiesTrafficTargets]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainPropertiesTrafficTargets]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d166dda905f6d53af5c24ca1cabd590dbaf10aeec210dffe21d38ca7836d90df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiGtmDomainPropertiesTrafficTargetsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainPropertiesTrafficTargetsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__60bf05bb1fe48b3fb91b2794ec3fbb28254ea29c15fa9a505f73db36c8785dd5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="datacenterId")
    def datacenter_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "datacenterId"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "enabled"))

    @builtins.property
    @jsii.member(jsii_name="handoutCname")
    def handout_cname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "handoutCname"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="servers")
    def servers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "servers"))

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weight"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainPropertiesTrafficTargets]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainPropertiesTrafficTargets]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainPropertiesTrafficTargets]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17b4d3127877583ad30cda615dae4c250d54667c74bb829ecce7fdf15116d3e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainResources",
    jsii_struct_bases=[],
    name_mapping={"links": "links", "resource_instances": "resourceInstances"},
)
class DataAkamaiGtmDomainResources:
    def __init__(
        self,
        *,
        links: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainResourcesLinks", typing.Dict[builtins.str, typing.Any]]]]] = None,
        resource_instances: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainResourcesResourceInstances", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param links: links block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#links DataAkamaiGtmDomain#links}
        :param resource_instances: resource_instances block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#resource_instances DataAkamaiGtmDomain#resource_instances}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c71b0383f6800aababfde64e2a55936dcb5f0b91837e62dc65753f0c46100d1)
            check_type(argname="argument links", value=links, expected_type=type_hints["links"])
            check_type(argname="argument resource_instances", value=resource_instances, expected_type=type_hints["resource_instances"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if links is not None:
            self._values["links"] = links
        if resource_instances is not None:
            self._values["resource_instances"] = resource_instances

    @builtins.property
    def links(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainResourcesLinks"]]]:
        '''links block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#links DataAkamaiGtmDomain#links}
        '''
        result = self._values.get("links")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainResourcesLinks"]]], result)

    @builtins.property
    def resource_instances(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainResourcesResourceInstances"]]]:
        '''resource_instances block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#resource_instances DataAkamaiGtmDomain#resource_instances}
        '''
        result = self._values.get("resource_instances")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainResourcesResourceInstances"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiGtmDomainResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainResourcesLinks",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiGtmDomainResourcesLinks:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiGtmDomainResourcesLinks(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiGtmDomainResourcesLinksList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainResourcesLinksList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b967a66418bc9d5576d9acb0fe2ddd8a4ab0a6e1086d817ecb77ea44e0cb9c44)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiGtmDomainResourcesLinksOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa89bd40791c758b4e7940a9919a11ad3de13fe7d63a797953cdd292a371ef80)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiGtmDomainResourcesLinksOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__682fa59f2b0701a76cadb09b380525d929b205e0af071d99abc9c73de4d6465c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__df27b9fbd3d836d8ee6c168d1be0bd1f56581981d9f58440eb9ad3c269824d55)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dc4740029b19c39b7b237b3b1ae5eb55845327fecd34dd9d176c1fec224f0a37)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainResourcesLinks]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainResourcesLinks]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainResourcesLinks]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4469b93f1207e78f004aa56f574c61f1bda3481dc6ca783d232ed62efd8064f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiGtmDomainResourcesLinksOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainResourcesLinksOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e685fdd510d68b7b44fc2e9134a9bdefbbf39f16d36560414de4659451df3028)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="href")
    def href(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "href"))

    @builtins.property
    @jsii.member(jsii_name="rel")
    def rel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rel"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainResourcesLinks]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainResourcesLinks]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainResourcesLinks]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a494de091df0e01d1587f5b936169340392451f1ffb186ef216b66a3f2d1d604)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiGtmDomainResourcesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainResourcesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__de296f5f40c79d4d35b3f06cba975d66e8c0117ea3cc3753fe7a8d7df66e53c3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DataAkamaiGtmDomainResourcesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b827ec25fac82c363c9cfc998ba45ccd291f7f47c9eafc85852ae84518efbdc8)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiGtmDomainResourcesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94bbceb50926812b8e42930deb031b311462e57c58ca9053fa046c431a3fce00)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5e8be1ec8ee9639777daefe0304f6552150bdfac8f8e27eb31cb4fa6fbcce0b1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3c6049ca96b45c79039e0afc860c42de7c550bf21524589dafdd28fd3e302854)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainResources]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainResources]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainResources]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95e5784cc43ff030d19a8eec9c41f744a674d964440c9257b8be3373e55a061e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiGtmDomainResourcesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainResourcesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__29d12af921eba97e4c69ac4191164fd7c50d5589f738f2fbd69660689686271a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putLinks")
    def put_links(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainResourcesLinks, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d44b36441197303138be5b21fd961cd1e4ca34f1bc645ac25676ac078ca05497)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLinks", [value]))

    @jsii.member(jsii_name="putResourceInstances")
    def put_resource_instances(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainResourcesResourceInstances", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92838c56dc22a49ef7a964f290a1c562348647061e6ee6468f8ba962e484eeb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putResourceInstances", [value]))

    @jsii.member(jsii_name="resetLinks")
    def reset_links(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinks", []))

    @jsii.member(jsii_name="resetResourceInstances")
    def reset_resource_instances(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceInstances", []))

    @builtins.property
    @jsii.member(jsii_name="aggregationType")
    def aggregation_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aggregationType"))

    @builtins.property
    @jsii.member(jsii_name="constrainedProperty")
    def constrained_property(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "constrainedProperty"))

    @builtins.property
    @jsii.member(jsii_name="decayRate")
    def decay_rate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "decayRate"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="hostHeader")
    def host_header(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostHeader"))

    @builtins.property
    @jsii.member(jsii_name="leaderString")
    def leader_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "leaderString"))

    @builtins.property
    @jsii.member(jsii_name="leastSquaresDecay")
    def least_squares_decay(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "leastSquaresDecay"))

    @builtins.property
    @jsii.member(jsii_name="links")
    def links(self) -> DataAkamaiGtmDomainResourcesLinksList:
        return typing.cast(DataAkamaiGtmDomainResourcesLinksList, jsii.get(self, "links"))

    @builtins.property
    @jsii.member(jsii_name="loadImbalancePercentage")
    def load_imbalance_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "loadImbalancePercentage"))

    @builtins.property
    @jsii.member(jsii_name="maxUMultiplicativeIncrement")
    def max_u_multiplicative_increment(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxUMultiplicativeIncrement"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="resourceInstances")
    def resource_instances(self) -> "DataAkamaiGtmDomainResourcesResourceInstancesList":
        return typing.cast("DataAkamaiGtmDomainResourcesResourceInstancesList", jsii.get(self, "resourceInstances"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="upperBound")
    def upper_bound(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "upperBound"))

    @builtins.property
    @jsii.member(jsii_name="linksInput")
    def links_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainResourcesLinks]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainResourcesLinks]]], jsii.get(self, "linksInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceInstancesInput")
    def resource_instances_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainResourcesResourceInstances"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainResourcesResourceInstances"]]], jsii.get(self, "resourceInstancesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainResources]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainResources]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainResources]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3411a0a002fddcf4b46da356e865eabc7cb589d526b44ba65d747a1920dbb95c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainResourcesResourceInstances",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiGtmDomainResourcesResourceInstances:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiGtmDomainResourcesResourceInstances(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiGtmDomainResourcesResourceInstancesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainResourcesResourceInstancesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__45e917e097aa8937a689f07600d12bc3c38f4d7e566e7a66e53161d756b841f8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiGtmDomainResourcesResourceInstancesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e8b9beaaeee661e7698f3895c7e8bf3a6afd1222e1043c29b090405eb9063eb)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiGtmDomainResourcesResourceInstancesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7113f5f90a08550fc9ea8f5de229f3a16bcfa35ca899892fe2343b3d23012df)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fcba008fc9d19f03435351636f516ebb7c9f6b2bf17bac9520573c7678d28420)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ed385236fd96d1d079d95d24cbf0a29cd417fb23e295012bb63b22c88c2107bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainResourcesResourceInstances]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainResourcesResourceInstances]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainResourcesResourceInstances]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8345d39a5824b2199a3a25d63f187a67e8fe78c6c27028f12e3e27612ce86640)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiGtmDomainResourcesResourceInstancesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainResourcesResourceInstancesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5cbe32863780da478432e46db19392c021fb49e4f446c5421d249131df5f79bc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="datacenterId")
    def datacenter_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "datacenterId"))

    @builtins.property
    @jsii.member(jsii_name="loadObject")
    def load_object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loadObject"))

    @builtins.property
    @jsii.member(jsii_name="loadObjectPort")
    def load_object_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "loadObjectPort"))

    @builtins.property
    @jsii.member(jsii_name="loadServers")
    def load_servers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "loadServers"))

    @builtins.property
    @jsii.member(jsii_name="useDefaultLoadObject")
    def use_default_load_object(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "useDefaultLoadObject"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainResourcesResourceInstances]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainResourcesResourceInstances]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainResourcesResourceInstances]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5baa5631da0120da91ea07380a5d02a7e27146e323ef8a0989564dfb105b3d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainStatus",
    jsii_struct_bases=[],
    name_mapping={"links": "links"},
)
class DataAkamaiGtmDomainStatus:
    def __init__(
        self,
        *,
        links: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiGtmDomainStatusLinks", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param links: links block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#links DataAkamaiGtmDomain#links}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06dea4992fecf92e80cdf73b9fcae078248872171991664a80282e555379770b)
            check_type(argname="argument links", value=links, expected_type=type_hints["links"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if links is not None:
            self._values["links"] = links

    @builtins.property
    def links(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainStatusLinks"]]]:
        '''links block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/gtm_domain#links DataAkamaiGtmDomain#links}
        '''
        result = self._values.get("links")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiGtmDomainStatusLinks"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiGtmDomainStatus(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainStatusLinks",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiGtmDomainStatusLinks:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiGtmDomainStatusLinks(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiGtmDomainStatusLinksList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainStatusLinksList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fdf03d4f71f27c74e5154bcee46ccaa954ce231c9c6dd6366a606b31de22e2bb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiGtmDomainStatusLinksOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab537c3d4493e33717de78ae437db96a3bc15fbe0c96732138acc1ec6e8bfec5)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiGtmDomainStatusLinksOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94c4cbdb4b07ac83423955252b1333febbe1250971e021bb65598af81519552c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f016b1560f188993d2f8e289e9058fc6d0a8c415dfbae0aedacab23c21447617)
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
            type_hints = typing.get_type_hints(_typecheckingstub__721d428366ce3bbb17d3c4cba3ee1eadfa5fb07f16a324e105cdb6585069edb9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainStatusLinks]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainStatusLinks]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainStatusLinks]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5688bcee2d8aaa41de84660f92222638bda2d887f70b1bfc1c08197e7675490e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiGtmDomainStatusLinksOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainStatusLinksOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a8e3a3089eea5e626b16007e56a1e84e2502f48da1840ed87f0294c2ab3578a6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="href")
    def href(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "href"))

    @builtins.property
    @jsii.member(jsii_name="rel")
    def rel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rel"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainStatusLinks]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainStatusLinks]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainStatusLinks]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__159319c4fbe4520cb0121e5e998017b8d930dbd83abbc34512a516b248f604cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiGtmDomainStatusOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiGtmDomain.DataAkamaiGtmDomainStatusOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__78ca1310040b9ff848d849320695052c79478dcce0192789edf524c0a0fa33bf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLinks")
    def put_links(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainStatusLinks, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__200a72dd4db9f9019df8663f219c32885875847462708157dce4209fd34a68ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLinks", [value]))

    @jsii.member(jsii_name="resetLinks")
    def reset_links(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinks", []))

    @builtins.property
    @jsii.member(jsii_name="changeId")
    def change_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "changeId"))

    @builtins.property
    @jsii.member(jsii_name="links")
    def links(self) -> DataAkamaiGtmDomainStatusLinksList:
        return typing.cast(DataAkamaiGtmDomainStatusLinksList, jsii.get(self, "links"))

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "message"))

    @builtins.property
    @jsii.member(jsii_name="passingValidation")
    def passing_validation(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "passingValidation"))

    @builtins.property
    @jsii.member(jsii_name="propagationStatus")
    def propagation_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "propagationStatus"))

    @builtins.property
    @jsii.member(jsii_name="propagationStatusDate")
    def propagation_status_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "propagationStatusDate"))

    @builtins.property
    @jsii.member(jsii_name="linksInput")
    def links_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainStatusLinks]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainStatusLinks]]], jsii.get(self, "linksInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainStatus]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainStatus]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainStatus]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74808c3a663ceb1189d12cddd2bf5de3d3924e11d5e54e4afe3f1185b6275a8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataAkamaiGtmDomain",
    "DataAkamaiGtmDomainAsMaps",
    "DataAkamaiGtmDomainAsMapsAssignments",
    "DataAkamaiGtmDomainAsMapsAssignmentsList",
    "DataAkamaiGtmDomainAsMapsAssignmentsOutputReference",
    "DataAkamaiGtmDomainAsMapsDefaultDatacenter",
    "DataAkamaiGtmDomainAsMapsDefaultDatacenterOutputReference",
    "DataAkamaiGtmDomainAsMapsLinks",
    "DataAkamaiGtmDomainAsMapsLinksList",
    "DataAkamaiGtmDomainAsMapsLinksOutputReference",
    "DataAkamaiGtmDomainAsMapsList",
    "DataAkamaiGtmDomainAsMapsOutputReference",
    "DataAkamaiGtmDomainCidrMaps",
    "DataAkamaiGtmDomainCidrMapsAssignments",
    "DataAkamaiGtmDomainCidrMapsAssignmentsList",
    "DataAkamaiGtmDomainCidrMapsAssignmentsOutputReference",
    "DataAkamaiGtmDomainCidrMapsDefaultDatacenter",
    "DataAkamaiGtmDomainCidrMapsDefaultDatacenterOutputReference",
    "DataAkamaiGtmDomainCidrMapsLinks",
    "DataAkamaiGtmDomainCidrMapsLinksList",
    "DataAkamaiGtmDomainCidrMapsLinksOutputReference",
    "DataAkamaiGtmDomainCidrMapsList",
    "DataAkamaiGtmDomainCidrMapsOutputReference",
    "DataAkamaiGtmDomainConfig",
    "DataAkamaiGtmDomainDatacenters",
    "DataAkamaiGtmDomainDatacentersDefaultLoadObject",
    "DataAkamaiGtmDomainDatacentersDefaultLoadObjectList",
    "DataAkamaiGtmDomainDatacentersDefaultLoadObjectOutputReference",
    "DataAkamaiGtmDomainDatacentersLinks",
    "DataAkamaiGtmDomainDatacentersLinksList",
    "DataAkamaiGtmDomainDatacentersLinksOutputReference",
    "DataAkamaiGtmDomainDatacentersList",
    "DataAkamaiGtmDomainDatacentersOutputReference",
    "DataAkamaiGtmDomainGeographicMaps",
    "DataAkamaiGtmDomainGeographicMapsAssignments",
    "DataAkamaiGtmDomainGeographicMapsAssignmentsList",
    "DataAkamaiGtmDomainGeographicMapsAssignmentsOutputReference",
    "DataAkamaiGtmDomainGeographicMapsDefaultDatacenter",
    "DataAkamaiGtmDomainGeographicMapsDefaultDatacenterOutputReference",
    "DataAkamaiGtmDomainGeographicMapsLinks",
    "DataAkamaiGtmDomainGeographicMapsLinksList",
    "DataAkamaiGtmDomainGeographicMapsLinksOutputReference",
    "DataAkamaiGtmDomainGeographicMapsList",
    "DataAkamaiGtmDomainGeographicMapsOutputReference",
    "DataAkamaiGtmDomainLinks",
    "DataAkamaiGtmDomainLinksList",
    "DataAkamaiGtmDomainLinksOutputReference",
    "DataAkamaiGtmDomainProperties",
    "DataAkamaiGtmDomainPropertiesLinks",
    "DataAkamaiGtmDomainPropertiesLinksList",
    "DataAkamaiGtmDomainPropertiesLinksOutputReference",
    "DataAkamaiGtmDomainPropertiesList",
    "DataAkamaiGtmDomainPropertiesLivenessTests",
    "DataAkamaiGtmDomainPropertiesLivenessTestsHttpHeaders",
    "DataAkamaiGtmDomainPropertiesLivenessTestsHttpHeadersList",
    "DataAkamaiGtmDomainPropertiesLivenessTestsHttpHeadersOutputReference",
    "DataAkamaiGtmDomainPropertiesLivenessTestsList",
    "DataAkamaiGtmDomainPropertiesLivenessTestsOutputReference",
    "DataAkamaiGtmDomainPropertiesOutputReference",
    "DataAkamaiGtmDomainPropertiesStaticRrSets",
    "DataAkamaiGtmDomainPropertiesStaticRrSetsList",
    "DataAkamaiGtmDomainPropertiesStaticRrSetsOutputReference",
    "DataAkamaiGtmDomainPropertiesTrafficTargets",
    "DataAkamaiGtmDomainPropertiesTrafficTargetsList",
    "DataAkamaiGtmDomainPropertiesTrafficTargetsOutputReference",
    "DataAkamaiGtmDomainResources",
    "DataAkamaiGtmDomainResourcesLinks",
    "DataAkamaiGtmDomainResourcesLinksList",
    "DataAkamaiGtmDomainResourcesLinksOutputReference",
    "DataAkamaiGtmDomainResourcesList",
    "DataAkamaiGtmDomainResourcesOutputReference",
    "DataAkamaiGtmDomainResourcesResourceInstances",
    "DataAkamaiGtmDomainResourcesResourceInstancesList",
    "DataAkamaiGtmDomainResourcesResourceInstancesOutputReference",
    "DataAkamaiGtmDomainStatus",
    "DataAkamaiGtmDomainStatusLinks",
    "DataAkamaiGtmDomainStatusLinksList",
    "DataAkamaiGtmDomainStatusLinksOutputReference",
    "DataAkamaiGtmDomainStatusOutputReference",
]

publication.publish()

def _typecheckingstub__cc99b076fa668ce0302c478187128723057998556f055572f4e3c069de44c375(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    as_maps: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainAsMaps, typing.Dict[builtins.str, typing.Any]]]]] = None,
    cidr_maps: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainCidrMaps, typing.Dict[builtins.str, typing.Any]]]]] = None,
    datacenters: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainDatacenters, typing.Dict[builtins.str, typing.Any]]]]] = None,
    geographic_maps: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainGeographicMaps, typing.Dict[builtins.str, typing.Any]]]]] = None,
    links: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainLinks, typing.Dict[builtins.str, typing.Any]]]]] = None,
    properties: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainProperties, typing.Dict[builtins.str, typing.Any]]]]] = None,
    resources: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainResources, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__a31327bc46ec10aff34f8b648337da6e9c72f763a7ffb81126890d0adf365fb7(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7961ef7617f01a85ff53ff90dcea60ec687e19997b82226d7a8285c9d433f97(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainAsMaps, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a26ab55124363dbcf8374664ef345912f1e3222501d2f007577c3f9fc9d9703f(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainCidrMaps, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7eca313ad4bdd1a9ebb532e5f15992efa9a19fd75c1fd52b5568d9ff1121a07(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainDatacenters, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c99ba84c69ec8a7c657806d34ab46a20bf9f9c8214b3de579e305d24b41e2389(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainGeographicMaps, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f10d1d768cde6f7bb2b032b0f7e0d4877ce1e2eb9c6d40059d31522badfd45aa(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainLinks, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f62edf5cf8300402c294841fd730738557d72a1a2f8fa04c4159533cbc7f1a2(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainProperties, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd6849bc1768e76d8c168d649401647de6d7b06ec11ba90ffc00c74c2e125a6b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainResources, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af6d5339d333720882a806c2b83bd4d9aa8e74ec0418c756b0f088a80f190c53(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__117dae3a40c054eefa18efd0dd88f00ad359648d01c11619db4b36e45b8b2e48(
    *,
    assignments: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainAsMapsAssignments, typing.Dict[builtins.str, typing.Any]]]]] = None,
    links: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainAsMapsLinks, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f1dcd6bcfd9b9a86da619cd0251003fad21c40586719f2dce5d8dffbd02fd30(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2c31d25363903edf3e43d1fcf43086ad029cd24f774322270a81bc748eb25c7(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cab25170fc30e3a97c17e256246861ef114b7b9e26b3f200a89352d6e94b652f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4c866fffa513bb3a9294e01a772cd3c3fbfb220678e3a98a44843e80731a5b6(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb7230d2d76e13756f5a0fef84cd71157203ca3a4f500fbcd5f0454179bc3a2a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c6483b68879ec38928a7d41f6213d1080f21d7d4008a93039a522142968a7f0(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainAsMapsAssignments]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a46d7157378d024a8efb72a59e69188408897bbb5b9806c9e280046f43de6e4f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfd9fad3bfedaaab8a56c70bdc7f9e4ca61ac3c5339eb2b4f97c92f1d1d515f5(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainAsMapsAssignments]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ff644c1bc4ac53266f5e3c9f77a04a47c8b29ea7d93d28f4b5a66da865148ca(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d2cf23da11015885e9820d16133f9dba68072f415780deb77345e7ceec12d0b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainAsMapsDefaultDatacenter]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7eeb55c1766ec4994028d49b21f5c8496770cf5eba48d4fefb8d95ece8acc27(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3a22de048bde43cb4e81ae9d13f7e061c7a958c323227571d251789e841ba21(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15a03b6fecbc756f2dbd5ffa1179aeffca9eca052601da43945782c3d085b25f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f94e8a3986035f6c1c50c18fbd33130c96c6e8abe8a453f2f1870d0648f5693(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b55406fcc325dbfa569afac38dc98d72e8ebbf8462346ce25278df33c3958d71(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d91391615e040ea22d1ea6c4f2aeb565f73ff18e10972c70946130a497e7c916(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainAsMapsLinks]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ee67eb20e32d3638733d7ae75f2e3316b13d4bf08dfeec998fd5d046229c7d6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__932edcc7ae400af27fed64c39f27fb06984afdcd1f9bfc4c15ba154fc9136702(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainAsMapsLinks]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a06aca9322b9665923d8d1716abdde7ec706d729b0bcc245a4c68a0eb8c4bf2a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__506c3b14246b23dbfd05342cfd3f5267121cb9f2fceb34ce6b15fa9d0ba00a88(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c0f1fe368db5f4519d429b14e6f032e07dde47cb234fb288eb6c3b568170208(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2da84afd3535387fed938ae3178cc43d934842392972d6478fbcc404a6a9a14(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__633dde1f522fc81048d14348edd4cd09eedda0a42aaca07bef8b22c664f52a79(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b53e5c16e693cce125406d85cb5769d8d208513fa5cd200007fb699abc22b6db(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainAsMaps]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e0b813c9d179717290463b4585995946b592a9072f4b9d7c34f4161c68cb3a1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f307c5d420b1aa3225bacabdcd10a68a0b3722bb80b04c937ec459f1035f3cb(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainAsMapsAssignments, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c53d538e41fde4bcdf940dd75937b9974ffb7de4f19286f8caab99cf4c30235(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainAsMapsLinks, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d6e69afc79b9114469f100d59f91cff68f91897fc9a341ca3e87b1dc2e3f4ee(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainAsMaps]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c35f3cef77edb09a9d64773bae3e47f9836f5e45102d671044fd6d68f0b59711(
    *,
    assignments: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainCidrMapsAssignments, typing.Dict[builtins.str, typing.Any]]]]] = None,
    links: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainCidrMapsLinks, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__660e83c0a7f9c299354d4b1a7a7423ab918a0d0dce0fad67db3b63f608056cc2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1ccfcc8cea5f706d96a1e8b3ed2c695f32b662cb7f6d507a00d50fd6ce9537c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51d3ba59610302fa2d82f3085ded03fc1a07479c9c83077ce0ee4e5eeb590c2f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b97aa01fc09980746e76086be4752091f756ac9651d467e72abab60e6a1f0a89(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da5af43edbc77bf60c372c9681964271572716b0151b6c4e5919e396f89e1470(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39901a5d37e182c2bb9792ea9ef2030545354c3f38b5ba90b1a1e150caea4248(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainCidrMapsAssignments]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__471f816db77cc152e999c48034a2187ebee7aef0aab74e8287d2cee4f060bfe7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da9a49f246d6db6d88a91fa6ea1a7fdc70cdbfc54217aa230cb18e21e1cd1575(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainCidrMapsAssignments]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2202be0848a69f28b3b741bb7b4c8fac81fa93aeca9d5c4bcd50009fd24df84(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2043831eb13861b5a77153750a3803336f95e00fe16b016c33dcb323f31385e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainCidrMapsDefaultDatacenter]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c1115a74c4e3904e1e2d97219218d61b89ac281f8cf8ece76d5855b95c0bfa2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5d4834f083c414cbe0f53616b8ada7aef99f32e834c7d5095453cf5da8f6c6e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9375a1356441d0ba5737f0cad363726b720050acec9d01b8c3e0a9fa67506bcb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4362e30d07b0aba0f43bd2a05a907bf20e9d262c12adee67fc968c0d0a1a885(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f46b4a3d11e136578998404cc35dce6eacf7c2e33a4971a59c3cac72e65e4659(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cb6692cdeafb1f44faec0da21294140d885f0800646a8b16833e35f3bb9d48e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainCidrMapsLinks]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70f1d8923917abdc90c85223a7fdd8fd463915b696fc7c27858f7e6e144b4778(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9676a820d90a622246364a01450039345f208503e8b39023a74c9b2285c54cef(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainCidrMapsLinks]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__872965da83f92521ad6ff3663c69a6968ad6d7966dc418857801167ffe6cd5b6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcd7c97b0945d706eda069f12b1e964542975efa3be0384acee605220a25a875(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2a99532567ee594d0effa0fac0ab3eed4529345daac90f7f206ef19e0a9af8b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6461dc73ae25b1fac533ba41be0ee3bf4e3587cc1dba2adfe32766576d433e0f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d9a8163c6b6906a5c8d446333baf80a9932ccfb3f62c41dd9a1d1f261e6454d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d65e96c6114635a0fbb3aad868e7280b42ba6de9bcf4ce82ad7c54cee5bff75(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainCidrMaps]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f598a9a051eed6f11c85bc43a0b31a49265c7d92e5096299a50a13e2abd2bd90(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4ab867c8775cbd58d19a8ee7dd0710ccabdfaae7dcb8e08edf0de12f16658e7(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainCidrMapsAssignments, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__568bbb84a0e6b538a5385884a194565496fa6ceb01f19839237019a65590f491(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainCidrMapsLinks, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__733aeb5d161759e22acbedbd4dda5833f7b732fc23d0895c7fcc44b1330ce99b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainCidrMaps]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__999093c45980b70972e1a2556d6c34e398122c6f64dbbdf48515ee724f913f92(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    as_maps: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainAsMaps, typing.Dict[builtins.str, typing.Any]]]]] = None,
    cidr_maps: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainCidrMaps, typing.Dict[builtins.str, typing.Any]]]]] = None,
    datacenters: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainDatacenters, typing.Dict[builtins.str, typing.Any]]]]] = None,
    geographic_maps: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainGeographicMaps, typing.Dict[builtins.str, typing.Any]]]]] = None,
    links: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainLinks, typing.Dict[builtins.str, typing.Any]]]]] = None,
    properties: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainProperties, typing.Dict[builtins.str, typing.Any]]]]] = None,
    resources: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainResources, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd872b6fa0fcc0af3910923b387e92fc3828b22efa71ae45a0c0495ca7407645(
    *,
    default_load_object: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainDatacentersDefaultLoadObject, typing.Dict[builtins.str, typing.Any]]]]] = None,
    links: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainDatacentersLinks, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48452f3d422eabafa639b426342b56dad2ee330e9a33f85c6442042779459975(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5712aed638a40cb49d5452028f48415108cb7ea4325f5771d5c94b1c628e9ed6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25428e49cd6b17c4ad5cb65ddfd3a1c9a2adc62d1c3e12f51f0b48f77ec7bd14(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b01413a6918072a40707f610b6f1d868185659138167341525f6cc18d8a9d4be(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13aa6e63be8b5395a17ba5fea73a870a48811ac24ca1238df04dab12c46fe6ec(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00910c6ded0da1a26c670e01ad8d1c572cd867a90d8e9e5074b87c9492e52605(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainDatacentersDefaultLoadObject]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e86d18689be4e2931e41f6d75c3017d9a1a4beeb7374a105de47dd48d7676a1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8aa3163988cd379b1a8029be86f4e0a268e50aa850ca4f5ceb5b8ead1f4d41df(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainDatacentersDefaultLoadObject]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16eb6dbd160ecafe1e45bd0efa6b524eaee7f555f6f597b64bcfce8f5e48fa75(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d30346389b9cf264203028227a32efcecc95cc17900f0603381f641b30c6fdb3(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df0491943f18b9c1e1292101c2bdde258edbf828f82d0542c6ba22a5e30494ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92e48165b7f453bb5de1e3995d4d819f8e8ed6e328b6668ca34b24282338abe8(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42b9fd5ab646a4f45bb3b55d9008d51238d1845cfd61c9ae26ea41c31f4e7148(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d21178e44918c8d57eb546b54edde9a87a8b6ffb15945f6923da5b8100dacd3e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainDatacentersLinks]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0d1967c3b5975b83f7bb07ec9c7165864ed0e97889982f7617ea6b1c24c4ee4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9987f807c07305efe23bfb41a1e52389fb9b1cfdbca574c87faf93e5a7488946(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainDatacentersLinks]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3780c73597e6addaac05f4922fe65f5d2c2184f844661c719762271da82acad2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b2464f413a5287510cf77dc1572f86e007a0e7cadc1e5a21fb09db29c71b320(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7ada49c5ae09b27f36577f2dc5057b0c59d0c1a6809d6d08ecf963e43f926f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8924c1d623d3fb246d027dc108dbc2fbfb11df402691d922fd0b0805d7e04835(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f08603530ef6e7538029ef05aeb9ccb98d38aab598ef3f04c9e471a5a46dbee(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b2a6f7c9f9437e42fdb22ee79bbd7ae4bdf3aff4d703ad1bfac2c3e440ae106(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainDatacenters]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87f2e0032ffe19fd75d30671d1e4a31ef891dc043a5ba4261202e556db4506e3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__542d5f37bf01070873ec9bc0805d1f1bd1935c1cb7c344bb82d87fe39019653a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainDatacentersDefaultLoadObject, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f215c9c7a2ec567cc32ccc348ec0a347103e050966130380679acdb6cb5b0ead(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainDatacentersLinks, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4db4f9fcf4f1b89813294a1f56630347b70e21971f0ee07247dc3cc24aeae304(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainDatacenters]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c3de928e81dc71e24a9b0ae7ee3c5e67686c00a9d663fd850d8d13925271d44(
    *,
    assignments: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainGeographicMapsAssignments, typing.Dict[builtins.str, typing.Any]]]]] = None,
    links: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainGeographicMapsLinks, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76e4dae3ebc38a1490bed57c42ff2cd5a2f49d8c9afa5456445d661a80d2f44e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c49343ecbbb643683fe49b3f8755edd6d04f8e6b641c1093615dba05c924e7d4(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f328e14c6a1ad64431f55893cb2dda55fe3b4a5fa53a8041b2a5d27b98e63ee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d7eae75f8e9720439a617bcd3a2468e85e8ac94888df832084543fe91588eda(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ceb648f1edefbfb75285d125759df1b1f2bee9307be2a8331b8c467538f8060b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb4b258138b90533ecc2c9b1cdfb537fcc146d2a2643b6cf70d79f907db6bd61(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainGeographicMapsAssignments]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__432fe6c6556c6789c935c3301fccb07ed809b97368d91d016aebaec33dd8af11(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__844e34aa0cfb1bc49426ed42a00e8726f61cb779e8a27f68ce025cffb8f02242(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainGeographicMapsAssignments]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da34d0e021ca1d1126fd97245625cd1422dd22342f363e24c102bb5e2fa5493e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c28b8b246040e76d037f063b6fcea5346f4257e47fd20a3fa6dcdea55b34317(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainGeographicMapsDefaultDatacenter]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6d997917c645740acbe19d4a950ab7c8e4867ac8855d60a6ae82d9a624cc6ec(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f72cd61bec4a2a8ae76ff9818ec1644afb13e50ed930adba905f0fdad8ebcb83(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0307be876d6fbab7c6b7831ae28cf6066fb1d3f0ab567c3bdbab9c8e559da05(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8303a9d8fe2a69ed69b27700f23180fc9528c58fc5c338b06ee609d3b7e147cd(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c7dfd841afc02d7baa1a9fe982eec9c62609fd2f375aedee395bcdbc8956a11(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2bba8e4d2b486254bda3d1af4c38e2f8a27a5604fd723f02cbbf8399506eb25(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainGeographicMapsLinks]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a78363ca5cc37fb34a1c98c52a719d30ee6fff99593de259d02be92eb6b8a02(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35807f4af5ae737d900d2e293dd57b85faab264c7d27ca69f639ed8315f79a0f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainGeographicMapsLinks]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__988f78bf4b52c3878b15de87209d40501f6088463d49847ca5bb617cb496c259(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f84608cd2218dc507bea5ab0d58d7090c223c7362f2f6632e8e4aa829afd8394(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c800bdacfca73b059a03fd82f58efc9e16336fc9ecea7eba1976d96e4fef152a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e821d5143880b148765d655956b09da931e9207ab12bd8a6255f0ce3708edd1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4d7aa51b5ccf675f7709cc67946df3c8dc4234b94c420197c3155b62c2e14c7(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__478622864ab4b4693885667502417d192576cb8200c28e80c959b283544b92e8(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainGeographicMaps]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c63ecf4c6087e1c9c90aa77e5a72cfbad5375bb482f9bed1d3e9e1c6253a2cbd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a08caf62ed4dd36e6d25de847dcfaec223b111038c35cfb2ceff56b05dea0769(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainGeographicMapsAssignments, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ecdfad811262af7f38cd5b3245f2c5e7d1acd2238066da7fb5bd52013de1305(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainGeographicMapsLinks, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da63413184520d3ea13b54e74a09794431d2b4b7d1de64c27549bde1c727f883(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainGeographicMaps]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c31d5cf2f0ff69210125527fb641786f570764149e2970f36863e08776247600(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11d546688afe77c948aec5a28d4d7d831d15dd17edc3742fa5a520f3fcf6106e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bfa75255d309e514a185855ba43f932b3900dbf9c0b7e000d7a3cd21e177c04(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68a2ab3e99a74b09903af54d49577c9f33a8fad86b20c5293eaf849d9e54a7c9(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9920acb7862ebb7437c5afad57cedfb0951de77b0dc933f28f9de063eb533545(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c28c9059a3b4a8f9505ec5ac238fbac290c97ccabdd661a0ebd9a0aad71a80d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainLinks]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32a45a736639d7013127b3c4d62f639fd493587d2d38ee700137c91c39d81322(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__deed70c4f7496ebc130300afb21af89819da440566003d9efb3bfbfa03f55739(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainLinks]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bbb51ba39023fb923970bbd4bc6f89498c7694b24a7ca08ba7ad55e1920107d(
    *,
    links: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainPropertiesLinks, typing.Dict[builtins.str, typing.Any]]]]] = None,
    liveness_tests: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainPropertiesLivenessTests, typing.Dict[builtins.str, typing.Any]]]]] = None,
    static_rr_sets: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainPropertiesStaticRrSets, typing.Dict[builtins.str, typing.Any]]]]] = None,
    traffic_targets: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainPropertiesTrafficTargets, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af2ab56e72e01f58267b023f05aa62e98386ed4bc2459fa271f26ef02c1f91f2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b14141cd964dd13d5c1ad1283edaf2e5f77b9be0c7fae217ef514137a17bedb(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00112e045e346929b4d9f1d094cb924c6dcdbc2f8c27493f7a66a864ca4ac847(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9626356c056db986fdc85386000508ddda4474d5e4bfcf1745bebb2a7439b78(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9277fec70a15cee9ce4105b93e35153d35dc9b7f3f80ad99993c87bd8a36829a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05bb7f30eb6954bec6a1b64cfd9f13a65650c8c3f3bf4b0e1a5a7c5431d92cc5(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainPropertiesLinks]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c19e048a13187842c2727eb43a9a78e4e7d482be34c47d4d3e28b2bb28b39a8c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba41ffb48bbd0f4a5e112b30e9b8e67d4361eb64c31d7b2c6a84067912490c7f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainPropertiesLinks]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__922b0285e652b4451565b527cce994c1deff27fa7bf1ed7a5dd521545b3ee035(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bc5482810fd6974a58fc2be4630056067c191499b3efae2ea5afa15bc542908(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22cbda29728dc31e4bbd4e4dca509fde065d5a893d393e60178b52079ffd75b7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f661787c14d064b4a77ea9e6b8f22a41d332ee5a857c34c2b1fda83249083f10(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd62f726dfaa523a3a1865f856d971dc59477f3744dca34be3db2adea843e1bf(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfa3af1318b8f164550f5391850e0b94c25738192fe6e840e555d904924f666e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainProperties]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f33141af781f4637231dae9f7d7eb24a31bf8d3ee829c232fa2e8b85c8fd2836(
    *,
    http_headers: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainPropertiesLivenessTestsHttpHeaders, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffa50cbb8bea00907a6aabdd650195591afdc719b4f2738730a9d2c50c74afcd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d07acab8ee3509015ff9d62581f654e94396c6c82aa2c8cf7aad448d26f39030(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aaa289cda490d44d3aef9dc8500378410f2d7a970c5a00497b90b01178b706ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__488a7b48687246791775b362d60108129eb64618a46be4468ffac920c84ae41f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d22ac68a6fde5f543ce063de8330bdb8b81fe1a233b7e5b6fe3eb9db430a47a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3d62f7d1eb2d07f4d85ad7e0a330c614214919efdd87226aa8b550959fa233d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainPropertiesLivenessTestsHttpHeaders]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfa9a1c9f17a7d229f3f039d179dccbf51073eaead1b350c6ca139270acefe3d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9990b601e5e816e65942d7c5d0436deb822d16b3c1fd463cc2438b5c7a2ce038(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainPropertiesLivenessTestsHttpHeaders]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42b6f65bb933609e5f89e1de22f23fef2909a008478d94fe5ef935c350163829(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8502d5c482516738f6380b7a13baa3966ae8d163b720d49b5dcecb7e434d2b52(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d801603f5fd2a2ff6cb87c1394fcbe893152359afb4c5eb58f61cf87c117ba6a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f68dbfecfab50a4bb276dad23bc22fdb20a909919f40b62cf3ba842d8790197(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93259587b0c970d8f2083cf567bdee5bf8bebd24c851ab9830d772338e811c1c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a6b374367a94799625e9b16ba7a117c5530c22b59ab726e851fd952ffd42288(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainPropertiesLivenessTests]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b51ef33c246c2c949de5180e856205e7cfdb3b0fc80b3a8c9813c1d2e694399a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3adb86a2805366417b68227f707c87137e077cf2bf520087bc72fa1a54368af2(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainPropertiesLivenessTestsHttpHeaders, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18b1c9c15e478d7b63103dfc8bbc11a1b40ed87ac93296ba8f4b41f158045119(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainPropertiesLivenessTests]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe2c4a6405736453b2ffccad03d07d252b35321a87bc6c330ab173b8edc02cb6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17141713ad42db431fae10f5d53e6f63353ee43364eab0446a71699f66100d73(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainPropertiesLinks, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f424f3043969afd40b18cfc49dc6d726d1ceff17e02f13b3178066660c7ee7c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainPropertiesLivenessTests, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81e631d4afe20d04f47ebd2c711dbb96e6c1acc3164b7dd64acaa4c79f89596b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainPropertiesStaticRrSets, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ed630636f51ed2d8c98b9c222a03464bef138c9ef4aacdbf08f4af39d3a30c2(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainPropertiesTrafficTargets, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6950b0ef605d19748c5ab53fe236cb8aaa61ec2c2963dee7d384bfef15d0ecef(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainProperties]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5abad77a74da6825c81c9cb016a0736515fc65543f7697b12f7863cc0f08c1f7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7611b9549816707c57e6c0194f303725b929cdd130f9683a70b71ee6ef5ad5fc(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d76f0a0f8be321e85501528065b5f3c3412b68707ef260cb7bd7a26012c9a88(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89ace75c51bf79a76c36a4d6137efe0f03fe92c87c62cc112e94c79bf2475cf9(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78ab1fa998bc5e7538316a88a0d27e7b6f9ef88ad71dc9388ba777104789bb9e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3aa6a2919cd76d4e8650538852a406922a62fbfc0ea3dcf9135bb025adb5a96(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainPropertiesStaticRrSets]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d51a256fbb92a00a404bd04cf2f76607d25c485de8bf2c6b8eb20f8bc261778(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae34d41cfcd2b18d2175e522b88a519bc080bda1edd3e868459c32539e5930f8(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainPropertiesStaticRrSets]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebc8052c227f5b7c1f53c75519ccd20a6716979c5f0be2831b06a11098b3e108(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f5d331af2cd33bf41266a26d8d073c79b3c040df7166d1a6313d3eec5862ef6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a9d86090814975068cd35bfb14964dbc1b9553a2aac0d0bd9c9c71de408ea1b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aec1099e7d73cecc275cf6447ef11a40e68fbd45f2e0bba22b70eb6946446481(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d9d38dead3397121f6d1102ea6a562036f7ab96706dbfac1f18ca55f092e09f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d166dda905f6d53af5c24ca1cabd590dbaf10aeec210dffe21d38ca7836d90df(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainPropertiesTrafficTargets]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60bf05bb1fe48b3fb91b2794ec3fbb28254ea29c15fa9a505f73db36c8785dd5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17b4d3127877583ad30cda615dae4c250d54667c74bb829ecce7fdf15116d3e8(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainPropertiesTrafficTargets]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c71b0383f6800aababfde64e2a55936dcb5f0b91837e62dc65753f0c46100d1(
    *,
    links: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainResourcesLinks, typing.Dict[builtins.str, typing.Any]]]]] = None,
    resource_instances: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainResourcesResourceInstances, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b967a66418bc9d5576d9acb0fe2ddd8a4ab0a6e1086d817ecb77ea44e0cb9c44(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa89bd40791c758b4e7940a9919a11ad3de13fe7d63a797953cdd292a371ef80(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__682fa59f2b0701a76cadb09b380525d929b205e0af071d99abc9c73de4d6465c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df27b9fbd3d836d8ee6c168d1be0bd1f56581981d9f58440eb9ad3c269824d55(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc4740029b19c39b7b237b3b1ae5eb55845327fecd34dd9d176c1fec224f0a37(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4469b93f1207e78f004aa56f574c61f1bda3481dc6ca783d232ed62efd8064f5(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainResourcesLinks]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e685fdd510d68b7b44fc2e9134a9bdefbbf39f16d36560414de4659451df3028(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a494de091df0e01d1587f5b936169340392451f1ffb186ef216b66a3f2d1d604(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainResourcesLinks]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de296f5f40c79d4d35b3f06cba975d66e8c0117ea3cc3753fe7a8d7df66e53c3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b827ec25fac82c363c9cfc998ba45ccd291f7f47c9eafc85852ae84518efbdc8(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94bbceb50926812b8e42930deb031b311462e57c58ca9053fa046c431a3fce00(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e8be1ec8ee9639777daefe0304f6552150bdfac8f8e27eb31cb4fa6fbcce0b1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c6049ca96b45c79039e0afc860c42de7c550bf21524589dafdd28fd3e302854(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95e5784cc43ff030d19a8eec9c41f744a674d964440c9257b8be3373e55a061e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainResources]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29d12af921eba97e4c69ac4191164fd7c50d5589f738f2fbd69660689686271a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d44b36441197303138be5b21fd961cd1e4ca34f1bc645ac25676ac078ca05497(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainResourcesLinks, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92838c56dc22a49ef7a964f290a1c562348647061e6ee6468f8ba962e484eeb6(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainResourcesResourceInstances, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3411a0a002fddcf4b46da356e865eabc7cb589d526b44ba65d747a1920dbb95c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainResources]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45e917e097aa8937a689f07600d12bc3c38f4d7e566e7a66e53161d756b841f8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e8b9beaaeee661e7698f3895c7e8bf3a6afd1222e1043c29b090405eb9063eb(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7113f5f90a08550fc9ea8f5de229f3a16bcfa35ca899892fe2343b3d23012df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcba008fc9d19f03435351636f516ebb7c9f6b2bf17bac9520573c7678d28420(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed385236fd96d1d079d95d24cbf0a29cd417fb23e295012bb63b22c88c2107bc(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8345d39a5824b2199a3a25d63f187a67e8fe78c6c27028f12e3e27612ce86640(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainResourcesResourceInstances]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cbe32863780da478432e46db19392c021fb49e4f446c5421d249131df5f79bc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5baa5631da0120da91ea07380a5d02a7e27146e323ef8a0989564dfb105b3d8(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainResourcesResourceInstances]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06dea4992fecf92e80cdf73b9fcae078248872171991664a80282e555379770b(
    *,
    links: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainStatusLinks, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdf03d4f71f27c74e5154bcee46ccaa954ce231c9c6dd6366a606b31de22e2bb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab537c3d4493e33717de78ae437db96a3bc15fbe0c96732138acc1ec6e8bfec5(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94c4cbdb4b07ac83423955252b1333febbe1250971e021bb65598af81519552c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f016b1560f188993d2f8e289e9058fc6d0a8c415dfbae0aedacab23c21447617(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__721d428366ce3bbb17d3c4cba3ee1eadfa5fb07f16a324e105cdb6585069edb9(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5688bcee2d8aaa41de84660f92222638bda2d887f70b1bfc1c08197e7675490e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiGtmDomainStatusLinks]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8e3a3089eea5e626b16007e56a1e84e2502f48da1840ed87f0294c2ab3578a6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__159319c4fbe4520cb0121e5e998017b8d930dbd83abbc34512a516b248f604cb(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainStatusLinks]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78ca1310040b9ff848d849320695052c79478dcce0192789edf524c0a0fa33bf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__200a72dd4db9f9019df8663f219c32885875847462708157dce4209fd34a68ca(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiGtmDomainStatusLinks, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74808c3a663ceb1189d12cddd2bf5de3d3924e11d5e54e4afe3f1185b6275a8b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiGtmDomainStatus]],
) -> None:
    """Type checking stubs"""
    pass
