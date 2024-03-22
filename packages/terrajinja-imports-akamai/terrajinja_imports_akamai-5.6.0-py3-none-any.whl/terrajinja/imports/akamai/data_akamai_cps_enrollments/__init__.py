'''
# `data_akamai_cps_enrollments`

Refer to the Terraform Registry for docs: [`data_akamai_cps_enrollments`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cps_enrollments).
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


class DataAkamaiCpsEnrollments(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCpsEnrollments.DataAkamaiCpsEnrollments",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cps_enrollments akamai_cps_enrollments}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        contract_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cps_enrollments akamai_cps_enrollments} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param contract_id: Contract ID for which enrollments are retrieved. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cps_enrollments#contract_id DataAkamaiCpsEnrollments#contract_id}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cps_enrollments#id DataAkamaiCpsEnrollments#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e06682e36098b9195c48a06654703b07c514a695aaf60be9063ba4d888a55adc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAkamaiCpsEnrollmentsConfig(
            contract_id=contract_id,
            id=id,
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
        '''Generates CDKTF code for importing a DataAkamaiCpsEnrollments resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the DataAkamaiCpsEnrollments to import.
        :param import_from_id: The id of the existing DataAkamaiCpsEnrollments that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cps_enrollments#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the DataAkamaiCpsEnrollments to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7b2424d556ca68a19b5f86403c53b8b95fbedc58bf0804783e443158fcbde92)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    @jsii.member(jsii_name="enrollments")
    def enrollments(self) -> "DataAkamaiCpsEnrollmentsEnrollmentsList":
        return typing.cast("DataAkamaiCpsEnrollmentsEnrollmentsList", jsii.get(self, "enrollments"))

    @builtins.property
    @jsii.member(jsii_name="contractIdInput")
    def contract_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contractIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="contractId")
    def contract_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contractId"))

    @contract_id.setter
    def contract_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7a466c6a55b749a1524ec67b3e2afe3b75e20e847d5d8eb0e7a080c2deceaf6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contractId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7078f60212e683b7a3151db595a71bfd2e679af2e5e3f41f0d98559eeea85af5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCpsEnrollments.DataAkamaiCpsEnrollmentsConfig",
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
        "id": "id",
    },
)
class DataAkamaiCpsEnrollmentsConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param contract_id: Contract ID for which enrollments are retrieved. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cps_enrollments#contract_id DataAkamaiCpsEnrollments#contract_id}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cps_enrollments#id DataAkamaiCpsEnrollments#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c50cc0d2fc554db1f7902355c67724c6e490b79ed773f8ded0deeb98204b6d5e)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument contract_id", value=contract_id, expected_type=type_hints["contract_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "contract_id": contract_id,
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
        '''Contract ID for which enrollments are retrieved.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cps_enrollments#contract_id DataAkamaiCpsEnrollments#contract_id}
        '''
        result = self._values.get("contract_id")
        assert result is not None, "Required property 'contract_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/cps_enrollments#id DataAkamaiCpsEnrollments#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCpsEnrollmentsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCpsEnrollments.DataAkamaiCpsEnrollmentsEnrollments",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiCpsEnrollmentsEnrollments:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCpsEnrollmentsEnrollments(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCpsEnrollments.DataAkamaiCpsEnrollmentsEnrollmentsAdminContact",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiCpsEnrollmentsEnrollmentsAdminContact:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCpsEnrollmentsEnrollmentsAdminContact(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCpsEnrollmentsEnrollmentsAdminContactList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCpsEnrollments.DataAkamaiCpsEnrollmentsEnrollmentsAdminContactList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cb91928574de1db3f6b23fe22a30bd4a0209c4af80b334057d9269f4dc9294b7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiCpsEnrollmentsEnrollmentsAdminContactOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5f144d6bbd908d33542ac351e49e5caf1d5eedc31c9e4e3be67a534286d399f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiCpsEnrollmentsEnrollmentsAdminContactOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cb3894b7b2bb76e029a88fc3e7d466368c4d5f272754f563599987616b0ae81)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6ee466a8cd909bf774bae4bf7718227a5797f88f6ac385b7b347b0b6cab1f02b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d15c3dfaaed109656bc2086e3e7ea0c15198079ca448a9c3a6fa6b7f0875e0b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataAkamaiCpsEnrollmentsEnrollmentsAdminContactOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCpsEnrollments.DataAkamaiCpsEnrollmentsEnrollmentsAdminContactOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__46ebf2971b3274174e0569970e0490ca94f7070e8d068f3651b0143426090225)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="addressLineOne")
    def address_line_one(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "addressLineOne"))

    @builtins.property
    @jsii.member(jsii_name="addressLineTwo")
    def address_line_two(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "addressLineTwo"))

    @builtins.property
    @jsii.member(jsii_name="city")
    def city(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "city"))

    @builtins.property
    @jsii.member(jsii_name="countryCode")
    def country_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "countryCode"))

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @builtins.property
    @jsii.member(jsii_name="firstName")
    def first_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firstName"))

    @builtins.property
    @jsii.member(jsii_name="lastName")
    def last_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastName"))

    @builtins.property
    @jsii.member(jsii_name="organization")
    def organization(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organization"))

    @builtins.property
    @jsii.member(jsii_name="phone")
    def phone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "phone"))

    @builtins.property
    @jsii.member(jsii_name="postalCode")
    def postal_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "postalCode"))

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAkamaiCpsEnrollmentsEnrollmentsAdminContact]:
        return typing.cast(typing.Optional[DataAkamaiCpsEnrollmentsEnrollmentsAdminContact], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAkamaiCpsEnrollmentsEnrollmentsAdminContact],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__501787cce4f2179ad792f356e986eddd42ef96ac294980ad3bfd2569a50a10ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCpsEnrollments.DataAkamaiCpsEnrollmentsEnrollmentsCsr",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiCpsEnrollmentsEnrollmentsCsr:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCpsEnrollmentsEnrollmentsCsr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCpsEnrollmentsEnrollmentsCsrList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCpsEnrollments.DataAkamaiCpsEnrollmentsEnrollmentsCsrList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8cb9a5e8be23a3ce506f1df2d21a7429281ad3669d7f5ef737dffce37e6abab4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiCpsEnrollmentsEnrollmentsCsrOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8956128617827ed77626380f77990ffde7cf2609b7523f0eb8afd7e0e1cf30ba)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiCpsEnrollmentsEnrollmentsCsrOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c173c95cfd07e00649de415e87c28b25617fd0bd8b785cf2be98cb22cd349169)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d203b79f2191a96b0bfb831ec3ac2c7830acb303ecc6cb61dbead9dc27b95c8b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cd309a09f75d79486e35f3b68532bda20e7e1ef6e864dff8ac53a98ea8569ffe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataAkamaiCpsEnrollmentsEnrollmentsCsrOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCpsEnrollments.DataAkamaiCpsEnrollmentsEnrollmentsCsrOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7a9fc48758ac915ff9df6cd32b6dd293dfcb88fd59bdafd71b06f5ba77473741)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="city")
    def city(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "city"))

    @builtins.property
    @jsii.member(jsii_name="countryCode")
    def country_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "countryCode"))

    @builtins.property
    @jsii.member(jsii_name="organization")
    def organization(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organization"))

    @builtins.property
    @jsii.member(jsii_name="organizationalUnit")
    def organizational_unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organizationalUnit"))

    @builtins.property
    @jsii.member(jsii_name="preferredTrustChain")
    def preferred_trust_chain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "preferredTrustChain"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAkamaiCpsEnrollmentsEnrollmentsCsr]:
        return typing.cast(typing.Optional[DataAkamaiCpsEnrollmentsEnrollmentsCsr], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAkamaiCpsEnrollmentsEnrollmentsCsr],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8decc1c1b7834d6490638c8fe874af420a0d87c0b9962990035615b1b230ffe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCpsEnrollmentsEnrollmentsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCpsEnrollments.DataAkamaiCpsEnrollmentsEnrollmentsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8663f312210489f1f66d2e3fc34f0913869f600f632e1fb896ff4612cf725a3d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiCpsEnrollmentsEnrollmentsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d7e16d2b0dfdeac7f86b67005a42e08eb5e24feae079a3de1689be86336c43d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiCpsEnrollmentsEnrollmentsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ace62db4be630b19cfcecc3b8ee291339fcd9a4f3f09a4c8a4a5d09ded134c9f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b4188e290a5136b5c115051ad6018e4d22e7720ae622e4fbf30aa88b4d1e9997)
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
            type_hints = typing.get_type_hints(_typecheckingstub__22a8241801409be0b1eb38d73d1a5d6619986994ce5078ea601afe0e8f774039)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCpsEnrollments.DataAkamaiCpsEnrollmentsEnrollmentsNetworkConfiguration",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiCpsEnrollmentsEnrollmentsNetworkConfiguration:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCpsEnrollmentsEnrollmentsNetworkConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCpsEnrollments.DataAkamaiCpsEnrollmentsEnrollmentsNetworkConfigurationClientMutualAuthentication",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiCpsEnrollmentsEnrollmentsNetworkConfigurationClientMutualAuthentication:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCpsEnrollmentsEnrollmentsNetworkConfigurationClientMutualAuthentication(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCpsEnrollmentsEnrollmentsNetworkConfigurationClientMutualAuthenticationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCpsEnrollments.DataAkamaiCpsEnrollmentsEnrollmentsNetworkConfigurationClientMutualAuthenticationList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ae1032d3462eb1494cc06850b034e7f2a3fc57678507a37e375b26cff6e2c9d8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiCpsEnrollmentsEnrollmentsNetworkConfigurationClientMutualAuthenticationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c883a7c1de74b2f0b044348df8fe77cf5e0def32c8e4dab7f510eb54f48985b0)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiCpsEnrollmentsEnrollmentsNetworkConfigurationClientMutualAuthenticationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34eba161cbb715a97c763ce5871287de60c931ee6c7d4d5854e99294b95153c9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__de545aa4ae67ad9be9b2cb46971ea0f6a6f1b6923756b76993c1b3e6c0edf4b8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2d50cdaf9b3f78a78c7a143e4bbfd89d78a5d0c0f0a6560b85ae448eb2168673)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataAkamaiCpsEnrollmentsEnrollmentsNetworkConfigurationClientMutualAuthenticationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCpsEnrollments.DataAkamaiCpsEnrollmentsEnrollmentsNetworkConfigurationClientMutualAuthenticationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__71d7ba7fccb719177f98c508f4e297c0b6734d5a0c5c10f8f39d15bb46b889d6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="ocspEnabled")
    def ocsp_enabled(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "ocspEnabled"))

    @builtins.property
    @jsii.member(jsii_name="sendCaListToClient")
    def send_ca_list_to_client(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "sendCaListToClient"))

    @builtins.property
    @jsii.member(jsii_name="setId")
    def set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "setId"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAkamaiCpsEnrollmentsEnrollmentsNetworkConfigurationClientMutualAuthentication]:
        return typing.cast(typing.Optional[DataAkamaiCpsEnrollmentsEnrollmentsNetworkConfigurationClientMutualAuthentication], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAkamaiCpsEnrollmentsEnrollmentsNetworkConfigurationClientMutualAuthentication],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7df9b7eb7030df1a61e8323a965e9d7dd8cc898d7afbdda4e539c351e310ff1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCpsEnrollmentsEnrollmentsNetworkConfigurationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCpsEnrollments.DataAkamaiCpsEnrollmentsEnrollmentsNetworkConfigurationList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__877d751e38686dbd2ecd6e39a435ed3d23d188f630f1de5ccd5b6cb8589cfbaf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiCpsEnrollmentsEnrollmentsNetworkConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__869284542e3df7df3f2745daed5e60a0269c550e38120a6bb9fe595cfdb3872d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiCpsEnrollmentsEnrollmentsNetworkConfigurationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac136c24d345886fe4d1ffbc19e56c357d6788f0864d1aebc0b6f340423171e8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__19353d812df427a0caf1087bf6c5409313e51eb9470d24e277669403701d2bf4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__03ed086c4f864f7f8734ef8c985160c155619bbd2b7c437d2215b207bc15cdd7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataAkamaiCpsEnrollmentsEnrollmentsNetworkConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCpsEnrollments.DataAkamaiCpsEnrollmentsEnrollmentsNetworkConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3145ba25cacbed0e63ba55771e6a2209260c234b6dac23009576c9ec9f383b15)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="clientMutualAuthentication")
    def client_mutual_authentication(
        self,
    ) -> DataAkamaiCpsEnrollmentsEnrollmentsNetworkConfigurationClientMutualAuthenticationList:
        return typing.cast(DataAkamaiCpsEnrollmentsEnrollmentsNetworkConfigurationClientMutualAuthenticationList, jsii.get(self, "clientMutualAuthentication"))

    @builtins.property
    @jsii.member(jsii_name="cloneDnsNames")
    def clone_dns_names(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "cloneDnsNames"))

    @builtins.property
    @jsii.member(jsii_name="disallowedTlsVersions")
    def disallowed_tls_versions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "disallowedTlsVersions"))

    @builtins.property
    @jsii.member(jsii_name="geography")
    def geography(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "geography"))

    @builtins.property
    @jsii.member(jsii_name="mustHaveCiphers")
    def must_have_ciphers(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mustHaveCiphers"))

    @builtins.property
    @jsii.member(jsii_name="ocspStapling")
    def ocsp_stapling(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ocspStapling"))

    @builtins.property
    @jsii.member(jsii_name="preferredCiphers")
    def preferred_ciphers(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "preferredCiphers"))

    @builtins.property
    @jsii.member(jsii_name="quicEnabled")
    def quic_enabled(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "quicEnabled"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAkamaiCpsEnrollmentsEnrollmentsNetworkConfiguration]:
        return typing.cast(typing.Optional[DataAkamaiCpsEnrollmentsEnrollmentsNetworkConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAkamaiCpsEnrollmentsEnrollmentsNetworkConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4108a1c5b16491b787c7bbe22cd847cac7c88a7c192e5eecb8e5efde477d11b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCpsEnrollments.DataAkamaiCpsEnrollmentsEnrollmentsOrganization",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiCpsEnrollmentsEnrollmentsOrganization:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCpsEnrollmentsEnrollmentsOrganization(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCpsEnrollmentsEnrollmentsOrganizationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCpsEnrollments.DataAkamaiCpsEnrollmentsEnrollmentsOrganizationList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d0a50ee26248424d291b3650894cd3f7c5a2c7f5650582aa3f7081f6f897fb60)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiCpsEnrollmentsEnrollmentsOrganizationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92339bc3c76ddb9db628e20d740e785a06c34ac043765ab380f3ebd0e6daed28)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiCpsEnrollmentsEnrollmentsOrganizationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3a4c34fa1a9bb538127205d689a5e39c42ecbc6bc4d349096de9bbbee2df432)
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
            type_hints = typing.get_type_hints(_typecheckingstub__348a16e6e9eb51c1e0bc793a3f43a2895aa8a1769cbf5fddc9b171dbcbbf38bb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__656e0406eea65bf5a997b4222722dbbf5e760c062cf09359d0b0c810f2f6d3e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataAkamaiCpsEnrollmentsEnrollmentsOrganizationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCpsEnrollments.DataAkamaiCpsEnrollmentsEnrollmentsOrganizationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__05cfc13591a8bc66fbea1d38171ac435226ff067d09ce7fc483bdde2a4ce5125)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="addressLineOne")
    def address_line_one(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "addressLineOne"))

    @builtins.property
    @jsii.member(jsii_name="addressLineTwo")
    def address_line_two(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "addressLineTwo"))

    @builtins.property
    @jsii.member(jsii_name="city")
    def city(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "city"))

    @builtins.property
    @jsii.member(jsii_name="countryCode")
    def country_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "countryCode"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="phone")
    def phone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "phone"))

    @builtins.property
    @jsii.member(jsii_name="postalCode")
    def postal_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "postalCode"))

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAkamaiCpsEnrollmentsEnrollmentsOrganization]:
        return typing.cast(typing.Optional[DataAkamaiCpsEnrollmentsEnrollmentsOrganization], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAkamaiCpsEnrollmentsEnrollmentsOrganization],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d9ba014394a0a2e4f047e38c92d8936db17a1f81ccf36d3686c1b5847675358)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiCpsEnrollmentsEnrollmentsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCpsEnrollments.DataAkamaiCpsEnrollmentsEnrollmentsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1d7c274bfc1d59950782f629cf15069ef80e8b5247a6933482a9ab1e6f36e2eb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="adminContact")
    def admin_contact(self) -> DataAkamaiCpsEnrollmentsEnrollmentsAdminContactList:
        return typing.cast(DataAkamaiCpsEnrollmentsEnrollmentsAdminContactList, jsii.get(self, "adminContact"))

    @builtins.property
    @jsii.member(jsii_name="certificateChainType")
    def certificate_chain_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateChainType"))

    @builtins.property
    @jsii.member(jsii_name="certificateType")
    def certificate_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateType"))

    @builtins.property
    @jsii.member(jsii_name="commonName")
    def common_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "commonName"))

    @builtins.property
    @jsii.member(jsii_name="csr")
    def csr(self) -> DataAkamaiCpsEnrollmentsEnrollmentsCsrList:
        return typing.cast(DataAkamaiCpsEnrollmentsEnrollmentsCsrList, jsii.get(self, "csr"))

    @builtins.property
    @jsii.member(jsii_name="enableMultiStackedCertificates")
    def enable_multi_stacked_certificates(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "enableMultiStackedCertificates"))

    @builtins.property
    @jsii.member(jsii_name="enrollmentId")
    def enrollment_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "enrollmentId"))

    @builtins.property
    @jsii.member(jsii_name="networkConfiguration")
    def network_configuration(
        self,
    ) -> DataAkamaiCpsEnrollmentsEnrollmentsNetworkConfigurationList:
        return typing.cast(DataAkamaiCpsEnrollmentsEnrollmentsNetworkConfigurationList, jsii.get(self, "networkConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="organization")
    def organization(self) -> DataAkamaiCpsEnrollmentsEnrollmentsOrganizationList:
        return typing.cast(DataAkamaiCpsEnrollmentsEnrollmentsOrganizationList, jsii.get(self, "organization"))

    @builtins.property
    @jsii.member(jsii_name="pendingChanges")
    def pending_changes(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "pendingChanges"))

    @builtins.property
    @jsii.member(jsii_name="registrationAuthority")
    def registration_authority(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "registrationAuthority"))

    @builtins.property
    @jsii.member(jsii_name="sans")
    def sans(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sans"))

    @builtins.property
    @jsii.member(jsii_name="secureNetwork")
    def secure_network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secureNetwork"))

    @builtins.property
    @jsii.member(jsii_name="signatureAlgorithm")
    def signature_algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signatureAlgorithm"))

    @builtins.property
    @jsii.member(jsii_name="sniOnly")
    def sni_only(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "sniOnly"))

    @builtins.property
    @jsii.member(jsii_name="techContact")
    def tech_contact(self) -> "DataAkamaiCpsEnrollmentsEnrollmentsTechContactList":
        return typing.cast("DataAkamaiCpsEnrollmentsEnrollmentsTechContactList", jsii.get(self, "techContact"))

    @builtins.property
    @jsii.member(jsii_name="validationType")
    def validation_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "validationType"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAkamaiCpsEnrollmentsEnrollments]:
        return typing.cast(typing.Optional[DataAkamaiCpsEnrollmentsEnrollments], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAkamaiCpsEnrollmentsEnrollments],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__068727bb73818edff1392e237e1fcb1d76aa7f3179e1be02bf38cdda680e481d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiCpsEnrollments.DataAkamaiCpsEnrollmentsEnrollmentsTechContact",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAkamaiCpsEnrollmentsEnrollmentsTechContact:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiCpsEnrollmentsEnrollmentsTechContact(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiCpsEnrollmentsEnrollmentsTechContactList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCpsEnrollments.DataAkamaiCpsEnrollmentsEnrollmentsTechContactList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f5fe092a5804d499a3e00809263d408378d08332ff46b78a4a1703fb4a9d93f3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiCpsEnrollmentsEnrollmentsTechContactOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e980cab6f5d71e6f958b6203dc4a1144b71ad3069ffa9df4201bdd07711eb42)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiCpsEnrollmentsEnrollmentsTechContactOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5f638a4850a55bbf22335908a8dde3ded7c37c905c702872dff5711bfb3cebc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c3a07e636f9dbf82eed52eab30ac6eafcd5218c120443f14f8a07b37c5ff1859)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3137a75f57bdf8237037abf4aa60b3a6af89b1f1d34d54d273bddfe9fe88fc43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataAkamaiCpsEnrollmentsEnrollmentsTechContactOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiCpsEnrollments.DataAkamaiCpsEnrollmentsEnrollmentsTechContactOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fb5bc9ce51444448dba390eda3833ea0ed8b94cc4e490b4709a0a2cba5c47e79)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="addressLineOne")
    def address_line_one(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "addressLineOne"))

    @builtins.property
    @jsii.member(jsii_name="addressLineTwo")
    def address_line_two(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "addressLineTwo"))

    @builtins.property
    @jsii.member(jsii_name="city")
    def city(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "city"))

    @builtins.property
    @jsii.member(jsii_name="countryCode")
    def country_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "countryCode"))

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @builtins.property
    @jsii.member(jsii_name="firstName")
    def first_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firstName"))

    @builtins.property
    @jsii.member(jsii_name="lastName")
    def last_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastName"))

    @builtins.property
    @jsii.member(jsii_name="organization")
    def organization(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organization"))

    @builtins.property
    @jsii.member(jsii_name="phone")
    def phone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "phone"))

    @builtins.property
    @jsii.member(jsii_name="postalCode")
    def postal_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "postalCode"))

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAkamaiCpsEnrollmentsEnrollmentsTechContact]:
        return typing.cast(typing.Optional[DataAkamaiCpsEnrollmentsEnrollmentsTechContact], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAkamaiCpsEnrollmentsEnrollmentsTechContact],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0734d7f7f1211fef7cf28032c646ff5a4ea5b4e65f539f78571ab49b24a2baa5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataAkamaiCpsEnrollments",
    "DataAkamaiCpsEnrollmentsConfig",
    "DataAkamaiCpsEnrollmentsEnrollments",
    "DataAkamaiCpsEnrollmentsEnrollmentsAdminContact",
    "DataAkamaiCpsEnrollmentsEnrollmentsAdminContactList",
    "DataAkamaiCpsEnrollmentsEnrollmentsAdminContactOutputReference",
    "DataAkamaiCpsEnrollmentsEnrollmentsCsr",
    "DataAkamaiCpsEnrollmentsEnrollmentsCsrList",
    "DataAkamaiCpsEnrollmentsEnrollmentsCsrOutputReference",
    "DataAkamaiCpsEnrollmentsEnrollmentsList",
    "DataAkamaiCpsEnrollmentsEnrollmentsNetworkConfiguration",
    "DataAkamaiCpsEnrollmentsEnrollmentsNetworkConfigurationClientMutualAuthentication",
    "DataAkamaiCpsEnrollmentsEnrollmentsNetworkConfigurationClientMutualAuthenticationList",
    "DataAkamaiCpsEnrollmentsEnrollmentsNetworkConfigurationClientMutualAuthenticationOutputReference",
    "DataAkamaiCpsEnrollmentsEnrollmentsNetworkConfigurationList",
    "DataAkamaiCpsEnrollmentsEnrollmentsNetworkConfigurationOutputReference",
    "DataAkamaiCpsEnrollmentsEnrollmentsOrganization",
    "DataAkamaiCpsEnrollmentsEnrollmentsOrganizationList",
    "DataAkamaiCpsEnrollmentsEnrollmentsOrganizationOutputReference",
    "DataAkamaiCpsEnrollmentsEnrollmentsOutputReference",
    "DataAkamaiCpsEnrollmentsEnrollmentsTechContact",
    "DataAkamaiCpsEnrollmentsEnrollmentsTechContactList",
    "DataAkamaiCpsEnrollmentsEnrollmentsTechContactOutputReference",
]

publication.publish()

def _typecheckingstub__e06682e36098b9195c48a06654703b07c514a695aaf60be9063ba4d888a55adc(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    contract_id: builtins.str,
    id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__e7b2424d556ca68a19b5f86403c53b8b95fbedc58bf0804783e443158fcbde92(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7a466c6a55b749a1524ec67b3e2afe3b75e20e847d5d8eb0e7a080c2deceaf6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7078f60212e683b7a3151db595a71bfd2e679af2e5e3f41f0d98559eeea85af5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c50cc0d2fc554db1f7902355c67724c6e490b79ed773f8ded0deeb98204b6d5e(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    contract_id: builtins.str,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb91928574de1db3f6b23fe22a30bd4a0209c4af80b334057d9269f4dc9294b7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5f144d6bbd908d33542ac351e49e5caf1d5eedc31c9e4e3be67a534286d399f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cb3894b7b2bb76e029a88fc3e7d466368c4d5f272754f563599987616b0ae81(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ee466a8cd909bf774bae4bf7718227a5797f88f6ac385b7b347b0b6cab1f02b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d15c3dfaaed109656bc2086e3e7ea0c15198079ca448a9c3a6fa6b7f0875e0b1(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46ebf2971b3274174e0569970e0490ca94f7070e8d068f3651b0143426090225(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__501787cce4f2179ad792f356e986eddd42ef96ac294980ad3bfd2569a50a10ed(
    value: typing.Optional[DataAkamaiCpsEnrollmentsEnrollmentsAdminContact],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cb9a5e8be23a3ce506f1df2d21a7429281ad3669d7f5ef737dffce37e6abab4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8956128617827ed77626380f77990ffde7cf2609b7523f0eb8afd7e0e1cf30ba(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c173c95cfd07e00649de415e87c28b25617fd0bd8b785cf2be98cb22cd349169(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d203b79f2191a96b0bfb831ec3ac2c7830acb303ecc6cb61dbead9dc27b95c8b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd309a09f75d79486e35f3b68532bda20e7e1ef6e864dff8ac53a98ea8569ffe(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a9fc48758ac915ff9df6cd32b6dd293dfcb88fd59bdafd71b06f5ba77473741(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8decc1c1b7834d6490638c8fe874af420a0d87c0b9962990035615b1b230ffe(
    value: typing.Optional[DataAkamaiCpsEnrollmentsEnrollmentsCsr],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8663f312210489f1f66d2e3fc34f0913869f600f632e1fb896ff4612cf725a3d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d7e16d2b0dfdeac7f86b67005a42e08eb5e24feae079a3de1689be86336c43d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ace62db4be630b19cfcecc3b8ee291339fcd9a4f3f09a4c8a4a5d09ded134c9f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4188e290a5136b5c115051ad6018e4d22e7720ae622e4fbf30aa88b4d1e9997(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22a8241801409be0b1eb38d73d1a5d6619986994ce5078ea601afe0e8f774039(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae1032d3462eb1494cc06850b034e7f2a3fc57678507a37e375b26cff6e2c9d8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c883a7c1de74b2f0b044348df8fe77cf5e0def32c8e4dab7f510eb54f48985b0(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34eba161cbb715a97c763ce5871287de60c931ee6c7d4d5854e99294b95153c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de545aa4ae67ad9be9b2cb46971ea0f6a6f1b6923756b76993c1b3e6c0edf4b8(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d50cdaf9b3f78a78c7a143e4bbfd89d78a5d0c0f0a6560b85ae448eb2168673(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71d7ba7fccb719177f98c508f4e297c0b6734d5a0c5c10f8f39d15bb46b889d6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7df9b7eb7030df1a61e8323a965e9d7dd8cc898d7afbdda4e539c351e310ff1(
    value: typing.Optional[DataAkamaiCpsEnrollmentsEnrollmentsNetworkConfigurationClientMutualAuthentication],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__877d751e38686dbd2ecd6e39a435ed3d23d188f630f1de5ccd5b6cb8589cfbaf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__869284542e3df7df3f2745daed5e60a0269c550e38120a6bb9fe595cfdb3872d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac136c24d345886fe4d1ffbc19e56c357d6788f0864d1aebc0b6f340423171e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19353d812df427a0caf1087bf6c5409313e51eb9470d24e277669403701d2bf4(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03ed086c4f864f7f8734ef8c985160c155619bbd2b7c437d2215b207bc15cdd7(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3145ba25cacbed0e63ba55771e6a2209260c234b6dac23009576c9ec9f383b15(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4108a1c5b16491b787c7bbe22cd847cac7c88a7c192e5eecb8e5efde477d11b(
    value: typing.Optional[DataAkamaiCpsEnrollmentsEnrollmentsNetworkConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0a50ee26248424d291b3650894cd3f7c5a2c7f5650582aa3f7081f6f897fb60(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92339bc3c76ddb9db628e20d740e785a06c34ac043765ab380f3ebd0e6daed28(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3a4c34fa1a9bb538127205d689a5e39c42ecbc6bc4d349096de9bbbee2df432(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__348a16e6e9eb51c1e0bc793a3f43a2895aa8a1769cbf5fddc9b171dbcbbf38bb(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__656e0406eea65bf5a997b4222722dbbf5e760c062cf09359d0b0c810f2f6d3e5(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05cfc13591a8bc66fbea1d38171ac435226ff067d09ce7fc483bdde2a4ce5125(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d9ba014394a0a2e4f047e38c92d8936db17a1f81ccf36d3686c1b5847675358(
    value: typing.Optional[DataAkamaiCpsEnrollmentsEnrollmentsOrganization],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d7c274bfc1d59950782f629cf15069ef80e8b5247a6933482a9ab1e6f36e2eb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__068727bb73818edff1392e237e1fcb1d76aa7f3179e1be02bf38cdda680e481d(
    value: typing.Optional[DataAkamaiCpsEnrollmentsEnrollments],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5fe092a5804d499a3e00809263d408378d08332ff46b78a4a1703fb4a9d93f3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e980cab6f5d71e6f958b6203dc4a1144b71ad3069ffa9df4201bdd07711eb42(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5f638a4850a55bbf22335908a8dde3ded7c37c905c702872dff5711bfb3cebc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3a07e636f9dbf82eed52eab30ac6eafcd5218c120443f14f8a07b37c5ff1859(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3137a75f57bdf8237037abf4aa60b3a6af89b1f1d34d54d273bddfe9fe88fc43(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb5bc9ce51444448dba390eda3833ea0ed8b94cc4e490b4709a0a2cba5c47e79(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0734d7f7f1211fef7cf28032c646ff5a4ea5b4e65f539f78571ab49b24a2baa5(
    value: typing.Optional[DataAkamaiCpsEnrollmentsEnrollmentsTechContact],
) -> None:
    """Type checking stubs"""
    pass
