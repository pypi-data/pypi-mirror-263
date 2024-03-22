'''
# `akamai_gtm_datacenter`

Refer to the Terraform Registry for docs: [`akamai_gtm_datacenter`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter).
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


class GtmDatacenter(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.gtmDatacenter.GtmDatacenter",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter akamai_gtm_datacenter}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        domain: builtins.str,
        city: typing.Optional[builtins.str] = None,
        clone_of: typing.Optional[jsii.Number] = None,
        cloud_server_host_header_override: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        cloud_server_targeting: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        continent: typing.Optional[builtins.str] = None,
        country: typing.Optional[builtins.str] = None,
        default_load_object: typing.Optional[typing.Union["GtmDatacenterDefaultLoadObject", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        latitude: typing.Optional[jsii.Number] = None,
        longitude: typing.Optional[jsii.Number] = None,
        nickname: typing.Optional[builtins.str] = None,
        state_or_province: typing.Optional[builtins.str] = None,
        wait_on_complete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter akamai_gtm_datacenter} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param domain: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#domain GtmDatacenter#domain}.
        :param city: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#city GtmDatacenter#city}.
        :param clone_of: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#clone_of GtmDatacenter#clone_of}.
        :param cloud_server_host_header_override: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#cloud_server_host_header_override GtmDatacenter#cloud_server_host_header_override}.
        :param cloud_server_targeting: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#cloud_server_targeting GtmDatacenter#cloud_server_targeting}.
        :param continent: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#continent GtmDatacenter#continent}.
        :param country: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#country GtmDatacenter#country}.
        :param default_load_object: default_load_object block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#default_load_object GtmDatacenter#default_load_object}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#id GtmDatacenter#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param latitude: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#latitude GtmDatacenter#latitude}.
        :param longitude: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#longitude GtmDatacenter#longitude}.
        :param nickname: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#nickname GtmDatacenter#nickname}.
        :param state_or_province: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#state_or_province GtmDatacenter#state_or_province}.
        :param wait_on_complete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#wait_on_complete GtmDatacenter#wait_on_complete}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73891043a670e3dc7cee5023fd05250c051c3401799bb4d0559f247062f669eb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GtmDatacenterConfig(
            domain=domain,
            city=city,
            clone_of=clone_of,
            cloud_server_host_header_override=cloud_server_host_header_override,
            cloud_server_targeting=cloud_server_targeting,
            continent=continent,
            country=country,
            default_load_object=default_load_object,
            id=id,
            latitude=latitude,
            longitude=longitude,
            nickname=nickname,
            state_or_province=state_or_province,
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
        '''Generates CDKTF code for importing a GtmDatacenter resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the GtmDatacenter to import.
        :param import_from_id: The id of the existing GtmDatacenter that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the GtmDatacenter to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__024b4e9215d7152d14b6d203f1d33aa07ad201c141f5737d66960d0abfb6bbdc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putDefaultLoadObject")
    def put_default_load_object(
        self,
        *,
        load_object: typing.Optional[builtins.str] = None,
        load_object_port: typing.Optional[jsii.Number] = None,
        load_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param load_object: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#load_object GtmDatacenter#load_object}.
        :param load_object_port: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#load_object_port GtmDatacenter#load_object_port}.
        :param load_servers: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#load_servers GtmDatacenter#load_servers}.
        '''
        value = GtmDatacenterDefaultLoadObject(
            load_object=load_object,
            load_object_port=load_object_port,
            load_servers=load_servers,
        )

        return typing.cast(None, jsii.invoke(self, "putDefaultLoadObject", [value]))

    @jsii.member(jsii_name="resetCity")
    def reset_city(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCity", []))

    @jsii.member(jsii_name="resetCloneOf")
    def reset_clone_of(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloneOf", []))

    @jsii.member(jsii_name="resetCloudServerHostHeaderOverride")
    def reset_cloud_server_host_header_override(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudServerHostHeaderOverride", []))

    @jsii.member(jsii_name="resetCloudServerTargeting")
    def reset_cloud_server_targeting(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudServerTargeting", []))

    @jsii.member(jsii_name="resetContinent")
    def reset_continent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContinent", []))

    @jsii.member(jsii_name="resetCountry")
    def reset_country(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCountry", []))

    @jsii.member(jsii_name="resetDefaultLoadObject")
    def reset_default_load_object(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultLoadObject", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLatitude")
    def reset_latitude(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLatitude", []))

    @jsii.member(jsii_name="resetLongitude")
    def reset_longitude(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLongitude", []))

    @jsii.member(jsii_name="resetNickname")
    def reset_nickname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNickname", []))

    @jsii.member(jsii_name="resetStateOrProvince")
    def reset_state_or_province(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStateOrProvince", []))

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
    @jsii.member(jsii_name="datacenterId")
    def datacenter_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "datacenterId"))

    @builtins.property
    @jsii.member(jsii_name="defaultLoadObject")
    def default_load_object(self) -> "GtmDatacenterDefaultLoadObjectOutputReference":
        return typing.cast("GtmDatacenterDefaultLoadObjectOutputReference", jsii.get(self, "defaultLoadObject"))

    @builtins.property
    @jsii.member(jsii_name="pingInterval")
    def ping_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "pingInterval"))

    @builtins.property
    @jsii.member(jsii_name="pingPacketSize")
    def ping_packet_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "pingPacketSize"))

    @builtins.property
    @jsii.member(jsii_name="scorePenalty")
    def score_penalty(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scorePenalty"))

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
    @jsii.member(jsii_name="virtual")
    def virtual(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "virtual"))

    @builtins.property
    @jsii.member(jsii_name="cityInput")
    def city_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cityInput"))

    @builtins.property
    @jsii.member(jsii_name="cloneOfInput")
    def clone_of_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cloneOfInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudServerHostHeaderOverrideInput")
    def cloud_server_host_header_override_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "cloudServerHostHeaderOverrideInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudServerTargetingInput")
    def cloud_server_targeting_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "cloudServerTargetingInput"))

    @builtins.property
    @jsii.member(jsii_name="continentInput")
    def continent_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "continentInput"))

    @builtins.property
    @jsii.member(jsii_name="countryInput")
    def country_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "countryInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultLoadObjectInput")
    def default_load_object_input(
        self,
    ) -> typing.Optional["GtmDatacenterDefaultLoadObject"]:
        return typing.cast(typing.Optional["GtmDatacenterDefaultLoadObject"], jsii.get(self, "defaultLoadObjectInput"))

    @builtins.property
    @jsii.member(jsii_name="domainInput")
    def domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="latitudeInput")
    def latitude_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "latitudeInput"))

    @builtins.property
    @jsii.member(jsii_name="longitudeInput")
    def longitude_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "longitudeInput"))

    @builtins.property
    @jsii.member(jsii_name="nicknameInput")
    def nickname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nicknameInput"))

    @builtins.property
    @jsii.member(jsii_name="stateOrProvinceInput")
    def state_or_province_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateOrProvinceInput"))

    @builtins.property
    @jsii.member(jsii_name="waitOnCompleteInput")
    def wait_on_complete_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "waitOnCompleteInput"))

    @builtins.property
    @jsii.member(jsii_name="city")
    def city(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "city"))

    @city.setter
    def city(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c21ad9385d512fb97c5f00affddb7ead8ce0d18c2a15ee8943d3c1a3b766f8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "city", value)

    @builtins.property
    @jsii.member(jsii_name="cloneOf")
    def clone_of(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cloneOf"))

    @clone_of.setter
    def clone_of(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__935316d3b431019fd71eb5ce181a86a15ef982879835dbc6e1f49c523245297f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloneOf", value)

    @builtins.property
    @jsii.member(jsii_name="cloudServerHostHeaderOverride")
    def cloud_server_host_header_override(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "cloudServerHostHeaderOverride"))

    @cloud_server_host_header_override.setter
    def cloud_server_host_header_override(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f78d0baf09337f67ef244c05635fb926078d4b680483163267603d644c666044)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudServerHostHeaderOverride", value)

    @builtins.property
    @jsii.member(jsii_name="cloudServerTargeting")
    def cloud_server_targeting(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "cloudServerTargeting"))

    @cloud_server_targeting.setter
    def cloud_server_targeting(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40b1f3bed6dcbf6c0e97529ea4e7454b1f6690fad32b0ee8747ab51b77663120)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudServerTargeting", value)

    @builtins.property
    @jsii.member(jsii_name="continent")
    def continent(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "continent"))

    @continent.setter
    def continent(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44412561b9d94ba7612c39c224687c90371058a7c0762083dfc7dbad9227bce0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "continent", value)

    @builtins.property
    @jsii.member(jsii_name="country")
    def country(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "country"))

    @country.setter
    def country(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e73f324f71332d59f1cbd258c12dc3ccbb5380c7bc242ac02ce70d1fd7d10297)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "country", value)

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ceaedcfc7e7c4da6ce6656b7b16845ab3abd56c675c0c12109d15f0dd9c932d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8511df0d80f7f34faafb5ddd9f9f793d8775b297a9be22a7164d90f605f6f703)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="latitude")
    def latitude(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "latitude"))

    @latitude.setter
    def latitude(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b101d0efa33186088640e900fb2e27570380607747cc281363e3b94c3e536492)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "latitude", value)

    @builtins.property
    @jsii.member(jsii_name="longitude")
    def longitude(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "longitude"))

    @longitude.setter
    def longitude(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5fe315b5b265043c9fce6f19c868ed6ef1ec0a38a6f07d5499fb4118e745549)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "longitude", value)

    @builtins.property
    @jsii.member(jsii_name="nickname")
    def nickname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nickname"))

    @nickname.setter
    def nickname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbf0e6c65bf41e7118548d0072ae028a0d5dc4098d7cdcdd0db6524e85992dae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nickname", value)

    @builtins.property
    @jsii.member(jsii_name="stateOrProvince")
    def state_or_province(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stateOrProvince"))

    @state_or_province.setter
    def state_or_province(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90237cec63311d44ac006dfebc09b4d455e65e0790e89dff7e49d515da58da9d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stateOrProvince", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__3b4052ab13a33f7c7c9e4ac2ce312aded3871ffb7c574b4b19b3dfd3dad2ba0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitOnComplete", value)


@jsii.data_type(
    jsii_type="akamai.gtmDatacenter.GtmDatacenterConfig",
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
        "city": "city",
        "clone_of": "cloneOf",
        "cloud_server_host_header_override": "cloudServerHostHeaderOverride",
        "cloud_server_targeting": "cloudServerTargeting",
        "continent": "continent",
        "country": "country",
        "default_load_object": "defaultLoadObject",
        "id": "id",
        "latitude": "latitude",
        "longitude": "longitude",
        "nickname": "nickname",
        "state_or_province": "stateOrProvince",
        "wait_on_complete": "waitOnComplete",
    },
)
class GtmDatacenterConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        city: typing.Optional[builtins.str] = None,
        clone_of: typing.Optional[jsii.Number] = None,
        cloud_server_host_header_override: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        cloud_server_targeting: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        continent: typing.Optional[builtins.str] = None,
        country: typing.Optional[builtins.str] = None,
        default_load_object: typing.Optional[typing.Union["GtmDatacenterDefaultLoadObject", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        latitude: typing.Optional[jsii.Number] = None,
        longitude: typing.Optional[jsii.Number] = None,
        nickname: typing.Optional[builtins.str] = None,
        state_or_province: typing.Optional[builtins.str] = None,
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
        :param domain: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#domain GtmDatacenter#domain}.
        :param city: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#city GtmDatacenter#city}.
        :param clone_of: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#clone_of GtmDatacenter#clone_of}.
        :param cloud_server_host_header_override: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#cloud_server_host_header_override GtmDatacenter#cloud_server_host_header_override}.
        :param cloud_server_targeting: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#cloud_server_targeting GtmDatacenter#cloud_server_targeting}.
        :param continent: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#continent GtmDatacenter#continent}.
        :param country: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#country GtmDatacenter#country}.
        :param default_load_object: default_load_object block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#default_load_object GtmDatacenter#default_load_object}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#id GtmDatacenter#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param latitude: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#latitude GtmDatacenter#latitude}.
        :param longitude: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#longitude GtmDatacenter#longitude}.
        :param nickname: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#nickname GtmDatacenter#nickname}.
        :param state_or_province: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#state_or_province GtmDatacenter#state_or_province}.
        :param wait_on_complete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#wait_on_complete GtmDatacenter#wait_on_complete}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(default_load_object, dict):
            default_load_object = GtmDatacenterDefaultLoadObject(**default_load_object)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21e4994eac7a6936d48f419cad2bfad14365c9ae5ab2fc07d52dd5f85facef0d)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            check_type(argname="argument city", value=city, expected_type=type_hints["city"])
            check_type(argname="argument clone_of", value=clone_of, expected_type=type_hints["clone_of"])
            check_type(argname="argument cloud_server_host_header_override", value=cloud_server_host_header_override, expected_type=type_hints["cloud_server_host_header_override"])
            check_type(argname="argument cloud_server_targeting", value=cloud_server_targeting, expected_type=type_hints["cloud_server_targeting"])
            check_type(argname="argument continent", value=continent, expected_type=type_hints["continent"])
            check_type(argname="argument country", value=country, expected_type=type_hints["country"])
            check_type(argname="argument default_load_object", value=default_load_object, expected_type=type_hints["default_load_object"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument latitude", value=latitude, expected_type=type_hints["latitude"])
            check_type(argname="argument longitude", value=longitude, expected_type=type_hints["longitude"])
            check_type(argname="argument nickname", value=nickname, expected_type=type_hints["nickname"])
            check_type(argname="argument state_or_province", value=state_or_province, expected_type=type_hints["state_or_province"])
            check_type(argname="argument wait_on_complete", value=wait_on_complete, expected_type=type_hints["wait_on_complete"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain": domain,
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
        if city is not None:
            self._values["city"] = city
        if clone_of is not None:
            self._values["clone_of"] = clone_of
        if cloud_server_host_header_override is not None:
            self._values["cloud_server_host_header_override"] = cloud_server_host_header_override
        if cloud_server_targeting is not None:
            self._values["cloud_server_targeting"] = cloud_server_targeting
        if continent is not None:
            self._values["continent"] = continent
        if country is not None:
            self._values["country"] = country
        if default_load_object is not None:
            self._values["default_load_object"] = default_load_object
        if id is not None:
            self._values["id"] = id
        if latitude is not None:
            self._values["latitude"] = latitude
        if longitude is not None:
            self._values["longitude"] = longitude
        if nickname is not None:
            self._values["nickname"] = nickname
        if state_or_province is not None:
            self._values["state_or_province"] = state_or_province
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
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#domain GtmDatacenter#domain}.'''
        result = self._values.get("domain")
        assert result is not None, "Required property 'domain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def city(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#city GtmDatacenter#city}.'''
        result = self._values.get("city")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def clone_of(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#clone_of GtmDatacenter#clone_of}.'''
        result = self._values.get("clone_of")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cloud_server_host_header_override(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#cloud_server_host_header_override GtmDatacenter#cloud_server_host_header_override}.'''
        result = self._values.get("cloud_server_host_header_override")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def cloud_server_targeting(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#cloud_server_targeting GtmDatacenter#cloud_server_targeting}.'''
        result = self._values.get("cloud_server_targeting")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def continent(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#continent GtmDatacenter#continent}.'''
        result = self._values.get("continent")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def country(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#country GtmDatacenter#country}.'''
        result = self._values.get("country")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_load_object(self) -> typing.Optional["GtmDatacenterDefaultLoadObject"]:
        '''default_load_object block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#default_load_object GtmDatacenter#default_load_object}
        '''
        result = self._values.get("default_load_object")
        return typing.cast(typing.Optional["GtmDatacenterDefaultLoadObject"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#id GtmDatacenter#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def latitude(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#latitude GtmDatacenter#latitude}.'''
        result = self._values.get("latitude")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def longitude(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#longitude GtmDatacenter#longitude}.'''
        result = self._values.get("longitude")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def nickname(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#nickname GtmDatacenter#nickname}.'''
        result = self._values.get("nickname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state_or_province(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#state_or_province GtmDatacenter#state_or_province}.'''
        result = self._values.get("state_or_province")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wait_on_complete(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#wait_on_complete GtmDatacenter#wait_on_complete}.'''
        result = self._values.get("wait_on_complete")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GtmDatacenterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.gtmDatacenter.GtmDatacenterDefaultLoadObject",
    jsii_struct_bases=[],
    name_mapping={
        "load_object": "loadObject",
        "load_object_port": "loadObjectPort",
        "load_servers": "loadServers",
    },
)
class GtmDatacenterDefaultLoadObject:
    def __init__(
        self,
        *,
        load_object: typing.Optional[builtins.str] = None,
        load_object_port: typing.Optional[jsii.Number] = None,
        load_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param load_object: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#load_object GtmDatacenter#load_object}.
        :param load_object_port: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#load_object_port GtmDatacenter#load_object_port}.
        :param load_servers: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#load_servers GtmDatacenter#load_servers}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44aeaeed303481f708247dac3e380bab92c42156405c5ba60c71e89d3c32952c)
            check_type(argname="argument load_object", value=load_object, expected_type=type_hints["load_object"])
            check_type(argname="argument load_object_port", value=load_object_port, expected_type=type_hints["load_object_port"])
            check_type(argname="argument load_servers", value=load_servers, expected_type=type_hints["load_servers"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if load_object is not None:
            self._values["load_object"] = load_object
        if load_object_port is not None:
            self._values["load_object_port"] = load_object_port
        if load_servers is not None:
            self._values["load_servers"] = load_servers

    @builtins.property
    def load_object(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#load_object GtmDatacenter#load_object}.'''
        result = self._values.get("load_object")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def load_object_port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#load_object_port GtmDatacenter#load_object_port}.'''
        result = self._values.get("load_object_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def load_servers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_datacenter#load_servers GtmDatacenter#load_servers}.'''
        result = self._values.get("load_servers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GtmDatacenterDefaultLoadObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GtmDatacenterDefaultLoadObjectOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.gtmDatacenter.GtmDatacenterDefaultLoadObjectOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__159b427d871dba43308ed00362b1a45df44297b5c3f8539ddb0e8d725677fb41)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLoadObject")
    def reset_load_object(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadObject", []))

    @jsii.member(jsii_name="resetLoadObjectPort")
    def reset_load_object_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadObjectPort", []))

    @jsii.member(jsii_name="resetLoadServers")
    def reset_load_servers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadServers", []))

    @builtins.property
    @jsii.member(jsii_name="loadObjectInput")
    def load_object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loadObjectInput"))

    @builtins.property
    @jsii.member(jsii_name="loadObjectPortInput")
    def load_object_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "loadObjectPortInput"))

    @builtins.property
    @jsii.member(jsii_name="loadServersInput")
    def load_servers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "loadServersInput"))

    @builtins.property
    @jsii.member(jsii_name="loadObject")
    def load_object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loadObject"))

    @load_object.setter
    def load_object(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63296365092f15f1c0f03d54f41dc59847fe36a511814703887d2fc5fa6d6f94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadObject", value)

    @builtins.property
    @jsii.member(jsii_name="loadObjectPort")
    def load_object_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "loadObjectPort"))

    @load_object_port.setter
    def load_object_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__640287fed40781ca7ccee6192c5f82cc762ef609524e625e50225bdef9e8224e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadObjectPort", value)

    @builtins.property
    @jsii.member(jsii_name="loadServers")
    def load_servers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "loadServers"))

    @load_servers.setter
    def load_servers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33e0e24b22f250e0ba4ad034d9394af374b5ed09a8c6f3e7e4c75948500af222)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadServers", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GtmDatacenterDefaultLoadObject]:
        return typing.cast(typing.Optional[GtmDatacenterDefaultLoadObject], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GtmDatacenterDefaultLoadObject],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aeb64a4cedbb0e5af9492378b8b96ea3e2d44671c63e96eb848d2e93e28abcaa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GtmDatacenter",
    "GtmDatacenterConfig",
    "GtmDatacenterDefaultLoadObject",
    "GtmDatacenterDefaultLoadObjectOutputReference",
]

publication.publish()

def _typecheckingstub__73891043a670e3dc7cee5023fd05250c051c3401799bb4d0559f247062f669eb(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    domain: builtins.str,
    city: typing.Optional[builtins.str] = None,
    clone_of: typing.Optional[jsii.Number] = None,
    cloud_server_host_header_override: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    cloud_server_targeting: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    continent: typing.Optional[builtins.str] = None,
    country: typing.Optional[builtins.str] = None,
    default_load_object: typing.Optional[typing.Union[GtmDatacenterDefaultLoadObject, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    latitude: typing.Optional[jsii.Number] = None,
    longitude: typing.Optional[jsii.Number] = None,
    nickname: typing.Optional[builtins.str] = None,
    state_or_province: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__024b4e9215d7152d14b6d203f1d33aa07ad201c141f5737d66960d0abfb6bbdc(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c21ad9385d512fb97c5f00affddb7ead8ce0d18c2a15ee8943d3c1a3b766f8d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__935316d3b431019fd71eb5ce181a86a15ef982879835dbc6e1f49c523245297f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f78d0baf09337f67ef244c05635fb926078d4b680483163267603d644c666044(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40b1f3bed6dcbf6c0e97529ea4e7454b1f6690fad32b0ee8747ab51b77663120(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44412561b9d94ba7612c39c224687c90371058a7c0762083dfc7dbad9227bce0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e73f324f71332d59f1cbd258c12dc3ccbb5380c7bc242ac02ce70d1fd7d10297(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ceaedcfc7e7c4da6ce6656b7b16845ab3abd56c675c0c12109d15f0dd9c932d0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8511df0d80f7f34faafb5ddd9f9f793d8775b297a9be22a7164d90f605f6f703(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b101d0efa33186088640e900fb2e27570380607747cc281363e3b94c3e536492(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5fe315b5b265043c9fce6f19c868ed6ef1ec0a38a6f07d5499fb4118e745549(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbf0e6c65bf41e7118548d0072ae028a0d5dc4098d7cdcdd0db6524e85992dae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90237cec63311d44ac006dfebc09b4d455e65e0790e89dff7e49d515da58da9d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b4052ab13a33f7c7c9e4ac2ce312aded3871ffb7c574b4b19b3dfd3dad2ba0b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21e4994eac7a6936d48f419cad2bfad14365c9ae5ab2fc07d52dd5f85facef0d(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    domain: builtins.str,
    city: typing.Optional[builtins.str] = None,
    clone_of: typing.Optional[jsii.Number] = None,
    cloud_server_host_header_override: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    cloud_server_targeting: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    continent: typing.Optional[builtins.str] = None,
    country: typing.Optional[builtins.str] = None,
    default_load_object: typing.Optional[typing.Union[GtmDatacenterDefaultLoadObject, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    latitude: typing.Optional[jsii.Number] = None,
    longitude: typing.Optional[jsii.Number] = None,
    nickname: typing.Optional[builtins.str] = None,
    state_or_province: typing.Optional[builtins.str] = None,
    wait_on_complete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44aeaeed303481f708247dac3e380bab92c42156405c5ba60c71e89d3c32952c(
    *,
    load_object: typing.Optional[builtins.str] = None,
    load_object_port: typing.Optional[jsii.Number] = None,
    load_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__159b427d871dba43308ed00362b1a45df44297b5c3f8539ddb0e8d725677fb41(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63296365092f15f1c0f03d54f41dc59847fe36a511814703887d2fc5fa6d6f94(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__640287fed40781ca7ccee6192c5f82cc762ef609524e625e50225bdef9e8224e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33e0e24b22f250e0ba4ad034d9394af374b5ed09a8c6f3e7e4c75948500af222(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aeb64a4cedbb0e5af9492378b8b96ea3e2d44671c63e96eb848d2e93e28abcaa(
    value: typing.Optional[GtmDatacenterDefaultLoadObject],
) -> None:
    """Type checking stubs"""
    pass
