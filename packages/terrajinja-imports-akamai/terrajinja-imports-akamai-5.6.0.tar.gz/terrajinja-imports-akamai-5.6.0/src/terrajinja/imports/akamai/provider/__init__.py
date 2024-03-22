'''
# `provider`

Refer to the Terraform Registry for docs: [`akamai`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs).
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


class AkamaiProvider(
    _cdktf_9a9027ec.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.provider.AkamaiProvider",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs akamai}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        alias: typing.Optional[builtins.str] = None,
        cache_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AkamaiProviderConfigA", typing.Dict[builtins.str, typing.Any]]]]] = None,
        config_section: typing.Optional[builtins.str] = None,
        edgerc: typing.Optional[builtins.str] = None,
        request_limit: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs akamai} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param alias: Alias name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs#alias AkamaiProvider#alias}
        :param cache_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs#cache_enabled AkamaiProvider#cache_enabled}.
        :param config: config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs#config AkamaiProvider#config}
        :param config_section: The section of the edgerc file to use for configuration. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs#config_section AkamaiProvider#config_section}
        :param edgerc: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs#edgerc AkamaiProvider#edgerc}.
        :param request_limit: The maximum number of API requests to be made per second (0 for no limit). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs#request_limit AkamaiProvider#request_limit}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdeee1a08ba037ce852825e69bc5f370743ef0fa4e3b132b6d8c247aaa075555)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config_ = AkamaiProviderConfig(
            alias=alias,
            cache_enabled=cache_enabled,
            config=config,
            config_section=config_section,
            edgerc=edgerc,
            request_limit=request_limit,
        )

        jsii.create(self.__class__, self, [scope, id, config_])

    @jsii.member(jsii_name="generateConfigForImport")
    @builtins.classmethod
    def generate_config_for_import(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        import_to_id: builtins.str,
        import_from_id: builtins.str,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    ) -> _cdktf_9a9027ec.ImportableResource:
        '''Generates CDKTF code for importing a AkamaiProvider resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the AkamaiProvider to import.
        :param import_from_id: The id of the existing AkamaiProvider that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the AkamaiProvider to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60488e9f18b4a196c532370cba7c44f9822c3ed6bddd625186074da6e6abd1c0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetCacheEnabled")
    def reset_cache_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheEnabled", []))

    @jsii.member(jsii_name="resetConfig")
    def reset_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfig", []))

    @jsii.member(jsii_name="resetConfigSection")
    def reset_config_section(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigSection", []))

    @jsii.member(jsii_name="resetEdgerc")
    def reset_edgerc(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEdgerc", []))

    @jsii.member(jsii_name="resetRequestLimit")
    def reset_request_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestLimit", []))

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
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheEnabledInput")
    def cache_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "cacheEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="configInput")
    def config_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AkamaiProviderConfigA"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AkamaiProviderConfigA"]]], jsii.get(self, "configInput"))

    @builtins.property
    @jsii.member(jsii_name="configSectionInput")
    def config_section_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configSectionInput"))

    @builtins.property
    @jsii.member(jsii_name="edgercInput")
    def edgerc_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "edgercInput"))

    @builtins.property
    @jsii.member(jsii_name="requestLimitInput")
    def request_limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "requestLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a08c23e7c2a6e63ed411164ef3b7484bef50803ce00cdcde635eae1a783f9d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="cacheEnabled")
    def cache_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "cacheEnabled"))

    @cache_enabled.setter
    def cache_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7afb69d47e0ed646cc53067c13001a81e990fb8ec0fb99fb7753ecf87390084)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="config")
    def config(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AkamaiProviderConfigA"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AkamaiProviderConfigA"]]], jsii.get(self, "config"))

    @config.setter
    def config(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AkamaiProviderConfigA"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d611c40ff2c3f0e75d1b025f9de19eaf8a97cf4d29d3b9f0ef75bbdfb67304a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "config", value)

    @builtins.property
    @jsii.member(jsii_name="configSection")
    def config_section(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configSection"))

    @config_section.setter
    def config_section(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb580b061cb872f61e0ae995a201d070bf087e987ee22f314e03f3f5ffeb69d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configSection", value)

    @builtins.property
    @jsii.member(jsii_name="edgerc")
    def edgerc(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "edgerc"))

    @edgerc.setter
    def edgerc(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b869b903fe91bcaeed9ad13a68532e2cdb17c1563c2741c941b8a4478ec9bde6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "edgerc", value)

    @builtins.property
    @jsii.member(jsii_name="requestLimit")
    def request_limit(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "requestLimit"))

    @request_limit.setter
    def request_limit(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48898fa6a6b3fef2ec7d3c7049133199c40bb0658ea298c225aa39d36fd0415e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestLimit", value)


@jsii.data_type(
    jsii_type="akamai.provider.AkamaiProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "alias": "alias",
        "cache_enabled": "cacheEnabled",
        "config": "config",
        "config_section": "configSection",
        "edgerc": "edgerc",
        "request_limit": "requestLimit",
    },
)
class AkamaiProviderConfig:
    def __init__(
        self,
        *,
        alias: typing.Optional[builtins.str] = None,
        cache_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AkamaiProviderConfigA", typing.Dict[builtins.str, typing.Any]]]]] = None,
        config_section: typing.Optional[builtins.str] = None,
        edgerc: typing.Optional[builtins.str] = None,
        request_limit: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param alias: Alias name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs#alias AkamaiProvider#alias}
        :param cache_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs#cache_enabled AkamaiProvider#cache_enabled}.
        :param config: config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs#config AkamaiProvider#config}
        :param config_section: The section of the edgerc file to use for configuration. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs#config_section AkamaiProvider#config_section}
        :param edgerc: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs#edgerc AkamaiProvider#edgerc}.
        :param request_limit: The maximum number of API requests to be made per second (0 for no limit). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs#request_limit AkamaiProvider#request_limit}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4421eaf909d5435777f5081fe6bcd8568ea2e9dc6d5b6bf670d2c519546cdda7)
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument cache_enabled", value=cache_enabled, expected_type=type_hints["cache_enabled"])
            check_type(argname="argument config", value=config, expected_type=type_hints["config"])
            check_type(argname="argument config_section", value=config_section, expected_type=type_hints["config_section"])
            check_type(argname="argument edgerc", value=edgerc, expected_type=type_hints["edgerc"])
            check_type(argname="argument request_limit", value=request_limit, expected_type=type_hints["request_limit"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if alias is not None:
            self._values["alias"] = alias
        if cache_enabled is not None:
            self._values["cache_enabled"] = cache_enabled
        if config is not None:
            self._values["config"] = config
        if config_section is not None:
            self._values["config_section"] = config_section
        if edgerc is not None:
            self._values["edgerc"] = edgerc
        if request_limit is not None:
            self._values["request_limit"] = request_limit

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs#alias AkamaiProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cache_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs#cache_enabled AkamaiProvider#cache_enabled}.'''
        result = self._values.get("cache_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def config(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AkamaiProviderConfigA"]]]:
        '''config block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs#config AkamaiProvider#config}
        '''
        result = self._values.get("config")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AkamaiProviderConfigA"]]], result)

    @builtins.property
    def config_section(self) -> typing.Optional[builtins.str]:
        '''The section of the edgerc file to use for configuration.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs#config_section AkamaiProvider#config_section}
        '''
        result = self._values.get("config_section")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def edgerc(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs#edgerc AkamaiProvider#edgerc}.'''
        result = self._values.get("edgerc")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_limit(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of API requests to be made per second (0 for no limit).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs#request_limit AkamaiProvider#request_limit}
        '''
        result = self._values.get("request_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AkamaiProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.provider.AkamaiProviderConfigA",
    jsii_struct_bases=[],
    name_mapping={
        "access_token": "accessToken",
        "client_secret": "clientSecret",
        "client_token": "clientToken",
        "host": "host",
        "account_key": "accountKey",
        "max_body": "maxBody",
    },
)
class AkamaiProviderConfigA:
    def __init__(
        self,
        *,
        access_token: builtins.str,
        client_secret: builtins.str,
        client_token: builtins.str,
        host: builtins.str,
        account_key: typing.Optional[builtins.str] = None,
        max_body: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param access_token: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs#access_token AkamaiProvider#access_token}.
        :param client_secret: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs#client_secret AkamaiProvider#client_secret}.
        :param client_token: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs#client_token AkamaiProvider#client_token}.
        :param host: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs#host AkamaiProvider#host}.
        :param account_key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs#account_key AkamaiProvider#account_key}.
        :param max_body: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs#max_body AkamaiProvider#max_body}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa862f584c0471659ae31c37e34b1dda60c0bffd038e24e5d89c3bfed4beb178)
            check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument client_token", value=client_token, expected_type=type_hints["client_token"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument account_key", value=account_key, expected_type=type_hints["account_key"])
            check_type(argname="argument max_body", value=max_body, expected_type=type_hints["max_body"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_token": access_token,
            "client_secret": client_secret,
            "client_token": client_token,
            "host": host,
        }
        if account_key is not None:
            self._values["account_key"] = account_key
        if max_body is not None:
            self._values["max_body"] = max_body

    @builtins.property
    def access_token(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs#access_token AkamaiProvider#access_token}.'''
        result = self._values.get("access_token")
        assert result is not None, "Required property 'access_token' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs#client_secret AkamaiProvider#client_secret}.'''
        result = self._values.get("client_secret")
        assert result is not None, "Required property 'client_secret' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_token(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs#client_token AkamaiProvider#client_token}.'''
        result = self._values.get("client_token")
        assert result is not None, "Required property 'client_token' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs#host AkamaiProvider#host}.'''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs#account_key AkamaiProvider#account_key}.'''
        result = self._values.get("account_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_body(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs#max_body AkamaiProvider#max_body}.'''
        result = self._values.get("max_body")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AkamaiProviderConfigA(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AkamaiProvider",
    "AkamaiProviderConfig",
    "AkamaiProviderConfigA",
]

publication.publish()

def _typecheckingstub__cdeee1a08ba037ce852825e69bc5f370743ef0fa4e3b132b6d8c247aaa075555(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    alias: typing.Optional[builtins.str] = None,
    cache_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AkamaiProviderConfigA, typing.Dict[builtins.str, typing.Any]]]]] = None,
    config_section: typing.Optional[builtins.str] = None,
    edgerc: typing.Optional[builtins.str] = None,
    request_limit: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60488e9f18b4a196c532370cba7c44f9822c3ed6bddd625186074da6e6abd1c0(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a08c23e7c2a6e63ed411164ef3b7484bef50803ce00cdcde635eae1a783f9d9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7afb69d47e0ed646cc53067c13001a81e990fb8ec0fb99fb7753ecf87390084(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d611c40ff2c3f0e75d1b025f9de19eaf8a97cf4d29d3b9f0ef75bbdfb67304a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AkamaiProviderConfigA]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb580b061cb872f61e0ae995a201d070bf087e987ee22f314e03f3f5ffeb69d8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b869b903fe91bcaeed9ad13a68532e2cdb17c1563c2741c941b8a4478ec9bde6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48898fa6a6b3fef2ec7d3c7049133199c40bb0658ea298c225aa39d36fd0415e(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4421eaf909d5435777f5081fe6bcd8568ea2e9dc6d5b6bf670d2c519546cdda7(
    *,
    alias: typing.Optional[builtins.str] = None,
    cache_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AkamaiProviderConfigA, typing.Dict[builtins.str, typing.Any]]]]] = None,
    config_section: typing.Optional[builtins.str] = None,
    edgerc: typing.Optional[builtins.str] = None,
    request_limit: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa862f584c0471659ae31c37e34b1dda60c0bffd038e24e5d89c3bfed4beb178(
    *,
    access_token: builtins.str,
    client_secret: builtins.str,
    client_token: builtins.str,
    host: builtins.str,
    account_key: typing.Optional[builtins.str] = None,
    max_body: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass
