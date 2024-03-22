'''
# `akamai_cps_upload_certificate`

Refer to the Terraform Registry for docs: [`akamai_cps_upload_certificate`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate).
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


class CpsUploadCertificate(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.cpsUploadCertificate.CpsUploadCertificate",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate akamai_cps_upload_certificate}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        enrollment_id: jsii.Number,
        acknowledge_change_management: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        acknowledge_post_verification_warnings: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        auto_approve_warnings: typing.Optional[typing.Sequence[builtins.str]] = None,
        certificate_ecdsa_pem: typing.Optional[builtins.str] = None,
        certificate_rsa_pem: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["CpsUploadCertificateTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        trust_chain_ecdsa_pem: typing.Optional[builtins.str] = None,
        trust_chain_rsa_pem: typing.Optional[builtins.str] = None,
        wait_for_deployment: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate akamai_cps_upload_certificate} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param enrollment_id: The unique identifier of the enrollment. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#enrollment_id CpsUploadCertificate#enrollment_id}
        :param acknowledge_change_management: Whether to acknowledge change management. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#acknowledge_change_management CpsUploadCertificate#acknowledge_change_management}
        :param acknowledge_post_verification_warnings: Whether to acknowledge post-verification warnings. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#acknowledge_post_verification_warnings CpsUploadCertificate#acknowledge_post_verification_warnings}
        :param auto_approve_warnings: List of post-verification warnings to be automatically acknowledged. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#auto_approve_warnings CpsUploadCertificate#auto_approve_warnings}
        :param certificate_ecdsa_pem: ECDSA certificate in pem format to be uploaded. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#certificate_ecdsa_pem CpsUploadCertificate#certificate_ecdsa_pem}
        :param certificate_rsa_pem: RSA certificate in pem format to be uploaded. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#certificate_rsa_pem CpsUploadCertificate#certificate_rsa_pem}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#id CpsUploadCertificate#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#timeouts CpsUploadCertificate#timeouts}
        :param trust_chain_ecdsa_pem: Trust chain in pem format for provided ECDSA certificate. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#trust_chain_ecdsa_pem CpsUploadCertificate#trust_chain_ecdsa_pem}
        :param trust_chain_rsa_pem: Trust chain in pem format for provided RSA certificate. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#trust_chain_rsa_pem CpsUploadCertificate#trust_chain_rsa_pem}
        :param wait_for_deployment: Whether to wait for certificate to be deployed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#wait_for_deployment CpsUploadCertificate#wait_for_deployment}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b16a989fd507f41f4e47c71952085679774005252c6cb584d5c64a3caa580918)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CpsUploadCertificateConfig(
            enrollment_id=enrollment_id,
            acknowledge_change_management=acknowledge_change_management,
            acknowledge_post_verification_warnings=acknowledge_post_verification_warnings,
            auto_approve_warnings=auto_approve_warnings,
            certificate_ecdsa_pem=certificate_ecdsa_pem,
            certificate_rsa_pem=certificate_rsa_pem,
            id=id,
            timeouts=timeouts,
            trust_chain_ecdsa_pem=trust_chain_ecdsa_pem,
            trust_chain_rsa_pem=trust_chain_rsa_pem,
            wait_for_deployment=wait_for_deployment,
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
        '''Generates CDKTF code for importing a CpsUploadCertificate resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the CpsUploadCertificate to import.
        :param import_from_id: The id of the existing CpsUploadCertificate that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the CpsUploadCertificate to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ca8d12b5aaae5e6b08a7951639dd19652d6bda94c62be0a4ece1e57441bd085)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self, *, default: typing.Optional[builtins.str] = None) -> None:
        '''
        :param default: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#default CpsUploadCertificate#default}.
        '''
        value = CpsUploadCertificateTimeouts(default=default)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAcknowledgeChangeManagement")
    def reset_acknowledge_change_management(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcknowledgeChangeManagement", []))

    @jsii.member(jsii_name="resetAcknowledgePostVerificationWarnings")
    def reset_acknowledge_post_verification_warnings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcknowledgePostVerificationWarnings", []))

    @jsii.member(jsii_name="resetAutoApproveWarnings")
    def reset_auto_approve_warnings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoApproveWarnings", []))

    @jsii.member(jsii_name="resetCertificateEcdsaPem")
    def reset_certificate_ecdsa_pem(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateEcdsaPem", []))

    @jsii.member(jsii_name="resetCertificateRsaPem")
    def reset_certificate_rsa_pem(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateRsaPem", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTrustChainEcdsaPem")
    def reset_trust_chain_ecdsa_pem(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrustChainEcdsaPem", []))

    @jsii.member(jsii_name="resetTrustChainRsaPem")
    def reset_trust_chain_rsa_pem(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrustChainRsaPem", []))

    @jsii.member(jsii_name="resetWaitForDeployment")
    def reset_wait_for_deployment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitForDeployment", []))

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
    def timeouts(self) -> "CpsUploadCertificateTimeoutsOutputReference":
        return typing.cast("CpsUploadCertificateTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="unacknowledgedWarnings")
    def unacknowledged_warnings(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "unacknowledgedWarnings"))

    @builtins.property
    @jsii.member(jsii_name="acknowledgeChangeManagementInput")
    def acknowledge_change_management_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "acknowledgeChangeManagementInput"))

    @builtins.property
    @jsii.member(jsii_name="acknowledgePostVerificationWarningsInput")
    def acknowledge_post_verification_warnings_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "acknowledgePostVerificationWarningsInput"))

    @builtins.property
    @jsii.member(jsii_name="autoApproveWarningsInput")
    def auto_approve_warnings_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "autoApproveWarningsInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateEcdsaPemInput")
    def certificate_ecdsa_pem_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateEcdsaPemInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateRsaPemInput")
    def certificate_rsa_pem_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateRsaPemInput"))

    @builtins.property
    @jsii.member(jsii_name="enrollmentIdInput")
    def enrollment_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "enrollmentIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(self) -> typing.Optional["CpsUploadCertificateTimeouts"]:
        return typing.cast(typing.Optional["CpsUploadCertificateTimeouts"], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="trustChainEcdsaPemInput")
    def trust_chain_ecdsa_pem_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "trustChainEcdsaPemInput"))

    @builtins.property
    @jsii.member(jsii_name="trustChainRsaPemInput")
    def trust_chain_rsa_pem_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "trustChainRsaPemInput"))

    @builtins.property
    @jsii.member(jsii_name="waitForDeploymentInput")
    def wait_for_deployment_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "waitForDeploymentInput"))

    @builtins.property
    @jsii.member(jsii_name="acknowledgeChangeManagement")
    def acknowledge_change_management(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "acknowledgeChangeManagement"))

    @acknowledge_change_management.setter
    def acknowledge_change_management(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07a10f825807fec4bfe645e624093bedb085d28ee32a6f5d11998fbe20747490)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acknowledgeChangeManagement", value)

    @builtins.property
    @jsii.member(jsii_name="acknowledgePostVerificationWarnings")
    def acknowledge_post_verification_warnings(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "acknowledgePostVerificationWarnings"))

    @acknowledge_post_verification_warnings.setter
    def acknowledge_post_verification_warnings(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb4e781961baff3f056319b9d484179dd2218d08200ea641bd88b21c24cee502)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acknowledgePostVerificationWarnings", value)

    @builtins.property
    @jsii.member(jsii_name="autoApproveWarnings")
    def auto_approve_warnings(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "autoApproveWarnings"))

    @auto_approve_warnings.setter
    def auto_approve_warnings(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef87fb7a6bd1482916dc219e4c4a1c5663f21c664cf1b5815ed75ff046a08618)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoApproveWarnings", value)

    @builtins.property
    @jsii.member(jsii_name="certificateEcdsaPem")
    def certificate_ecdsa_pem(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateEcdsaPem"))

    @certificate_ecdsa_pem.setter
    def certificate_ecdsa_pem(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2203845b503ad53b0b4429266e6eaae21b0a0c2238a6de1a5b9ca6591ee225f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateEcdsaPem", value)

    @builtins.property
    @jsii.member(jsii_name="certificateRsaPem")
    def certificate_rsa_pem(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateRsaPem"))

    @certificate_rsa_pem.setter
    def certificate_rsa_pem(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb23f727dafa55eebe80c982f85e2b37bc782cbfa64b307d75651b8a85561b50)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateRsaPem", value)

    @builtins.property
    @jsii.member(jsii_name="enrollmentId")
    def enrollment_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "enrollmentId"))

    @enrollment_id.setter
    def enrollment_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fedf6d58e46e7c811cd9d29986f7a0b1969354b02ff9ae24f5342aa9de83b17)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enrollmentId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9891aeaa10f491628918dbf625a0e12b4515575c783b93d9628f25024b137701)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="trustChainEcdsaPem")
    def trust_chain_ecdsa_pem(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "trustChainEcdsaPem"))

    @trust_chain_ecdsa_pem.setter
    def trust_chain_ecdsa_pem(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5907a4a7f5e2837f7051d9429d9282d993f8893cc683c025cf35db078a5bb178)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trustChainEcdsaPem", value)

    @builtins.property
    @jsii.member(jsii_name="trustChainRsaPem")
    def trust_chain_rsa_pem(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "trustChainRsaPem"))

    @trust_chain_rsa_pem.setter
    def trust_chain_rsa_pem(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3ed29c9db2fdb0755c1a0d5696c4122f1adf8c0a2333205a6fd06cc93b901ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trustChainRsaPem", value)

    @builtins.property
    @jsii.member(jsii_name="waitForDeployment")
    def wait_for_deployment(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "waitForDeployment"))

    @wait_for_deployment.setter
    def wait_for_deployment(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5761f3505fdfd8e547f26b8c98aed09f913ee6cf91a11eb2dc0b6e863c84939)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitForDeployment", value)


@jsii.data_type(
    jsii_type="akamai.cpsUploadCertificate.CpsUploadCertificateConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "enrollment_id": "enrollmentId",
        "acknowledge_change_management": "acknowledgeChangeManagement",
        "acknowledge_post_verification_warnings": "acknowledgePostVerificationWarnings",
        "auto_approve_warnings": "autoApproveWarnings",
        "certificate_ecdsa_pem": "certificateEcdsaPem",
        "certificate_rsa_pem": "certificateRsaPem",
        "id": "id",
        "timeouts": "timeouts",
        "trust_chain_ecdsa_pem": "trustChainEcdsaPem",
        "trust_chain_rsa_pem": "trustChainRsaPem",
        "wait_for_deployment": "waitForDeployment",
    },
)
class CpsUploadCertificateConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        enrollment_id: jsii.Number,
        acknowledge_change_management: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        acknowledge_post_verification_warnings: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        auto_approve_warnings: typing.Optional[typing.Sequence[builtins.str]] = None,
        certificate_ecdsa_pem: typing.Optional[builtins.str] = None,
        certificate_rsa_pem: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["CpsUploadCertificateTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        trust_chain_ecdsa_pem: typing.Optional[builtins.str] = None,
        trust_chain_rsa_pem: typing.Optional[builtins.str] = None,
        wait_for_deployment: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param enrollment_id: The unique identifier of the enrollment. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#enrollment_id CpsUploadCertificate#enrollment_id}
        :param acknowledge_change_management: Whether to acknowledge change management. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#acknowledge_change_management CpsUploadCertificate#acknowledge_change_management}
        :param acknowledge_post_verification_warnings: Whether to acknowledge post-verification warnings. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#acknowledge_post_verification_warnings CpsUploadCertificate#acknowledge_post_verification_warnings}
        :param auto_approve_warnings: List of post-verification warnings to be automatically acknowledged. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#auto_approve_warnings CpsUploadCertificate#auto_approve_warnings}
        :param certificate_ecdsa_pem: ECDSA certificate in pem format to be uploaded. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#certificate_ecdsa_pem CpsUploadCertificate#certificate_ecdsa_pem}
        :param certificate_rsa_pem: RSA certificate in pem format to be uploaded. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#certificate_rsa_pem CpsUploadCertificate#certificate_rsa_pem}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#id CpsUploadCertificate#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#timeouts CpsUploadCertificate#timeouts}
        :param trust_chain_ecdsa_pem: Trust chain in pem format for provided ECDSA certificate. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#trust_chain_ecdsa_pem CpsUploadCertificate#trust_chain_ecdsa_pem}
        :param trust_chain_rsa_pem: Trust chain in pem format for provided RSA certificate. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#trust_chain_rsa_pem CpsUploadCertificate#trust_chain_rsa_pem}
        :param wait_for_deployment: Whether to wait for certificate to be deployed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#wait_for_deployment CpsUploadCertificate#wait_for_deployment}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = CpsUploadCertificateTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77fdd7b4f6a83ade55bc198838a4d597c088b4a86c80b6506e9a95cca8a0a255)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument enrollment_id", value=enrollment_id, expected_type=type_hints["enrollment_id"])
            check_type(argname="argument acknowledge_change_management", value=acknowledge_change_management, expected_type=type_hints["acknowledge_change_management"])
            check_type(argname="argument acknowledge_post_verification_warnings", value=acknowledge_post_verification_warnings, expected_type=type_hints["acknowledge_post_verification_warnings"])
            check_type(argname="argument auto_approve_warnings", value=auto_approve_warnings, expected_type=type_hints["auto_approve_warnings"])
            check_type(argname="argument certificate_ecdsa_pem", value=certificate_ecdsa_pem, expected_type=type_hints["certificate_ecdsa_pem"])
            check_type(argname="argument certificate_rsa_pem", value=certificate_rsa_pem, expected_type=type_hints["certificate_rsa_pem"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument trust_chain_ecdsa_pem", value=trust_chain_ecdsa_pem, expected_type=type_hints["trust_chain_ecdsa_pem"])
            check_type(argname="argument trust_chain_rsa_pem", value=trust_chain_rsa_pem, expected_type=type_hints["trust_chain_rsa_pem"])
            check_type(argname="argument wait_for_deployment", value=wait_for_deployment, expected_type=type_hints["wait_for_deployment"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enrollment_id": enrollment_id,
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
        if acknowledge_change_management is not None:
            self._values["acknowledge_change_management"] = acknowledge_change_management
        if acknowledge_post_verification_warnings is not None:
            self._values["acknowledge_post_verification_warnings"] = acknowledge_post_verification_warnings
        if auto_approve_warnings is not None:
            self._values["auto_approve_warnings"] = auto_approve_warnings
        if certificate_ecdsa_pem is not None:
            self._values["certificate_ecdsa_pem"] = certificate_ecdsa_pem
        if certificate_rsa_pem is not None:
            self._values["certificate_rsa_pem"] = certificate_rsa_pem
        if id is not None:
            self._values["id"] = id
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if trust_chain_ecdsa_pem is not None:
            self._values["trust_chain_ecdsa_pem"] = trust_chain_ecdsa_pem
        if trust_chain_rsa_pem is not None:
            self._values["trust_chain_rsa_pem"] = trust_chain_rsa_pem
        if wait_for_deployment is not None:
            self._values["wait_for_deployment"] = wait_for_deployment

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
    def enrollment_id(self) -> jsii.Number:
        '''The unique identifier of the enrollment.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#enrollment_id CpsUploadCertificate#enrollment_id}
        '''
        result = self._values.get("enrollment_id")
        assert result is not None, "Required property 'enrollment_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def acknowledge_change_management(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to acknowledge change management.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#acknowledge_change_management CpsUploadCertificate#acknowledge_change_management}
        '''
        result = self._values.get("acknowledge_change_management")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def acknowledge_post_verification_warnings(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to acknowledge post-verification warnings.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#acknowledge_post_verification_warnings CpsUploadCertificate#acknowledge_post_verification_warnings}
        '''
        result = self._values.get("acknowledge_post_verification_warnings")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def auto_approve_warnings(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of post-verification warnings to be automatically acknowledged.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#auto_approve_warnings CpsUploadCertificate#auto_approve_warnings}
        '''
        result = self._values.get("auto_approve_warnings")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def certificate_ecdsa_pem(self) -> typing.Optional[builtins.str]:
        '''ECDSA certificate in pem format to be uploaded.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#certificate_ecdsa_pem CpsUploadCertificate#certificate_ecdsa_pem}
        '''
        result = self._values.get("certificate_ecdsa_pem")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_rsa_pem(self) -> typing.Optional[builtins.str]:
        '''RSA certificate in pem format to be uploaded.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#certificate_rsa_pem CpsUploadCertificate#certificate_rsa_pem}
        '''
        result = self._values.get("certificate_rsa_pem")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#id CpsUploadCertificate#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["CpsUploadCertificateTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#timeouts CpsUploadCertificate#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["CpsUploadCertificateTimeouts"], result)

    @builtins.property
    def trust_chain_ecdsa_pem(self) -> typing.Optional[builtins.str]:
        '''Trust chain in pem format for provided ECDSA certificate.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#trust_chain_ecdsa_pem CpsUploadCertificate#trust_chain_ecdsa_pem}
        '''
        result = self._values.get("trust_chain_ecdsa_pem")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def trust_chain_rsa_pem(self) -> typing.Optional[builtins.str]:
        '''Trust chain in pem format for provided RSA certificate.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#trust_chain_rsa_pem CpsUploadCertificate#trust_chain_rsa_pem}
        '''
        result = self._values.get("trust_chain_rsa_pem")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wait_for_deployment(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to wait for certificate to be deployed.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#wait_for_deployment CpsUploadCertificate#wait_for_deployment}
        '''
        result = self._values.get("wait_for_deployment")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CpsUploadCertificateConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.cpsUploadCertificate.CpsUploadCertificateTimeouts",
    jsii_struct_bases=[],
    name_mapping={"default": "default"},
)
class CpsUploadCertificateTimeouts:
    def __init__(self, *, default: typing.Optional[builtins.str] = None) -> None:
        '''
        :param default: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#default CpsUploadCertificate#default}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a9702a9d53a049076a8fe43aab7c2e1da50f6ab212cc1dda5907a9b069c542a)
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if default is not None:
            self._values["default"] = default

    @builtins.property
    def default(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_upload_certificate#default CpsUploadCertificate#default}.'''
        result = self._values.get("default")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CpsUploadCertificateTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CpsUploadCertificateTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.cpsUploadCertificate.CpsUploadCertificateTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a17762b49f8da72ca3ce6d6095a99ee4a5df7ed96c6dee03cdec8d76bf85af24)
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
            type_hints = typing.get_type_hints(_typecheckingstub__49b212c51e3f30d582c206431abfa95ade25c82c641dcf9352d93efaafa2503d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CpsUploadCertificateTimeouts]:
        return typing.cast(typing.Optional[CpsUploadCertificateTimeouts], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CpsUploadCertificateTimeouts],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0dc87c519d04a78a10e3a9d73e73136d3cd6f4b078185f97a761b9e873716ad1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CpsUploadCertificate",
    "CpsUploadCertificateConfig",
    "CpsUploadCertificateTimeouts",
    "CpsUploadCertificateTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__b16a989fd507f41f4e47c71952085679774005252c6cb584d5c64a3caa580918(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    enrollment_id: jsii.Number,
    acknowledge_change_management: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    acknowledge_post_verification_warnings: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    auto_approve_warnings: typing.Optional[typing.Sequence[builtins.str]] = None,
    certificate_ecdsa_pem: typing.Optional[builtins.str] = None,
    certificate_rsa_pem: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[CpsUploadCertificateTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    trust_chain_ecdsa_pem: typing.Optional[builtins.str] = None,
    trust_chain_rsa_pem: typing.Optional[builtins.str] = None,
    wait_for_deployment: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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

def _typecheckingstub__7ca8d12b5aaae5e6b08a7951639dd19652d6bda94c62be0a4ece1e57441bd085(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07a10f825807fec4bfe645e624093bedb085d28ee32a6f5d11998fbe20747490(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb4e781961baff3f056319b9d484179dd2218d08200ea641bd88b21c24cee502(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef87fb7a6bd1482916dc219e4c4a1c5663f21c664cf1b5815ed75ff046a08618(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2203845b503ad53b0b4429266e6eaae21b0a0c2238a6de1a5b9ca6591ee225f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb23f727dafa55eebe80c982f85e2b37bc782cbfa64b307d75651b8a85561b50(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fedf6d58e46e7c811cd9d29986f7a0b1969354b02ff9ae24f5342aa9de83b17(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9891aeaa10f491628918dbf625a0e12b4515575c783b93d9628f25024b137701(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5907a4a7f5e2837f7051d9429d9282d993f8893cc683c025cf35db078a5bb178(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3ed29c9db2fdb0755c1a0d5696c4122f1adf8c0a2333205a6fd06cc93b901ca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5761f3505fdfd8e547f26b8c98aed09f913ee6cf91a11eb2dc0b6e863c84939(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77fdd7b4f6a83ade55bc198838a4d597c088b4a86c80b6506e9a95cca8a0a255(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    enrollment_id: jsii.Number,
    acknowledge_change_management: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    acknowledge_post_verification_warnings: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    auto_approve_warnings: typing.Optional[typing.Sequence[builtins.str]] = None,
    certificate_ecdsa_pem: typing.Optional[builtins.str] = None,
    certificate_rsa_pem: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[CpsUploadCertificateTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    trust_chain_ecdsa_pem: typing.Optional[builtins.str] = None,
    trust_chain_rsa_pem: typing.Optional[builtins.str] = None,
    wait_for_deployment: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a9702a9d53a049076a8fe43aab7c2e1da50f6ab212cc1dda5907a9b069c542a(
    *,
    default: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a17762b49f8da72ca3ce6d6095a99ee4a5df7ed96c6dee03cdec8d76bf85af24(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49b212c51e3f30d582c206431abfa95ade25c82c641dcf9352d93efaafa2503d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dc87c519d04a78a10e3a9d73e73136d3cd6f4b078185f97a761b9e873716ad1(
    value: typing.Optional[CpsUploadCertificateTimeouts],
) -> None:
    """Type checking stubs"""
    pass
