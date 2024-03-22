'''
# `akamai_iam_user`

Refer to the Terraform Registry for docs: [`akamai_iam_user`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user).
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


class IamUser(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.iamUser.IamUser",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user akamai_iam_user}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        auth_grants_json: builtins.str,
        country: builtins.str,
        email: builtins.str,
        enable_tfa: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        first_name: builtins.str,
        last_name: builtins.str,
        address: typing.Optional[builtins.str] = None,
        city: typing.Optional[builtins.str] = None,
        contact_type: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        job_title: typing.Optional[builtins.str] = None,
        lock: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        mobile_phone: typing.Optional[builtins.str] = None,
        phone: typing.Optional[builtins.str] = None,
        preferred_language: typing.Optional[builtins.str] = None,
        secondary_email: typing.Optional[builtins.str] = None,
        session_timeout: typing.Optional[jsii.Number] = None,
        state: typing.Optional[builtins.str] = None,
        time_zone: typing.Optional[builtins.str] = None,
        zip_code: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user akamai_iam_user} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param auth_grants_json: A user's per-group role assignments, in JSON form. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#auth_grants_json IamUser#auth_grants_json}
        :param country: As part of the user's location, the value can be any that are available from the view-supported-countries operation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#country IamUser#country}
        :param email: The user's email address. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#email IamUser#email}
        :param enable_tfa: Indicates whether two-factor authentication is allowed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#enable_tfa IamUser#enable_tfa}
        :param first_name: The user's first name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#first_name IamUser#first_name}
        :param last_name: The user's surname. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#last_name IamUser#last_name}
        :param address: The user's street address. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#address IamUser#address}
        :param city: The user's city. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#city IamUser#city}
        :param contact_type: To help characterize the user, the value can be any that are available from the view-contact-types operation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#contact_type IamUser#contact_type}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#id IamUser#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param job_title: The user's position at your company. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#job_title IamUser#job_title}
        :param lock: Flag to block a user account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#lock IamUser#lock}
        :param mobile_phone: The user's mobile phone number. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#mobile_phone IamUser#mobile_phone}
        :param phone: The user's main phone number. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#phone IamUser#phone}
        :param preferred_language: The value can be any that are available from the view-languages operation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#preferred_language IamUser#preferred_language}
        :param secondary_email: The user's secondary email address. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#secondary_email IamUser#secondary_email}
        :param session_timeout: The number of seconds it takes for the user's Control Center session to time out if there hasn't been any activity. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#session_timeout IamUser#session_timeout}
        :param state: The user's state. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#state IamUser#state}
        :param time_zone: The user's time zone. The value can be any that are available from the view-time-zones operation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#time_zone IamUser#time_zone}
        :param zip_code: The user's five-digit ZIP code. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#zip_code IamUser#zip_code}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12af66a7f971010205e2afc3920d5cf9de2495748e0bac33481a2c7107d6683a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = IamUserConfig(
            auth_grants_json=auth_grants_json,
            country=country,
            email=email,
            enable_tfa=enable_tfa,
            first_name=first_name,
            last_name=last_name,
            address=address,
            city=city,
            contact_type=contact_type,
            id=id,
            job_title=job_title,
            lock=lock,
            mobile_phone=mobile_phone,
            phone=phone,
            preferred_language=preferred_language,
            secondary_email=secondary_email,
            session_timeout=session_timeout,
            state=state,
            time_zone=time_zone,
            zip_code=zip_code,
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
        '''Generates CDKTF code for importing a IamUser resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the IamUser to import.
        :param import_from_id: The id of the existing IamUser that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the IamUser to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__637b3a066e617a62532daf169b293a18f016ae3f94101bd06ba9cd551d03271d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetAddress")
    def reset_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddress", []))

    @jsii.member(jsii_name="resetCity")
    def reset_city(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCity", []))

    @jsii.member(jsii_name="resetContactType")
    def reset_contact_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContactType", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetJobTitle")
    def reset_job_title(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJobTitle", []))

    @jsii.member(jsii_name="resetLock")
    def reset_lock(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLock", []))

    @jsii.member(jsii_name="resetMobilePhone")
    def reset_mobile_phone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMobilePhone", []))

    @jsii.member(jsii_name="resetPhone")
    def reset_phone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPhone", []))

    @jsii.member(jsii_name="resetPreferredLanguage")
    def reset_preferred_language(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreferredLanguage", []))

    @jsii.member(jsii_name="resetSecondaryEmail")
    def reset_secondary_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecondaryEmail", []))

    @jsii.member(jsii_name="resetSessionTimeout")
    def reset_session_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSessionTimeout", []))

    @jsii.member(jsii_name="resetState")
    def reset_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetState", []))

    @jsii.member(jsii_name="resetTimeZone")
    def reset_time_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeZone", []))

    @jsii.member(jsii_name="resetZipCode")
    def reset_zip_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZipCode", []))

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
    @jsii.member(jsii_name="emailUpdatePending")
    def email_update_pending(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "emailUpdatePending"))

    @builtins.property
    @jsii.member(jsii_name="lastLogin")
    def last_login(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastLogin"))

    @builtins.property
    @jsii.member(jsii_name="passwordExpiredAfter")
    def password_expired_after(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "passwordExpiredAfter"))

    @builtins.property
    @jsii.member(jsii_name="tfaConfigured")
    def tfa_configured(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "tfaConfigured"))

    @builtins.property
    @jsii.member(jsii_name="userName")
    def user_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userName"))

    @builtins.property
    @jsii.member(jsii_name="addressInput")
    def address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressInput"))

    @builtins.property
    @jsii.member(jsii_name="authGrantsJsonInput")
    def auth_grants_json_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authGrantsJsonInput"))

    @builtins.property
    @jsii.member(jsii_name="cityInput")
    def city_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cityInput"))

    @builtins.property
    @jsii.member(jsii_name="contactTypeInput")
    def contact_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contactTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="countryInput")
    def country_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "countryInput"))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="enableTfaInput")
    def enable_tfa_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableTfaInput"))

    @builtins.property
    @jsii.member(jsii_name="firstNameInput")
    def first_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firstNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="jobTitleInput")
    def job_title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobTitleInput"))

    @builtins.property
    @jsii.member(jsii_name="lastNameInput")
    def last_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lastNameInput"))

    @builtins.property
    @jsii.member(jsii_name="lockInput")
    def lock_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "lockInput"))

    @builtins.property
    @jsii.member(jsii_name="mobilePhoneInput")
    def mobile_phone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mobilePhoneInput"))

    @builtins.property
    @jsii.member(jsii_name="phoneInput")
    def phone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "phoneInput"))

    @builtins.property
    @jsii.member(jsii_name="preferredLanguageInput")
    def preferred_language_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredLanguageInput"))

    @builtins.property
    @jsii.member(jsii_name="secondaryEmailInput")
    def secondary_email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secondaryEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionTimeoutInput")
    def session_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sessionTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="stateInput")
    def state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateInput"))

    @builtins.property
    @jsii.member(jsii_name="timeZoneInput")
    def time_zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeZoneInput"))

    @builtins.property
    @jsii.member(jsii_name="zipCodeInput")
    def zip_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zipCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="address")
    def address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "address"))

    @address.setter
    def address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf93dfb2d7abc25e1a5451b5d96bc5e82768594e3cc00c6e89804a5c85957c53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "address", value)

    @builtins.property
    @jsii.member(jsii_name="authGrantsJson")
    def auth_grants_json(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authGrantsJson"))

    @auth_grants_json.setter
    def auth_grants_json(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdd7d0cf1b4dae9cd56923f01cba20187276bb93985acfd24816d734a21dfd79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authGrantsJson", value)

    @builtins.property
    @jsii.member(jsii_name="city")
    def city(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "city"))

    @city.setter
    def city(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e3cac745b5ad8f6f676ab89713f54d951b36d64f206b1f69ea4a8a58b53852a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "city", value)

    @builtins.property
    @jsii.member(jsii_name="contactType")
    def contact_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contactType"))

    @contact_type.setter
    def contact_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb394b39322d07c9fbb2ed6f8cc1a7c3104f14719fa12c3e2c86b2d10796c6eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contactType", value)

    @builtins.property
    @jsii.member(jsii_name="country")
    def country(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "country"))

    @country.setter
    def country(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__017ca8f64b28bfc6f5009ca62f11e80385a985f2d9601f27688621d96507ea81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "country", value)

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @email.setter
    def email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d200361c724187ef36bde9f0583611cbc1c841951f382cafc45d619b6e2e9bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="enableTfa")
    def enable_tfa(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableTfa"))

    @enable_tfa.setter
    def enable_tfa(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__629f9edccc590768391d5a2d0db598d33d6c035ffdea1f7854c4dddda15f7662)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableTfa", value)

    @builtins.property
    @jsii.member(jsii_name="firstName")
    def first_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firstName"))

    @first_name.setter
    def first_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d703cd2ba4a23c18ed2593f9c529a93274f41c0760402f63bb8fd84360d1b977)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firstName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25eaea8123c4672b024517b86d91b4b43858623155eb0468ce1454961bab21f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="jobTitle")
    def job_title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jobTitle"))

    @job_title.setter
    def job_title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fd5e5d792e3b7b7a7b499f76ee8bf2ca72229de20ff94eba2bd2be866242728)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobTitle", value)

    @builtins.property
    @jsii.member(jsii_name="lastName")
    def last_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastName"))

    @last_name.setter
    def last_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5683a469cbba77af7218f3303c5271c7b651c3516e1b6e135f57fadc6b76e9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lastName", value)

    @builtins.property
    @jsii.member(jsii_name="lock")
    def lock(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "lock"))

    @lock.setter
    def lock(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f978ae403e036c83ca1e70486d2ceaa7fc7313471da747ac444b91e73bb84b80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lock", value)

    @builtins.property
    @jsii.member(jsii_name="mobilePhone")
    def mobile_phone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mobilePhone"))

    @mobile_phone.setter
    def mobile_phone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf142c74f621bd2c9afb3dec484b4a563c5339816432177420babc9cfe1f0f7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mobilePhone", value)

    @builtins.property
    @jsii.member(jsii_name="phone")
    def phone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "phone"))

    @phone.setter
    def phone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70e1bf4a512c514707c8e968ab189792c9e777d3fc462f6e650bdf102a45c9f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phone", value)

    @builtins.property
    @jsii.member(jsii_name="preferredLanguage")
    def preferred_language(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "preferredLanguage"))

    @preferred_language.setter
    def preferred_language(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__520ad98d61a14e592016c6c3d2d7a847eab9fae0b9f35a3d0249e4f74bbfe4e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredLanguage", value)

    @builtins.property
    @jsii.member(jsii_name="secondaryEmail")
    def secondary_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryEmail"))

    @secondary_email.setter
    def secondary_email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05760533addaa7ba4d525992f0beb6cd7c50f1869f197628454314ada21a17f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secondaryEmail", value)

    @builtins.property
    @jsii.member(jsii_name="sessionTimeout")
    def session_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sessionTimeout"))

    @session_timeout.setter
    def session_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e2a793daafaa1c7c37755a1a291a46cd20e70735e4a7979ca98520580aa214d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @state.setter
    def state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fec3da2a260d0f95f06113cd03321622f5865f2a3ee4ff0e69e4da75d28fd526)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @builtins.property
    @jsii.member(jsii_name="timeZone")
    def time_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeZone"))

    @time_zone.setter
    def time_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfaa301c5737d44b150787bb419a30d34a589969f763031f148dea79b9ed743c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeZone", value)

    @builtins.property
    @jsii.member(jsii_name="zipCode")
    def zip_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zipCode"))

    @zip_code.setter
    def zip_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96044bb553393d6101b9af96018bce996c3a920fce84a03382a2c6a74b70972e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zipCode", value)


@jsii.data_type(
    jsii_type="akamai.iamUser.IamUserConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "auth_grants_json": "authGrantsJson",
        "country": "country",
        "email": "email",
        "enable_tfa": "enableTfa",
        "first_name": "firstName",
        "last_name": "lastName",
        "address": "address",
        "city": "city",
        "contact_type": "contactType",
        "id": "id",
        "job_title": "jobTitle",
        "lock": "lock",
        "mobile_phone": "mobilePhone",
        "phone": "phone",
        "preferred_language": "preferredLanguage",
        "secondary_email": "secondaryEmail",
        "session_timeout": "sessionTimeout",
        "state": "state",
        "time_zone": "timeZone",
        "zip_code": "zipCode",
    },
)
class IamUserConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        auth_grants_json: builtins.str,
        country: builtins.str,
        email: builtins.str,
        enable_tfa: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        first_name: builtins.str,
        last_name: builtins.str,
        address: typing.Optional[builtins.str] = None,
        city: typing.Optional[builtins.str] = None,
        contact_type: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        job_title: typing.Optional[builtins.str] = None,
        lock: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        mobile_phone: typing.Optional[builtins.str] = None,
        phone: typing.Optional[builtins.str] = None,
        preferred_language: typing.Optional[builtins.str] = None,
        secondary_email: typing.Optional[builtins.str] = None,
        session_timeout: typing.Optional[jsii.Number] = None,
        state: typing.Optional[builtins.str] = None,
        time_zone: typing.Optional[builtins.str] = None,
        zip_code: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param auth_grants_json: A user's per-group role assignments, in JSON form. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#auth_grants_json IamUser#auth_grants_json}
        :param country: As part of the user's location, the value can be any that are available from the view-supported-countries operation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#country IamUser#country}
        :param email: The user's email address. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#email IamUser#email}
        :param enable_tfa: Indicates whether two-factor authentication is allowed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#enable_tfa IamUser#enable_tfa}
        :param first_name: The user's first name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#first_name IamUser#first_name}
        :param last_name: The user's surname. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#last_name IamUser#last_name}
        :param address: The user's street address. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#address IamUser#address}
        :param city: The user's city. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#city IamUser#city}
        :param contact_type: To help characterize the user, the value can be any that are available from the view-contact-types operation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#contact_type IamUser#contact_type}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#id IamUser#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param job_title: The user's position at your company. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#job_title IamUser#job_title}
        :param lock: Flag to block a user account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#lock IamUser#lock}
        :param mobile_phone: The user's mobile phone number. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#mobile_phone IamUser#mobile_phone}
        :param phone: The user's main phone number. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#phone IamUser#phone}
        :param preferred_language: The value can be any that are available from the view-languages operation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#preferred_language IamUser#preferred_language}
        :param secondary_email: The user's secondary email address. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#secondary_email IamUser#secondary_email}
        :param session_timeout: The number of seconds it takes for the user's Control Center session to time out if there hasn't been any activity. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#session_timeout IamUser#session_timeout}
        :param state: The user's state. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#state IamUser#state}
        :param time_zone: The user's time zone. The value can be any that are available from the view-time-zones operation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#time_zone IamUser#time_zone}
        :param zip_code: The user's five-digit ZIP code. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#zip_code IamUser#zip_code}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86e92c2fcc1969f35de7b9ab5f7a673240ebd4ce6180fd93262be80628dae0d4)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument auth_grants_json", value=auth_grants_json, expected_type=type_hints["auth_grants_json"])
            check_type(argname="argument country", value=country, expected_type=type_hints["country"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument enable_tfa", value=enable_tfa, expected_type=type_hints["enable_tfa"])
            check_type(argname="argument first_name", value=first_name, expected_type=type_hints["first_name"])
            check_type(argname="argument last_name", value=last_name, expected_type=type_hints["last_name"])
            check_type(argname="argument address", value=address, expected_type=type_hints["address"])
            check_type(argname="argument city", value=city, expected_type=type_hints["city"])
            check_type(argname="argument contact_type", value=contact_type, expected_type=type_hints["contact_type"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument job_title", value=job_title, expected_type=type_hints["job_title"])
            check_type(argname="argument lock", value=lock, expected_type=type_hints["lock"])
            check_type(argname="argument mobile_phone", value=mobile_phone, expected_type=type_hints["mobile_phone"])
            check_type(argname="argument phone", value=phone, expected_type=type_hints["phone"])
            check_type(argname="argument preferred_language", value=preferred_language, expected_type=type_hints["preferred_language"])
            check_type(argname="argument secondary_email", value=secondary_email, expected_type=type_hints["secondary_email"])
            check_type(argname="argument session_timeout", value=session_timeout, expected_type=type_hints["session_timeout"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument time_zone", value=time_zone, expected_type=type_hints["time_zone"])
            check_type(argname="argument zip_code", value=zip_code, expected_type=type_hints["zip_code"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "auth_grants_json": auth_grants_json,
            "country": country,
            "email": email,
            "enable_tfa": enable_tfa,
            "first_name": first_name,
            "last_name": last_name,
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
        if address is not None:
            self._values["address"] = address
        if city is not None:
            self._values["city"] = city
        if contact_type is not None:
            self._values["contact_type"] = contact_type
        if id is not None:
            self._values["id"] = id
        if job_title is not None:
            self._values["job_title"] = job_title
        if lock is not None:
            self._values["lock"] = lock
        if mobile_phone is not None:
            self._values["mobile_phone"] = mobile_phone
        if phone is not None:
            self._values["phone"] = phone
        if preferred_language is not None:
            self._values["preferred_language"] = preferred_language
        if secondary_email is not None:
            self._values["secondary_email"] = secondary_email
        if session_timeout is not None:
            self._values["session_timeout"] = session_timeout
        if state is not None:
            self._values["state"] = state
        if time_zone is not None:
            self._values["time_zone"] = time_zone
        if zip_code is not None:
            self._values["zip_code"] = zip_code

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
    def auth_grants_json(self) -> builtins.str:
        '''A user's per-group role assignments, in JSON form.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#auth_grants_json IamUser#auth_grants_json}
        '''
        result = self._values.get("auth_grants_json")
        assert result is not None, "Required property 'auth_grants_json' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def country(self) -> builtins.str:
        '''As part of the user's location, the value can be any that are available from the view-supported-countries operation.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#country IamUser#country}
        '''
        result = self._values.get("country")
        assert result is not None, "Required property 'country' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def email(self) -> builtins.str:
        '''The user's email address.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#email IamUser#email}
        '''
        result = self._values.get("email")
        assert result is not None, "Required property 'email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enable_tfa(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Indicates whether two-factor authentication is allowed.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#enable_tfa IamUser#enable_tfa}
        '''
        result = self._values.get("enable_tfa")
        assert result is not None, "Required property 'enable_tfa' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def first_name(self) -> builtins.str:
        '''The user's first name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#first_name IamUser#first_name}
        '''
        result = self._values.get("first_name")
        assert result is not None, "Required property 'first_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def last_name(self) -> builtins.str:
        '''The user's surname.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#last_name IamUser#last_name}
        '''
        result = self._values.get("last_name")
        assert result is not None, "Required property 'last_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def address(self) -> typing.Optional[builtins.str]:
        '''The user's street address.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#address IamUser#address}
        '''
        result = self._values.get("address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def city(self) -> typing.Optional[builtins.str]:
        '''The user's city.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#city IamUser#city}
        '''
        result = self._values.get("city")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def contact_type(self) -> typing.Optional[builtins.str]:
        '''To help characterize the user, the value can be any that are available from the view-contact-types operation.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#contact_type IamUser#contact_type}
        '''
        result = self._values.get("contact_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#id IamUser#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def job_title(self) -> typing.Optional[builtins.str]:
        '''The user's position at your company.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#job_title IamUser#job_title}
        '''
        result = self._values.get("job_title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lock(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Flag to block a user account.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#lock IamUser#lock}
        '''
        result = self._values.get("lock")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def mobile_phone(self) -> typing.Optional[builtins.str]:
        '''The user's mobile phone number.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#mobile_phone IamUser#mobile_phone}
        '''
        result = self._values.get("mobile_phone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def phone(self) -> typing.Optional[builtins.str]:
        '''The user's main phone number.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#phone IamUser#phone}
        '''
        result = self._values.get("phone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preferred_language(self) -> typing.Optional[builtins.str]:
        '''The value can be any that are available from the view-languages operation.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#preferred_language IamUser#preferred_language}
        '''
        result = self._values.get("preferred_language")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secondary_email(self) -> typing.Optional[builtins.str]:
        '''The user's secondary email address.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#secondary_email IamUser#secondary_email}
        '''
        result = self._values.get("secondary_email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_timeout(self) -> typing.Optional[jsii.Number]:
        '''The number of seconds it takes for the user's Control Center session to time out if there hasn't been any activity.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#session_timeout IamUser#session_timeout}
        '''
        result = self._values.get("session_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''The user's state.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#state IamUser#state}
        '''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_zone(self) -> typing.Optional[builtins.str]:
        '''The user's time zone. The value can be any that are available from the view-time-zones operation.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#time_zone IamUser#time_zone}
        '''
        result = self._values.get("time_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def zip_code(self) -> typing.Optional[builtins.str]:
        '''The user's five-digit ZIP code.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/iam_user#zip_code IamUser#zip_code}
        '''
        result = self._values.get("zip_code")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IamUserConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IamUser",
    "IamUserConfig",
]

publication.publish()

def _typecheckingstub__12af66a7f971010205e2afc3920d5cf9de2495748e0bac33481a2c7107d6683a(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    auth_grants_json: builtins.str,
    country: builtins.str,
    email: builtins.str,
    enable_tfa: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    first_name: builtins.str,
    last_name: builtins.str,
    address: typing.Optional[builtins.str] = None,
    city: typing.Optional[builtins.str] = None,
    contact_type: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    job_title: typing.Optional[builtins.str] = None,
    lock: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    mobile_phone: typing.Optional[builtins.str] = None,
    phone: typing.Optional[builtins.str] = None,
    preferred_language: typing.Optional[builtins.str] = None,
    secondary_email: typing.Optional[builtins.str] = None,
    session_timeout: typing.Optional[jsii.Number] = None,
    state: typing.Optional[builtins.str] = None,
    time_zone: typing.Optional[builtins.str] = None,
    zip_code: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__637b3a066e617a62532daf169b293a18f016ae3f94101bd06ba9cd551d03271d(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf93dfb2d7abc25e1a5451b5d96bc5e82768594e3cc00c6e89804a5c85957c53(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdd7d0cf1b4dae9cd56923f01cba20187276bb93985acfd24816d734a21dfd79(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e3cac745b5ad8f6f676ab89713f54d951b36d64f206b1f69ea4a8a58b53852a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb394b39322d07c9fbb2ed6f8cc1a7c3104f14719fa12c3e2c86b2d10796c6eb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__017ca8f64b28bfc6f5009ca62f11e80385a985f2d9601f27688621d96507ea81(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d200361c724187ef36bde9f0583611cbc1c841951f382cafc45d619b6e2e9bb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__629f9edccc590768391d5a2d0db598d33d6c035ffdea1f7854c4dddda15f7662(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d703cd2ba4a23c18ed2593f9c529a93274f41c0760402f63bb8fd84360d1b977(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25eaea8123c4672b024517b86d91b4b43858623155eb0468ce1454961bab21f2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fd5e5d792e3b7b7a7b499f76ee8bf2ca72229de20ff94eba2bd2be866242728(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5683a469cbba77af7218f3303c5271c7b651c3516e1b6e135f57fadc6b76e9f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f978ae403e036c83ca1e70486d2ceaa7fc7313471da747ac444b91e73bb84b80(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf142c74f621bd2c9afb3dec484b4a563c5339816432177420babc9cfe1f0f7e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70e1bf4a512c514707c8e968ab189792c9e777d3fc462f6e650bdf102a45c9f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__520ad98d61a14e592016c6c3d2d7a847eab9fae0b9f35a3d0249e4f74bbfe4e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05760533addaa7ba4d525992f0beb6cd7c50f1869f197628454314ada21a17f4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e2a793daafaa1c7c37755a1a291a46cd20e70735e4a7979ca98520580aa214d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fec3da2a260d0f95f06113cd03321622f5865f2a3ee4ff0e69e4da75d28fd526(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfaa301c5737d44b150787bb419a30d34a589969f763031f148dea79b9ed743c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96044bb553393d6101b9af96018bce996c3a920fce84a03382a2c6a74b70972e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86e92c2fcc1969f35de7b9ab5f7a673240ebd4ce6180fd93262be80628dae0d4(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    auth_grants_json: builtins.str,
    country: builtins.str,
    email: builtins.str,
    enable_tfa: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    first_name: builtins.str,
    last_name: builtins.str,
    address: typing.Optional[builtins.str] = None,
    city: typing.Optional[builtins.str] = None,
    contact_type: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    job_title: typing.Optional[builtins.str] = None,
    lock: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    mobile_phone: typing.Optional[builtins.str] = None,
    phone: typing.Optional[builtins.str] = None,
    preferred_language: typing.Optional[builtins.str] = None,
    secondary_email: typing.Optional[builtins.str] = None,
    session_timeout: typing.Optional[jsii.Number] = None,
    state: typing.Optional[builtins.str] = None,
    time_zone: typing.Optional[builtins.str] = None,
    zip_code: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
