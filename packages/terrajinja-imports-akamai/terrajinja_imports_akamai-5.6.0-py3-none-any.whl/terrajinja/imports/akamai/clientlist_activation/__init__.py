'''
# `akamai_clientlist_activation`

Refer to the Terraform Registry for docs: [`akamai_clientlist_activation`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/clientlist_activation).
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


class ClientlistActivation(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.clientlistActivation.ClientlistActivation",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/clientlist_activation akamai_clientlist_activation}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        list_id: builtins.str,
        network: builtins.str,
        version: jsii.Number,
        comments: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        notification_recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
        siebel_ticket_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/clientlist_activation akamai_clientlist_activation} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param list_id: The client list unique identifier. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/clientlist_activation#list_id ClientlistActivation#list_id}
        :param network: The network environment where you activate your client list: either STAGING or PRODUCTION. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/clientlist_activation#network ClientlistActivation#network}
        :param version: The client list version. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/clientlist_activation#version ClientlistActivation#version}
        :param comments: A brief description for the activation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/clientlist_activation#comments ClientlistActivation#comments}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/clientlist_activation#id ClientlistActivation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param notification_recipients: Users to notify via email. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/clientlist_activation#notification_recipients ClientlistActivation#notification_recipients}
        :param siebel_ticket_id: Identifies the Siebel ticket, if the activation is linked to one. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/clientlist_activation#siebel_ticket_id ClientlistActivation#siebel_ticket_id}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7af88d59bda916db437e00d396449f60f8f785170df5d69235ecd3b3e935e5d1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ClientlistActivationConfig(
            list_id=list_id,
            network=network,
            version=version,
            comments=comments,
            id=id,
            notification_recipients=notification_recipients,
            siebel_ticket_id=siebel_ticket_id,
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
        '''Generates CDKTF code for importing a ClientlistActivation resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the ClientlistActivation to import.
        :param import_from_id: The id of the existing ClientlistActivation that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/clientlist_activation#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the ClientlistActivation to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a992c3d3e4af5577efa1aa2dc236f90cf06be686862f7807934973fa5d83349b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetComments")
    def reset_comments(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComments", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNotificationRecipients")
    def reset_notification_recipients(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationRecipients", []))

    @jsii.member(jsii_name="resetSiebelTicketId")
    def reset_siebel_ticket_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSiebelTicketId", []))

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
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="commentsInput")
    def comments_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="listIdInput")
    def list_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "listIdInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInput")
    def network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationRecipientsInput")
    def notification_recipients_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "notificationRecipientsInput"))

    @builtins.property
    @jsii.member(jsii_name="siebelTicketIdInput")
    def siebel_ticket_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "siebelTicketIdInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="comments")
    def comments(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comments"))

    @comments.setter
    def comments(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebc67d74f74a068e0e2abc587102e4aa431f3de83127cdeaae257aeca29de32d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comments", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a69617369fc897084e1a8d4ee129a0d0213699ff903fa58db949048f0f757ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="listId")
    def list_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "listId"))

    @list_id.setter
    def list_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fb440239cc8ad3a7cba68ad2220636157c163b5f1bed8dba2e315356cc22b0e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "listId", value)

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "network"))

    @network.setter
    def network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6793abceb96545704a53ec52f41d04dc7aed0af427f9b2c272314cb94e96551)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "network", value)

    @builtins.property
    @jsii.member(jsii_name="notificationRecipients")
    def notification_recipients(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "notificationRecipients"))

    @notification_recipients.setter
    def notification_recipients(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c765f76ae18cfce823132b6bfac72073c4c837fa6b889e3fc08d6df1549dcd24)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationRecipients", value)

    @builtins.property
    @jsii.member(jsii_name="siebelTicketId")
    def siebel_ticket_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "siebelTicketId"))

    @siebel_ticket_id.setter
    def siebel_ticket_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9e30f9ae444317a7ae3e5b6510c6d63bc283c2cf684434c0e35343940101b8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "siebelTicketId", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "version"))

    @version.setter
    def version(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a29cc035debc93d7e24d2653f9af7c83a7d926f18e96d3d492b858cebd0e8d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)


@jsii.data_type(
    jsii_type="akamai.clientlistActivation.ClientlistActivationConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "list_id": "listId",
        "network": "network",
        "version": "version",
        "comments": "comments",
        "id": "id",
        "notification_recipients": "notificationRecipients",
        "siebel_ticket_id": "siebelTicketId",
    },
)
class ClientlistActivationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        list_id: builtins.str,
        network: builtins.str,
        version: jsii.Number,
        comments: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        notification_recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
        siebel_ticket_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param list_id: The client list unique identifier. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/clientlist_activation#list_id ClientlistActivation#list_id}
        :param network: The network environment where you activate your client list: either STAGING or PRODUCTION. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/clientlist_activation#network ClientlistActivation#network}
        :param version: The client list version. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/clientlist_activation#version ClientlistActivation#version}
        :param comments: A brief description for the activation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/clientlist_activation#comments ClientlistActivation#comments}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/clientlist_activation#id ClientlistActivation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param notification_recipients: Users to notify via email. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/clientlist_activation#notification_recipients ClientlistActivation#notification_recipients}
        :param siebel_ticket_id: Identifies the Siebel ticket, if the activation is linked to one. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/clientlist_activation#siebel_ticket_id ClientlistActivation#siebel_ticket_id}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92c3ac855e325408a27e8f7176ab94d0c7d400d523dbf7803146cfdbc4c93834)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument list_id", value=list_id, expected_type=type_hints["list_id"])
            check_type(argname="argument network", value=network, expected_type=type_hints["network"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument comments", value=comments, expected_type=type_hints["comments"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument notification_recipients", value=notification_recipients, expected_type=type_hints["notification_recipients"])
            check_type(argname="argument siebel_ticket_id", value=siebel_ticket_id, expected_type=type_hints["siebel_ticket_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "list_id": list_id,
            "network": network,
            "version": version,
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
        if comments is not None:
            self._values["comments"] = comments
        if id is not None:
            self._values["id"] = id
        if notification_recipients is not None:
            self._values["notification_recipients"] = notification_recipients
        if siebel_ticket_id is not None:
            self._values["siebel_ticket_id"] = siebel_ticket_id

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
    def list_id(self) -> builtins.str:
        '''The client list unique identifier.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/clientlist_activation#list_id ClientlistActivation#list_id}
        '''
        result = self._values.get("list_id")
        assert result is not None, "Required property 'list_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network(self) -> builtins.str:
        '''The network environment where you activate your client list: either STAGING or PRODUCTION.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/clientlist_activation#network ClientlistActivation#network}
        '''
        result = self._values.get("network")
        assert result is not None, "Required property 'network' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> jsii.Number:
        '''The client list version.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/clientlist_activation#version ClientlistActivation#version}
        '''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def comments(self) -> typing.Optional[builtins.str]:
        '''A brief description for the activation.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/clientlist_activation#comments ClientlistActivation#comments}
        '''
        result = self._values.get("comments")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/clientlist_activation#id ClientlistActivation#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_recipients(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Users to notify via email.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/clientlist_activation#notification_recipients ClientlistActivation#notification_recipients}
        '''
        result = self._values.get("notification_recipients")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def siebel_ticket_id(self) -> typing.Optional[builtins.str]:
        '''Identifies the Siebel ticket, if the activation is linked to one.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/clientlist_activation#siebel_ticket_id ClientlistActivation#siebel_ticket_id}
        '''
        result = self._values.get("siebel_ticket_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClientlistActivationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ClientlistActivation",
    "ClientlistActivationConfig",
]

publication.publish()

def _typecheckingstub__7af88d59bda916db437e00d396449f60f8f785170df5d69235ecd3b3e935e5d1(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    list_id: builtins.str,
    network: builtins.str,
    version: jsii.Number,
    comments: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    notification_recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
    siebel_ticket_id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__a992c3d3e4af5577efa1aa2dc236f90cf06be686862f7807934973fa5d83349b(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebc67d74f74a068e0e2abc587102e4aa431f3de83127cdeaae257aeca29de32d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a69617369fc897084e1a8d4ee129a0d0213699ff903fa58db949048f0f757ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fb440239cc8ad3a7cba68ad2220636157c163b5f1bed8dba2e315356cc22b0e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6793abceb96545704a53ec52f41d04dc7aed0af427f9b2c272314cb94e96551(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c765f76ae18cfce823132b6bfac72073c4c837fa6b889e3fc08d6df1549dcd24(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9e30f9ae444317a7ae3e5b6510c6d63bc283c2cf684434c0e35343940101b8e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a29cc035debc93d7e24d2653f9af7c83a7d926f18e96d3d492b858cebd0e8d8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92c3ac855e325408a27e8f7176ab94d0c7d400d523dbf7803146cfdbc4c93834(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    list_id: builtins.str,
    network: builtins.str,
    version: jsii.Number,
    comments: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    notification_recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
    siebel_ticket_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
