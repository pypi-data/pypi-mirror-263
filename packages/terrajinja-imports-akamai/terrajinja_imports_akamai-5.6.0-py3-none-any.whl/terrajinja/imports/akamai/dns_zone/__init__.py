'''
# `akamai_dns_zone`

Refer to the Terraform Registry for docs: [`akamai_dns_zone`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone).
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


class DnsZone(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dnsZone.DnsZone",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone akamai_dns_zone}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        contract: builtins.str,
        type: builtins.str,
        zone: builtins.str,
        comment: typing.Optional[builtins.str] = None,
        end_customer_id: typing.Optional[builtins.str] = None,
        group: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        masters: typing.Optional[typing.Sequence[builtins.str]] = None,
        sign_and_serve: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        sign_and_serve_algorithm: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
        tsig_key: typing.Optional[typing.Union["DnsZoneTsigKey", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone akamai_dns_zone} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param contract: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#contract DnsZone#contract}.
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#type DnsZone#type}.
        :param zone: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#zone DnsZone#zone}.
        :param comment: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#comment DnsZone#comment}.
        :param end_customer_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#end_customer_id DnsZone#end_customer_id}.
        :param group: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#group DnsZone#group}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#id DnsZone#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param masters: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#masters DnsZone#masters}.
        :param sign_and_serve: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#sign_and_serve DnsZone#sign_and_serve}.
        :param sign_and_serve_algorithm: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#sign_and_serve_algorithm DnsZone#sign_and_serve_algorithm}.
        :param target: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#target DnsZone#target}.
        :param tsig_key: tsig_key block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#tsig_key DnsZone#tsig_key}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__947812e90d9d1d6c1892c8d046147c7231cbf6b3728b50be6851c8f4128edb45)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DnsZoneConfig(
            contract=contract,
            type=type,
            zone=zone,
            comment=comment,
            end_customer_id=end_customer_id,
            group=group,
            id=id,
            masters=masters,
            sign_and_serve=sign_and_serve,
            sign_and_serve_algorithm=sign_and_serve_algorithm,
            target=target,
            tsig_key=tsig_key,
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
        '''Generates CDKTF code for importing a DnsZone resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the DnsZone to import.
        :param import_from_id: The id of the existing DnsZone that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the DnsZone to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__446ac9423b3dce52d0173a6c51adfe50c2f1d37fad6927dc921d7b01a679209c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putTsigKey")
    def put_tsig_key(
        self,
        *,
        algorithm: builtins.str,
        name: builtins.str,
        secret: builtins.str,
    ) -> None:
        '''
        :param algorithm: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#algorithm DnsZone#algorithm}.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#name DnsZone#name}.
        :param secret: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#secret DnsZone#secret}.
        '''
        value = DnsZoneTsigKey(algorithm=algorithm, name=name, secret=secret)

        return typing.cast(None, jsii.invoke(self, "putTsigKey", [value]))

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

    @jsii.member(jsii_name="resetEndCustomerId")
    def reset_end_customer_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndCustomerId", []))

    @jsii.member(jsii_name="resetGroup")
    def reset_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroup", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMasters")
    def reset_masters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasters", []))

    @jsii.member(jsii_name="resetSignAndServe")
    def reset_sign_and_serve(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSignAndServe", []))

    @jsii.member(jsii_name="resetSignAndServeAlgorithm")
    def reset_sign_and_serve_algorithm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSignAndServeAlgorithm", []))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @jsii.member(jsii_name="resetTsigKey")
    def reset_tsig_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTsigKey", []))

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
    @jsii.member(jsii_name="activationState")
    def activation_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "activationState"))

    @builtins.property
    @jsii.member(jsii_name="aliasCount")
    def alias_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "aliasCount"))

    @builtins.property
    @jsii.member(jsii_name="tsigKey")
    def tsig_key(self) -> "DnsZoneTsigKeyOutputReference":
        return typing.cast("DnsZoneTsigKeyOutputReference", jsii.get(self, "tsigKey"))

    @builtins.property
    @jsii.member(jsii_name="versionId")
    def version_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "versionId"))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="contractInput")
    def contract_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contractInput"))

    @builtins.property
    @jsii.member(jsii_name="endCustomerIdInput")
    def end_customer_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endCustomerIdInput"))

    @builtins.property
    @jsii.member(jsii_name="groupInput")
    def group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="mastersInput")
    def masters_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "mastersInput"))

    @builtins.property
    @jsii.member(jsii_name="signAndServeAlgorithmInput")
    def sign_and_serve_algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "signAndServeAlgorithmInput"))

    @builtins.property
    @jsii.member(jsii_name="signAndServeInput")
    def sign_and_serve_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "signAndServeInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="tsigKeyInput")
    def tsig_key_input(self) -> typing.Optional["DnsZoneTsigKey"]:
        return typing.cast(typing.Optional["DnsZoneTsigKey"], jsii.get(self, "tsigKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneInput")
    def zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneInput"))

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa64a5e94b3d9d2179e6135c5b465b8edd84a8b3e60fb6fc796742ac5f470d85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="contract")
    def contract(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contract"))

    @contract.setter
    def contract(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60f4d43270658810ee516178ddedc343605bfe6984cb07aafdd05375753e5550)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contract", value)

    @builtins.property
    @jsii.member(jsii_name="endCustomerId")
    def end_customer_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endCustomerId"))

    @end_customer_id.setter
    def end_customer_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__274f5fead510a0b4d6ca8e30fb4dc5e70242524f21db934d99e0e0fbcb11b44c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endCustomerId", value)

    @builtins.property
    @jsii.member(jsii_name="group")
    def group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "group"))

    @group.setter
    def group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a350e96f1ee8dcd81db178cab0d30c8cc83236d1667a387ff730930b47902ae9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "group", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b943674de364fff9c310d644a398311d722e2dff7c42625d0c7048ebe5d46841)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="masters")
    def masters(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "masters"))

    @masters.setter
    def masters(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aab50ae4b6f930170fb493b1cdfe66d7974b2d4ccc41de52cadc4caaa062d78a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masters", value)

    @builtins.property
    @jsii.member(jsii_name="signAndServe")
    def sign_and_serve(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "signAndServe"))

    @sign_and_serve.setter
    def sign_and_serve(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22ef1ad487612ee4bdf2b57cf86e37c09d0938be422e04c95aeb0f5709199f09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signAndServe", value)

    @builtins.property
    @jsii.member(jsii_name="signAndServeAlgorithm")
    def sign_and_serve_algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signAndServeAlgorithm"))

    @sign_and_serve_algorithm.setter
    def sign_and_serve_algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c4cffd6dc34fe21eced0b6f7ef0fe78ef9b66283ce24f2c79a55ae04b63e8c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signAndServeAlgorithm", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__600f772eb9b441e671236a1991eed5f5d6dd7c63615bd93a53b89a1c21201cc7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cf7490b6386b4f0c1a7f3cab2dbb755cecc74a78bec305ed262a17fc4eb5987)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="zone")
    def zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zone"))

    @zone.setter
    def zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b12106ddddc1110fb9bc8743df6d665b06200cb11f4b141d0dcb70f6eec742ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zone", value)


@jsii.data_type(
    jsii_type="akamai.dnsZone.DnsZoneConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "contract": "contract",
        "type": "type",
        "zone": "zone",
        "comment": "comment",
        "end_customer_id": "endCustomerId",
        "group": "group",
        "id": "id",
        "masters": "masters",
        "sign_and_serve": "signAndServe",
        "sign_and_serve_algorithm": "signAndServeAlgorithm",
        "target": "target",
        "tsig_key": "tsigKey",
    },
)
class DnsZoneConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        contract: builtins.str,
        type: builtins.str,
        zone: builtins.str,
        comment: typing.Optional[builtins.str] = None,
        end_customer_id: typing.Optional[builtins.str] = None,
        group: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        masters: typing.Optional[typing.Sequence[builtins.str]] = None,
        sign_and_serve: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        sign_and_serve_algorithm: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
        tsig_key: typing.Optional[typing.Union["DnsZoneTsigKey", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param contract: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#contract DnsZone#contract}.
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#type DnsZone#type}.
        :param zone: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#zone DnsZone#zone}.
        :param comment: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#comment DnsZone#comment}.
        :param end_customer_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#end_customer_id DnsZone#end_customer_id}.
        :param group: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#group DnsZone#group}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#id DnsZone#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param masters: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#masters DnsZone#masters}.
        :param sign_and_serve: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#sign_and_serve DnsZone#sign_and_serve}.
        :param sign_and_serve_algorithm: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#sign_and_serve_algorithm DnsZone#sign_and_serve_algorithm}.
        :param target: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#target DnsZone#target}.
        :param tsig_key: tsig_key block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#tsig_key DnsZone#tsig_key}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(tsig_key, dict):
            tsig_key = DnsZoneTsigKey(**tsig_key)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf38cb79739c948bb7ba1e44998459b26b1b7a03876b0e1a3b9bf6a047c3fdb8)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument contract", value=contract, expected_type=type_hints["contract"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument end_customer_id", value=end_customer_id, expected_type=type_hints["end_customer_id"])
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument masters", value=masters, expected_type=type_hints["masters"])
            check_type(argname="argument sign_and_serve", value=sign_and_serve, expected_type=type_hints["sign_and_serve"])
            check_type(argname="argument sign_and_serve_algorithm", value=sign_and_serve_algorithm, expected_type=type_hints["sign_and_serve_algorithm"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument tsig_key", value=tsig_key, expected_type=type_hints["tsig_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "contract": contract,
            "type": type,
            "zone": zone,
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
        if comment is not None:
            self._values["comment"] = comment
        if end_customer_id is not None:
            self._values["end_customer_id"] = end_customer_id
        if group is not None:
            self._values["group"] = group
        if id is not None:
            self._values["id"] = id
        if masters is not None:
            self._values["masters"] = masters
        if sign_and_serve is not None:
            self._values["sign_and_serve"] = sign_and_serve
        if sign_and_serve_algorithm is not None:
            self._values["sign_and_serve_algorithm"] = sign_and_serve_algorithm
        if target is not None:
            self._values["target"] = target
        if tsig_key is not None:
            self._values["tsig_key"] = tsig_key

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
    def contract(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#contract DnsZone#contract}.'''
        result = self._values.get("contract")
        assert result is not None, "Required property 'contract' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#type DnsZone#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def zone(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#zone DnsZone#zone}.'''
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#comment DnsZone#comment}.'''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def end_customer_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#end_customer_id DnsZone#end_customer_id}.'''
        result = self._values.get("end_customer_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def group(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#group DnsZone#group}.'''
        result = self._values.get("group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#id DnsZone#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def masters(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#masters DnsZone#masters}.'''
        result = self._values.get("masters")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def sign_and_serve(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#sign_and_serve DnsZone#sign_and_serve}.'''
        result = self._values.get("sign_and_serve")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def sign_and_serve_algorithm(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#sign_and_serve_algorithm DnsZone#sign_and_serve_algorithm}.'''
        result = self._values.get("sign_and_serve_algorithm")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#target DnsZone#target}.'''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tsig_key(self) -> typing.Optional["DnsZoneTsigKey"]:
        '''tsig_key block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#tsig_key DnsZone#tsig_key}
        '''
        result = self._values.get("tsig_key")
        return typing.cast(typing.Optional["DnsZoneTsigKey"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DnsZoneConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dnsZone.DnsZoneTsigKey",
    jsii_struct_bases=[],
    name_mapping={"algorithm": "algorithm", "name": "name", "secret": "secret"},
)
class DnsZoneTsigKey:
    def __init__(
        self,
        *,
        algorithm: builtins.str,
        name: builtins.str,
        secret: builtins.str,
    ) -> None:
        '''
        :param algorithm: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#algorithm DnsZone#algorithm}.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#name DnsZone#name}.
        :param secret: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#secret DnsZone#secret}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccc19e0564964ed83471b3cafad720c7791a74479f3c3856b4f2077e9947e68e)
            check_type(argname="argument algorithm", value=algorithm, expected_type=type_hints["algorithm"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument secret", value=secret, expected_type=type_hints["secret"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "algorithm": algorithm,
            "name": name,
            "secret": secret,
        }

    @builtins.property
    def algorithm(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#algorithm DnsZone#algorithm}.'''
        result = self._values.get("algorithm")
        assert result is not None, "Required property 'algorithm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#name DnsZone#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def secret(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_zone#secret DnsZone#secret}.'''
        result = self._values.get("secret")
        assert result is not None, "Required property 'secret' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DnsZoneTsigKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DnsZoneTsigKeyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dnsZone.DnsZoneTsigKeyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fc9344b2832b2936a282fe030bb66c1670d6391cfe8a0415c2569913d39a6034)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="algorithmInput")
    def algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "algorithmInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="secretInput")
    def secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretInput"))

    @builtins.property
    @jsii.member(jsii_name="algorithm")
    def algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "algorithm"))

    @algorithm.setter
    def algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46257f67893bc74e9bb391d7cf80b9f267f7c68e49a7531002db8bbecfaad4c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "algorithm", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__856e817f494949cb70ef3625606ab792a4c3c84f6cf56912644539b88836d347)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="secret")
    def secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secret"))

    @secret.setter
    def secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c736d5fae21c114ac695e6bb14236271167415409da0793959960d0befd50b4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secret", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DnsZoneTsigKey]:
        return typing.cast(typing.Optional[DnsZoneTsigKey], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DnsZoneTsigKey]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a51d811249f811f063d182a0b349a6ff1861a828d0f3f68dee07a860bedb97cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DnsZone",
    "DnsZoneConfig",
    "DnsZoneTsigKey",
    "DnsZoneTsigKeyOutputReference",
]

publication.publish()

def _typecheckingstub__947812e90d9d1d6c1892c8d046147c7231cbf6b3728b50be6851c8f4128edb45(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    contract: builtins.str,
    type: builtins.str,
    zone: builtins.str,
    comment: typing.Optional[builtins.str] = None,
    end_customer_id: typing.Optional[builtins.str] = None,
    group: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    masters: typing.Optional[typing.Sequence[builtins.str]] = None,
    sign_and_serve: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    sign_and_serve_algorithm: typing.Optional[builtins.str] = None,
    target: typing.Optional[builtins.str] = None,
    tsig_key: typing.Optional[typing.Union[DnsZoneTsigKey, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__446ac9423b3dce52d0173a6c51adfe50c2f1d37fad6927dc921d7b01a679209c(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa64a5e94b3d9d2179e6135c5b465b8edd84a8b3e60fb6fc796742ac5f470d85(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60f4d43270658810ee516178ddedc343605bfe6984cb07aafdd05375753e5550(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__274f5fead510a0b4d6ca8e30fb4dc5e70242524f21db934d99e0e0fbcb11b44c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a350e96f1ee8dcd81db178cab0d30c8cc83236d1667a387ff730930b47902ae9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b943674de364fff9c310d644a398311d722e2dff7c42625d0c7048ebe5d46841(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aab50ae4b6f930170fb493b1cdfe66d7974b2d4ccc41de52cadc4caaa062d78a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22ef1ad487612ee4bdf2b57cf86e37c09d0938be422e04c95aeb0f5709199f09(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c4cffd6dc34fe21eced0b6f7ef0fe78ef9b66283ce24f2c79a55ae04b63e8c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__600f772eb9b441e671236a1991eed5f5d6dd7c63615bd93a53b89a1c21201cc7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cf7490b6386b4f0c1a7f3cab2dbb755cecc74a78bec305ed262a17fc4eb5987(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b12106ddddc1110fb9bc8743df6d665b06200cb11f4b141d0dcb70f6eec742ac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf38cb79739c948bb7ba1e44998459b26b1b7a03876b0e1a3b9bf6a047c3fdb8(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    contract: builtins.str,
    type: builtins.str,
    zone: builtins.str,
    comment: typing.Optional[builtins.str] = None,
    end_customer_id: typing.Optional[builtins.str] = None,
    group: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    masters: typing.Optional[typing.Sequence[builtins.str]] = None,
    sign_and_serve: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    sign_and_serve_algorithm: typing.Optional[builtins.str] = None,
    target: typing.Optional[builtins.str] = None,
    tsig_key: typing.Optional[typing.Union[DnsZoneTsigKey, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccc19e0564964ed83471b3cafad720c7791a74479f3c3856b4f2077e9947e68e(
    *,
    algorithm: builtins.str,
    name: builtins.str,
    secret: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc9344b2832b2936a282fe030bb66c1670d6391cfe8a0415c2569913d39a6034(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46257f67893bc74e9bb391d7cf80b9f267f7c68e49a7531002db8bbecfaad4c1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__856e817f494949cb70ef3625606ab792a4c3c84f6cf56912644539b88836d347(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c736d5fae21c114ac695e6bb14236271167415409da0793959960d0befd50b4e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a51d811249f811f063d182a0b349a6ff1861a828d0f3f68dee07a860bedb97cf(
    value: typing.Optional[DnsZoneTsigKey],
) -> None:
    """Type checking stubs"""
    pass
