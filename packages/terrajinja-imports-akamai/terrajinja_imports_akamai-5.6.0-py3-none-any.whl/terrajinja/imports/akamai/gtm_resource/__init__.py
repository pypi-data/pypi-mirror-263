'''
# `akamai_gtm_resource`

Refer to the Terraform Registry for docs: [`akamai_gtm_resource`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource).
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


class GtmResource(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.gtmResource.GtmResource",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource akamai_gtm_resource}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        aggregation_type: builtins.str,
        domain: builtins.str,
        name: builtins.str,
        type: builtins.str,
        constrained_property: typing.Optional[builtins.str] = None,
        decay_rate: typing.Optional[jsii.Number] = None,
        description: typing.Optional[builtins.str] = None,
        host_header: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        leader_string: typing.Optional[builtins.str] = None,
        least_squares_decay: typing.Optional[jsii.Number] = None,
        load_imbalance_percentage: typing.Optional[jsii.Number] = None,
        max_u_multiplicative_increment: typing.Optional[jsii.Number] = None,
        resource_instance: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GtmResourceResourceInstance", typing.Dict[builtins.str, typing.Any]]]]] = None,
        upper_bound: typing.Optional[jsii.Number] = None,
        wait_on_complete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource akamai_gtm_resource} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param aggregation_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#aggregation_type GtmResource#aggregation_type}.
        :param domain: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#domain GtmResource#domain}.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#name GtmResource#name}.
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#type GtmResource#type}.
        :param constrained_property: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#constrained_property GtmResource#constrained_property}.
        :param decay_rate: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#decay_rate GtmResource#decay_rate}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#description GtmResource#description}.
        :param host_header: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#host_header GtmResource#host_header}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#id GtmResource#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param leader_string: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#leader_string GtmResource#leader_string}.
        :param least_squares_decay: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#least_squares_decay GtmResource#least_squares_decay}.
        :param load_imbalance_percentage: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#load_imbalance_percentage GtmResource#load_imbalance_percentage}.
        :param max_u_multiplicative_increment: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#max_u_multiplicative_increment GtmResource#max_u_multiplicative_increment}.
        :param resource_instance: resource_instance block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#resource_instance GtmResource#resource_instance}
        :param upper_bound: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#upper_bound GtmResource#upper_bound}.
        :param wait_on_complete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#wait_on_complete GtmResource#wait_on_complete}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01f4edabcceb50dfcfcfa1c5e9f3e2a8cdc0f7678152ce5ac4d45b5c7204af84)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GtmResourceConfig(
            aggregation_type=aggregation_type,
            domain=domain,
            name=name,
            type=type,
            constrained_property=constrained_property,
            decay_rate=decay_rate,
            description=description,
            host_header=host_header,
            id=id,
            leader_string=leader_string,
            least_squares_decay=least_squares_decay,
            load_imbalance_percentage=load_imbalance_percentage,
            max_u_multiplicative_increment=max_u_multiplicative_increment,
            resource_instance=resource_instance,
            upper_bound=upper_bound,
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
        '''Generates CDKTF code for importing a GtmResource resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the GtmResource to import.
        :param import_from_id: The id of the existing GtmResource that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the GtmResource to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__594221324a358e6e38e777b551c4abe248c83b4cab88412317e9c136f9dc2e1f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putResourceInstance")
    def put_resource_instance(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GtmResourceResourceInstance", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9c2a20ee1b51b2f6c8f021880717f3dacaf43a4bacb56f85224cc38b5238908)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putResourceInstance", [value]))

    @jsii.member(jsii_name="resetConstrainedProperty")
    def reset_constrained_property(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConstrainedProperty", []))

    @jsii.member(jsii_name="resetDecayRate")
    def reset_decay_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDecayRate", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetHostHeader")
    def reset_host_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostHeader", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLeaderString")
    def reset_leader_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLeaderString", []))

    @jsii.member(jsii_name="resetLeastSquaresDecay")
    def reset_least_squares_decay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLeastSquaresDecay", []))

    @jsii.member(jsii_name="resetLoadImbalancePercentage")
    def reset_load_imbalance_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadImbalancePercentage", []))

    @jsii.member(jsii_name="resetMaxUMultiplicativeIncrement")
    def reset_max_u_multiplicative_increment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxUMultiplicativeIncrement", []))

    @jsii.member(jsii_name="resetResourceInstance")
    def reset_resource_instance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceInstance", []))

    @jsii.member(jsii_name="resetUpperBound")
    def reset_upper_bound(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpperBound", []))

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
    @jsii.member(jsii_name="resourceInstance")
    def resource_instance(self) -> "GtmResourceResourceInstanceList":
        return typing.cast("GtmResourceResourceInstanceList", jsii.get(self, "resourceInstance"))

    @builtins.property
    @jsii.member(jsii_name="aggregationTypeInput")
    def aggregation_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aggregationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="constrainedPropertyInput")
    def constrained_property_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "constrainedPropertyInput"))

    @builtins.property
    @jsii.member(jsii_name="decayRateInput")
    def decay_rate_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "decayRateInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="domainInput")
    def domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainInput"))

    @builtins.property
    @jsii.member(jsii_name="hostHeaderInput")
    def host_header_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="leaderStringInput")
    def leader_string_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "leaderStringInput"))

    @builtins.property
    @jsii.member(jsii_name="leastSquaresDecayInput")
    def least_squares_decay_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "leastSquaresDecayInput"))

    @builtins.property
    @jsii.member(jsii_name="loadImbalancePercentageInput")
    def load_imbalance_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "loadImbalancePercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="maxUMultiplicativeIncrementInput")
    def max_u_multiplicative_increment_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxUMultiplicativeIncrementInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceInstanceInput")
    def resource_instance_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GtmResourceResourceInstance"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GtmResourceResourceInstance"]]], jsii.get(self, "resourceInstanceInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="upperBoundInput")
    def upper_bound_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "upperBoundInput"))

    @builtins.property
    @jsii.member(jsii_name="waitOnCompleteInput")
    def wait_on_complete_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "waitOnCompleteInput"))

    @builtins.property
    @jsii.member(jsii_name="aggregationType")
    def aggregation_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aggregationType"))

    @aggregation_type.setter
    def aggregation_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc95fd52068ec7dd4b1a42cd70eb485eab760c4076be3114871c802b1ac7118a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aggregationType", value)

    @builtins.property
    @jsii.member(jsii_name="constrainedProperty")
    def constrained_property(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "constrainedProperty"))

    @constrained_property.setter
    def constrained_property(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8db16e428063b8df6d056916bd118d21ff25ef6ddb2b518c91df55f576b51eee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "constrainedProperty", value)

    @builtins.property
    @jsii.member(jsii_name="decayRate")
    def decay_rate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "decayRate"))

    @decay_rate.setter
    def decay_rate(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f58dc6701bc155c626176bf5febb8fdcec4320a15bd2059ce225653d5a26d121)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "decayRate", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c421735e731f7b01afc8a955b78c1d32f93dca354e24f4eab212c9310bfeb0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff01c9acc8d4ed98081ed6556d71168918e25fb95e06e40ebe7face3bb5e72c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)

    @builtins.property
    @jsii.member(jsii_name="hostHeader")
    def host_header(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostHeader"))

    @host_header.setter
    def host_header(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7236b6ec88fe5b92959d7922baee45eb10397d2701b1d8ea392f69fd05e3582c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostHeader", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6edc37c6eb3588f13002be4706cc1448c49f3be4f686270075ff965c80f42da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="leaderString")
    def leader_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "leaderString"))

    @leader_string.setter
    def leader_string(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9ea555255e5c6d58cc4b2ce38cc0c254bf8c2b0fe1122c93e78c14b39244463)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "leaderString", value)

    @builtins.property
    @jsii.member(jsii_name="leastSquaresDecay")
    def least_squares_decay(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "leastSquaresDecay"))

    @least_squares_decay.setter
    def least_squares_decay(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b3761601cbe4cf28cb2c637300d4544b9289ef49722a0c214498c3a2e334838)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "leastSquaresDecay", value)

    @builtins.property
    @jsii.member(jsii_name="loadImbalancePercentage")
    def load_imbalance_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "loadImbalancePercentage"))

    @load_imbalance_percentage.setter
    def load_imbalance_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ddd6e24fea928606ec410b7f026641045d10785208222412a06ac525466a165)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadImbalancePercentage", value)

    @builtins.property
    @jsii.member(jsii_name="maxUMultiplicativeIncrement")
    def max_u_multiplicative_increment(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxUMultiplicativeIncrement"))

    @max_u_multiplicative_increment.setter
    def max_u_multiplicative_increment(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40961aa4ef2b35893e030f26543727f9b63ff6b6fc62efd2a4b38048aaab03a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxUMultiplicativeIncrement", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c330eeedf409e2f3b1594ae4e719b1811591910d1bb3a04e08d1cecbc7d7d8f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11f8f032e22b42ec0765f7a4f81078c80c985ef56a9124056b37e5839af12c13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="upperBound")
    def upper_bound(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "upperBound"))

    @upper_bound.setter
    def upper_bound(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25dda4c90235ff530eeb865b295fa01bb9ea5143a1c90e0b234e20d49f0c2f0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "upperBound", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__cea5d8042cd1fc46f3e00aaece7d39cb2b819a9a479c084e75ff805d509a062f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitOnComplete", value)


@jsii.data_type(
    jsii_type="akamai.gtmResource.GtmResourceConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "aggregation_type": "aggregationType",
        "domain": "domain",
        "name": "name",
        "type": "type",
        "constrained_property": "constrainedProperty",
        "decay_rate": "decayRate",
        "description": "description",
        "host_header": "hostHeader",
        "id": "id",
        "leader_string": "leaderString",
        "least_squares_decay": "leastSquaresDecay",
        "load_imbalance_percentage": "loadImbalancePercentage",
        "max_u_multiplicative_increment": "maxUMultiplicativeIncrement",
        "resource_instance": "resourceInstance",
        "upper_bound": "upperBound",
        "wait_on_complete": "waitOnComplete",
    },
)
class GtmResourceConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        aggregation_type: builtins.str,
        domain: builtins.str,
        name: builtins.str,
        type: builtins.str,
        constrained_property: typing.Optional[builtins.str] = None,
        decay_rate: typing.Optional[jsii.Number] = None,
        description: typing.Optional[builtins.str] = None,
        host_header: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        leader_string: typing.Optional[builtins.str] = None,
        least_squares_decay: typing.Optional[jsii.Number] = None,
        load_imbalance_percentage: typing.Optional[jsii.Number] = None,
        max_u_multiplicative_increment: typing.Optional[jsii.Number] = None,
        resource_instance: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GtmResourceResourceInstance", typing.Dict[builtins.str, typing.Any]]]]] = None,
        upper_bound: typing.Optional[jsii.Number] = None,
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
        :param aggregation_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#aggregation_type GtmResource#aggregation_type}.
        :param domain: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#domain GtmResource#domain}.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#name GtmResource#name}.
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#type GtmResource#type}.
        :param constrained_property: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#constrained_property GtmResource#constrained_property}.
        :param decay_rate: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#decay_rate GtmResource#decay_rate}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#description GtmResource#description}.
        :param host_header: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#host_header GtmResource#host_header}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#id GtmResource#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param leader_string: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#leader_string GtmResource#leader_string}.
        :param least_squares_decay: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#least_squares_decay GtmResource#least_squares_decay}.
        :param load_imbalance_percentage: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#load_imbalance_percentage GtmResource#load_imbalance_percentage}.
        :param max_u_multiplicative_increment: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#max_u_multiplicative_increment GtmResource#max_u_multiplicative_increment}.
        :param resource_instance: resource_instance block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#resource_instance GtmResource#resource_instance}
        :param upper_bound: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#upper_bound GtmResource#upper_bound}.
        :param wait_on_complete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#wait_on_complete GtmResource#wait_on_complete}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96e644bdc04abc97cb8a60e745d8d8efcb623508e9cd3f97abf372920362e72f)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument aggregation_type", value=aggregation_type, expected_type=type_hints["aggregation_type"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument constrained_property", value=constrained_property, expected_type=type_hints["constrained_property"])
            check_type(argname="argument decay_rate", value=decay_rate, expected_type=type_hints["decay_rate"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument host_header", value=host_header, expected_type=type_hints["host_header"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument leader_string", value=leader_string, expected_type=type_hints["leader_string"])
            check_type(argname="argument least_squares_decay", value=least_squares_decay, expected_type=type_hints["least_squares_decay"])
            check_type(argname="argument load_imbalance_percentage", value=load_imbalance_percentage, expected_type=type_hints["load_imbalance_percentage"])
            check_type(argname="argument max_u_multiplicative_increment", value=max_u_multiplicative_increment, expected_type=type_hints["max_u_multiplicative_increment"])
            check_type(argname="argument resource_instance", value=resource_instance, expected_type=type_hints["resource_instance"])
            check_type(argname="argument upper_bound", value=upper_bound, expected_type=type_hints["upper_bound"])
            check_type(argname="argument wait_on_complete", value=wait_on_complete, expected_type=type_hints["wait_on_complete"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aggregation_type": aggregation_type,
            "domain": domain,
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
        if constrained_property is not None:
            self._values["constrained_property"] = constrained_property
        if decay_rate is not None:
            self._values["decay_rate"] = decay_rate
        if description is not None:
            self._values["description"] = description
        if host_header is not None:
            self._values["host_header"] = host_header
        if id is not None:
            self._values["id"] = id
        if leader_string is not None:
            self._values["leader_string"] = leader_string
        if least_squares_decay is not None:
            self._values["least_squares_decay"] = least_squares_decay
        if load_imbalance_percentage is not None:
            self._values["load_imbalance_percentage"] = load_imbalance_percentage
        if max_u_multiplicative_increment is not None:
            self._values["max_u_multiplicative_increment"] = max_u_multiplicative_increment
        if resource_instance is not None:
            self._values["resource_instance"] = resource_instance
        if upper_bound is not None:
            self._values["upper_bound"] = upper_bound
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
    def aggregation_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#aggregation_type GtmResource#aggregation_type}.'''
        result = self._values.get("aggregation_type")
        assert result is not None, "Required property 'aggregation_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#domain GtmResource#domain}.'''
        result = self._values.get("domain")
        assert result is not None, "Required property 'domain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#name GtmResource#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#type GtmResource#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def constrained_property(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#constrained_property GtmResource#constrained_property}.'''
        result = self._values.get("constrained_property")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def decay_rate(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#decay_rate GtmResource#decay_rate}.'''
        result = self._values.get("decay_rate")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#description GtmResource#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def host_header(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#host_header GtmResource#host_header}.'''
        result = self._values.get("host_header")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#id GtmResource#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def leader_string(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#leader_string GtmResource#leader_string}.'''
        result = self._values.get("leader_string")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def least_squares_decay(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#least_squares_decay GtmResource#least_squares_decay}.'''
        result = self._values.get("least_squares_decay")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def load_imbalance_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#load_imbalance_percentage GtmResource#load_imbalance_percentage}.'''
        result = self._values.get("load_imbalance_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_u_multiplicative_increment(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#max_u_multiplicative_increment GtmResource#max_u_multiplicative_increment}.'''
        result = self._values.get("max_u_multiplicative_increment")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_instance(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GtmResourceResourceInstance"]]]:
        '''resource_instance block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#resource_instance GtmResource#resource_instance}
        '''
        result = self._values.get("resource_instance")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GtmResourceResourceInstance"]]], result)

    @builtins.property
    def upper_bound(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#upper_bound GtmResource#upper_bound}.'''
        result = self._values.get("upper_bound")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def wait_on_complete(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#wait_on_complete GtmResource#wait_on_complete}.'''
        result = self._values.get("wait_on_complete")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GtmResourceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.gtmResource.GtmResourceResourceInstance",
    jsii_struct_bases=[],
    name_mapping={
        "datacenter_id": "datacenterId",
        "load_object": "loadObject",
        "load_object_port": "loadObjectPort",
        "load_servers": "loadServers",
        "use_default_load_object": "useDefaultLoadObject",
    },
)
class GtmResourceResourceInstance:
    def __init__(
        self,
        *,
        datacenter_id: jsii.Number,
        load_object: typing.Optional[builtins.str] = None,
        load_object_port: typing.Optional[jsii.Number] = None,
        load_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
        use_default_load_object: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param datacenter_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#datacenter_id GtmResource#datacenter_id}.
        :param load_object: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#load_object GtmResource#load_object}.
        :param load_object_port: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#load_object_port GtmResource#load_object_port}.
        :param load_servers: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#load_servers GtmResource#load_servers}.
        :param use_default_load_object: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#use_default_load_object GtmResource#use_default_load_object}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59c937aecaf6d7268e4441195e64c20295d9df6e99fccaafe9bb65be4a12f4f5)
            check_type(argname="argument datacenter_id", value=datacenter_id, expected_type=type_hints["datacenter_id"])
            check_type(argname="argument load_object", value=load_object, expected_type=type_hints["load_object"])
            check_type(argname="argument load_object_port", value=load_object_port, expected_type=type_hints["load_object_port"])
            check_type(argname="argument load_servers", value=load_servers, expected_type=type_hints["load_servers"])
            check_type(argname="argument use_default_load_object", value=use_default_load_object, expected_type=type_hints["use_default_load_object"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "datacenter_id": datacenter_id,
        }
        if load_object is not None:
            self._values["load_object"] = load_object
        if load_object_port is not None:
            self._values["load_object_port"] = load_object_port
        if load_servers is not None:
            self._values["load_servers"] = load_servers
        if use_default_load_object is not None:
            self._values["use_default_load_object"] = use_default_load_object

    @builtins.property
    def datacenter_id(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#datacenter_id GtmResource#datacenter_id}.'''
        result = self._values.get("datacenter_id")
        assert result is not None, "Required property 'datacenter_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def load_object(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#load_object GtmResource#load_object}.'''
        result = self._values.get("load_object")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def load_object_port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#load_object_port GtmResource#load_object_port}.'''
        result = self._values.get("load_object_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def load_servers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#load_servers GtmResource#load_servers}.'''
        result = self._values.get("load_servers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def use_default_load_object(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/gtm_resource#use_default_load_object GtmResource#use_default_load_object}.'''
        result = self._values.get("use_default_load_object")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GtmResourceResourceInstance(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GtmResourceResourceInstanceList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.gtmResource.GtmResourceResourceInstanceList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__576e2ac222d921b43855a1b9365d0d53b382935b1c26ed33e38091009833c69e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GtmResourceResourceInstanceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cbf409905ebb4ec769d90fc890bebd3c8b078aa4546dbd38baa1fabc1289527)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GtmResourceResourceInstanceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db3206483ac7d9c9b79e1f823230e13fbdec3923adc875e8d65546aab7904ab3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5e039dda19d44e45998b1092f21dd4bddd7d7344255de6bcb50d741611667686)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cfcb45d4d3704476307c361b6bb1081cb2885c722a4ca9ae8c2aaf6ff918ca4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmResourceResourceInstance]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmResourceResourceInstance]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmResourceResourceInstance]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37680ba5e5665f487fd8ca69d77b5c91e4d22444d5acd0987127e3b4d8ea80f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GtmResourceResourceInstanceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.gtmResource.GtmResourceResourceInstanceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2ab428b588d8a6908aa93829a760e7e9d5260a25d1af760ce9bebed04960ddad)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetLoadObject")
    def reset_load_object(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadObject", []))

    @jsii.member(jsii_name="resetLoadObjectPort")
    def reset_load_object_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadObjectPort", []))

    @jsii.member(jsii_name="resetLoadServers")
    def reset_load_servers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadServers", []))

    @jsii.member(jsii_name="resetUseDefaultLoadObject")
    def reset_use_default_load_object(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseDefaultLoadObject", []))

    @builtins.property
    @jsii.member(jsii_name="datacenterIdInput")
    def datacenter_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "datacenterIdInput"))

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
    @jsii.member(jsii_name="useDefaultLoadObjectInput")
    def use_default_load_object_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "useDefaultLoadObjectInput"))

    @builtins.property
    @jsii.member(jsii_name="datacenterId")
    def datacenter_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "datacenterId"))

    @datacenter_id.setter
    def datacenter_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a80620d6ea52158fc8fa04420a222655db659d497c1e4c5f28dd9296ab262575)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datacenterId", value)

    @builtins.property
    @jsii.member(jsii_name="loadObject")
    def load_object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loadObject"))

    @load_object.setter
    def load_object(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__635755a31b7293018c8380ec0606fe0fd7f4b563b85a211a1479d4bf87f6d329)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadObject", value)

    @builtins.property
    @jsii.member(jsii_name="loadObjectPort")
    def load_object_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "loadObjectPort"))

    @load_object_port.setter
    def load_object_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aed7ccfe6c558fde27d90cada3e77674028d35b3142b82a838767a75446b2ffd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadObjectPort", value)

    @builtins.property
    @jsii.member(jsii_name="loadServers")
    def load_servers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "loadServers"))

    @load_servers.setter
    def load_servers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ce7790a6723d835448410a3e0ed298744afce80e3616fed203d61f6c68627fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadServers", value)

    @builtins.property
    @jsii.member(jsii_name="useDefaultLoadObject")
    def use_default_load_object(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "useDefaultLoadObject"))

    @use_default_load_object.setter
    def use_default_load_object(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d03d6349dd74740745a942070652efb7223721b396aaf510c9419c8a818a84c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useDefaultLoadObject", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GtmResourceResourceInstance]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GtmResourceResourceInstance]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GtmResourceResourceInstance]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0621f700fe9f79c2c4e8155e3236336c3aa7d7f1a61f2e75f5014966ad725045)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GtmResource",
    "GtmResourceConfig",
    "GtmResourceResourceInstance",
    "GtmResourceResourceInstanceList",
    "GtmResourceResourceInstanceOutputReference",
]

publication.publish()

def _typecheckingstub__01f4edabcceb50dfcfcfa1c5e9f3e2a8cdc0f7678152ce5ac4d45b5c7204af84(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    aggregation_type: builtins.str,
    domain: builtins.str,
    name: builtins.str,
    type: builtins.str,
    constrained_property: typing.Optional[builtins.str] = None,
    decay_rate: typing.Optional[jsii.Number] = None,
    description: typing.Optional[builtins.str] = None,
    host_header: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    leader_string: typing.Optional[builtins.str] = None,
    least_squares_decay: typing.Optional[jsii.Number] = None,
    load_imbalance_percentage: typing.Optional[jsii.Number] = None,
    max_u_multiplicative_increment: typing.Optional[jsii.Number] = None,
    resource_instance: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GtmResourceResourceInstance, typing.Dict[builtins.str, typing.Any]]]]] = None,
    upper_bound: typing.Optional[jsii.Number] = None,
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

def _typecheckingstub__594221324a358e6e38e777b551c4abe248c83b4cab88412317e9c136f9dc2e1f(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9c2a20ee1b51b2f6c8f021880717f3dacaf43a4bacb56f85224cc38b5238908(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GtmResourceResourceInstance, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc95fd52068ec7dd4b1a42cd70eb485eab760c4076be3114871c802b1ac7118a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8db16e428063b8df6d056916bd118d21ff25ef6ddb2b518c91df55f576b51eee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f58dc6701bc155c626176bf5febb8fdcec4320a15bd2059ce225653d5a26d121(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c421735e731f7b01afc8a955b78c1d32f93dca354e24f4eab212c9310bfeb0d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff01c9acc8d4ed98081ed6556d71168918e25fb95e06e40ebe7face3bb5e72c7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7236b6ec88fe5b92959d7922baee45eb10397d2701b1d8ea392f69fd05e3582c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6edc37c6eb3588f13002be4706cc1448c49f3be4f686270075ff965c80f42da(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9ea555255e5c6d58cc4b2ce38cc0c254bf8c2b0fe1122c93e78c14b39244463(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b3761601cbe4cf28cb2c637300d4544b9289ef49722a0c214498c3a2e334838(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ddd6e24fea928606ec410b7f026641045d10785208222412a06ac525466a165(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40961aa4ef2b35893e030f26543727f9b63ff6b6fc62efd2a4b38048aaab03a8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c330eeedf409e2f3b1594ae4e719b1811591910d1bb3a04e08d1cecbc7d7d8f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11f8f032e22b42ec0765f7a4f81078c80c985ef56a9124056b37e5839af12c13(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25dda4c90235ff530eeb865b295fa01bb9ea5143a1c90e0b234e20d49f0c2f0b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cea5d8042cd1fc46f3e00aaece7d39cb2b819a9a479c084e75ff805d509a062f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96e644bdc04abc97cb8a60e745d8d8efcb623508e9cd3f97abf372920362e72f(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    aggregation_type: builtins.str,
    domain: builtins.str,
    name: builtins.str,
    type: builtins.str,
    constrained_property: typing.Optional[builtins.str] = None,
    decay_rate: typing.Optional[jsii.Number] = None,
    description: typing.Optional[builtins.str] = None,
    host_header: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    leader_string: typing.Optional[builtins.str] = None,
    least_squares_decay: typing.Optional[jsii.Number] = None,
    load_imbalance_percentage: typing.Optional[jsii.Number] = None,
    max_u_multiplicative_increment: typing.Optional[jsii.Number] = None,
    resource_instance: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GtmResourceResourceInstance, typing.Dict[builtins.str, typing.Any]]]]] = None,
    upper_bound: typing.Optional[jsii.Number] = None,
    wait_on_complete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59c937aecaf6d7268e4441195e64c20295d9df6e99fccaafe9bb65be4a12f4f5(
    *,
    datacenter_id: jsii.Number,
    load_object: typing.Optional[builtins.str] = None,
    load_object_port: typing.Optional[jsii.Number] = None,
    load_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
    use_default_load_object: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__576e2ac222d921b43855a1b9365d0d53b382935b1c26ed33e38091009833c69e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cbf409905ebb4ec769d90fc890bebd3c8b078aa4546dbd38baa1fabc1289527(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db3206483ac7d9c9b79e1f823230e13fbdec3923adc875e8d65546aab7904ab3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e039dda19d44e45998b1092f21dd4bddd7d7344255de6bcb50d741611667686(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfcb45d4d3704476307c361b6bb1081cb2885c722a4ca9ae8c2aaf6ff918ca4d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37680ba5e5665f487fd8ca69d77b5c91e4d22444d5acd0987127e3b4d8ea80f8(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GtmResourceResourceInstance]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ab428b588d8a6908aa93829a760e7e9d5260a25d1af760ce9bebed04960ddad(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a80620d6ea52158fc8fa04420a222655db659d497c1e4c5f28dd9296ab262575(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__635755a31b7293018c8380ec0606fe0fd7f4b563b85a211a1479d4bf87f6d329(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aed7ccfe6c558fde27d90cada3e77674028d35b3142b82a838767a75446b2ffd(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ce7790a6723d835448410a3e0ed298744afce80e3616fed203d61f6c68627fe(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d03d6349dd74740745a942070652efb7223721b396aaf510c9419c8a818a84c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0621f700fe9f79c2c4e8155e3236336c3aa7d7f1a61f2e75f5014966ad725045(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, GtmResourceResourceInstance]],
) -> None:
    """Type checking stubs"""
    pass
