'''
# `akamai_imaging_policy_video`

Refer to the Terraform Registry for docs: [`akamai_imaging_policy_video`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/imaging_policy_video).
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


class ImagingPolicyVideo(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.imagingPolicyVideo.ImagingPolicyVideo",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/imaging_policy_video akamai_imaging_policy_video}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        contract_id: builtins.str,
        json: builtins.str,
        policy_id: builtins.str,
        policyset_id: builtins.str,
        activate_on_production: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/imaging_policy_video akamai_imaging_policy_video} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param contract_id: Unique identifier for the Akamai Contract containing the Policy Set(s). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/imaging_policy_video#contract_id ImagingPolicyVideo#contract_id}
        :param json: A JSON encoded policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/imaging_policy_video#json ImagingPolicyVideo#json}
        :param policy_id: Unique identifier for a Policy. It is not possible to modify the id of the policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/imaging_policy_video#policy_id ImagingPolicyVideo#policy_id}
        :param policyset_id: Unique identifier for the Image & Video Manager Policy Set. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/imaging_policy_video#policyset_id ImagingPolicyVideo#policyset_id}
        :param activate_on_production: With this flag set to false, the user can perform modifications on staging without affecting the version already saved to production. With this flag set to true, the policy will be saved on the production network. It is possible to change it back to false only when there are any changes to the policy qualifying it for the new version. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/imaging_policy_video#activate_on_production ImagingPolicyVideo#activate_on_production}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/imaging_policy_video#id ImagingPolicyVideo#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cab353bce3e77f81c7ef224c2d83a7e20cc3f766ab16890bcccb837119fd69c0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ImagingPolicyVideoConfig(
            contract_id=contract_id,
            json=json,
            policy_id=policy_id,
            policyset_id=policyset_id,
            activate_on_production=activate_on_production,
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
        '''Generates CDKTF code for importing a ImagingPolicyVideo resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the ImagingPolicyVideo to import.
        :param import_from_id: The id of the existing ImagingPolicyVideo that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/imaging_policy_video#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the ImagingPolicyVideo to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__462833115a8be95cc6b684f61ee5a0d5cf82ff8b4b7643382deae0a5cab5d7d3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetActivateOnProduction")
    def reset_activate_on_production(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActivateOnProduction", []))

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
    @jsii.member(jsii_name="version")
    def version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="activateOnProductionInput")
    def activate_on_production_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "activateOnProductionInput"))

    @builtins.property
    @jsii.member(jsii_name="contractIdInput")
    def contract_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contractIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="jsonInput")
    def json_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jsonInput"))

    @builtins.property
    @jsii.member(jsii_name="policyIdInput")
    def policy_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="policysetIdInput")
    def policyset_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policysetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="activateOnProduction")
    def activate_on_production(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "activateOnProduction"))

    @activate_on_production.setter
    def activate_on_production(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70f0568ec6cd7f2a2fbb956a9dd7e55754fc12931b84591e3bf9757575d6b4a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "activateOnProduction", value)

    @builtins.property
    @jsii.member(jsii_name="contractId")
    def contract_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contractId"))

    @contract_id.setter
    def contract_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c715683ffff8e656b532cb2bef56823bc4ad71c0f9ffd8996fa4b1e88f3cf1b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contractId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fae3268992ebfe4a9ae87315e2f22db48d1ddcfb7a5a7b7fe4e320ae706ae9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="json")
    def json(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "json"))

    @json.setter
    def json(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cb665a77deb36692a34754219dfdd68afb394a998d3d8cd92bbd5fec92d712d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "json", value)

    @builtins.property
    @jsii.member(jsii_name="policyId")
    def policy_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policyId"))

    @policy_id.setter
    def policy_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d593fcd8d0e66a10c524642957f3e319930a019079cb8e7b62f552255f1812b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyId", value)

    @builtins.property
    @jsii.member(jsii_name="policysetId")
    def policyset_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policysetId"))

    @policyset_id.setter
    def policyset_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc0b02f491cc602c38281942f31999a958ef23fe32211c79df8891c0531a6c94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policysetId", value)


@jsii.data_type(
    jsii_type="akamai.imagingPolicyVideo.ImagingPolicyVideoConfig",
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
        "json": "json",
        "policy_id": "policyId",
        "policyset_id": "policysetId",
        "activate_on_production": "activateOnProduction",
        "id": "id",
    },
)
class ImagingPolicyVideoConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        json: builtins.str,
        policy_id: builtins.str,
        policyset_id: builtins.str,
        activate_on_production: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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
        :param contract_id: Unique identifier for the Akamai Contract containing the Policy Set(s). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/imaging_policy_video#contract_id ImagingPolicyVideo#contract_id}
        :param json: A JSON encoded policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/imaging_policy_video#json ImagingPolicyVideo#json}
        :param policy_id: Unique identifier for a Policy. It is not possible to modify the id of the policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/imaging_policy_video#policy_id ImagingPolicyVideo#policy_id}
        :param policyset_id: Unique identifier for the Image & Video Manager Policy Set. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/imaging_policy_video#policyset_id ImagingPolicyVideo#policyset_id}
        :param activate_on_production: With this flag set to false, the user can perform modifications on staging without affecting the version already saved to production. With this flag set to true, the policy will be saved on the production network. It is possible to change it back to false only when there are any changes to the policy qualifying it for the new version. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/imaging_policy_video#activate_on_production ImagingPolicyVideo#activate_on_production}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/imaging_policy_video#id ImagingPolicyVideo#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52f2174d6dbd6059b800087ff42623b8aba16001326ed8c2ece1e78852040b42)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument contract_id", value=contract_id, expected_type=type_hints["contract_id"])
            check_type(argname="argument json", value=json, expected_type=type_hints["json"])
            check_type(argname="argument policy_id", value=policy_id, expected_type=type_hints["policy_id"])
            check_type(argname="argument policyset_id", value=policyset_id, expected_type=type_hints["policyset_id"])
            check_type(argname="argument activate_on_production", value=activate_on_production, expected_type=type_hints["activate_on_production"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "contract_id": contract_id,
            "json": json,
            "policy_id": policy_id,
            "policyset_id": policyset_id,
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
        if activate_on_production is not None:
            self._values["activate_on_production"] = activate_on_production
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
        '''Unique identifier for the Akamai Contract containing the Policy Set(s).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/imaging_policy_video#contract_id ImagingPolicyVideo#contract_id}
        '''
        result = self._values.get("contract_id")
        assert result is not None, "Required property 'contract_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def json(self) -> builtins.str:
        '''A JSON encoded policy.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/imaging_policy_video#json ImagingPolicyVideo#json}
        '''
        result = self._values.get("json")
        assert result is not None, "Required property 'json' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_id(self) -> builtins.str:
        '''Unique identifier for a Policy. It is not possible to modify the id of the policy.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/imaging_policy_video#policy_id ImagingPolicyVideo#policy_id}
        '''
        result = self._values.get("policy_id")
        assert result is not None, "Required property 'policy_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policyset_id(self) -> builtins.str:
        '''Unique identifier for the Image & Video Manager Policy Set.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/imaging_policy_video#policyset_id ImagingPolicyVideo#policyset_id}
        '''
        result = self._values.get("policyset_id")
        assert result is not None, "Required property 'policyset_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def activate_on_production(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''With this flag set to false, the user can perform modifications on staging without affecting the version already saved to production.

        With this flag set to true, the policy will be saved on the production network. It is possible to change it back to false only when there are any changes to the policy qualifying it for the new version.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/imaging_policy_video#activate_on_production ImagingPolicyVideo#activate_on_production}
        '''
        result = self._values.get("activate_on_production")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/imaging_policy_video#id ImagingPolicyVideo#id}.

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
        return "ImagingPolicyVideoConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ImagingPolicyVideo",
    "ImagingPolicyVideoConfig",
]

publication.publish()

def _typecheckingstub__cab353bce3e77f81c7ef224c2d83a7e20cc3f766ab16890bcccb837119fd69c0(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    contract_id: builtins.str,
    json: builtins.str,
    policy_id: builtins.str,
    policyset_id: builtins.str,
    activate_on_production: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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

def _typecheckingstub__462833115a8be95cc6b684f61ee5a0d5cf82ff8b4b7643382deae0a5cab5d7d3(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70f0568ec6cd7f2a2fbb956a9dd7e55754fc12931b84591e3bf9757575d6b4a4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c715683ffff8e656b532cb2bef56823bc4ad71c0f9ffd8996fa4b1e88f3cf1b0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fae3268992ebfe4a9ae87315e2f22db48d1ddcfb7a5a7b7fe4e320ae706ae9e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cb665a77deb36692a34754219dfdd68afb394a998d3d8cd92bbd5fec92d712d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d593fcd8d0e66a10c524642957f3e319930a019079cb8e7b62f552255f1812b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc0b02f491cc602c38281942f31999a958ef23fe32211c79df8891c0531a6c94(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52f2174d6dbd6059b800087ff42623b8aba16001326ed8c2ece1e78852040b42(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    contract_id: builtins.str,
    json: builtins.str,
    policy_id: builtins.str,
    policyset_id: builtins.str,
    activate_on_production: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
