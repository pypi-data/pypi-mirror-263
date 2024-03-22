'''
# `data_akamai_cloudlets_shared_policy`

Refer to the Terraform Registry for docs: [`data_akamai_cloudlets_shared_policy`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_shared_policy).
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


class DataAkamaiCloudletsSharedPolicy(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsSharedPolicy.DataAkamaiCloudletsSharedPolicy",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_shared_policy akamai_cloudlets_shared_policy}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        policy_id: jsii.Number,
        version: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_shared_policy akamai_cloudlets_shared_policy} Data Source.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param policy_id: An integer ID that is associated with a policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_shared_policy#policy_id DataAkamaiCloudletsSharedPolicy#policy_id}
        :param version: The number of the policy version. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_shared_policy#version DataAkamaiCloudletsSharedPolicy#version}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b79cd73be3e14419303d8464b32ec7515165dd03018e060517f560e3e0d6058d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = DataAkamaiCloudletsSharedPolicyConfig(
            policy_id=policy_id,
            version=version,
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
        '''Generates CDKTF code for importing a DataAkamaiCloudletsSharedPolicy resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the DataAkamaiCloudletsSharedPolicy to import.
        :param import_from_id: The id of the existing DataAkamaiCloudletsSharedPolicy that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_shared_policy#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the DataAkamaiCloudletsSharedPolicy to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59f4aa1902ebfba0060be6f291ba02fdf86c6f89cd95cdd5172e6cb2ca8617bd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

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
    @jsii.member(jsii_name="activations")
    def activations(
        self,
    ) -> "DataAkamaiCloudletsSharedPolicyActivationsOutputReference":
        return typing.cast("DataAkamaiCloudletsSharedPolicyActivationsOutputReference", jsii.get(self, "activations"))

    @builtins.property
    @jsii.member(jsii_name="cloudletType")
    def cloudlet_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudletType"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="groupId")
    def group_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "groupId"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="matchRules")
    def match_rules(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchRules"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="versionDescription")
    def version_description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "versionDescription"))

    @builtins.property
    @jsii.member(jsii_name="warnings")
    def warnings(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "warnings"))

    @builtins.property
    @jsii.member(jsii_name="policyIdInput")
    def policy_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "policyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="policyId")
    def policy_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "policyId"))

    @policy_id.setter
    def policy_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__432cd4d33253c286abb3eea2b5a555dffd98e4db54a530b80fa16ebd30a06fce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyId", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "version"))

    @version.setter
    def version(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aaf2167cc6bd8845f488a8d734e140dcb4a6e005bccc5495336df287d213f574)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsSharedPolicy.DataAkamaiCloudletsSharedPolicyActivations",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiCloudletsSharedPolicyActivations:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsSharedPolicyActivations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudletsSharedPolicyActivationsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsSharedPolicy.DataAkamaiCloudletsSharedPolicyActivationsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fa35b631405d92ee53d89e71ca6c1a128f022ef243029095d3b778938837c108)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="production")
    def production(
        self,
    ) -> "DataAkamaiCloudletsSharedPolicyActivationsProductionOutputReference":
        return typing.cast("DataAkamaiCloudletsSharedPolicyActivationsProductionOutputReference", jsii.get(self, "production"))

    @builtins.property
    @jsii.member(jsii_name="staging")
    def staging(
        self,
    ) -> "DataAkamaiCloudletsSharedPolicyActivationsStagingOutputReference":
        return typing.cast("DataAkamaiCloudletsSharedPolicyActivationsStagingOutputReference", jsii.get(self, "staging"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsSharedPolicyActivations]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsSharedPolicyActivations]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsSharedPolicyActivations]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53545aa225281443a223c4e526675ce8f50b39e383e3251937b09bfdf9e0b32c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsSharedPolicy.DataAkamaiCloudletsSharedPolicyActivationsProduction",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiCloudletsSharedPolicyActivationsProduction:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsSharedPolicyActivationsProduction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsSharedPolicy.DataAkamaiCloudletsSharedPolicyActivationsProductionEffective",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiCloudletsSharedPolicyActivationsProductionEffective:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsSharedPolicyActivationsProductionEffective(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudletsSharedPolicyActivationsProductionEffectiveOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsSharedPolicy.DataAkamaiCloudletsSharedPolicyActivationsProductionEffectiveOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__756caaccc20a487b85e2ece7ca8750f73d27008253666b16d1122b0be2af1789)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="activationId")
    def activation_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "activationId"))

    @builtins.property
    @jsii.member(jsii_name="createdBy")
    def created_by(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdBy"))

    @builtins.property
    @jsii.member(jsii_name="createdDate")
    def created_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdDate"))

    @builtins.property
    @jsii.member(jsii_name="finishDate")
    def finish_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "finishDate"))

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "network"))

    @builtins.property
    @jsii.member(jsii_name="operation")
    def operation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operation"))

    @builtins.property
    @jsii.member(jsii_name="policyId")
    def policy_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "policyId"))

    @builtins.property
    @jsii.member(jsii_name="policyVersion")
    def policy_version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "policyVersion"))

    @builtins.property
    @jsii.member(jsii_name="policyVersionDeleted")
    def policy_version_deleted(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "policyVersionDeleted"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsSharedPolicyActivationsProductionEffective]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsSharedPolicyActivationsProductionEffective]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsSharedPolicyActivationsProductionEffective]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57beae3188b152ec021e168db9ccbadbeb80e6127490ef3f1ceaa3f04a5989cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsSharedPolicy.DataAkamaiCloudletsSharedPolicyActivationsProductionLatest",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiCloudletsSharedPolicyActivationsProductionLatest:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsSharedPolicyActivationsProductionLatest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudletsSharedPolicyActivationsProductionLatestOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsSharedPolicy.DataAkamaiCloudletsSharedPolicyActivationsProductionLatestOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__57408fc8f40b94cae34f12bdb594d07810ed0b3e8880afe13f3e745866f0a3ad)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="activationId")
    def activation_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "activationId"))

    @builtins.property
    @jsii.member(jsii_name="createdBy")
    def created_by(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdBy"))

    @builtins.property
    @jsii.member(jsii_name="createdDate")
    def created_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdDate"))

    @builtins.property
    @jsii.member(jsii_name="finishDate")
    def finish_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "finishDate"))

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "network"))

    @builtins.property
    @jsii.member(jsii_name="operation")
    def operation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operation"))

    @builtins.property
    @jsii.member(jsii_name="policyId")
    def policy_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "policyId"))

    @builtins.property
    @jsii.member(jsii_name="policyVersion")
    def policy_version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "policyVersion"))

    @builtins.property
    @jsii.member(jsii_name="policyVersionDeleted")
    def policy_version_deleted(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "policyVersionDeleted"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsSharedPolicyActivationsProductionLatest]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsSharedPolicyActivationsProductionLatest]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsSharedPolicyActivationsProductionLatest]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c48b3061254e00e5b06798bdb538c27faee1644647bf16241c052767e148df7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudletsSharedPolicyActivationsProductionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsSharedPolicy.DataAkamaiCloudletsSharedPolicyActivationsProductionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5bddd2d958c513f6a2bd42ff6b2e2781afae0b82f2b85a7b07d5d8bd51604d3c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="effective")
    def effective(
        self,
    ) -> DataAkamaiCloudletsSharedPolicyActivationsProductionEffectiveOutputReference:
        return typing.cast(DataAkamaiCloudletsSharedPolicyActivationsProductionEffectiveOutputReference, jsii.get(self, "effective"))

    @builtins.property
    @jsii.member(jsii_name="latest")
    def latest(
        self,
    ) -> DataAkamaiCloudletsSharedPolicyActivationsProductionLatestOutputReference:
        return typing.cast(DataAkamaiCloudletsSharedPolicyActivationsProductionLatestOutputReference, jsii.get(self, "latest"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsSharedPolicyActivationsProduction]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsSharedPolicyActivationsProduction]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsSharedPolicyActivationsProduction]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7cfffc5fd0cd58f27ec15de645b853bc3b0597724df30b92afa9d3e03bf5d266)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsSharedPolicy.DataAkamaiCloudletsSharedPolicyActivationsStaging",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiCloudletsSharedPolicyActivationsStaging:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsSharedPolicyActivationsStaging(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsSharedPolicy.DataAkamaiCloudletsSharedPolicyActivationsStagingEffective",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiCloudletsSharedPolicyActivationsStagingEffective:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsSharedPolicyActivationsStagingEffective(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudletsSharedPolicyActivationsStagingEffectiveOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsSharedPolicy.DataAkamaiCloudletsSharedPolicyActivationsStagingEffectiveOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__746dc71a77a4c4c405677f343c3f35306568b09ca375b45addff4c2d4dc4e686)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="activationId")
    def activation_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "activationId"))

    @builtins.property
    @jsii.member(jsii_name="createdBy")
    def created_by(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdBy"))

    @builtins.property
    @jsii.member(jsii_name="createdDate")
    def created_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdDate"))

    @builtins.property
    @jsii.member(jsii_name="finishDate")
    def finish_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "finishDate"))

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "network"))

    @builtins.property
    @jsii.member(jsii_name="operation")
    def operation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operation"))

    @builtins.property
    @jsii.member(jsii_name="policyId")
    def policy_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "policyId"))

    @builtins.property
    @jsii.member(jsii_name="policyVersion")
    def policy_version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "policyVersion"))

    @builtins.property
    @jsii.member(jsii_name="policyVersionDeleted")
    def policy_version_deleted(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "policyVersionDeleted"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsSharedPolicyActivationsStagingEffective]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsSharedPolicyActivationsStagingEffective]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsSharedPolicyActivationsStagingEffective]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05167fff9e8817feb6c9f2f5b945df2407943818b63127b38d0bda2eb8403c72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsSharedPolicy.DataAkamaiCloudletsSharedPolicyActivationsStagingLatest",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiCloudletsSharedPolicyActivationsStagingLatest:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsSharedPolicyActivationsStagingLatest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudletsSharedPolicyActivationsStagingLatestOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsSharedPolicy.DataAkamaiCloudletsSharedPolicyActivationsStagingLatestOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fbf018ccdd48f5baa2a74c82e512c16827c5dd2372eaf6fd1c78ae9aa4bd4eae)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="activationId")
    def activation_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "activationId"))

    @builtins.property
    @jsii.member(jsii_name="createdBy")
    def created_by(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdBy"))

    @builtins.property
    @jsii.member(jsii_name="createdDate")
    def created_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdDate"))

    @builtins.property
    @jsii.member(jsii_name="finishDate")
    def finish_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "finishDate"))

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "network"))

    @builtins.property
    @jsii.member(jsii_name="operation")
    def operation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operation"))

    @builtins.property
    @jsii.member(jsii_name="policyId")
    def policy_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "policyId"))

    @builtins.property
    @jsii.member(jsii_name="policyVersion")
    def policy_version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "policyVersion"))

    @builtins.property
    @jsii.member(jsii_name="policyVersionDeleted")
    def policy_version_deleted(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "policyVersionDeleted"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsSharedPolicyActivationsStagingLatest]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsSharedPolicyActivationsStagingLatest]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsSharedPolicyActivationsStagingLatest]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5eda29a307c86daf613640e3cff1c9f0cf6a2155d082b85fef4aa68c6a456797)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCloudletsSharedPolicyActivationsStagingOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsSharedPolicy.DataAkamaiCloudletsSharedPolicyActivationsStagingOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f1a6dda500eeabba17f965688059e280ce4a74cd868190632d6f832b0e110d47)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="effective")
    def effective(
        self,
    ) -> DataAkamaiCloudletsSharedPolicyActivationsStagingEffectiveOutputReference:
        return typing.cast(DataAkamaiCloudletsSharedPolicyActivationsStagingEffectiveOutputReference, jsii.get(self, "effective"))

    @builtins.property
    @jsii.member(jsii_name="latest")
    def latest(
        self,
    ) -> DataAkamaiCloudletsSharedPolicyActivationsStagingLatestOutputReference:
        return typing.cast(DataAkamaiCloudletsSharedPolicyActivationsStagingLatestOutputReference, jsii.get(self, "latest"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsSharedPolicyActivationsStaging]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsSharedPolicyActivationsStaging]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsSharedPolicyActivationsStaging]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__549f222949f60df0d48b51a60fbc9be3c7623e70967c5915d05cba617d2399a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsSharedPolicy.DataAkamaiCloudletsSharedPolicyConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "policy_id": "policyId",
        "version": "version",
    },
)
class DataAkamaiCloudletsSharedPolicyConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        policy_id: jsii.Number,
        version: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param policy_id: An integer ID that is associated with a policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_shared_policy#policy_id DataAkamaiCloudletsSharedPolicy#policy_id}
        :param version: The number of the policy version. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_shared_policy#version DataAkamaiCloudletsSharedPolicy#version}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50346ceeb761045b116c48b3bbc9a44a63eb733025b686516e4dc3aeeecbd28f)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument policy_id", value=policy_id, expected_type=type_hints["policy_id"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_id": policy_id,
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
        if version is not None:
            self._values["version"] = version

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
    def policy_id(self) -> jsii.Number:
        '''An integer ID that is associated with a policy.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_shared_policy#policy_id DataAkamaiCloudletsSharedPolicy#policy_id}
        '''
        result = self._values.get("policy_id")
        assert result is not None, "Required property 'policy_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def version(self) -> typing.Optional[jsii.Number]:
        '''The number of the policy version.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_shared_policy#version DataAkamaiCloudletsSharedPolicy#version}
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsSharedPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DataAkamaiCloudletsSharedPolicy",
    "DataAkamaiCloudletsSharedPolicyActivations",
    "DataAkamaiCloudletsSharedPolicyActivationsOutputReference",
    "DataAkamaiCloudletsSharedPolicyActivationsProduction",
    "DataAkamaiCloudletsSharedPolicyActivationsProductionEffective",
    "DataAkamaiCloudletsSharedPolicyActivationsProductionEffectiveOutputReference",
    "DataAkamaiCloudletsSharedPolicyActivationsProductionLatest",
    "DataAkamaiCloudletsSharedPolicyActivationsProductionLatestOutputReference",
    "DataAkamaiCloudletsSharedPolicyActivationsProductionOutputReference",
    "DataAkamaiCloudletsSharedPolicyActivationsStaging",
    "DataAkamaiCloudletsSharedPolicyActivationsStagingEffective",
    "DataAkamaiCloudletsSharedPolicyActivationsStagingEffectiveOutputReference",
    "DataAkamaiCloudletsSharedPolicyActivationsStagingLatest",
    "DataAkamaiCloudletsSharedPolicyActivationsStagingLatestOutputReference",
    "DataAkamaiCloudletsSharedPolicyActivationsStagingOutputReference",
    "DataAkamaiCloudletsSharedPolicyConfig",
]

publication.publish()

def _typecheckingstub__b79cd73be3e14419303d8464b32ec7515165dd03018e060517f560e3e0d6058d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    policy_id: jsii.Number,
    version: typing.Optional[jsii.Number] = None,
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

def _typecheckingstub__59f4aa1902ebfba0060be6f291ba02fdf86c6f89cd95cdd5172e6cb2ca8617bd(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__432cd4d33253c286abb3eea2b5a555dffd98e4db54a530b80fa16ebd30a06fce(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aaf2167cc6bd8845f488a8d734e140dcb4a6e005bccc5495336df287d213f574(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa35b631405d92ee53d89e71ca6c1a128f022ef243029095d3b778938837c108(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53545aa225281443a223c4e526675ce8f50b39e383e3251937b09bfdf9e0b32c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsSharedPolicyActivations]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__756caaccc20a487b85e2ece7ca8750f73d27008253666b16d1122b0be2af1789(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57beae3188b152ec021e168db9ccbadbeb80e6127490ef3f1ceaa3f04a5989cb(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsSharedPolicyActivationsProductionEffective]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57408fc8f40b94cae34f12bdb594d07810ed0b3e8880afe13f3e745866f0a3ad(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c48b3061254e00e5b06798bdb538c27faee1644647bf16241c052767e148df7(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsSharedPolicyActivationsProductionLatest]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bddd2d958c513f6a2bd42ff6b2e2781afae0b82f2b85a7b07d5d8bd51604d3c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cfffc5fd0cd58f27ec15de645b853bc3b0597724df30b92afa9d3e03bf5d266(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsSharedPolicyActivationsProduction]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__746dc71a77a4c4c405677f343c3f35306568b09ca375b45addff4c2d4dc4e686(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05167fff9e8817feb6c9f2f5b945df2407943818b63127b38d0bda2eb8403c72(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsSharedPolicyActivationsStagingEffective]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbf018ccdd48f5baa2a74c82e512c16827c5dd2372eaf6fd1c78ae9aa4bd4eae(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5eda29a307c86daf613640e3cff1c9f0cf6a2155d082b85fef4aa68c6a456797(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsSharedPolicyActivationsStagingLatest]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1a6dda500eeabba17f965688059e280ce4a74cd868190632d6f832b0e110d47(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__549f222949f60df0d48b51a60fbc9be3c7623e70967c5915d05cba617d2399a0(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiCloudletsSharedPolicyActivationsStaging]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50346ceeb761045b116c48b3bbc9a44a63eb733025b686516e4dc3aeeecbd28f(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    policy_id: jsii.Number,
    version: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass
