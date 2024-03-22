'''
# `akamai_cps_dv_enrollment`

Refer to the Terraform Registry for docs: [`akamai_cps_dv_enrollment`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment).
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


class CpsDvEnrollment(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.cpsDvEnrollment.CpsDvEnrollment",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment akamai_cps_dv_enrollment}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        admin_contact: typing.Union["CpsDvEnrollmentAdminContact", typing.Dict[builtins.str, typing.Any]],
        common_name: builtins.str,
        contract_id: builtins.str,
        csr: typing.Union["CpsDvEnrollmentCsr", typing.Dict[builtins.str, typing.Any]],
        network_configuration: typing.Union["CpsDvEnrollmentNetworkConfiguration", typing.Dict[builtins.str, typing.Any]],
        organization: typing.Union["CpsDvEnrollmentOrganization", typing.Dict[builtins.str, typing.Any]],
        secure_network: builtins.str,
        signature_algorithm: builtins.str,
        sni_only: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        tech_contact: typing.Union["CpsDvEnrollmentTechContact", typing.Dict[builtins.str, typing.Any]],
        acknowledge_pre_verification_warnings: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        allow_duplicate_common_name: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        certificate_chain_type: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        sans: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["CpsDvEnrollmentTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment akamai_cps_dv_enrollment} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param admin_contact: admin_contact block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#admin_contact CpsDvEnrollment#admin_contact}
        :param common_name: Common name used for enrollment. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#common_name CpsDvEnrollment#common_name}
        :param contract_id: Contract ID for which enrollment is retrieved. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#contract_id CpsDvEnrollment#contract_id}
        :param csr: csr block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#csr CpsDvEnrollment#csr}
        :param network_configuration: network_configuration block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#network_configuration CpsDvEnrollment#network_configuration}
        :param organization: organization block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#organization CpsDvEnrollment#organization}
        :param secure_network: Type of TLS deployment network. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#secure_network CpsDvEnrollment#secure_network}
        :param signature_algorithm: SHA algorithm type. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#signature_algorithm CpsDvEnrollment#signature_algorithm}
        :param sni_only: Whether Server Name Indication is used for enrollment. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#sni_only CpsDvEnrollment#sni_only}
        :param tech_contact: tech_contact block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#tech_contact CpsDvEnrollment#tech_contact}
        :param acknowledge_pre_verification_warnings: Whether acknowledge warnings before certificate verification. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#acknowledge_pre_verification_warnings CpsDvEnrollment#acknowledge_pre_verification_warnings}
        :param allow_duplicate_common_name: Allow to duplicate common name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#allow_duplicate_common_name CpsDvEnrollment#allow_duplicate_common_name}
        :param certificate_chain_type: Certificate trust chain type. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#certificate_chain_type CpsDvEnrollment#certificate_chain_type}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#id CpsDvEnrollment#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param sans: List of SANs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#sans CpsDvEnrollment#sans}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#timeouts CpsDvEnrollment#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d47d3b6066213b12181792744ba72c90f0bb0f519f95fb7d4495f47e40c14067)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CpsDvEnrollmentConfig(
            admin_contact=admin_contact,
            common_name=common_name,
            contract_id=contract_id,
            csr=csr,
            network_configuration=network_configuration,
            organization=organization,
            secure_network=secure_network,
            signature_algorithm=signature_algorithm,
            sni_only=sni_only,
            tech_contact=tech_contact,
            acknowledge_pre_verification_warnings=acknowledge_pre_verification_warnings,
            allow_duplicate_common_name=allow_duplicate_common_name,
            certificate_chain_type=certificate_chain_type,
            id=id,
            sans=sans,
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
        '''Generates CDKTF code for importing a CpsDvEnrollment resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the CpsDvEnrollment to import.
        :param import_from_id: The id of the existing CpsDvEnrollment that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the CpsDvEnrollment to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0d651d10022e22f0156895e6cf4e5405cfe0056513e0793f4c3ebb022bab88d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putAdminContact")
    def put_admin_contact(
        self,
        *,
        address_line_one: builtins.str,
        city: builtins.str,
        country_code: builtins.str,
        email: builtins.str,
        first_name: builtins.str,
        last_name: builtins.str,
        organization: builtins.str,
        phone: builtins.str,
        postal_code: builtins.str,
        region: builtins.str,
        address_line_two: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param address_line_one: The address of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#address_line_one CpsDvEnrollment#address_line_one}
        :param city: City of residence of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#city CpsDvEnrollment#city}
        :param country_code: Country code of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#country_code CpsDvEnrollment#country_code}
        :param email: E-mail address of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#email CpsDvEnrollment#email}
        :param first_name: First name of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#first_name CpsDvEnrollment#first_name}
        :param last_name: Last name of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#last_name CpsDvEnrollment#last_name}
        :param organization: Organization where contact is hired. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#organization CpsDvEnrollment#organization}
        :param phone: Phone number of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#phone CpsDvEnrollment#phone}
        :param postal_code: Postal code of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#postal_code CpsDvEnrollment#postal_code}
        :param region: The region of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#region CpsDvEnrollment#region}
        :param address_line_two: The address of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#address_line_two CpsDvEnrollment#address_line_two}
        :param title: Title of the the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#title CpsDvEnrollment#title}
        '''
        value = CpsDvEnrollmentAdminContact(
            address_line_one=address_line_one,
            city=city,
            country_code=country_code,
            email=email,
            first_name=first_name,
            last_name=last_name,
            organization=organization,
            phone=phone,
            postal_code=postal_code,
            region=region,
            address_line_two=address_line_two,
            title=title,
        )

        return typing.cast(None, jsii.invoke(self, "putAdminContact", [value]))

    @jsii.member(jsii_name="putCsr")
    def put_csr(
        self,
        *,
        city: builtins.str,
        country_code: builtins.str,
        organization: builtins.str,
        organizational_unit: typing.Optional[builtins.str] = None,
        preferred_trust_chain: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param city: City where organization is located. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#city CpsDvEnrollment#city}
        :param country_code: The code of the country where organization is located. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#country_code CpsDvEnrollment#country_code}
        :param organization: Name of organization used in all legal documents. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#organization CpsDvEnrollment#organization}
        :param organizational_unit: Organizational unit of organization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#organizational_unit CpsDvEnrollment#organizational_unit}
        :param preferred_trust_chain: For the Let's Encrypt Domain Validated (DV) SAN certificates, the preferred trust chain will be included by CPS with the leaf certificate in the TLS handshake. If the field does not have a value, whichever trust chain Akamai chooses will be used by default Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#preferred_trust_chain CpsDvEnrollment#preferred_trust_chain}
        :param state: State or province of organization location. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#state CpsDvEnrollment#state}
        '''
        value = CpsDvEnrollmentCsr(
            city=city,
            country_code=country_code,
            organization=organization,
            organizational_unit=organizational_unit,
            preferred_trust_chain=preferred_trust_chain,
            state=state,
        )

        return typing.cast(None, jsii.invoke(self, "putCsr", [value]))

    @jsii.member(jsii_name="putNetworkConfiguration")
    def put_network_configuration(
        self,
        *,
        geography: builtins.str,
        client_mutual_authentication: typing.Optional[typing.Union["CpsDvEnrollmentNetworkConfigurationClientMutualAuthentication", typing.Dict[builtins.str, typing.Any]]] = None,
        clone_dns_names: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        disallowed_tls_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
        must_have_ciphers: typing.Optional[builtins.str] = None,
        ocsp_stapling: typing.Optional[builtins.str] = None,
        preferred_ciphers: typing.Optional[builtins.str] = None,
        quic_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param geography: Geography type used for enrollment. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#geography CpsDvEnrollment#geography}
        :param client_mutual_authentication: client_mutual_authentication block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#client_mutual_authentication CpsDvEnrollment#client_mutual_authentication}
        :param clone_dns_names: Enable CPS to direct traffic using all the SANs listed in the SANs parameter when enrollment is created. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#clone_dns_names CpsDvEnrollment#clone_dns_names}
        :param disallowed_tls_versions: TLS versions which are disallowed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#disallowed_tls_versions CpsDvEnrollment#disallowed_tls_versions}
        :param must_have_ciphers: Mandatory Ciphers which are included for enrollment. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#must_have_ciphers CpsDvEnrollment#must_have_ciphers}
        :param ocsp_stapling: Enable OCSP stapling. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#ocsp_stapling CpsDvEnrollment#ocsp_stapling}
        :param preferred_ciphers: Preferred Ciphers which are included for enrollment. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#preferred_ciphers CpsDvEnrollment#preferred_ciphers}
        :param quic_enabled: Enable QUIC protocol. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#quic_enabled CpsDvEnrollment#quic_enabled}
        '''
        value = CpsDvEnrollmentNetworkConfiguration(
            geography=geography,
            client_mutual_authentication=client_mutual_authentication,
            clone_dns_names=clone_dns_names,
            disallowed_tls_versions=disallowed_tls_versions,
            must_have_ciphers=must_have_ciphers,
            ocsp_stapling=ocsp_stapling,
            preferred_ciphers=preferred_ciphers,
            quic_enabled=quic_enabled,
        )

        return typing.cast(None, jsii.invoke(self, "putNetworkConfiguration", [value]))

    @jsii.member(jsii_name="putOrganization")
    def put_organization(
        self,
        *,
        address_line_one: builtins.str,
        city: builtins.str,
        country_code: builtins.str,
        name: builtins.str,
        phone: builtins.str,
        postal_code: builtins.str,
        region: builtins.str,
        address_line_two: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param address_line_one: The address of organization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#address_line_one CpsDvEnrollment#address_line_one}
        :param city: City of organization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#city CpsDvEnrollment#city}
        :param country_code: Country code of organization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#country_code CpsDvEnrollment#country_code}
        :param name: Name of organization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#name CpsDvEnrollment#name}
        :param phone: Phone number of organization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#phone CpsDvEnrollment#phone}
        :param postal_code: Postal code of organization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#postal_code CpsDvEnrollment#postal_code}
        :param region: The region of organization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#region CpsDvEnrollment#region}
        :param address_line_two: The address of organization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#address_line_two CpsDvEnrollment#address_line_two}
        '''
        value = CpsDvEnrollmentOrganization(
            address_line_one=address_line_one,
            city=city,
            country_code=country_code,
            name=name,
            phone=phone,
            postal_code=postal_code,
            region=region,
            address_line_two=address_line_two,
        )

        return typing.cast(None, jsii.invoke(self, "putOrganization", [value]))

    @jsii.member(jsii_name="putTechContact")
    def put_tech_contact(
        self,
        *,
        address_line_one: builtins.str,
        city: builtins.str,
        country_code: builtins.str,
        email: builtins.str,
        first_name: builtins.str,
        last_name: builtins.str,
        organization: builtins.str,
        phone: builtins.str,
        postal_code: builtins.str,
        region: builtins.str,
        address_line_two: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param address_line_one: The address of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#address_line_one CpsDvEnrollment#address_line_one}
        :param city: City of residence of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#city CpsDvEnrollment#city}
        :param country_code: Country code of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#country_code CpsDvEnrollment#country_code}
        :param email: E-mail address of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#email CpsDvEnrollment#email}
        :param first_name: First name of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#first_name CpsDvEnrollment#first_name}
        :param last_name: Last name of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#last_name CpsDvEnrollment#last_name}
        :param organization: Organization where contact is hired. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#organization CpsDvEnrollment#organization}
        :param phone: Phone number of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#phone CpsDvEnrollment#phone}
        :param postal_code: Postal code of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#postal_code CpsDvEnrollment#postal_code}
        :param region: The region of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#region CpsDvEnrollment#region}
        :param address_line_two: The address of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#address_line_two CpsDvEnrollment#address_line_two}
        :param title: Title of the the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#title CpsDvEnrollment#title}
        '''
        value = CpsDvEnrollmentTechContact(
            address_line_one=address_line_one,
            city=city,
            country_code=country_code,
            email=email,
            first_name=first_name,
            last_name=last_name,
            organization=organization,
            phone=phone,
            postal_code=postal_code,
            region=region,
            address_line_two=address_line_two,
            title=title,
        )

        return typing.cast(None, jsii.invoke(self, "putTechContact", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self, *, default: typing.Optional[builtins.str] = None) -> None:
        '''
        :param default: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#default CpsDvEnrollment#default}.
        '''
        value = CpsDvEnrollmentTimeouts(default=default)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAcknowledgePreVerificationWarnings")
    def reset_acknowledge_pre_verification_warnings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcknowledgePreVerificationWarnings", []))

    @jsii.member(jsii_name="resetAllowDuplicateCommonName")
    def reset_allow_duplicate_common_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowDuplicateCommonName", []))

    @jsii.member(jsii_name="resetCertificateChainType")
    def reset_certificate_chain_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateChainType", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSans")
    def reset_sans(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSans", []))

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
    @jsii.member(jsii_name="adminContact")
    def admin_contact(self) -> "CpsDvEnrollmentAdminContactOutputReference":
        return typing.cast("CpsDvEnrollmentAdminContactOutputReference", jsii.get(self, "adminContact"))

    @builtins.property
    @jsii.member(jsii_name="certificateType")
    def certificate_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateType"))

    @builtins.property
    @jsii.member(jsii_name="csr")
    def csr(self) -> "CpsDvEnrollmentCsrOutputReference":
        return typing.cast("CpsDvEnrollmentCsrOutputReference", jsii.get(self, "csr"))

    @builtins.property
    @jsii.member(jsii_name="dnsChallenges")
    def dns_challenges(self) -> "CpsDvEnrollmentDnsChallengesList":
        return typing.cast("CpsDvEnrollmentDnsChallengesList", jsii.get(self, "dnsChallenges"))

    @builtins.property
    @jsii.member(jsii_name="httpChallenges")
    def http_challenges(self) -> "CpsDvEnrollmentHttpChallengesList":
        return typing.cast("CpsDvEnrollmentHttpChallengesList", jsii.get(self, "httpChallenges"))

    @builtins.property
    @jsii.member(jsii_name="networkConfiguration")
    def network_configuration(
        self,
    ) -> "CpsDvEnrollmentNetworkConfigurationOutputReference":
        return typing.cast("CpsDvEnrollmentNetworkConfigurationOutputReference", jsii.get(self, "networkConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="organization")
    def organization(self) -> "CpsDvEnrollmentOrganizationOutputReference":
        return typing.cast("CpsDvEnrollmentOrganizationOutputReference", jsii.get(self, "organization"))

    @builtins.property
    @jsii.member(jsii_name="registrationAuthority")
    def registration_authority(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "registrationAuthority"))

    @builtins.property
    @jsii.member(jsii_name="techContact")
    def tech_contact(self) -> "CpsDvEnrollmentTechContactOutputReference":
        return typing.cast("CpsDvEnrollmentTechContactOutputReference", jsii.get(self, "techContact"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "CpsDvEnrollmentTimeoutsOutputReference":
        return typing.cast("CpsDvEnrollmentTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="validationType")
    def validation_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "validationType"))

    @builtins.property
    @jsii.member(jsii_name="acknowledgePreVerificationWarningsInput")
    def acknowledge_pre_verification_warnings_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "acknowledgePreVerificationWarningsInput"))

    @builtins.property
    @jsii.member(jsii_name="adminContactInput")
    def admin_contact_input(self) -> typing.Optional["CpsDvEnrollmentAdminContact"]:
        return typing.cast(typing.Optional["CpsDvEnrollmentAdminContact"], jsii.get(self, "adminContactInput"))

    @builtins.property
    @jsii.member(jsii_name="allowDuplicateCommonNameInput")
    def allow_duplicate_common_name_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allowDuplicateCommonNameInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateChainTypeInput")
    def certificate_chain_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateChainTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="commonNameInput")
    def common_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commonNameInput"))

    @builtins.property
    @jsii.member(jsii_name="contractIdInput")
    def contract_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contractIdInput"))

    @builtins.property
    @jsii.member(jsii_name="csrInput")
    def csr_input(self) -> typing.Optional["CpsDvEnrollmentCsr"]:
        return typing.cast(typing.Optional["CpsDvEnrollmentCsr"], jsii.get(self, "csrInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="networkConfigurationInput")
    def network_configuration_input(
        self,
    ) -> typing.Optional["CpsDvEnrollmentNetworkConfiguration"]:
        return typing.cast(typing.Optional["CpsDvEnrollmentNetworkConfiguration"], jsii.get(self, "networkConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="organizationInput")
    def organization_input(self) -> typing.Optional["CpsDvEnrollmentOrganization"]:
        return typing.cast(typing.Optional["CpsDvEnrollmentOrganization"], jsii.get(self, "organizationInput"))

    @builtins.property
    @jsii.member(jsii_name="sansInput")
    def sans_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sansInput"))

    @builtins.property
    @jsii.member(jsii_name="secureNetworkInput")
    def secure_network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secureNetworkInput"))

    @builtins.property
    @jsii.member(jsii_name="signatureAlgorithmInput")
    def signature_algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "signatureAlgorithmInput"))

    @builtins.property
    @jsii.member(jsii_name="sniOnlyInput")
    def sni_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "sniOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="techContactInput")
    def tech_contact_input(self) -> typing.Optional["CpsDvEnrollmentTechContact"]:
        return typing.cast(typing.Optional["CpsDvEnrollmentTechContact"], jsii.get(self, "techContactInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(self) -> typing.Optional["CpsDvEnrollmentTimeouts"]:
        return typing.cast(typing.Optional["CpsDvEnrollmentTimeouts"], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="acknowledgePreVerificationWarnings")
    def acknowledge_pre_verification_warnings(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "acknowledgePreVerificationWarnings"))

    @acknowledge_pre_verification_warnings.setter
    def acknowledge_pre_verification_warnings(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5cac497d9172511b27cfea5c94a2059f39c33f52d5357753a7ea0d68629ad794)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acknowledgePreVerificationWarnings", value)

    @builtins.property
    @jsii.member(jsii_name="allowDuplicateCommonName")
    def allow_duplicate_common_name(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "allowDuplicateCommonName"))

    @allow_duplicate_common_name.setter
    def allow_duplicate_common_name(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77bd5c980456140e7ba871a827dddebd394fe5a580f1425da9bd09bb392e0c4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowDuplicateCommonName", value)

    @builtins.property
    @jsii.member(jsii_name="certificateChainType")
    def certificate_chain_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateChainType"))

    @certificate_chain_type.setter
    def certificate_chain_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4251bdedfa9850942471d76588481bad48779a3a7f6a5e785e6d8044c927191)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateChainType", value)

    @builtins.property
    @jsii.member(jsii_name="commonName")
    def common_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "commonName"))

    @common_name.setter
    def common_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e22ac9d74350257827c64b2c35f2285c0baecb9adb0c272f70f8d148bb4e973)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commonName", value)

    @builtins.property
    @jsii.member(jsii_name="contractId")
    def contract_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contractId"))

    @contract_id.setter
    def contract_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__879ca8bb06fc39afdffc5866e20a9e9b6fa2b423305b5862b27667eea6a75740)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contractId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d862d6f96a6ce9653e57e874782f162405f2bb32c4fbd33fc48d7201744db1d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="sans")
    def sans(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sans"))

    @sans.setter
    def sans(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c9594f01a884375305573c8816443c638e4ae6e4c0d3b455858d394a9244cba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sans", value)

    @builtins.property
    @jsii.member(jsii_name="secureNetwork")
    def secure_network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secureNetwork"))

    @secure_network.setter
    def secure_network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da77a9499c3f0fdc0ab00d019333c282f7e37ef44c68a09e54b58ed02261a022)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secureNetwork", value)

    @builtins.property
    @jsii.member(jsii_name="signatureAlgorithm")
    def signature_algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signatureAlgorithm"))

    @signature_algorithm.setter
    def signature_algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90909a6cbf31717cbc4eb0bb55bc04cf3eeea01379b4461f9c496d2199a1c158)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signatureAlgorithm", value)

    @builtins.property
    @jsii.member(jsii_name="sniOnly")
    def sni_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "sniOnly"))

    @sni_only.setter
    def sni_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a47dbc0f0fe5bfdb814954d39df376664598a6ae4c51a4b4c5ae26cb15eafb21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sniOnly", value)


@jsii.data_type(
    jsii_type="akamai.cpsDvEnrollment.CpsDvEnrollmentAdminContact",
    jsii_struct_bases=[],
    name_mapping={
        "address_line_one": "addressLineOne",
        "city": "city",
        "country_code": "countryCode",
        "email": "email",
        "first_name": "firstName",
        "last_name": "lastName",
        "organization": "organization",
        "phone": "phone",
        "postal_code": "postalCode",
        "region": "region",
        "address_line_two": "addressLineTwo",
        "title": "title",
    },
)
class CpsDvEnrollmentAdminContact:
    def __init__(
        self,
        *,
        address_line_one: builtins.str,
        city: builtins.str,
        country_code: builtins.str,
        email: builtins.str,
        first_name: builtins.str,
        last_name: builtins.str,
        organization: builtins.str,
        phone: builtins.str,
        postal_code: builtins.str,
        region: builtins.str,
        address_line_two: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param address_line_one: The address of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#address_line_one CpsDvEnrollment#address_line_one}
        :param city: City of residence of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#city CpsDvEnrollment#city}
        :param country_code: Country code of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#country_code CpsDvEnrollment#country_code}
        :param email: E-mail address of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#email CpsDvEnrollment#email}
        :param first_name: First name of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#first_name CpsDvEnrollment#first_name}
        :param last_name: Last name of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#last_name CpsDvEnrollment#last_name}
        :param organization: Organization where contact is hired. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#organization CpsDvEnrollment#organization}
        :param phone: Phone number of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#phone CpsDvEnrollment#phone}
        :param postal_code: Postal code of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#postal_code CpsDvEnrollment#postal_code}
        :param region: The region of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#region CpsDvEnrollment#region}
        :param address_line_two: The address of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#address_line_two CpsDvEnrollment#address_line_two}
        :param title: Title of the the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#title CpsDvEnrollment#title}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f99049bc84f189a97341b3bbf868c8293c4d528ed225ceae13869682cc88932)
            check_type(argname="argument address_line_one", value=address_line_one, expected_type=type_hints["address_line_one"])
            check_type(argname="argument city", value=city, expected_type=type_hints["city"])
            check_type(argname="argument country_code", value=country_code, expected_type=type_hints["country_code"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument first_name", value=first_name, expected_type=type_hints["first_name"])
            check_type(argname="argument last_name", value=last_name, expected_type=type_hints["last_name"])
            check_type(argname="argument organization", value=organization, expected_type=type_hints["organization"])
            check_type(argname="argument phone", value=phone, expected_type=type_hints["phone"])
            check_type(argname="argument postal_code", value=postal_code, expected_type=type_hints["postal_code"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument address_line_two", value=address_line_two, expected_type=type_hints["address_line_two"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "address_line_one": address_line_one,
            "city": city,
            "country_code": country_code,
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "organization": organization,
            "phone": phone,
            "postal_code": postal_code,
            "region": region,
        }
        if address_line_two is not None:
            self._values["address_line_two"] = address_line_two
        if title is not None:
            self._values["title"] = title

    @builtins.property
    def address_line_one(self) -> builtins.str:
        '''The address of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#address_line_one CpsDvEnrollment#address_line_one}
        '''
        result = self._values.get("address_line_one")
        assert result is not None, "Required property 'address_line_one' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def city(self) -> builtins.str:
        '''City of residence of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#city CpsDvEnrollment#city}
        '''
        result = self._values.get("city")
        assert result is not None, "Required property 'city' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def country_code(self) -> builtins.str:
        '''Country code of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#country_code CpsDvEnrollment#country_code}
        '''
        result = self._values.get("country_code")
        assert result is not None, "Required property 'country_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def email(self) -> builtins.str:
        '''E-mail address of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#email CpsDvEnrollment#email}
        '''
        result = self._values.get("email")
        assert result is not None, "Required property 'email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def first_name(self) -> builtins.str:
        '''First name of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#first_name CpsDvEnrollment#first_name}
        '''
        result = self._values.get("first_name")
        assert result is not None, "Required property 'first_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def last_name(self) -> builtins.str:
        '''Last name of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#last_name CpsDvEnrollment#last_name}
        '''
        result = self._values.get("last_name")
        assert result is not None, "Required property 'last_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def organization(self) -> builtins.str:
        '''Organization where contact is hired.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#organization CpsDvEnrollment#organization}
        '''
        result = self._values.get("organization")
        assert result is not None, "Required property 'organization' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def phone(self) -> builtins.str:
        '''Phone number of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#phone CpsDvEnrollment#phone}
        '''
        result = self._values.get("phone")
        assert result is not None, "Required property 'phone' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def postal_code(self) -> builtins.str:
        '''Postal code of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#postal_code CpsDvEnrollment#postal_code}
        '''
        result = self._values.get("postal_code")
        assert result is not None, "Required property 'postal_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''The region of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#region CpsDvEnrollment#region}
        '''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def address_line_two(self) -> typing.Optional[builtins.str]:
        '''The address of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#address_line_two CpsDvEnrollment#address_line_two}
        '''
        result = self._values.get("address_line_two")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''Title of the the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#title CpsDvEnrollment#title}
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CpsDvEnrollmentAdminContact(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CpsDvEnrollmentAdminContactOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.cpsDvEnrollment.CpsDvEnrollmentAdminContactOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0c9183388eda36dc59b73d9c48995f7cfe9aaaf946a38c47701cb027529b623a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAddressLineTwo")
    def reset_address_line_two(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddressLineTwo", []))

    @jsii.member(jsii_name="resetTitle")
    def reset_title(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTitle", []))

    @builtins.property
    @jsii.member(jsii_name="addressLineOneInput")
    def address_line_one_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressLineOneInput"))

    @builtins.property
    @jsii.member(jsii_name="addressLineTwoInput")
    def address_line_two_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressLineTwoInput"))

    @builtins.property
    @jsii.member(jsii_name="cityInput")
    def city_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cityInput"))

    @builtins.property
    @jsii.member(jsii_name="countryCodeInput")
    def country_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "countryCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="firstNameInput")
    def first_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firstNameInput"))

    @builtins.property
    @jsii.member(jsii_name="lastNameInput")
    def last_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lastNameInput"))

    @builtins.property
    @jsii.member(jsii_name="organizationInput")
    def organization_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "organizationInput"))

    @builtins.property
    @jsii.member(jsii_name="phoneInput")
    def phone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "phoneInput"))

    @builtins.property
    @jsii.member(jsii_name="postalCodeInput")
    def postal_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "postalCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="addressLineOne")
    def address_line_one(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "addressLineOne"))

    @address_line_one.setter
    def address_line_one(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d878036b968fae26a745d2aa6da34934ac7543a93ad4c434682d348e74c25834)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addressLineOne", value)

    @builtins.property
    @jsii.member(jsii_name="addressLineTwo")
    def address_line_two(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "addressLineTwo"))

    @address_line_two.setter
    def address_line_two(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97db2bfb735e09c10d5cbff20adea6189884a7b2586329f5476b3e8b56e31f65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addressLineTwo", value)

    @builtins.property
    @jsii.member(jsii_name="city")
    def city(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "city"))

    @city.setter
    def city(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c519ed4cc2be46e1ceae5efd695de347ac1f987a4f21d2152c6431521b2ef33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "city", value)

    @builtins.property
    @jsii.member(jsii_name="countryCode")
    def country_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "countryCode"))

    @country_code.setter
    def country_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__661f3e15dceffb1e22bb037ba1a131f3043d4d2ff441021fcf66c430154cc737)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "countryCode", value)

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @email.setter
    def email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61464cc3cab4a6ac39abe6ccb555d72922dab378c3a8e7b4a477de686923d5a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="firstName")
    def first_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firstName"))

    @first_name.setter
    def first_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ef090d6d2aae6a2060960a3da991ef44b5ad218a5a34f0731fa281f18282cc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firstName", value)

    @builtins.property
    @jsii.member(jsii_name="lastName")
    def last_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastName"))

    @last_name.setter
    def last_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b2f9ad6ff7e0608751e19f9d976fd91f2bdf85e2babae4998522da64591ce61)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lastName", value)

    @builtins.property
    @jsii.member(jsii_name="organization")
    def organization(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organization"))

    @organization.setter
    def organization(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2266c0cbdd0bd5f66ee73018d06a2445722de80ff2873e5f2e34fca0bc107705)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organization", value)

    @builtins.property
    @jsii.member(jsii_name="phone")
    def phone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "phone"))

    @phone.setter
    def phone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__509ef31b42a162f8d3d77c9421e5f342144783483f3bbfb9e113cf817efa9407)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phone", value)

    @builtins.property
    @jsii.member(jsii_name="postalCode")
    def postal_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "postalCode"))

    @postal_code.setter
    def postal_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75bef00f820cf6aa28006305af8f0c2809c0c978de23478b18495b7f90dbaa0f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "postalCode", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e255b86b480ea5498dbc2691179dffff90b58ba0987f0915717543e836f632c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1532f7f75dd8641df4cd9cd8c5ca580810155e36092ad5793faa5c3870164fb0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CpsDvEnrollmentAdminContact]:
        return typing.cast(typing.Optional[CpsDvEnrollmentAdminContact], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CpsDvEnrollmentAdminContact],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6a41cad1c5032e6651141fd1d6174211ca890f8eb106eb18cd5c1cda5068e6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.cpsDvEnrollment.CpsDvEnrollmentConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "admin_contact": "adminContact",
        "common_name": "commonName",
        "contract_id": "contractId",
        "csr": "csr",
        "network_configuration": "networkConfiguration",
        "organization": "organization",
        "secure_network": "secureNetwork",
        "signature_algorithm": "signatureAlgorithm",
        "sni_only": "sniOnly",
        "tech_contact": "techContact",
        "acknowledge_pre_verification_warnings": "acknowledgePreVerificationWarnings",
        "allow_duplicate_common_name": "allowDuplicateCommonName",
        "certificate_chain_type": "certificateChainType",
        "id": "id",
        "sans": "sans",
        "timeouts": "timeouts",
    },
)
class CpsDvEnrollmentConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        admin_contact: typing.Union[CpsDvEnrollmentAdminContact, typing.Dict[builtins.str, typing.Any]],
        common_name: builtins.str,
        contract_id: builtins.str,
        csr: typing.Union["CpsDvEnrollmentCsr", typing.Dict[builtins.str, typing.Any]],
        network_configuration: typing.Union["CpsDvEnrollmentNetworkConfiguration", typing.Dict[builtins.str, typing.Any]],
        organization: typing.Union["CpsDvEnrollmentOrganization", typing.Dict[builtins.str, typing.Any]],
        secure_network: builtins.str,
        signature_algorithm: builtins.str,
        sni_only: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        tech_contact: typing.Union["CpsDvEnrollmentTechContact", typing.Dict[builtins.str, typing.Any]],
        acknowledge_pre_verification_warnings: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        allow_duplicate_common_name: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        certificate_chain_type: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        sans: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["CpsDvEnrollmentTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param admin_contact: admin_contact block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#admin_contact CpsDvEnrollment#admin_contact}
        :param common_name: Common name used for enrollment. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#common_name CpsDvEnrollment#common_name}
        :param contract_id: Contract ID for which enrollment is retrieved. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#contract_id CpsDvEnrollment#contract_id}
        :param csr: csr block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#csr CpsDvEnrollment#csr}
        :param network_configuration: network_configuration block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#network_configuration CpsDvEnrollment#network_configuration}
        :param organization: organization block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#organization CpsDvEnrollment#organization}
        :param secure_network: Type of TLS deployment network. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#secure_network CpsDvEnrollment#secure_network}
        :param signature_algorithm: SHA algorithm type. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#signature_algorithm CpsDvEnrollment#signature_algorithm}
        :param sni_only: Whether Server Name Indication is used for enrollment. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#sni_only CpsDvEnrollment#sni_only}
        :param tech_contact: tech_contact block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#tech_contact CpsDvEnrollment#tech_contact}
        :param acknowledge_pre_verification_warnings: Whether acknowledge warnings before certificate verification. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#acknowledge_pre_verification_warnings CpsDvEnrollment#acknowledge_pre_verification_warnings}
        :param allow_duplicate_common_name: Allow to duplicate common name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#allow_duplicate_common_name CpsDvEnrollment#allow_duplicate_common_name}
        :param certificate_chain_type: Certificate trust chain type. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#certificate_chain_type CpsDvEnrollment#certificate_chain_type}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#id CpsDvEnrollment#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param sans: List of SANs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#sans CpsDvEnrollment#sans}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#timeouts CpsDvEnrollment#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(admin_contact, dict):
            admin_contact = CpsDvEnrollmentAdminContact(**admin_contact)
        if isinstance(csr, dict):
            csr = CpsDvEnrollmentCsr(**csr)
        if isinstance(network_configuration, dict):
            network_configuration = CpsDvEnrollmentNetworkConfiguration(**network_configuration)
        if isinstance(organization, dict):
            organization = CpsDvEnrollmentOrganization(**organization)
        if isinstance(tech_contact, dict):
            tech_contact = CpsDvEnrollmentTechContact(**tech_contact)
        if isinstance(timeouts, dict):
            timeouts = CpsDvEnrollmentTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79b472d87d02fee1bb634b8b447b8076651ee2832717e811853842633143dab2)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument admin_contact", value=admin_contact, expected_type=type_hints["admin_contact"])
            check_type(argname="argument common_name", value=common_name, expected_type=type_hints["common_name"])
            check_type(argname="argument contract_id", value=contract_id, expected_type=type_hints["contract_id"])
            check_type(argname="argument csr", value=csr, expected_type=type_hints["csr"])
            check_type(argname="argument network_configuration", value=network_configuration, expected_type=type_hints["network_configuration"])
            check_type(argname="argument organization", value=organization, expected_type=type_hints["organization"])
            check_type(argname="argument secure_network", value=secure_network, expected_type=type_hints["secure_network"])
            check_type(argname="argument signature_algorithm", value=signature_algorithm, expected_type=type_hints["signature_algorithm"])
            check_type(argname="argument sni_only", value=sni_only, expected_type=type_hints["sni_only"])
            check_type(argname="argument tech_contact", value=tech_contact, expected_type=type_hints["tech_contact"])
            check_type(argname="argument acknowledge_pre_verification_warnings", value=acknowledge_pre_verification_warnings, expected_type=type_hints["acknowledge_pre_verification_warnings"])
            check_type(argname="argument allow_duplicate_common_name", value=allow_duplicate_common_name, expected_type=type_hints["allow_duplicate_common_name"])
            check_type(argname="argument certificate_chain_type", value=certificate_chain_type, expected_type=type_hints["certificate_chain_type"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument sans", value=sans, expected_type=type_hints["sans"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "admin_contact": admin_contact,
            "common_name": common_name,
            "contract_id": contract_id,
            "csr": csr,
            "network_configuration": network_configuration,
            "organization": organization,
            "secure_network": secure_network,
            "signature_algorithm": signature_algorithm,
            "sni_only": sni_only,
            "tech_contact": tech_contact,
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
        if acknowledge_pre_verification_warnings is not None:
            self._values["acknowledge_pre_verification_warnings"] = acknowledge_pre_verification_warnings
        if allow_duplicate_common_name is not None:
            self._values["allow_duplicate_common_name"] = allow_duplicate_common_name
        if certificate_chain_type is not None:
            self._values["certificate_chain_type"] = certificate_chain_type
        if id is not None:
            self._values["id"] = id
        if sans is not None:
            self._values["sans"] = sans
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
    def admin_contact(self) -> CpsDvEnrollmentAdminContact:
        '''admin_contact block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#admin_contact CpsDvEnrollment#admin_contact}
        '''
        result = self._values.get("admin_contact")
        assert result is not None, "Required property 'admin_contact' is missing"
        return typing.cast(CpsDvEnrollmentAdminContact, result)

    @builtins.property
    def common_name(self) -> builtins.str:
        '''Common name used for enrollment.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#common_name CpsDvEnrollment#common_name}
        '''
        result = self._values.get("common_name")
        assert result is not None, "Required property 'common_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def contract_id(self) -> builtins.str:
        '''Contract ID for which enrollment is retrieved.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#contract_id CpsDvEnrollment#contract_id}
        '''
        result = self._values.get("contract_id")
        assert result is not None, "Required property 'contract_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def csr(self) -> "CpsDvEnrollmentCsr":
        '''csr block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#csr CpsDvEnrollment#csr}
        '''
        result = self._values.get("csr")
        assert result is not None, "Required property 'csr' is missing"
        return typing.cast("CpsDvEnrollmentCsr", result)

    @builtins.property
    def network_configuration(self) -> "CpsDvEnrollmentNetworkConfiguration":
        '''network_configuration block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#network_configuration CpsDvEnrollment#network_configuration}
        '''
        result = self._values.get("network_configuration")
        assert result is not None, "Required property 'network_configuration' is missing"
        return typing.cast("CpsDvEnrollmentNetworkConfiguration", result)

    @builtins.property
    def organization(self) -> "CpsDvEnrollmentOrganization":
        '''organization block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#organization CpsDvEnrollment#organization}
        '''
        result = self._values.get("organization")
        assert result is not None, "Required property 'organization' is missing"
        return typing.cast("CpsDvEnrollmentOrganization", result)

    @builtins.property
    def secure_network(self) -> builtins.str:
        '''Type of TLS deployment network.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#secure_network CpsDvEnrollment#secure_network}
        '''
        result = self._values.get("secure_network")
        assert result is not None, "Required property 'secure_network' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def signature_algorithm(self) -> builtins.str:
        '''SHA algorithm type.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#signature_algorithm CpsDvEnrollment#signature_algorithm}
        '''
        result = self._values.get("signature_algorithm")
        assert result is not None, "Required property 'signature_algorithm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sni_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Whether Server Name Indication is used for enrollment.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#sni_only CpsDvEnrollment#sni_only}
        '''
        result = self._values.get("sni_only")
        assert result is not None, "Required property 'sni_only' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def tech_contact(self) -> "CpsDvEnrollmentTechContact":
        '''tech_contact block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#tech_contact CpsDvEnrollment#tech_contact}
        '''
        result = self._values.get("tech_contact")
        assert result is not None, "Required property 'tech_contact' is missing"
        return typing.cast("CpsDvEnrollmentTechContact", result)

    @builtins.property
    def acknowledge_pre_verification_warnings(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether acknowledge warnings before certificate verification.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#acknowledge_pre_verification_warnings CpsDvEnrollment#acknowledge_pre_verification_warnings}
        '''
        result = self._values.get("acknowledge_pre_verification_warnings")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def allow_duplicate_common_name(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Allow to duplicate common name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#allow_duplicate_common_name CpsDvEnrollment#allow_duplicate_common_name}
        '''
        result = self._values.get("allow_duplicate_common_name")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def certificate_chain_type(self) -> typing.Optional[builtins.str]:
        '''Certificate trust chain type.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#certificate_chain_type CpsDvEnrollment#certificate_chain_type}
        '''
        result = self._values.get("certificate_chain_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#id CpsDvEnrollment#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sans(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of SANs.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#sans CpsDvEnrollment#sans}
        '''
        result = self._values.get("sans")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["CpsDvEnrollmentTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#timeouts CpsDvEnrollment#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["CpsDvEnrollmentTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CpsDvEnrollmentConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.cpsDvEnrollment.CpsDvEnrollmentCsr",
    jsii_struct_bases=[],
    name_mapping={
        "city": "city",
        "country_code": "countryCode",
        "organization": "organization",
        "organizational_unit": "organizationalUnit",
        "preferred_trust_chain": "preferredTrustChain",
        "state": "state",
    },
)
class CpsDvEnrollmentCsr:
    def __init__(
        self,
        *,
        city: builtins.str,
        country_code: builtins.str,
        organization: builtins.str,
        organizational_unit: typing.Optional[builtins.str] = None,
        preferred_trust_chain: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param city: City where organization is located. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#city CpsDvEnrollment#city}
        :param country_code: The code of the country where organization is located. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#country_code CpsDvEnrollment#country_code}
        :param organization: Name of organization used in all legal documents. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#organization CpsDvEnrollment#organization}
        :param organizational_unit: Organizational unit of organization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#organizational_unit CpsDvEnrollment#organizational_unit}
        :param preferred_trust_chain: For the Let's Encrypt Domain Validated (DV) SAN certificates, the preferred trust chain will be included by CPS with the leaf certificate in the TLS handshake. If the field does not have a value, whichever trust chain Akamai chooses will be used by default Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#preferred_trust_chain CpsDvEnrollment#preferred_trust_chain}
        :param state: State or province of organization location. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#state CpsDvEnrollment#state}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5134b460b9fb72a273c7d61f452ee19e0996cb9971a7aeac027d6c1fcc32d50)
            check_type(argname="argument city", value=city, expected_type=type_hints["city"])
            check_type(argname="argument country_code", value=country_code, expected_type=type_hints["country_code"])
            check_type(argname="argument organization", value=organization, expected_type=type_hints["organization"])
            check_type(argname="argument organizational_unit", value=organizational_unit, expected_type=type_hints["organizational_unit"])
            check_type(argname="argument preferred_trust_chain", value=preferred_trust_chain, expected_type=type_hints["preferred_trust_chain"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "city": city,
            "country_code": country_code,
            "organization": organization,
        }
        if organizational_unit is not None:
            self._values["organizational_unit"] = organizational_unit
        if preferred_trust_chain is not None:
            self._values["preferred_trust_chain"] = preferred_trust_chain
        if state is not None:
            self._values["state"] = state

    @builtins.property
    def city(self) -> builtins.str:
        '''City where organization is located.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#city CpsDvEnrollment#city}
        '''
        result = self._values.get("city")
        assert result is not None, "Required property 'city' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def country_code(self) -> builtins.str:
        '''The code of the country where organization is located.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#country_code CpsDvEnrollment#country_code}
        '''
        result = self._values.get("country_code")
        assert result is not None, "Required property 'country_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def organization(self) -> builtins.str:
        '''Name of organization used in all legal documents.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#organization CpsDvEnrollment#organization}
        '''
        result = self._values.get("organization")
        assert result is not None, "Required property 'organization' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def organizational_unit(self) -> typing.Optional[builtins.str]:
        '''Organizational unit of organization.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#organizational_unit CpsDvEnrollment#organizational_unit}
        '''
        result = self._values.get("organizational_unit")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preferred_trust_chain(self) -> typing.Optional[builtins.str]:
        '''For the Let's Encrypt Domain Validated (DV) SAN certificates, the preferred trust chain will be included by CPS with the leaf certificate in the TLS handshake.

        If the field does not have a value, whichever trust chain Akamai chooses will be used by default

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#preferred_trust_chain CpsDvEnrollment#preferred_trust_chain}
        '''
        result = self._values.get("preferred_trust_chain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''State or province of organization location.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#state CpsDvEnrollment#state}
        '''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CpsDvEnrollmentCsr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CpsDvEnrollmentCsrOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.cpsDvEnrollment.CpsDvEnrollmentCsrOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f51f44ae67c2729219b5365b6c7d7bbaaf34b44798b80321954bddd453f7b495)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetOrganizationalUnit")
    def reset_organizational_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrganizationalUnit", []))

    @jsii.member(jsii_name="resetPreferredTrustChain")
    def reset_preferred_trust_chain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreferredTrustChain", []))

    @jsii.member(jsii_name="resetState")
    def reset_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetState", []))

    @builtins.property
    @jsii.member(jsii_name="cityInput")
    def city_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cityInput"))

    @builtins.property
    @jsii.member(jsii_name="countryCodeInput")
    def country_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "countryCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="organizationalUnitInput")
    def organizational_unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "organizationalUnitInput"))

    @builtins.property
    @jsii.member(jsii_name="organizationInput")
    def organization_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "organizationInput"))

    @builtins.property
    @jsii.member(jsii_name="preferredTrustChainInput")
    def preferred_trust_chain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredTrustChainInput"))

    @builtins.property
    @jsii.member(jsii_name="stateInput")
    def state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateInput"))

    @builtins.property
    @jsii.member(jsii_name="city")
    def city(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "city"))

    @city.setter
    def city(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75b348890a07e2ade55717439ffe0405363e2619df62d396945e80c49aa37b56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "city", value)

    @builtins.property
    @jsii.member(jsii_name="countryCode")
    def country_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "countryCode"))

    @country_code.setter
    def country_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76430d7dcc52dedb5eac9febc62058e4e370d9c5b70cae91e06d6c7871fdab0f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "countryCode", value)

    @builtins.property
    @jsii.member(jsii_name="organization")
    def organization(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organization"))

    @organization.setter
    def organization(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6784d4d5608220a908dacd17e7be2e00fd7bdbb66ff6b2b67ded8025d7b939ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organization", value)

    @builtins.property
    @jsii.member(jsii_name="organizationalUnit")
    def organizational_unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organizationalUnit"))

    @organizational_unit.setter
    def organizational_unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c42503d2cb23cf514b26570048c7462c8463ba9f54cdcd7a344f108572d5410)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organizationalUnit", value)

    @builtins.property
    @jsii.member(jsii_name="preferredTrustChain")
    def preferred_trust_chain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "preferredTrustChain"))

    @preferred_trust_chain.setter
    def preferred_trust_chain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20be3390dd2e93373e5476118c88cfa37876004f9a0db7829d4d205ff1fa3909)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredTrustChain", value)

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @state.setter
    def state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fe52198391a21d630a5f27c219770c17bb2d327ac228c6bf4bea97ab3cbbb33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CpsDvEnrollmentCsr]:
        return typing.cast(typing.Optional[CpsDvEnrollmentCsr], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CpsDvEnrollmentCsr]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1915ec229ebe79956ed384a0e722f28a8646e2667542480b40f2c31678b79c84)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.cpsDvEnrollment.CpsDvEnrollmentDnsChallenges",
    jsii_struct_bases=[],
    name_mapping={},
)
class CpsDvEnrollmentDnsChallenges:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CpsDvEnrollmentDnsChallenges(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CpsDvEnrollmentDnsChallengesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.cpsDvEnrollment.CpsDvEnrollmentDnsChallengesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5ad5d5ddaf567165aa45cdd81d24233877bb02ba3b955ca1aba894881f841755)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "CpsDvEnrollmentDnsChallengesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28646549724fd9e2da27971e8c91e6d887feff029ea4d64e86b981c84c12904a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CpsDvEnrollmentDnsChallengesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a041d3eaaa89552e88080a473ae62c6fb3f40b28d77a1378105ee4307e9dc72)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a059892ce0fe7124f8402c7745053a7cfecb7fef379f0472f05caf1460b72a24)
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
            type_hints = typing.get_type_hints(_typecheckingstub__88938160f8d52c83488d2d2b2846a65b2f80f7f4370a85ee6ae7972003dc04d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class CpsDvEnrollmentDnsChallengesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.cpsDvEnrollment.CpsDvEnrollmentDnsChallengesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c554baaad36b06cd6479bf012470a288c4ab120107f53c08faf3c52bc678c93a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @builtins.property
    @jsii.member(jsii_name="fullPath")
    def full_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fullPath"))

    @builtins.property
    @jsii.member(jsii_name="responseBody")
    def response_body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseBody"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CpsDvEnrollmentDnsChallenges]:
        return typing.cast(typing.Optional[CpsDvEnrollmentDnsChallenges], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CpsDvEnrollmentDnsChallenges],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c4a41630f1c45133fd41ebc1485ecb1e210d198616e4e8b817a4e6b95746476)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.cpsDvEnrollment.CpsDvEnrollmentHttpChallenges",
    jsii_struct_bases=[],
    name_mapping={},
)
class CpsDvEnrollmentHttpChallenges:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CpsDvEnrollmentHttpChallenges(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CpsDvEnrollmentHttpChallengesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.cpsDvEnrollment.CpsDvEnrollmentHttpChallengesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__147c482dbfde049abcb359afc7db684dc9206380f7c54b5364cee54c23054009)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "CpsDvEnrollmentHttpChallengesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0102bffd6b685a25718d272e096ed70a2fb4adfdb05980b69429d924ff6abb78)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CpsDvEnrollmentHttpChallengesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db22d4072d57302d61149f9ca0448af382938d3d19fe2fbc016e51900254c57a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__012dbb1743e7d8141c76d79ebcd15c67905cbc4d7028251bb3763533dfc92b37)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fc131411270c1bec3774830787883fb621eaa5321bb3c1df06c8e9aa0c4c5c45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class CpsDvEnrollmentHttpChallengesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.cpsDvEnrollment.CpsDvEnrollmentHttpChallengesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f2962a7a4543592e28f1b6f628bd4549636960c42086a3d8f3e602e89176c697)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @builtins.property
    @jsii.member(jsii_name="fullPath")
    def full_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fullPath"))

    @builtins.property
    @jsii.member(jsii_name="responseBody")
    def response_body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseBody"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CpsDvEnrollmentHttpChallenges]:
        return typing.cast(typing.Optional[CpsDvEnrollmentHttpChallenges], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CpsDvEnrollmentHttpChallenges],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a984c568a2a2d17019b99f403a38516dacdee8a357d4324aed24bf9abad86b63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.cpsDvEnrollment.CpsDvEnrollmentNetworkConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "geography": "geography",
        "client_mutual_authentication": "clientMutualAuthentication",
        "clone_dns_names": "cloneDnsNames",
        "disallowed_tls_versions": "disallowedTlsVersions",
        "must_have_ciphers": "mustHaveCiphers",
        "ocsp_stapling": "ocspStapling",
        "preferred_ciphers": "preferredCiphers",
        "quic_enabled": "quicEnabled",
    },
)
class CpsDvEnrollmentNetworkConfiguration:
    def __init__(
        self,
        *,
        geography: builtins.str,
        client_mutual_authentication: typing.Optional[typing.Union["CpsDvEnrollmentNetworkConfigurationClientMutualAuthentication", typing.Dict[builtins.str, typing.Any]]] = None,
        clone_dns_names: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        disallowed_tls_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
        must_have_ciphers: typing.Optional[builtins.str] = None,
        ocsp_stapling: typing.Optional[builtins.str] = None,
        preferred_ciphers: typing.Optional[builtins.str] = None,
        quic_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param geography: Geography type used for enrollment. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#geography CpsDvEnrollment#geography}
        :param client_mutual_authentication: client_mutual_authentication block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#client_mutual_authentication CpsDvEnrollment#client_mutual_authentication}
        :param clone_dns_names: Enable CPS to direct traffic using all the SANs listed in the SANs parameter when enrollment is created. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#clone_dns_names CpsDvEnrollment#clone_dns_names}
        :param disallowed_tls_versions: TLS versions which are disallowed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#disallowed_tls_versions CpsDvEnrollment#disallowed_tls_versions}
        :param must_have_ciphers: Mandatory Ciphers which are included for enrollment. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#must_have_ciphers CpsDvEnrollment#must_have_ciphers}
        :param ocsp_stapling: Enable OCSP stapling. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#ocsp_stapling CpsDvEnrollment#ocsp_stapling}
        :param preferred_ciphers: Preferred Ciphers which are included for enrollment. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#preferred_ciphers CpsDvEnrollment#preferred_ciphers}
        :param quic_enabled: Enable QUIC protocol. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#quic_enabled CpsDvEnrollment#quic_enabled}
        '''
        if isinstance(client_mutual_authentication, dict):
            client_mutual_authentication = CpsDvEnrollmentNetworkConfigurationClientMutualAuthentication(**client_mutual_authentication)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__534327d28ca2299c194358cd6ec77934bbb6f2fe995992da87183dcd1518cc84)
            check_type(argname="argument geography", value=geography, expected_type=type_hints["geography"])
            check_type(argname="argument client_mutual_authentication", value=client_mutual_authentication, expected_type=type_hints["client_mutual_authentication"])
            check_type(argname="argument clone_dns_names", value=clone_dns_names, expected_type=type_hints["clone_dns_names"])
            check_type(argname="argument disallowed_tls_versions", value=disallowed_tls_versions, expected_type=type_hints["disallowed_tls_versions"])
            check_type(argname="argument must_have_ciphers", value=must_have_ciphers, expected_type=type_hints["must_have_ciphers"])
            check_type(argname="argument ocsp_stapling", value=ocsp_stapling, expected_type=type_hints["ocsp_stapling"])
            check_type(argname="argument preferred_ciphers", value=preferred_ciphers, expected_type=type_hints["preferred_ciphers"])
            check_type(argname="argument quic_enabled", value=quic_enabled, expected_type=type_hints["quic_enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "geography": geography,
        }
        if client_mutual_authentication is not None:
            self._values["client_mutual_authentication"] = client_mutual_authentication
        if clone_dns_names is not None:
            self._values["clone_dns_names"] = clone_dns_names
        if disallowed_tls_versions is not None:
            self._values["disallowed_tls_versions"] = disallowed_tls_versions
        if must_have_ciphers is not None:
            self._values["must_have_ciphers"] = must_have_ciphers
        if ocsp_stapling is not None:
            self._values["ocsp_stapling"] = ocsp_stapling
        if preferred_ciphers is not None:
            self._values["preferred_ciphers"] = preferred_ciphers
        if quic_enabled is not None:
            self._values["quic_enabled"] = quic_enabled

    @builtins.property
    def geography(self) -> builtins.str:
        '''Geography type used for enrollment.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#geography CpsDvEnrollment#geography}
        '''
        result = self._values.get("geography")
        assert result is not None, "Required property 'geography' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_mutual_authentication(
        self,
    ) -> typing.Optional["CpsDvEnrollmentNetworkConfigurationClientMutualAuthentication"]:
        '''client_mutual_authentication block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#client_mutual_authentication CpsDvEnrollment#client_mutual_authentication}
        '''
        result = self._values.get("client_mutual_authentication")
        return typing.cast(typing.Optional["CpsDvEnrollmentNetworkConfigurationClientMutualAuthentication"], result)

    @builtins.property
    def clone_dns_names(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Enable CPS to direct traffic using all the SANs listed in the SANs parameter when enrollment is created.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#clone_dns_names CpsDvEnrollment#clone_dns_names}
        '''
        result = self._values.get("clone_dns_names")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def disallowed_tls_versions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''TLS versions which are disallowed.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#disallowed_tls_versions CpsDvEnrollment#disallowed_tls_versions}
        '''
        result = self._values.get("disallowed_tls_versions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def must_have_ciphers(self) -> typing.Optional[builtins.str]:
        '''Mandatory Ciphers which are included for enrollment.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#must_have_ciphers CpsDvEnrollment#must_have_ciphers}
        '''
        result = self._values.get("must_have_ciphers")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ocsp_stapling(self) -> typing.Optional[builtins.str]:
        '''Enable OCSP stapling.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#ocsp_stapling CpsDvEnrollment#ocsp_stapling}
        '''
        result = self._values.get("ocsp_stapling")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preferred_ciphers(self) -> typing.Optional[builtins.str]:
        '''Preferred Ciphers which are included for enrollment.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#preferred_ciphers CpsDvEnrollment#preferred_ciphers}
        '''
        result = self._values.get("preferred_ciphers")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def quic_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Enable QUIC protocol.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#quic_enabled CpsDvEnrollment#quic_enabled}
        '''
        result = self._values.get("quic_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CpsDvEnrollmentNetworkConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.cpsDvEnrollment.CpsDvEnrollmentNetworkConfigurationClientMutualAuthentication",
    jsii_struct_bases=[],
    name_mapping={
        "ocsp_enabled": "ocspEnabled",
        "send_ca_list_to_client": "sendCaListToClient",
        "set_id": "setId",
    },
)
class CpsDvEnrollmentNetworkConfigurationClientMutualAuthentication:
    def __init__(
        self,
        *,
        ocsp_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        send_ca_list_to_client: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        set_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ocsp_enabled: Enable OCSP stapling. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#ocsp_enabled CpsDvEnrollment#ocsp_enabled}
        :param send_ca_list_to_client: Enable the server to send the certificate authority (CA) list to the client. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#send_ca_list_to_client CpsDvEnrollment#send_ca_list_to_client}
        :param set_id: The identifier of the set of trust chains, created in the Trust Chain Manager. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#set_id CpsDvEnrollment#set_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3eeb99cf34f97a9b668267967fe1529019bc09737bf25dc6374b19da8257d613)
            check_type(argname="argument ocsp_enabled", value=ocsp_enabled, expected_type=type_hints["ocsp_enabled"])
            check_type(argname="argument send_ca_list_to_client", value=send_ca_list_to_client, expected_type=type_hints["send_ca_list_to_client"])
            check_type(argname="argument set_id", value=set_id, expected_type=type_hints["set_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ocsp_enabled is not None:
            self._values["ocsp_enabled"] = ocsp_enabled
        if send_ca_list_to_client is not None:
            self._values["send_ca_list_to_client"] = send_ca_list_to_client
        if set_id is not None:
            self._values["set_id"] = set_id

    @builtins.property
    def ocsp_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Enable OCSP stapling.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#ocsp_enabled CpsDvEnrollment#ocsp_enabled}
        '''
        result = self._values.get("ocsp_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def send_ca_list_to_client(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Enable the server to send the certificate authority (CA) list to the client.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#send_ca_list_to_client CpsDvEnrollment#send_ca_list_to_client}
        '''
        result = self._values.get("send_ca_list_to_client")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def set_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of the set of trust chains, created in the Trust Chain Manager.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#set_id CpsDvEnrollment#set_id}
        '''
        result = self._values.get("set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CpsDvEnrollmentNetworkConfigurationClientMutualAuthentication(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CpsDvEnrollmentNetworkConfigurationClientMutualAuthenticationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.cpsDvEnrollment.CpsDvEnrollmentNetworkConfigurationClientMutualAuthenticationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e40beb6845ad2374115cc5fb5b8c5425ae61d4d96c14526f5192a0868f60d4f1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetOcspEnabled")
    def reset_ocsp_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOcspEnabled", []))

    @jsii.member(jsii_name="resetSendCaListToClient")
    def reset_send_ca_list_to_client(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSendCaListToClient", []))

    @jsii.member(jsii_name="resetSetId")
    def reset_set_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSetId", []))

    @builtins.property
    @jsii.member(jsii_name="ocspEnabledInput")
    def ocsp_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "ocspEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="sendCaListToClientInput")
    def send_ca_list_to_client_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "sendCaListToClientInput"))

    @builtins.property
    @jsii.member(jsii_name="setIdInput")
    def set_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "setIdInput"))

    @builtins.property
    @jsii.member(jsii_name="ocspEnabled")
    def ocsp_enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "ocspEnabled"))

    @ocsp_enabled.setter
    def ocsp_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abdb06f6f124dda8bb9b8a1295cea4d7fa7b2532eb7cec8be7619cb68f682700)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ocspEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="sendCaListToClient")
    def send_ca_list_to_client(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "sendCaListToClient"))

    @send_ca_list_to_client.setter
    def send_ca_list_to_client(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1586bbdc8b22eafe9a7224d418d7e231a3e8390fb05e29ce20f2691d49f547b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sendCaListToClient", value)

    @builtins.property
    @jsii.member(jsii_name="setId")
    def set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "setId"))

    @set_id.setter
    def set_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e82610ffd40a351b1830973f777ca0a99bac6959bfdc17575899fa33ff92f39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "setId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CpsDvEnrollmentNetworkConfigurationClientMutualAuthentication]:
        return typing.cast(typing.Optional[CpsDvEnrollmentNetworkConfigurationClientMutualAuthentication], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CpsDvEnrollmentNetworkConfigurationClientMutualAuthentication],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a149d4bf6cc68cd68f570b796723bf334e4c34d933ad62c61a24444192256a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CpsDvEnrollmentNetworkConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.cpsDvEnrollment.CpsDvEnrollmentNetworkConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a8481d3bcd32056710ea9cbf33cf094e4f7eef3f36bd479400297b1aa86c2d5d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putClientMutualAuthentication")
    def put_client_mutual_authentication(
        self,
        *,
        ocsp_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        send_ca_list_to_client: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        set_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ocsp_enabled: Enable OCSP stapling. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#ocsp_enabled CpsDvEnrollment#ocsp_enabled}
        :param send_ca_list_to_client: Enable the server to send the certificate authority (CA) list to the client. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#send_ca_list_to_client CpsDvEnrollment#send_ca_list_to_client}
        :param set_id: The identifier of the set of trust chains, created in the Trust Chain Manager. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#set_id CpsDvEnrollment#set_id}
        '''
        value = CpsDvEnrollmentNetworkConfigurationClientMutualAuthentication(
            ocsp_enabled=ocsp_enabled,
            send_ca_list_to_client=send_ca_list_to_client,
            set_id=set_id,
        )

        return typing.cast(None, jsii.invoke(self, "putClientMutualAuthentication", [value]))

    @jsii.member(jsii_name="resetClientMutualAuthentication")
    def reset_client_mutual_authentication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientMutualAuthentication", []))

    @jsii.member(jsii_name="resetCloneDnsNames")
    def reset_clone_dns_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloneDnsNames", []))

    @jsii.member(jsii_name="resetDisallowedTlsVersions")
    def reset_disallowed_tls_versions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisallowedTlsVersions", []))

    @jsii.member(jsii_name="resetMustHaveCiphers")
    def reset_must_have_ciphers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMustHaveCiphers", []))

    @jsii.member(jsii_name="resetOcspStapling")
    def reset_ocsp_stapling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOcspStapling", []))

    @jsii.member(jsii_name="resetPreferredCiphers")
    def reset_preferred_ciphers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreferredCiphers", []))

    @jsii.member(jsii_name="resetQuicEnabled")
    def reset_quic_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQuicEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="clientMutualAuthentication")
    def client_mutual_authentication(
        self,
    ) -> CpsDvEnrollmentNetworkConfigurationClientMutualAuthenticationOutputReference:
        return typing.cast(CpsDvEnrollmentNetworkConfigurationClientMutualAuthenticationOutputReference, jsii.get(self, "clientMutualAuthentication"))

    @builtins.property
    @jsii.member(jsii_name="clientMutualAuthenticationInput")
    def client_mutual_authentication_input(
        self,
    ) -> typing.Optional[CpsDvEnrollmentNetworkConfigurationClientMutualAuthentication]:
        return typing.cast(typing.Optional[CpsDvEnrollmentNetworkConfigurationClientMutualAuthentication], jsii.get(self, "clientMutualAuthenticationInput"))

    @builtins.property
    @jsii.member(jsii_name="cloneDnsNamesInput")
    def clone_dns_names_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "cloneDnsNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="disallowedTlsVersionsInput")
    def disallowed_tls_versions_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "disallowedTlsVersionsInput"))

    @builtins.property
    @jsii.member(jsii_name="geographyInput")
    def geography_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "geographyInput"))

    @builtins.property
    @jsii.member(jsii_name="mustHaveCiphersInput")
    def must_have_ciphers_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mustHaveCiphersInput"))

    @builtins.property
    @jsii.member(jsii_name="ocspStaplingInput")
    def ocsp_stapling_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ocspStaplingInput"))

    @builtins.property
    @jsii.member(jsii_name="preferredCiphersInput")
    def preferred_ciphers_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredCiphersInput"))

    @builtins.property
    @jsii.member(jsii_name="quicEnabledInput")
    def quic_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "quicEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="cloneDnsNames")
    def clone_dns_names(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "cloneDnsNames"))

    @clone_dns_names.setter
    def clone_dns_names(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3226bab4df5d3f7422ec072ed587602b72943f10fa255ba2f9571fa5ed278376)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloneDnsNames", value)

    @builtins.property
    @jsii.member(jsii_name="disallowedTlsVersions")
    def disallowed_tls_versions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "disallowedTlsVersions"))

    @disallowed_tls_versions.setter
    def disallowed_tls_versions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df97967a9f69b3290b7a3eaf4ef3b061a04100bb33183e9f6a409cbc3f72cc9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disallowedTlsVersions", value)

    @builtins.property
    @jsii.member(jsii_name="geography")
    def geography(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "geography"))

    @geography.setter
    def geography(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d457e38225939842cd9c0e16ac7c4645105ac98819009f02bd41e21d6c786832)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "geography", value)

    @builtins.property
    @jsii.member(jsii_name="mustHaveCiphers")
    def must_have_ciphers(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mustHaveCiphers"))

    @must_have_ciphers.setter
    def must_have_ciphers(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb1704e2a60d94e5e158bf0c3231288413c7ad43eea19d74755e5a08424a2df6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mustHaveCiphers", value)

    @builtins.property
    @jsii.member(jsii_name="ocspStapling")
    def ocsp_stapling(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ocspStapling"))

    @ocsp_stapling.setter
    def ocsp_stapling(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f32aca30fb40935c442ca47477c9f5014ac39b41aba02eb1e3fe3ee1ad9073b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ocspStapling", value)

    @builtins.property
    @jsii.member(jsii_name="preferredCiphers")
    def preferred_ciphers(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "preferredCiphers"))

    @preferred_ciphers.setter
    def preferred_ciphers(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b24594539d2ee304a5938a605524597767c695c9ee4b398b95a519504bee38ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredCiphers", value)

    @builtins.property
    @jsii.member(jsii_name="quicEnabled")
    def quic_enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "quicEnabled"))

    @quic_enabled.setter
    def quic_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fea9b32f0cb0070be223d813d3bb5f871126d503e220caedf02985ce0af3527)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "quicEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CpsDvEnrollmentNetworkConfiguration]:
        return typing.cast(typing.Optional[CpsDvEnrollmentNetworkConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CpsDvEnrollmentNetworkConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48265f40c838cb2016b26db27e133bed617f4f319de299319db791d549a4b52c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.cpsDvEnrollment.CpsDvEnrollmentOrganization",
    jsii_struct_bases=[],
    name_mapping={
        "address_line_one": "addressLineOne",
        "city": "city",
        "country_code": "countryCode",
        "name": "name",
        "phone": "phone",
        "postal_code": "postalCode",
        "region": "region",
        "address_line_two": "addressLineTwo",
    },
)
class CpsDvEnrollmentOrganization:
    def __init__(
        self,
        *,
        address_line_one: builtins.str,
        city: builtins.str,
        country_code: builtins.str,
        name: builtins.str,
        phone: builtins.str,
        postal_code: builtins.str,
        region: builtins.str,
        address_line_two: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param address_line_one: The address of organization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#address_line_one CpsDvEnrollment#address_line_one}
        :param city: City of organization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#city CpsDvEnrollment#city}
        :param country_code: Country code of organization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#country_code CpsDvEnrollment#country_code}
        :param name: Name of organization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#name CpsDvEnrollment#name}
        :param phone: Phone number of organization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#phone CpsDvEnrollment#phone}
        :param postal_code: Postal code of organization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#postal_code CpsDvEnrollment#postal_code}
        :param region: The region of organization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#region CpsDvEnrollment#region}
        :param address_line_two: The address of organization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#address_line_two CpsDvEnrollment#address_line_two}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d6124d821572c297acb71fa51a0be88c5a4039d553681d11086e980dd961e32)
            check_type(argname="argument address_line_one", value=address_line_one, expected_type=type_hints["address_line_one"])
            check_type(argname="argument city", value=city, expected_type=type_hints["city"])
            check_type(argname="argument country_code", value=country_code, expected_type=type_hints["country_code"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument phone", value=phone, expected_type=type_hints["phone"])
            check_type(argname="argument postal_code", value=postal_code, expected_type=type_hints["postal_code"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument address_line_two", value=address_line_two, expected_type=type_hints["address_line_two"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "address_line_one": address_line_one,
            "city": city,
            "country_code": country_code,
            "name": name,
            "phone": phone,
            "postal_code": postal_code,
            "region": region,
        }
        if address_line_two is not None:
            self._values["address_line_two"] = address_line_two

    @builtins.property
    def address_line_one(self) -> builtins.str:
        '''The address of organization.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#address_line_one CpsDvEnrollment#address_line_one}
        '''
        result = self._values.get("address_line_one")
        assert result is not None, "Required property 'address_line_one' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def city(self) -> builtins.str:
        '''City of organization.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#city CpsDvEnrollment#city}
        '''
        result = self._values.get("city")
        assert result is not None, "Required property 'city' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def country_code(self) -> builtins.str:
        '''Country code of organization.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#country_code CpsDvEnrollment#country_code}
        '''
        result = self._values.get("country_code")
        assert result is not None, "Required property 'country_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of organization.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#name CpsDvEnrollment#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def phone(self) -> builtins.str:
        '''Phone number of organization.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#phone CpsDvEnrollment#phone}
        '''
        result = self._values.get("phone")
        assert result is not None, "Required property 'phone' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def postal_code(self) -> builtins.str:
        '''Postal code of organization.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#postal_code CpsDvEnrollment#postal_code}
        '''
        result = self._values.get("postal_code")
        assert result is not None, "Required property 'postal_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''The region of organization.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#region CpsDvEnrollment#region}
        '''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def address_line_two(self) -> typing.Optional[builtins.str]:
        '''The address of organization.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#address_line_two CpsDvEnrollment#address_line_two}
        '''
        result = self._values.get("address_line_two")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CpsDvEnrollmentOrganization(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CpsDvEnrollmentOrganizationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.cpsDvEnrollment.CpsDvEnrollmentOrganizationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0cda7847aad94d0adfbc5c6388388290fe10800462c2b9ca48893b9ddff04437)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAddressLineTwo")
    def reset_address_line_two(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddressLineTwo", []))

    @builtins.property
    @jsii.member(jsii_name="addressLineOneInput")
    def address_line_one_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressLineOneInput"))

    @builtins.property
    @jsii.member(jsii_name="addressLineTwoInput")
    def address_line_two_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressLineTwoInput"))

    @builtins.property
    @jsii.member(jsii_name="cityInput")
    def city_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cityInput"))

    @builtins.property
    @jsii.member(jsii_name="countryCodeInput")
    def country_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "countryCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="phoneInput")
    def phone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "phoneInput"))

    @builtins.property
    @jsii.member(jsii_name="postalCodeInput")
    def postal_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "postalCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="addressLineOne")
    def address_line_one(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "addressLineOne"))

    @address_line_one.setter
    def address_line_one(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9adf7f202c731068b721a615a3f9cccc3bd0c2e571f2182777cebd2263f3ca3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addressLineOne", value)

    @builtins.property
    @jsii.member(jsii_name="addressLineTwo")
    def address_line_two(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "addressLineTwo"))

    @address_line_two.setter
    def address_line_two(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e38cd4ef2d8656f3483a68218c0e34a3cc2f18e441b0a712bc546dfeeff33adf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addressLineTwo", value)

    @builtins.property
    @jsii.member(jsii_name="city")
    def city(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "city"))

    @city.setter
    def city(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff4f5e8699d8546610e1950bfd9d7a1f1cc00e0b1954bd823759ba93537d2d2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "city", value)

    @builtins.property
    @jsii.member(jsii_name="countryCode")
    def country_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "countryCode"))

    @country_code.setter
    def country_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94312d8f2f982ff047e2e0784cc068825923133f48fc9d6a1e7a1b7e43ffdf78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "countryCode", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fc41f86bf40dee15b508753e32d69d4eb479db98f3d3a354c43aa785d0ca4ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="phone")
    def phone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "phone"))

    @phone.setter
    def phone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9229161429f9cbd4506ebfcd760048f2157e36da2f4b883d9ce4c0b48903dfa9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phone", value)

    @builtins.property
    @jsii.member(jsii_name="postalCode")
    def postal_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "postalCode"))

    @postal_code.setter
    def postal_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd68ba73859b6525bd81b72f695d5acb5cdfcdaa47bae744705e507b7ff0659f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "postalCode", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8c185847e2686d3869c1fcfdf57559c166d410e2c2c6751669dc19a36f8dcd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CpsDvEnrollmentOrganization]:
        return typing.cast(typing.Optional[CpsDvEnrollmentOrganization], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CpsDvEnrollmentOrganization],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00710fb2f4a531572f32cbb87757d317e84ff1d6e852bc7dcc0246fce4630333)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.cpsDvEnrollment.CpsDvEnrollmentTechContact",
    jsii_struct_bases=[],
    name_mapping={
        "address_line_one": "addressLineOne",
        "city": "city",
        "country_code": "countryCode",
        "email": "email",
        "first_name": "firstName",
        "last_name": "lastName",
        "organization": "organization",
        "phone": "phone",
        "postal_code": "postalCode",
        "region": "region",
        "address_line_two": "addressLineTwo",
        "title": "title",
    },
)
class CpsDvEnrollmentTechContact:
    def __init__(
        self,
        *,
        address_line_one: builtins.str,
        city: builtins.str,
        country_code: builtins.str,
        email: builtins.str,
        first_name: builtins.str,
        last_name: builtins.str,
        organization: builtins.str,
        phone: builtins.str,
        postal_code: builtins.str,
        region: builtins.str,
        address_line_two: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param address_line_one: The address of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#address_line_one CpsDvEnrollment#address_line_one}
        :param city: City of residence of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#city CpsDvEnrollment#city}
        :param country_code: Country code of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#country_code CpsDvEnrollment#country_code}
        :param email: E-mail address of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#email CpsDvEnrollment#email}
        :param first_name: First name of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#first_name CpsDvEnrollment#first_name}
        :param last_name: Last name of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#last_name CpsDvEnrollment#last_name}
        :param organization: Organization where contact is hired. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#organization CpsDvEnrollment#organization}
        :param phone: Phone number of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#phone CpsDvEnrollment#phone}
        :param postal_code: Postal code of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#postal_code CpsDvEnrollment#postal_code}
        :param region: The region of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#region CpsDvEnrollment#region}
        :param address_line_two: The address of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#address_line_two CpsDvEnrollment#address_line_two}
        :param title: Title of the the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#title CpsDvEnrollment#title}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d91a33c8095ccfe7b5ff66a14ecf4467e489895815b9bcd7767e4240811ea09a)
            check_type(argname="argument address_line_one", value=address_line_one, expected_type=type_hints["address_line_one"])
            check_type(argname="argument city", value=city, expected_type=type_hints["city"])
            check_type(argname="argument country_code", value=country_code, expected_type=type_hints["country_code"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument first_name", value=first_name, expected_type=type_hints["first_name"])
            check_type(argname="argument last_name", value=last_name, expected_type=type_hints["last_name"])
            check_type(argname="argument organization", value=organization, expected_type=type_hints["organization"])
            check_type(argname="argument phone", value=phone, expected_type=type_hints["phone"])
            check_type(argname="argument postal_code", value=postal_code, expected_type=type_hints["postal_code"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument address_line_two", value=address_line_two, expected_type=type_hints["address_line_two"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "address_line_one": address_line_one,
            "city": city,
            "country_code": country_code,
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "organization": organization,
            "phone": phone,
            "postal_code": postal_code,
            "region": region,
        }
        if address_line_two is not None:
            self._values["address_line_two"] = address_line_two
        if title is not None:
            self._values["title"] = title

    @builtins.property
    def address_line_one(self) -> builtins.str:
        '''The address of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#address_line_one CpsDvEnrollment#address_line_one}
        '''
        result = self._values.get("address_line_one")
        assert result is not None, "Required property 'address_line_one' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def city(self) -> builtins.str:
        '''City of residence of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#city CpsDvEnrollment#city}
        '''
        result = self._values.get("city")
        assert result is not None, "Required property 'city' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def country_code(self) -> builtins.str:
        '''Country code of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#country_code CpsDvEnrollment#country_code}
        '''
        result = self._values.get("country_code")
        assert result is not None, "Required property 'country_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def email(self) -> builtins.str:
        '''E-mail address of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#email CpsDvEnrollment#email}
        '''
        result = self._values.get("email")
        assert result is not None, "Required property 'email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def first_name(self) -> builtins.str:
        '''First name of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#first_name CpsDvEnrollment#first_name}
        '''
        result = self._values.get("first_name")
        assert result is not None, "Required property 'first_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def last_name(self) -> builtins.str:
        '''Last name of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#last_name CpsDvEnrollment#last_name}
        '''
        result = self._values.get("last_name")
        assert result is not None, "Required property 'last_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def organization(self) -> builtins.str:
        '''Organization where contact is hired.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#organization CpsDvEnrollment#organization}
        '''
        result = self._values.get("organization")
        assert result is not None, "Required property 'organization' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def phone(self) -> builtins.str:
        '''Phone number of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#phone CpsDvEnrollment#phone}
        '''
        result = self._values.get("phone")
        assert result is not None, "Required property 'phone' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def postal_code(self) -> builtins.str:
        '''Postal code of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#postal_code CpsDvEnrollment#postal_code}
        '''
        result = self._values.get("postal_code")
        assert result is not None, "Required property 'postal_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''The region of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#region CpsDvEnrollment#region}
        '''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def address_line_two(self) -> typing.Optional[builtins.str]:
        '''The address of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#address_line_two CpsDvEnrollment#address_line_two}
        '''
        result = self._values.get("address_line_two")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''Title of the the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#title CpsDvEnrollment#title}
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CpsDvEnrollmentTechContact(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CpsDvEnrollmentTechContactOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.cpsDvEnrollment.CpsDvEnrollmentTechContactOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f2fed9473cdb0ca245758884f5fee55f2282923f7f2fd0f2226f55bfcec2b456)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAddressLineTwo")
    def reset_address_line_two(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddressLineTwo", []))

    @jsii.member(jsii_name="resetTitle")
    def reset_title(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTitle", []))

    @builtins.property
    @jsii.member(jsii_name="addressLineOneInput")
    def address_line_one_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressLineOneInput"))

    @builtins.property
    @jsii.member(jsii_name="addressLineTwoInput")
    def address_line_two_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressLineTwoInput"))

    @builtins.property
    @jsii.member(jsii_name="cityInput")
    def city_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cityInput"))

    @builtins.property
    @jsii.member(jsii_name="countryCodeInput")
    def country_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "countryCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="firstNameInput")
    def first_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firstNameInput"))

    @builtins.property
    @jsii.member(jsii_name="lastNameInput")
    def last_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lastNameInput"))

    @builtins.property
    @jsii.member(jsii_name="organizationInput")
    def organization_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "organizationInput"))

    @builtins.property
    @jsii.member(jsii_name="phoneInput")
    def phone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "phoneInput"))

    @builtins.property
    @jsii.member(jsii_name="postalCodeInput")
    def postal_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "postalCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="addressLineOne")
    def address_line_one(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "addressLineOne"))

    @address_line_one.setter
    def address_line_one(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__267b005e4d93bc9f7096303ed300ef2961479f70ccf21877aeb2cd54667911d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addressLineOne", value)

    @builtins.property
    @jsii.member(jsii_name="addressLineTwo")
    def address_line_two(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "addressLineTwo"))

    @address_line_two.setter
    def address_line_two(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f7376b4e0233ab089e93e710faacaa3eac27e1b93662aba775c263455e1afac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addressLineTwo", value)

    @builtins.property
    @jsii.member(jsii_name="city")
    def city(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "city"))

    @city.setter
    def city(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9898478bff3ac448f7aa84e589bed4bff81ce7bbd1a067178719ba36493bc20)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "city", value)

    @builtins.property
    @jsii.member(jsii_name="countryCode")
    def country_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "countryCode"))

    @country_code.setter
    def country_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df1661501977fb9cb7a038f3b7e928426ec8438d7f803f58cf30d336e5031801)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "countryCode", value)

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @email.setter
    def email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0041e605b3446d5115cde3d90bc2b8128459aac8de1bc7ec974e7bc9b2e89141)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="firstName")
    def first_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firstName"))

    @first_name.setter
    def first_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef8b64aaac0c931518f56418704ba61bfb5c8a790bc0ccf62f1f598d43515234)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firstName", value)

    @builtins.property
    @jsii.member(jsii_name="lastName")
    def last_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastName"))

    @last_name.setter
    def last_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e9f164cc450ba9f77e6f0d22f5e648e3a3bb6d3b503e49a3f1206a807d9c92f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lastName", value)

    @builtins.property
    @jsii.member(jsii_name="organization")
    def organization(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organization"))

    @organization.setter
    def organization(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__461eec30c02c716151435d31b09ce0e68e01c767e2aeb9f59ba15ff8a875d5da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organization", value)

    @builtins.property
    @jsii.member(jsii_name="phone")
    def phone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "phone"))

    @phone.setter
    def phone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d77a5a19fafc01e874233ffc8e7a7804ad8994b089b89efc6ba6aae38ad061fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phone", value)

    @builtins.property
    @jsii.member(jsii_name="postalCode")
    def postal_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "postalCode"))

    @postal_code.setter
    def postal_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c16ca16eb3cc054290878676f0af479881036f94453b419ff151f2cd66f34a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "postalCode", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73c232ce966d71bf6ac628eacee50235daef74b972d51771e5b616c891b65df5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__338f6d4e90b626f705cc53184c916d12bccd608a9bbc12b842cf832377db614e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CpsDvEnrollmentTechContact]:
        return typing.cast(typing.Optional[CpsDvEnrollmentTechContact], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CpsDvEnrollmentTechContact],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a228f4343aefd2eb6cbd01ca057db662e958c0d9b42eaf6a28a8079d3c407176)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.cpsDvEnrollment.CpsDvEnrollmentTimeouts",
    jsii_struct_bases=[],
    name_mapping={"default": "default"},
)
class CpsDvEnrollmentTimeouts:
    def __init__(self, *, default: typing.Optional[builtins.str] = None) -> None:
        '''
        :param default: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#default CpsDvEnrollment#default}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5cc4156985cec7d9b52aa5a0bf22a286b619f17078024ed441d7d4746f9e305b)
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if default is not None:
            self._values["default"] = default

    @builtins.property
    def default(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_dv_enrollment#default CpsDvEnrollment#default}.'''
        result = self._values.get("default")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CpsDvEnrollmentTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CpsDvEnrollmentTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.cpsDvEnrollment.CpsDvEnrollmentTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2f09cd6b46916cba5fdcaf01565415c44a1e2b80651a8ee7f6b2db477affcf08)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c8d6a9baf537aac2494081f29db253119c44ff09894f62827aefefe57b314bd9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CpsDvEnrollmentTimeouts]:
        return typing.cast(typing.Optional[CpsDvEnrollmentTimeouts], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CpsDvEnrollmentTimeouts]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7656656ee512f4b6ed99c6563861f364113fa092b04d4a74ae27b3a61f289ced)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CpsDvEnrollment",
    "CpsDvEnrollmentAdminContact",
    "CpsDvEnrollmentAdminContactOutputReference",
    "CpsDvEnrollmentConfig",
    "CpsDvEnrollmentCsr",
    "CpsDvEnrollmentCsrOutputReference",
    "CpsDvEnrollmentDnsChallenges",
    "CpsDvEnrollmentDnsChallengesList",
    "CpsDvEnrollmentDnsChallengesOutputReference",
    "CpsDvEnrollmentHttpChallenges",
    "CpsDvEnrollmentHttpChallengesList",
    "CpsDvEnrollmentHttpChallengesOutputReference",
    "CpsDvEnrollmentNetworkConfiguration",
    "CpsDvEnrollmentNetworkConfigurationClientMutualAuthentication",
    "CpsDvEnrollmentNetworkConfigurationClientMutualAuthenticationOutputReference",
    "CpsDvEnrollmentNetworkConfigurationOutputReference",
    "CpsDvEnrollmentOrganization",
    "CpsDvEnrollmentOrganizationOutputReference",
    "CpsDvEnrollmentTechContact",
    "CpsDvEnrollmentTechContactOutputReference",
    "CpsDvEnrollmentTimeouts",
    "CpsDvEnrollmentTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__d47d3b6066213b12181792744ba72c90f0bb0f519f95fb7d4495f47e40c14067(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    admin_contact: typing.Union[CpsDvEnrollmentAdminContact, typing.Dict[builtins.str, typing.Any]],
    common_name: builtins.str,
    contract_id: builtins.str,
    csr: typing.Union[CpsDvEnrollmentCsr, typing.Dict[builtins.str, typing.Any]],
    network_configuration: typing.Union[CpsDvEnrollmentNetworkConfiguration, typing.Dict[builtins.str, typing.Any]],
    organization: typing.Union[CpsDvEnrollmentOrganization, typing.Dict[builtins.str, typing.Any]],
    secure_network: builtins.str,
    signature_algorithm: builtins.str,
    sni_only: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    tech_contact: typing.Union[CpsDvEnrollmentTechContact, typing.Dict[builtins.str, typing.Any]],
    acknowledge_pre_verification_warnings: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    allow_duplicate_common_name: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    certificate_chain_type: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    sans: typing.Optional[typing.Sequence[builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[CpsDvEnrollmentTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__d0d651d10022e22f0156895e6cf4e5405cfe0056513e0793f4c3ebb022bab88d(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cac497d9172511b27cfea5c94a2059f39c33f52d5357753a7ea0d68629ad794(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77bd5c980456140e7ba871a827dddebd394fe5a580f1425da9bd09bb392e0c4a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4251bdedfa9850942471d76588481bad48779a3a7f6a5e785e6d8044c927191(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e22ac9d74350257827c64b2c35f2285c0baecb9adb0c272f70f8d148bb4e973(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__879ca8bb06fc39afdffc5866e20a9e9b6fa2b423305b5862b27667eea6a75740(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d862d6f96a6ce9653e57e874782f162405f2bb32c4fbd33fc48d7201744db1d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c9594f01a884375305573c8816443c638e4ae6e4c0d3b455858d394a9244cba(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da77a9499c3f0fdc0ab00d019333c282f7e37ef44c68a09e54b58ed02261a022(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90909a6cbf31717cbc4eb0bb55bc04cf3eeea01379b4461f9c496d2199a1c158(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a47dbc0f0fe5bfdb814954d39df376664598a6ae4c51a4b4c5ae26cb15eafb21(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f99049bc84f189a97341b3bbf868c8293c4d528ed225ceae13869682cc88932(
    *,
    address_line_one: builtins.str,
    city: builtins.str,
    country_code: builtins.str,
    email: builtins.str,
    first_name: builtins.str,
    last_name: builtins.str,
    organization: builtins.str,
    phone: builtins.str,
    postal_code: builtins.str,
    region: builtins.str,
    address_line_two: typing.Optional[builtins.str] = None,
    title: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c9183388eda36dc59b73d9c48995f7cfe9aaaf946a38c47701cb027529b623a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d878036b968fae26a745d2aa6da34934ac7543a93ad4c434682d348e74c25834(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97db2bfb735e09c10d5cbff20adea6189884a7b2586329f5476b3e8b56e31f65(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c519ed4cc2be46e1ceae5efd695de347ac1f987a4f21d2152c6431521b2ef33(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__661f3e15dceffb1e22bb037ba1a131f3043d4d2ff441021fcf66c430154cc737(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61464cc3cab4a6ac39abe6ccb555d72922dab378c3a8e7b4a477de686923d5a8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ef090d6d2aae6a2060960a3da991ef44b5ad218a5a34f0731fa281f18282cc0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b2f9ad6ff7e0608751e19f9d976fd91f2bdf85e2babae4998522da64591ce61(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2266c0cbdd0bd5f66ee73018d06a2445722de80ff2873e5f2e34fca0bc107705(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__509ef31b42a162f8d3d77c9421e5f342144783483f3bbfb9e113cf817efa9407(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75bef00f820cf6aa28006305af8f0c2809c0c978de23478b18495b7f90dbaa0f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e255b86b480ea5498dbc2691179dffff90b58ba0987f0915717543e836f632c0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1532f7f75dd8641df4cd9cd8c5ca580810155e36092ad5793faa5c3870164fb0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6a41cad1c5032e6651141fd1d6174211ca890f8eb106eb18cd5c1cda5068e6f(
    value: typing.Optional[CpsDvEnrollmentAdminContact],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79b472d87d02fee1bb634b8b447b8076651ee2832717e811853842633143dab2(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    admin_contact: typing.Union[CpsDvEnrollmentAdminContact, typing.Dict[builtins.str, typing.Any]],
    common_name: builtins.str,
    contract_id: builtins.str,
    csr: typing.Union[CpsDvEnrollmentCsr, typing.Dict[builtins.str, typing.Any]],
    network_configuration: typing.Union[CpsDvEnrollmentNetworkConfiguration, typing.Dict[builtins.str, typing.Any]],
    organization: typing.Union[CpsDvEnrollmentOrganization, typing.Dict[builtins.str, typing.Any]],
    secure_network: builtins.str,
    signature_algorithm: builtins.str,
    sni_only: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    tech_contact: typing.Union[CpsDvEnrollmentTechContact, typing.Dict[builtins.str, typing.Any]],
    acknowledge_pre_verification_warnings: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    allow_duplicate_common_name: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    certificate_chain_type: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    sans: typing.Optional[typing.Sequence[builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[CpsDvEnrollmentTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5134b460b9fb72a273c7d61f452ee19e0996cb9971a7aeac027d6c1fcc32d50(
    *,
    city: builtins.str,
    country_code: builtins.str,
    organization: builtins.str,
    organizational_unit: typing.Optional[builtins.str] = None,
    preferred_trust_chain: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f51f44ae67c2729219b5365b6c7d7bbaaf34b44798b80321954bddd453f7b495(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75b348890a07e2ade55717439ffe0405363e2619df62d396945e80c49aa37b56(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76430d7dcc52dedb5eac9febc62058e4e370d9c5b70cae91e06d6c7871fdab0f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6784d4d5608220a908dacd17e7be2e00fd7bdbb66ff6b2b67ded8025d7b939ef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c42503d2cb23cf514b26570048c7462c8463ba9f54cdcd7a344f108572d5410(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20be3390dd2e93373e5476118c88cfa37876004f9a0db7829d4d205ff1fa3909(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fe52198391a21d630a5f27c219770c17bb2d327ac228c6bf4bea97ab3cbbb33(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1915ec229ebe79956ed384a0e722f28a8646e2667542480b40f2c31678b79c84(
    value: typing.Optional[CpsDvEnrollmentCsr],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ad5d5ddaf567165aa45cdd81d24233877bb02ba3b955ca1aba894881f841755(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28646549724fd9e2da27971e8c91e6d887feff029ea4d64e86b981c84c12904a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a041d3eaaa89552e88080a473ae62c6fb3f40b28d77a1378105ee4307e9dc72(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a059892ce0fe7124f8402c7745053a7cfecb7fef379f0472f05caf1460b72a24(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88938160f8d52c83488d2d2b2846a65b2f80f7f4370a85ee6ae7972003dc04d6(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c554baaad36b06cd6479bf012470a288c4ab120107f53c08faf3c52bc678c93a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c4a41630f1c45133fd41ebc1485ecb1e210d198616e4e8b817a4e6b95746476(
    value: typing.Optional[CpsDvEnrollmentDnsChallenges],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__147c482dbfde049abcb359afc7db684dc9206380f7c54b5364cee54c23054009(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0102bffd6b685a25718d272e096ed70a2fb4adfdb05980b69429d924ff6abb78(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db22d4072d57302d61149f9ca0448af382938d3d19fe2fbc016e51900254c57a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__012dbb1743e7d8141c76d79ebcd15c67905cbc4d7028251bb3763533dfc92b37(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc131411270c1bec3774830787883fb621eaa5321bb3c1df06c8e9aa0c4c5c45(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2962a7a4543592e28f1b6f628bd4549636960c42086a3d8f3e602e89176c697(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a984c568a2a2d17019b99f403a38516dacdee8a357d4324aed24bf9abad86b63(
    value: typing.Optional[CpsDvEnrollmentHttpChallenges],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__534327d28ca2299c194358cd6ec77934bbb6f2fe995992da87183dcd1518cc84(
    *,
    geography: builtins.str,
    client_mutual_authentication: typing.Optional[typing.Union[CpsDvEnrollmentNetworkConfigurationClientMutualAuthentication, typing.Dict[builtins.str, typing.Any]]] = None,
    clone_dns_names: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    disallowed_tls_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
    must_have_ciphers: typing.Optional[builtins.str] = None,
    ocsp_stapling: typing.Optional[builtins.str] = None,
    preferred_ciphers: typing.Optional[builtins.str] = None,
    quic_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3eeb99cf34f97a9b668267967fe1529019bc09737bf25dc6374b19da8257d613(
    *,
    ocsp_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    send_ca_list_to_client: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    set_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e40beb6845ad2374115cc5fb5b8c5425ae61d4d96c14526f5192a0868f60d4f1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abdb06f6f124dda8bb9b8a1295cea4d7fa7b2532eb7cec8be7619cb68f682700(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1586bbdc8b22eafe9a7224d418d7e231a3e8390fb05e29ce20f2691d49f547b1(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e82610ffd40a351b1830973f777ca0a99bac6959bfdc17575899fa33ff92f39(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a149d4bf6cc68cd68f570b796723bf334e4c34d933ad62c61a24444192256a1(
    value: typing.Optional[CpsDvEnrollmentNetworkConfigurationClientMutualAuthentication],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8481d3bcd32056710ea9cbf33cf094e4f7eef3f36bd479400297b1aa86c2d5d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3226bab4df5d3f7422ec072ed587602b72943f10fa255ba2f9571fa5ed278376(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df97967a9f69b3290b7a3eaf4ef3b061a04100bb33183e9f6a409cbc3f72cc9e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d457e38225939842cd9c0e16ac7c4645105ac98819009f02bd41e21d6c786832(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb1704e2a60d94e5e158bf0c3231288413c7ad43eea19d74755e5a08424a2df6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f32aca30fb40935c442ca47477c9f5014ac39b41aba02eb1e3fe3ee1ad9073b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b24594539d2ee304a5938a605524597767c695c9ee4b398b95a519504bee38ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fea9b32f0cb0070be223d813d3bb5f871126d503e220caedf02985ce0af3527(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48265f40c838cb2016b26db27e133bed617f4f319de299319db791d549a4b52c(
    value: typing.Optional[CpsDvEnrollmentNetworkConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d6124d821572c297acb71fa51a0be88c5a4039d553681d11086e980dd961e32(
    *,
    address_line_one: builtins.str,
    city: builtins.str,
    country_code: builtins.str,
    name: builtins.str,
    phone: builtins.str,
    postal_code: builtins.str,
    region: builtins.str,
    address_line_two: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cda7847aad94d0adfbc5c6388388290fe10800462c2b9ca48893b9ddff04437(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9adf7f202c731068b721a615a3f9cccc3bd0c2e571f2182777cebd2263f3ca3f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e38cd4ef2d8656f3483a68218c0e34a3cc2f18e441b0a712bc546dfeeff33adf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff4f5e8699d8546610e1950bfd9d7a1f1cc00e0b1954bd823759ba93537d2d2e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94312d8f2f982ff047e2e0784cc068825923133f48fc9d6a1e7a1b7e43ffdf78(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fc41f86bf40dee15b508753e32d69d4eb479db98f3d3a354c43aa785d0ca4ec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9229161429f9cbd4506ebfcd760048f2157e36da2f4b883d9ce4c0b48903dfa9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd68ba73859b6525bd81b72f695d5acb5cdfcdaa47bae744705e507b7ff0659f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8c185847e2686d3869c1fcfdf57559c166d410e2c2c6751669dc19a36f8dcd4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00710fb2f4a531572f32cbb87757d317e84ff1d6e852bc7dcc0246fce4630333(
    value: typing.Optional[CpsDvEnrollmentOrganization],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d91a33c8095ccfe7b5ff66a14ecf4467e489895815b9bcd7767e4240811ea09a(
    *,
    address_line_one: builtins.str,
    city: builtins.str,
    country_code: builtins.str,
    email: builtins.str,
    first_name: builtins.str,
    last_name: builtins.str,
    organization: builtins.str,
    phone: builtins.str,
    postal_code: builtins.str,
    region: builtins.str,
    address_line_two: typing.Optional[builtins.str] = None,
    title: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2fed9473cdb0ca245758884f5fee55f2282923f7f2fd0f2226f55bfcec2b456(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__267b005e4d93bc9f7096303ed300ef2961479f70ccf21877aeb2cd54667911d5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f7376b4e0233ab089e93e710faacaa3eac27e1b93662aba775c263455e1afac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9898478bff3ac448f7aa84e589bed4bff81ce7bbd1a067178719ba36493bc20(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df1661501977fb9cb7a038f3b7e928426ec8438d7f803f58cf30d336e5031801(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0041e605b3446d5115cde3d90bc2b8128459aac8de1bc7ec974e7bc9b2e89141(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef8b64aaac0c931518f56418704ba61bfb5c8a790bc0ccf62f1f598d43515234(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e9f164cc450ba9f77e6f0d22f5e648e3a3bb6d3b503e49a3f1206a807d9c92f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__461eec30c02c716151435d31b09ce0e68e01c767e2aeb9f59ba15ff8a875d5da(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d77a5a19fafc01e874233ffc8e7a7804ad8994b089b89efc6ba6aae38ad061fe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c16ca16eb3cc054290878676f0af479881036f94453b419ff151f2cd66f34a6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73c232ce966d71bf6ac628eacee50235daef74b972d51771e5b616c891b65df5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__338f6d4e90b626f705cc53184c916d12bccd608a9bbc12b842cf832377db614e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a228f4343aefd2eb6cbd01ca057db662e958c0d9b42eaf6a28a8079d3c407176(
    value: typing.Optional[CpsDvEnrollmentTechContact],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cc4156985cec7d9b52aa5a0bf22a286b619f17078024ed441d7d4746f9e305b(
    *,
    default: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f09cd6b46916cba5fdcaf01565415c44a1e2b80651a8ee7f6b2db477affcf08(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8d6a9baf537aac2494081f29db253119c44ff09894f62827aefefe57b314bd9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7656656ee512f4b6ed99c6563861f364113fa092b04d4a74ae27b3a61f289ced(
    value: typing.Optional[CpsDvEnrollmentTimeouts],
) -> None:
    """Type checking stubs"""
    pass
