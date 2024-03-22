'''
# `akamai_cps_third_party_enrollment`

Refer to the Terraform Registry for docs: [`akamai_cps_third_party_enrollment`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment).
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


class CpsThirdPartyEnrollment(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.cpsThirdPartyEnrollment.CpsThirdPartyEnrollment",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment akamai_cps_third_party_enrollment}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        admin_contact: typing.Union["CpsThirdPartyEnrollmentAdminContact", typing.Dict[builtins.str, typing.Any]],
        common_name: builtins.str,
        contract_id: builtins.str,
        csr: typing.Union["CpsThirdPartyEnrollmentCsr", typing.Dict[builtins.str, typing.Any]],
        network_configuration: typing.Union["CpsThirdPartyEnrollmentNetworkConfiguration", typing.Dict[builtins.str, typing.Any]],
        organization: typing.Union["CpsThirdPartyEnrollmentOrganization", typing.Dict[builtins.str, typing.Any]],
        secure_network: builtins.str,
        sni_only: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        tech_contact: typing.Union["CpsThirdPartyEnrollmentTechContact", typing.Dict[builtins.str, typing.Any]],
        acknowledge_pre_verification_warnings: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        allow_duplicate_common_name: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        auto_approve_warnings: typing.Optional[typing.Sequence[builtins.str]] = None,
        certificate_chain_type: typing.Optional[builtins.str] = None,
        change_management: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        exclude_sans: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        sans: typing.Optional[typing.Sequence[builtins.str]] = None,
        signature_algorithm: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["CpsThirdPartyEnrollmentTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment akamai_cps_third_party_enrollment} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param admin_contact: admin_contact block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#admin_contact CpsThirdPartyEnrollment#admin_contact}
        :param common_name: Common name used for enrollment. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#common_name CpsThirdPartyEnrollment#common_name}
        :param contract_id: Contract ID for which enrollment is retrieved. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#contract_id CpsThirdPartyEnrollment#contract_id}
        :param csr: csr block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#csr CpsThirdPartyEnrollment#csr}
        :param network_configuration: network_configuration block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#network_configuration CpsThirdPartyEnrollment#network_configuration}
        :param organization: organization block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#organization CpsThirdPartyEnrollment#organization}
        :param secure_network: Type of TLS deployment network. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#secure_network CpsThirdPartyEnrollment#secure_network}
        :param sni_only: Whether Server Name Indication is used for enrollment. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#sni_only CpsThirdPartyEnrollment#sni_only}
        :param tech_contact: tech_contact block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#tech_contact CpsThirdPartyEnrollment#tech_contact}
        :param acknowledge_pre_verification_warnings: Whether acknowledge warnings before certificate verification. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#acknowledge_pre_verification_warnings CpsThirdPartyEnrollment#acknowledge_pre_verification_warnings}
        :param allow_duplicate_common_name: Allow to duplicate common name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#allow_duplicate_common_name CpsThirdPartyEnrollment#allow_duplicate_common_name}
        :param auto_approve_warnings: List of warnings to be automatically approved. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#auto_approve_warnings CpsThirdPartyEnrollment#auto_approve_warnings}
        :param certificate_chain_type: Certificate trust chain type. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#certificate_chain_type CpsThirdPartyEnrollment#certificate_chain_type}
        :param change_management: When set to false, the certificate will be deployed to both staging and production networks. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#change_management CpsThirdPartyEnrollment#change_management}
        :param exclude_sans: When true, SANs are excluded from the CSR. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#exclude_sans CpsThirdPartyEnrollment#exclude_sans}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#id CpsThirdPartyEnrollment#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param sans: List of SANs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#sans CpsThirdPartyEnrollment#sans}
        :param signature_algorithm: The SHA function. Changing this value may require running terraform destroy, terraform apply. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#signature_algorithm CpsThirdPartyEnrollment#signature_algorithm}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#timeouts CpsThirdPartyEnrollment#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8b74227e0e7e49790938892316060da326e71b6dded4597d68c21e7c12b3139)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CpsThirdPartyEnrollmentConfig(
            admin_contact=admin_contact,
            common_name=common_name,
            contract_id=contract_id,
            csr=csr,
            network_configuration=network_configuration,
            organization=organization,
            secure_network=secure_network,
            sni_only=sni_only,
            tech_contact=tech_contact,
            acknowledge_pre_verification_warnings=acknowledge_pre_verification_warnings,
            allow_duplicate_common_name=allow_duplicate_common_name,
            auto_approve_warnings=auto_approve_warnings,
            certificate_chain_type=certificate_chain_type,
            change_management=change_management,
            exclude_sans=exclude_sans,
            id=id,
            sans=sans,
            signature_algorithm=signature_algorithm,
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
        '''Generates CDKTF code for importing a CpsThirdPartyEnrollment resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the CpsThirdPartyEnrollment to import.
        :param import_from_id: The id of the existing CpsThirdPartyEnrollment that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the CpsThirdPartyEnrollment to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a516b2889fe63c98c5417942c409542c755a30470b9d329bd1bc0a37fe14b5a)
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
        :param address_line_one: The address of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#address_line_one CpsThirdPartyEnrollment#address_line_one}
        :param city: City of residence of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#city CpsThirdPartyEnrollment#city}
        :param country_code: Country code of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#country_code CpsThirdPartyEnrollment#country_code}
        :param email: E-mail address of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#email CpsThirdPartyEnrollment#email}
        :param first_name: First name of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#first_name CpsThirdPartyEnrollment#first_name}
        :param last_name: Last name of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#last_name CpsThirdPartyEnrollment#last_name}
        :param organization: Organization where contact is hired. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#organization CpsThirdPartyEnrollment#organization}
        :param phone: Phone number of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#phone CpsThirdPartyEnrollment#phone}
        :param postal_code: Postal code of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#postal_code CpsThirdPartyEnrollment#postal_code}
        :param region: The region of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#region CpsThirdPartyEnrollment#region}
        :param address_line_two: The address of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#address_line_two CpsThirdPartyEnrollment#address_line_two}
        :param title: Title of the the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#title CpsThirdPartyEnrollment#title}
        '''
        value = CpsThirdPartyEnrollmentAdminContact(
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
        :param city: City where organization is located. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#city CpsThirdPartyEnrollment#city}
        :param country_code: The code of the country where organization is located. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#country_code CpsThirdPartyEnrollment#country_code}
        :param organization: Name of organization used in all legal documents. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#organization CpsThirdPartyEnrollment#organization}
        :param organizational_unit: Organizational unit of organization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#organizational_unit CpsThirdPartyEnrollment#organizational_unit}
        :param preferred_trust_chain: For the Let's Encrypt Domain Validated (DV) SAN certificates, the preferred trust chain will be included by CPS with the leaf certificate in the TLS handshake. If the field does not have a value, whichever trust chain Akamai chooses will be used by default Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#preferred_trust_chain CpsThirdPartyEnrollment#preferred_trust_chain}
        :param state: State or province of organization location. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#state CpsThirdPartyEnrollment#state}
        '''
        value = CpsThirdPartyEnrollmentCsr(
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
        client_mutual_authentication: typing.Optional[typing.Union["CpsThirdPartyEnrollmentNetworkConfigurationClientMutualAuthentication", typing.Dict[builtins.str, typing.Any]]] = None,
        clone_dns_names: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        disallowed_tls_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
        must_have_ciphers: typing.Optional[builtins.str] = None,
        ocsp_stapling: typing.Optional[builtins.str] = None,
        preferred_ciphers: typing.Optional[builtins.str] = None,
        quic_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param geography: Geography type used for enrollment. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#geography CpsThirdPartyEnrollment#geography}
        :param client_mutual_authentication: client_mutual_authentication block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#client_mutual_authentication CpsThirdPartyEnrollment#client_mutual_authentication}
        :param clone_dns_names: Enable CPS to direct traffic using all the SANs listed in the SANs parameter when enrollment is created. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#clone_dns_names CpsThirdPartyEnrollment#clone_dns_names}
        :param disallowed_tls_versions: TLS versions which are disallowed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#disallowed_tls_versions CpsThirdPartyEnrollment#disallowed_tls_versions}
        :param must_have_ciphers: Mandatory Ciphers which are included for enrollment. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#must_have_ciphers CpsThirdPartyEnrollment#must_have_ciphers}
        :param ocsp_stapling: Enable OCSP stapling. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#ocsp_stapling CpsThirdPartyEnrollment#ocsp_stapling}
        :param preferred_ciphers: Preferred Ciphers which are included for enrollment. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#preferred_ciphers CpsThirdPartyEnrollment#preferred_ciphers}
        :param quic_enabled: Enable QUIC protocol. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#quic_enabled CpsThirdPartyEnrollment#quic_enabled}
        '''
        value = CpsThirdPartyEnrollmentNetworkConfiguration(
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
        :param address_line_one: The address of organization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#address_line_one CpsThirdPartyEnrollment#address_line_one}
        :param city: City of organization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#city CpsThirdPartyEnrollment#city}
        :param country_code: Country code of organization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#country_code CpsThirdPartyEnrollment#country_code}
        :param name: Name of organization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#name CpsThirdPartyEnrollment#name}
        :param phone: Phone number of organization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#phone CpsThirdPartyEnrollment#phone}
        :param postal_code: Postal code of organization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#postal_code CpsThirdPartyEnrollment#postal_code}
        :param region: The region of organization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#region CpsThirdPartyEnrollment#region}
        :param address_line_two: The address of organization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#address_line_two CpsThirdPartyEnrollment#address_line_two}
        '''
        value = CpsThirdPartyEnrollmentOrganization(
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
        :param address_line_one: The address of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#address_line_one CpsThirdPartyEnrollment#address_line_one}
        :param city: City of residence of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#city CpsThirdPartyEnrollment#city}
        :param country_code: Country code of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#country_code CpsThirdPartyEnrollment#country_code}
        :param email: E-mail address of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#email CpsThirdPartyEnrollment#email}
        :param first_name: First name of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#first_name CpsThirdPartyEnrollment#first_name}
        :param last_name: Last name of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#last_name CpsThirdPartyEnrollment#last_name}
        :param organization: Organization where contact is hired. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#organization CpsThirdPartyEnrollment#organization}
        :param phone: Phone number of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#phone CpsThirdPartyEnrollment#phone}
        :param postal_code: Postal code of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#postal_code CpsThirdPartyEnrollment#postal_code}
        :param region: The region of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#region CpsThirdPartyEnrollment#region}
        :param address_line_two: The address of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#address_line_two CpsThirdPartyEnrollment#address_line_two}
        :param title: Title of the the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#title CpsThirdPartyEnrollment#title}
        '''
        value = CpsThirdPartyEnrollmentTechContact(
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
        :param default: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#default CpsThirdPartyEnrollment#default}.
        '''
        value = CpsThirdPartyEnrollmentTimeouts(default=default)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAcknowledgePreVerificationWarnings")
    def reset_acknowledge_pre_verification_warnings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcknowledgePreVerificationWarnings", []))

    @jsii.member(jsii_name="resetAllowDuplicateCommonName")
    def reset_allow_duplicate_common_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowDuplicateCommonName", []))

    @jsii.member(jsii_name="resetAutoApproveWarnings")
    def reset_auto_approve_warnings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoApproveWarnings", []))

    @jsii.member(jsii_name="resetCertificateChainType")
    def reset_certificate_chain_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateChainType", []))

    @jsii.member(jsii_name="resetChangeManagement")
    def reset_change_management(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetChangeManagement", []))

    @jsii.member(jsii_name="resetExcludeSans")
    def reset_exclude_sans(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludeSans", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSans")
    def reset_sans(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSans", []))

    @jsii.member(jsii_name="resetSignatureAlgorithm")
    def reset_signature_algorithm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSignatureAlgorithm", []))

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
    def admin_contact(self) -> "CpsThirdPartyEnrollmentAdminContactOutputReference":
        return typing.cast("CpsThirdPartyEnrollmentAdminContactOutputReference", jsii.get(self, "adminContact"))

    @builtins.property
    @jsii.member(jsii_name="csr")
    def csr(self) -> "CpsThirdPartyEnrollmentCsrOutputReference":
        return typing.cast("CpsThirdPartyEnrollmentCsrOutputReference", jsii.get(self, "csr"))

    @builtins.property
    @jsii.member(jsii_name="networkConfiguration")
    def network_configuration(
        self,
    ) -> "CpsThirdPartyEnrollmentNetworkConfigurationOutputReference":
        return typing.cast("CpsThirdPartyEnrollmentNetworkConfigurationOutputReference", jsii.get(self, "networkConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="organization")
    def organization(self) -> "CpsThirdPartyEnrollmentOrganizationOutputReference":
        return typing.cast("CpsThirdPartyEnrollmentOrganizationOutputReference", jsii.get(self, "organization"))

    @builtins.property
    @jsii.member(jsii_name="techContact")
    def tech_contact(self) -> "CpsThirdPartyEnrollmentTechContactOutputReference":
        return typing.cast("CpsThirdPartyEnrollmentTechContactOutputReference", jsii.get(self, "techContact"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "CpsThirdPartyEnrollmentTimeoutsOutputReference":
        return typing.cast("CpsThirdPartyEnrollmentTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="acknowledgePreVerificationWarningsInput")
    def acknowledge_pre_verification_warnings_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "acknowledgePreVerificationWarningsInput"))

    @builtins.property
    @jsii.member(jsii_name="adminContactInput")
    def admin_contact_input(
        self,
    ) -> typing.Optional["CpsThirdPartyEnrollmentAdminContact"]:
        return typing.cast(typing.Optional["CpsThirdPartyEnrollmentAdminContact"], jsii.get(self, "adminContactInput"))

    @builtins.property
    @jsii.member(jsii_name="allowDuplicateCommonNameInput")
    def allow_duplicate_common_name_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allowDuplicateCommonNameInput"))

    @builtins.property
    @jsii.member(jsii_name="autoApproveWarningsInput")
    def auto_approve_warnings_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "autoApproveWarningsInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateChainTypeInput")
    def certificate_chain_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateChainTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="changeManagementInput")
    def change_management_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "changeManagementInput"))

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
    def csr_input(self) -> typing.Optional["CpsThirdPartyEnrollmentCsr"]:
        return typing.cast(typing.Optional["CpsThirdPartyEnrollmentCsr"], jsii.get(self, "csrInput"))

    @builtins.property
    @jsii.member(jsii_name="excludeSansInput")
    def exclude_sans_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "excludeSansInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="networkConfigurationInput")
    def network_configuration_input(
        self,
    ) -> typing.Optional["CpsThirdPartyEnrollmentNetworkConfiguration"]:
        return typing.cast(typing.Optional["CpsThirdPartyEnrollmentNetworkConfiguration"], jsii.get(self, "networkConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="organizationInput")
    def organization_input(
        self,
    ) -> typing.Optional["CpsThirdPartyEnrollmentOrganization"]:
        return typing.cast(typing.Optional["CpsThirdPartyEnrollmentOrganization"], jsii.get(self, "organizationInput"))

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
    def tech_contact_input(
        self,
    ) -> typing.Optional["CpsThirdPartyEnrollmentTechContact"]:
        return typing.cast(typing.Optional["CpsThirdPartyEnrollmentTechContact"], jsii.get(self, "techContactInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(self) -> typing.Optional["CpsThirdPartyEnrollmentTimeouts"]:
        return typing.cast(typing.Optional["CpsThirdPartyEnrollmentTimeouts"], jsii.get(self, "timeoutsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__43c138b11b5403c4a1856b59a0ce5f7d33b3d795a274dd49b9908a75ab14d58c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__39a4c5990c2abd892168604ae2d66bdd9a3a097ba46761b98be9ce868451638d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowDuplicateCommonName", value)

    @builtins.property
    @jsii.member(jsii_name="autoApproveWarnings")
    def auto_approve_warnings(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "autoApproveWarnings"))

    @auto_approve_warnings.setter
    def auto_approve_warnings(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46dacde178b035b55e8978a368103475fc99621f34cbb54cecf97469716b5694)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoApproveWarnings", value)

    @builtins.property
    @jsii.member(jsii_name="certificateChainType")
    def certificate_chain_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateChainType"))

    @certificate_chain_type.setter
    def certificate_chain_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67aa728f8d86dbf4d930d3563cc8d86899b54beb74bb61db3cf2c7d8b0ae0a99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateChainType", value)

    @builtins.property
    @jsii.member(jsii_name="changeManagement")
    def change_management(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "changeManagement"))

    @change_management.setter
    def change_management(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed365cbb86475db65d4cd83c71625939d021f4de95049680effd75f81ef7dc5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "changeManagement", value)

    @builtins.property
    @jsii.member(jsii_name="commonName")
    def common_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "commonName"))

    @common_name.setter
    def common_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2dcbce18a2eeb3eb3d56234cba4df071331da966644222886aa50849960addd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commonName", value)

    @builtins.property
    @jsii.member(jsii_name="contractId")
    def contract_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contractId"))

    @contract_id.setter
    def contract_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7e99d15d1e32ca8ce68b4c09483d8ab6b19d5ae5162b97131e28b252f73eec0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contractId", value)

    @builtins.property
    @jsii.member(jsii_name="excludeSans")
    def exclude_sans(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "excludeSans"))

    @exclude_sans.setter
    def exclude_sans(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9828d8e2f1a4aed36d6633f08f381273af9d299cc3600df97891a35ffd65b1ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludeSans", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0acd4f12d4dacb2bc64cb1b139ef45aa0e7710547914eef775b1d8248cd0fd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="sans")
    def sans(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sans"))

    @sans.setter
    def sans(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9647669192ffb9a543c914d741064d3f12fe53197b3e820eb189db601d872c6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sans", value)

    @builtins.property
    @jsii.member(jsii_name="secureNetwork")
    def secure_network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secureNetwork"))

    @secure_network.setter
    def secure_network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e21f69529d9ec5f1c394e28af08577e683ee07411e0979abd05fc89da47f14f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secureNetwork", value)

    @builtins.property
    @jsii.member(jsii_name="signatureAlgorithm")
    def signature_algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signatureAlgorithm"))

    @signature_algorithm.setter
    def signature_algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37082e6869cb65b70a0752cc61fa578099bbdc71f3dbd43fd9bc0e32fd5836aa)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7c3a238aef9af1b357782ae69796bfaa68b3da9f3528d7c3c25e84aa6fd949d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sniOnly", value)


@jsii.data_type(
    jsii_type="akamai.cpsThirdPartyEnrollment.CpsThirdPartyEnrollmentAdminContact",
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
class CpsThirdPartyEnrollmentAdminContact:
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
        :param address_line_one: The address of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#address_line_one CpsThirdPartyEnrollment#address_line_one}
        :param city: City of residence of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#city CpsThirdPartyEnrollment#city}
        :param country_code: Country code of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#country_code CpsThirdPartyEnrollment#country_code}
        :param email: E-mail address of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#email CpsThirdPartyEnrollment#email}
        :param first_name: First name of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#first_name CpsThirdPartyEnrollment#first_name}
        :param last_name: Last name of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#last_name CpsThirdPartyEnrollment#last_name}
        :param organization: Organization where contact is hired. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#organization CpsThirdPartyEnrollment#organization}
        :param phone: Phone number of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#phone CpsThirdPartyEnrollment#phone}
        :param postal_code: Postal code of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#postal_code CpsThirdPartyEnrollment#postal_code}
        :param region: The region of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#region CpsThirdPartyEnrollment#region}
        :param address_line_two: The address of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#address_line_two CpsThirdPartyEnrollment#address_line_two}
        :param title: Title of the the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#title CpsThirdPartyEnrollment#title}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db1d34aeee8136866a1bdc617b60060395e9f410e65b1a8acbf0dfdaac776779)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#address_line_one CpsThirdPartyEnrollment#address_line_one}
        '''
        result = self._values.get("address_line_one")
        assert result is not None, "Required property 'address_line_one' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def city(self) -> builtins.str:
        '''City of residence of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#city CpsThirdPartyEnrollment#city}
        '''
        result = self._values.get("city")
        assert result is not None, "Required property 'city' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def country_code(self) -> builtins.str:
        '''Country code of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#country_code CpsThirdPartyEnrollment#country_code}
        '''
        result = self._values.get("country_code")
        assert result is not None, "Required property 'country_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def email(self) -> builtins.str:
        '''E-mail address of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#email CpsThirdPartyEnrollment#email}
        '''
        result = self._values.get("email")
        assert result is not None, "Required property 'email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def first_name(self) -> builtins.str:
        '''First name of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#first_name CpsThirdPartyEnrollment#first_name}
        '''
        result = self._values.get("first_name")
        assert result is not None, "Required property 'first_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def last_name(self) -> builtins.str:
        '''Last name of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#last_name CpsThirdPartyEnrollment#last_name}
        '''
        result = self._values.get("last_name")
        assert result is not None, "Required property 'last_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def organization(self) -> builtins.str:
        '''Organization where contact is hired.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#organization CpsThirdPartyEnrollment#organization}
        '''
        result = self._values.get("organization")
        assert result is not None, "Required property 'organization' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def phone(self) -> builtins.str:
        '''Phone number of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#phone CpsThirdPartyEnrollment#phone}
        '''
        result = self._values.get("phone")
        assert result is not None, "Required property 'phone' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def postal_code(self) -> builtins.str:
        '''Postal code of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#postal_code CpsThirdPartyEnrollment#postal_code}
        '''
        result = self._values.get("postal_code")
        assert result is not None, "Required property 'postal_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''The region of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#region CpsThirdPartyEnrollment#region}
        '''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def address_line_two(self) -> typing.Optional[builtins.str]:
        '''The address of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#address_line_two CpsThirdPartyEnrollment#address_line_two}
        '''
        result = self._values.get("address_line_two")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''Title of the the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#title CpsThirdPartyEnrollment#title}
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CpsThirdPartyEnrollmentAdminContact(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CpsThirdPartyEnrollmentAdminContactOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.cpsThirdPartyEnrollment.CpsThirdPartyEnrollmentAdminContactOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__65c52a792ddb474cbddf4f7432daee6602d252fdc2cca07cd2f304b49858bf2e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8b6f544a0f2588115042b954b0f615b0c824aebce39372a067da986345e16947)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addressLineOne", value)

    @builtins.property
    @jsii.member(jsii_name="addressLineTwo")
    def address_line_two(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "addressLineTwo"))

    @address_line_two.setter
    def address_line_two(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1694ad3b022735c9a7ee99a58e32888ec3fca33f177e73d7606148ae8d6643d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addressLineTwo", value)

    @builtins.property
    @jsii.member(jsii_name="city")
    def city(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "city"))

    @city.setter
    def city(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e3b5495e941df28f4797b52aa08d84e69f02a6ec6034b462d4f56417f84d633)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "city", value)

    @builtins.property
    @jsii.member(jsii_name="countryCode")
    def country_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "countryCode"))

    @country_code.setter
    def country_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f17f6b09386392080b09c633a5cf0d74d943eca32610e7042713f28ae4446d41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "countryCode", value)

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @email.setter
    def email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a566436e879630edac32f53d6b605c9a025a9222a746e60bf3e227d0c12c242)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="firstName")
    def first_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firstName"))

    @first_name.setter
    def first_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b4eabe3406a6f274f943c3b25d2486e8d0e53a10a8a6496cfe6d76a2119f588)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firstName", value)

    @builtins.property
    @jsii.member(jsii_name="lastName")
    def last_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastName"))

    @last_name.setter
    def last_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51d878e3200f56da5e57467a1e8bd93640bf128afada27533ac3da9d852e3bb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lastName", value)

    @builtins.property
    @jsii.member(jsii_name="organization")
    def organization(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organization"))

    @organization.setter
    def organization(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__786bb08554e2ddb079fcf8dc4e69bc9255fc1ef8509c4131cd8d7d11e4945e5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organization", value)

    @builtins.property
    @jsii.member(jsii_name="phone")
    def phone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "phone"))

    @phone.setter
    def phone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13221ba626ea7939d5088d42a57816e441ad50db492dcf307a3f9c2f98d89a8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phone", value)

    @builtins.property
    @jsii.member(jsii_name="postalCode")
    def postal_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "postalCode"))

    @postal_code.setter
    def postal_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b038bcc0b47c63d84e337404cee7702001142062710ccb838344b480ff40ea7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "postalCode", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__158488385793407db6399d65d29700e481f8d4a0d5eca2733577322e209a0267)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__789585320adc6c45e47a2e1fc7e7a35632691bd2bf8944e356f2685727fa50a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CpsThirdPartyEnrollmentAdminContact]:
        return typing.cast(typing.Optional[CpsThirdPartyEnrollmentAdminContact], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CpsThirdPartyEnrollmentAdminContact],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b46c7dd94abcc03b87bb495a302673777a02795c7774ac45e1f9209cf71d255a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.cpsThirdPartyEnrollment.CpsThirdPartyEnrollmentConfig",
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
        "sni_only": "sniOnly",
        "tech_contact": "techContact",
        "acknowledge_pre_verification_warnings": "acknowledgePreVerificationWarnings",
        "allow_duplicate_common_name": "allowDuplicateCommonName",
        "auto_approve_warnings": "autoApproveWarnings",
        "certificate_chain_type": "certificateChainType",
        "change_management": "changeManagement",
        "exclude_sans": "excludeSans",
        "id": "id",
        "sans": "sans",
        "signature_algorithm": "signatureAlgorithm",
        "timeouts": "timeouts",
    },
)
class CpsThirdPartyEnrollmentConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        admin_contact: typing.Union[CpsThirdPartyEnrollmentAdminContact, typing.Dict[builtins.str, typing.Any]],
        common_name: builtins.str,
        contract_id: builtins.str,
        csr: typing.Union["CpsThirdPartyEnrollmentCsr", typing.Dict[builtins.str, typing.Any]],
        network_configuration: typing.Union["CpsThirdPartyEnrollmentNetworkConfiguration", typing.Dict[builtins.str, typing.Any]],
        organization: typing.Union["CpsThirdPartyEnrollmentOrganization", typing.Dict[builtins.str, typing.Any]],
        secure_network: builtins.str,
        sni_only: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        tech_contact: typing.Union["CpsThirdPartyEnrollmentTechContact", typing.Dict[builtins.str, typing.Any]],
        acknowledge_pre_verification_warnings: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        allow_duplicate_common_name: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        auto_approve_warnings: typing.Optional[typing.Sequence[builtins.str]] = None,
        certificate_chain_type: typing.Optional[builtins.str] = None,
        change_management: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        exclude_sans: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        sans: typing.Optional[typing.Sequence[builtins.str]] = None,
        signature_algorithm: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["CpsThirdPartyEnrollmentTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param admin_contact: admin_contact block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#admin_contact CpsThirdPartyEnrollment#admin_contact}
        :param common_name: Common name used for enrollment. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#common_name CpsThirdPartyEnrollment#common_name}
        :param contract_id: Contract ID for which enrollment is retrieved. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#contract_id CpsThirdPartyEnrollment#contract_id}
        :param csr: csr block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#csr CpsThirdPartyEnrollment#csr}
        :param network_configuration: network_configuration block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#network_configuration CpsThirdPartyEnrollment#network_configuration}
        :param organization: organization block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#organization CpsThirdPartyEnrollment#organization}
        :param secure_network: Type of TLS deployment network. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#secure_network CpsThirdPartyEnrollment#secure_network}
        :param sni_only: Whether Server Name Indication is used for enrollment. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#sni_only CpsThirdPartyEnrollment#sni_only}
        :param tech_contact: tech_contact block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#tech_contact CpsThirdPartyEnrollment#tech_contact}
        :param acknowledge_pre_verification_warnings: Whether acknowledge warnings before certificate verification. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#acknowledge_pre_verification_warnings CpsThirdPartyEnrollment#acknowledge_pre_verification_warnings}
        :param allow_duplicate_common_name: Allow to duplicate common name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#allow_duplicate_common_name CpsThirdPartyEnrollment#allow_duplicate_common_name}
        :param auto_approve_warnings: List of warnings to be automatically approved. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#auto_approve_warnings CpsThirdPartyEnrollment#auto_approve_warnings}
        :param certificate_chain_type: Certificate trust chain type. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#certificate_chain_type CpsThirdPartyEnrollment#certificate_chain_type}
        :param change_management: When set to false, the certificate will be deployed to both staging and production networks. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#change_management CpsThirdPartyEnrollment#change_management}
        :param exclude_sans: When true, SANs are excluded from the CSR. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#exclude_sans CpsThirdPartyEnrollment#exclude_sans}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#id CpsThirdPartyEnrollment#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param sans: List of SANs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#sans CpsThirdPartyEnrollment#sans}
        :param signature_algorithm: The SHA function. Changing this value may require running terraform destroy, terraform apply. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#signature_algorithm CpsThirdPartyEnrollment#signature_algorithm}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#timeouts CpsThirdPartyEnrollment#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(admin_contact, dict):
            admin_contact = CpsThirdPartyEnrollmentAdminContact(**admin_contact)
        if isinstance(csr, dict):
            csr = CpsThirdPartyEnrollmentCsr(**csr)
        if isinstance(network_configuration, dict):
            network_configuration = CpsThirdPartyEnrollmentNetworkConfiguration(**network_configuration)
        if isinstance(organization, dict):
            organization = CpsThirdPartyEnrollmentOrganization(**organization)
        if isinstance(tech_contact, dict):
            tech_contact = CpsThirdPartyEnrollmentTechContact(**tech_contact)
        if isinstance(timeouts, dict):
            timeouts = CpsThirdPartyEnrollmentTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c908b3ec6234c956266abb51c0a50e019a56d618eee0d7d358768d649951c61)
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
            check_type(argname="argument sni_only", value=sni_only, expected_type=type_hints["sni_only"])
            check_type(argname="argument tech_contact", value=tech_contact, expected_type=type_hints["tech_contact"])
            check_type(argname="argument acknowledge_pre_verification_warnings", value=acknowledge_pre_verification_warnings, expected_type=type_hints["acknowledge_pre_verification_warnings"])
            check_type(argname="argument allow_duplicate_common_name", value=allow_duplicate_common_name, expected_type=type_hints["allow_duplicate_common_name"])
            check_type(argname="argument auto_approve_warnings", value=auto_approve_warnings, expected_type=type_hints["auto_approve_warnings"])
            check_type(argname="argument certificate_chain_type", value=certificate_chain_type, expected_type=type_hints["certificate_chain_type"])
            check_type(argname="argument change_management", value=change_management, expected_type=type_hints["change_management"])
            check_type(argname="argument exclude_sans", value=exclude_sans, expected_type=type_hints["exclude_sans"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument sans", value=sans, expected_type=type_hints["sans"])
            check_type(argname="argument signature_algorithm", value=signature_algorithm, expected_type=type_hints["signature_algorithm"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "admin_contact": admin_contact,
            "common_name": common_name,
            "contract_id": contract_id,
            "csr": csr,
            "network_configuration": network_configuration,
            "organization": organization,
            "secure_network": secure_network,
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
        if auto_approve_warnings is not None:
            self._values["auto_approve_warnings"] = auto_approve_warnings
        if certificate_chain_type is not None:
            self._values["certificate_chain_type"] = certificate_chain_type
        if change_management is not None:
            self._values["change_management"] = change_management
        if exclude_sans is not None:
            self._values["exclude_sans"] = exclude_sans
        if id is not None:
            self._values["id"] = id
        if sans is not None:
            self._values["sans"] = sans
        if signature_algorithm is not None:
            self._values["signature_algorithm"] = signature_algorithm
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
    def admin_contact(self) -> CpsThirdPartyEnrollmentAdminContact:
        '''admin_contact block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#admin_contact CpsThirdPartyEnrollment#admin_contact}
        '''
        result = self._values.get("admin_contact")
        assert result is not None, "Required property 'admin_contact' is missing"
        return typing.cast(CpsThirdPartyEnrollmentAdminContact, result)

    @builtins.property
    def common_name(self) -> builtins.str:
        '''Common name used for enrollment.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#common_name CpsThirdPartyEnrollment#common_name}
        '''
        result = self._values.get("common_name")
        assert result is not None, "Required property 'common_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def contract_id(self) -> builtins.str:
        '''Contract ID for which enrollment is retrieved.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#contract_id CpsThirdPartyEnrollment#contract_id}
        '''
        result = self._values.get("contract_id")
        assert result is not None, "Required property 'contract_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def csr(self) -> "CpsThirdPartyEnrollmentCsr":
        '''csr block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#csr CpsThirdPartyEnrollment#csr}
        '''
        result = self._values.get("csr")
        assert result is not None, "Required property 'csr' is missing"
        return typing.cast("CpsThirdPartyEnrollmentCsr", result)

    @builtins.property
    def network_configuration(self) -> "CpsThirdPartyEnrollmentNetworkConfiguration":
        '''network_configuration block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#network_configuration CpsThirdPartyEnrollment#network_configuration}
        '''
        result = self._values.get("network_configuration")
        assert result is not None, "Required property 'network_configuration' is missing"
        return typing.cast("CpsThirdPartyEnrollmentNetworkConfiguration", result)

    @builtins.property
    def organization(self) -> "CpsThirdPartyEnrollmentOrganization":
        '''organization block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#organization CpsThirdPartyEnrollment#organization}
        '''
        result = self._values.get("organization")
        assert result is not None, "Required property 'organization' is missing"
        return typing.cast("CpsThirdPartyEnrollmentOrganization", result)

    @builtins.property
    def secure_network(self) -> builtins.str:
        '''Type of TLS deployment network.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#secure_network CpsThirdPartyEnrollment#secure_network}
        '''
        result = self._values.get("secure_network")
        assert result is not None, "Required property 'secure_network' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sni_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Whether Server Name Indication is used for enrollment.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#sni_only CpsThirdPartyEnrollment#sni_only}
        '''
        result = self._values.get("sni_only")
        assert result is not None, "Required property 'sni_only' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def tech_contact(self) -> "CpsThirdPartyEnrollmentTechContact":
        '''tech_contact block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#tech_contact CpsThirdPartyEnrollment#tech_contact}
        '''
        result = self._values.get("tech_contact")
        assert result is not None, "Required property 'tech_contact' is missing"
        return typing.cast("CpsThirdPartyEnrollmentTechContact", result)

    @builtins.property
    def acknowledge_pre_verification_warnings(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether acknowledge warnings before certificate verification.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#acknowledge_pre_verification_warnings CpsThirdPartyEnrollment#acknowledge_pre_verification_warnings}
        '''
        result = self._values.get("acknowledge_pre_verification_warnings")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def allow_duplicate_common_name(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Allow to duplicate common name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#allow_duplicate_common_name CpsThirdPartyEnrollment#allow_duplicate_common_name}
        '''
        result = self._values.get("allow_duplicate_common_name")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def auto_approve_warnings(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of warnings to be automatically approved.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#auto_approve_warnings CpsThirdPartyEnrollment#auto_approve_warnings}
        '''
        result = self._values.get("auto_approve_warnings")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def certificate_chain_type(self) -> typing.Optional[builtins.str]:
        '''Certificate trust chain type.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#certificate_chain_type CpsThirdPartyEnrollment#certificate_chain_type}
        '''
        result = self._values.get("certificate_chain_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def change_management(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''When set to false, the certificate will be deployed to both staging and production networks.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#change_management CpsThirdPartyEnrollment#change_management}
        '''
        result = self._values.get("change_management")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def exclude_sans(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''When true, SANs are excluded from the CSR.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#exclude_sans CpsThirdPartyEnrollment#exclude_sans}
        '''
        result = self._values.get("exclude_sans")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#id CpsThirdPartyEnrollment#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sans(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of SANs.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#sans CpsThirdPartyEnrollment#sans}
        '''
        result = self._values.get("sans")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def signature_algorithm(self) -> typing.Optional[builtins.str]:
        '''The SHA function. Changing this value may require running terraform destroy, terraform apply.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#signature_algorithm CpsThirdPartyEnrollment#signature_algorithm}
        '''
        result = self._values.get("signature_algorithm")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["CpsThirdPartyEnrollmentTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#timeouts CpsThirdPartyEnrollment#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["CpsThirdPartyEnrollmentTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CpsThirdPartyEnrollmentConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.cpsThirdPartyEnrollment.CpsThirdPartyEnrollmentCsr",
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
class CpsThirdPartyEnrollmentCsr:
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
        :param city: City where organization is located. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#city CpsThirdPartyEnrollment#city}
        :param country_code: The code of the country where organization is located. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#country_code CpsThirdPartyEnrollment#country_code}
        :param organization: Name of organization used in all legal documents. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#organization CpsThirdPartyEnrollment#organization}
        :param organizational_unit: Organizational unit of organization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#organizational_unit CpsThirdPartyEnrollment#organizational_unit}
        :param preferred_trust_chain: For the Let's Encrypt Domain Validated (DV) SAN certificates, the preferred trust chain will be included by CPS with the leaf certificate in the TLS handshake. If the field does not have a value, whichever trust chain Akamai chooses will be used by default Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#preferred_trust_chain CpsThirdPartyEnrollment#preferred_trust_chain}
        :param state: State or province of organization location. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#state CpsThirdPartyEnrollment#state}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbac853f4202f632f65b59f7b82403a49e426450f5522e3582f5e52574c2c8ad)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#city CpsThirdPartyEnrollment#city}
        '''
        result = self._values.get("city")
        assert result is not None, "Required property 'city' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def country_code(self) -> builtins.str:
        '''The code of the country where organization is located.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#country_code CpsThirdPartyEnrollment#country_code}
        '''
        result = self._values.get("country_code")
        assert result is not None, "Required property 'country_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def organization(self) -> builtins.str:
        '''Name of organization used in all legal documents.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#organization CpsThirdPartyEnrollment#organization}
        '''
        result = self._values.get("organization")
        assert result is not None, "Required property 'organization' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def organizational_unit(self) -> typing.Optional[builtins.str]:
        '''Organizational unit of organization.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#organizational_unit CpsThirdPartyEnrollment#organizational_unit}
        '''
        result = self._values.get("organizational_unit")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preferred_trust_chain(self) -> typing.Optional[builtins.str]:
        '''For the Let's Encrypt Domain Validated (DV) SAN certificates, the preferred trust chain will be included by CPS with the leaf certificate in the TLS handshake.

        If the field does not have a value, whichever trust chain Akamai chooses will be used by default

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#preferred_trust_chain CpsThirdPartyEnrollment#preferred_trust_chain}
        '''
        result = self._values.get("preferred_trust_chain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''State or province of organization location.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#state CpsThirdPartyEnrollment#state}
        '''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CpsThirdPartyEnrollmentCsr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CpsThirdPartyEnrollmentCsrOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.cpsThirdPartyEnrollment.CpsThirdPartyEnrollmentCsrOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b0c7dc6ea06951a8369d847116ed8d58986f7e24ee5d1301c41f6d55d0add38e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ee0084fc7b7517dda0e46ee7b12a16738982322e9f5a9ca329ba46acc2da876c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "city", value)

    @builtins.property
    @jsii.member(jsii_name="countryCode")
    def country_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "countryCode"))

    @country_code.setter
    def country_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e10ece55c75a92bd779f7eaee5edd47e56ee55a4b20cc5def3f7a8e807e0e53b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "countryCode", value)

    @builtins.property
    @jsii.member(jsii_name="organization")
    def organization(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organization"))

    @organization.setter
    def organization(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f610b8c9e60e3ba32d3f780ade53f2b9d6551f85c6b1b951bf9925d42268c630)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organization", value)

    @builtins.property
    @jsii.member(jsii_name="organizationalUnit")
    def organizational_unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organizationalUnit"))

    @organizational_unit.setter
    def organizational_unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9029790a6033dfb4e4cef92daf53a262647b77fe28847592976189fa539fcbfd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organizationalUnit", value)

    @builtins.property
    @jsii.member(jsii_name="preferredTrustChain")
    def preferred_trust_chain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "preferredTrustChain"))

    @preferred_trust_chain.setter
    def preferred_trust_chain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f67806278c73acafdf87c45870133ae8d6aa8cf3927feccbed7f6908ca57760f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredTrustChain", value)

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @state.setter
    def state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d28a2153edbe4d36492996149f993a2abf2a0d399aad9aaad20a2f348e33dee5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CpsThirdPartyEnrollmentCsr]:
        return typing.cast(typing.Optional[CpsThirdPartyEnrollmentCsr], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CpsThirdPartyEnrollmentCsr],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__107b62487e7d36a6577fbc553cc3c0b16f97235ce3fe68311171794f8c33d769)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.cpsThirdPartyEnrollment.CpsThirdPartyEnrollmentNetworkConfiguration",
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
class CpsThirdPartyEnrollmentNetworkConfiguration:
    def __init__(
        self,
        *,
        geography: builtins.str,
        client_mutual_authentication: typing.Optional[typing.Union["CpsThirdPartyEnrollmentNetworkConfigurationClientMutualAuthentication", typing.Dict[builtins.str, typing.Any]]] = None,
        clone_dns_names: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        disallowed_tls_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
        must_have_ciphers: typing.Optional[builtins.str] = None,
        ocsp_stapling: typing.Optional[builtins.str] = None,
        preferred_ciphers: typing.Optional[builtins.str] = None,
        quic_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param geography: Geography type used for enrollment. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#geography CpsThirdPartyEnrollment#geography}
        :param client_mutual_authentication: client_mutual_authentication block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#client_mutual_authentication CpsThirdPartyEnrollment#client_mutual_authentication}
        :param clone_dns_names: Enable CPS to direct traffic using all the SANs listed in the SANs parameter when enrollment is created. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#clone_dns_names CpsThirdPartyEnrollment#clone_dns_names}
        :param disallowed_tls_versions: TLS versions which are disallowed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#disallowed_tls_versions CpsThirdPartyEnrollment#disallowed_tls_versions}
        :param must_have_ciphers: Mandatory Ciphers which are included for enrollment. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#must_have_ciphers CpsThirdPartyEnrollment#must_have_ciphers}
        :param ocsp_stapling: Enable OCSP stapling. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#ocsp_stapling CpsThirdPartyEnrollment#ocsp_stapling}
        :param preferred_ciphers: Preferred Ciphers which are included for enrollment. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#preferred_ciphers CpsThirdPartyEnrollment#preferred_ciphers}
        :param quic_enabled: Enable QUIC protocol. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#quic_enabled CpsThirdPartyEnrollment#quic_enabled}
        '''
        if isinstance(client_mutual_authentication, dict):
            client_mutual_authentication = CpsThirdPartyEnrollmentNetworkConfigurationClientMutualAuthentication(**client_mutual_authentication)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c2625fad337ccc0a4703d491fd5849b94a8d20bdeabcca215c9eb6f865a3dbe)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#geography CpsThirdPartyEnrollment#geography}
        '''
        result = self._values.get("geography")
        assert result is not None, "Required property 'geography' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_mutual_authentication(
        self,
    ) -> typing.Optional["CpsThirdPartyEnrollmentNetworkConfigurationClientMutualAuthentication"]:
        '''client_mutual_authentication block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#client_mutual_authentication CpsThirdPartyEnrollment#client_mutual_authentication}
        '''
        result = self._values.get("client_mutual_authentication")
        return typing.cast(typing.Optional["CpsThirdPartyEnrollmentNetworkConfigurationClientMutualAuthentication"], result)

    @builtins.property
    def clone_dns_names(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Enable CPS to direct traffic using all the SANs listed in the SANs parameter when enrollment is created.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#clone_dns_names CpsThirdPartyEnrollment#clone_dns_names}
        '''
        result = self._values.get("clone_dns_names")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def disallowed_tls_versions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''TLS versions which are disallowed.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#disallowed_tls_versions CpsThirdPartyEnrollment#disallowed_tls_versions}
        '''
        result = self._values.get("disallowed_tls_versions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def must_have_ciphers(self) -> typing.Optional[builtins.str]:
        '''Mandatory Ciphers which are included for enrollment.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#must_have_ciphers CpsThirdPartyEnrollment#must_have_ciphers}
        '''
        result = self._values.get("must_have_ciphers")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ocsp_stapling(self) -> typing.Optional[builtins.str]:
        '''Enable OCSP stapling.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#ocsp_stapling CpsThirdPartyEnrollment#ocsp_stapling}
        '''
        result = self._values.get("ocsp_stapling")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preferred_ciphers(self) -> typing.Optional[builtins.str]:
        '''Preferred Ciphers which are included for enrollment.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#preferred_ciphers CpsThirdPartyEnrollment#preferred_ciphers}
        '''
        result = self._values.get("preferred_ciphers")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def quic_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Enable QUIC protocol.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#quic_enabled CpsThirdPartyEnrollment#quic_enabled}
        '''
        result = self._values.get("quic_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CpsThirdPartyEnrollmentNetworkConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.cpsThirdPartyEnrollment.CpsThirdPartyEnrollmentNetworkConfigurationClientMutualAuthentication",
    jsii_struct_bases=[],
    name_mapping={
        "ocsp_enabled": "ocspEnabled",
        "send_ca_list_to_client": "sendCaListToClient",
        "set_id": "setId",
    },
)
class CpsThirdPartyEnrollmentNetworkConfigurationClientMutualAuthentication:
    def __init__(
        self,
        *,
        ocsp_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        send_ca_list_to_client: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        set_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ocsp_enabled: Enable OCSP stapling. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#ocsp_enabled CpsThirdPartyEnrollment#ocsp_enabled}
        :param send_ca_list_to_client: Enable the server to send the certificate authority (CA) list to the client. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#send_ca_list_to_client CpsThirdPartyEnrollment#send_ca_list_to_client}
        :param set_id: The identifier of the set of trust chains, created in the Trust Chain Manager. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#set_id CpsThirdPartyEnrollment#set_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__407981548a9ec497f56a3539dd1503c4ac29542d067ce27ee5186002cc3d0755)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#ocsp_enabled CpsThirdPartyEnrollment#ocsp_enabled}
        '''
        result = self._values.get("ocsp_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def send_ca_list_to_client(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Enable the server to send the certificate authority (CA) list to the client.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#send_ca_list_to_client CpsThirdPartyEnrollment#send_ca_list_to_client}
        '''
        result = self._values.get("send_ca_list_to_client")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def set_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of the set of trust chains, created in the Trust Chain Manager.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#set_id CpsThirdPartyEnrollment#set_id}
        '''
        result = self._values.get("set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CpsThirdPartyEnrollmentNetworkConfigurationClientMutualAuthentication(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CpsThirdPartyEnrollmentNetworkConfigurationClientMutualAuthenticationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.cpsThirdPartyEnrollment.CpsThirdPartyEnrollmentNetworkConfigurationClientMutualAuthenticationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cb55cfb7e5367f6ef6dc086338def62f30ceafbaf7538b549aaaa30c48b95adb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7e6b058feae80c0a950fed6ea9f1930e3c5e9198a574d4084fb9e22b90b2057c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3c2163992b708f7ff3903c9231a6e719416b47f93634138770b7b712865620e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sendCaListToClient", value)

    @builtins.property
    @jsii.member(jsii_name="setId")
    def set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "setId"))

    @set_id.setter
    def set_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e840a4ce7a98c5786d3c5cb5bac105949c759fda132256db2c0374793dda11d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "setId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CpsThirdPartyEnrollmentNetworkConfigurationClientMutualAuthentication]:
        return typing.cast(typing.Optional[CpsThirdPartyEnrollmentNetworkConfigurationClientMutualAuthentication], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CpsThirdPartyEnrollmentNetworkConfigurationClientMutualAuthentication],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22a5f97b9934bf1ccd01de2f52c3460c44174af9d4fb6a8b3c72515355b77036)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CpsThirdPartyEnrollmentNetworkConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.cpsThirdPartyEnrollment.CpsThirdPartyEnrollmentNetworkConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__de701672dc8921152b67e255f42ab8a94263e4aee5e05431dca892249a640244)
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
        :param ocsp_enabled: Enable OCSP stapling. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#ocsp_enabled CpsThirdPartyEnrollment#ocsp_enabled}
        :param send_ca_list_to_client: Enable the server to send the certificate authority (CA) list to the client. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#send_ca_list_to_client CpsThirdPartyEnrollment#send_ca_list_to_client}
        :param set_id: The identifier of the set of trust chains, created in the Trust Chain Manager. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#set_id CpsThirdPartyEnrollment#set_id}
        '''
        value = CpsThirdPartyEnrollmentNetworkConfigurationClientMutualAuthentication(
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
    ) -> CpsThirdPartyEnrollmentNetworkConfigurationClientMutualAuthenticationOutputReference:
        return typing.cast(CpsThirdPartyEnrollmentNetworkConfigurationClientMutualAuthenticationOutputReference, jsii.get(self, "clientMutualAuthentication"))

    @builtins.property
    @jsii.member(jsii_name="clientMutualAuthenticationInput")
    def client_mutual_authentication_input(
        self,
    ) -> typing.Optional[CpsThirdPartyEnrollmentNetworkConfigurationClientMutualAuthentication]:
        return typing.cast(typing.Optional[CpsThirdPartyEnrollmentNetworkConfigurationClientMutualAuthentication], jsii.get(self, "clientMutualAuthenticationInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__6f4e665e812d5e54d99b54aa6b7c9cde5b099d5b76843bc44f3f51d1e8175a4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloneDnsNames", value)

    @builtins.property
    @jsii.member(jsii_name="disallowedTlsVersions")
    def disallowed_tls_versions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "disallowedTlsVersions"))

    @disallowed_tls_versions.setter
    def disallowed_tls_versions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f386804308fca6c9b6d647393d7ffa151e924be3f007ea59cc422a2bcd196a61)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disallowedTlsVersions", value)

    @builtins.property
    @jsii.member(jsii_name="geography")
    def geography(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "geography"))

    @geography.setter
    def geography(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__851192180e50a10d0c7598b14f5218364ea8c48f08f1be7217b7fdc4c9e7ef43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "geography", value)

    @builtins.property
    @jsii.member(jsii_name="mustHaveCiphers")
    def must_have_ciphers(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mustHaveCiphers"))

    @must_have_ciphers.setter
    def must_have_ciphers(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a9bdae9fb21f4bc75b17fa1e0f27edc98672409252d92b82a6dec8251e69a90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mustHaveCiphers", value)

    @builtins.property
    @jsii.member(jsii_name="ocspStapling")
    def ocsp_stapling(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ocspStapling"))

    @ocsp_stapling.setter
    def ocsp_stapling(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c08e6e2d4557ba20afd9cb0402488464830c8a6cac612353c44b1d42f1519f4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ocspStapling", value)

    @builtins.property
    @jsii.member(jsii_name="preferredCiphers")
    def preferred_ciphers(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "preferredCiphers"))

    @preferred_ciphers.setter
    def preferred_ciphers(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6f4910cff2470cad37158ea2670224d699faa59c62cb8509c6821942ec0e054)
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
            type_hints = typing.get_type_hints(_typecheckingstub__73c0f47213e2dac377c1d2d3d2515c0bc9969c6b996f29cb315875451c9d17c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "quicEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CpsThirdPartyEnrollmentNetworkConfiguration]:
        return typing.cast(typing.Optional[CpsThirdPartyEnrollmentNetworkConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CpsThirdPartyEnrollmentNetworkConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d1b7d9ec2a66026e258f6b65d0532aeba6f4537c635e78643d0f4e8aa9ddd33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.cpsThirdPartyEnrollment.CpsThirdPartyEnrollmentOrganization",
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
class CpsThirdPartyEnrollmentOrganization:
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
        :param address_line_one: The address of organization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#address_line_one CpsThirdPartyEnrollment#address_line_one}
        :param city: City of organization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#city CpsThirdPartyEnrollment#city}
        :param country_code: Country code of organization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#country_code CpsThirdPartyEnrollment#country_code}
        :param name: Name of organization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#name CpsThirdPartyEnrollment#name}
        :param phone: Phone number of organization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#phone CpsThirdPartyEnrollment#phone}
        :param postal_code: Postal code of organization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#postal_code CpsThirdPartyEnrollment#postal_code}
        :param region: The region of organization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#region CpsThirdPartyEnrollment#region}
        :param address_line_two: The address of organization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#address_line_two CpsThirdPartyEnrollment#address_line_two}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ddeea747da7a2cc8468200c16ece1097e7a3802942f538372bec247b23a1d8d)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#address_line_one CpsThirdPartyEnrollment#address_line_one}
        '''
        result = self._values.get("address_line_one")
        assert result is not None, "Required property 'address_line_one' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def city(self) -> builtins.str:
        '''City of organization.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#city CpsThirdPartyEnrollment#city}
        '''
        result = self._values.get("city")
        assert result is not None, "Required property 'city' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def country_code(self) -> builtins.str:
        '''Country code of organization.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#country_code CpsThirdPartyEnrollment#country_code}
        '''
        result = self._values.get("country_code")
        assert result is not None, "Required property 'country_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of organization.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#name CpsThirdPartyEnrollment#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def phone(self) -> builtins.str:
        '''Phone number of organization.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#phone CpsThirdPartyEnrollment#phone}
        '''
        result = self._values.get("phone")
        assert result is not None, "Required property 'phone' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def postal_code(self) -> builtins.str:
        '''Postal code of organization.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#postal_code CpsThirdPartyEnrollment#postal_code}
        '''
        result = self._values.get("postal_code")
        assert result is not None, "Required property 'postal_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''The region of organization.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#region CpsThirdPartyEnrollment#region}
        '''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def address_line_two(self) -> typing.Optional[builtins.str]:
        '''The address of organization.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#address_line_two CpsThirdPartyEnrollment#address_line_two}
        '''
        result = self._values.get("address_line_two")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CpsThirdPartyEnrollmentOrganization(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CpsThirdPartyEnrollmentOrganizationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.cpsThirdPartyEnrollment.CpsThirdPartyEnrollmentOrganizationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6ace5a99750732ddde0f6f7c6a3f3ef92d3f9894e5a55a5744a5ac9c6b1d8983)
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
            type_hints = typing.get_type_hints(_typecheckingstub__298efd8c60151c75ff8520e60aa41f2945d3d94e1b5b3582460b4edc0b9d9ebd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addressLineOne", value)

    @builtins.property
    @jsii.member(jsii_name="addressLineTwo")
    def address_line_two(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "addressLineTwo"))

    @address_line_two.setter
    def address_line_two(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7984529a8721ba9fc7a120bdf98ff6388d4e65b84150cedadf7e3a81b7871caa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addressLineTwo", value)

    @builtins.property
    @jsii.member(jsii_name="city")
    def city(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "city"))

    @city.setter
    def city(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2802623e9ae2e6d79040fac838b4664a53fdfa3168ac87ef143f8755e5ac50e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "city", value)

    @builtins.property
    @jsii.member(jsii_name="countryCode")
    def country_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "countryCode"))

    @country_code.setter
    def country_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f42b9581b923eafc1e662df6e93fd1d5d2f8a3a30cb0a0d0bee7f1d4b4d8c604)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "countryCode", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb40ef09b640ca0f8598f5293f2b757f452029ddafdea9c91ec0bbde8a5576a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="phone")
    def phone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "phone"))

    @phone.setter
    def phone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aeae4a2bbaeaa53173bd20d9554732ee1b64e774478332b16c33aca4f5d0e517)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phone", value)

    @builtins.property
    @jsii.member(jsii_name="postalCode")
    def postal_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "postalCode"))

    @postal_code.setter
    def postal_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed7392751d941b3caf01508305a695d841a67e96cdbc46fb35222af1ae5629e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "postalCode", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1be83b25e730a28d99b1ef6e6c6e0031c1cc87ee5e7c8189b3678d64bf498a86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CpsThirdPartyEnrollmentOrganization]:
        return typing.cast(typing.Optional[CpsThirdPartyEnrollmentOrganization], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CpsThirdPartyEnrollmentOrganization],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85de2c1e25a54517041a4b7279aeab9f1172fab64ffc3fc5a44f3de6b0aac4fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.cpsThirdPartyEnrollment.CpsThirdPartyEnrollmentTechContact",
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
class CpsThirdPartyEnrollmentTechContact:
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
        :param address_line_one: The address of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#address_line_one CpsThirdPartyEnrollment#address_line_one}
        :param city: City of residence of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#city CpsThirdPartyEnrollment#city}
        :param country_code: Country code of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#country_code CpsThirdPartyEnrollment#country_code}
        :param email: E-mail address of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#email CpsThirdPartyEnrollment#email}
        :param first_name: First name of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#first_name CpsThirdPartyEnrollment#first_name}
        :param last_name: Last name of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#last_name CpsThirdPartyEnrollment#last_name}
        :param organization: Organization where contact is hired. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#organization CpsThirdPartyEnrollment#organization}
        :param phone: Phone number of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#phone CpsThirdPartyEnrollment#phone}
        :param postal_code: Postal code of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#postal_code CpsThirdPartyEnrollment#postal_code}
        :param region: The region of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#region CpsThirdPartyEnrollment#region}
        :param address_line_two: The address of the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#address_line_two CpsThirdPartyEnrollment#address_line_two}
        :param title: Title of the the contact. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#title CpsThirdPartyEnrollment#title}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a05870f218bb6bee422cf8c37a8cd929c1985ff3c5d2583321b7500c01011a4)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#address_line_one CpsThirdPartyEnrollment#address_line_one}
        '''
        result = self._values.get("address_line_one")
        assert result is not None, "Required property 'address_line_one' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def city(self) -> builtins.str:
        '''City of residence of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#city CpsThirdPartyEnrollment#city}
        '''
        result = self._values.get("city")
        assert result is not None, "Required property 'city' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def country_code(self) -> builtins.str:
        '''Country code of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#country_code CpsThirdPartyEnrollment#country_code}
        '''
        result = self._values.get("country_code")
        assert result is not None, "Required property 'country_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def email(self) -> builtins.str:
        '''E-mail address of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#email CpsThirdPartyEnrollment#email}
        '''
        result = self._values.get("email")
        assert result is not None, "Required property 'email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def first_name(self) -> builtins.str:
        '''First name of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#first_name CpsThirdPartyEnrollment#first_name}
        '''
        result = self._values.get("first_name")
        assert result is not None, "Required property 'first_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def last_name(self) -> builtins.str:
        '''Last name of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#last_name CpsThirdPartyEnrollment#last_name}
        '''
        result = self._values.get("last_name")
        assert result is not None, "Required property 'last_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def organization(self) -> builtins.str:
        '''Organization where contact is hired.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#organization CpsThirdPartyEnrollment#organization}
        '''
        result = self._values.get("organization")
        assert result is not None, "Required property 'organization' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def phone(self) -> builtins.str:
        '''Phone number of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#phone CpsThirdPartyEnrollment#phone}
        '''
        result = self._values.get("phone")
        assert result is not None, "Required property 'phone' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def postal_code(self) -> builtins.str:
        '''Postal code of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#postal_code CpsThirdPartyEnrollment#postal_code}
        '''
        result = self._values.get("postal_code")
        assert result is not None, "Required property 'postal_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''The region of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#region CpsThirdPartyEnrollment#region}
        '''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def address_line_two(self) -> typing.Optional[builtins.str]:
        '''The address of the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#address_line_two CpsThirdPartyEnrollment#address_line_two}
        '''
        result = self._values.get("address_line_two")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''Title of the the contact.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#title CpsThirdPartyEnrollment#title}
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CpsThirdPartyEnrollmentTechContact(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CpsThirdPartyEnrollmentTechContactOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.cpsThirdPartyEnrollment.CpsThirdPartyEnrollmentTechContactOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9daa0bc8032fa0e062ee34d037df58ae108dcf11eb32d5ebec266e8ae3cd1330)
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
            type_hints = typing.get_type_hints(_typecheckingstub__eda2cbb9780265dd7732fdef5d962ef5c6dfc669bbef56e3feecc4cf3706512f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addressLineOne", value)

    @builtins.property
    @jsii.member(jsii_name="addressLineTwo")
    def address_line_two(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "addressLineTwo"))

    @address_line_two.setter
    def address_line_two(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93047b93d95f15842ac2e016485744ae4ac9f213b5dce4b4dba23f1fde38d081)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addressLineTwo", value)

    @builtins.property
    @jsii.member(jsii_name="city")
    def city(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "city"))

    @city.setter
    def city(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2dde532db3d6632f40156144ec9f29690dfbe253c5aef02f044fe4d72f0944cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "city", value)

    @builtins.property
    @jsii.member(jsii_name="countryCode")
    def country_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "countryCode"))

    @country_code.setter
    def country_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b9438b9750dab3eed6d183ed85dd7a5d225d830d58a7cdd6771997c689cb623)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "countryCode", value)

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @email.setter
    def email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e6ce139d5a715ac8bff13ab125403f2adb072ac5a46fddd61da3d70d62125fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="firstName")
    def first_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firstName"))

    @first_name.setter
    def first_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12494fa6df8396fafd9155f1abe8fdc55afc4536993de705c63898ebb5ce646c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firstName", value)

    @builtins.property
    @jsii.member(jsii_name="lastName")
    def last_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastName"))

    @last_name.setter
    def last_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__686e200c5f8d88ef3a5a8a3ba574234c25082a93077fe347a21bc542b7bc05f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lastName", value)

    @builtins.property
    @jsii.member(jsii_name="organization")
    def organization(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organization"))

    @organization.setter
    def organization(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f164330d29133bdedcaf52175ffae8449078533f3e3272dff18a3d1f320c2e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organization", value)

    @builtins.property
    @jsii.member(jsii_name="phone")
    def phone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "phone"))

    @phone.setter
    def phone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0235b5556ef459db3d6c49608e30c243abb8552204eb97f8b710d2978b028f05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phone", value)

    @builtins.property
    @jsii.member(jsii_name="postalCode")
    def postal_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "postalCode"))

    @postal_code.setter
    def postal_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__958f11252f3c8d49f98edef507ab33fb8964161778bda1041d693e1ae49e1813)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "postalCode", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2cccb8c82744d8bee0c7749e51c90b06a8cf8878b5e11111dc119771efc15af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__833d92bf89b35e1bc6e6fb1a4131c3a39c834242d1e968aa0015c578439fc6e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CpsThirdPartyEnrollmentTechContact]:
        return typing.cast(typing.Optional[CpsThirdPartyEnrollmentTechContact], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CpsThirdPartyEnrollmentTechContact],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40f975c640e3b79c3ff8224a97dc8655242e401cf2b317b68ae5b6408efa078e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.cpsThirdPartyEnrollment.CpsThirdPartyEnrollmentTimeouts",
    jsii_struct_bases=[],
    name_mapping={"default": "default"},
)
class CpsThirdPartyEnrollmentTimeouts:
    def __init__(self, *, default: typing.Optional[builtins.str] = None) -> None:
        '''
        :param default: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#default CpsThirdPartyEnrollment#default}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2ded53378b5d6584f1e940ad217d336e26b1cbc7d65e7d5dba3c3daefa451ee)
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if default is not None:
            self._values["default"] = default

    @builtins.property
    def default(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/cps_third_party_enrollment#default CpsThirdPartyEnrollment#default}.'''
        result = self._values.get("default")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CpsThirdPartyEnrollmentTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CpsThirdPartyEnrollmentTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.cpsThirdPartyEnrollment.CpsThirdPartyEnrollmentTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6a37ad3822f000a9cd517e10ef706b5e5246349264522619f20c36e5bafbc394)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0398a125197c3f9d4542c435b9b9807d8643cf457c3d49c826acbfe7c1c6a59d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CpsThirdPartyEnrollmentTimeouts]:
        return typing.cast(typing.Optional[CpsThirdPartyEnrollmentTimeouts], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CpsThirdPartyEnrollmentTimeouts],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1661bf31d0cb46f4dd5c401fd736975c439ca8ca934124e923ed68e1aa4a4bea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CpsThirdPartyEnrollment",
    "CpsThirdPartyEnrollmentAdminContact",
    "CpsThirdPartyEnrollmentAdminContactOutputReference",
    "CpsThirdPartyEnrollmentConfig",
    "CpsThirdPartyEnrollmentCsr",
    "CpsThirdPartyEnrollmentCsrOutputReference",
    "CpsThirdPartyEnrollmentNetworkConfiguration",
    "CpsThirdPartyEnrollmentNetworkConfigurationClientMutualAuthentication",
    "CpsThirdPartyEnrollmentNetworkConfigurationClientMutualAuthenticationOutputReference",
    "CpsThirdPartyEnrollmentNetworkConfigurationOutputReference",
    "CpsThirdPartyEnrollmentOrganization",
    "CpsThirdPartyEnrollmentOrganizationOutputReference",
    "CpsThirdPartyEnrollmentTechContact",
    "CpsThirdPartyEnrollmentTechContactOutputReference",
    "CpsThirdPartyEnrollmentTimeouts",
    "CpsThirdPartyEnrollmentTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__a8b74227e0e7e49790938892316060da326e71b6dded4597d68c21e7c12b3139(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    admin_contact: typing.Union[CpsThirdPartyEnrollmentAdminContact, typing.Dict[builtins.str, typing.Any]],
    common_name: builtins.str,
    contract_id: builtins.str,
    csr: typing.Union[CpsThirdPartyEnrollmentCsr, typing.Dict[builtins.str, typing.Any]],
    network_configuration: typing.Union[CpsThirdPartyEnrollmentNetworkConfiguration, typing.Dict[builtins.str, typing.Any]],
    organization: typing.Union[CpsThirdPartyEnrollmentOrganization, typing.Dict[builtins.str, typing.Any]],
    secure_network: builtins.str,
    sni_only: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    tech_contact: typing.Union[CpsThirdPartyEnrollmentTechContact, typing.Dict[builtins.str, typing.Any]],
    acknowledge_pre_verification_warnings: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    allow_duplicate_common_name: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    auto_approve_warnings: typing.Optional[typing.Sequence[builtins.str]] = None,
    certificate_chain_type: typing.Optional[builtins.str] = None,
    change_management: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    exclude_sans: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    sans: typing.Optional[typing.Sequence[builtins.str]] = None,
    signature_algorithm: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[CpsThirdPartyEnrollmentTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__5a516b2889fe63c98c5417942c409542c755a30470b9d329bd1bc0a37fe14b5a(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43c138b11b5403c4a1856b59a0ce5f7d33b3d795a274dd49b9908a75ab14d58c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39a4c5990c2abd892168604ae2d66bdd9a3a097ba46761b98be9ce868451638d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46dacde178b035b55e8978a368103475fc99621f34cbb54cecf97469716b5694(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67aa728f8d86dbf4d930d3563cc8d86899b54beb74bb61db3cf2c7d8b0ae0a99(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed365cbb86475db65d4cd83c71625939d021f4de95049680effd75f81ef7dc5c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2dcbce18a2eeb3eb3d56234cba4df071331da966644222886aa50849960addd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7e99d15d1e32ca8ce68b4c09483d8ab6b19d5ae5162b97131e28b252f73eec0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9828d8e2f1a4aed36d6633f08f381273af9d299cc3600df97891a35ffd65b1ca(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0acd4f12d4dacb2bc64cb1b139ef45aa0e7710547914eef775b1d8248cd0fd6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9647669192ffb9a543c914d741064d3f12fe53197b3e820eb189db601d872c6e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e21f69529d9ec5f1c394e28af08577e683ee07411e0979abd05fc89da47f14f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37082e6869cb65b70a0752cc61fa578099bbdc71f3dbd43fd9bc0e32fd5836aa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c3a238aef9af1b357782ae69796bfaa68b3da9f3528d7c3c25e84aa6fd949d1(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db1d34aeee8136866a1bdc617b60060395e9f410e65b1a8acbf0dfdaac776779(
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

def _typecheckingstub__65c52a792ddb474cbddf4f7432daee6602d252fdc2cca07cd2f304b49858bf2e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b6f544a0f2588115042b954b0f615b0c824aebce39372a067da986345e16947(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1694ad3b022735c9a7ee99a58e32888ec3fca33f177e73d7606148ae8d6643d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e3b5495e941df28f4797b52aa08d84e69f02a6ec6034b462d4f56417f84d633(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f17f6b09386392080b09c633a5cf0d74d943eca32610e7042713f28ae4446d41(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a566436e879630edac32f53d6b605c9a025a9222a746e60bf3e227d0c12c242(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b4eabe3406a6f274f943c3b25d2486e8d0e53a10a8a6496cfe6d76a2119f588(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51d878e3200f56da5e57467a1e8bd93640bf128afada27533ac3da9d852e3bb5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__786bb08554e2ddb079fcf8dc4e69bc9255fc1ef8509c4131cd8d7d11e4945e5d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13221ba626ea7939d5088d42a57816e441ad50db492dcf307a3f9c2f98d89a8f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b038bcc0b47c63d84e337404cee7702001142062710ccb838344b480ff40ea7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__158488385793407db6399d65d29700e481f8d4a0d5eca2733577322e209a0267(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__789585320adc6c45e47a2e1fc7e7a35632691bd2bf8944e356f2685727fa50a1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b46c7dd94abcc03b87bb495a302673777a02795c7774ac45e1f9209cf71d255a(
    value: typing.Optional[CpsThirdPartyEnrollmentAdminContact],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c908b3ec6234c956266abb51c0a50e019a56d618eee0d7d358768d649951c61(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    admin_contact: typing.Union[CpsThirdPartyEnrollmentAdminContact, typing.Dict[builtins.str, typing.Any]],
    common_name: builtins.str,
    contract_id: builtins.str,
    csr: typing.Union[CpsThirdPartyEnrollmentCsr, typing.Dict[builtins.str, typing.Any]],
    network_configuration: typing.Union[CpsThirdPartyEnrollmentNetworkConfiguration, typing.Dict[builtins.str, typing.Any]],
    organization: typing.Union[CpsThirdPartyEnrollmentOrganization, typing.Dict[builtins.str, typing.Any]],
    secure_network: builtins.str,
    sni_only: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    tech_contact: typing.Union[CpsThirdPartyEnrollmentTechContact, typing.Dict[builtins.str, typing.Any]],
    acknowledge_pre_verification_warnings: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    allow_duplicate_common_name: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    auto_approve_warnings: typing.Optional[typing.Sequence[builtins.str]] = None,
    certificate_chain_type: typing.Optional[builtins.str] = None,
    change_management: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    exclude_sans: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    sans: typing.Optional[typing.Sequence[builtins.str]] = None,
    signature_algorithm: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[CpsThirdPartyEnrollmentTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbac853f4202f632f65b59f7b82403a49e426450f5522e3582f5e52574c2c8ad(
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

def _typecheckingstub__b0c7dc6ea06951a8369d847116ed8d58986f7e24ee5d1301c41f6d55d0add38e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee0084fc7b7517dda0e46ee7b12a16738982322e9f5a9ca329ba46acc2da876c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e10ece55c75a92bd779f7eaee5edd47e56ee55a4b20cc5def3f7a8e807e0e53b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f610b8c9e60e3ba32d3f780ade53f2b9d6551f85c6b1b951bf9925d42268c630(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9029790a6033dfb4e4cef92daf53a262647b77fe28847592976189fa539fcbfd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f67806278c73acafdf87c45870133ae8d6aa8cf3927feccbed7f6908ca57760f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d28a2153edbe4d36492996149f993a2abf2a0d399aad9aaad20a2f348e33dee5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__107b62487e7d36a6577fbc553cc3c0b16f97235ce3fe68311171794f8c33d769(
    value: typing.Optional[CpsThirdPartyEnrollmentCsr],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c2625fad337ccc0a4703d491fd5849b94a8d20bdeabcca215c9eb6f865a3dbe(
    *,
    geography: builtins.str,
    client_mutual_authentication: typing.Optional[typing.Union[CpsThirdPartyEnrollmentNetworkConfigurationClientMutualAuthentication, typing.Dict[builtins.str, typing.Any]]] = None,
    clone_dns_names: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    disallowed_tls_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
    must_have_ciphers: typing.Optional[builtins.str] = None,
    ocsp_stapling: typing.Optional[builtins.str] = None,
    preferred_ciphers: typing.Optional[builtins.str] = None,
    quic_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__407981548a9ec497f56a3539dd1503c4ac29542d067ce27ee5186002cc3d0755(
    *,
    ocsp_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    send_ca_list_to_client: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    set_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb55cfb7e5367f6ef6dc086338def62f30ceafbaf7538b549aaaa30c48b95adb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e6b058feae80c0a950fed6ea9f1930e3c5e9198a574d4084fb9e22b90b2057c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c2163992b708f7ff3903c9231a6e719416b47f93634138770b7b712865620e6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e840a4ce7a98c5786d3c5cb5bac105949c759fda132256db2c0374793dda11d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22a5f97b9934bf1ccd01de2f52c3460c44174af9d4fb6a8b3c72515355b77036(
    value: typing.Optional[CpsThirdPartyEnrollmentNetworkConfigurationClientMutualAuthentication],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de701672dc8921152b67e255f42ab8a94263e4aee5e05431dca892249a640244(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f4e665e812d5e54d99b54aa6b7c9cde5b099d5b76843bc44f3f51d1e8175a4f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f386804308fca6c9b6d647393d7ffa151e924be3f007ea59cc422a2bcd196a61(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__851192180e50a10d0c7598b14f5218364ea8c48f08f1be7217b7fdc4c9e7ef43(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a9bdae9fb21f4bc75b17fa1e0f27edc98672409252d92b82a6dec8251e69a90(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c08e6e2d4557ba20afd9cb0402488464830c8a6cac612353c44b1d42f1519f4f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6f4910cff2470cad37158ea2670224d699faa59c62cb8509c6821942ec0e054(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73c0f47213e2dac377c1d2d3d2515c0bc9969c6b996f29cb315875451c9d17c3(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d1b7d9ec2a66026e258f6b65d0532aeba6f4537c635e78643d0f4e8aa9ddd33(
    value: typing.Optional[CpsThirdPartyEnrollmentNetworkConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ddeea747da7a2cc8468200c16ece1097e7a3802942f538372bec247b23a1d8d(
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

def _typecheckingstub__6ace5a99750732ddde0f6f7c6a3f3ef92d3f9894e5a55a5744a5ac9c6b1d8983(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__298efd8c60151c75ff8520e60aa41f2945d3d94e1b5b3582460b4edc0b9d9ebd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7984529a8721ba9fc7a120bdf98ff6388d4e65b84150cedadf7e3a81b7871caa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2802623e9ae2e6d79040fac838b4664a53fdfa3168ac87ef143f8755e5ac50e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f42b9581b923eafc1e662df6e93fd1d5d2f8a3a30cb0a0d0bee7f1d4b4d8c604(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb40ef09b640ca0f8598f5293f2b757f452029ddafdea9c91ec0bbde8a5576a9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aeae4a2bbaeaa53173bd20d9554732ee1b64e774478332b16c33aca4f5d0e517(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed7392751d941b3caf01508305a695d841a67e96cdbc46fb35222af1ae5629e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1be83b25e730a28d99b1ef6e6c6e0031c1cc87ee5e7c8189b3678d64bf498a86(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85de2c1e25a54517041a4b7279aeab9f1172fab64ffc3fc5a44f3de6b0aac4fd(
    value: typing.Optional[CpsThirdPartyEnrollmentOrganization],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a05870f218bb6bee422cf8c37a8cd929c1985ff3c5d2583321b7500c01011a4(
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

def _typecheckingstub__9daa0bc8032fa0e062ee34d037df58ae108dcf11eb32d5ebec266e8ae3cd1330(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eda2cbb9780265dd7732fdef5d962ef5c6dfc669bbef56e3feecc4cf3706512f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93047b93d95f15842ac2e016485744ae4ac9f213b5dce4b4dba23f1fde38d081(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dde532db3d6632f40156144ec9f29690dfbe253c5aef02f044fe4d72f0944cd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b9438b9750dab3eed6d183ed85dd7a5d225d830d58a7cdd6771997c689cb623(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e6ce139d5a715ac8bff13ab125403f2adb072ac5a46fddd61da3d70d62125fc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12494fa6df8396fafd9155f1abe8fdc55afc4536993de705c63898ebb5ce646c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__686e200c5f8d88ef3a5a8a3ba574234c25082a93077fe347a21bc542b7bc05f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f164330d29133bdedcaf52175ffae8449078533f3e3272dff18a3d1f320c2e3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0235b5556ef459db3d6c49608e30c243abb8552204eb97f8b710d2978b028f05(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__958f11252f3c8d49f98edef507ab33fb8964161778bda1041d693e1ae49e1813(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2cccb8c82744d8bee0c7749e51c90b06a8cf8878b5e11111dc119771efc15af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__833d92bf89b35e1bc6e6fb1a4131c3a39c834242d1e968aa0015c578439fc6e3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40f975c640e3b79c3ff8224a97dc8655242e401cf2b317b68ae5b6408efa078e(
    value: typing.Optional[CpsThirdPartyEnrollmentTechContact],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2ded53378b5d6584f1e940ad217d336e26b1cbc7d65e7d5dba3c3daefa451ee(
    *,
    default: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a37ad3822f000a9cd517e10ef706b5e5246349264522619f20c36e5bafbc394(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0398a125197c3f9d4542c435b9b9807d8643cf457c3d49c826acbfe7c1c6a59d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1661bf31d0cb46f4dd5c401fd736975c439ca8ca934124e923ed68e1aa4a4bea(
    value: typing.Optional[CpsThirdPartyEnrollmentTimeouts],
) -> None:
    """Type checking stubs"""
    pass
