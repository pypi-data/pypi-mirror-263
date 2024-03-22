'''
# `akamai_cloudlets_application_load_balancer`

Refer to the Terraform Registry for docs: [`akamai_cloudlets_application_load_balancer`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer).
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


class CloudletsApplicationLoadBalancer(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.cloudletsApplicationLoadBalancer.CloudletsApplicationLoadBalancer",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer akamai_cloudlets_application_load_balancer}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        data_centers: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudletsApplicationLoadBalancerDataCenters", typing.Dict[builtins.str, typing.Any]]]],
        origin_id: builtins.str,
        balancing_type: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        liveness_settings: typing.Optional[typing.Union["CloudletsApplicationLoadBalancerLivenessSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        origin_description: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer akamai_cloudlets_application_load_balancer} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param data_centers: data_centers block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#data_centers CloudletsApplicationLoadBalancer#data_centers}
        :param origin_id: The conditional origin's unique identifier. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#origin_id CloudletsApplicationLoadBalancer#origin_id}
        :param balancing_type: The type of load balancing being performed. Options include WEIGHTED and PERFORMANCE. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#balancing_type CloudletsApplicationLoadBalancer#balancing_type}
        :param description: The load balancer configuration version description. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#description CloudletsApplicationLoadBalancer#description}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#id CloudletsApplicationLoadBalancer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param liveness_settings: liveness_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#liveness_settings CloudletsApplicationLoadBalancer#liveness_settings}
        :param origin_description: The load balancer configuration description. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#origin_description CloudletsApplicationLoadBalancer#origin_description}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fdd9e4e2f0e7f0606ee583cf7351d545d09143bff293e3d290aeff26d659f68)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CloudletsApplicationLoadBalancerConfig(
            data_centers=data_centers,
            origin_id=origin_id,
            balancing_type=balancing_type,
            description=description,
            id=id,
            liveness_settings=liveness_settings,
            origin_description=origin_description,
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
        '''Generates CDKTF code for importing a CloudletsApplicationLoadBalancer resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the CloudletsApplicationLoadBalancer to import.
        :param import_from_id: The id of the existing CloudletsApplicationLoadBalancer that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the CloudletsApplicationLoadBalancer to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9e23ea5c1ddecf87ae70ee8ad6d8a6f70f852eedb36e916df46ba041957e42b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putDataCenters")
    def put_data_centers(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudletsApplicationLoadBalancerDataCenters", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4daae7a77cc7434f84cca4be639254310518002a997fb4963525bc9d1a0910ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDataCenters", [value]))

    @jsii.member(jsii_name="putLivenessSettings")
    def put_liveness_settings(
        self,
        *,
        path: builtins.str,
        port: jsii.Number,
        protocol: builtins.str,
        additional_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        host_header: typing.Optional[builtins.str] = None,
        interval: typing.Optional[jsii.Number] = None,
        peer_certificate_verification: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        request_string: typing.Optional[builtins.str] = None,
        response_string: typing.Optional[builtins.str] = None,
        status3_xx_failure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        status4_xx_failure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        status5_xx_failure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        timeout: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param path: The path to the test object used for liveness testing. The function of the test object is to help determine whether the data center is functioning. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#path CloudletsApplicationLoadBalancer#path}
        :param port: The port for the test object. The default port is 80, which is standard for HTTP. Enter 443 if you are using HTTPS. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#port CloudletsApplicationLoadBalancer#port}
        :param protocol: The protocol or scheme for the database, either HTTP or HTTPS. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#protocol CloudletsApplicationLoadBalancer#protocol}
        :param additional_headers: Maps additional case-insensitive HTTP header names included to the liveness testing requests. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#additional_headers CloudletsApplicationLoadBalancer#additional_headers}
        :param host_header: The Host header for the liveness HTTP request. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#host_header CloudletsApplicationLoadBalancer#host_header}
        :param interval: Describes how often the liveness test will be performed. Optional defaults to 60 seconds, minimum is 10 seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#interval CloudletsApplicationLoadBalancer#interval}
        :param peer_certificate_verification: Describes whether or not to validate the origin certificate for an HTTPS request. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#peer_certificate_verification CloudletsApplicationLoadBalancer#peer_certificate_verification}
        :param request_string: The request which will be used for TCP(S) tests. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#request_string CloudletsApplicationLoadBalancer#request_string}
        :param response_string: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#response_string CloudletsApplicationLoadBalancer#response_string}.
        :param status3_xx_failure: Set to true to mark the liveness test as failed when the request returns a 3xx (redirection) status code. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#status_3xx_failure CloudletsApplicationLoadBalancer#status_3xx_failure}
        :param status4_xx_failure: Set to true to mark the liveness test as failed when the request returns a 4xx (client error) status code. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#status_4xx_failure CloudletsApplicationLoadBalancer#status_4xx_failure}
        :param status5_xx_failure: Set to true to mark the liveness test as failed when the request returns a 5xx (server error) status code. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#status_5xx_failure CloudletsApplicationLoadBalancer#status_5xx_failure}
        :param timeout: The number of seconds the system waits before failing the liveness test. The default is 25 seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#timeout CloudletsApplicationLoadBalancer#timeout}
        '''
        value = CloudletsApplicationLoadBalancerLivenessSettings(
            path=path,
            port=port,
            protocol=protocol,
            additional_headers=additional_headers,
            host_header=host_header,
            interval=interval,
            peer_certificate_verification=peer_certificate_verification,
            request_string=request_string,
            response_string=response_string,
            status3_xx_failure=status3_xx_failure,
            status4_xx_failure=status4_xx_failure,
            status5_xx_failure=status5_xx_failure,
            timeout=timeout,
        )

        return typing.cast(None, jsii.invoke(self, "putLivenessSettings", [value]))

    @jsii.member(jsii_name="resetBalancingType")
    def reset_balancing_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBalancingType", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLivenessSettings")
    def reset_liveness_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLivenessSettings", []))

    @jsii.member(jsii_name="resetOriginDescription")
    def reset_origin_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOriginDescription", []))

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
    @jsii.member(jsii_name="dataCenters")
    def data_centers(self) -> "CloudletsApplicationLoadBalancerDataCentersList":
        return typing.cast("CloudletsApplicationLoadBalancerDataCentersList", jsii.get(self, "dataCenters"))

    @builtins.property
    @jsii.member(jsii_name="livenessSettings")
    def liveness_settings(
        self,
    ) -> "CloudletsApplicationLoadBalancerLivenessSettingsOutputReference":
        return typing.cast("CloudletsApplicationLoadBalancerLivenessSettingsOutputReference", jsii.get(self, "livenessSettings"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="warnings")
    def warnings(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "warnings"))

    @builtins.property
    @jsii.member(jsii_name="balancingTypeInput")
    def balancing_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "balancingTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="dataCentersInput")
    def data_centers_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudletsApplicationLoadBalancerDataCenters"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudletsApplicationLoadBalancerDataCenters"]]], jsii.get(self, "dataCentersInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="livenessSettingsInput")
    def liveness_settings_input(
        self,
    ) -> typing.Optional["CloudletsApplicationLoadBalancerLivenessSettings"]:
        return typing.cast(typing.Optional["CloudletsApplicationLoadBalancerLivenessSettings"], jsii.get(self, "livenessSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="originDescriptionInput")
    def origin_description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "originDescriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="originIdInput")
    def origin_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "originIdInput"))

    @builtins.property
    @jsii.member(jsii_name="balancingType")
    def balancing_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "balancingType"))

    @balancing_type.setter
    def balancing_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ee29745ca61fafcc0819165ca506ee4ac7c06f36792b687492b287ce3073e34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "balancingType", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__480db0df6c10e2996a85f58c35cfeeff479c045b9024c914dbedade89281c46e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6e5ce7380344ef3d4990f55c2ed93fd1aa699d6f37246e0c109b943ff2a5981)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="originDescription")
    def origin_description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "originDescription"))

    @origin_description.setter
    def origin_description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__466b4ea5655ff68cac705b6e9db906b8aa095a809e12bb739f48e9d0e06cf8bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originDescription", value)

    @builtins.property
    @jsii.member(jsii_name="originId")
    def origin_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "originId"))

    @origin_id.setter
    def origin_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91bcffb95712f82d1f0bbc624c61466ecc0778d5d086b7017f4be14da6a91b2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originId", value)


@jsii.data_type(
    jsii_type="akamai.cloudletsApplicationLoadBalancer.CloudletsApplicationLoadBalancerConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "data_centers": "dataCenters",
        "origin_id": "originId",
        "balancing_type": "balancingType",
        "description": "description",
        "id": "id",
        "liveness_settings": "livenessSettings",
        "origin_description": "originDescription",
    },
)
class CloudletsApplicationLoadBalancerConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        data_centers: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudletsApplicationLoadBalancerDataCenters", typing.Dict[builtins.str, typing.Any]]]],
        origin_id: builtins.str,
        balancing_type: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        liveness_settings: typing.Optional[typing.Union["CloudletsApplicationLoadBalancerLivenessSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        origin_description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param data_centers: data_centers block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#data_centers CloudletsApplicationLoadBalancer#data_centers}
        :param origin_id: The conditional origin's unique identifier. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#origin_id CloudletsApplicationLoadBalancer#origin_id}
        :param balancing_type: The type of load balancing being performed. Options include WEIGHTED and PERFORMANCE. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#balancing_type CloudletsApplicationLoadBalancer#balancing_type}
        :param description: The load balancer configuration version description. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#description CloudletsApplicationLoadBalancer#description}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#id CloudletsApplicationLoadBalancer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param liveness_settings: liveness_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#liveness_settings CloudletsApplicationLoadBalancer#liveness_settings}
        :param origin_description: The load balancer configuration description. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#origin_description CloudletsApplicationLoadBalancer#origin_description}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(liveness_settings, dict):
            liveness_settings = CloudletsApplicationLoadBalancerLivenessSettings(**liveness_settings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f379e911f8ae4f9095344a62ef278902d8cedb55487d857cf6b8e5385571af1b)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument data_centers", value=data_centers, expected_type=type_hints["data_centers"])
            check_type(argname="argument origin_id", value=origin_id, expected_type=type_hints["origin_id"])
            check_type(argname="argument balancing_type", value=balancing_type, expected_type=type_hints["balancing_type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument liveness_settings", value=liveness_settings, expected_type=type_hints["liveness_settings"])
            check_type(argname="argument origin_description", value=origin_description, expected_type=type_hints["origin_description"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_centers": data_centers,
            "origin_id": origin_id,
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
        if balancing_type is not None:
            self._values["balancing_type"] = balancing_type
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if liveness_settings is not None:
            self._values["liveness_settings"] = liveness_settings
        if origin_description is not None:
            self._values["origin_description"] = origin_description

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
    def data_centers(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudletsApplicationLoadBalancerDataCenters"]]:
        '''data_centers block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#data_centers CloudletsApplicationLoadBalancer#data_centers}
        '''
        result = self._values.get("data_centers")
        assert result is not None, "Required property 'data_centers' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudletsApplicationLoadBalancerDataCenters"]], result)

    @builtins.property
    def origin_id(self) -> builtins.str:
        '''The conditional origin's unique identifier.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#origin_id CloudletsApplicationLoadBalancer#origin_id}
        '''
        result = self._values.get("origin_id")
        assert result is not None, "Required property 'origin_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def balancing_type(self) -> typing.Optional[builtins.str]:
        '''The type of load balancing being performed. Options include WEIGHTED and PERFORMANCE.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#balancing_type CloudletsApplicationLoadBalancer#balancing_type}
        '''
        result = self._values.get("balancing_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The load balancer configuration version description.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#description CloudletsApplicationLoadBalancer#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#id CloudletsApplicationLoadBalancer#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def liveness_settings(
        self,
    ) -> typing.Optional["CloudletsApplicationLoadBalancerLivenessSettings"]:
        '''liveness_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#liveness_settings CloudletsApplicationLoadBalancer#liveness_settings}
        '''
        result = self._values.get("liveness_settings")
        return typing.cast(typing.Optional["CloudletsApplicationLoadBalancerLivenessSettings"], result)

    @builtins.property
    def origin_description(self) -> typing.Optional[builtins.str]:
        '''The load balancer configuration description.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#origin_description CloudletsApplicationLoadBalancer#origin_description}
        '''
        result = self._values.get("origin_description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudletsApplicationLoadBalancerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.cloudletsApplicationLoadBalancer.CloudletsApplicationLoadBalancerDataCenters",
    jsii_struct_bases=[],
    name_mapping={
        "continent": "continent",
        "country": "country",
        "latitude": "latitude",
        "longitude": "longitude",
        "origin_id": "originId",
        "percent": "percent",
        "city": "city",
        "cloud_server_host_header_override": "cloudServerHostHeaderOverride",
        "cloud_service": "cloudService",
        "hostname": "hostname",
        "liveness_hosts": "livenessHosts",
        "state_or_province": "stateOrProvince",
    },
)
class CloudletsApplicationLoadBalancerDataCenters:
    def __init__(
        self,
        *,
        continent: builtins.str,
        country: builtins.str,
        latitude: jsii.Number,
        longitude: jsii.Number,
        origin_id: builtins.str,
        percent: jsii.Number,
        city: typing.Optional[builtins.str] = None,
        cloud_server_host_header_override: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        cloud_service: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        hostname: typing.Optional[builtins.str] = None,
        liveness_hosts: typing.Optional[typing.Sequence[builtins.str]] = None,
        state_or_province: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param continent: The continent on which the data center is located. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#continent CloudletsApplicationLoadBalancer#continent}
        :param country: The country in which the data center is located. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#country CloudletsApplicationLoadBalancer#country}
        :param latitude: The latitude value for the data center. This member supports six decimal places of precision. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#latitude CloudletsApplicationLoadBalancer#latitude}
        :param longitude: The longitude value for the data center. This member supports six decimal places of precision. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#longitude CloudletsApplicationLoadBalancer#longitude}
        :param origin_id: The ID of an origin that represents the data center. The conditional origin, which is defined in the Property Manager API, must have an originType of either CUSTOMER or NET_STORAGE Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#origin_id CloudletsApplicationLoadBalancer#origin_id}
        :param percent: The percent of traffic that is sent to the data center. The total for all data centers must equal 100%. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#percent CloudletsApplicationLoadBalancer#percent}
        :param city: The city in which the data center is located. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#city CloudletsApplicationLoadBalancer#city}
        :param cloud_server_host_header_override: Describes if cloud server host header is overridden. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#cloud_server_host_header_override CloudletsApplicationLoadBalancer#cloud_server_host_header_override}
        :param cloud_service: Describes if this datacenter is a cloud service. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#cloud_service CloudletsApplicationLoadBalancer#cloud_service}
        :param hostname: This should match the 'hostname' value defined for this datacenter in Property Manager. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#hostname CloudletsApplicationLoadBalancer#hostname}
        :param liveness_hosts: An array of strings that represent the origin servers used to poll the data centers in an application load balancer configuration. These servers support basic HTTP polling. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#liveness_hosts CloudletsApplicationLoadBalancer#liveness_hosts}
        :param state_or_province: The state, province, or region where the data center is located. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#state_or_province CloudletsApplicationLoadBalancer#state_or_province}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f6323bee64f67a4a9960a4e6403b148d9f2eba07b61e172b2cee6ccebf25a24)
            check_type(argname="argument continent", value=continent, expected_type=type_hints["continent"])
            check_type(argname="argument country", value=country, expected_type=type_hints["country"])
            check_type(argname="argument latitude", value=latitude, expected_type=type_hints["latitude"])
            check_type(argname="argument longitude", value=longitude, expected_type=type_hints["longitude"])
            check_type(argname="argument origin_id", value=origin_id, expected_type=type_hints["origin_id"])
            check_type(argname="argument percent", value=percent, expected_type=type_hints["percent"])
            check_type(argname="argument city", value=city, expected_type=type_hints["city"])
            check_type(argname="argument cloud_server_host_header_override", value=cloud_server_host_header_override, expected_type=type_hints["cloud_server_host_header_override"])
            check_type(argname="argument cloud_service", value=cloud_service, expected_type=type_hints["cloud_service"])
            check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
            check_type(argname="argument liveness_hosts", value=liveness_hosts, expected_type=type_hints["liveness_hosts"])
            check_type(argname="argument state_or_province", value=state_or_province, expected_type=type_hints["state_or_province"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "continent": continent,
            "country": country,
            "latitude": latitude,
            "longitude": longitude,
            "origin_id": origin_id,
            "percent": percent,
        }
        if city is not None:
            self._values["city"] = city
        if cloud_server_host_header_override is not None:
            self._values["cloud_server_host_header_override"] = cloud_server_host_header_override
        if cloud_service is not None:
            self._values["cloud_service"] = cloud_service
        if hostname is not None:
            self._values["hostname"] = hostname
        if liveness_hosts is not None:
            self._values["liveness_hosts"] = liveness_hosts
        if state_or_province is not None:
            self._values["state_or_province"] = state_or_province

    @builtins.property
    def continent(self) -> builtins.str:
        '''The continent on which the data center is located.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#continent CloudletsApplicationLoadBalancer#continent}
        '''
        result = self._values.get("continent")
        assert result is not None, "Required property 'continent' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def country(self) -> builtins.str:
        '''The country in which the data center is located.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#country CloudletsApplicationLoadBalancer#country}
        '''
        result = self._values.get("country")
        assert result is not None, "Required property 'country' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def latitude(self) -> jsii.Number:
        '''The latitude value for the data center. This member supports six decimal places of precision.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#latitude CloudletsApplicationLoadBalancer#latitude}
        '''
        result = self._values.get("latitude")
        assert result is not None, "Required property 'latitude' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def longitude(self) -> jsii.Number:
        '''The longitude value for the data center. This member supports six decimal places of precision.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#longitude CloudletsApplicationLoadBalancer#longitude}
        '''
        result = self._values.get("longitude")
        assert result is not None, "Required property 'longitude' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def origin_id(self) -> builtins.str:
        '''The ID of an origin that represents the data center.

        The conditional origin, which is defined in the Property Manager API, must have an originType of either CUSTOMER or NET_STORAGE

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#origin_id CloudletsApplicationLoadBalancer#origin_id}
        '''
        result = self._values.get("origin_id")
        assert result is not None, "Required property 'origin_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def percent(self) -> jsii.Number:
        '''The percent of traffic that is sent to the data center.

        The total for all data centers must equal 100%.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#percent CloudletsApplicationLoadBalancer#percent}
        '''
        result = self._values.get("percent")
        assert result is not None, "Required property 'percent' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def city(self) -> typing.Optional[builtins.str]:
        '''The city in which the data center is located.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#city CloudletsApplicationLoadBalancer#city}
        '''
        result = self._values.get("city")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloud_server_host_header_override(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Describes if cloud server host header is overridden.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#cloud_server_host_header_override CloudletsApplicationLoadBalancer#cloud_server_host_header_override}
        '''
        result = self._values.get("cloud_server_host_header_override")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def cloud_service(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Describes if this datacenter is a cloud service.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#cloud_service CloudletsApplicationLoadBalancer#cloud_service}
        '''
        result = self._values.get("cloud_service")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def hostname(self) -> typing.Optional[builtins.str]:
        '''This should match the 'hostname' value defined for this datacenter in Property Manager.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#hostname CloudletsApplicationLoadBalancer#hostname}
        '''
        result = self._values.get("hostname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def liveness_hosts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of strings that represent the origin servers used to poll the data centers in an application load balancer configuration.

        These servers support basic HTTP polling.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#liveness_hosts CloudletsApplicationLoadBalancer#liveness_hosts}
        '''
        result = self._values.get("liveness_hosts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def state_or_province(self) -> typing.Optional[builtins.str]:
        '''The state, province, or region where the data center is located.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#state_or_province CloudletsApplicationLoadBalancer#state_or_province}
        '''
        result = self._values.get("state_or_province")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudletsApplicationLoadBalancerDataCenters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudletsApplicationLoadBalancerDataCentersList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.cloudletsApplicationLoadBalancer.CloudletsApplicationLoadBalancerDataCentersList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ffaf6c4cabc400749ad9a2737e937c45406b2cd7a6396e8d7d06f4aba4bec746)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CloudletsApplicationLoadBalancerDataCentersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e6cd781eec868b4be65c9d53f0d5b2fc30d2c14e18b388665a0a5eaf476579a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudletsApplicationLoadBalancerDataCentersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9de67ea8f629e9aaec0722b95ee014438aa7aa26d41d79f3a2fd2f9fc2f6379e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8c6963b681d9c234e18c17548ae4f92f939864a114fcf5ecd76afd50c971640f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bdcee22c767989a7d3c5dbd20f20a42b0bd0dd12ae423d1b2e3609bc70b563b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudletsApplicationLoadBalancerDataCenters]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudletsApplicationLoadBalancerDataCenters]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudletsApplicationLoadBalancerDataCenters]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7a92089cbf2d0bdafedd3f3013843dda53345daba7963f08494220dff6d6ef8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudletsApplicationLoadBalancerDataCentersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.cloudletsApplicationLoadBalancer.CloudletsApplicationLoadBalancerDataCentersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__618669e436306cedba42c7e1cf98c3b4a3d81bb07865d1d440b9b77186465a52)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCity")
    def reset_city(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCity", []))

    @jsii.member(jsii_name="resetCloudServerHostHeaderOverride")
    def reset_cloud_server_host_header_override(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudServerHostHeaderOverride", []))

    @jsii.member(jsii_name="resetCloudService")
    def reset_cloud_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudService", []))

    @jsii.member(jsii_name="resetHostname")
    def reset_hostname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostname", []))

    @jsii.member(jsii_name="resetLivenessHosts")
    def reset_liveness_hosts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLivenessHosts", []))

    @jsii.member(jsii_name="resetStateOrProvince")
    def reset_state_or_province(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStateOrProvince", []))

    @builtins.property
    @jsii.member(jsii_name="cityInput")
    def city_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cityInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudServerHostHeaderOverrideInput")
    def cloud_server_host_header_override_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "cloudServerHostHeaderOverrideInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudServiceInput")
    def cloud_service_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "cloudServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="continentInput")
    def continent_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "continentInput"))

    @builtins.property
    @jsii.member(jsii_name="countryInput")
    def country_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "countryInput"))

    @builtins.property
    @jsii.member(jsii_name="hostnameInput")
    def hostname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="latitudeInput")
    def latitude_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "latitudeInput"))

    @builtins.property
    @jsii.member(jsii_name="livenessHostsInput")
    def liveness_hosts_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "livenessHostsInput"))

    @builtins.property
    @jsii.member(jsii_name="longitudeInput")
    def longitude_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "longitudeInput"))

    @builtins.property
    @jsii.member(jsii_name="originIdInput")
    def origin_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "originIdInput"))

    @builtins.property
    @jsii.member(jsii_name="percentInput")
    def percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "percentInput"))

    @builtins.property
    @jsii.member(jsii_name="stateOrProvinceInput")
    def state_or_province_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateOrProvinceInput"))

    @builtins.property
    @jsii.member(jsii_name="city")
    def city(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "city"))

    @city.setter
    def city(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a6f2a0a833ed0a4d25ecdf8ed9b28e24b18b22d80a917b0a55239cf02bc89c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "city", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__8bb65f2138ff7ebe0ecfb1dbe70e355fa193d1da85bebf796765e32e241b2020)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudServerHostHeaderOverride", value)

    @builtins.property
    @jsii.member(jsii_name="cloudService")
    def cloud_service(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "cloudService"))

    @cloud_service.setter
    def cloud_service(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d02bd99b7ff2931e0bfcaf6fb6b42b05188f15eea8dba92ce2615e8e22fcb5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudService", value)

    @builtins.property
    @jsii.member(jsii_name="continent")
    def continent(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "continent"))

    @continent.setter
    def continent(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a3ae972a693f8c4a90d3405b6dd8b86cffbe542752430b72018acee113ff7a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "continent", value)

    @builtins.property
    @jsii.member(jsii_name="country")
    def country(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "country"))

    @country.setter
    def country(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__178a0652f938b484930b5158b42e6269b699ee7eecfb8d6f1587f44c5648cf3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "country", value)

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostname"))

    @hostname.setter
    def hostname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7688b1c0e696237c229c5daff87dffe0c69484600ca4cbb08c4495a16241e6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostname", value)

    @builtins.property
    @jsii.member(jsii_name="latitude")
    def latitude(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "latitude"))

    @latitude.setter
    def latitude(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cadc4c15def75f253cc07cf7fa8e3a26a5a482d9d322b3d277f851599373c474)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "latitude", value)

    @builtins.property
    @jsii.member(jsii_name="livenessHosts")
    def liveness_hosts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "livenessHosts"))

    @liveness_hosts.setter
    def liveness_hosts(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__997de3dbdf4f7a5288efcc9da51e02bc97b2002392c16fd1972fb0c2eb945b74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "livenessHosts", value)

    @builtins.property
    @jsii.member(jsii_name="longitude")
    def longitude(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "longitude"))

    @longitude.setter
    def longitude(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__330b5608c2f85ca19bf32c88969fd81b7c34aa768c996ad4a6309d5dc46a3e39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "longitude", value)

    @builtins.property
    @jsii.member(jsii_name="originId")
    def origin_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "originId"))

    @origin_id.setter
    def origin_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c85ba84b9eea170a7f515c15de05c9add33bb7d9f1bce2254f47509683a07332)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originId", value)

    @builtins.property
    @jsii.member(jsii_name="percent")
    def percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "percent"))

    @percent.setter
    def percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c317118bbdad360d4d1c59b75056c35644a8f51e53caed2c0304c6a5705c8d92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "percent", value)

    @builtins.property
    @jsii.member(jsii_name="stateOrProvince")
    def state_or_province(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stateOrProvince"))

    @state_or_province.setter
    def state_or_province(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8e8e925529c03fffbc454c96cfd1ec41077b25a1b686c81c469c0c6b8c8b449)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stateOrProvince", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CloudletsApplicationLoadBalancerDataCenters]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CloudletsApplicationLoadBalancerDataCenters]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CloudletsApplicationLoadBalancerDataCenters]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c724d0ca3f90df85390cc7b67a91bcfa2a3ff7a8359adbbda2c84d69da00b3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.cloudletsApplicationLoadBalancer.CloudletsApplicationLoadBalancerLivenessSettings",
    jsii_struct_bases=[],
    name_mapping={
        "path": "path",
        "port": "port",
        "protocol": "protocol",
        "additional_headers": "additionalHeaders",
        "host_header": "hostHeader",
        "interval": "interval",
        "peer_certificate_verification": "peerCertificateVerification",
        "request_string": "requestString",
        "response_string": "responseString",
        "status3_xx_failure": "status3XxFailure",
        "status4_xx_failure": "status4XxFailure",
        "status5_xx_failure": "status5XxFailure",
        "timeout": "timeout",
    },
)
class CloudletsApplicationLoadBalancerLivenessSettings:
    def __init__(
        self,
        *,
        path: builtins.str,
        port: jsii.Number,
        protocol: builtins.str,
        additional_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        host_header: typing.Optional[builtins.str] = None,
        interval: typing.Optional[jsii.Number] = None,
        peer_certificate_verification: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        request_string: typing.Optional[builtins.str] = None,
        response_string: typing.Optional[builtins.str] = None,
        status3_xx_failure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        status4_xx_failure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        status5_xx_failure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        timeout: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param path: The path to the test object used for liveness testing. The function of the test object is to help determine whether the data center is functioning. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#path CloudletsApplicationLoadBalancer#path}
        :param port: The port for the test object. The default port is 80, which is standard for HTTP. Enter 443 if you are using HTTPS. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#port CloudletsApplicationLoadBalancer#port}
        :param protocol: The protocol or scheme for the database, either HTTP or HTTPS. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#protocol CloudletsApplicationLoadBalancer#protocol}
        :param additional_headers: Maps additional case-insensitive HTTP header names included to the liveness testing requests. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#additional_headers CloudletsApplicationLoadBalancer#additional_headers}
        :param host_header: The Host header for the liveness HTTP request. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#host_header CloudletsApplicationLoadBalancer#host_header}
        :param interval: Describes how often the liveness test will be performed. Optional defaults to 60 seconds, minimum is 10 seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#interval CloudletsApplicationLoadBalancer#interval}
        :param peer_certificate_verification: Describes whether or not to validate the origin certificate for an HTTPS request. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#peer_certificate_verification CloudletsApplicationLoadBalancer#peer_certificate_verification}
        :param request_string: The request which will be used for TCP(S) tests. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#request_string CloudletsApplicationLoadBalancer#request_string}
        :param response_string: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#response_string CloudletsApplicationLoadBalancer#response_string}.
        :param status3_xx_failure: Set to true to mark the liveness test as failed when the request returns a 3xx (redirection) status code. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#status_3xx_failure CloudletsApplicationLoadBalancer#status_3xx_failure}
        :param status4_xx_failure: Set to true to mark the liveness test as failed when the request returns a 4xx (client error) status code. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#status_4xx_failure CloudletsApplicationLoadBalancer#status_4xx_failure}
        :param status5_xx_failure: Set to true to mark the liveness test as failed when the request returns a 5xx (server error) status code. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#status_5xx_failure CloudletsApplicationLoadBalancer#status_5xx_failure}
        :param timeout: The number of seconds the system waits before failing the liveness test. The default is 25 seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#timeout CloudletsApplicationLoadBalancer#timeout}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9115454a1c12ea99b2f45725773aeedb69839354b2841d5cbfb0ebe4d0baa5f)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument additional_headers", value=additional_headers, expected_type=type_hints["additional_headers"])
            check_type(argname="argument host_header", value=host_header, expected_type=type_hints["host_header"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument peer_certificate_verification", value=peer_certificate_verification, expected_type=type_hints["peer_certificate_verification"])
            check_type(argname="argument request_string", value=request_string, expected_type=type_hints["request_string"])
            check_type(argname="argument response_string", value=response_string, expected_type=type_hints["response_string"])
            check_type(argname="argument status3_xx_failure", value=status3_xx_failure, expected_type=type_hints["status3_xx_failure"])
            check_type(argname="argument status4_xx_failure", value=status4_xx_failure, expected_type=type_hints["status4_xx_failure"])
            check_type(argname="argument status5_xx_failure", value=status5_xx_failure, expected_type=type_hints["status5_xx_failure"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "path": path,
            "port": port,
            "protocol": protocol,
        }
        if additional_headers is not None:
            self._values["additional_headers"] = additional_headers
        if host_header is not None:
            self._values["host_header"] = host_header
        if interval is not None:
            self._values["interval"] = interval
        if peer_certificate_verification is not None:
            self._values["peer_certificate_verification"] = peer_certificate_verification
        if request_string is not None:
            self._values["request_string"] = request_string
        if response_string is not None:
            self._values["response_string"] = response_string
        if status3_xx_failure is not None:
            self._values["status3_xx_failure"] = status3_xx_failure
        if status4_xx_failure is not None:
            self._values["status4_xx_failure"] = status4_xx_failure
        if status5_xx_failure is not None:
            self._values["status5_xx_failure"] = status5_xx_failure
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def path(self) -> builtins.str:
        '''The path to the test object used for liveness testing.

        The function of the test object is to help determine whether the data center is functioning.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#path CloudletsApplicationLoadBalancer#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''The port for the test object.

        The default port is 80, which is standard for HTTP. Enter 443 if you are using HTTPS.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#port CloudletsApplicationLoadBalancer#port}
        '''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''The protocol or scheme for the database, either HTTP or HTTPS.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#protocol CloudletsApplicationLoadBalancer#protocol}
        '''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Maps additional case-insensitive HTTP header names included to the liveness testing requests.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#additional_headers CloudletsApplicationLoadBalancer#additional_headers}
        '''
        result = self._values.get("additional_headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def host_header(self) -> typing.Optional[builtins.str]:
        '''The Host header for the liveness HTTP request.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#host_header CloudletsApplicationLoadBalancer#host_header}
        '''
        result = self._values.get("host_header")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def interval(self) -> typing.Optional[jsii.Number]:
        '''Describes how often the liveness test will be performed. Optional defaults to 60 seconds, minimum is 10 seconds.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#interval CloudletsApplicationLoadBalancer#interval}
        '''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def peer_certificate_verification(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Describes whether or not to validate the origin certificate for an HTTPS request.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#peer_certificate_verification CloudletsApplicationLoadBalancer#peer_certificate_verification}
        '''
        result = self._values.get("peer_certificate_verification")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def request_string(self) -> typing.Optional[builtins.str]:
        '''The request which will be used for TCP(S) tests.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#request_string CloudletsApplicationLoadBalancer#request_string}
        '''
        result = self._values.get("request_string")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def response_string(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#response_string CloudletsApplicationLoadBalancer#response_string}.'''
        result = self._values.get("response_string")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status3_xx_failure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set to true to mark the liveness test as failed when the request returns a 3xx (redirection) status code.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#status_3xx_failure CloudletsApplicationLoadBalancer#status_3xx_failure}
        '''
        result = self._values.get("status3_xx_failure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def status4_xx_failure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set to true to mark the liveness test as failed when the request returns a 4xx (client error) status code.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#status_4xx_failure CloudletsApplicationLoadBalancer#status_4xx_failure}
        '''
        result = self._values.get("status4_xx_failure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def status5_xx_failure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set to true to mark the liveness test as failed when the request returns a 5xx (server error) status code.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#status_5xx_failure CloudletsApplicationLoadBalancer#status_5xx_failure}
        '''
        result = self._values.get("status5_xx_failure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def timeout(self) -> typing.Optional[jsii.Number]:
        '''The number of seconds the system waits before failing the liveness test. The default is 25 seconds.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cloudlets_application_load_balancer#timeout CloudletsApplicationLoadBalancer#timeout}
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudletsApplicationLoadBalancerLivenessSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudletsApplicationLoadBalancerLivenessSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.cloudletsApplicationLoadBalancer.CloudletsApplicationLoadBalancerLivenessSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b660c763bffaa97080cd5bc94a7a507a710e085ca82c7d94b017bb7a8b645bb9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAdditionalHeaders")
    def reset_additional_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalHeaders", []))

    @jsii.member(jsii_name="resetHostHeader")
    def reset_host_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostHeader", []))

    @jsii.member(jsii_name="resetInterval")
    def reset_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterval", []))

    @jsii.member(jsii_name="resetPeerCertificateVerification")
    def reset_peer_certificate_verification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeerCertificateVerification", []))

    @jsii.member(jsii_name="resetRequestString")
    def reset_request_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestString", []))

    @jsii.member(jsii_name="resetResponseString")
    def reset_response_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseString", []))

    @jsii.member(jsii_name="resetStatus3XxFailure")
    def reset_status3_xx_failure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus3XxFailure", []))

    @jsii.member(jsii_name="resetStatus4XxFailure")
    def reset_status4_xx_failure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus4XxFailure", []))

    @jsii.member(jsii_name="resetStatus5XxFailure")
    def reset_status5_xx_failure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus5XxFailure", []))

    @jsii.member(jsii_name="resetTimeout")
    def reset_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeout", []))

    @builtins.property
    @jsii.member(jsii_name="additionalHeadersInput")
    def additional_headers_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "additionalHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="hostHeaderInput")
    def host_header_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="peerCertificateVerificationInput")
    def peer_certificate_verification_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "peerCertificateVerificationInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="requestStringInput")
    def request_string_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "requestStringInput"))

    @builtins.property
    @jsii.member(jsii_name="responseStringInput")
    def response_string_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseStringInput"))

    @builtins.property
    @jsii.member(jsii_name="status3XxFailureInput")
    def status3_xx_failure_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "status3XxFailureInput"))

    @builtins.property
    @jsii.member(jsii_name="status4XxFailureInput")
    def status4_xx_failure_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "status4XxFailureInput"))

    @builtins.property
    @jsii.member(jsii_name="status5XxFailureInput")
    def status5_xx_failure_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "status5XxFailureInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="additionalHeaders")
    def additional_headers(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "additionalHeaders"))

    @additional_headers.setter
    def additional_headers(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__706b225fabc6339cbbf0d41fe9d2b11bca48a54984b13bf6d29a7aba0e35776d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="hostHeader")
    def host_header(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostHeader"))

    @host_header.setter
    def host_header(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0433b2bea4fde48a2253cfdb8dfffdb67e5e581a7d6a96b7d5ec6aeb86a3acf4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostHeader", value)

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1505c4f6d0b53460450c3722761352df785d5e4397387561e00fa6d99d5d9c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__358dfb532e99626e905c21b2af7d572f3289b521cfa810f53df23b880c9be1ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__82bd970c5e3264eba5e054d89e91db6684d2797d3f8f4780461db28d2a57a246)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "peerCertificateVerification", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc36ecb2b3b22017091e794702b15eb644582f3fe7375197e61c62a34c73c072)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b9cf4623503a12aa834c2801fcc628755d7dfec9b7f4926dc9d49f92d9027c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="requestString")
    def request_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "requestString"))

    @request_string.setter
    def request_string(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21016c40509490f4f6b4277339b9ccfda674a58dfe322c23dd14a40db01ea53b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestString", value)

    @builtins.property
    @jsii.member(jsii_name="responseString")
    def response_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseString"))

    @response_string.setter
    def response_string(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6b362c263363a028456efcc99f77e954638d8321f67752bd732cec315984c12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseString", value)

    @builtins.property
    @jsii.member(jsii_name="status3XxFailure")
    def status3_xx_failure(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "status3XxFailure"))

    @status3_xx_failure.setter
    def status3_xx_failure(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d7803822d98973e287e06703954fdfa7b1e194fc8c22744e6d497ec7a33630c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status3XxFailure", value)

    @builtins.property
    @jsii.member(jsii_name="status4XxFailure")
    def status4_xx_failure(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "status4XxFailure"))

    @status4_xx_failure.setter
    def status4_xx_failure(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16d65feb97d97c40e74b0c95049e6babc6b4f04f583af2f8119b1aedb4ee516d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status4XxFailure", value)

    @builtins.property
    @jsii.member(jsii_name="status5XxFailure")
    def status5_xx_failure(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "status5XxFailure"))

    @status5_xx_failure.setter
    def status5_xx_failure(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1ce434ee7f170310ef4953b5181eda5022f5f171a7069ced61fe6bab235371b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status5XxFailure", value)

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23cee8f5ed07015e0763d65058c1c153fb00bf2a05ba77845290f62b8090d8a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeout", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudletsApplicationLoadBalancerLivenessSettings]:
        return typing.cast(typing.Optional[CloudletsApplicationLoadBalancerLivenessSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudletsApplicationLoadBalancerLivenessSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2720fe785d31753be2e461dcf27d376e3946c45a1ed604f88c9b24447eeb0dd8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CloudletsApplicationLoadBalancer",
    "CloudletsApplicationLoadBalancerConfig",
    "CloudletsApplicationLoadBalancerDataCenters",
    "CloudletsApplicationLoadBalancerDataCentersList",
    "CloudletsApplicationLoadBalancerDataCentersOutputReference",
    "CloudletsApplicationLoadBalancerLivenessSettings",
    "CloudletsApplicationLoadBalancerLivenessSettingsOutputReference",
]

publication.publish()

def _typecheckingstub__3fdd9e4e2f0e7f0606ee583cf7351d545d09143bff293e3d290aeff26d659f68(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    data_centers: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudletsApplicationLoadBalancerDataCenters, typing.Dict[builtins.str, typing.Any]]]],
    origin_id: builtins.str,
    balancing_type: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    liveness_settings: typing.Optional[typing.Union[CloudletsApplicationLoadBalancerLivenessSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    origin_description: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__a9e23ea5c1ddecf87ae70ee8ad6d8a6f70f852eedb36e916df46ba041957e42b(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4daae7a77cc7434f84cca4be639254310518002a997fb4963525bc9d1a0910ba(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudletsApplicationLoadBalancerDataCenters, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ee29745ca61fafcc0819165ca506ee4ac7c06f36792b687492b287ce3073e34(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__480db0df6c10e2996a85f58c35cfeeff479c045b9024c914dbedade89281c46e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6e5ce7380344ef3d4990f55c2ed93fd1aa699d6f37246e0c109b943ff2a5981(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__466b4ea5655ff68cac705b6e9db906b8aa095a809e12bb739f48e9d0e06cf8bf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91bcffb95712f82d1f0bbc624c61466ecc0778d5d086b7017f4be14da6a91b2b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f379e911f8ae4f9095344a62ef278902d8cedb55487d857cf6b8e5385571af1b(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    data_centers: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudletsApplicationLoadBalancerDataCenters, typing.Dict[builtins.str, typing.Any]]]],
    origin_id: builtins.str,
    balancing_type: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    liveness_settings: typing.Optional[typing.Union[CloudletsApplicationLoadBalancerLivenessSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    origin_description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f6323bee64f67a4a9960a4e6403b148d9f2eba07b61e172b2cee6ccebf25a24(
    *,
    continent: builtins.str,
    country: builtins.str,
    latitude: jsii.Number,
    longitude: jsii.Number,
    origin_id: builtins.str,
    percent: jsii.Number,
    city: typing.Optional[builtins.str] = None,
    cloud_server_host_header_override: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    cloud_service: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    hostname: typing.Optional[builtins.str] = None,
    liveness_hosts: typing.Optional[typing.Sequence[builtins.str]] = None,
    state_or_province: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffaf6c4cabc400749ad9a2737e937c45406b2cd7a6396e8d7d06f4aba4bec746(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e6cd781eec868b4be65c9d53f0d5b2fc30d2c14e18b388665a0a5eaf476579a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9de67ea8f629e9aaec0722b95ee014438aa7aa26d41d79f3a2fd2f9fc2f6379e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c6963b681d9c234e18c17548ae4f92f939864a114fcf5ecd76afd50c971640f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdcee22c767989a7d3c5dbd20f20a42b0bd0dd12ae423d1b2e3609bc70b563b8(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7a92089cbf2d0bdafedd3f3013843dda53345daba7963f08494220dff6d6ef8(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudletsApplicationLoadBalancerDataCenters]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__618669e436306cedba42c7e1cf98c3b4a3d81bb07865d1d440b9b77186465a52(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a6f2a0a833ed0a4d25ecdf8ed9b28e24b18b22d80a917b0a55239cf02bc89c0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bb65f2138ff7ebe0ecfb1dbe70e355fa193d1da85bebf796765e32e241b2020(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d02bd99b7ff2931e0bfcaf6fb6b42b05188f15eea8dba92ce2615e8e22fcb5f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a3ae972a693f8c4a90d3405b6dd8b86cffbe542752430b72018acee113ff7a6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__178a0652f938b484930b5158b42e6269b699ee7eecfb8d6f1587f44c5648cf3f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7688b1c0e696237c229c5daff87dffe0c69484600ca4cbb08c4495a16241e6c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cadc4c15def75f253cc07cf7fa8e3a26a5a482d9d322b3d277f851599373c474(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__997de3dbdf4f7a5288efcc9da51e02bc97b2002392c16fd1972fb0c2eb945b74(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__330b5608c2f85ca19bf32c88969fd81b7c34aa768c996ad4a6309d5dc46a3e39(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c85ba84b9eea170a7f515c15de05c9add33bb7d9f1bce2254f47509683a07332(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c317118bbdad360d4d1c59b75056c35644a8f51e53caed2c0304c6a5705c8d92(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8e8e925529c03fffbc454c96cfd1ec41077b25a1b686c81c469c0c6b8c8b449(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c724d0ca3f90df85390cc7b67a91bcfa2a3ff7a8359adbbda2c84d69da00b3c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CloudletsApplicationLoadBalancerDataCenters]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9115454a1c12ea99b2f45725773aeedb69839354b2841d5cbfb0ebe4d0baa5f(
    *,
    path: builtins.str,
    port: jsii.Number,
    protocol: builtins.str,
    additional_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    host_header: typing.Optional[builtins.str] = None,
    interval: typing.Optional[jsii.Number] = None,
    peer_certificate_verification: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    request_string: typing.Optional[builtins.str] = None,
    response_string: typing.Optional[builtins.str] = None,
    status3_xx_failure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    status4_xx_failure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    status5_xx_failure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    timeout: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b660c763bffaa97080cd5bc94a7a507a710e085ca82c7d94b017bb7a8b645bb9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__706b225fabc6339cbbf0d41fe9d2b11bca48a54984b13bf6d29a7aba0e35776d(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0433b2bea4fde48a2253cfdb8dfffdb67e5e581a7d6a96b7d5ec6aeb86a3acf4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1505c4f6d0b53460450c3722761352df785d5e4397387561e00fa6d99d5d9c2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__358dfb532e99626e905c21b2af7d572f3289b521cfa810f53df23b880c9be1ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82bd970c5e3264eba5e054d89e91db6684d2797d3f8f4780461db28d2a57a246(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc36ecb2b3b22017091e794702b15eb644582f3fe7375197e61c62a34c73c072(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b9cf4623503a12aa834c2801fcc628755d7dfec9b7f4926dc9d49f92d9027c8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21016c40509490f4f6b4277339b9ccfda674a58dfe322c23dd14a40db01ea53b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6b362c263363a028456efcc99f77e954638d8321f67752bd732cec315984c12(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d7803822d98973e287e06703954fdfa7b1e194fc8c22744e6d497ec7a33630c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16d65feb97d97c40e74b0c95049e6babc6b4f04f583af2f8119b1aedb4ee516d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1ce434ee7f170310ef4953b5181eda5022f5f171a7069ced61fe6bab235371b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23cee8f5ed07015e0763d65058c1c153fb00bf2a05ba77845290f62b8090d8a2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2720fe785d31753be2e461dcf27d376e3946c45a1ed604f88c9b24447eeb0dd8(
    value: typing.Optional[CloudletsApplicationLoadBalancerLivenessSettings],
) -> None:
    """Type checking stubs"""
    pass
