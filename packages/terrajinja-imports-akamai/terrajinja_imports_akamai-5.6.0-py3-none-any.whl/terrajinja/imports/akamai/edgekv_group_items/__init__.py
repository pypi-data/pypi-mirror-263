'''
# `akamai_edgekv_group_items`

Refer to the Terraform Registry for docs: [`akamai_edgekv_group_items`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv_group_items).
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


class EdgekvGroupItems(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.edgekvGroupItems.EdgekvGroupItems",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv_group_items akamai_edgekv_group_items}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        group_name: builtins.str,
        items: typing.Mapping[builtins.str, builtins.str],
        namespace_name: builtins.str,
        network: builtins.str,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["EdgekvGroupItemsTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv_group_items akamai_edgekv_group_items} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param group_name: The name of the EdgeKV group. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv_group_items#group_name EdgekvGroupItems#group_name}
        :param items: A map of items within the specified group. Each item consists of an item key and a value. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv_group_items#items EdgekvGroupItems#items}
        :param namespace_name: The name for the EdgeKV namespace. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv_group_items#namespace_name EdgekvGroupItems#namespace_name}
        :param network: The network against which to execute the API request. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv_group_items#network EdgekvGroupItems#network}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv_group_items#id EdgekvGroupItems#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv_group_items#timeouts EdgekvGroupItems#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13d85b41295a5e4a74e1584af2c8a57d1b15f08badb5121eb23be7a15e96217b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = EdgekvGroupItemsConfig(
            group_name=group_name,
            items=items,
            namespace_name=namespace_name,
            network=network,
            id=id,
            timeouts=timeouts,
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
        '''Generates CDKTF code for importing a EdgekvGroupItems resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the EdgekvGroupItems to import.
        :param import_from_id: The id of the existing EdgekvGroupItems that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv_group_items#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the EdgekvGroupItems to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04d248e1a3aa6f76f999295092e857ed575d0ba30d5fcbea1c3baf72ff66e904)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self, *, default: typing.Optional[builtins.str] = None) -> None:
        '''
        :param default: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv_group_items#default EdgekvGroupItems#default}.
        '''
        value = EdgekvGroupItemsTimeouts(default=default)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

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
    def timeouts(self) -> "EdgekvGroupItemsTimeoutsOutputReference":
        return typing.cast("EdgekvGroupItemsTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="groupNameInput")
    def group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="itemsInput")
    def items_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "itemsInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceNameInput")
    def namespace_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInput")
    def network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(self) -> typing.Optional["EdgekvGroupItemsTimeouts"]:
        return typing.cast(typing.Optional["EdgekvGroupItemsTimeouts"], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="groupName")
    def group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupName"))

    @group_name.setter
    def group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c98a153a1ae3e5c191d22dc2f8e3acc9ba9ce222daf3a85557f3358ac8a47df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bee3d8f4ded4e1c2dce408d46cb7f7a9ecdd0c7a2b419336b694073669e60b14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="items")
    def items(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "items"))

    @items.setter
    def items(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eacb9b18ad6811ef782391587294bb0fd561d5df96d14f7329a102c043dbb5eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "items", value)

    @builtins.property
    @jsii.member(jsii_name="namespaceName")
    def namespace_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespaceName"))

    @namespace_name.setter
    def namespace_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7989fcc16ea3092da1ae47a82527aefe6af7f1abaa9a607183543dd6125cc3f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespaceName", value)

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "network"))

    @network.setter
    def network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__884c5b2211396de0023e093a194dd20f3832ffbf262e659f275b833e5d25ccf9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "network", value)


@jsii.data_type(
    jsii_type="akamai.edgekvGroupItems.EdgekvGroupItemsConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "group_name": "groupName",
        "items": "items",
        "namespace_name": "namespaceName",
        "network": "network",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class EdgekvGroupItemsConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        group_name: builtins.str,
        items: typing.Mapping[builtins.str, builtins.str],
        namespace_name: builtins.str,
        network: builtins.str,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["EdgekvGroupItemsTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param group_name: The name of the EdgeKV group. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv_group_items#group_name EdgekvGroupItems#group_name}
        :param items: A map of items within the specified group. Each item consists of an item key and a value. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv_group_items#items EdgekvGroupItems#items}
        :param namespace_name: The name for the EdgeKV namespace. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv_group_items#namespace_name EdgekvGroupItems#namespace_name}
        :param network: The network against which to execute the API request. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv_group_items#network EdgekvGroupItems#network}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv_group_items#id EdgekvGroupItems#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv_group_items#timeouts EdgekvGroupItems#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = EdgekvGroupItemsTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fafb02f6a5c250a1a1ca2f89c2a7d95775b0f503ed650f4293010aae6f055dc)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument group_name", value=group_name, expected_type=type_hints["group_name"])
            check_type(argname="argument items", value=items, expected_type=type_hints["items"])
            check_type(argname="argument namespace_name", value=namespace_name, expected_type=type_hints["namespace_name"])
            check_type(argname="argument network", value=network, expected_type=type_hints["network"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "group_name": group_name,
            "items": items,
            "namespace_name": namespace_name,
            "network": network,
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
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
    def group_name(self) -> builtins.str:
        '''The name of the EdgeKV group.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv_group_items#group_name EdgekvGroupItems#group_name}
        '''
        result = self._values.get("group_name")
        assert result is not None, "Required property 'group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def items(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''A map of items within the specified group. Each item consists of an item key and a value.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv_group_items#items EdgekvGroupItems#items}
        '''
        result = self._values.get("items")
        assert result is not None, "Required property 'items' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    @builtins.property
    def namespace_name(self) -> builtins.str:
        '''The name for the EdgeKV namespace.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv_group_items#namespace_name EdgekvGroupItems#namespace_name}
        '''
        result = self._values.get("namespace_name")
        assert result is not None, "Required property 'namespace_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network(self) -> builtins.str:
        '''The network against which to execute the API request.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv_group_items#network EdgekvGroupItems#network}
        '''
        result = self._values.get("network")
        assert result is not None, "Required property 'network' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv_group_items#id EdgekvGroupItems#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["EdgekvGroupItemsTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv_group_items#timeouts EdgekvGroupItems#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["EdgekvGroupItemsTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EdgekvGroupItemsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.edgekvGroupItems.EdgekvGroupItemsTimeouts",
    jsii_struct_bases=[],
    name_mapping={"default": "default"},
)
class EdgekvGroupItemsTimeouts:
    def __init__(self, *, default: typing.Optional[builtins.str] = None) -> None:
        '''
        :param default: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv_group_items#default EdgekvGroupItems#default}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18b21507ca4f8fabab46ad01cc3ce31542ec23cfb7f51334c854a25175e1414f)
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if default is not None:
            self._values["default"] = default

    @builtins.property
    def default(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/edgekv_group_items#default EdgekvGroupItems#default}.'''
        result = self._values.get("default")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EdgekvGroupItemsTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EdgekvGroupItemsTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.edgekvGroupItems.EdgekvGroupItemsTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fed501fa35df66340c2835f98b93af24af8d9dc18cc72b04a295f2a734fa3544)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ff2bd7f114bd79a4a59de43e1af39413170a7891994b1f04b89e6137e4eb10b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EdgekvGroupItemsTimeouts]:
        return typing.cast(typing.Optional[EdgekvGroupItemsTimeouts], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[EdgekvGroupItemsTimeouts]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f03aed7e56e75f097ecfc30834c4afd4b6ffd087c8c179ecc0a3e466a18b3945)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "EdgekvGroupItems",
    "EdgekvGroupItemsConfig",
    "EdgekvGroupItemsTimeouts",
    "EdgekvGroupItemsTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__13d85b41295a5e4a74e1584af2c8a57d1b15f08badb5121eb23be7a15e96217b(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    group_name: builtins.str,
    items: typing.Mapping[builtins.str, builtins.str],
    namespace_name: builtins.str,
    network: builtins.str,
    id: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[EdgekvGroupItemsTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__04d248e1a3aa6f76f999295092e857ed575d0ba30d5fcbea1c3baf72ff66e904(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c98a153a1ae3e5c191d22dc2f8e3acc9ba9ce222daf3a85557f3358ac8a47df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bee3d8f4ded4e1c2dce408d46cb7f7a9ecdd0c7a2b419336b694073669e60b14(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eacb9b18ad6811ef782391587294bb0fd561d5df96d14f7329a102c043dbb5eb(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7989fcc16ea3092da1ae47a82527aefe6af7f1abaa9a607183543dd6125cc3f0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__884c5b2211396de0023e093a194dd20f3832ffbf262e659f275b833e5d25ccf9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fafb02f6a5c250a1a1ca2f89c2a7d95775b0f503ed650f4293010aae6f055dc(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    group_name: builtins.str,
    items: typing.Mapping[builtins.str, builtins.str],
    namespace_name: builtins.str,
    network: builtins.str,
    id: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[EdgekvGroupItemsTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18b21507ca4f8fabab46ad01cc3ce31542ec23cfb7f51334c854a25175e1414f(
    *,
    default: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fed501fa35df66340c2835f98b93af24af8d9dc18cc72b04a295f2a734fa3544(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff2bd7f114bd79a4a59de43e1af39413170a7891994b1f04b89e6137e4eb10b9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f03aed7e56e75f097ecfc30834c4afd4b6ffd087c8c179ecc0a3e466a18b3945(
    value: typing.Optional[EdgekvGroupItemsTimeouts],
) -> None:
    """Type checking stubs"""
    pass
