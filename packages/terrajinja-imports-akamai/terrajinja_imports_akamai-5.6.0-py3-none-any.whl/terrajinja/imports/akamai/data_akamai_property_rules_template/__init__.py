'''
# `data_akamai_property_rules_template`

Refer to the Terraform Registry for docs: [`data_akamai_property_rules_template`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules_template).
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


class DataAkamaiPropertyRulesTemplate(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiPropertyRulesTemplate.DataAkamaiPropertyRulesTemplate",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules_template akamai_property_rules_template}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        id: typing.Optional[builtins.str] = None,
        template: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiPropertyRulesTemplateTemplate", typing.Dict[builtins.str, typing.Any]]]]] = None,
        template_file: typing.Optional[builtins.str] = None,
        var_definition_file: typing.Optional[builtins.str] = None,
        variables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiPropertyRulesTemplateVariables", typing.Dict[builtins.str, typing.Any]]]]] = None,
        var_values_file: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules_template akamai_property_rules_template} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules_template#id DataAkamaiPropertyRulesTemplate#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param template: template block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules_template#template DataAkamaiPropertyRulesTemplate#template}
        :param template_file: File path to the template file. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules_template#template_file DataAkamaiPropertyRulesTemplate#template_file}
        :param var_definition_file: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules_template#var_definition_file DataAkamaiPropertyRulesTemplate#var_definition_file}.
        :param variables: variables block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules_template#variables DataAkamaiPropertyRulesTemplate#variables}
        :param var_values_file: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules_template#var_values_file DataAkamaiPropertyRulesTemplate#var_values_file}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbbd823d03efee7e0b28dd562c05aadf57880fbda070da38ac265211dad98d5a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAkamaiPropertyRulesTemplateConfig(
            id=id,
            template=template,
            template_file=template_file,
            var_definition_file=var_definition_file,
            variables=variables,
            var_values_file=var_values_file,
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
        '''Generates CDKTF code for importing a DataAkamaiPropertyRulesTemplate resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the DataAkamaiPropertyRulesTemplate to import.
        :param import_from_id: The id of the existing DataAkamaiPropertyRulesTemplate that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules_template#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the DataAkamaiPropertyRulesTemplate to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2564be069ea56297109889cce7fe3bdbcff94d3657946c336a7bed2089e936e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putTemplate")
    def put_template(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiPropertyRulesTemplateTemplate", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e772e81212e06143c92f2924e1d4640cad39f522d379ee3bb844abb0bf015f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTemplate", [value]))

    @jsii.member(jsii_name="putVariables")
    def put_variables(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiPropertyRulesTemplateVariables", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fb858dc38d40012d94871c3c7c5c7f954cb418db51087d9c7f222e7bf13f849)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putVariables", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTemplate")
    def reset_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTemplate", []))

    @jsii.member(jsii_name="resetTemplateFile")
    def reset_template_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTemplateFile", []))

    @jsii.member(jsii_name="resetVarDefinitionFile")
    def reset_var_definition_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVarDefinitionFile", []))

    @jsii.member(jsii_name="resetVariables")
    def reset_variables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVariables", []))

    @jsii.member(jsii_name="resetVarValuesFile")
    def reset_var_values_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVarValuesFile", []))

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
    @jsii.member(jsii_name="json")
    def json(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "json"))

    @builtins.property
    @jsii.member(jsii_name="template")
    def template(self) -> "DataAkamaiPropertyRulesTemplateTemplateList":
        return typing.cast("DataAkamaiPropertyRulesTemplateTemplateList", jsii.get(self, "template"))

    @builtins.property
    @jsii.member(jsii_name="variables")
    def variables(self) -> "DataAkamaiPropertyRulesTemplateVariablesList":
        return typing.cast("DataAkamaiPropertyRulesTemplateVariablesList", jsii.get(self, "variables"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="templateFileInput")
    def template_file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateFileInput"))

    @builtins.property
    @jsii.member(jsii_name="templateInput")
    def template_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiPropertyRulesTemplateTemplate"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiPropertyRulesTemplateTemplate"]]], jsii.get(self, "templateInput"))

    @builtins.property
    @jsii.member(jsii_name="varDefinitionFileInput")
    def var_definition_file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "varDefinitionFileInput"))

    @builtins.property
    @jsii.member(jsii_name="variablesInput")
    def variables_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiPropertyRulesTemplateVariables"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiPropertyRulesTemplateVariables"]]], jsii.get(self, "variablesInput"))

    @builtins.property
    @jsii.member(jsii_name="varValuesFileInput")
    def var_values_file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "varValuesFileInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65c31228aa34ea06ea3845e24ff8e83d445bcc408f7ada644084b0d8a249696d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="templateFile")
    def template_file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "templateFile"))

    @template_file.setter
    def template_file(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea13382fb6155da5668b9a6a3f720e8c60b301e95cb6a6a17cb1981c39486a54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateFile", value)

    @builtins.property
    @jsii.member(jsii_name="varDefinitionFile")
    def var_definition_file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "varDefinitionFile"))

    @var_definition_file.setter
    def var_definition_file(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__316fb1bf5d99b3d2a6d0255e89eac0b8fbe85f46885b0c8bd8e6ef1bfb94d6fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "varDefinitionFile", value)

    @builtins.property
    @jsii.member(jsii_name="varValuesFile")
    def var_values_file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "varValuesFile"))

    @var_values_file.setter
    def var_values_file(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbccec53de28a6eeadab66428b41fbc963876ae25e89f1152a827a29294aca13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "varValuesFile", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiPropertyRulesTemplate.DataAkamaiPropertyRulesTemplateConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "id": "id",
        "template": "template",
        "template_file": "templateFile",
        "var_definition_file": "varDefinitionFile",
        "variables": "variables",
        "var_values_file": "varValuesFile",
    },
)
class DataAkamaiPropertyRulesTemplateConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        id: typing.Optional[builtins.str] = None,
        template: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiPropertyRulesTemplateTemplate", typing.Dict[builtins.str, typing.Any]]]]] = None,
        template_file: typing.Optional[builtins.str] = None,
        var_definition_file: typing.Optional[builtins.str] = None,
        variables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAkamaiPropertyRulesTemplateVariables", typing.Dict[builtins.str, typing.Any]]]]] = None,
        var_values_file: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules_template#id DataAkamaiPropertyRulesTemplate#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param template: template block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules_template#template DataAkamaiPropertyRulesTemplate#template}
        :param template_file: File path to the template file. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules_template#template_file DataAkamaiPropertyRulesTemplate#template_file}
        :param var_definition_file: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules_template#var_definition_file DataAkamaiPropertyRulesTemplate#var_definition_file}.
        :param variables: variables block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules_template#variables DataAkamaiPropertyRulesTemplate#variables}
        :param var_values_file: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules_template#var_values_file DataAkamaiPropertyRulesTemplate#var_values_file}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d916142f2b5864970850d8fe6b80b18d9d3406b71b8f2cd945fb11fc1348c892)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument template", value=template, expected_type=type_hints["template"])
            check_type(argname="argument template_file", value=template_file, expected_type=type_hints["template_file"])
            check_type(argname="argument var_definition_file", value=var_definition_file, expected_type=type_hints["var_definition_file"])
            check_type(argname="argument variables", value=variables, expected_type=type_hints["variables"])
            check_type(argname="argument var_values_file", value=var_values_file, expected_type=type_hints["var_values_file"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
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
        if template is not None:
            self._values["template"] = template
        if template_file is not None:
            self._values["template_file"] = template_file
        if var_definition_file is not None:
            self._values["var_definition_file"] = var_definition_file
        if variables is not None:
            self._values["variables"] = variables
        if var_values_file is not None:
            self._values["var_values_file"] = var_values_file

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
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules_template#id DataAkamaiPropertyRulesTemplate#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiPropertyRulesTemplateTemplate"]]]:
        '''template block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules_template#template DataAkamaiPropertyRulesTemplate#template}
        '''
        result = self._values.get("template")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiPropertyRulesTemplateTemplate"]]], result)

    @builtins.property
    def template_file(self) -> typing.Optional[builtins.str]:
        '''File path to the template file.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules_template#template_file DataAkamaiPropertyRulesTemplate#template_file}
        '''
        result = self._values.get("template_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def var_definition_file(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules_template#var_definition_file DataAkamaiPropertyRulesTemplate#var_definition_file}.'''
        result = self._values.get("var_definition_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def variables(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiPropertyRulesTemplateVariables"]]]:
        '''variables block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules_template#variables DataAkamaiPropertyRulesTemplate#variables}
        '''
        result = self._values.get("variables")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAkamaiPropertyRulesTemplateVariables"]]], result)

    @builtins.property
    def var_values_file(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules_template#var_values_file DataAkamaiPropertyRulesTemplate#var_values_file}.'''
        result = self._values.get("var_values_file")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiPropertyRulesTemplateConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.dataAkamaiPropertyRulesTemplate.DataAkamaiPropertyRulesTemplateTemplate",
    jsii_struct_bases=[],
    name_mapping={"template_data": "templateData", "template_dir": "templateDir"},
)
class DataAkamaiPropertyRulesTemplateTemplate:
    def __init__(
        self,
        *,
        template_data: builtins.str,
        template_dir: builtins.str,
    ) -> None:
        '''
        :param template_data: Content of the template as string. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules_template#template_data DataAkamaiPropertyRulesTemplate#template_data}
        :param template_dir: Directory points to a folder, which contains snippets to include into template. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules_template#template_dir DataAkamaiPropertyRulesTemplate#template_dir}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccb3e71921e78cd974684049ee68f08ef1bc1a92ca8664a8476a177ab778d06c)
            check_type(argname="argument template_data", value=template_data, expected_type=type_hints["template_data"])
            check_type(argname="argument template_dir", value=template_dir, expected_type=type_hints["template_dir"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "template_data": template_data,
            "template_dir": template_dir,
        }

    @builtins.property
    def template_data(self) -> builtins.str:
        '''Content of the template as string.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules_template#template_data DataAkamaiPropertyRulesTemplate#template_data}
        '''
        result = self._values.get("template_data")
        assert result is not None, "Required property 'template_data' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template_dir(self) -> builtins.str:
        '''Directory points to a folder, which contains snippets to include into template.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules_template#template_dir DataAkamaiPropertyRulesTemplate#template_dir}
        '''
        result = self._values.get("template_dir")
        assert result is not None, "Required property 'template_dir' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiPropertyRulesTemplateTemplate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiPropertyRulesTemplateTemplateList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiPropertyRulesTemplate.DataAkamaiPropertyRulesTemplateTemplateList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__753d72258343e86cf4b31419c9da83fcba70cd06b2147985e6b2c747ba797da8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiPropertyRulesTemplateTemplateOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f330a9e0459c523c18a56aa7b6a9af36706d058797bb9f73ff7db3cd97e2956)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiPropertyRulesTemplateTemplateOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fabb204b16e63793e82e2fb518f78ca0a4eddbada078a7ec49af6436cb195172)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4674e6b6dde9ab43d96ffb79bda5602afc92ffd3e001cf3e09671af4156cfec3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9e9192f47a19cc74255763a9ea4a86141f8392f4a277e9077f8105f3c84b210d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiPropertyRulesTemplateTemplate]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiPropertyRulesTemplateTemplate]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiPropertyRulesTemplateTemplate]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5cf36c8437ceb534f92546402d9e93689fc978f72e181de38829a83b12aed258)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiPropertyRulesTemplateTemplateOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiPropertyRulesTemplate.DataAkamaiPropertyRulesTemplateTemplateOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4442e2d0f7af4a4b315e0b69a1eb94037a455930a1e93a91811d27160e87edca)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="templateDataInput")
    def template_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateDataInput"))

    @builtins.property
    @jsii.member(jsii_name="templateDirInput")
    def template_dir_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateDirInput"))

    @builtins.property
    @jsii.member(jsii_name="templateData")
    def template_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "templateData"))

    @template_data.setter
    def template_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b3d14df0d3ba986a301cd020c64c850ac696f02094f26333c3c8fba70b04619)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateData", value)

    @builtins.property
    @jsii.member(jsii_name="templateDir")
    def template_dir(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "templateDir"))

    @template_dir.setter
    def template_dir(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__785587dc01318c8566053afa0c81dea8762fc90c2c2e76ce5f298f7b1c283613)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateDir", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiPropertyRulesTemplateTemplate]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiPropertyRulesTemplateTemplate]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiPropertyRulesTemplateTemplate]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e950d617ceb27e9bd810562c157d032399be9f941ed89842115d58f4e83961f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.dataAkamaiPropertyRulesTemplate.DataAkamaiPropertyRulesTemplateVariables",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value", "type": "type"},
)
class DataAkamaiPropertyRulesTemplateVariables:
    def __init__(
        self,
        *,
        name: builtins.str,
        value: builtins.str,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules_template#name DataAkamaiPropertyRulesTemplate#name}.
        :param value: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules_template#value DataAkamaiPropertyRulesTemplate#value}.
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules_template#type DataAkamaiPropertyRulesTemplate#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c84bd2be0bd6e17bebd1e414a8b04006772cc3450f67e19d194343e218f0e4e)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "value": value,
        }
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules_template#name DataAkamaiPropertyRulesTemplate#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules_template#value DataAkamaiPropertyRulesTemplate#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/data-sources/property_rules_template#type DataAkamaiPropertyRulesTemplate#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAkamaiPropertyRulesTemplateVariables(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAkamaiPropertyRulesTemplateVariablesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiPropertyRulesTemplate.DataAkamaiPropertyRulesTemplateVariablesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4916408568f387dbf6924d440962aa67942fda4413745a44c448303d78e7b488)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAkamaiPropertyRulesTemplateVariablesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec873d21c5b191ab0411d0681d4be24b6b73853562251ce657d7e9bc109b36d9)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAkamaiPropertyRulesTemplateVariablesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__923a89c705187ad0994a788df87f48303c137263dd3509b46c6bde5a71629b26)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ebcb2dce6cf1a2d6df63a847af79ba5215c7bd19aceff940d1fb2e357593fa7f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8555f562c555af4bffc9fa400331f82a0f5226d88a72ff7083161bb9a3af3eba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiPropertyRulesTemplateVariables]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiPropertyRulesTemplateVariables]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiPropertyRulesTemplateVariables]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd65e65ce53c585f735788b3e8bbc956b1630777eb81579eb4ddd1686d2f8730)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAkamaiPropertyRulesTemplateVariablesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.dataAkamaiPropertyRulesTemplate.DataAkamaiPropertyRulesTemplateVariablesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__617ca954b2511cf4e5b73160a38c60d7a9e484a1f3f51f8031d062a083fe808e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36adbd2bac9342bfd910024038c95e5647677d767dfd602c10f2525a198ce167)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__834d2962640168cd95431f33d3532507554eee2d1fd72928e2386765a7f914c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b18e35641dafe1c4506c23a259731ae62ef9beb2de499c0962e89447abbce2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiPropertyRulesTemplateVariables]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiPropertyRulesTemplateVariables]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiPropertyRulesTemplateVariables]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__420b745e535716d6b1131c505e94cf3666c447403f277c20682ed90e53035eb4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataAkamaiPropertyRulesTemplate",
    "DataAkamaiPropertyRulesTemplateConfig",
    "DataAkamaiPropertyRulesTemplateTemplate",
    "DataAkamaiPropertyRulesTemplateTemplateList",
    "DataAkamaiPropertyRulesTemplateTemplateOutputReference",
    "DataAkamaiPropertyRulesTemplateVariables",
    "DataAkamaiPropertyRulesTemplateVariablesList",
    "DataAkamaiPropertyRulesTemplateVariablesOutputReference",
]

publication.publish()

def _typecheckingstub__bbbd823d03efee7e0b28dd562c05aadf57880fbda070da38ac265211dad98d5a(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    id: typing.Optional[builtins.str] = None,
    template: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiPropertyRulesTemplateTemplate, typing.Dict[builtins.str, typing.Any]]]]] = None,
    template_file: typing.Optional[builtins.str] = None,
    var_definition_file: typing.Optional[builtins.str] = None,
    variables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiPropertyRulesTemplateVariables, typing.Dict[builtins.str, typing.Any]]]]] = None,
    var_values_file: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__a2564be069ea56297109889cce7fe3bdbcff94d3657946c336a7bed2089e936e(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e772e81212e06143c92f2924e1d4640cad39f522d379ee3bb844abb0bf015f4(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiPropertyRulesTemplateTemplate, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fb858dc38d40012d94871c3c7c5c7f954cb418db51087d9c7f222e7bf13f849(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiPropertyRulesTemplateVariables, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65c31228aa34ea06ea3845e24ff8e83d445bcc408f7ada644084b0d8a249696d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea13382fb6155da5668b9a6a3f720e8c60b301e95cb6a6a17cb1981c39486a54(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__316fb1bf5d99b3d2a6d0255e89eac0b8fbe85f46885b0c8bd8e6ef1bfb94d6fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbccec53de28a6eeadab66428b41fbc963876ae25e89f1152a827a29294aca13(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d916142f2b5864970850d8fe6b80b18d9d3406b71b8f2cd945fb11fc1348c892(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    template: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiPropertyRulesTemplateTemplate, typing.Dict[builtins.str, typing.Any]]]]] = None,
    template_file: typing.Optional[builtins.str] = None,
    var_definition_file: typing.Optional[builtins.str] = None,
    variables: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAkamaiPropertyRulesTemplateVariables, typing.Dict[builtins.str, typing.Any]]]]] = None,
    var_values_file: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccb3e71921e78cd974684049ee68f08ef1bc1a92ca8664a8476a177ab778d06c(
    *,
    template_data: builtins.str,
    template_dir: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__753d72258343e86cf4b31419c9da83fcba70cd06b2147985e6b2c747ba797da8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f330a9e0459c523c18a56aa7b6a9af36706d058797bb9f73ff7db3cd97e2956(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fabb204b16e63793e82e2fb518f78ca0a4eddbada078a7ec49af6436cb195172(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4674e6b6dde9ab43d96ffb79bda5602afc92ffd3e001cf3e09671af4156cfec3(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e9192f47a19cc74255763a9ea4a86141f8392f4a277e9077f8105f3c84b210d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cf36c8437ceb534f92546402d9e93689fc978f72e181de38829a83b12aed258(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiPropertyRulesTemplateTemplate]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4442e2d0f7af4a4b315e0b69a1eb94037a455930a1e93a91811d27160e87edca(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b3d14df0d3ba986a301cd020c64c850ac696f02094f26333c3c8fba70b04619(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__785587dc01318c8566053afa0c81dea8762fc90c2c2e76ce5f298f7b1c283613(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e950d617ceb27e9bd810562c157d032399be9f941ed89842115d58f4e83961f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiPropertyRulesTemplateTemplate]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c84bd2be0bd6e17bebd1e414a8b04006772cc3450f67e19d194343e218f0e4e(
    *,
    name: builtins.str,
    value: builtins.str,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4916408568f387dbf6924d440962aa67942fda4413745a44c448303d78e7b488(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec873d21c5b191ab0411d0681d4be24b6b73853562251ce657d7e9bc109b36d9(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__923a89c705187ad0994a788df87f48303c137263dd3509b46c6bde5a71629b26(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebcb2dce6cf1a2d6df63a847af79ba5215c7bd19aceff940d1fb2e357593fa7f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8555f562c555af4bffc9fa400331f82a0f5226d88a72ff7083161bb9a3af3eba(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd65e65ce53c585f735788b3e8bbc956b1630777eb81579eb4ddd1686d2f8730(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAkamaiPropertyRulesTemplateVariables]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__617ca954b2511cf4e5b73160a38c60d7a9e484a1f3f51f8031d062a083fe808e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36adbd2bac9342bfd910024038c95e5647677d767dfd602c10f2525a198ce167(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__834d2962640168cd95431f33d3532507554eee2d1fd72928e2386765a7f914c3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b18e35641dafe1c4506c23a259731ae62ef9beb2de499c0962e89447abbce2e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__420b745e535716d6b1131c505e94cf3666c447403f277c20682ed90e53035eb4(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAkamaiPropertyRulesTemplateVariables]],
) -> None:
    """Type checking stubs"""
    pass
