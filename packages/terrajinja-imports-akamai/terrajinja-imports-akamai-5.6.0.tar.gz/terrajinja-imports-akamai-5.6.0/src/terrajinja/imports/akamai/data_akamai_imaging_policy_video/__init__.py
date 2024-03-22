'''
# `data_akamai_imaging_policy_video`

Refer to the Terraform Registry for docs: [`data_akamai_imaging_policy_video`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video).
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


class DataAkamaiImagingPolicyVideo(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiImagingPolicyVideo.DataAkamaiImagingPolicyVideo",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video akamai_imaging_policy_video}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        policy: typing.Union["DataAkamaiImagingPolicyVideoPolicy", typing.Dict[builtins.str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video akamai_imaging_policy_video} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param policy: policy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#policy DataAkamaiImagingPolicyVideo#policy}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#id DataAkamaiImagingPolicyVideo#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c96bfc5e8e884df10981289855d54a84dd83be22c43e2d8b621aebbc2abb56f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAkamaiImagingPolicyVideoConfig(
            policy=policy,
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
        '''Generates CDKTF code for importing a DataAkamaiImagingPolicyVideo resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the DataAkamaiImagingPolicyVideo to import.
        :param import_from_id: The id of the existing DataAkamaiImagingPolicyVideo that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the DataAkamaiImagingPolicyVideo to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__601d1fa6ec585593dd1bcdc8aeb7fdbbfa943cc4d2ab8358f8dcb5f745d5413a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putPolicy")
    def put_policy(
        self,
        *,
        breakpoints: typing.Optional[typing.Union["DataAkamaiImagingPolicyVideoPolicyBreakpoints", typing.Dict[builtins.str, typing.Any]]] = None,
        hosts: typing.Optional[typing.Sequence[builtins.str]] = None,
        output: typing.Optional[typing.Union["DataAkamaiImagingPolicyVideoPolicyOutput", typing.Dict[builtins.str, typing.Any]]] = None,
        rollout_duration: typing.Optional[builtins.str] = None,
        variables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiImagingPolicyVideoPolicyVariables", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param breakpoints: breakpoints block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#breakpoints DataAkamaiImagingPolicyVideo#breakpoints}
        :param hosts: Hosts that are allowed for image/video URLs within transformations or variables. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#hosts DataAkamaiImagingPolicyVideo#hosts}
        :param output: output block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#output DataAkamaiImagingPolicyVideo#output}
        :param rollout_duration: The amount of time in seconds that the policy takes to rollout. During the rollout an increasing proportion of images/videos will begin to use the new policy instead of the cached images/videos from the previous version. This value has no effect on the staging network. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#rollout_duration DataAkamaiImagingPolicyVideo#rollout_duration}
        :param variables: variables block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#variables DataAkamaiImagingPolicyVideo#variables}
        '''
        value = DataAkamaiImagingPolicyVideoPolicy(
            breakpoints=breakpoints,
            hosts=hosts,
            output=output,
            rollout_duration=rollout_duration,
            variables=variables,
        )

        return typing.cast(None, jsii.invoke(self, "putPolicy", [value]))

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
    @jsii.member(jsii_name="json")
    def json(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "json"))

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> "DataAkamaiImagingPolicyVideoPolicyOutputReference":
        return typing.cast("DataAkamaiImagingPolicyVideoPolicyOutputReference", jsii.get(self, "policy"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="policyInput")
    def policy_input(self) -> typing.Optional["DataAkamaiImagingPolicyVideoPolicy"]:
        return typing.cast(typing.Optional["DataAkamaiImagingPolicyVideoPolicy"], jsii.get(self, "policyInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b776ef9fff804195cee6502364f97d3e0ac4ed464c75945d583d07e5a723b6d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiImagingPolicyVideo.DataAkamaiImagingPolicyVideoConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "policy": "policy",
        "id": "id",
    },
)
class DataAkamaiImagingPolicyVideoConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        policy: typing.Union["DataAkamaiImagingPolicyVideoPolicy", typing.Dict[builtins.str, typing.Any]],
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
        :param policy: policy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#policy DataAkamaiImagingPolicyVideo#policy}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#id DataAkamaiImagingPolicyVideo#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(policy, dict):
            policy = DataAkamaiImagingPolicyVideoPolicy(**policy)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__906b4064a4d8d03e8df77f5b05a9805dfe935891929f5f1305d0d51f561cbc35)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy": policy,
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
    def policy(self) -> "DataAkamaiImagingPolicyVideoPolicy":
        '''policy block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#policy DataAkamaiImagingPolicyVideo#policy}
        '''
        result = self._values.get("policy")
        assert result is not None, "Required property 'policy' is missing"
        return typing.cast("DataAkamaiImagingPolicyVideoPolicy", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#id DataAkamaiImagingPolicyVideo#id}.

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
        return "DataAkamaiImagingPolicyVideoConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dataAkamaiImagingPolicyVideo.DataAkamaiImagingPolicyVideoPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "breakpoints": "breakpoints",
        "hosts": "hosts",
        "output": "output",
        "rollout_duration": "rolloutDuration",
        "variables": "variables",
    },
)
class DataAkamaiImagingPolicyVideoPolicy:
    def __init__(
        self,
        *,
        breakpoints: typing.Optional[typing.Union["DataAkamaiImagingPolicyVideoPolicyBreakpoints", typing.Dict[builtins.str, typing.Any]]] = None,
        hosts: typing.Optional[typing.Sequence[builtins.str]] = None,
        output: typing.Optional[typing.Union["DataAkamaiImagingPolicyVideoPolicyOutput", typing.Dict[builtins.str, typing.Any]]] = None,
        rollout_duration: typing.Optional[builtins.str] = None,
        variables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiImagingPolicyVideoPolicyVariables", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param breakpoints: breakpoints block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#breakpoints DataAkamaiImagingPolicyVideo#breakpoints}
        :param hosts: Hosts that are allowed for image/video URLs within transformations or variables. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#hosts DataAkamaiImagingPolicyVideo#hosts}
        :param output: output block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#output DataAkamaiImagingPolicyVideo#output}
        :param rollout_duration: The amount of time in seconds that the policy takes to rollout. During the rollout an increasing proportion of images/videos will begin to use the new policy instead of the cached images/videos from the previous version. This value has no effect on the staging network. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#rollout_duration DataAkamaiImagingPolicyVideo#rollout_duration}
        :param variables: variables block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#variables DataAkamaiImagingPolicyVideo#variables}
        '''
        if isinstance(breakpoints, dict):
            breakpoints = DataAkamaiImagingPolicyVideoPolicyBreakpoints(**breakpoints)
        if isinstance(output, dict):
            output = DataAkamaiImagingPolicyVideoPolicyOutput(**output)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2b43843d81cf2cf5a86092588063a070a148f904f6b3579424a10966822aad5)
            check_type(argname="argument breakpoints", value=breakpoints, expected_type=type_hints["breakpoints"])
            check_type(argname="argument hosts", value=hosts, expected_type=type_hints["hosts"])
            check_type(argname="argument output", value=output, expected_type=type_hints["output"])
            check_type(argname="argument rollout_duration", value=rollout_duration, expected_type=type_hints["rollout_duration"])
            check_type(argname="argument variables", value=variables, expected_type=type_hints["variables"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if breakpoints is not None:
            self._values["breakpoints"] = breakpoints
        if hosts is not None:
            self._values["hosts"] = hosts
        if output is not None:
            self._values["output"] = output
        if rollout_duration is not None:
            self._values["rollout_duration"] = rollout_duration
        if variables is not None:
            self._values["variables"] = variables

    @builtins.property
    def breakpoints(
        self,
    ) -> typing.Optional["DataAkamaiImagingPolicyVideoPolicyBreakpoints"]:
        '''breakpoints block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#breakpoints DataAkamaiImagingPolicyVideo#breakpoints}
        '''
        result = self._values.get("breakpoints")
        return typing.cast(typing.Optional["DataAkamaiImagingPolicyVideoPolicyBreakpoints"], result)

    @builtins.property
    def hosts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Hosts that are allowed for image/video URLs within transformations or variables.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#hosts DataAkamaiImagingPolicyVideo#hosts}
        '''
        result = self._values.get("hosts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def output(self) -> typing.Optional["DataAkamaiImagingPolicyVideoPolicyOutput"]:
        '''output block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#output DataAkamaiImagingPolicyVideo#output}
        '''
        result = self._values.get("output")
        return typing.cast(typing.Optional["DataAkamaiImagingPolicyVideoPolicyOutput"], result)

    @builtins.property
    def rollout_duration(self) -> typing.Optional[builtins.str]:
        '''The amount of time in seconds that the policy takes to rollout.

        During the rollout an increasing proportion of images/videos will begin to use the new policy instead of the cached images/videos from the previous version. This value has no effect on the staging network.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#rollout_duration DataAkamaiImagingPolicyVideo#rollout_duration}
        '''
        result = self._values.get("rollout_duration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def variables(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiImagingPolicyVideoPolicyVariables"]]]:
        '''variables block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#variables DataAkamaiImagingPolicyVideo#variables}
        '''
        result = self._values.get("variables")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiImagingPolicyVideoPolicyVariables"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiImagingPolicyVideoPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dataAkamaiImagingPolicyVideo.DataAkamaiImagingPolicyVideoPolicyBreakpoints",
    jsii_struct_bases=[],
    name_mapping={"widths": "widths"},
)
class DataAkamaiImagingPolicyVideoPolicyBreakpoints:
    def __init__(
        self,
        *,
        widths: typing.Optional[typing.Sequence[jsii.Number]] = None,
    ) -> None:
        '''
        :param widths: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#widths DataAkamaiImagingPolicyVideo#widths}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cc9e503ea0e19d606d21c32d3457e49eb6e723bcc288d38e34284e33bc33c22)
            check_type(argname="argument widths", value=widths, expected_type=type_hints["widths"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if widths is not None:
            self._values["widths"] = widths

    @builtins.property
    def widths(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#widths DataAkamaiImagingPolicyVideo#widths}.'''
        result = self._values.get("widths")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiImagingPolicyVideoPolicyBreakpoints(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiImagingPolicyVideoPolicyBreakpointsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiImagingPolicyVideo.DataAkamaiImagingPolicyVideoPolicyBreakpointsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__57f367e523c3e0e471cb8efa3b84ee9d94ffdee02648c7487f1e43b786731289)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetWidths")
    def reset_widths(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWidths", []))

    @builtins.property
    @jsii.member(jsii_name="widthsInput")
    def widths_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "widthsInput"))

    @builtins.property
    @jsii.member(jsii_name="widths")
    def widths(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "widths"))

    @widths.setter
    def widths(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3e4a8c47b70528e542996dcd18e1afcf4544d53ec7dcbd585488f723ee21975)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "widths", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAkamaiImagingPolicyVideoPolicyBreakpoints]:
        return typing.cast(typing.Optional[DataAkamaiImagingPolicyVideoPolicyBreakpoints], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAkamaiImagingPolicyVideoPolicyBreakpoints],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9188ae8e442e8efe5855395b1642d5d8e184d1ac0c9bbcbad237b29a37ae3e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiImagingPolicyVideo.DataAkamaiImagingPolicyVideoPolicyOutput",
    jsii_struct_bases=[],
    name_mapping={
        "perceptual_quality": "perceptualQuality",
        "perceptual_quality_var": "perceptualQualityVar",
        "placeholder_video_url": "placeholderVideoUrl",
        "placeholder_video_url_var": "placeholderVideoUrlVar",
        "video_adaptive_quality": "videoAdaptiveQuality",
        "video_adaptive_quality_var": "videoAdaptiveQualityVar",
    },
)
class DataAkamaiImagingPolicyVideoPolicyOutput:
    def __init__(
        self,
        *,
        perceptual_quality: typing.Optional[builtins.str] = None,
        perceptual_quality_var: typing.Optional[builtins.str] = None,
        placeholder_video_url: typing.Optional[builtins.str] = None,
        placeholder_video_url_var: typing.Optional[builtins.str] = None,
        video_adaptive_quality: typing.Optional[builtins.str] = None,
        video_adaptive_quality_var: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param perceptual_quality: The quality of derivative videos. High preserves video quality with reduced byte savings while low reduces video quality to increase byte savings. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#perceptual_quality DataAkamaiImagingPolicyVideo#perceptual_quality}
        :param perceptual_quality_var: The quality of derivative videos. High preserves video quality with reduced byte savings while low reduces video quality to increase byte savings. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#perceptual_quality_var DataAkamaiImagingPolicyVideo#perceptual_quality_var}
        :param placeholder_video_url: Allows you to add a specific placeholder video that appears when a user first requests a video, but before Image & Video Manager processes the video. If not specified the original video plays during the processing time. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#placeholder_video_url DataAkamaiImagingPolicyVideo#placeholder_video_url}
        :param placeholder_video_url_var: Allows you to add a specific placeholder video that appears when a user first requests a video, but before Image & Video Manager processes the video. If not specified the original video plays during the processing time. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#placeholder_video_url_var DataAkamaiImagingPolicyVideo#placeholder_video_url_var}
        :param video_adaptive_quality: Override the quality of video to serve when Image & Video Manager detects a slow connection. Specifying lower values lets users with slow connections browse your site with reduced load times without impacting the quality of videos for users with faster connections. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#video_adaptive_quality DataAkamaiImagingPolicyVideo#video_adaptive_quality}
        :param video_adaptive_quality_var: Override the quality of video to serve when Image & Video Manager detects a slow connection. Specifying lower values lets users with slow connections browse your site with reduced load times without impacting the quality of videos for users with faster connections. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#video_adaptive_quality_var DataAkamaiImagingPolicyVideo#video_adaptive_quality_var}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e8324c05e97d278ccdaf690ed9edc349d902603467fe5f13e9f78e94d372eaa)
            check_type(argname="argument perceptual_quality", value=perceptual_quality, expected_type=type_hints["perceptual_quality"])
            check_type(argname="argument perceptual_quality_var", value=perceptual_quality_var, expected_type=type_hints["perceptual_quality_var"])
            check_type(argname="argument placeholder_video_url", value=placeholder_video_url, expected_type=type_hints["placeholder_video_url"])
            check_type(argname="argument placeholder_video_url_var", value=placeholder_video_url_var, expected_type=type_hints["placeholder_video_url_var"])
            check_type(argname="argument video_adaptive_quality", value=video_adaptive_quality, expected_type=type_hints["video_adaptive_quality"])
            check_type(argname="argument video_adaptive_quality_var", value=video_adaptive_quality_var, expected_type=type_hints["video_adaptive_quality_var"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if perceptual_quality is not None:
            self._values["perceptual_quality"] = perceptual_quality
        if perceptual_quality_var is not None:
            self._values["perceptual_quality_var"] = perceptual_quality_var
        if placeholder_video_url is not None:
            self._values["placeholder_video_url"] = placeholder_video_url
        if placeholder_video_url_var is not None:
            self._values["placeholder_video_url_var"] = placeholder_video_url_var
        if video_adaptive_quality is not None:
            self._values["video_adaptive_quality"] = video_adaptive_quality
        if video_adaptive_quality_var is not None:
            self._values["video_adaptive_quality_var"] = video_adaptive_quality_var

    @builtins.property
    def perceptual_quality(self) -> typing.Optional[builtins.str]:
        '''The quality of derivative videos.

        High preserves video quality with reduced byte savings while low reduces video quality to increase byte savings.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#perceptual_quality DataAkamaiImagingPolicyVideo#perceptual_quality}
        '''
        result = self._values.get("perceptual_quality")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def perceptual_quality_var(self) -> typing.Optional[builtins.str]:
        '''The quality of derivative videos.

        High preserves video quality with reduced byte savings while low reduces video quality to increase byte savings.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#perceptual_quality_var DataAkamaiImagingPolicyVideo#perceptual_quality_var}
        '''
        result = self._values.get("perceptual_quality_var")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def placeholder_video_url(self) -> typing.Optional[builtins.str]:
        '''Allows you to add a specific placeholder video that appears when a user first requests a video, but before Image & Video Manager processes the video.

        If not specified the original video plays during the processing time.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#placeholder_video_url DataAkamaiImagingPolicyVideo#placeholder_video_url}
        '''
        result = self._values.get("placeholder_video_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def placeholder_video_url_var(self) -> typing.Optional[builtins.str]:
        '''Allows you to add a specific placeholder video that appears when a user first requests a video, but before Image & Video Manager processes the video.

        If not specified the original video plays during the processing time.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#placeholder_video_url_var DataAkamaiImagingPolicyVideo#placeholder_video_url_var}
        '''
        result = self._values.get("placeholder_video_url_var")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def video_adaptive_quality(self) -> typing.Optional[builtins.str]:
        '''Override the quality of video to serve when Image & Video Manager detects a slow connection.

        Specifying lower values lets users with slow connections browse your site with reduced load times without impacting the quality of videos for users with faster connections.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#video_adaptive_quality DataAkamaiImagingPolicyVideo#video_adaptive_quality}
        '''
        result = self._values.get("video_adaptive_quality")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def video_adaptive_quality_var(self) -> typing.Optional[builtins.str]:
        '''Override the quality of video to serve when Image & Video Manager detects a slow connection.

        Specifying lower values lets users with slow connections browse your site with reduced load times without impacting the quality of videos for users with faster connections.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#video_adaptive_quality_var DataAkamaiImagingPolicyVideo#video_adaptive_quality_var}
        '''
        result = self._values.get("video_adaptive_quality_var")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiImagingPolicyVideoPolicyOutput(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiImagingPolicyVideoPolicyOutputOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiImagingPolicyVideo.DataAkamaiImagingPolicyVideoPolicyOutputOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__49d61acc94b45f3c9eb7f9e092681a0201f4966fba2bf21093edfb7afdfaf3bf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPerceptualQuality")
    def reset_perceptual_quality(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPerceptualQuality", []))

    @jsii.member(jsii_name="resetPerceptualQualityVar")
    def reset_perceptual_quality_var(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPerceptualQualityVar", []))

    @jsii.member(jsii_name="resetPlaceholderVideoUrl")
    def reset_placeholder_video_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlaceholderVideoUrl", []))

    @jsii.member(jsii_name="resetPlaceholderVideoUrlVar")
    def reset_placeholder_video_url_var(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlaceholderVideoUrlVar", []))

    @jsii.member(jsii_name="resetVideoAdaptiveQuality")
    def reset_video_adaptive_quality(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVideoAdaptiveQuality", []))

    @jsii.member(jsii_name="resetVideoAdaptiveQualityVar")
    def reset_video_adaptive_quality_var(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVideoAdaptiveQualityVar", []))

    @builtins.property
    @jsii.member(jsii_name="perceptualQualityInput")
    def perceptual_quality_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "perceptualQualityInput"))

    @builtins.property
    @jsii.member(jsii_name="perceptualQualityVarInput")
    def perceptual_quality_var_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "perceptualQualityVarInput"))

    @builtins.property
    @jsii.member(jsii_name="placeholderVideoUrlInput")
    def placeholder_video_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "placeholderVideoUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="placeholderVideoUrlVarInput")
    def placeholder_video_url_var_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "placeholderVideoUrlVarInput"))

    @builtins.property
    @jsii.member(jsii_name="videoAdaptiveQualityInput")
    def video_adaptive_quality_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "videoAdaptiveQualityInput"))

    @builtins.property
    @jsii.member(jsii_name="videoAdaptiveQualityVarInput")
    def video_adaptive_quality_var_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "videoAdaptiveQualityVarInput"))

    @builtins.property
    @jsii.member(jsii_name="perceptualQuality")
    def perceptual_quality(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "perceptualQuality"))

    @perceptual_quality.setter
    def perceptual_quality(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ed413c1c42d4d637881d01e90628425b64574927a6813ae624b0cdc28401d07)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "perceptualQuality", value)

    @builtins.property
    @jsii.member(jsii_name="perceptualQualityVar")
    def perceptual_quality_var(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "perceptualQualityVar"))

    @perceptual_quality_var.setter
    def perceptual_quality_var(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1ba56ed033c0a0041c5a599d550a6afbd56ed0bd7e1c710f4e1e29d621d7e50)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "perceptualQualityVar", value)

    @builtins.property
    @jsii.member(jsii_name="placeholderVideoUrl")
    def placeholder_video_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "placeholderVideoUrl"))

    @placeholder_video_url.setter
    def placeholder_video_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1449fb17c3fb753d386483bf903806f1ef0ae98b460cbafd016dc5f842f0a14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "placeholderVideoUrl", value)

    @builtins.property
    @jsii.member(jsii_name="placeholderVideoUrlVar")
    def placeholder_video_url_var(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "placeholderVideoUrlVar"))

    @placeholder_video_url_var.setter
    def placeholder_video_url_var(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a96f42f08472708650360bbb332bb9f66705fe2aad97f4ed57a25cb84153caaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "placeholderVideoUrlVar", value)

    @builtins.property
    @jsii.member(jsii_name="videoAdaptiveQuality")
    def video_adaptive_quality(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "videoAdaptiveQuality"))

    @video_adaptive_quality.setter
    def video_adaptive_quality(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4b3d93f2238972c61e839a32791d3c1514521d42be673a067a68e11a630eabd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "videoAdaptiveQuality", value)

    @builtins.property
    @jsii.member(jsii_name="videoAdaptiveQualityVar")
    def video_adaptive_quality_var(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "videoAdaptiveQualityVar"))

    @video_adaptive_quality_var.setter
    def video_adaptive_quality_var(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39a34e91817e0c7b3bf9f25909cbc667c0c62b38f4dc2249a96b7a5516c4c1e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "videoAdaptiveQualityVar", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAkamaiImagingPolicyVideoPolicyOutput]:
        return typing.cast(typing.Optional[DataAkamaiImagingPolicyVideoPolicyOutput], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAkamaiImagingPolicyVideoPolicyOutput],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed988eaa0eb2daf19c8fbc90bc2931911368536ec07c368c68a8659391b76729)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiImagingPolicyVideoPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiImagingPolicyVideo.DataAkamaiImagingPolicyVideoPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__47c8161d48d36c5f5d93c57d0af4ebfee88385e164c7caccb307a34b8c477657)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBreakpoints")
    def put_breakpoints(
        self,
        *,
        widths: typing.Optional[typing.Sequence[jsii.Number]] = None,
    ) -> None:
        '''
        :param widths: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#widths DataAkamaiImagingPolicyVideo#widths}.
        '''
        value = DataAkamaiImagingPolicyVideoPolicyBreakpoints(widths=widths)

        return typing.cast(None, jsii.invoke(self, "putBreakpoints", [value]))

    @jsii.member(jsii_name="putOutput")
    def put_output(
        self,
        *,
        perceptual_quality: typing.Optional[builtins.str] = None,
        perceptual_quality_var: typing.Optional[builtins.str] = None,
        placeholder_video_url: typing.Optional[builtins.str] = None,
        placeholder_video_url_var: typing.Optional[builtins.str] = None,
        video_adaptive_quality: typing.Optional[builtins.str] = None,
        video_adaptive_quality_var: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param perceptual_quality: The quality of derivative videos. High preserves video quality with reduced byte savings while low reduces video quality to increase byte savings. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#perceptual_quality DataAkamaiImagingPolicyVideo#perceptual_quality}
        :param perceptual_quality_var: The quality of derivative videos. High preserves video quality with reduced byte savings while low reduces video quality to increase byte savings. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#perceptual_quality_var DataAkamaiImagingPolicyVideo#perceptual_quality_var}
        :param placeholder_video_url: Allows you to add a specific placeholder video that appears when a user first requests a video, but before Image & Video Manager processes the video. If not specified the original video plays during the processing time. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#placeholder_video_url DataAkamaiImagingPolicyVideo#placeholder_video_url}
        :param placeholder_video_url_var: Allows you to add a specific placeholder video that appears when a user first requests a video, but before Image & Video Manager processes the video. If not specified the original video plays during the processing time. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#placeholder_video_url_var DataAkamaiImagingPolicyVideo#placeholder_video_url_var}
        :param video_adaptive_quality: Override the quality of video to serve when Image & Video Manager detects a slow connection. Specifying lower values lets users with slow connections browse your site with reduced load times without impacting the quality of videos for users with faster connections. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#video_adaptive_quality DataAkamaiImagingPolicyVideo#video_adaptive_quality}
        :param video_adaptive_quality_var: Override the quality of video to serve when Image & Video Manager detects a slow connection. Specifying lower values lets users with slow connections browse your site with reduced load times without impacting the quality of videos for users with faster connections. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#video_adaptive_quality_var DataAkamaiImagingPolicyVideo#video_adaptive_quality_var}
        '''
        value = DataAkamaiImagingPolicyVideoPolicyOutput(
            perceptual_quality=perceptual_quality,
            perceptual_quality_var=perceptual_quality_var,
            placeholder_video_url=placeholder_video_url,
            placeholder_video_url_var=placeholder_video_url_var,
            video_adaptive_quality=video_adaptive_quality,
            video_adaptive_quality_var=video_adaptive_quality_var,
        )

        return typing.cast(None, jsii.invoke(self, "putOutput", [value]))

    @jsii.member(jsii_name="putVariables")
    def put_variables(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiImagingPolicyVideoPolicyVariables", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e69b9bc0622e6167eb8e5b4dbf24a81981339444737cd0016dc6fdc6664eb74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putVariables", [value]))

    @jsii.member(jsii_name="resetBreakpoints")
    def reset_breakpoints(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBreakpoints", []))

    @jsii.member(jsii_name="resetHosts")
    def reset_hosts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHosts", []))

    @jsii.member(jsii_name="resetOutput")
    def reset_output(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutput", []))

    @jsii.member(jsii_name="resetRolloutDuration")
    def reset_rollout_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRolloutDuration", []))

    @jsii.member(jsii_name="resetVariables")
    def reset_variables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVariables", []))

    @builtins.property
    @jsii.member(jsii_name="breakpoints")
    def breakpoints(
        self,
    ) -> DataAkamaiImagingPolicyVideoPolicyBreakpointsOutputReference:
        return typing.cast(DataAkamaiImagingPolicyVideoPolicyBreakpointsOutputReference, jsii.get(self, "breakpoints"))

    @builtins.property
    @jsii.member(jsii_name="output")
    def output(self) -> DataAkamaiImagingPolicyVideoPolicyOutputOutputReference:
        return typing.cast(DataAkamaiImagingPolicyVideoPolicyOutputOutputReference, jsii.get(self, "output"))

    @builtins.property
    @jsii.member(jsii_name="variables")
    def variables(self) -> "DataAkamaiImagingPolicyVideoPolicyVariablesList":
        return typing.cast("DataAkamaiImagingPolicyVideoPolicyVariablesList", jsii.get(self, "variables"))

    @builtins.property
    @jsii.member(jsii_name="breakpointsInput")
    def breakpoints_input(
        self,
    ) -> typing.Optional[DataAkamaiImagingPolicyVideoPolicyBreakpoints]:
        return typing.cast(typing.Optional[DataAkamaiImagingPolicyVideoPolicyBreakpoints], jsii.get(self, "breakpointsInput"))

    @builtins.property
    @jsii.member(jsii_name="hostsInput")
    def hosts_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "hostsInput"))

    @builtins.property
    @jsii.member(jsii_name="outputInput")
    def output_input(self) -> typing.Optional[DataAkamaiImagingPolicyVideoPolicyOutput]:
        return typing.cast(typing.Optional[DataAkamaiImagingPolicyVideoPolicyOutput], jsii.get(self, "outputInput"))

    @builtins.property
    @jsii.member(jsii_name="rolloutDurationInput")
    def rollout_duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rolloutDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="variablesInput")
    def variables_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiImagingPolicyVideoPolicyVariables"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiImagingPolicyVideoPolicyVariables"]]], jsii.get(self, "variablesInput"))

    @builtins.property
    @jsii.member(jsii_name="hosts")
    def hosts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "hosts"))

    @hosts.setter
    def hosts(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c523120d4f0360ef85e538d86b0ddd2ba6c87838c8fdb4fea7d7327b5522016)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hosts", value)

    @builtins.property
    @jsii.member(jsii_name="rolloutDuration")
    def rollout_duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rolloutDuration"))

    @rollout_duration.setter
    def rollout_duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__056d8efd531d663699dfc4537fbcad30f789154421823b2aa4839d6fb1f361a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rolloutDuration", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAkamaiImagingPolicyVideoPolicy]:
        return typing.cast(typing.Optional[DataAkamaiImagingPolicyVideoPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAkamaiImagingPolicyVideoPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5fb21cc9e68decda6bf5ee7864c9b6ee279d82aed6892faf86e00f813e4ee37)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiImagingPolicyVideo.DataAkamaiImagingPolicyVideoPolicyVariables",
    jsii_struct_bases=[],
    name_mapping={
        "default_value": "defaultValue",
        "name": "name",
        "type": "type",
        "enum_options": "enumOptions",
        "postfix": "postfix",
        "prefix": "prefix",
    },
)
class DataAkamaiImagingPolicyVideoPolicyVariables:
    def __init__(
        self,
        *,
        default_value: builtins.str,
        name: builtins.str,
        type: builtins.str,
        enum_options: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiImagingPolicyVideoPolicyVariablesEnumOptions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        postfix: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param default_value: The default value of the variable if no query parameter is provided. It needs to be one of the ``enumOptions`` if any are provided. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#default_value DataAkamaiImagingPolicyVideo#default_value}
        :param name: The name of the variable, also available as the query parameter name to set the variable's value dynamically. Use up to 50 alphanumeric characters. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#name DataAkamaiImagingPolicyVideo#name}
        :param type: The type of value for the variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#type DataAkamaiImagingPolicyVideo#type}
        :param enum_options: enum_options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#enum_options DataAkamaiImagingPolicyVideo#enum_options}
        :param postfix: A postfix added to the value provided for the variable, or to the default value. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#postfix DataAkamaiImagingPolicyVideo#postfix}
        :param prefix: A prefix added to the value provided for the variable, or to the default value. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#prefix DataAkamaiImagingPolicyVideo#prefix}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2dfa98011c1832067eee4bb4e36f75cac65c0c4e69a8487bed4e24b1bfacd4e)
            check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument enum_options", value=enum_options, expected_type=type_hints["enum_options"])
            check_type(argname="argument postfix", value=postfix, expected_type=type_hints["postfix"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "default_value": default_value,
            "name": name,
            "type": type,
        }
        if enum_options is not None:
            self._values["enum_options"] = enum_options
        if postfix is not None:
            self._values["postfix"] = postfix
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def default_value(self) -> builtins.str:
        '''The default value of the variable if no query parameter is provided.

        It needs to be one of the ``enumOptions`` if any are provided.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#default_value DataAkamaiImagingPolicyVideo#default_value}
        '''
        result = self._values.get("default_value")
        assert result is not None, "Required property 'default_value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the variable, also available as the query parameter name to set the variable's value dynamically.

        Use up to 50 alphanumeric characters.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#name DataAkamaiImagingPolicyVideo#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of value for the variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#type DataAkamaiImagingPolicyVideo#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enum_options(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiImagingPolicyVideoPolicyVariablesEnumOptions"]]]:
        '''enum_options block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#enum_options DataAkamaiImagingPolicyVideo#enum_options}
        '''
        result = self._values.get("enum_options")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiImagingPolicyVideoPolicyVariablesEnumOptions"]]], result)

    @builtins.property
    def postfix(self) -> typing.Optional[builtins.str]:
        '''A postfix added to the value provided for the variable, or to the default value.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#postfix DataAkamaiImagingPolicyVideo#postfix}
        '''
        result = self._values.get("postfix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''A prefix added to the value provided for the variable, or to the default value.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#prefix DataAkamaiImagingPolicyVideo#prefix}
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiImagingPolicyVideoPolicyVariables(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dataAkamaiImagingPolicyVideo.DataAkamaiImagingPolicyVideoPolicyVariablesEnumOptions",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "value": "value"},
)
class DataAkamaiImagingPolicyVideoPolicyVariablesEnumOptions:
    def __init__(self, *, id: builtins.str, value: builtins.str) -> None:
        '''
        :param id: The unique identifier for each enum value, up to 50 alphanumeric characters. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#id DataAkamaiImagingPolicyVideo#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param value: The value of the variable when the ``id`` is provided. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#value DataAkamaiImagingPolicyVideo#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d7108d0469593998bad0ec267d23b6d9496c200e6f3a62d2d6d470b9861fc8c)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
            "value": value,
        }

    @builtins.property
    def id(self) -> builtins.str:
        '''The unique identifier for each enum value, up to 50 alphanumeric characters.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#id DataAkamaiImagingPolicyVideo#id}

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''The value of the variable when the ``id`` is provided.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/imaging_policy_video#value DataAkamaiImagingPolicyVideo#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiImagingPolicyVideoPolicyVariablesEnumOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiImagingPolicyVideoPolicyVariablesEnumOptionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiImagingPolicyVideo.DataAkamaiImagingPolicyVideoPolicyVariablesEnumOptionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__852fbfa20a34cf0794e486f250bbb94078390358e22713f5978db82cf74b6dcf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiImagingPolicyVideoPolicyVariablesEnumOptionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f79168a7464d69ecdb81c585347da098b5197c972753898631b02b883d2bfac3)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiImagingPolicyVideoPolicyVariablesEnumOptionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ff16e83834e9abd8ec017faa262223dbcb6910911f9dda08a19fbd12e0afb1e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7ae8c4a783481eb8906f4102e55988bd10eb0131ddcbc9f928a1282298afcaad)
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
            type_hints = typing.get_type_hints(_typecheckingstub__95bdd0e069587dd00b00d26bbccc4784f5f7aba25e98e4de7bf4e2cd6b1355d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiImagingPolicyVideoPolicyVariablesEnumOptions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiImagingPolicyVideoPolicyVariablesEnumOptions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiImagingPolicyVideoPolicyVariablesEnumOptions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__942b6e90a023660b98ca40c0c93f225258bec57ef1fba28a176fe788135c55fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiImagingPolicyVideoPolicyVariablesEnumOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiImagingPolicyVideo.DataAkamaiImagingPolicyVideoPolicyVariablesEnumOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__91ee1957c0a6db7db0d15567e99e71044bc5244d29dc21775ce115fbf54ff06f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d6fad12a8a08fb81ab596eb3b7bb30a1253a7be78416ebdfc5b81e1e4079ccf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9e16e9d699d611f24d2660e3a71f8b70570544956dbe0c71bbaf5f5ae1383f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiImagingPolicyVideoPolicyVariablesEnumOptions]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiImagingPolicyVideoPolicyVariablesEnumOptions]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiImagingPolicyVideoPolicyVariablesEnumOptions]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c1790a3ca7fe2ae01680c42dcddd356f6c62bed9977b5bd31a26a9e61b4d8bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiImagingPolicyVideoPolicyVariablesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiImagingPolicyVideo.DataAkamaiImagingPolicyVideoPolicyVariablesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5e38ebb5682c867fc6fb40ce76326bad35f71e02962d7ff87078774ebea03387)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiImagingPolicyVideoPolicyVariablesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c24926e368d83b04001d82a6aac33b9a093d919ffbedc4f8aca7f71d83253e57)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiImagingPolicyVideoPolicyVariablesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0457df910ef3d53ac8ed66f061bc6a45a9270a212161ceb237e852dbb166ed5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__260cdf538fb3849cb60746e655fa6912a00beeb8626e8c41766dbbc9e3513513)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6464f76f605f64caff7cc44dbab8519b198c6ecf24661c2678ec33c75651fa67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiImagingPolicyVideoPolicyVariables]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiImagingPolicyVideoPolicyVariables]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiImagingPolicyVideoPolicyVariables]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__552968330bd6dddd832224f62656ff1f4a901e7eab85d6e552734201709b6510)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiImagingPolicyVideoPolicyVariablesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiImagingPolicyVideo.DataAkamaiImagingPolicyVideoPolicyVariablesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1017da595a4330b8debe2337b35bb24731f6d5574a8b4228c1d573d9121a6036)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putEnumOptions")
    def put_enum_options(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiImagingPolicyVideoPolicyVariablesEnumOptions, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86b495c7c1ca1c1ed0d7708ece8f115c83f0887e040819c81f7a5526682df521)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEnumOptions", [value]))

    @jsii.member(jsii_name="resetEnumOptions")
    def reset_enum_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnumOptions", []))

    @jsii.member(jsii_name="resetPostfix")
    def reset_postfix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPostfix", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="enumOptions")
    def enum_options(
        self,
    ) -> DataAkamaiImagingPolicyVideoPolicyVariablesEnumOptionsList:
        return typing.cast(DataAkamaiImagingPolicyVideoPolicyVariablesEnumOptionsList, jsii.get(self, "enumOptions"))

    @builtins.property
    @jsii.member(jsii_name="defaultValueInput")
    def default_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultValueInput"))

    @builtins.property
    @jsii.member(jsii_name="enumOptionsInput")
    def enum_options_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiImagingPolicyVideoPolicyVariablesEnumOptions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiImagingPolicyVideoPolicyVariablesEnumOptions]]], jsii.get(self, "enumOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="postfixInput")
    def postfix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "postfixInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultValue")
    def default_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultValue"))

    @default_value.setter
    def default_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0c2bb0329fe38aa2ad8846c871d6a1ab7d9847a66be7e5178277c0afa039a84)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultValue", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e0697c89ae42d6c94a349b19aab8e00e2a9ddb286f3b7240afdbad17e7c117a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="postfix")
    def postfix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "postfix"))

    @postfix.setter
    def postfix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13686a8c37abaeb1e720aab0e70e18ff6e0c6e34bb6b502613937121c356361e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "postfix", value)

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afb8ca8c6622fa34fefde14dc2b07152a016aebda641d51c9b86460a4a999518)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78e6c294719cb90d91471f9de6f94f046866d824d489740b0cd548e96b89d6b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiImagingPolicyVideoPolicyVariables]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiImagingPolicyVideoPolicyVariables]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiImagingPolicyVideoPolicyVariables]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85a8e98a9b8100436df5d1eb4cd3e76fb34bf250967e5dad0abbe2081313d539)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataAkamaiImagingPolicyVideo",
    "DataAkamaiImagingPolicyVideoConfig",
    "DataAkamaiImagingPolicyVideoPolicy",
    "DataAkamaiImagingPolicyVideoPolicyBreakpoints",
    "DataAkamaiImagingPolicyVideoPolicyBreakpointsOutputReference",
    "DataAkamaiImagingPolicyVideoPolicyOutput",
    "DataAkamaiImagingPolicyVideoPolicyOutputOutputReference",
    "DataAkamaiImagingPolicyVideoPolicyOutputReference",
    "DataAkamaiImagingPolicyVideoPolicyVariables",
    "DataAkamaiImagingPolicyVideoPolicyVariablesEnumOptions",
    "DataAkamaiImagingPolicyVideoPolicyVariablesEnumOptionsList",
    "DataAkamaiImagingPolicyVideoPolicyVariablesEnumOptionsOutputReference",
    "DataAkamaiImagingPolicyVideoPolicyVariablesList",
    "DataAkamaiImagingPolicyVideoPolicyVariablesOutputReference",
]

publication.publish()

def _typecheckingstub__9c96bfc5e8e884df10981289855d54a84dd83be22c43e2d8b621aebbc2abb56f(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    policy: typing.Union[DataAkamaiImagingPolicyVideoPolicy, typing.Dict[builtins.str, typing.Any]],
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

def _typecheckingstub__601d1fa6ec585593dd1bcdc8aeb7fdbbfa943cc4d2ab8358f8dcb5f745d5413a(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b776ef9fff804195cee6502364f97d3e0ac4ed464c75945d583d07e5a723b6d8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__906b4064a4d8d03e8df77f5b05a9805dfe935891929f5f1305d0d51f561cbc35(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    policy: typing.Union[DataAkamaiImagingPolicyVideoPolicy, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2b43843d81cf2cf5a86092588063a070a148f904f6b3579424a10966822aad5(
    *,
    breakpoints: typing.Optional[typing.Union[DataAkamaiImagingPolicyVideoPolicyBreakpoints, typing.Dict[builtins.str, typing.Any]]] = None,
    hosts: typing.Optional[typing.Sequence[builtins.str]] = None,
    output: typing.Optional[typing.Union[DataAkamaiImagingPolicyVideoPolicyOutput, typing.Dict[builtins.str, typing.Any]]] = None,
    rollout_duration: typing.Optional[builtins.str] = None,
    variables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiImagingPolicyVideoPolicyVariables, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cc9e503ea0e19d606d21c32d3457e49eb6e723bcc288d38e34284e33bc33c22(
    *,
    widths: typing.Optional[typing.Sequence[jsii.Number]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57f367e523c3e0e471cb8efa3b84ee9d94ffdee02648c7487f1e43b786731289(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3e4a8c47b70528e542996dcd18e1afcf4544d53ec7dcbd585488f723ee21975(
    value: typing.List[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9188ae8e442e8efe5855395b1642d5d8e184d1ac0c9bbcbad237b29a37ae3e0(
    value: typing.Optional[DataAkamaiImagingPolicyVideoPolicyBreakpoints],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e8324c05e97d278ccdaf690ed9edc349d902603467fe5f13e9f78e94d372eaa(
    *,
    perceptual_quality: typing.Optional[builtins.str] = None,
    perceptual_quality_var: typing.Optional[builtins.str] = None,
    placeholder_video_url: typing.Optional[builtins.str] = None,
    placeholder_video_url_var: typing.Optional[builtins.str] = None,
    video_adaptive_quality: typing.Optional[builtins.str] = None,
    video_adaptive_quality_var: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49d61acc94b45f3c9eb7f9e092681a0201f4966fba2bf21093edfb7afdfaf3bf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ed413c1c42d4d637881d01e90628425b64574927a6813ae624b0cdc28401d07(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1ba56ed033c0a0041c5a599d550a6afbd56ed0bd7e1c710f4e1e29d621d7e50(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1449fb17c3fb753d386483bf903806f1ef0ae98b460cbafd016dc5f842f0a14(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a96f42f08472708650360bbb332bb9f66705fe2aad97f4ed57a25cb84153caaf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4b3d93f2238972c61e839a32791d3c1514521d42be673a067a68e11a630eabd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39a34e91817e0c7b3bf9f25909cbc667c0c62b38f4dc2249a96b7a5516c4c1e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed988eaa0eb2daf19c8fbc90bc2931911368536ec07c368c68a8659391b76729(
    value: typing.Optional[DataAkamaiImagingPolicyVideoPolicyOutput],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47c8161d48d36c5f5d93c57d0af4ebfee88385e164c7caccb307a34b8c477657(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e69b9bc0622e6167eb8e5b4dbf24a81981339444737cd0016dc6fdc6664eb74(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiImagingPolicyVideoPolicyVariables, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c523120d4f0360ef85e538d86b0ddd2ba6c87838c8fdb4fea7d7327b5522016(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__056d8efd531d663699dfc4537fbcad30f789154421823b2aa4839d6fb1f361a4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5fb21cc9e68decda6bf5ee7864c9b6ee279d82aed6892faf86e00f813e4ee37(
    value: typing.Optional[DataAkamaiImagingPolicyVideoPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2dfa98011c1832067eee4bb4e36f75cac65c0c4e69a8487bed4e24b1bfacd4e(
    *,
    default_value: builtins.str,
    name: builtins.str,
    type: builtins.str,
    enum_options: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiImagingPolicyVideoPolicyVariablesEnumOptions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    postfix: typing.Optional[builtins.str] = None,
    prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d7108d0469593998bad0ec267d23b6d9496c200e6f3a62d2d6d470b9861fc8c(
    *,
    id: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__852fbfa20a34cf0794e486f250bbb94078390358e22713f5978db82cf74b6dcf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f79168a7464d69ecdb81c585347da098b5197c972753898631b02b883d2bfac3(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ff16e83834e9abd8ec017faa262223dbcb6910911f9dda08a19fbd12e0afb1e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ae8c4a783481eb8906f4102e55988bd10eb0131ddcbc9f928a1282298afcaad(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95bdd0e069587dd00b00d26bbccc4784f5f7aba25e98e4de7bf4e2cd6b1355d0(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__942b6e90a023660b98ca40c0c93f225258bec57ef1fba28a176fe788135c55fc(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiImagingPolicyVideoPolicyVariablesEnumOptions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91ee1957c0a6db7db0d15567e99e71044bc5244d29dc21775ce115fbf54ff06f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d6fad12a8a08fb81ab596eb3b7bb30a1253a7be78416ebdfc5b81e1e4079ccf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9e16e9d699d611f24d2660e3a71f8b70570544956dbe0c71bbaf5f5ae1383f5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c1790a3ca7fe2ae01680c42dcddd356f6c62bed9977b5bd31a26a9e61b4d8bb(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiImagingPolicyVideoPolicyVariablesEnumOptions]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e38ebb5682c867fc6fb40ce76326bad35f71e02962d7ff87078774ebea03387(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c24926e368d83b04001d82a6aac33b9a093d919ffbedc4f8aca7f71d83253e57(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0457df910ef3d53ac8ed66f061bc6a45a9270a212161ceb237e852dbb166ed5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__260cdf538fb3849cb60746e655fa6912a00beeb8626e8c41766dbbc9e3513513(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6464f76f605f64caff7cc44dbab8519b198c6ecf24661c2678ec33c75651fa67(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__552968330bd6dddd832224f62656ff1f4a901e7eab85d6e552734201709b6510(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiImagingPolicyVideoPolicyVariables]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1017da595a4330b8debe2337b35bb24731f6d5574a8b4228c1d573d9121a6036(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86b495c7c1ca1c1ed0d7708ece8f115c83f0887e040819c81f7a5526682df521(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiImagingPolicyVideoPolicyVariablesEnumOptions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0c2bb0329fe38aa2ad8846c871d6a1ab7d9847a66be7e5178277c0afa039a84(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e0697c89ae42d6c94a349b19aab8e00e2a9ddb286f3b7240afdbad17e7c117a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13686a8c37abaeb1e720aab0e70e18ff6e0c6e34bb6b502613937121c356361e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afb8ca8c6622fa34fefde14dc2b07152a016aebda641d51c9b86460a4a999518(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78e6c294719cb90d91471f9de6f94f046866d824d489740b0cd548e96b89d6b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85a8e98a9b8100436df5d1eb4cd3e76fb34bf250967e5dad0abbe2081313d539(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiImagingPolicyVideoPolicyVariables]],
) -> None:
    """Type checking stubs"""
    pass
