'''
# `data_akamai_cloudlets_policy`

Refer to the Terraform Registry for docs: [`data_akamai_cloudlets_policy`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_policy).
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


class DataAkamaiCloudletsPolicy(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsPolicy.DataAkamaiCloudletsPolicy",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_policy akamai_cloudlets_policy}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        policy_id: jsii.Number,
        id: typing.Optional[builtins.str] = None,
        version: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_policy akamai_cloudlets_policy} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param policy_id: An integer ID that is associated with a policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_policy#policy_id DataAkamaiCloudletsPolicy#policy_id}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_policy#id DataAkamaiCloudletsPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param version: The version number of the policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_policy#version DataAkamaiCloudletsPolicy#version}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87581871923df3b0ddb51f3454bb5d76e42dd4a728c9bc9b82037a4eb2d7ad8b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAkamaiCloudletsPolicyConfig(
            policy_id=policy_id,
            id=id,
            version=version,
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
        '''Generates CDKTF code for importing a DataAkamaiCloudletsPolicy resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the DataAkamaiCloudletsPolicy to import.
        :param import_from_id: The id of the existing DataAkamaiCloudletsPolicy that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_policy#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the DataAkamaiCloudletsPolicy to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23bce650235ba4f576f51735f20f89963d335d3c33e7593c46106de430018528)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    def activations(self) -> "DataAkamaiCloudletsPolicyActivationsList":
        return typing.cast("DataAkamaiCloudletsPolicyActivationsList", jsii.get(self, "activations"))

    @builtins.property
    @jsii.member(jsii_name="apiVersion")
    def api_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiVersion"))

    @builtins.property
    @jsii.member(jsii_name="cloudletCode")
    def cloudlet_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudletCode"))

    @builtins.property
    @jsii.member(jsii_name="cloudletId")
    def cloudlet_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cloudletId"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="groupId")
    def group_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "groupId"))

    @builtins.property
    @jsii.member(jsii_name="matchRuleFormat")
    def match_rule_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchRuleFormat"))

    @builtins.property
    @jsii.member(jsii_name="matchRules")
    def match_rules(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchRules"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="revisionId")
    def revision_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "revisionId"))

    @builtins.property
    @jsii.member(jsii_name="rulesLocked")
    def rules_locked(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "rulesLocked"))

    @builtins.property
    @jsii.member(jsii_name="versionDescription")
    def version_description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "versionDescription"))

    @builtins.property
    @jsii.member(jsii_name="warnings")
    def warnings(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "warnings"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="policyIdInput")
    def policy_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "policyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29d02a17258ab38adcb01073588a089fe8e7d61185304526662eda6fa972f739)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="policyId")
    def policy_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "policyId"))

    @policy_id.setter
    def policy_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30f646f53bb477c0bdcfab1dac7c2467e331a1d5dcec464742a7c5679d6dd8c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyId", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "version"))

    @version.setter
    def version(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de2999ca9754bcd472f1c8a0560da74531fd2d82518eb1c92c93be91dc6f4317)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsPolicy.DataAkamaiCloudletsPolicyActivations",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiCloudletsPolicyActivations:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsPolicyActivations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudletsPolicyActivationsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsPolicy.DataAkamaiCloudletsPolicyActivationsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b77d00b0c1081bc11dc10f0b5580ac536d6e087441265d97911f90824338d33d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiCloudletsPolicyActivationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab635b3dcfee464e5f6883c9d463598d0fa28cb0fa71c302cddd0b79a3912343)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiCloudletsPolicyActivationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d568df36a5355eb412d01319997d9b0ee68649b7575042e83d40ccc771464798)
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
            type_hints = typing.get_type_hints(_typecheckingstub__35547daa505945c6ca59aa2c334ad852e0769e3f9a68549f9024f916e450698a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a6478273e8afa758505746ab54a361894a45e6c15325c2dfe0b67a7ab8091819)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataAkamaiCloudletsPolicyActivationsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsPolicy.DataAkamaiCloudletsPolicyActivationsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fb1ca8ac586bd2adf81335cad0b3580c978535f7f0b2b5727d9234c04748debe)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="apiVersion")
    def api_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiVersion"))

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "network"))

    @builtins.property
    @jsii.member(jsii_name="policyInfo")
    def policy_info(self) -> "DataAkamaiCloudletsPolicyActivationsPolicyInfoList":
        return typing.cast("DataAkamaiCloudletsPolicyActivationsPolicyInfoList", jsii.get(self, "policyInfo"))

    @builtins.property
    @jsii.member(jsii_name="propertyInfo")
    def property_info(self) -> "DataAkamaiCloudletsPolicyActivationsPropertyInfoList":
        return typing.cast("DataAkamaiCloudletsPolicyActivationsPropertyInfoList", jsii.get(self, "propertyInfo"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAkamaiCloudletsPolicyActivations]:
        return typing.cast(typing.Optional[DataAkamaiCloudletsPolicyActivations], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAkamaiCloudletsPolicyActivations],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a4197ab1e32c512fcc5f75dc0df9fcc5efd2038f51ae017bb58643ff0586eb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsPolicy.DataAkamaiCloudletsPolicyActivationsPolicyInfo",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiCloudletsPolicyActivationsPolicyInfo:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsPolicyActivationsPolicyInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudletsPolicyActivationsPolicyInfoList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsPolicy.DataAkamaiCloudletsPolicyActivationsPolicyInfoList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8e4a427b4cf74f896ae4ccfce7c9b4b0f9329cb8b88975522b075c99b3b60ecd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiCloudletsPolicyActivationsPolicyInfoOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1b172a2b7e590e1763a93a0ee2ce4ae347b200139db2e912216329f7804de69)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiCloudletsPolicyActivationsPolicyInfoOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bb073765bdb2b9aef9d0864d4eb035d7551c6c1b4840976cb671a7204b97f4e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b6675497e8ac8580dcb755a6cd4b1613ba9cf099392b19a00cee4b6fb1437a72)
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
            type_hints = typing.get_type_hints(_typecheckingstub__baa1b181b07bd66d6fe3ab93f9c518db30996bdc37d8d1e9231da38e0c8b158a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataAkamaiCloudletsPolicyActivationsPolicyInfoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsPolicy.DataAkamaiCloudletsPolicyActivationsPolicyInfoOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5a867b33336b2b94bcc9699dc5c7896526d1ad8dddc26e98637700323bb1f14a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="activatedBy")
    def activated_by(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "activatedBy"))

    @builtins.property
    @jsii.member(jsii_name="activationDate")
    def activation_date(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "activationDate"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="policyId")
    def policy_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "policyId"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="statusDetail")
    def status_detail(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statusDetail"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAkamaiCloudletsPolicyActivationsPolicyInfo]:
        return typing.cast(typing.Optional[DataAkamaiCloudletsPolicyActivationsPolicyInfo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAkamaiCloudletsPolicyActivationsPolicyInfo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60b9c72ca4c576d0678fc2cd43ff97d777164b79477b1fe8df455c4d71ecc8e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsPolicy.DataAkamaiCloudletsPolicyActivationsPropertyInfo",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiCloudletsPolicyActivationsPropertyInfo:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsPolicyActivationsPropertyInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCloudletsPolicyActivationsPropertyInfoList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsPolicy.DataAkamaiCloudletsPolicyActivationsPropertyInfoList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__02ffa80e086f7b2934f196df335dfa66d15f6828f285c6342fbb8ab68aab9b27)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiCloudletsPolicyActivationsPropertyInfoOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__302fc151a04c095ea82260fdad03ac8bcc40038dd356d982573d697f7467894f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiCloudletsPolicyActivationsPropertyInfoOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__290a5c9bd279cd997eccaf27b31985a9c1f807b87009b9068da55e102f4de1ad)
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
            type_hints = typing.get_type_hints(_typecheckingstub__271acd12d059b2290f6faba590227e5a57f67c32366cdab19b3b2d4f90d147ba)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d7aa3cc8beb5b67f03ffc396121218e7c4f54886d4c4e5bdbe84530f14a6879c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataAkamaiCloudletsPolicyActivationsPropertyInfoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCloudletsPolicy.DataAkamaiCloudletsPolicyActivationsPropertyInfoOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cf8b3012a6658a5423b46b47f092a3bc6bbf83218733531a66d8a5e6ae592a20)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="activatedBy")
    def activated_by(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "activatedBy"))

    @builtins.property
    @jsii.member(jsii_name="activationDate")
    def activation_date(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "activationDate"))

    @builtins.property
    @jsii.member(jsii_name="groupId")
    def group_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "groupId"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAkamaiCloudletsPolicyActivationsPropertyInfo]:
        return typing.cast(typing.Optional[DataAkamaiCloudletsPolicyActivationsPropertyInfo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAkamaiCloudletsPolicyActivationsPropertyInfo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3f9932b9527956b41d51ece815e61d258bba0d4490f96737739da0ddf19f2b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCloudletsPolicy.DataAkamaiCloudletsPolicyConfig",
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
        "id": "id",
        "version": "version",
    },
)
class DataAkamaiCloudletsPolicyConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        id: typing.Optional[builtins.str] = None,
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
        :param policy_id: An integer ID that is associated with a policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_policy#policy_id DataAkamaiCloudletsPolicy#policy_id}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_policy#id DataAkamaiCloudletsPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param version: The version number of the policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_policy#version DataAkamaiCloudletsPolicy#version}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c921136c18ad3fd4f75f73bc9099721ff937c0251f2d432d95822c4907d987c9)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument policy_id", value=policy_id, expected_type=type_hints["policy_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
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
        if id is not None:
            self._values["id"] = id
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_policy#policy_id DataAkamaiCloudletsPolicy#policy_id}
        '''
        result = self._values.get("policy_id")
        assert result is not None, "Required property 'policy_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_policy#id DataAkamaiCloudletsPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[jsii.Number]:
        '''The version number of the policy.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cloudlets_policy#version DataAkamaiCloudletsPolicy#version}
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCloudletsPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DataAkamaiCloudletsPolicy",
    "DataAkamaiCloudletsPolicyActivations",
    "DataAkamaiCloudletsPolicyActivationsList",
    "DataAkamaiCloudletsPolicyActivationsOutputReference",
    "DataAkamaiCloudletsPolicyActivationsPolicyInfo",
    "DataAkamaiCloudletsPolicyActivationsPolicyInfoList",
    "DataAkamaiCloudletsPolicyActivationsPolicyInfoOutputReference",
    "DataAkamaiCloudletsPolicyActivationsPropertyInfo",
    "DataAkamaiCloudletsPolicyActivationsPropertyInfoList",
    "DataAkamaiCloudletsPolicyActivationsPropertyInfoOutputReference",
    "DataAkamaiCloudletsPolicyConfig",
]

publication.publish()

def _typecheckingstub__87581871923df3b0ddb51f3454bb5d76e42dd4a728c9bc9b82037a4eb2d7ad8b(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    policy_id: jsii.Number,
    id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__23bce650235ba4f576f51735f20f89963d335d3c33e7593c46106de430018528(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29d02a17258ab38adcb01073588a089fe8e7d61185304526662eda6fa972f739(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30f646f53bb477c0bdcfab1dac7c2467e331a1d5dcec464742a7c5679d6dd8c2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de2999ca9754bcd472f1c8a0560da74531fd2d82518eb1c92c93be91dc6f4317(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b77d00b0c1081bc11dc10f0b5580ac536d6e087441265d97911f90824338d33d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab635b3dcfee464e5f6883c9d463598d0fa28cb0fa71c302cddd0b79a3912343(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d568df36a5355eb412d01319997d9b0ee68649b7575042e83d40ccc771464798(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35547daa505945c6ca59aa2c334ad852e0769e3f9a68549f9024f916e450698a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6478273e8afa758505746ab54a361894a45e6c15325c2dfe0b67a7ab8091819(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb1ca8ac586bd2adf81335cad0b3580c978535f7f0b2b5727d9234c04748debe(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a4197ab1e32c512fcc5f75dc0df9fcc5efd2038f51ae017bb58643ff0586eb5(
    value: typing.Optional[DataAkamaiCloudletsPolicyActivations],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e4a427b4cf74f896ae4ccfce7c9b4b0f9329cb8b88975522b075c99b3b60ecd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1b172a2b7e590e1763a93a0ee2ce4ae347b200139db2e912216329f7804de69(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bb073765bdb2b9aef9d0864d4eb035d7551c6c1b4840976cb671a7204b97f4e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6675497e8ac8580dcb755a6cd4b1613ba9cf099392b19a00cee4b6fb1437a72(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__baa1b181b07bd66d6fe3ab93f9c518db30996bdc37d8d1e9231da38e0c8b158a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a867b33336b2b94bcc9699dc5c7896526d1ad8dddc26e98637700323bb1f14a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60b9c72ca4c576d0678fc2cd43ff97d777164b79477b1fe8df455c4d71ecc8e0(
    value: typing.Optional[DataAkamaiCloudletsPolicyActivationsPolicyInfo],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02ffa80e086f7b2934f196df335dfa66d15f6828f285c6342fbb8ab68aab9b27(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__302fc151a04c095ea82260fdad03ac8bcc40038dd356d982573d697f7467894f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__290a5c9bd279cd997eccaf27b31985a9c1f807b87009b9068da55e102f4de1ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__271acd12d059b2290f6faba590227e5a57f67c32366cdab19b3b2d4f90d147ba(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7aa3cc8beb5b67f03ffc396121218e7c4f54886d4c4e5bdbe84530f14a6879c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf8b3012a6658a5423b46b47f092a3bc6bbf83218733531a66d8a5e6ae592a20(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3f9932b9527956b41d51ece815e61d258bba0d4490f96737739da0ddf19f2b9(
    value: typing.Optional[DataAkamaiCloudletsPolicyActivationsPropertyInfo],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c921136c18ad3fd4f75f73bc9099721ff937c0251f2d432d95822c4907d987c9(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    policy_id: jsii.Number,
    id: typing.Optional[builtins.str] = None,
    version: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass
