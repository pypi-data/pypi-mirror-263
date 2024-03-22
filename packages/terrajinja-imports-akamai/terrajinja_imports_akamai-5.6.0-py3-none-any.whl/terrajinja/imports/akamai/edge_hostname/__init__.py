'''
# `akamai_edge_hostname`

Refer to the Terraform Registry for docs: [`akamai_edge_hostname`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname).
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


class EdgeHostname(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.edgeHostname.EdgeHostname",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname akamai_edge_hostname}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        contract_id: builtins.str,
        edge_hostname: builtins.str,
        group_id: builtins.str,
        ip_behavior: builtins.str,
        certificate: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        product_id: typing.Optional[builtins.str] = None,
        status_update_email: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["EdgeHostnameTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        use_cases: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname akamai_edge_hostname} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param contract_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname#contract_id EdgeHostname#contract_id}.
        :param edge_hostname: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname#edge_hostname EdgeHostname#edge_hostname}.
        :param group_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname#group_id EdgeHostname#group_id}.
        :param ip_behavior: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname#ip_behavior EdgeHostname#ip_behavior}.
        :param certificate: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname#certificate EdgeHostname#certificate}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname#id EdgeHostname#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param product_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname#product_id EdgeHostname#product_id}.
        :param status_update_email: Email address that should receive updates on the IP behavior update request. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname#status_update_email EdgeHostname#status_update_email}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname#timeouts EdgeHostname#timeouts}
        :param use_cases: A JSON encoded list of use cases. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname#use_cases EdgeHostname#use_cases}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b3079da19bf74f6bf9da744c95181b8f9a8d21019245a41af03e7e8d5c42f2c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = EdgeHostnameConfig(
            contract_id=contract_id,
            edge_hostname=edge_hostname,
            group_id=group_id,
            ip_behavior=ip_behavior,
            certificate=certificate,
            id=id,
            product_id=product_id,
            status_update_email=status_update_email,
            timeouts=timeouts,
            use_cases=use_cases,
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
        '''Generates CDKTF code for importing a EdgeHostname resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the EdgeHostname to import.
        :param import_from_id: The id of the existing EdgeHostname that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the EdgeHostname to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd48fe892230337ba11baf221a9dee829b09dac21671485043834dab67b53707)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self, *, default: typing.Optional[builtins.str] = None) -> None:
        '''
        :param default: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname#default EdgeHostname#default}.
        '''
        value = EdgeHostnameTimeouts(default=default)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCertificate")
    def reset_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificate", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetProductId")
    def reset_product_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProductId", []))

    @jsii.member(jsii_name="resetStatusUpdateEmail")
    def reset_status_update_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatusUpdateEmail", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetUseCases")
    def reset_use_cases(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseCases", []))

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
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "EdgeHostnameTimeoutsOutputReference":
        return typing.cast("EdgeHostnameTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="contractIdInput")
    def contract_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contractIdInput"))

    @builtins.property
    @jsii.member(jsii_name="edgeHostnameInput")
    def edge_hostname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "edgeHostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="groupIdInput")
    def group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ipBehaviorInput")
    def ip_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="productIdInput")
    def product_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "productIdInput"))

    @builtins.property
    @jsii.member(jsii_name="statusUpdateEmailInput")
    def status_update_email_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "statusUpdateEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(self) -> typing.Optional["EdgeHostnameTimeouts"]:
        return typing.cast(typing.Optional["EdgeHostnameTimeouts"], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="useCasesInput")
    def use_cases_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "useCasesInput"))

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b644460cd01aad5a34b1da8f584e5f4e0244376bf06b90148b7a160805cd1fda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificate", value)

    @builtins.property
    @jsii.member(jsii_name="contractId")
    def contract_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contractId"))

    @contract_id.setter
    def contract_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8b3532f563c2dc5769d2a691dec0186c1288052a1bb0974f52ac4eed5ce563a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contractId", value)

    @builtins.property
    @jsii.member(jsii_name="edgeHostname")
    def edge_hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "edgeHostname"))

    @edge_hostname.setter
    def edge_hostname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d489cef33bfea88d154f2694583375d0915e0338002205eef02f47e6f74f0c88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "edgeHostname", value)

    @builtins.property
    @jsii.member(jsii_name="groupId")
    def group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupId"))

    @group_id.setter
    def group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df145dfba82a9d72fedf2dfe5b74ee022aa3cd644e0e86a04e6afa1b330bbdbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b285a5d4251e6124948053b3cc69827d95be6a565fae3937cda6aa76e31b7948)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ipBehavior")
    def ip_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipBehavior"))

    @ip_behavior.setter
    def ip_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d3c640edaf22821492d32504d8ac73757e0741072792335aa6b8bf2451f682e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="productId")
    def product_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "productId"))

    @product_id.setter
    def product_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4b1dfc3f9ad838e23dc5728e2f2315033b3e522079a34536ebc173bbfcddffd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "productId", value)

    @builtins.property
    @jsii.member(jsii_name="statusUpdateEmail")
    def status_update_email(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "statusUpdateEmail"))

    @status_update_email.setter
    def status_update_email(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__377eea4fbeb562b032e1ef2dc7a3449ee90f05061b57332de185db31ff02fa03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statusUpdateEmail", value)

    @builtins.property
    @jsii.member(jsii_name="useCases")
    def use_cases(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "useCases"))

    @use_cases.setter
    def use_cases(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__821563456f0917e20db3223020285fcf4f6a342117cba972a0cbafa0a7beec13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useCases", value)


@jsii.data_type(
    jsii_type="akamai.edgeHostname.EdgeHostnameConfig",
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
        "edge_hostname": "edgeHostname",
        "group_id": "groupId",
        "ip_behavior": "ipBehavior",
        "certificate": "certificate",
        "id": "id",
        "product_id": "productId",
        "status_update_email": "statusUpdateEmail",
        "timeouts": "timeouts",
        "use_cases": "useCases",
    },
)
class EdgeHostnameConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        edge_hostname: builtins.str,
        group_id: builtins.str,
        ip_behavior: builtins.str,
        certificate: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        product_id: typing.Optional[builtins.str] = None,
        status_update_email: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["EdgeHostnameTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        use_cases: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param contract_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname#contract_id EdgeHostname#contract_id}.
        :param edge_hostname: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname#edge_hostname EdgeHostname#edge_hostname}.
        :param group_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname#group_id EdgeHostname#group_id}.
        :param ip_behavior: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname#ip_behavior EdgeHostname#ip_behavior}.
        :param certificate: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname#certificate EdgeHostname#certificate}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname#id EdgeHostname#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param product_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname#product_id EdgeHostname#product_id}.
        :param status_update_email: Email address that should receive updates on the IP behavior update request. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname#status_update_email EdgeHostname#status_update_email}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname#timeouts EdgeHostname#timeouts}
        :param use_cases: A JSON encoded list of use cases. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname#use_cases EdgeHostname#use_cases}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = EdgeHostnameTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__075d0f8b3b111998f52d96457e3bec6ab3f6f2d75a2b647e2357db8a57ac35ca)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument contract_id", value=contract_id, expected_type=type_hints["contract_id"])
            check_type(argname="argument edge_hostname", value=edge_hostname, expected_type=type_hints["edge_hostname"])
            check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
            check_type(argname="argument ip_behavior", value=ip_behavior, expected_type=type_hints["ip_behavior"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument product_id", value=product_id, expected_type=type_hints["product_id"])
            check_type(argname="argument status_update_email", value=status_update_email, expected_type=type_hints["status_update_email"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument use_cases", value=use_cases, expected_type=type_hints["use_cases"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "contract_id": contract_id,
            "edge_hostname": edge_hostname,
            "group_id": group_id,
            "ip_behavior": ip_behavior,
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
        if certificate is not None:
            self._values["certificate"] = certificate
        if id is not None:
            self._values["id"] = id
        if product_id is not None:
            self._values["product_id"] = product_id
        if status_update_email is not None:
            self._values["status_update_email"] = status_update_email
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if use_cases is not None:
            self._values["use_cases"] = use_cases

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
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname#contract_id EdgeHostname#contract_id}.'''
        result = self._values.get("contract_id")
        assert result is not None, "Required property 'contract_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def edge_hostname(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname#edge_hostname EdgeHostname#edge_hostname}.'''
        result = self._values.get("edge_hostname")
        assert result is not None, "Required property 'edge_hostname' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname#group_id EdgeHostname#group_id}.'''
        result = self._values.get("group_id")
        assert result is not None, "Required property 'group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ip_behavior(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname#ip_behavior EdgeHostname#ip_behavior}.'''
        result = self._values.get("ip_behavior")
        assert result is not None, "Required property 'ip_behavior' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname#certificate EdgeHostname#certificate}.'''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname#id EdgeHostname#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def product_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname#product_id EdgeHostname#product_id}.'''
        result = self._values.get("product_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status_update_email(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Email address that should receive updates on the IP behavior update request.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname#status_update_email EdgeHostname#status_update_email}
        '''
        result = self._values.get("status_update_email")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["EdgeHostnameTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname#timeouts EdgeHostname#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["EdgeHostnameTimeouts"], result)

    @builtins.property
    def use_cases(self) -> typing.Optional[builtins.str]:
        '''A JSON encoded list of use cases.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname#use_cases EdgeHostname#use_cases}
        '''
        result = self._values.get("use_cases")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EdgeHostnameConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.edgeHostname.EdgeHostnameTimeouts",
    jsii_struct_bases=[],
    name_mapping={"default": "default"},
)
class EdgeHostnameTimeouts:
    def __init__(self, *, default: typing.Optional[builtins.str] = None) -> None:
        '''
        :param default: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname#default EdgeHostname#default}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fa81c7187e99abcfaec360ba2e448eee8e7222dd56d4f5b6407ef5c398b8290)
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if default is not None:
            self._values["default"] = default

    @builtins.property
    def default(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edge_hostname#default EdgeHostname#default}.'''
        result = self._values.get("default")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EdgeHostnameTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EdgeHostnameTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.edgeHostname.EdgeHostnameTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8a3673314c5be0aed1681ad2ea92246ea6df78c90f67729a85b8cbdf83910de0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDefault")
    def reset_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefault", []))

    @builtins.property
    @jsii.member(jsii_name="defaultInput")
    def default_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultInput"))

    @builtins.property
    @jsii.member(jsii_name="default")
    def default(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "default"))

    @default.setter
    def default(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af0d33507f05f95044f3f4ea1a31a501b5ef4cc78380cc10e63fa912575e8146)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EdgeHostnameTimeouts]:
        return typing.cast(typing.Optional[EdgeHostnameTimeouts], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[EdgeHostnameTimeouts]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db3c1140341af8b07bae57b4535783351ee8baacacb0b87b60432c6e79ef9ed0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "EdgeHostname",
    "EdgeHostnameConfig",
    "EdgeHostnameTimeouts",
    "EdgeHostnameTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__6b3079da19bf74f6bf9da744c95181b8f9a8d21019245a41af03e7e8d5c42f2c(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    contract_id: builtins.str,
    edge_hostname: builtins.str,
    group_id: builtins.str,
    ip_behavior: builtins.str,
    certificate: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    product_id: typing.Optional[builtins.str] = None,
    status_update_email: typing.Optional[typing.Sequence[builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[EdgeHostnameTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    use_cases: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__fd48fe892230337ba11baf221a9dee829b09dac21671485043834dab67b53707(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b644460cd01aad5a34b1da8f584e5f4e0244376bf06b90148b7a160805cd1fda(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8b3532f563c2dc5769d2a691dec0186c1288052a1bb0974f52ac4eed5ce563a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d489cef33bfea88d154f2694583375d0915e0338002205eef02f47e6f74f0c88(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df145dfba82a9d72fedf2dfe5b74ee022aa3cd644e0e86a04e6afa1b330bbdbe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b285a5d4251e6124948053b3cc69827d95be6a565fae3937cda6aa76e31b7948(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d3c640edaf22821492d32504d8ac73757e0741072792335aa6b8bf2451f682e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4b1dfc3f9ad838e23dc5728e2f2315033b3e522079a34536ebc173bbfcddffd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__377eea4fbeb562b032e1ef2dc7a3449ee90f05061b57332de185db31ff02fa03(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__821563456f0917e20db3223020285fcf4f6a342117cba972a0cbafa0a7beec13(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__075d0f8b3b111998f52d96457e3bec6ab3f6f2d75a2b647e2357db8a57ac35ca(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    contract_id: builtins.str,
    edge_hostname: builtins.str,
    group_id: builtins.str,
    ip_behavior: builtins.str,
    certificate: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    product_id: typing.Optional[builtins.str] = None,
    status_update_email: typing.Optional[typing.Sequence[builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[EdgeHostnameTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    use_cases: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fa81c7187e99abcfaec360ba2e448eee8e7222dd56d4f5b6407ef5c398b8290(
    *,
    default: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a3673314c5be0aed1681ad2ea92246ea6df78c90f67729a85b8cbdf83910de0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af0d33507f05f95044f3f4ea1a31a501b5ef4cc78380cc10e63fa912575e8146(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db3c1140341af8b07bae57b4535783351ee8baacacb0b87b60432c6e79ef9ed0(
    value: typing.Optional[EdgeHostnameTimeouts],
) -> None:
    """Type checking stubs"""
    pass
