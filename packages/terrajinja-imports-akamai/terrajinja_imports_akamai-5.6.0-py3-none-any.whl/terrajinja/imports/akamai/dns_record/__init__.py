'''
# `akamai_dns_record`

Refer to the Terraform Registry for docs: [`akamai_dns_record`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record).
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


class DnsRecord(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dnsRecord.DnsRecord",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record akamai_dns_record}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        recordtype: builtins.str,
        ttl: jsii.Number,
        zone: builtins.str,
        active: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        algorithm: typing.Optional[jsii.Number] = None,
        certificate: typing.Optional[builtins.str] = None,
        digest: typing.Optional[builtins.str] = None,
        digest_type: typing.Optional[jsii.Number] = None,
        email_address: typing.Optional[builtins.str] = None,
        expiration: typing.Optional[builtins.str] = None,
        expiry: typing.Optional[jsii.Number] = None,
        fingerprint: typing.Optional[builtins.str] = None,
        fingerprint_type: typing.Optional[jsii.Number] = None,
        flags: typing.Optional[jsii.Number] = None,
        flagsnaptr: typing.Optional[builtins.str] = None,
        hardware: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        inception: typing.Optional[builtins.str] = None,
        iterations: typing.Optional[jsii.Number] = None,
        key: typing.Optional[builtins.str] = None,
        keytag: typing.Optional[jsii.Number] = None,
        labels: typing.Optional[jsii.Number] = None,
        mailbox: typing.Optional[builtins.str] = None,
        match_type: typing.Optional[jsii.Number] = None,
        name_server: typing.Optional[builtins.str] = None,
        next_hashed_owner_name: typing.Optional[builtins.str] = None,
        nxdomain_ttl: typing.Optional[jsii.Number] = None,
        order: typing.Optional[jsii.Number] = None,
        original_ttl: typing.Optional[jsii.Number] = None,
        port: typing.Optional[jsii.Number] = None,
        preference: typing.Optional[jsii.Number] = None,
        priority: typing.Optional[jsii.Number] = None,
        priority_increment: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional[jsii.Number] = None,
        refresh: typing.Optional[jsii.Number] = None,
        regexp: typing.Optional[builtins.str] = None,
        replacement: typing.Optional[builtins.str] = None,
        retry: typing.Optional[jsii.Number] = None,
        salt: typing.Optional[builtins.str] = None,
        selector: typing.Optional[jsii.Number] = None,
        service: typing.Optional[builtins.str] = None,
        signature: typing.Optional[builtins.str] = None,
        signer: typing.Optional[builtins.str] = None,
        software_attribute: typing.Optional[builtins.str] = None,
        subtype: typing.Optional[jsii.Number] = None,
        svc_params: typing.Optional[builtins.str] = None,
        svc_priority: typing.Optional[jsii.Number] = None,
        target: typing.Optional[typing.Sequence[builtins.str]] = None,
        target_name: typing.Optional[builtins.str] = None,
        txt: typing.Optional[builtins.str] = None,
        type_bitmaps: typing.Optional[builtins.str] = None,
        type_covered: typing.Optional[builtins.str] = None,
        type_mnemonic: typing.Optional[builtins.str] = None,
        type_value: typing.Optional[jsii.Number] = None,
        usage: typing.Optional[jsii.Number] = None,
        weight: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record akamai_dns_record} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#name DnsRecord#name}.
        :param recordtype: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#recordtype DnsRecord#recordtype}.
        :param ttl: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#ttl DnsRecord#ttl}.
        :param zone: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#zone DnsRecord#zone}.
        :param active: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#active DnsRecord#active}.
        :param algorithm: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#algorithm DnsRecord#algorithm}.
        :param certificate: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#certificate DnsRecord#certificate}.
        :param digest: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#digest DnsRecord#digest}.
        :param digest_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#digest_type DnsRecord#digest_type}.
        :param email_address: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#email_address DnsRecord#email_address}.
        :param expiration: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#expiration DnsRecord#expiration}.
        :param expiry: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#expiry DnsRecord#expiry}.
        :param fingerprint: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#fingerprint DnsRecord#fingerprint}.
        :param fingerprint_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#fingerprint_type DnsRecord#fingerprint_type}.
        :param flags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#flags DnsRecord#flags}.
        :param flagsnaptr: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#flagsnaptr DnsRecord#flagsnaptr}.
        :param hardware: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#hardware DnsRecord#hardware}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#id DnsRecord#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param inception: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#inception DnsRecord#inception}.
        :param iterations: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#iterations DnsRecord#iterations}.
        :param key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#key DnsRecord#key}.
        :param keytag: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#keytag DnsRecord#keytag}.
        :param labels: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#labels DnsRecord#labels}.
        :param mailbox: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#mailbox DnsRecord#mailbox}.
        :param match_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#match_type DnsRecord#match_type}.
        :param name_server: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#name_server DnsRecord#name_server}.
        :param next_hashed_owner_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#next_hashed_owner_name DnsRecord#next_hashed_owner_name}.
        :param nxdomain_ttl: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#nxdomain_ttl DnsRecord#nxdomain_ttl}.
        :param order: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#order DnsRecord#order}.
        :param original_ttl: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#original_ttl DnsRecord#original_ttl}.
        :param port: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#port DnsRecord#port}.
        :param preference: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#preference DnsRecord#preference}.
        :param priority: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#priority DnsRecord#priority}.
        :param priority_increment: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#priority_increment DnsRecord#priority_increment}.
        :param protocol: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#protocol DnsRecord#protocol}.
        :param refresh: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#refresh DnsRecord#refresh}.
        :param regexp: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#regexp DnsRecord#regexp}.
        :param replacement: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#replacement DnsRecord#replacement}.
        :param retry: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#retry DnsRecord#retry}.
        :param salt: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#salt DnsRecord#salt}.
        :param selector: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#selector DnsRecord#selector}.
        :param service: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#service DnsRecord#service}.
        :param signature: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#signature DnsRecord#signature}.
        :param signer: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#signer DnsRecord#signer}.
        :param software_attribute: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#software DnsRecord#software}.
        :param subtype: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#subtype DnsRecord#subtype}.
        :param svc_params: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#svc_params DnsRecord#svc_params}.
        :param svc_priority: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#svc_priority DnsRecord#svc_priority}.
        :param target: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#target DnsRecord#target}.
        :param target_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#target_name DnsRecord#target_name}.
        :param txt: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#txt DnsRecord#txt}.
        :param type_bitmaps: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#type_bitmaps DnsRecord#type_bitmaps}.
        :param type_covered: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#type_covered DnsRecord#type_covered}.
        :param type_mnemonic: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#type_mnemonic DnsRecord#type_mnemonic}.
        :param type_value: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#type_value DnsRecord#type_value}.
        :param usage: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#usage DnsRecord#usage}.
        :param weight: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#weight DnsRecord#weight}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e64539b4bd69d8ac100173b1efebca8d321920cf3ddd8188e73ceeaab1321cab)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DnsRecordConfig(
            name=name,
            recordtype=recordtype,
            ttl=ttl,
            zone=zone,
            active=active,
            algorithm=algorithm,
            certificate=certificate,
            digest=digest,
            digest_type=digest_type,
            email_address=email_address,
            expiration=expiration,
            expiry=expiry,
            fingerprint=fingerprint,
            fingerprint_type=fingerprint_type,
            flags=flags,
            flagsnaptr=flagsnaptr,
            hardware=hardware,
            id=id,
            inception=inception,
            iterations=iterations,
            key=key,
            keytag=keytag,
            labels=labels,
            mailbox=mailbox,
            match_type=match_type,
            name_server=name_server,
            next_hashed_owner_name=next_hashed_owner_name,
            nxdomain_ttl=nxdomain_ttl,
            order=order,
            original_ttl=original_ttl,
            port=port,
            preference=preference,
            priority=priority,
            priority_increment=priority_increment,
            protocol=protocol,
            refresh=refresh,
            regexp=regexp,
            replacement=replacement,
            retry=retry,
            salt=salt,
            selector=selector,
            service=service,
            signature=signature,
            signer=signer,
            software_attribute=software_attribute,
            subtype=subtype,
            svc_params=svc_params,
            svc_priority=svc_priority,
            target=target,
            target_name=target_name,
            txt=txt,
            type_bitmaps=type_bitmaps,
            type_covered=type_covered,
            type_mnemonic=type_mnemonic,
            type_value=type_value,
            usage=usage,
            weight=weight,
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
        '''Generates CDKTF code for importing a DnsRecord resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the DnsRecord to import.
        :param import_from_id: The id of the existing DnsRecord that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the DnsRecord to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95a781ec517f5e040563a01e2a2caff0a4b36a0a091610e8ebc2354749b9db17)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetActive")
    def reset_active(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActive", []))

    @jsii.member(jsii_name="resetAlgorithm")
    def reset_algorithm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlgorithm", []))

    @jsii.member(jsii_name="resetCertificate")
    def reset_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificate", []))

    @jsii.member(jsii_name="resetDigest")
    def reset_digest(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDigest", []))

    @jsii.member(jsii_name="resetDigestType")
    def reset_digest_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDigestType", []))

    @jsii.member(jsii_name="resetEmailAddress")
    def reset_email_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailAddress", []))

    @jsii.member(jsii_name="resetExpiration")
    def reset_expiration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpiration", []))

    @jsii.member(jsii_name="resetExpiry")
    def reset_expiry(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpiry", []))

    @jsii.member(jsii_name="resetFingerprint")
    def reset_fingerprint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFingerprint", []))

    @jsii.member(jsii_name="resetFingerprintType")
    def reset_fingerprint_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFingerprintType", []))

    @jsii.member(jsii_name="resetFlags")
    def reset_flags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFlags", []))

    @jsii.member(jsii_name="resetFlagsnaptr")
    def reset_flagsnaptr(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFlagsnaptr", []))

    @jsii.member(jsii_name="resetHardware")
    def reset_hardware(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHardware", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInception")
    def reset_inception(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInception", []))

    @jsii.member(jsii_name="resetIterations")
    def reset_iterations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIterations", []))

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetKeytag")
    def reset_keytag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeytag", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetMailbox")
    def reset_mailbox(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMailbox", []))

    @jsii.member(jsii_name="resetMatchType")
    def reset_match_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchType", []))

    @jsii.member(jsii_name="resetNameServer")
    def reset_name_server(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNameServer", []))

    @jsii.member(jsii_name="resetNextHashedOwnerName")
    def reset_next_hashed_owner_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNextHashedOwnerName", []))

    @jsii.member(jsii_name="resetNxdomainTtl")
    def reset_nxdomain_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNxdomainTtl", []))

    @jsii.member(jsii_name="resetOrder")
    def reset_order(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrder", []))

    @jsii.member(jsii_name="resetOriginalTtl")
    def reset_original_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOriginalTtl", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetPreference")
    def reset_preference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreference", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetPriorityIncrement")
    def reset_priority_increment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriorityIncrement", []))

    @jsii.member(jsii_name="resetProtocol")
    def reset_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocol", []))

    @jsii.member(jsii_name="resetRefresh")
    def reset_refresh(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRefresh", []))

    @jsii.member(jsii_name="resetRegexp")
    def reset_regexp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegexp", []))

    @jsii.member(jsii_name="resetReplacement")
    def reset_replacement(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplacement", []))

    @jsii.member(jsii_name="resetRetry")
    def reset_retry(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetry", []))

    @jsii.member(jsii_name="resetSalt")
    def reset_salt(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSalt", []))

    @jsii.member(jsii_name="resetSelector")
    def reset_selector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSelector", []))

    @jsii.member(jsii_name="resetService")
    def reset_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetService", []))

    @jsii.member(jsii_name="resetSignature")
    def reset_signature(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSignature", []))

    @jsii.member(jsii_name="resetSigner")
    def reset_signer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSigner", []))

    @jsii.member(jsii_name="resetSoftwareAttribute")
    def reset_software_attribute(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSoftwareAttribute", []))

    @jsii.member(jsii_name="resetSubtype")
    def reset_subtype(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubtype", []))

    @jsii.member(jsii_name="resetSvcParams")
    def reset_svc_params(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSvcParams", []))

    @jsii.member(jsii_name="resetSvcPriority")
    def reset_svc_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSvcPriority", []))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @jsii.member(jsii_name="resetTargetName")
    def reset_target_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetName", []))

    @jsii.member(jsii_name="resetTxt")
    def reset_txt(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTxt", []))

    @jsii.member(jsii_name="resetTypeBitmaps")
    def reset_type_bitmaps(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTypeBitmaps", []))

    @jsii.member(jsii_name="resetTypeCovered")
    def reset_type_covered(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTypeCovered", []))

    @jsii.member(jsii_name="resetTypeMnemonic")
    def reset_type_mnemonic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTypeMnemonic", []))

    @jsii.member(jsii_name="resetTypeValue")
    def reset_type_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTypeValue", []))

    @jsii.member(jsii_name="resetUsage")
    def reset_usage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsage", []))

    @jsii.member(jsii_name="resetWeight")
    def reset_weight(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeight", []))

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
    @jsii.member(jsii_name="answerType")
    def answer_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "answerType"))

    @builtins.property
    @jsii.member(jsii_name="dnsName")
    def dns_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dnsName"))

    @builtins.property
    @jsii.member(jsii_name="recordSha")
    def record_sha(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordSha"))

    @builtins.property
    @jsii.member(jsii_name="serial")
    def serial(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "serial"))

    @builtins.property
    @jsii.member(jsii_name="activeInput")
    def active_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "activeInput"))

    @builtins.property
    @jsii.member(jsii_name="algorithmInput")
    def algorithm_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "algorithmInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="digestInput")
    def digest_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "digestInput"))

    @builtins.property
    @jsii.member(jsii_name="digestTypeInput")
    def digest_type_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "digestTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="emailAddressInput")
    def email_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="expirationInput")
    def expiration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expirationInput"))

    @builtins.property
    @jsii.member(jsii_name="expiryInput")
    def expiry_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "expiryInput"))

    @builtins.property
    @jsii.member(jsii_name="fingerprintInput")
    def fingerprint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fingerprintInput"))

    @builtins.property
    @jsii.member(jsii_name="fingerprintTypeInput")
    def fingerprint_type_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "fingerprintTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="flagsInput")
    def flags_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "flagsInput"))

    @builtins.property
    @jsii.member(jsii_name="flagsnaptrInput")
    def flagsnaptr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "flagsnaptrInput"))

    @builtins.property
    @jsii.member(jsii_name="hardwareInput")
    def hardware_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hardwareInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="inceptionInput")
    def inception_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inceptionInput"))

    @builtins.property
    @jsii.member(jsii_name="iterationsInput")
    def iterations_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "iterationsInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="keytagInput")
    def keytag_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "keytagInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="mailboxInput")
    def mailbox_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mailboxInput"))

    @builtins.property
    @jsii.member(jsii_name="matchTypeInput")
    def match_type_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "matchTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="nameServerInput")
    def name_server_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameServerInput"))

    @builtins.property
    @jsii.member(jsii_name="nextHashedOwnerNameInput")
    def next_hashed_owner_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nextHashedOwnerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="nxdomainTtlInput")
    def nxdomain_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nxdomainTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="orderInput")
    def order_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "orderInput"))

    @builtins.property
    @jsii.member(jsii_name="originalTtlInput")
    def original_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "originalTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="preferenceInput")
    def preference_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "preferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityIncrementInput")
    def priority_increment_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityIncrementInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="recordtypeInput")
    def recordtype_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recordtypeInput"))

    @builtins.property
    @jsii.member(jsii_name="refreshInput")
    def refresh_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "refreshInput"))

    @builtins.property
    @jsii.member(jsii_name="regexpInput")
    def regexp_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regexpInput"))

    @builtins.property
    @jsii.member(jsii_name="replacementInput")
    def replacement_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replacementInput"))

    @builtins.property
    @jsii.member(jsii_name="retryInput")
    def retry_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retryInput"))

    @builtins.property
    @jsii.member(jsii_name="saltInput")
    def salt_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "saltInput"))

    @builtins.property
    @jsii.member(jsii_name="selectorInput")
    def selector_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "selectorInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="signatureInput")
    def signature_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "signatureInput"))

    @builtins.property
    @jsii.member(jsii_name="signerInput")
    def signer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "signerInput"))

    @builtins.property
    @jsii.member(jsii_name="softwareAttributeInput")
    def software_attribute_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "softwareAttributeInput"))

    @builtins.property
    @jsii.member(jsii_name="subtypeInput")
    def subtype_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "subtypeInput"))

    @builtins.property
    @jsii.member(jsii_name="svcParamsInput")
    def svc_params_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "svcParamsInput"))

    @builtins.property
    @jsii.member(jsii_name="svcPriorityInput")
    def svc_priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "svcPriorityInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="targetNameInput")
    def target_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetNameInput"))

    @builtins.property
    @jsii.member(jsii_name="ttlInput")
    def ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ttlInput"))

    @builtins.property
    @jsii.member(jsii_name="txtInput")
    def txt_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "txtInput"))

    @builtins.property
    @jsii.member(jsii_name="typeBitmapsInput")
    def type_bitmaps_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeBitmapsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeCoveredInput")
    def type_covered_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeCoveredInput"))

    @builtins.property
    @jsii.member(jsii_name="typeMnemonicInput")
    def type_mnemonic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeMnemonicInput"))

    @builtins.property
    @jsii.member(jsii_name="typeValueInput")
    def type_value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "typeValueInput"))

    @builtins.property
    @jsii.member(jsii_name="usageInput")
    def usage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "usageInput"))

    @builtins.property
    @jsii.member(jsii_name="weightInput")
    def weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneInput")
    def zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneInput"))

    @builtins.property
    @jsii.member(jsii_name="active")
    def active(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "active"))

    @active.setter
    def active(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f42c0869f26ddf680c11070ef11929e6dc06ac90dfe10aa402e0950e0594a0d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "active", value)

    @builtins.property
    @jsii.member(jsii_name="algorithm")
    def algorithm(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "algorithm"))

    @algorithm.setter
    def algorithm(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa1a4248401a873dbc2203db3423dcad4e149f0b64e6a29e41f5cb17a5838c6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "algorithm", value)

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9e1261e8322e3c2c29f7665489bf43a1f3ebecb9e295852797b0f5b1978d810)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificate", value)

    @builtins.property
    @jsii.member(jsii_name="digest")
    def digest(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "digest"))

    @digest.setter
    def digest(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc25aa8094f91d4fb18b3fd14da6d070c69bd987d75e65284c74d846b43080c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "digest", value)

    @builtins.property
    @jsii.member(jsii_name="digestType")
    def digest_type(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "digestType"))

    @digest_type.setter
    def digest_type(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df9f1e3ea4e335cad24543eebca59f13ac1cbce3d3a19672c05679a9d9380b00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "digestType", value)

    @builtins.property
    @jsii.member(jsii_name="emailAddress")
    def email_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emailAddress"))

    @email_address.setter
    def email_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5369ddf94d1c564c4e79131dedf4e05779a20bd1ba0da52f134e6aa0e8001820)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailAddress", value)

    @builtins.property
    @jsii.member(jsii_name="expiration")
    def expiration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expiration"))

    @expiration.setter
    def expiration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74659c93df90d05757bdab016bab34bdcbc05181cdb014cdbd674c7e1d2dc5e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expiration", value)

    @builtins.property
    @jsii.member(jsii_name="expiry")
    def expiry(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "expiry"))

    @expiry.setter
    def expiry(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06cf175ed86ca173ccfbcc0d3b50050892e31c48042b810f4ad62e7178d80cfa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expiry", value)

    @builtins.property
    @jsii.member(jsii_name="fingerprint")
    def fingerprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fingerprint"))

    @fingerprint.setter
    def fingerprint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e91c945ac634a5e22691800c587643c04e2a662277025411b58c46062bb7d436)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fingerprint", value)

    @builtins.property
    @jsii.member(jsii_name="fingerprintType")
    def fingerprint_type(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "fingerprintType"))

    @fingerprint_type.setter
    def fingerprint_type(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66a78935826432a8d8d35423d031e99a6f2e083970959c89ae39d7a19ffb66cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fingerprintType", value)

    @builtins.property
    @jsii.member(jsii_name="flags")
    def flags(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "flags"))

    @flags.setter
    def flags(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e6a7a14d06772ca11d040e7c1319fd7783ab88ef4516df157cf4b3068b89808)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flags", value)

    @builtins.property
    @jsii.member(jsii_name="flagsnaptr")
    def flagsnaptr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "flagsnaptr"))

    @flagsnaptr.setter
    def flagsnaptr(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2546b4754600fc3ab9b945a00bbd0a1886226bf269dac33b836f2bf2dffffe8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flagsnaptr", value)

    @builtins.property
    @jsii.member(jsii_name="hardware")
    def hardware(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hardware"))

    @hardware.setter
    def hardware(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3df04e206cd1f48ed66291f2c467be87da7e37f07d22f88f6de4c9cc4ad4c06d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hardware", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf9681d9a07237e59733f415c99a5c3720d63224615f3c4c51e01f3e8a2cee32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="inception")
    def inception(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "inception"))

    @inception.setter
    def inception(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b149b3f1d6545caddbc065ada987bd6ff8695fd6ac394dce712f16be8de269c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inception", value)

    @builtins.property
    @jsii.member(jsii_name="iterations")
    def iterations(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iterations"))

    @iterations.setter
    def iterations(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65cf4437f0d6c14ff3ac18215b52e2bb0e126e9d2c14076a8bf6306e25f5f06f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iterations", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b20b35bdf9454fe7d2e23db1b35cb48deac2a0a47f7492bc3f611f42526ad917)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="keytag")
    def keytag(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "keytag"))

    @keytag.setter
    def keytag(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fca335e62a15160f793d697753d2d5525430d003294b89244431ec578cd84206)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keytag", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89c9f2d454ecd8ffc2d8ca992ac648f059bf422f15ab7266e0f696be0b100db1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="mailbox")
    def mailbox(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mailbox"))

    @mailbox.setter
    def mailbox(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcfd8cc2ae364ea9fab2fc10965e534de887ae5f252bed2f8915e921813f37d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mailbox", value)

    @builtins.property
    @jsii.member(jsii_name="matchType")
    def match_type(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "matchType"))

    @match_type.setter
    def match_type(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a0e614c09a86847bba94e957506d31838c8bd01aee053c31f272e3aced0af60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92f33bf43c8bab033f0cc402aeeee65393820509d3b009a24c350847d119f6f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="nameServer")
    def name_server(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nameServer"))

    @name_server.setter
    def name_server(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__172adfe8f267c87e9a6ead2740a7bb0020ec421c2f54d064be2f979422580176)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nameServer", value)

    @builtins.property
    @jsii.member(jsii_name="nextHashedOwnerName")
    def next_hashed_owner_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nextHashedOwnerName"))

    @next_hashed_owner_name.setter
    def next_hashed_owner_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dac35b832576852b2ceb7e2ae92b5798c6dd9cdb8f9119446a72415ed3dc79f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nextHashedOwnerName", value)

    @builtins.property
    @jsii.member(jsii_name="nxdomainTtl")
    def nxdomain_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nxdomainTtl"))

    @nxdomain_ttl.setter
    def nxdomain_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59fce84d1391acae4ca0bc7bfe7d305c4fb849ed8499e74324de03497748215d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nxdomainTtl", value)

    @builtins.property
    @jsii.member(jsii_name="order")
    def order(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "order"))

    @order.setter
    def order(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__275d9eccea719d2ab8e32d5ae3ab66a127921758269d34b33993742517ffc75b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "order", value)

    @builtins.property
    @jsii.member(jsii_name="originalTtl")
    def original_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "originalTtl"))

    @original_ttl.setter
    def original_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e8f63f870e3904fd2e086e268b15abdbe39102cd1768e029163d5cbdacd3378)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originalTtl", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08bfad161f9132a14adfb7b5dbb84aeae1dee6aebcdda7a0147bf811413e0c7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="preference")
    def preference(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "preference"))

    @preference.setter
    def preference(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d0ce5a2b1a10436fe383bd244a2b0ad9fab28d5b6e8699cf8cc1d1143ae7db5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preference", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49be6c849c028daa4e428996a112d3e6521928ca083c453191dd5985fb18150a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="priorityIncrement")
    def priority_increment(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priorityIncrement"))

    @priority_increment.setter
    def priority_increment(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3a7dc6ba8e0d4193cfb32dc6d13d7c2b5258e9f3e7b89f8e403df2b96edc8ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priorityIncrement", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d335cffd1ba21c52cd7d05f522b79a9d29efd5582f04181a33f50357875784ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="recordtype")
    def recordtype(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordtype"))

    @recordtype.setter
    def recordtype(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd1fe41f762e8d7b3865d64d39bf93a9f8b99ade296bed1214da8d0120743a25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordtype", value)

    @builtins.property
    @jsii.member(jsii_name="refresh")
    def refresh(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "refresh"))

    @refresh.setter
    def refresh(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9106a7464b9eed912893c8a48393a4a61823f2afb62c066f19d568b33f97443a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "refresh", value)

    @builtins.property
    @jsii.member(jsii_name="regexp")
    def regexp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regexp"))

    @regexp.setter
    def regexp(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74a4a862a3dc5fac76e5dec8cca2a8e9432bfb01d9d69effcc461e2f639d269f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regexp", value)

    @builtins.property
    @jsii.member(jsii_name="replacement")
    def replacement(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replacement"))

    @replacement.setter
    def replacement(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f330bdc83eb1667600d7f293e2353e2b2a1c684f83ce362f2cce5d8922bb13cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replacement", value)

    @builtins.property
    @jsii.member(jsii_name="retry")
    def retry(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retry"))

    @retry.setter
    def retry(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4501069d17d89c197f621099d5f884fe20c2b252d9e06d80b4d3de6e98b5a2f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retry", value)

    @builtins.property
    @jsii.member(jsii_name="salt")
    def salt(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "salt"))

    @salt.setter
    def salt(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76f04ee2bfb85fa7545988f073a887cd79dd5749cbbc2bb968bb560b76c2eb93)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "salt", value)

    @builtins.property
    @jsii.member(jsii_name="selector")
    def selector(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "selector"))

    @selector.setter
    def selector(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__160f58e6c07764582b74fcdaec2f40c5c7addbc217b84ab5a54d638d5dffc13b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selector", value)

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "service"))

    @service.setter
    def service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__149d1396d45b5bea26ba5f146c196baaaba0a5ea286479f57213d0ad1e2aae54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "service", value)

    @builtins.property
    @jsii.member(jsii_name="signature")
    def signature(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signature"))

    @signature.setter
    def signature(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c334947df7b6324fc7137833988b74cd66ef1c9c4f2a9a34fa3270c71e899e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signature", value)

    @builtins.property
    @jsii.member(jsii_name="signer")
    def signer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signer"))

    @signer.setter
    def signer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__757090eea49e547f865d5f9e6e406a3cbd5120c216ad06d290dc01b85e63e575)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signer", value)

    @builtins.property
    @jsii.member(jsii_name="softwareAttribute")
    def software_attribute(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "softwareAttribute"))

    @software_attribute.setter
    def software_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd7ed63e4ff6810a40a464087072d38ca94a1e59d1d331b0518fc0aeebe314e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "softwareAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="subtype")
    def subtype(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "subtype"))

    @subtype.setter
    def subtype(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38922717543cccec3b1f0f14d59dff126cfc3bb2f55411ee74f939e6b2e0fb52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subtype", value)

    @builtins.property
    @jsii.member(jsii_name="svcParams")
    def svc_params(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "svcParams"))

    @svc_params.setter
    def svc_params(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5da82df4eb4677fc7f6a2d163f38e9f0931bb96b0f9c0178863fbb973c58edb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "svcParams", value)

    @builtins.property
    @jsii.member(jsii_name="svcPriority")
    def svc_priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "svcPriority"))

    @svc_priority.setter
    def svc_priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0697b13018db75a5582f3c43a2706f63afab3c1365e228ae2ac93f47d76b7095)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "svcPriority", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "target"))

    @target.setter
    def target(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__502117172eed4aa3494bbaee4f39ee9a6055cf467922541b7a9e6b67107ffbac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="targetName")
    def target_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetName"))

    @target_name.setter
    def target_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b49dccd2dfd3f5949b6117b99b62eb29627e38090f7074fa5d65045b70be77ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetName", value)

    @builtins.property
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ttl"))

    @ttl.setter
    def ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfe6a33fdd66869949f23316fefd277c6fb47be9ddbf5980264effc077b020d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ttl", value)

    @builtins.property
    @jsii.member(jsii_name="txt")
    def txt(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "txt"))

    @txt.setter
    def txt(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a84520c7b6b396f5d0787fc65362e391106f7ce2989723de65e89d3320e74f96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "txt", value)

    @builtins.property
    @jsii.member(jsii_name="typeBitmaps")
    def type_bitmaps(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "typeBitmaps"))

    @type_bitmaps.setter
    def type_bitmaps(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85a0aee3b294f543030c388392ebcd3ed072c116f242471d46fd391beaf46f4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeBitmaps", value)

    @builtins.property
    @jsii.member(jsii_name="typeCovered")
    def type_covered(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "typeCovered"))

    @type_covered.setter
    def type_covered(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9333b7c49952a9a103906f61654f8a0d219ebef9d1efb8276d8c4d5ae632b476)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeCovered", value)

    @builtins.property
    @jsii.member(jsii_name="typeMnemonic")
    def type_mnemonic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "typeMnemonic"))

    @type_mnemonic.setter
    def type_mnemonic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6bd4e4b18f1829e539cf88399e138b29a761fdcfc3eb37a1b274e580386f55d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeMnemonic", value)

    @builtins.property
    @jsii.member(jsii_name="typeValue")
    def type_value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "typeValue"))

    @type_value.setter
    def type_value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1d8d9bbda618d07f2454eff3141be41dcf93771f1768d78c59eb0494a7636d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeValue", value)

    @builtins.property
    @jsii.member(jsii_name="usage")
    def usage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "usage"))

    @usage.setter
    def usage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1b0579d010789e884a4c4d8a985f35dd80180c3195d21a79ce541a5c95a6182)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usage", value)

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weight"))

    @weight.setter
    def weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be3b5d39eb6f32044fc4c96ab9f37158bf614e1884bdae6db2097e48ca3b1587)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weight", value)

    @builtins.property
    @jsii.member(jsii_name="zone")
    def zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zone"))

    @zone.setter
    def zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94069f9359d5f2a8aab43986942c78a825615e9382cce6650466b5f824629bdc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zone", value)


@jsii.data_type(
    jsii_type="akamai.dnsRecord.DnsRecordConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "recordtype": "recordtype",
        "ttl": "ttl",
        "zone": "zone",
        "active": "active",
        "algorithm": "algorithm",
        "certificate": "certificate",
        "digest": "digest",
        "digest_type": "digestType",
        "email_address": "emailAddress",
        "expiration": "expiration",
        "expiry": "expiry",
        "fingerprint": "fingerprint",
        "fingerprint_type": "fingerprintType",
        "flags": "flags",
        "flagsnaptr": "flagsnaptr",
        "hardware": "hardware",
        "id": "id",
        "inception": "inception",
        "iterations": "iterations",
        "key": "key",
        "keytag": "keytag",
        "labels": "labels",
        "mailbox": "mailbox",
        "match_type": "matchType",
        "name_server": "nameServer",
        "next_hashed_owner_name": "nextHashedOwnerName",
        "nxdomain_ttl": "nxdomainTtl",
        "order": "order",
        "original_ttl": "originalTtl",
        "port": "port",
        "preference": "preference",
        "priority": "priority",
        "priority_increment": "priorityIncrement",
        "protocol": "protocol",
        "refresh": "refresh",
        "regexp": "regexp",
        "replacement": "replacement",
        "retry": "retry",
        "salt": "salt",
        "selector": "selector",
        "service": "service",
        "signature": "signature",
        "signer": "signer",
        "software_attribute": "softwareAttribute",
        "subtype": "subtype",
        "svc_params": "svcParams",
        "svc_priority": "svcPriority",
        "target": "target",
        "target_name": "targetName",
        "txt": "txt",
        "type_bitmaps": "typeBitmaps",
        "type_covered": "typeCovered",
        "type_mnemonic": "typeMnemonic",
        "type_value": "typeValue",
        "usage": "usage",
        "weight": "weight",
    },
)
class DnsRecordConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        name: builtins.str,
        recordtype: builtins.str,
        ttl: jsii.Number,
        zone: builtins.str,
        active: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        algorithm: typing.Optional[jsii.Number] = None,
        certificate: typing.Optional[builtins.str] = None,
        digest: typing.Optional[builtins.str] = None,
        digest_type: typing.Optional[jsii.Number] = None,
        email_address: typing.Optional[builtins.str] = None,
        expiration: typing.Optional[builtins.str] = None,
        expiry: typing.Optional[jsii.Number] = None,
        fingerprint: typing.Optional[builtins.str] = None,
        fingerprint_type: typing.Optional[jsii.Number] = None,
        flags: typing.Optional[jsii.Number] = None,
        flagsnaptr: typing.Optional[builtins.str] = None,
        hardware: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        inception: typing.Optional[builtins.str] = None,
        iterations: typing.Optional[jsii.Number] = None,
        key: typing.Optional[builtins.str] = None,
        keytag: typing.Optional[jsii.Number] = None,
        labels: typing.Optional[jsii.Number] = None,
        mailbox: typing.Optional[builtins.str] = None,
        match_type: typing.Optional[jsii.Number] = None,
        name_server: typing.Optional[builtins.str] = None,
        next_hashed_owner_name: typing.Optional[builtins.str] = None,
        nxdomain_ttl: typing.Optional[jsii.Number] = None,
        order: typing.Optional[jsii.Number] = None,
        original_ttl: typing.Optional[jsii.Number] = None,
        port: typing.Optional[jsii.Number] = None,
        preference: typing.Optional[jsii.Number] = None,
        priority: typing.Optional[jsii.Number] = None,
        priority_increment: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional[jsii.Number] = None,
        refresh: typing.Optional[jsii.Number] = None,
        regexp: typing.Optional[builtins.str] = None,
        replacement: typing.Optional[builtins.str] = None,
        retry: typing.Optional[jsii.Number] = None,
        salt: typing.Optional[builtins.str] = None,
        selector: typing.Optional[jsii.Number] = None,
        service: typing.Optional[builtins.str] = None,
        signature: typing.Optional[builtins.str] = None,
        signer: typing.Optional[builtins.str] = None,
        software_attribute: typing.Optional[builtins.str] = None,
        subtype: typing.Optional[jsii.Number] = None,
        svc_params: typing.Optional[builtins.str] = None,
        svc_priority: typing.Optional[jsii.Number] = None,
        target: typing.Optional[typing.Sequence[builtins.str]] = None,
        target_name: typing.Optional[builtins.str] = None,
        txt: typing.Optional[builtins.str] = None,
        type_bitmaps: typing.Optional[builtins.str] = None,
        type_covered: typing.Optional[builtins.str] = None,
        type_mnemonic: typing.Optional[builtins.str] = None,
        type_value: typing.Optional[jsii.Number] = None,
        usage: typing.Optional[jsii.Number] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#name DnsRecord#name}.
        :param recordtype: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#recordtype DnsRecord#recordtype}.
        :param ttl: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#ttl DnsRecord#ttl}.
        :param zone: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#zone DnsRecord#zone}.
        :param active: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#active DnsRecord#active}.
        :param algorithm: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#algorithm DnsRecord#algorithm}.
        :param certificate: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#certificate DnsRecord#certificate}.
        :param digest: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#digest DnsRecord#digest}.
        :param digest_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#digest_type DnsRecord#digest_type}.
        :param email_address: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#email_address DnsRecord#email_address}.
        :param expiration: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#expiration DnsRecord#expiration}.
        :param expiry: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#expiry DnsRecord#expiry}.
        :param fingerprint: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#fingerprint DnsRecord#fingerprint}.
        :param fingerprint_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#fingerprint_type DnsRecord#fingerprint_type}.
        :param flags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#flags DnsRecord#flags}.
        :param flagsnaptr: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#flagsnaptr DnsRecord#flagsnaptr}.
        :param hardware: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#hardware DnsRecord#hardware}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#id DnsRecord#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param inception: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#inception DnsRecord#inception}.
        :param iterations: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#iterations DnsRecord#iterations}.
        :param key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#key DnsRecord#key}.
        :param keytag: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#keytag DnsRecord#keytag}.
        :param labels: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#labels DnsRecord#labels}.
        :param mailbox: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#mailbox DnsRecord#mailbox}.
        :param match_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#match_type DnsRecord#match_type}.
        :param name_server: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#name_server DnsRecord#name_server}.
        :param next_hashed_owner_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#next_hashed_owner_name DnsRecord#next_hashed_owner_name}.
        :param nxdomain_ttl: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#nxdomain_ttl DnsRecord#nxdomain_ttl}.
        :param order: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#order DnsRecord#order}.
        :param original_ttl: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#original_ttl DnsRecord#original_ttl}.
        :param port: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#port DnsRecord#port}.
        :param preference: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#preference DnsRecord#preference}.
        :param priority: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#priority DnsRecord#priority}.
        :param priority_increment: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#priority_increment DnsRecord#priority_increment}.
        :param protocol: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#protocol DnsRecord#protocol}.
        :param refresh: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#refresh DnsRecord#refresh}.
        :param regexp: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#regexp DnsRecord#regexp}.
        :param replacement: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#replacement DnsRecord#replacement}.
        :param retry: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#retry DnsRecord#retry}.
        :param salt: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#salt DnsRecord#salt}.
        :param selector: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#selector DnsRecord#selector}.
        :param service: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#service DnsRecord#service}.
        :param signature: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#signature DnsRecord#signature}.
        :param signer: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#signer DnsRecord#signer}.
        :param software_attribute: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#software DnsRecord#software}.
        :param subtype: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#subtype DnsRecord#subtype}.
        :param svc_params: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#svc_params DnsRecord#svc_params}.
        :param svc_priority: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#svc_priority DnsRecord#svc_priority}.
        :param target: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#target DnsRecord#target}.
        :param target_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#target_name DnsRecord#target_name}.
        :param txt: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#txt DnsRecord#txt}.
        :param type_bitmaps: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#type_bitmaps DnsRecord#type_bitmaps}.
        :param type_covered: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#type_covered DnsRecord#type_covered}.
        :param type_mnemonic: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#type_mnemonic DnsRecord#type_mnemonic}.
        :param type_value: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#type_value DnsRecord#type_value}.
        :param usage: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#usage DnsRecord#usage}.
        :param weight: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#weight DnsRecord#weight}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0189bd2b3927ccd744c8591dfdbceb94981b8f2f8035b5279859df1d22ab131f)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument recordtype", value=recordtype, expected_type=type_hints["recordtype"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
            check_type(argname="argument active", value=active, expected_type=type_hints["active"])
            check_type(argname="argument algorithm", value=algorithm, expected_type=type_hints["algorithm"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument digest", value=digest, expected_type=type_hints["digest"])
            check_type(argname="argument digest_type", value=digest_type, expected_type=type_hints["digest_type"])
            check_type(argname="argument email_address", value=email_address, expected_type=type_hints["email_address"])
            check_type(argname="argument expiration", value=expiration, expected_type=type_hints["expiration"])
            check_type(argname="argument expiry", value=expiry, expected_type=type_hints["expiry"])
            check_type(argname="argument fingerprint", value=fingerprint, expected_type=type_hints["fingerprint"])
            check_type(argname="argument fingerprint_type", value=fingerprint_type, expected_type=type_hints["fingerprint_type"])
            check_type(argname="argument flags", value=flags, expected_type=type_hints["flags"])
            check_type(argname="argument flagsnaptr", value=flagsnaptr, expected_type=type_hints["flagsnaptr"])
            check_type(argname="argument hardware", value=hardware, expected_type=type_hints["hardware"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument inception", value=inception, expected_type=type_hints["inception"])
            check_type(argname="argument iterations", value=iterations, expected_type=type_hints["iterations"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument keytag", value=keytag, expected_type=type_hints["keytag"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument mailbox", value=mailbox, expected_type=type_hints["mailbox"])
            check_type(argname="argument match_type", value=match_type, expected_type=type_hints["match_type"])
            check_type(argname="argument name_server", value=name_server, expected_type=type_hints["name_server"])
            check_type(argname="argument next_hashed_owner_name", value=next_hashed_owner_name, expected_type=type_hints["next_hashed_owner_name"])
            check_type(argname="argument nxdomain_ttl", value=nxdomain_ttl, expected_type=type_hints["nxdomain_ttl"])
            check_type(argname="argument order", value=order, expected_type=type_hints["order"])
            check_type(argname="argument original_ttl", value=original_ttl, expected_type=type_hints["original_ttl"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument preference", value=preference, expected_type=type_hints["preference"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument priority_increment", value=priority_increment, expected_type=type_hints["priority_increment"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument refresh", value=refresh, expected_type=type_hints["refresh"])
            check_type(argname="argument regexp", value=regexp, expected_type=type_hints["regexp"])
            check_type(argname="argument replacement", value=replacement, expected_type=type_hints["replacement"])
            check_type(argname="argument retry", value=retry, expected_type=type_hints["retry"])
            check_type(argname="argument salt", value=salt, expected_type=type_hints["salt"])
            check_type(argname="argument selector", value=selector, expected_type=type_hints["selector"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument signature", value=signature, expected_type=type_hints["signature"])
            check_type(argname="argument signer", value=signer, expected_type=type_hints["signer"])
            check_type(argname="argument software_attribute", value=software_attribute, expected_type=type_hints["software_attribute"])
            check_type(argname="argument subtype", value=subtype, expected_type=type_hints["subtype"])
            check_type(argname="argument svc_params", value=svc_params, expected_type=type_hints["svc_params"])
            check_type(argname="argument svc_priority", value=svc_priority, expected_type=type_hints["svc_priority"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument target_name", value=target_name, expected_type=type_hints["target_name"])
            check_type(argname="argument txt", value=txt, expected_type=type_hints["txt"])
            check_type(argname="argument type_bitmaps", value=type_bitmaps, expected_type=type_hints["type_bitmaps"])
            check_type(argname="argument type_covered", value=type_covered, expected_type=type_hints["type_covered"])
            check_type(argname="argument type_mnemonic", value=type_mnemonic, expected_type=type_hints["type_mnemonic"])
            check_type(argname="argument type_value", value=type_value, expected_type=type_hints["type_value"])
            check_type(argname="argument usage", value=usage, expected_type=type_hints["usage"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "recordtype": recordtype,
            "ttl": ttl,
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
        if active is not None:
            self._values["active"] = active
        if algorithm is not None:
            self._values["algorithm"] = algorithm
        if certificate is not None:
            self._values["certificate"] = certificate
        if digest is not None:
            self._values["digest"] = digest
        if digest_type is not None:
            self._values["digest_type"] = digest_type
        if email_address is not None:
            self._values["email_address"] = email_address
        if expiration is not None:
            self._values["expiration"] = expiration
        if expiry is not None:
            self._values["expiry"] = expiry
        if fingerprint is not None:
            self._values["fingerprint"] = fingerprint
        if fingerprint_type is not None:
            self._values["fingerprint_type"] = fingerprint_type
        if flags is not None:
            self._values["flags"] = flags
        if flagsnaptr is not None:
            self._values["flagsnaptr"] = flagsnaptr
        if hardware is not None:
            self._values["hardware"] = hardware
        if id is not None:
            self._values["id"] = id
        if inception is not None:
            self._values["inception"] = inception
        if iterations is not None:
            self._values["iterations"] = iterations
        if key is not None:
            self._values["key"] = key
        if keytag is not None:
            self._values["keytag"] = keytag
        if labels is not None:
            self._values["labels"] = labels
        if mailbox is not None:
            self._values["mailbox"] = mailbox
        if match_type is not None:
            self._values["match_type"] = match_type
        if name_server is not None:
            self._values["name_server"] = name_server
        if next_hashed_owner_name is not None:
            self._values["next_hashed_owner_name"] = next_hashed_owner_name
        if nxdomain_ttl is not None:
            self._values["nxdomain_ttl"] = nxdomain_ttl
        if order is not None:
            self._values["order"] = order
        if original_ttl is not None:
            self._values["original_ttl"] = original_ttl
        if port is not None:
            self._values["port"] = port
        if preference is not None:
            self._values["preference"] = preference
        if priority is not None:
            self._values["priority"] = priority
        if priority_increment is not None:
            self._values["priority_increment"] = priority_increment
        if protocol is not None:
            self._values["protocol"] = protocol
        if refresh is not None:
            self._values["refresh"] = refresh
        if regexp is not None:
            self._values["regexp"] = regexp
        if replacement is not None:
            self._values["replacement"] = replacement
        if retry is not None:
            self._values["retry"] = retry
        if salt is not None:
            self._values["salt"] = salt
        if selector is not None:
            self._values["selector"] = selector
        if service is not None:
            self._values["service"] = service
        if signature is not None:
            self._values["signature"] = signature
        if signer is not None:
            self._values["signer"] = signer
        if software_attribute is not None:
            self._values["software_attribute"] = software_attribute
        if subtype is not None:
            self._values["subtype"] = subtype
        if svc_params is not None:
            self._values["svc_params"] = svc_params
        if svc_priority is not None:
            self._values["svc_priority"] = svc_priority
        if target is not None:
            self._values["target"] = target
        if target_name is not None:
            self._values["target_name"] = target_name
        if txt is not None:
            self._values["txt"] = txt
        if type_bitmaps is not None:
            self._values["type_bitmaps"] = type_bitmaps
        if type_covered is not None:
            self._values["type_covered"] = type_covered
        if type_mnemonic is not None:
            self._values["type_mnemonic"] = type_mnemonic
        if type_value is not None:
            self._values["type_value"] = type_value
        if usage is not None:
            self._values["usage"] = usage
        if weight is not None:
            self._values["weight"] = weight

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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#name DnsRecord#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def recordtype(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#recordtype DnsRecord#recordtype}.'''
        result = self._values.get("recordtype")
        assert result is not None, "Required property 'recordtype' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ttl(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#ttl DnsRecord#ttl}.'''
        result = self._values.get("ttl")
        assert result is not None, "Required property 'ttl' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def zone(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#zone DnsRecord#zone}.'''
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def active(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#active DnsRecord#active}.'''
        result = self._values.get("active")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def algorithm(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#algorithm DnsRecord#algorithm}.'''
        result = self._values.get("algorithm")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def certificate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#certificate DnsRecord#certificate}.'''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def digest(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#digest DnsRecord#digest}.'''
        result = self._values.get("digest")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def digest_type(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#digest_type DnsRecord#digest_type}.'''
        result = self._values.get("digest_type")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def email_address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#email_address DnsRecord#email_address}.'''
        result = self._values.get("email_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expiration(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#expiration DnsRecord#expiration}.'''
        result = self._values.get("expiration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expiry(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#expiry DnsRecord#expiry}.'''
        result = self._values.get("expiry")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def fingerprint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#fingerprint DnsRecord#fingerprint}.'''
        result = self._values.get("fingerprint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fingerprint_type(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#fingerprint_type DnsRecord#fingerprint_type}.'''
        result = self._values.get("fingerprint_type")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def flags(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#flags DnsRecord#flags}.'''
        result = self._values.get("flags")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def flagsnaptr(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#flagsnaptr DnsRecord#flagsnaptr}.'''
        result = self._values.get("flagsnaptr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hardware(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#hardware DnsRecord#hardware}.'''
        result = self._values.get("hardware")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#id DnsRecord#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def inception(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#inception DnsRecord#inception}.'''
        result = self._values.get("inception")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iterations(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#iterations DnsRecord#iterations}.'''
        result = self._values.get("iterations")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#key DnsRecord#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def keytag(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#keytag DnsRecord#keytag}.'''
        result = self._values.get("keytag")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def labels(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#labels DnsRecord#labels}.'''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def mailbox(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#mailbox DnsRecord#mailbox}.'''
        result = self._values.get("mailbox")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_type(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#match_type DnsRecord#match_type}.'''
        result = self._values.get("match_type")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name_server(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#name_server DnsRecord#name_server}.'''
        result = self._values.get("name_server")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def next_hashed_owner_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#next_hashed_owner_name DnsRecord#next_hashed_owner_name}.'''
        result = self._values.get("next_hashed_owner_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nxdomain_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#nxdomain_ttl DnsRecord#nxdomain_ttl}.'''
        result = self._values.get("nxdomain_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def order(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#order DnsRecord#order}.'''
        result = self._values.get("order")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def original_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#original_ttl DnsRecord#original_ttl}.'''
        result = self._values.get("original_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#port DnsRecord#port}.'''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def preference(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#preference DnsRecord#preference}.'''
        result = self._values.get("preference")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#priority DnsRecord#priority}.'''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def priority_increment(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#priority_increment DnsRecord#priority_increment}.'''
        result = self._values.get("priority_increment")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def protocol(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#protocol DnsRecord#protocol}.'''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def refresh(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#refresh DnsRecord#refresh}.'''
        result = self._values.get("refresh")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def regexp(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#regexp DnsRecord#regexp}.'''
        result = self._values.get("regexp")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replacement(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#replacement DnsRecord#replacement}.'''
        result = self._values.get("replacement")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retry(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#retry DnsRecord#retry}.'''
        result = self._values.get("retry")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def salt(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#salt DnsRecord#salt}.'''
        result = self._values.get("salt")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def selector(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#selector DnsRecord#selector}.'''
        result = self._values.get("selector")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def service(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#service DnsRecord#service}.'''
        result = self._values.get("service")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def signature(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#signature DnsRecord#signature}.'''
        result = self._values.get("signature")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def signer(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#signer DnsRecord#signer}.'''
        result = self._values.get("signer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def software_attribute(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#software DnsRecord#software}.'''
        result = self._values.get("software_attribute")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subtype(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#subtype DnsRecord#subtype}.'''
        result = self._values.get("subtype")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def svc_params(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#svc_params DnsRecord#svc_params}.'''
        result = self._values.get("svc_params")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def svc_priority(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#svc_priority DnsRecord#svc_priority}.'''
        result = self._values.get("svc_priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def target(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#target DnsRecord#target}.'''
        result = self._values.get("target")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def target_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#target_name DnsRecord#target_name}.'''
        result = self._values.get("target_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def txt(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#txt DnsRecord#txt}.'''
        result = self._values.get("txt")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type_bitmaps(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#type_bitmaps DnsRecord#type_bitmaps}.'''
        result = self._values.get("type_bitmaps")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type_covered(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#type_covered DnsRecord#type_covered}.'''
        result = self._values.get("type_covered")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type_mnemonic(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#type_mnemonic DnsRecord#type_mnemonic}.'''
        result = self._values.get("type_mnemonic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type_value(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#type_value DnsRecord#type_value}.'''
        result = self._values.get("type_value")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def usage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#usage DnsRecord#usage}.'''
        result = self._values.get("usage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/dns_record#weight DnsRecord#weight}.'''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DnsRecordConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DnsRecord",
    "DnsRecordConfig",
]

publication.publish()

def _typecheckingstub__e64539b4bd69d8ac100173b1efebca8d321920cf3ddd8188e73ceeaab1321cab(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    recordtype: builtins.str,
    ttl: jsii.Number,
    zone: builtins.str,
    active: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    algorithm: typing.Optional[jsii.Number] = None,
    certificate: typing.Optional[builtins.str] = None,
    digest: typing.Optional[builtins.str] = None,
    digest_type: typing.Optional[jsii.Number] = None,
    email_address: typing.Optional[builtins.str] = None,
    expiration: typing.Optional[builtins.str] = None,
    expiry: typing.Optional[jsii.Number] = None,
    fingerprint: typing.Optional[builtins.str] = None,
    fingerprint_type: typing.Optional[jsii.Number] = None,
    flags: typing.Optional[jsii.Number] = None,
    flagsnaptr: typing.Optional[builtins.str] = None,
    hardware: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    inception: typing.Optional[builtins.str] = None,
    iterations: typing.Optional[jsii.Number] = None,
    key: typing.Optional[builtins.str] = None,
    keytag: typing.Optional[jsii.Number] = None,
    labels: typing.Optional[jsii.Number] = None,
    mailbox: typing.Optional[builtins.str] = None,
    match_type: typing.Optional[jsii.Number] = None,
    name_server: typing.Optional[builtins.str] = None,
    next_hashed_owner_name: typing.Optional[builtins.str] = None,
    nxdomain_ttl: typing.Optional[jsii.Number] = None,
    order: typing.Optional[jsii.Number] = None,
    original_ttl: typing.Optional[jsii.Number] = None,
    port: typing.Optional[jsii.Number] = None,
    preference: typing.Optional[jsii.Number] = None,
    priority: typing.Optional[jsii.Number] = None,
    priority_increment: typing.Optional[jsii.Number] = None,
    protocol: typing.Optional[jsii.Number] = None,
    refresh: typing.Optional[jsii.Number] = None,
    regexp: typing.Optional[builtins.str] = None,
    replacement: typing.Optional[builtins.str] = None,
    retry: typing.Optional[jsii.Number] = None,
    salt: typing.Optional[builtins.str] = None,
    selector: typing.Optional[jsii.Number] = None,
    service: typing.Optional[builtins.str] = None,
    signature: typing.Optional[builtins.str] = None,
    signer: typing.Optional[builtins.str] = None,
    software_attribute: typing.Optional[builtins.str] = None,
    subtype: typing.Optional[jsii.Number] = None,
    svc_params: typing.Optional[builtins.str] = None,
    svc_priority: typing.Optional[jsii.Number] = None,
    target: typing.Optional[typing.Sequence[builtins.str]] = None,
    target_name: typing.Optional[builtins.str] = None,
    txt: typing.Optional[builtins.str] = None,
    type_bitmaps: typing.Optional[builtins.str] = None,
    type_covered: typing.Optional[builtins.str] = None,
    type_mnemonic: typing.Optional[builtins.str] = None,
    type_value: typing.Optional[jsii.Number] = None,
    usage: typing.Optional[jsii.Number] = None,
    weight: typing.Optional[jsii.Number] = None,
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

def _typecheckingstub__95a781ec517f5e040563a01e2a2caff0a4b36a0a091610e8ebc2354749b9db17(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f42c0869f26ddf680c11070ef11929e6dc06ac90dfe10aa402e0950e0594a0d6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa1a4248401a873dbc2203db3423dcad4e149f0b64e6a29e41f5cb17a5838c6e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9e1261e8322e3c2c29f7665489bf43a1f3ebecb9e295852797b0f5b1978d810(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc25aa8094f91d4fb18b3fd14da6d070c69bd987d75e65284c74d846b43080c1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df9f1e3ea4e335cad24543eebca59f13ac1cbce3d3a19672c05679a9d9380b00(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5369ddf94d1c564c4e79131dedf4e05779a20bd1ba0da52f134e6aa0e8001820(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74659c93df90d05757bdab016bab34bdcbc05181cdb014cdbd674c7e1d2dc5e6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06cf175ed86ca173ccfbcc0d3b50050892e31c48042b810f4ad62e7178d80cfa(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e91c945ac634a5e22691800c587643c04e2a662277025411b58c46062bb7d436(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66a78935826432a8d8d35423d031e99a6f2e083970959c89ae39d7a19ffb66cc(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e6a7a14d06772ca11d040e7c1319fd7783ab88ef4516df157cf4b3068b89808(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2546b4754600fc3ab9b945a00bbd0a1886226bf269dac33b836f2bf2dffffe8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3df04e206cd1f48ed66291f2c467be87da7e37f07d22f88f6de4c9cc4ad4c06d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf9681d9a07237e59733f415c99a5c3720d63224615f3c4c51e01f3e8a2cee32(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b149b3f1d6545caddbc065ada987bd6ff8695fd6ac394dce712f16be8de269c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65cf4437f0d6c14ff3ac18215b52e2bb0e126e9d2c14076a8bf6306e25f5f06f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b20b35bdf9454fe7d2e23db1b35cb48deac2a0a47f7492bc3f611f42526ad917(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fca335e62a15160f793d697753d2d5525430d003294b89244431ec578cd84206(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89c9f2d454ecd8ffc2d8ca992ac648f059bf422f15ab7266e0f696be0b100db1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcfd8cc2ae364ea9fab2fc10965e534de887ae5f252bed2f8915e921813f37d6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a0e614c09a86847bba94e957506d31838c8bd01aee053c31f272e3aced0af60(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92f33bf43c8bab033f0cc402aeeee65393820509d3b009a24c350847d119f6f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__172adfe8f267c87e9a6ead2740a7bb0020ec421c2f54d064be2f979422580176(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dac35b832576852b2ceb7e2ae92b5798c6dd9cdb8f9119446a72415ed3dc79f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59fce84d1391acae4ca0bc7bfe7d305c4fb849ed8499e74324de03497748215d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__275d9eccea719d2ab8e32d5ae3ab66a127921758269d34b33993742517ffc75b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e8f63f870e3904fd2e086e268b15abdbe39102cd1768e029163d5cbdacd3378(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08bfad161f9132a14adfb7b5dbb84aeae1dee6aebcdda7a0147bf811413e0c7f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d0ce5a2b1a10436fe383bd244a2b0ad9fab28d5b6e8699cf8cc1d1143ae7db5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49be6c849c028daa4e428996a112d3e6521928ca083c453191dd5985fb18150a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3a7dc6ba8e0d4193cfb32dc6d13d7c2b5258e9f3e7b89f8e403df2b96edc8ee(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d335cffd1ba21c52cd7d05f522b79a9d29efd5582f04181a33f50357875784ea(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd1fe41f762e8d7b3865d64d39bf93a9f8b99ade296bed1214da8d0120743a25(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9106a7464b9eed912893c8a48393a4a61823f2afb62c066f19d568b33f97443a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74a4a862a3dc5fac76e5dec8cca2a8e9432bfb01d9d69effcc461e2f639d269f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f330bdc83eb1667600d7f293e2353e2b2a1c684f83ce362f2cce5d8922bb13cd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4501069d17d89c197f621099d5f884fe20c2b252d9e06d80b4d3de6e98b5a2f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76f04ee2bfb85fa7545988f073a887cd79dd5749cbbc2bb968bb560b76c2eb93(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__160f58e6c07764582b74fcdaec2f40c5c7addbc217b84ab5a54d638d5dffc13b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__149d1396d45b5bea26ba5f146c196baaaba0a5ea286479f57213d0ad1e2aae54(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c334947df7b6324fc7137833988b74cd66ef1c9c4f2a9a34fa3270c71e899e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__757090eea49e547f865d5f9e6e406a3cbd5120c216ad06d290dc01b85e63e575(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd7ed63e4ff6810a40a464087072d38ca94a1e59d1d331b0518fc0aeebe314e6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38922717543cccec3b1f0f14d59dff126cfc3bb2f55411ee74f939e6b2e0fb52(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5da82df4eb4677fc7f6a2d163f38e9f0931bb96b0f9c0178863fbb973c58edb5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0697b13018db75a5582f3c43a2706f63afab3c1365e228ae2ac93f47d76b7095(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__502117172eed4aa3494bbaee4f39ee9a6055cf467922541b7a9e6b67107ffbac(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b49dccd2dfd3f5949b6117b99b62eb29627e38090f7074fa5d65045b70be77ed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfe6a33fdd66869949f23316fefd277c6fb47be9ddbf5980264effc077b020d2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a84520c7b6b396f5d0787fc65362e391106f7ce2989723de65e89d3320e74f96(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85a0aee3b294f543030c388392ebcd3ed072c116f242471d46fd391beaf46f4f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9333b7c49952a9a103906f61654f8a0d219ebef9d1efb8276d8c4d5ae632b476(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6bd4e4b18f1829e539cf88399e138b29a761fdcfc3eb37a1b274e580386f55d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1d8d9bbda618d07f2454eff3141be41dcf93771f1768d78c59eb0494a7636d4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1b0579d010789e884a4c4d8a985f35dd80180c3195d21a79ce541a5c95a6182(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be3b5d39eb6f32044fc4c96ab9f37158bf614e1884bdae6db2097e48ca3b1587(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94069f9359d5f2a8aab43986942c78a825615e9382cce6650466b5f824629bdc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0189bd2b3927ccd744c8591dfdbceb94981b8f2f8035b5279859df1d22ab131f(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    recordtype: builtins.str,
    ttl: jsii.Number,
    zone: builtins.str,
    active: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    algorithm: typing.Optional[jsii.Number] = None,
    certificate: typing.Optional[builtins.str] = None,
    digest: typing.Optional[builtins.str] = None,
    digest_type: typing.Optional[jsii.Number] = None,
    email_address: typing.Optional[builtins.str] = None,
    expiration: typing.Optional[builtins.str] = None,
    expiry: typing.Optional[jsii.Number] = None,
    fingerprint: typing.Optional[builtins.str] = None,
    fingerprint_type: typing.Optional[jsii.Number] = None,
    flags: typing.Optional[jsii.Number] = None,
    flagsnaptr: typing.Optional[builtins.str] = None,
    hardware: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    inception: typing.Optional[builtins.str] = None,
    iterations: typing.Optional[jsii.Number] = None,
    key: typing.Optional[builtins.str] = None,
    keytag: typing.Optional[jsii.Number] = None,
    labels: typing.Optional[jsii.Number] = None,
    mailbox: typing.Optional[builtins.str] = None,
    match_type: typing.Optional[jsii.Number] = None,
    name_server: typing.Optional[builtins.str] = None,
    next_hashed_owner_name: typing.Optional[builtins.str] = None,
    nxdomain_ttl: typing.Optional[jsii.Number] = None,
    order: typing.Optional[jsii.Number] = None,
    original_ttl: typing.Optional[jsii.Number] = None,
    port: typing.Optional[jsii.Number] = None,
    preference: typing.Optional[jsii.Number] = None,
    priority: typing.Optional[jsii.Number] = None,
    priority_increment: typing.Optional[jsii.Number] = None,
    protocol: typing.Optional[jsii.Number] = None,
    refresh: typing.Optional[jsii.Number] = None,
    regexp: typing.Optional[builtins.str] = None,
    replacement: typing.Optional[builtins.str] = None,
    retry: typing.Optional[jsii.Number] = None,
    salt: typing.Optional[builtins.str] = None,
    selector: typing.Optional[jsii.Number] = None,
    service: typing.Optional[builtins.str] = None,
    signature: typing.Optional[builtins.str] = None,
    signer: typing.Optional[builtins.str] = None,
    software_attribute: typing.Optional[builtins.str] = None,
    subtype: typing.Optional[jsii.Number] = None,
    svc_params: typing.Optional[builtins.str] = None,
    svc_priority: typing.Optional[jsii.Number] = None,
    target: typing.Optional[typing.Sequence[builtins.str]] = None,
    target_name: typing.Optional[builtins.str] = None,
    txt: typing.Optional[builtins.str] = None,
    type_bitmaps: typing.Optional[builtins.str] = None,
    type_covered: typing.Optional[builtins.str] = None,
    type_mnemonic: typing.Optional[builtins.str] = None,
    type_value: typing.Optional[jsii.Number] = None,
    usage: typing.Optional[jsii.Number] = None,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass
