'''
# `akamai_datastream`

Refer to the Terraform Registry for docs: [`akamai_datastream`](https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream).
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


class Datastream(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.datastream.Datastream",
):
    '''Represents a {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream akamai_datastream}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        active: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        contract_id: builtins.str,
        dataset_fields: typing.Sequence[jsii.Number],
        delivery_configuration: typing.Union["DatastreamDeliveryConfiguration", typing.Dict[builtins.str, typing.Any]],
        group_id: builtins.str,
        properties: typing.Sequence[builtins.str],
        stream_name: builtins.str,
        azure_connector: typing.Optional[typing.Union["DatastreamAzureConnector", typing.Dict[builtins.str, typing.Any]]] = None,
        collect_midgress: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        datadog_connector: typing.Optional[typing.Union["DatastreamDatadogConnector", typing.Dict[builtins.str, typing.Any]]] = None,
        elasticsearch_connector: typing.Optional[typing.Union["DatastreamElasticsearchConnector", typing.Dict[builtins.str, typing.Any]]] = None,
        gcs_connector: typing.Optional[typing.Union["DatastreamGcsConnector", typing.Dict[builtins.str, typing.Any]]] = None,
        https_connector: typing.Optional[typing.Union["DatastreamHttpsConnector", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        loggly_connector: typing.Optional[typing.Union["DatastreamLogglyConnector", typing.Dict[builtins.str, typing.Any]]] = None,
        new_relic_connector: typing.Optional[typing.Union["DatastreamNewRelicConnector", typing.Dict[builtins.str, typing.Any]]] = None,
        notification_emails: typing.Optional[typing.Sequence[builtins.str]] = None,
        oracle_connector: typing.Optional[typing.Union["DatastreamOracleConnector", typing.Dict[builtins.str, typing.Any]]] = None,
        s3_connector: typing.Optional[typing.Union["DatastreamS3Connector", typing.Dict[builtins.str, typing.Any]]] = None,
        splunk_connector: typing.Optional[typing.Union["DatastreamSplunkConnector", typing.Dict[builtins.str, typing.Any]]] = None,
        sumologic_connector: typing.Optional[typing.Union["DatastreamSumologicConnector", typing.Dict[builtins.str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["DatastreamTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream akamai_datastream} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param active: Defining if stream should be active or not. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#active Datastream#active}
        :param contract_id: Identifies the contract that has access to the product. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#contract_id Datastream#contract_id}
        :param dataset_fields: A list of data set fields selected from the associated template that the stream monitors in logs. The order of the identifiers define how the value for these fields appear in the log lines Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#dataset_fields Datastream#dataset_fields}
        :param delivery_configuration: delivery_configuration block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#delivery_configuration Datastream#delivery_configuration}
        :param group_id: Identifies the group that has access to the product and for which the stream configuration was created. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#group_id Datastream#group_id}
        :param properties: Identifies the properties monitored in the stream. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#properties Datastream#properties}
        :param stream_name: The name of the stream. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#stream_name Datastream#stream_name}
        :param azure_connector: azure_connector block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#azure_connector Datastream#azure_connector}
        :param collect_midgress: Identifies if stream needs to collect midgress data. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#collect_midgress Datastream#collect_midgress}
        :param datadog_connector: datadog_connector block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#datadog_connector Datastream#datadog_connector}
        :param elasticsearch_connector: elasticsearch_connector block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#elasticsearch_connector Datastream#elasticsearch_connector}
        :param gcs_connector: gcs_connector block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#gcs_connector Datastream#gcs_connector}
        :param https_connector: https_connector block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#https_connector Datastream#https_connector}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#id Datastream#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param loggly_connector: loggly_connector block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#loggly_connector Datastream#loggly_connector}
        :param new_relic_connector: new_relic_connector block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#new_relic_connector Datastream#new_relic_connector}
        :param notification_emails: List of email addresses where the system sends notifications about activations and deactivations of the stream. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#notification_emails Datastream#notification_emails}
        :param oracle_connector: oracle_connector block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#oracle_connector Datastream#oracle_connector}
        :param s3_connector: s3_connector block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#s3_connector Datastream#s3_connector}
        :param splunk_connector: splunk_connector block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#splunk_connector Datastream#splunk_connector}
        :param sumologic_connector: sumologic_connector block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#sumologic_connector Datastream#sumologic_connector}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#timeouts Datastream#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39c7b6fa10d3cc155a2087a11d80145369c81cc9b39d5da5078a32ae2afd2168)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DatastreamConfig(
            active=active,
            contract_id=contract_id,
            dataset_fields=dataset_fields,
            delivery_configuration=delivery_configuration,
            group_id=group_id,
            properties=properties,
            stream_name=stream_name,
            azure_connector=azure_connector,
            collect_midgress=collect_midgress,
            datadog_connector=datadog_connector,
            elasticsearch_connector=elasticsearch_connector,
            gcs_connector=gcs_connector,
            https_connector=https_connector,
            id=id,
            loggly_connector=loggly_connector,
            new_relic_connector=new_relic_connector,
            notification_emails=notification_emails,
            oracle_connector=oracle_connector,
            s3_connector=s3_connector,
            splunk_connector=splunk_connector,
            sumologic_connector=sumologic_connector,
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
        '''Generates CDKTF code for importing a Datastream resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the Datastream to import.
        :param import_from_id: The id of the existing Datastream that should be imported. Refer to the {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the Datastream to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b0f3666ff22cf6ea1540ade6620249b05bd1f903d48eea8c428829ee0dd604b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putAzureConnector")
    def put_azure_connector(
        self,
        *,
        access_key: builtins.str,
        account_name: builtins.str,
        container_name: builtins.str,
        display_name: builtins.str,
        path: builtins.str,
    ) -> None:
        '''
        :param access_key: Access keys associated with Azure Storage account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#access_key Datastream#access_key}
        :param account_name: Specifies the Azure Storage account name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#account_name Datastream#account_name}
        :param container_name: Specifies the Azure Storage container name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#container_name Datastream#container_name}
        :param display_name: The name of the connector. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#display_name Datastream#display_name}
        :param path: The path to the folder within Azure Storage container where logs will be stored. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#path Datastream#path}
        '''
        value = DatastreamAzureConnector(
            access_key=access_key,
            account_name=account_name,
            container_name=container_name,
            display_name=display_name,
            path=path,
        )

        return typing.cast(None, jsii.invoke(self, "putAzureConnector", [value]))

    @jsii.member(jsii_name="putDatadogConnector")
    def put_datadog_connector(
        self,
        *,
        auth_token: builtins.str,
        display_name: builtins.str,
        endpoint: builtins.str,
        compress_logs: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        service: typing.Optional[builtins.str] = None,
        source: typing.Optional[builtins.str] = None,
        tags: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_token: The API key associated with Datadog account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#auth_token Datastream#auth_token}
        :param display_name: The name of the connector. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#display_name Datastream#display_name}
        :param endpoint: The Datadog endpoint where logs will be stored. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#endpoint Datastream#endpoint}
        :param compress_logs: Indicates whether the logs should be compressed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#compress_logs Datastream#compress_logs}
        :param service: The service of the Datadog connector. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#service Datastream#service}
        :param source: The source of the Datadog connector. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#source Datastream#source}
        :param tags: The tags of the Datadog connector. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#tags Datastream#tags}
        '''
        value = DatastreamDatadogConnector(
            auth_token=auth_token,
            display_name=display_name,
            endpoint=endpoint,
            compress_logs=compress_logs,
            service=service,
            source=source,
            tags=tags,
        )

        return typing.cast(None, jsii.invoke(self, "putDatadogConnector", [value]))

    @jsii.member(jsii_name="putDeliveryConfiguration")
    def put_delivery_configuration(
        self,
        *,
        format: builtins.str,
        frequency: typing.Union["DatastreamDeliveryConfigurationFrequency", typing.Dict[builtins.str, typing.Any]],
        field_delimiter: typing.Optional[builtins.str] = None,
        upload_file_prefix: typing.Optional[builtins.str] = None,
        upload_file_suffix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param format: The format in which logs will be received. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#format Datastream#format}
        :param frequency: frequency block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#frequency Datastream#frequency}
        :param field_delimiter: A delimiter that you use to separate data set fields in log lines. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#field_delimiter Datastream#field_delimiter}
        :param upload_file_prefix: The prefix of the log file that will be send to a destination. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#upload_file_prefix Datastream#upload_file_prefix}
        :param upload_file_suffix: The suffix of the log file that will be send to a destination. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#upload_file_suffix Datastream#upload_file_suffix}
        '''
        value = DatastreamDeliveryConfiguration(
            format=format,
            frequency=frequency,
            field_delimiter=field_delimiter,
            upload_file_prefix=upload_file_prefix,
            upload_file_suffix=upload_file_suffix,
        )

        return typing.cast(None, jsii.invoke(self, "putDeliveryConfiguration", [value]))

    @jsii.member(jsii_name="putElasticsearchConnector")
    def put_elasticsearch_connector(
        self,
        *,
        display_name: builtins.str,
        endpoint: builtins.str,
        index_name: builtins.str,
        password: builtins.str,
        user_name: builtins.str,
        ca_cert: typing.Optional[builtins.str] = None,
        client_cert: typing.Optional[builtins.str] = None,
        client_key: typing.Optional[builtins.str] = None,
        content_type: typing.Optional[builtins.str] = None,
        custom_header_name: typing.Optional[builtins.str] = None,
        custom_header_value: typing.Optional[builtins.str] = None,
        tls_hostname: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param display_name: The name of the connector. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#display_name Datastream#display_name}
        :param endpoint: The Elasticsearch bulk endpoint URL in the https://hostname.elastic-cloud.com:9243/_bulk/ format. Set indexName in the appropriate field instead of providing it in the URL. You can use Akamaized property hostnames as endpoint URLs. See Stream logs to Elasticsearch. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#endpoint Datastream#endpoint}
        :param index_name: The index name of the Elastic cloud where you want to store log files. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#index_name Datastream#index_name}
        :param password: The Elasticsearch basic access authentication password. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#password Datastream#password}
        :param user_name: The Elasticsearch basic access authentication username. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#user_name Datastream#user_name}
        :param ca_cert: The certification authority (CA) certificate used to verify the origin server's certificate. If the certificate is not signed by a well-known certification authority, enter the CA certificate in the PEM format for verification. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#ca_cert Datastream#ca_cert}
        :param client_cert: The PEM-formatted digital certificate you want to authenticate requests to your destination with. If you want to use mutual authentication, you need to provide both the client certificate and the client key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#client_cert Datastream#client_cert}
        :param client_key: The private key in the non-encrypted PKCS8 format you want to use to authenticate with the backend server. If you want to use mutual authentication, you need to provide both the client certificate and the client key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#client_key Datastream#client_key}
        :param content_type: The type of the resource passed in the request's custom header. For details, see Additional options in the DataStream user guide. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#content_type Datastream#content_type}
        :param custom_header_name: A human-readable name for the request's custom header, containing only alphanumeric, dash, and underscore characters. For details, see Additional options in the DataStream user guide. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#custom_header_name Datastream#custom_header_name}
        :param custom_header_value: The custom header's contents passed with the request that contains information about the client connection. For details, see Additional options in the DataStream user guide. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#custom_header_value Datastream#custom_header_value}
        :param tls_hostname: The hostname that verifies the server's certificate and matches the Subject Alternative Names (SANs) in the certificate. If not provided, DataStream fetches the hostname from the endpoint URL. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#tls_hostname Datastream#tls_hostname}
        '''
        value = DatastreamElasticsearchConnector(
            display_name=display_name,
            endpoint=endpoint,
            index_name=index_name,
            password=password,
            user_name=user_name,
            ca_cert=ca_cert,
            client_cert=client_cert,
            client_key=client_key,
            content_type=content_type,
            custom_header_name=custom_header_name,
            custom_header_value=custom_header_value,
            tls_hostname=tls_hostname,
        )

        return typing.cast(None, jsii.invoke(self, "putElasticsearchConnector", [value]))

    @jsii.member(jsii_name="putGcsConnector")
    def put_gcs_connector(
        self,
        *,
        bucket: builtins.str,
        display_name: builtins.str,
        private_key: builtins.str,
        project_id: builtins.str,
        service_account_name: builtins.str,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: The name of the storage bucket created in Google Cloud account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#bucket Datastream#bucket}
        :param display_name: The name of the connector. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#display_name Datastream#display_name}
        :param private_key: The contents of the JSON private key generated and downloaded in Google Cloud Storage account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#private_key Datastream#private_key}
        :param project_id: The unique ID of Google Cloud project. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#project_id Datastream#project_id}
        :param service_account_name: The name of the service account with the storage.object.create permission or Storage Object Creator role. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#service_account_name Datastream#service_account_name}
        :param path: The path to the folder within Google Cloud bucket where logs will be stored. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#path Datastream#path}
        '''
        value = DatastreamGcsConnector(
            bucket=bucket,
            display_name=display_name,
            private_key=private_key,
            project_id=project_id,
            service_account_name=service_account_name,
            path=path,
        )

        return typing.cast(None, jsii.invoke(self, "putGcsConnector", [value]))

    @jsii.member(jsii_name="putHttpsConnector")
    def put_https_connector(
        self,
        *,
        authentication_type: builtins.str,
        display_name: builtins.str,
        endpoint: builtins.str,
        ca_cert: typing.Optional[builtins.str] = None,
        client_cert: typing.Optional[builtins.str] = None,
        client_key: typing.Optional[builtins.str] = None,
        compress_logs: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        content_type: typing.Optional[builtins.str] = None,
        custom_header_name: typing.Optional[builtins.str] = None,
        custom_header_value: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        tls_hostname: typing.Optional[builtins.str] = None,
        user_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param authentication_type: Either NONE for no authentication, or BASIC for username and password authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#authentication_type Datastream#authentication_type}
        :param display_name: The name of the connector. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#display_name Datastream#display_name}
        :param endpoint: URL where logs will be stored. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#endpoint Datastream#endpoint}
        :param ca_cert: The certification authority (CA) certificate used to verify the origin server's certificate. If the certificate is not signed by a well-known certification authority, enter the CA certificate in the PEM format for verification. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#ca_cert Datastream#ca_cert}
        :param client_cert: The digital certificate in the PEM format you want to use to authenticate requests to your destination. If you want to use mutual authentication, you need to provide both the client certificate and the client key (in the PEM format). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#client_cert Datastream#client_cert}
        :param client_key: The private key in the non-encrypted PKCS8 format you want to use to authenticate with the back-end server. If you want to use mutual authentication, you need to provide both the client certificate and the client key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#client_key Datastream#client_key}
        :param compress_logs: Indicates whether the logs should be compressed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#compress_logs Datastream#compress_logs}
        :param content_type: Content type to pass in the log file header. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#content_type Datastream#content_type}
        :param custom_header_name: The name of custom header passed with the request to the destination. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#custom_header_name Datastream#custom_header_name}
        :param custom_header_value: The custom header's contents passed with the request to the destination. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#custom_header_value Datastream#custom_header_value}
        :param password: Password set for custom HTTPS endpoint for authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#password Datastream#password}
        :param tls_hostname: The hostname that verifies the server's certificate and matches the Subject Alternative Names (SANs) in the certificate. If not provided, DataStream fetches the hostname from the endpoint URL. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#tls_hostname Datastream#tls_hostname}
        :param user_name: Username used for authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#user_name Datastream#user_name}
        '''
        value = DatastreamHttpsConnector(
            authentication_type=authentication_type,
            display_name=display_name,
            endpoint=endpoint,
            ca_cert=ca_cert,
            client_cert=client_cert,
            client_key=client_key,
            compress_logs=compress_logs,
            content_type=content_type,
            custom_header_name=custom_header_name,
            custom_header_value=custom_header_value,
            password=password,
            tls_hostname=tls_hostname,
            user_name=user_name,
        )

        return typing.cast(None, jsii.invoke(self, "putHttpsConnector", [value]))

    @jsii.member(jsii_name="putLogglyConnector")
    def put_loggly_connector(
        self,
        *,
        auth_token: builtins.str,
        display_name: builtins.str,
        endpoint: builtins.str,
        content_type: typing.Optional[builtins.str] = None,
        custom_header_name: typing.Optional[builtins.str] = None,
        custom_header_value: typing.Optional[builtins.str] = None,
        tags: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_token: The unique HTTP code for your Loggly bulk endpoint. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#auth_token Datastream#auth_token}
        :param display_name: The name of the connector. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#display_name Datastream#display_name}
        :param endpoint: The Loggly bulk endpoint URL in the https://hostname.loggly.com/bulk/ format. Set the endpoint code in the authToken field instead of providing it in the URL. You can use Akamaized property hostnames as endpoint URLs. See Stream logs to Loggly. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#endpoint Datastream#endpoint}
        :param content_type: The type of the resource passed in the request's custom header. For details, see Additional options in the DataStream user guide. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#content_type Datastream#content_type}
        :param custom_header_name: A human-readable name for the request's custom header, containing only alphanumeric, dash, and underscore characters. For details, see Additional options in the DataStream user guide. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#custom_header_name Datastream#custom_header_name}
        :param custom_header_value: The custom header's contents passed with the request that contains information about the client connection. For details, see Additional options in the DataStream user guide. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#custom_header_value Datastream#custom_header_value}
        :param tags: The tags you can use to segment and filter log events in Loggly. See Tags in the Loggly documentation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#tags Datastream#tags}
        '''
        value = DatastreamLogglyConnector(
            auth_token=auth_token,
            display_name=display_name,
            endpoint=endpoint,
            content_type=content_type,
            custom_header_name=custom_header_name,
            custom_header_value=custom_header_value,
            tags=tags,
        )

        return typing.cast(None, jsii.invoke(self, "putLogglyConnector", [value]))

    @jsii.member(jsii_name="putNewRelicConnector")
    def put_new_relic_connector(
        self,
        *,
        auth_token: builtins.str,
        display_name: builtins.str,
        endpoint: builtins.str,
        content_type: typing.Optional[builtins.str] = None,
        custom_header_name: typing.Optional[builtins.str] = None,
        custom_header_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_token: Your Log API token for your account in New Relic. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#auth_token Datastream#auth_token}
        :param display_name: The name of the connector. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#display_name Datastream#display_name}
        :param endpoint: A New Relic endpoint URL you want to send your logs to. The endpoint URL should follow the https://<newrelic.com>/log/v1/ format format. See Introduction to the Log API https://docs.newrelic.com/docs/logs/log-api/introduction-log-api/ if you want to retrieve your New Relic endpoint URL. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#endpoint Datastream#endpoint}
        :param content_type: The type of the resource passed in the request's custom header. For details, see Additional options in the DataStream user guide. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#content_type Datastream#content_type}
        :param custom_header_name: A human-readable name for the request's custom header, containing only alphanumeric, dash, and underscore characters. For details, see Additional options in the DataStream user guide. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#custom_header_name Datastream#custom_header_name}
        :param custom_header_value: The custom header's contents passed with the request that contains information about the client connection. For details, see Additional options in the DataStream user guide. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#custom_header_value Datastream#custom_header_value}
        '''
        value = DatastreamNewRelicConnector(
            auth_token=auth_token,
            display_name=display_name,
            endpoint=endpoint,
            content_type=content_type,
            custom_header_name=custom_header_name,
            custom_header_value=custom_header_value,
        )

        return typing.cast(None, jsii.invoke(self, "putNewRelicConnector", [value]))

    @jsii.member(jsii_name="putOracleConnector")
    def put_oracle_connector(
        self,
        *,
        access_key: builtins.str,
        bucket: builtins.str,
        display_name: builtins.str,
        namespace: builtins.str,
        path: builtins.str,
        region: builtins.str,
        secret_access_key: builtins.str,
    ) -> None:
        '''
        :param access_key: The access key identifier used to authenticate requests to the Oracle Cloud account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#access_key Datastream#access_key}
        :param bucket: The name of the Oracle Cloud Storage bucket. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#bucket Datastream#bucket}
        :param display_name: The name of the connector. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#display_name Datastream#display_name}
        :param namespace: The namespace of Oracle Cloud Storage account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#namespace Datastream#namespace}
        :param path: The path to the folder within your Oracle Cloud Storage bucket where logs will be stored. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#path Datastream#path}
        :param region: The Oracle Cloud Storage region where bucket resides. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#region Datastream#region}
        :param secret_access_key: The secret access key identifier used to authenticate requests to the Oracle Cloud account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#secret_access_key Datastream#secret_access_key}
        '''
        value = DatastreamOracleConnector(
            access_key=access_key,
            bucket=bucket,
            display_name=display_name,
            namespace=namespace,
            path=path,
            region=region,
            secret_access_key=secret_access_key,
        )

        return typing.cast(None, jsii.invoke(self, "putOracleConnector", [value]))

    @jsii.member(jsii_name="putS3Connector")
    def put_s3_connector(
        self,
        *,
        access_key: builtins.str,
        bucket: builtins.str,
        display_name: builtins.str,
        path: builtins.str,
        region: builtins.str,
        secret_access_key: builtins.str,
    ) -> None:
        '''
        :param access_key: The access key identifier used to authenticate requests to the Amazon S3 account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#access_key Datastream#access_key}
        :param bucket: The name of the Amazon S3 bucket. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#bucket Datastream#bucket}
        :param display_name: The name of the connector. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#display_name Datastream#display_name}
        :param path: The path to the folder within Amazon S3 bucket where logs will be stored. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#path Datastream#path}
        :param region: The AWS region where Amazon S3 bucket resides. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#region Datastream#region}
        :param secret_access_key: The secret access key identifier used to authenticate requests to the Amazon S3 account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#secret_access_key Datastream#secret_access_key}
        '''
        value = DatastreamS3Connector(
            access_key=access_key,
            bucket=bucket,
            display_name=display_name,
            path=path,
            region=region,
            secret_access_key=secret_access_key,
        )

        return typing.cast(None, jsii.invoke(self, "putS3Connector", [value]))

    @jsii.member(jsii_name="putSplunkConnector")
    def put_splunk_connector(
        self,
        *,
        display_name: builtins.str,
        endpoint: builtins.str,
        event_collector_token: builtins.str,
        ca_cert: typing.Optional[builtins.str] = None,
        client_cert: typing.Optional[builtins.str] = None,
        client_key: typing.Optional[builtins.str] = None,
        compress_logs: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        custom_header_name: typing.Optional[builtins.str] = None,
        custom_header_value: typing.Optional[builtins.str] = None,
        tls_hostname: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param display_name: The name of the connector. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#display_name Datastream#display_name}
        :param endpoint: The raw event Splunk URL where logs will be stored. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#endpoint Datastream#endpoint}
        :param event_collector_token: The Event Collector token associated with Splunk account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#event_collector_token Datastream#event_collector_token}
        :param ca_cert: The certification authority (CA) certificate used to verify the origin server's certificate. If the certificate is not signed by a well-known certification authority, enter the CA certificate in the PEM format for verification. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#ca_cert Datastream#ca_cert}
        :param client_cert: The digital certificate in the PEM format you want to use to authenticate requests to your destination. If you want to use mutual authentication, you need to provide both the client certificate and the client key (in the PEM format). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#client_cert Datastream#client_cert}
        :param client_key: The private key in the non-encrypted PKCS8 format you want to use to authenticate with the back-end server. If you want to use mutual authentication, you need to provide both the client certificate and the client key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#client_key Datastream#client_key}
        :param compress_logs: Indicates whether the logs should be compressed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#compress_logs Datastream#compress_logs}
        :param custom_header_name: The name of custom header passed with the request to the destination. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#custom_header_name Datastream#custom_header_name}
        :param custom_header_value: The custom header's contents passed with the request to the destination. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#custom_header_value Datastream#custom_header_value}
        :param tls_hostname: The hostname that verifies the server's certificate and matches the Subject Alternative Names (SANs) in the certificate. If not provided, DataStream fetches the hostname from the endpoint URL. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#tls_hostname Datastream#tls_hostname}
        '''
        value = DatastreamSplunkConnector(
            display_name=display_name,
            endpoint=endpoint,
            event_collector_token=event_collector_token,
            ca_cert=ca_cert,
            client_cert=client_cert,
            client_key=client_key,
            compress_logs=compress_logs,
            custom_header_name=custom_header_name,
            custom_header_value=custom_header_value,
            tls_hostname=tls_hostname,
        )

        return typing.cast(None, jsii.invoke(self, "putSplunkConnector", [value]))

    @jsii.member(jsii_name="putSumologicConnector")
    def put_sumologic_connector(
        self,
        *,
        collector_code: builtins.str,
        display_name: builtins.str,
        endpoint: builtins.str,
        compress_logs: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        content_type: typing.Optional[builtins.str] = None,
        custom_header_name: typing.Optional[builtins.str] = None,
        custom_header_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param collector_code: The unique HTTP collector code of Sumo Logic endpoint. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#collector_code Datastream#collector_code}
        :param display_name: The name of the connector. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#display_name Datastream#display_name}
        :param endpoint: The Sumo Logic collection endpoint where logs will be stored. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#endpoint Datastream#endpoint}
        :param compress_logs: Indicates whether the logs should be compressed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#compress_logs Datastream#compress_logs}
        :param content_type: Content type to pass in the log file header. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#content_type Datastream#content_type}
        :param custom_header_name: The name of custom header passed with the request to the destination. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#custom_header_name Datastream#custom_header_name}
        :param custom_header_value: The custom header's contents passed with the request to the destination. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#custom_header_value Datastream#custom_header_value}
        '''
        value = DatastreamSumologicConnector(
            collector_code=collector_code,
            display_name=display_name,
            endpoint=endpoint,
            compress_logs=compress_logs,
            content_type=content_type,
            custom_header_name=custom_header_name,
            custom_header_value=custom_header_value,
        )

        return typing.cast(None, jsii.invoke(self, "putSumologicConnector", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self, *, default: typing.Optional[builtins.str] = None) -> None:
        '''
        :param default: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#default Datastream#default}.
        '''
        value = DatastreamTimeouts(default=default)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAzureConnector")
    def reset_azure_connector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureConnector", []))

    @jsii.member(jsii_name="resetCollectMidgress")
    def reset_collect_midgress(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCollectMidgress", []))

    @jsii.member(jsii_name="resetDatadogConnector")
    def reset_datadog_connector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatadogConnector", []))

    @jsii.member(jsii_name="resetElasticsearchConnector")
    def reset_elasticsearch_connector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetElasticsearchConnector", []))

    @jsii.member(jsii_name="resetGcsConnector")
    def reset_gcs_connector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcsConnector", []))

    @jsii.member(jsii_name="resetHttpsConnector")
    def reset_https_connector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpsConnector", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLogglyConnector")
    def reset_loggly_connector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogglyConnector", []))

    @jsii.member(jsii_name="resetNewRelicConnector")
    def reset_new_relic_connector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNewRelicConnector", []))

    @jsii.member(jsii_name="resetNotificationEmails")
    def reset_notification_emails(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationEmails", []))

    @jsii.member(jsii_name="resetOracleConnector")
    def reset_oracle_connector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOracleConnector", []))

    @jsii.member(jsii_name="resetS3Connector")
    def reset_s3_connector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3Connector", []))

    @jsii.member(jsii_name="resetSplunkConnector")
    def reset_splunk_connector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSplunkConnector", []))

    @jsii.member(jsii_name="resetSumologicConnector")
    def reset_sumologic_connector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSumologicConnector", []))

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
    @jsii.member(jsii_name="azureConnector")
    def azure_connector(self) -> "DatastreamAzureConnectorOutputReference":
        return typing.cast("DatastreamAzureConnectorOutputReference", jsii.get(self, "azureConnector"))

    @builtins.property
    @jsii.member(jsii_name="createdBy")
    def created_by(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdBy"))

    @builtins.property
    @jsii.member(jsii_name="createdDate")
    def created_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdDate"))

    @builtins.property
    @jsii.member(jsii_name="datadogConnector")
    def datadog_connector(self) -> "DatastreamDatadogConnectorOutputReference":
        return typing.cast("DatastreamDatadogConnectorOutputReference", jsii.get(self, "datadogConnector"))

    @builtins.property
    @jsii.member(jsii_name="deliveryConfiguration")
    def delivery_configuration(
        self,
    ) -> "DatastreamDeliveryConfigurationOutputReference":
        return typing.cast("DatastreamDeliveryConfigurationOutputReference", jsii.get(self, "deliveryConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="elasticsearchConnector")
    def elasticsearch_connector(
        self,
    ) -> "DatastreamElasticsearchConnectorOutputReference":
        return typing.cast("DatastreamElasticsearchConnectorOutputReference", jsii.get(self, "elasticsearchConnector"))

    @builtins.property
    @jsii.member(jsii_name="gcsConnector")
    def gcs_connector(self) -> "DatastreamGcsConnectorOutputReference":
        return typing.cast("DatastreamGcsConnectorOutputReference", jsii.get(self, "gcsConnector"))

    @builtins.property
    @jsii.member(jsii_name="httpsConnector")
    def https_connector(self) -> "DatastreamHttpsConnectorOutputReference":
        return typing.cast("DatastreamHttpsConnectorOutputReference", jsii.get(self, "httpsConnector"))

    @builtins.property
    @jsii.member(jsii_name="latestVersion")
    def latest_version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "latestVersion"))

    @builtins.property
    @jsii.member(jsii_name="logglyConnector")
    def loggly_connector(self) -> "DatastreamLogglyConnectorOutputReference":
        return typing.cast("DatastreamLogglyConnectorOutputReference", jsii.get(self, "logglyConnector"))

    @builtins.property
    @jsii.member(jsii_name="modifiedBy")
    def modified_by(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "modifiedBy"))

    @builtins.property
    @jsii.member(jsii_name="modifiedDate")
    def modified_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "modifiedDate"))

    @builtins.property
    @jsii.member(jsii_name="newRelicConnector")
    def new_relic_connector(self) -> "DatastreamNewRelicConnectorOutputReference":
        return typing.cast("DatastreamNewRelicConnectorOutputReference", jsii.get(self, "newRelicConnector"))

    @builtins.property
    @jsii.member(jsii_name="oracleConnector")
    def oracle_connector(self) -> "DatastreamOracleConnectorOutputReference":
        return typing.cast("DatastreamOracleConnectorOutputReference", jsii.get(self, "oracleConnector"))

    @builtins.property
    @jsii.member(jsii_name="papiJson")
    def papi_json(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "papiJson"))

    @builtins.property
    @jsii.member(jsii_name="productId")
    def product_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "productId"))

    @builtins.property
    @jsii.member(jsii_name="s3Connector")
    def s3_connector(self) -> "DatastreamS3ConnectorOutputReference":
        return typing.cast("DatastreamS3ConnectorOutputReference", jsii.get(self, "s3Connector"))

    @builtins.property
    @jsii.member(jsii_name="splunkConnector")
    def splunk_connector(self) -> "DatastreamSplunkConnectorOutputReference":
        return typing.cast("DatastreamSplunkConnectorOutputReference", jsii.get(self, "splunkConnector"))

    @builtins.property
    @jsii.member(jsii_name="streamVersion")
    def stream_version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "streamVersion"))

    @builtins.property
    @jsii.member(jsii_name="sumologicConnector")
    def sumologic_connector(self) -> "DatastreamSumologicConnectorOutputReference":
        return typing.cast("DatastreamSumologicConnectorOutputReference", jsii.get(self, "sumologicConnector"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DatastreamTimeoutsOutputReference":
        return typing.cast("DatastreamTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="activeInput")
    def active_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "activeInput"))

    @builtins.property
    @jsii.member(jsii_name="azureConnectorInput")
    def azure_connector_input(self) -> typing.Optional["DatastreamAzureConnector"]:
        return typing.cast(typing.Optional["DatastreamAzureConnector"], jsii.get(self, "azureConnectorInput"))

    @builtins.property
    @jsii.member(jsii_name="collectMidgressInput")
    def collect_midgress_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "collectMidgressInput"))

    @builtins.property
    @jsii.member(jsii_name="contractIdInput")
    def contract_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contractIdInput"))

    @builtins.property
    @jsii.member(jsii_name="datadogConnectorInput")
    def datadog_connector_input(self) -> typing.Optional["DatastreamDatadogConnector"]:
        return typing.cast(typing.Optional["DatastreamDatadogConnector"], jsii.get(self, "datadogConnectorInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetFieldsInput")
    def dataset_fields_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "datasetFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="deliveryConfigurationInput")
    def delivery_configuration_input(
        self,
    ) -> typing.Optional["DatastreamDeliveryConfiguration"]:
        return typing.cast(typing.Optional["DatastreamDeliveryConfiguration"], jsii.get(self, "deliveryConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="elasticsearchConnectorInput")
    def elasticsearch_connector_input(
        self,
    ) -> typing.Optional["DatastreamElasticsearchConnector"]:
        return typing.cast(typing.Optional["DatastreamElasticsearchConnector"], jsii.get(self, "elasticsearchConnectorInput"))

    @builtins.property
    @jsii.member(jsii_name="gcsConnectorInput")
    def gcs_connector_input(self) -> typing.Optional["DatastreamGcsConnector"]:
        return typing.cast(typing.Optional["DatastreamGcsConnector"], jsii.get(self, "gcsConnectorInput"))

    @builtins.property
    @jsii.member(jsii_name="groupIdInput")
    def group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="httpsConnectorInput")
    def https_connector_input(self) -> typing.Optional["DatastreamHttpsConnector"]:
        return typing.cast(typing.Optional["DatastreamHttpsConnector"], jsii.get(self, "httpsConnectorInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="logglyConnectorInput")
    def loggly_connector_input(self) -> typing.Optional["DatastreamLogglyConnector"]:
        return typing.cast(typing.Optional["DatastreamLogglyConnector"], jsii.get(self, "logglyConnectorInput"))

    @builtins.property
    @jsii.member(jsii_name="newRelicConnectorInput")
    def new_relic_connector_input(
        self,
    ) -> typing.Optional["DatastreamNewRelicConnector"]:
        return typing.cast(typing.Optional["DatastreamNewRelicConnector"], jsii.get(self, "newRelicConnectorInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationEmailsInput")
    def notification_emails_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "notificationEmailsInput"))

    @builtins.property
    @jsii.member(jsii_name="oracleConnectorInput")
    def oracle_connector_input(self) -> typing.Optional["DatastreamOracleConnector"]:
        return typing.cast(typing.Optional["DatastreamOracleConnector"], jsii.get(self, "oracleConnectorInput"))

    @builtins.property
    @jsii.member(jsii_name="propertiesInput")
    def properties_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "propertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="s3ConnectorInput")
    def s3_connector_input(self) -> typing.Optional["DatastreamS3Connector"]:
        return typing.cast(typing.Optional["DatastreamS3Connector"], jsii.get(self, "s3ConnectorInput"))

    @builtins.property
    @jsii.member(jsii_name="splunkConnectorInput")
    def splunk_connector_input(self) -> typing.Optional["DatastreamSplunkConnector"]:
        return typing.cast(typing.Optional["DatastreamSplunkConnector"], jsii.get(self, "splunkConnectorInput"))

    @builtins.property
    @jsii.member(jsii_name="streamNameInput")
    def stream_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streamNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sumologicConnectorInput")
    def sumologic_connector_input(
        self,
    ) -> typing.Optional["DatastreamSumologicConnector"]:
        return typing.cast(typing.Optional["DatastreamSumologicConnector"], jsii.get(self, "sumologicConnectorInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "DatastreamTimeouts"]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "DatastreamTimeouts"]], jsii.get(self, "timeoutsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__5616c88f95f7eccedc2ddedb799e592570145ea3e1ba1a37045b3eb6ad1b67d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "active", value)

    @builtins.property
    @jsii.member(jsii_name="collectMidgress")
    def collect_midgress(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "collectMidgress"))

    @collect_midgress.setter
    def collect_midgress(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cf4aabaf2e273d0d908f4ffa736348b6acb5081e7a6f503f53ead2fe996ba6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "collectMidgress", value)

    @builtins.property
    @jsii.member(jsii_name="contractId")
    def contract_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contractId"))

    @contract_id.setter
    def contract_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f100ab39744218f053b1736bbd9cf989f8d7a9bf44e9e124513054ee4725d85e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contractId", value)

    @builtins.property
    @jsii.member(jsii_name="datasetFields")
    def dataset_fields(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "datasetFields"))

    @dataset_fields.setter
    def dataset_fields(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2ec26371b1390d6bc90e4b424dde5085c868e45ae6d265ae07ec1ce88d2af1e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetFields", value)

    @builtins.property
    @jsii.member(jsii_name="groupId")
    def group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupId"))

    @group_id.setter
    def group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61f286b0021b8745f8a4902eacc8c3b6d3f5e19ca875b2e21679c506b8e7837c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e694ece03329bd5621bff093e8d22fef41c16405b05a1ef4ae6123bb16215707)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="notificationEmails")
    def notification_emails(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "notificationEmails"))

    @notification_emails.setter
    def notification_emails(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b3f3bb6e3a944571147caa1ba6893a86e053a9fa17c13b0e040154bbbb5bdd7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationEmails", value)

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "properties"))

    @properties.setter
    def properties(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5afb93c1a290c533da98fac1f91f934d4363ea379eae0bb189478fe203e20e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "properties", value)

    @builtins.property
    @jsii.member(jsii_name="streamName")
    def stream_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streamName"))

    @stream_name.setter
    def stream_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__462eebc52fdaa2d8bde23ff208b881ade325fa90d918363dec78006e1e9d914e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamName", value)


@jsii.data_type(
    jsii_type="akamai.datastream.DatastreamAzureConnector",
    jsii_struct_bases=[],
    name_mapping={
        "access_key": "accessKey",
        "account_name": "accountName",
        "container_name": "containerName",
        "display_name": "displayName",
        "path": "path",
    },
)
class DatastreamAzureConnector:
    def __init__(
        self,
        *,
        access_key: builtins.str,
        account_name: builtins.str,
        container_name: builtins.str,
        display_name: builtins.str,
        path: builtins.str,
    ) -> None:
        '''
        :param access_key: Access keys associated with Azure Storage account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#access_key Datastream#access_key}
        :param account_name: Specifies the Azure Storage account name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#account_name Datastream#account_name}
        :param container_name: Specifies the Azure Storage container name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#container_name Datastream#container_name}
        :param display_name: The name of the connector. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#display_name Datastream#display_name}
        :param path: The path to the folder within Azure Storage container where logs will be stored. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#path Datastream#path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__889176b7a91c186ba74438804fb29033ea2d6856a3f1dfc923acb06e31318b8f)
            check_type(argname="argument access_key", value=access_key, expected_type=type_hints["access_key"])
            check_type(argname="argument account_name", value=account_name, expected_type=type_hints["account_name"])
            check_type(argname="argument container_name", value=container_name, expected_type=type_hints["container_name"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_key": access_key,
            "account_name": account_name,
            "container_name": container_name,
            "display_name": display_name,
            "path": path,
        }

    @builtins.property
    def access_key(self) -> builtins.str:
        '''Access keys associated with Azure Storage account.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#access_key Datastream#access_key}
        '''
        result = self._values.get("access_key")
        assert result is not None, "Required property 'access_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_name(self) -> builtins.str:
        '''Specifies the Azure Storage account name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#account_name Datastream#account_name}
        '''
        result = self._values.get("account_name")
        assert result is not None, "Required property 'account_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_name(self) -> builtins.str:
        '''Specifies the Azure Storage container name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#container_name Datastream#container_name}
        '''
        result = self._values.get("container_name")
        assert result is not None, "Required property 'container_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def display_name(self) -> builtins.str:
        '''The name of the connector.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#display_name Datastream#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''The path to the folder within Azure Storage container where logs will be stored.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#path Datastream#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamAzureConnector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatastreamAzureConnectorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.datastream.DatastreamAzureConnectorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c35185cf030e1db2e5bb2d0e4bffb8d9dab7497af52390c6b1d0ea2b56dad408)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="compressLogs")
    def compress_logs(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "compressLogs"))

    @builtins.property
    @jsii.member(jsii_name="accessKeyInput")
    def access_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="accountNameInput")
    def account_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountNameInput"))

    @builtins.property
    @jsii.member(jsii_name="containerNameInput")
    def container_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="accessKey")
    def access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessKey"))

    @access_key.setter
    def access_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__feeb7c9c446111e2578c872ef6b7db5cf7e99aa3866e5da1ca4c8ba5f481459d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessKey", value)

    @builtins.property
    @jsii.member(jsii_name="accountName")
    def account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountName"))

    @account_name.setter
    def account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6dedced9ff591f528525ae1ea6f3dd909f747163ca4cacffd0449b7dc761ee1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountName", value)

    @builtins.property
    @jsii.member(jsii_name="containerName")
    def container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerName"))

    @container_name.setter
    def container_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ed8289fb6906910cfe3c2598554da85d5dceee09ced83f8666791adf2a81cc2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerName", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17229af0294d9e033556031c934cff9781c5f6f17140a2ea8a89d1360692838f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1684e8b3dd2814fa540a5e8fe672b1997ce5f3c2285dabda83a407e8f7bb09a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DatastreamAzureConnector]:
        return typing.cast(typing.Optional[DatastreamAzureConnector], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DatastreamAzureConnector]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0732f0eade8e00032b6c277a7b72e929486d6e64eecd2fb41f1a5da56bbf847)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.datastream.DatastreamConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "active": "active",
        "contract_id": "contractId",
        "dataset_fields": "datasetFields",
        "delivery_configuration": "deliveryConfiguration",
        "group_id": "groupId",
        "properties": "properties",
        "stream_name": "streamName",
        "azure_connector": "azureConnector",
        "collect_midgress": "collectMidgress",
        "datadog_connector": "datadogConnector",
        "elasticsearch_connector": "elasticsearchConnector",
        "gcs_connector": "gcsConnector",
        "https_connector": "httpsConnector",
        "id": "id",
        "loggly_connector": "logglyConnector",
        "new_relic_connector": "newRelicConnector",
        "notification_emails": "notificationEmails",
        "oracle_connector": "oracleConnector",
        "s3_connector": "s3Connector",
        "splunk_connector": "splunkConnector",
        "sumologic_connector": "sumologicConnector",
        "timeouts": "timeouts",
    },
)
class DatastreamConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        active: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        contract_id: builtins.str,
        dataset_fields: typing.Sequence[jsii.Number],
        delivery_configuration: typing.Union["DatastreamDeliveryConfiguration", typing.Dict[builtins.str, typing.Any]],
        group_id: builtins.str,
        properties: typing.Sequence[builtins.str],
        stream_name: builtins.str,
        azure_connector: typing.Optional[typing.Union[DatastreamAzureConnector, typing.Dict[builtins.str, typing.Any]]] = None,
        collect_midgress: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        datadog_connector: typing.Optional[typing.Union["DatastreamDatadogConnector", typing.Dict[builtins.str, typing.Any]]] = None,
        elasticsearch_connector: typing.Optional[typing.Union["DatastreamElasticsearchConnector", typing.Dict[builtins.str, typing.Any]]] = None,
        gcs_connector: typing.Optional[typing.Union["DatastreamGcsConnector", typing.Dict[builtins.str, typing.Any]]] = None,
        https_connector: typing.Optional[typing.Union["DatastreamHttpsConnector", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        loggly_connector: typing.Optional[typing.Union["DatastreamLogglyConnector", typing.Dict[builtins.str, typing.Any]]] = None,
        new_relic_connector: typing.Optional[typing.Union["DatastreamNewRelicConnector", typing.Dict[builtins.str, typing.Any]]] = None,
        notification_emails: typing.Optional[typing.Sequence[builtins.str]] = None,
        oracle_connector: typing.Optional[typing.Union["DatastreamOracleConnector", typing.Dict[builtins.str, typing.Any]]] = None,
        s3_connector: typing.Optional[typing.Union["DatastreamS3Connector", typing.Dict[builtins.str, typing.Any]]] = None,
        splunk_connector: typing.Optional[typing.Union["DatastreamSplunkConnector", typing.Dict[builtins.str, typing.Any]]] = None,
        sumologic_connector: typing.Optional[typing.Union["DatastreamSumologicConnector", typing.Dict[builtins.str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["DatastreamTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param active: Defining if stream should be active or not. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#active Datastream#active}
        :param contract_id: Identifies the contract that has access to the product. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#contract_id Datastream#contract_id}
        :param dataset_fields: A list of data set fields selected from the associated template that the stream monitors in logs. The order of the identifiers define how the value for these fields appear in the log lines Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#dataset_fields Datastream#dataset_fields}
        :param delivery_configuration: delivery_configuration block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#delivery_configuration Datastream#delivery_configuration}
        :param group_id: Identifies the group that has access to the product and for which the stream configuration was created. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#group_id Datastream#group_id}
        :param properties: Identifies the properties monitored in the stream. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#properties Datastream#properties}
        :param stream_name: The name of the stream. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#stream_name Datastream#stream_name}
        :param azure_connector: azure_connector block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#azure_connector Datastream#azure_connector}
        :param collect_midgress: Identifies if stream needs to collect midgress data. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#collect_midgress Datastream#collect_midgress}
        :param datadog_connector: datadog_connector block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#datadog_connector Datastream#datadog_connector}
        :param elasticsearch_connector: elasticsearch_connector block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#elasticsearch_connector Datastream#elasticsearch_connector}
        :param gcs_connector: gcs_connector block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#gcs_connector Datastream#gcs_connector}
        :param https_connector: https_connector block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#https_connector Datastream#https_connector}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#id Datastream#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param loggly_connector: loggly_connector block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#loggly_connector Datastream#loggly_connector}
        :param new_relic_connector: new_relic_connector block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#new_relic_connector Datastream#new_relic_connector}
        :param notification_emails: List of email addresses where the system sends notifications about activations and deactivations of the stream. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#notification_emails Datastream#notification_emails}
        :param oracle_connector: oracle_connector block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#oracle_connector Datastream#oracle_connector}
        :param s3_connector: s3_connector block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#s3_connector Datastream#s3_connector}
        :param splunk_connector: splunk_connector block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#splunk_connector Datastream#splunk_connector}
        :param sumologic_connector: sumologic_connector block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#sumologic_connector Datastream#sumologic_connector}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#timeouts Datastream#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(delivery_configuration, dict):
            delivery_configuration = DatastreamDeliveryConfiguration(**delivery_configuration)
        if isinstance(azure_connector, dict):
            azure_connector = DatastreamAzureConnector(**azure_connector)
        if isinstance(datadog_connector, dict):
            datadog_connector = DatastreamDatadogConnector(**datadog_connector)
        if isinstance(elasticsearch_connector, dict):
            elasticsearch_connector = DatastreamElasticsearchConnector(**elasticsearch_connector)
        if isinstance(gcs_connector, dict):
            gcs_connector = DatastreamGcsConnector(**gcs_connector)
        if isinstance(https_connector, dict):
            https_connector = DatastreamHttpsConnector(**https_connector)
        if isinstance(loggly_connector, dict):
            loggly_connector = DatastreamLogglyConnector(**loggly_connector)
        if isinstance(new_relic_connector, dict):
            new_relic_connector = DatastreamNewRelicConnector(**new_relic_connector)
        if isinstance(oracle_connector, dict):
            oracle_connector = DatastreamOracleConnector(**oracle_connector)
        if isinstance(s3_connector, dict):
            s3_connector = DatastreamS3Connector(**s3_connector)
        if isinstance(splunk_connector, dict):
            splunk_connector = DatastreamSplunkConnector(**splunk_connector)
        if isinstance(sumologic_connector, dict):
            sumologic_connector = DatastreamSumologicConnector(**sumologic_connector)
        if isinstance(timeouts, dict):
            timeouts = DatastreamTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c4366ae5518ac295d84409908df1fdcf2dd96da79082b5dc4707feb8338efce)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument active", value=active, expected_type=type_hints["active"])
            check_type(argname="argument contract_id", value=contract_id, expected_type=type_hints["contract_id"])
            check_type(argname="argument dataset_fields", value=dataset_fields, expected_type=type_hints["dataset_fields"])
            check_type(argname="argument delivery_configuration", value=delivery_configuration, expected_type=type_hints["delivery_configuration"])
            check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument stream_name", value=stream_name, expected_type=type_hints["stream_name"])
            check_type(argname="argument azure_connector", value=azure_connector, expected_type=type_hints["azure_connector"])
            check_type(argname="argument collect_midgress", value=collect_midgress, expected_type=type_hints["collect_midgress"])
            check_type(argname="argument datadog_connector", value=datadog_connector, expected_type=type_hints["datadog_connector"])
            check_type(argname="argument elasticsearch_connector", value=elasticsearch_connector, expected_type=type_hints["elasticsearch_connector"])
            check_type(argname="argument gcs_connector", value=gcs_connector, expected_type=type_hints["gcs_connector"])
            check_type(argname="argument https_connector", value=https_connector, expected_type=type_hints["https_connector"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument loggly_connector", value=loggly_connector, expected_type=type_hints["loggly_connector"])
            check_type(argname="argument new_relic_connector", value=new_relic_connector, expected_type=type_hints["new_relic_connector"])
            check_type(argname="argument notification_emails", value=notification_emails, expected_type=type_hints["notification_emails"])
            check_type(argname="argument oracle_connector", value=oracle_connector, expected_type=type_hints["oracle_connector"])
            check_type(argname="argument s3_connector", value=s3_connector, expected_type=type_hints["s3_connector"])
            check_type(argname="argument splunk_connector", value=splunk_connector, expected_type=type_hints["splunk_connector"])
            check_type(argname="argument sumologic_connector", value=sumologic_connector, expected_type=type_hints["sumologic_connector"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "active": active,
            "contract_id": contract_id,
            "dataset_fields": dataset_fields,
            "delivery_configuration": delivery_configuration,
            "group_id": group_id,
            "properties": properties,
            "stream_name": stream_name,
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
        if azure_connector is not None:
            self._values["azure_connector"] = azure_connector
        if collect_midgress is not None:
            self._values["collect_midgress"] = collect_midgress
        if datadog_connector is not None:
            self._values["datadog_connector"] = datadog_connector
        if elasticsearch_connector is not None:
            self._values["elasticsearch_connector"] = elasticsearch_connector
        if gcs_connector is not None:
            self._values["gcs_connector"] = gcs_connector
        if https_connector is not None:
            self._values["https_connector"] = https_connector
        if id is not None:
            self._values["id"] = id
        if loggly_connector is not None:
            self._values["loggly_connector"] = loggly_connector
        if new_relic_connector is not None:
            self._values["new_relic_connector"] = new_relic_connector
        if notification_emails is not None:
            self._values["notification_emails"] = notification_emails
        if oracle_connector is not None:
            self._values["oracle_connector"] = oracle_connector
        if s3_connector is not None:
            self._values["s3_connector"] = s3_connector
        if splunk_connector is not None:
            self._values["splunk_connector"] = splunk_connector
        if sumologic_connector is not None:
            self._values["sumologic_connector"] = sumologic_connector
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
    def active(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Defining if stream should be active or not.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#active Datastream#active}
        '''
        result = self._values.get("active")
        assert result is not None, "Required property 'active' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def contract_id(self) -> builtins.str:
        '''Identifies the contract that has access to the product.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#contract_id Datastream#contract_id}
        '''
        result = self._values.get("contract_id")
        assert result is not None, "Required property 'contract_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dataset_fields(self) -> typing.List[jsii.Number]:
        '''A list of data set fields selected from the associated template that the stream monitors in logs.

        The order of the identifiers define how the value for these fields appear in the log lines

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#dataset_fields Datastream#dataset_fields}
        '''
        result = self._values.get("dataset_fields")
        assert result is not None, "Required property 'dataset_fields' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    @builtins.property
    def delivery_configuration(self) -> "DatastreamDeliveryConfiguration":
        '''delivery_configuration block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#delivery_configuration Datastream#delivery_configuration}
        '''
        result = self._values.get("delivery_configuration")
        assert result is not None, "Required property 'delivery_configuration' is missing"
        return typing.cast("DatastreamDeliveryConfiguration", result)

    @builtins.property
    def group_id(self) -> builtins.str:
        '''Identifies the group that has access to the product and for which the stream configuration was created.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#group_id Datastream#group_id}
        '''
        result = self._values.get("group_id")
        assert result is not None, "Required property 'group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def properties(self) -> typing.List[builtins.str]:
        '''Identifies the properties monitored in the stream.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#properties Datastream#properties}
        '''
        result = self._values.get("properties")
        assert result is not None, "Required property 'properties' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def stream_name(self) -> builtins.str:
        '''The name of the stream.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#stream_name Datastream#stream_name}
        '''
        result = self._values.get("stream_name")
        assert result is not None, "Required property 'stream_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def azure_connector(self) -> typing.Optional[DatastreamAzureConnector]:
        '''azure_connector block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#azure_connector Datastream#azure_connector}
        '''
        result = self._values.get("azure_connector")
        return typing.cast(typing.Optional[DatastreamAzureConnector], result)

    @builtins.property
    def collect_midgress(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Identifies if stream needs to collect midgress data.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#collect_midgress Datastream#collect_midgress}
        '''
        result = self._values.get("collect_midgress")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def datadog_connector(self) -> typing.Optional["DatastreamDatadogConnector"]:
        '''datadog_connector block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#datadog_connector Datastream#datadog_connector}
        '''
        result = self._values.get("datadog_connector")
        return typing.cast(typing.Optional["DatastreamDatadogConnector"], result)

    @builtins.property
    def elasticsearch_connector(
        self,
    ) -> typing.Optional["DatastreamElasticsearchConnector"]:
        '''elasticsearch_connector block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#elasticsearch_connector Datastream#elasticsearch_connector}
        '''
        result = self._values.get("elasticsearch_connector")
        return typing.cast(typing.Optional["DatastreamElasticsearchConnector"], result)

    @builtins.property
    def gcs_connector(self) -> typing.Optional["DatastreamGcsConnector"]:
        '''gcs_connector block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#gcs_connector Datastream#gcs_connector}
        '''
        result = self._values.get("gcs_connector")
        return typing.cast(typing.Optional["DatastreamGcsConnector"], result)

    @builtins.property
    def https_connector(self) -> typing.Optional["DatastreamHttpsConnector"]:
        '''https_connector block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#https_connector Datastream#https_connector}
        '''
        result = self._values.get("https_connector")
        return typing.cast(typing.Optional["DatastreamHttpsConnector"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#id Datastream#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def loggly_connector(self) -> typing.Optional["DatastreamLogglyConnector"]:
        '''loggly_connector block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#loggly_connector Datastream#loggly_connector}
        '''
        result = self._values.get("loggly_connector")
        return typing.cast(typing.Optional["DatastreamLogglyConnector"], result)

    @builtins.property
    def new_relic_connector(self) -> typing.Optional["DatastreamNewRelicConnector"]:
        '''new_relic_connector block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#new_relic_connector Datastream#new_relic_connector}
        '''
        result = self._values.get("new_relic_connector")
        return typing.cast(typing.Optional["DatastreamNewRelicConnector"], result)

    @builtins.property
    def notification_emails(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of email addresses where the system sends notifications about activations and deactivations of the stream.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#notification_emails Datastream#notification_emails}
        '''
        result = self._values.get("notification_emails")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def oracle_connector(self) -> typing.Optional["DatastreamOracleConnector"]:
        '''oracle_connector block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#oracle_connector Datastream#oracle_connector}
        '''
        result = self._values.get("oracle_connector")
        return typing.cast(typing.Optional["DatastreamOracleConnector"], result)

    @builtins.property
    def s3_connector(self) -> typing.Optional["DatastreamS3Connector"]:
        '''s3_connector block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#s3_connector Datastream#s3_connector}
        '''
        result = self._values.get("s3_connector")
        return typing.cast(typing.Optional["DatastreamS3Connector"], result)

    @builtins.property
    def splunk_connector(self) -> typing.Optional["DatastreamSplunkConnector"]:
        '''splunk_connector block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#splunk_connector Datastream#splunk_connector}
        '''
        result = self._values.get("splunk_connector")
        return typing.cast(typing.Optional["DatastreamSplunkConnector"], result)

    @builtins.property
    def sumologic_connector(self) -> typing.Optional["DatastreamSumologicConnector"]:
        '''sumologic_connector block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#sumologic_connector Datastream#sumologic_connector}
        '''
        result = self._values.get("sumologic_connector")
        return typing.cast(typing.Optional["DatastreamSumologicConnector"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DatastreamTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#timeouts Datastream#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DatastreamTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.datastream.DatastreamDatadogConnector",
    jsii_struct_bases=[],
    name_mapping={
        "auth_token": "authToken",
        "display_name": "displayName",
        "endpoint": "endpoint",
        "compress_logs": "compressLogs",
        "service": "service",
        "source": "source",
        "tags": "tags",
    },
)
class DatastreamDatadogConnector:
    def __init__(
        self,
        *,
        auth_token: builtins.str,
        display_name: builtins.str,
        endpoint: builtins.str,
        compress_logs: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        service: typing.Optional[builtins.str] = None,
        source: typing.Optional[builtins.str] = None,
        tags: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_token: The API key associated with Datadog account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#auth_token Datastream#auth_token}
        :param display_name: The name of the connector. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#display_name Datastream#display_name}
        :param endpoint: The Datadog endpoint where logs will be stored. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#endpoint Datastream#endpoint}
        :param compress_logs: Indicates whether the logs should be compressed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#compress_logs Datastream#compress_logs}
        :param service: The service of the Datadog connector. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#service Datastream#service}
        :param source: The source of the Datadog connector. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#source Datastream#source}
        :param tags: The tags of the Datadog connector. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#tags Datastream#tags}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12735ef33d8684197e814eb496b60558ee2c19f2f5a5f643597b5b2900b5f131)
            check_type(argname="argument auth_token", value=auth_token, expected_type=type_hints["auth_token"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument compress_logs", value=compress_logs, expected_type=type_hints["compress_logs"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "auth_token": auth_token,
            "display_name": display_name,
            "endpoint": endpoint,
        }
        if compress_logs is not None:
            self._values["compress_logs"] = compress_logs
        if service is not None:
            self._values["service"] = service
        if source is not None:
            self._values["source"] = source
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def auth_token(self) -> builtins.str:
        '''The API key associated with Datadog account.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#auth_token Datastream#auth_token}
        '''
        result = self._values.get("auth_token")
        assert result is not None, "Required property 'auth_token' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def display_name(self) -> builtins.str:
        '''The name of the connector.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#display_name Datastream#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def endpoint(self) -> builtins.str:
        '''The Datadog endpoint where logs will be stored.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#endpoint Datastream#endpoint}
        '''
        result = self._values.get("endpoint")
        assert result is not None, "Required property 'endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def compress_logs(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Indicates whether the logs should be compressed.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#compress_logs Datastream#compress_logs}
        '''
        result = self._values.get("compress_logs")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def service(self) -> typing.Optional[builtins.str]:
        '''The service of the Datadog connector.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#service Datastream#service}
        '''
        result = self._values.get("service")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        '''The source of the Datadog connector.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#source Datastream#source}
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[builtins.str]:
        '''The tags of the Datadog connector.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#tags Datastream#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamDatadogConnector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatastreamDatadogConnectorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.datastream.DatastreamDatadogConnectorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5bbebad2884ed2014dac00dee3f39ce7626c938c3e31f7c5cfbf78453063083f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCompressLogs")
    def reset_compress_logs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompressLogs", []))

    @jsii.member(jsii_name="resetService")
    def reset_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetService", []))

    @jsii.member(jsii_name="resetSource")
    def reset_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSource", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @builtins.property
    @jsii.member(jsii_name="authTokenInput")
    def auth_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="compressLogsInput")
    def compress_logs_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "compressLogsInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="authToken")
    def auth_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authToken"))

    @auth_token.setter
    def auth_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b34229c187ebadd57d7e51e9f9e788e6e49b213bec25e6635d744ed031f90a89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authToken", value)

    @builtins.property
    @jsii.member(jsii_name="compressLogs")
    def compress_logs(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "compressLogs"))

    @compress_logs.setter
    def compress_logs(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9920293f5e0f8455b169f8668fd8861ca0c20fa91b5aa8a1e70ce7ac9c7e7315)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compressLogs", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87c619ddd2b8ecb45025bfbaa50955e905322102de50662bbd343da6a1448240)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d8667e72af45163e274a8ef251f5ff23a341440b41e7dfd48ec8188d23ad021)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "service"))

    @service.setter
    def service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee6325a72954853d446326f9738f87d2bd5a988185ffc9ff50483345e0532c34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "service", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__208fb39a21607da83b9d7be4712adb56290f6ff4bf6d9488974e9f72cc650904)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd0e7cbd0f9404a51d8f24c17fe4f2cb29591b3a8087cc5e5b4dcce0fe9c30ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DatastreamDatadogConnector]:
        return typing.cast(typing.Optional[DatastreamDatadogConnector], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatastreamDatadogConnector],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9952b513110f2a8e82c5eebe9c32bef9f0a35c1cd42f23f46e70f140f3f7e76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.datastream.DatastreamDeliveryConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "format": "format",
        "frequency": "frequency",
        "field_delimiter": "fieldDelimiter",
        "upload_file_prefix": "uploadFilePrefix",
        "upload_file_suffix": "uploadFileSuffix",
    },
)
class DatastreamDeliveryConfiguration:
    def __init__(
        self,
        *,
        format: builtins.str,
        frequency: typing.Union["DatastreamDeliveryConfigurationFrequency", typing.Dict[builtins.str, typing.Any]],
        field_delimiter: typing.Optional[builtins.str] = None,
        upload_file_prefix: typing.Optional[builtins.str] = None,
        upload_file_suffix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param format: The format in which logs will be received. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#format Datastream#format}
        :param frequency: frequency block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#frequency Datastream#frequency}
        :param field_delimiter: A delimiter that you use to separate data set fields in log lines. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#field_delimiter Datastream#field_delimiter}
        :param upload_file_prefix: The prefix of the log file that will be send to a destination. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#upload_file_prefix Datastream#upload_file_prefix}
        :param upload_file_suffix: The suffix of the log file that will be send to a destination. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#upload_file_suffix Datastream#upload_file_suffix}
        '''
        if isinstance(frequency, dict):
            frequency = DatastreamDeliveryConfigurationFrequency(**frequency)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9d61e42d9bd2a0c792677b2d5bdde380efff4023265e99dab04933c1b8650bf)
            check_type(argname="argument format", value=format, expected_type=type_hints["format"])
            check_type(argname="argument frequency", value=frequency, expected_type=type_hints["frequency"])
            check_type(argname="argument field_delimiter", value=field_delimiter, expected_type=type_hints["field_delimiter"])
            check_type(argname="argument upload_file_prefix", value=upload_file_prefix, expected_type=type_hints["upload_file_prefix"])
            check_type(argname="argument upload_file_suffix", value=upload_file_suffix, expected_type=type_hints["upload_file_suffix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "format": format,
            "frequency": frequency,
        }
        if field_delimiter is not None:
            self._values["field_delimiter"] = field_delimiter
        if upload_file_prefix is not None:
            self._values["upload_file_prefix"] = upload_file_prefix
        if upload_file_suffix is not None:
            self._values["upload_file_suffix"] = upload_file_suffix

    @builtins.property
    def format(self) -> builtins.str:
        '''The format in which logs will be received.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#format Datastream#format}
        '''
        result = self._values.get("format")
        assert result is not None, "Required property 'format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def frequency(self) -> "DatastreamDeliveryConfigurationFrequency":
        '''frequency block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#frequency Datastream#frequency}
        '''
        result = self._values.get("frequency")
        assert result is not None, "Required property 'frequency' is missing"
        return typing.cast("DatastreamDeliveryConfigurationFrequency", result)

    @builtins.property
    def field_delimiter(self) -> typing.Optional[builtins.str]:
        '''A delimiter that you use to separate data set fields in log lines.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#field_delimiter Datastream#field_delimiter}
        '''
        result = self._values.get("field_delimiter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def upload_file_prefix(self) -> typing.Optional[builtins.str]:
        '''The prefix of the log file that will be send to a destination.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#upload_file_prefix Datastream#upload_file_prefix}
        '''
        result = self._values.get("upload_file_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def upload_file_suffix(self) -> typing.Optional[builtins.str]:
        '''The suffix of the log file that will be send to a destination.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#upload_file_suffix Datastream#upload_file_suffix}
        '''
        result = self._values.get("upload_file_suffix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamDeliveryConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="akamai.datastream.DatastreamDeliveryConfigurationFrequency",
    jsii_struct_bases=[],
    name_mapping={"interval_in_secs": "intervalInSecs"},
)
class DatastreamDeliveryConfigurationFrequency:
    def __init__(self, *, interval_in_secs: jsii.Number) -> None:
        '''
        :param interval_in_secs: The time in seconds after which the system bundles log lines into a file and sends it to a destination. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#interval_in_secs Datastream#interval_in_secs}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3fc16d46e2f85e21f68893d478bd421dee853df32555f5457ffa28b9ba80621)
            check_type(argname="argument interval_in_secs", value=interval_in_secs, expected_type=type_hints["interval_in_secs"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "interval_in_secs": interval_in_secs,
        }

    @builtins.property
    def interval_in_secs(self) -> jsii.Number:
        '''The time in seconds after which the system bundles log lines into a file and sends it to a destination.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#interval_in_secs Datastream#interval_in_secs}
        '''
        result = self._values.get("interval_in_secs")
        assert result is not None, "Required property 'interval_in_secs' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamDeliveryConfigurationFrequency(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatastreamDeliveryConfigurationFrequencyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.datastream.DatastreamDeliveryConfigurationFrequencyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e2c477662ec7fc2f3ef204164aeba05eb9e3df5105fd0054befc9315c64e1c70)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="intervalInSecsInput")
    def interval_in_secs_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalInSecsInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalInSecs")
    def interval_in_secs(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "intervalInSecs"))

    @interval_in_secs.setter
    def interval_in_secs(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__009eae23cef0ef9ff1bbd97ccfdbf1aa809d7f45928377cd44f565b677ea3220)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intervalInSecs", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DatastreamDeliveryConfigurationFrequency]:
        return typing.cast(typing.Optional[DatastreamDeliveryConfigurationFrequency], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatastreamDeliveryConfigurationFrequency],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e56cac2c9d183e209e2be92d058e783ff85cdc7e7e58a2c3f5b2149ec3729c33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DatastreamDeliveryConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.datastream.DatastreamDeliveryConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c7d7c15445c8a42a3a3e01ae7291af1221a8a93808b780869970cb294482f8ee)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putFrequency")
    def put_frequency(self, *, interval_in_secs: jsii.Number) -> None:
        '''
        :param interval_in_secs: The time in seconds after which the system bundles log lines into a file and sends it to a destination. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#interval_in_secs Datastream#interval_in_secs}
        '''
        value = DatastreamDeliveryConfigurationFrequency(
            interval_in_secs=interval_in_secs
        )

        return typing.cast(None, jsii.invoke(self, "putFrequency", [value]))

    @jsii.member(jsii_name="resetFieldDelimiter")
    def reset_field_delimiter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFieldDelimiter", []))

    @jsii.member(jsii_name="resetUploadFilePrefix")
    def reset_upload_file_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUploadFilePrefix", []))

    @jsii.member(jsii_name="resetUploadFileSuffix")
    def reset_upload_file_suffix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUploadFileSuffix", []))

    @builtins.property
    @jsii.member(jsii_name="frequency")
    def frequency(self) -> DatastreamDeliveryConfigurationFrequencyOutputReference:
        return typing.cast(DatastreamDeliveryConfigurationFrequencyOutputReference, jsii.get(self, "frequency"))

    @builtins.property
    @jsii.member(jsii_name="fieldDelimiterInput")
    def field_delimiter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fieldDelimiterInput"))

    @builtins.property
    @jsii.member(jsii_name="formatInput")
    def format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "formatInput"))

    @builtins.property
    @jsii.member(jsii_name="frequencyInput")
    def frequency_input(
        self,
    ) -> typing.Optional[DatastreamDeliveryConfigurationFrequency]:
        return typing.cast(typing.Optional[DatastreamDeliveryConfigurationFrequency], jsii.get(self, "frequencyInput"))

    @builtins.property
    @jsii.member(jsii_name="uploadFilePrefixInput")
    def upload_file_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uploadFilePrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="uploadFileSuffixInput")
    def upload_file_suffix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uploadFileSuffixInput"))

    @builtins.property
    @jsii.member(jsii_name="fieldDelimiter")
    def field_delimiter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fieldDelimiter"))

    @field_delimiter.setter
    def field_delimiter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a308081c0afdc71dea95c0f6812aab2b8de61e5a73a1f5e8834439cf3e0d64a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fieldDelimiter", value)

    @builtins.property
    @jsii.member(jsii_name="format")
    def format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "format"))

    @format.setter
    def format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b322b64d9243e0422b601b927780aeb3d2a7f6f97a29712e2718bacc3bb51409)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "format", value)

    @builtins.property
    @jsii.member(jsii_name="uploadFilePrefix")
    def upload_file_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uploadFilePrefix"))

    @upload_file_prefix.setter
    def upload_file_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94eea5a0697533178d5151d0a1445cd2e8185808bd5eb528a23f256497e06e7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uploadFilePrefix", value)

    @builtins.property
    @jsii.member(jsii_name="uploadFileSuffix")
    def upload_file_suffix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uploadFileSuffix"))

    @upload_file_suffix.setter
    def upload_file_suffix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbc2f8b34db19219cebfee3a82921b08d44b9b1b5adc394be99d33729f95fa5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uploadFileSuffix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DatastreamDeliveryConfiguration]:
        return typing.cast(typing.Optional[DatastreamDeliveryConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatastreamDeliveryConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82638e8ae6729308c71449e5ebcf171aa4208b0a9fe210d97c4bffad8e2d33c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.datastream.DatastreamElasticsearchConnector",
    jsii_struct_bases=[],
    name_mapping={
        "display_name": "displayName",
        "endpoint": "endpoint",
        "index_name": "indexName",
        "password": "password",
        "user_name": "userName",
        "ca_cert": "caCert",
        "client_cert": "clientCert",
        "client_key": "clientKey",
        "content_type": "contentType",
        "custom_header_name": "customHeaderName",
        "custom_header_value": "customHeaderValue",
        "tls_hostname": "tlsHostname",
    },
)
class DatastreamElasticsearchConnector:
    def __init__(
        self,
        *,
        display_name: builtins.str,
        endpoint: builtins.str,
        index_name: builtins.str,
        password: builtins.str,
        user_name: builtins.str,
        ca_cert: typing.Optional[builtins.str] = None,
        client_cert: typing.Optional[builtins.str] = None,
        client_key: typing.Optional[builtins.str] = None,
        content_type: typing.Optional[builtins.str] = None,
        custom_header_name: typing.Optional[builtins.str] = None,
        custom_header_value: typing.Optional[builtins.str] = None,
        tls_hostname: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param display_name: The name of the connector. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#display_name Datastream#display_name}
        :param endpoint: The Elasticsearch bulk endpoint URL in the https://hostname.elastic-cloud.com:9243/_bulk/ format. Set indexName in the appropriate field instead of providing it in the URL. You can use Akamaized property hostnames as endpoint URLs. See Stream logs to Elasticsearch. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#endpoint Datastream#endpoint}
        :param index_name: The index name of the Elastic cloud where you want to store log files. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#index_name Datastream#index_name}
        :param password: The Elasticsearch basic access authentication password. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#password Datastream#password}
        :param user_name: The Elasticsearch basic access authentication username. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#user_name Datastream#user_name}
        :param ca_cert: The certification authority (CA) certificate used to verify the origin server's certificate. If the certificate is not signed by a well-known certification authority, enter the CA certificate in the PEM format for verification. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#ca_cert Datastream#ca_cert}
        :param client_cert: The PEM-formatted digital certificate you want to authenticate requests to your destination with. If you want to use mutual authentication, you need to provide both the client certificate and the client key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#client_cert Datastream#client_cert}
        :param client_key: The private key in the non-encrypted PKCS8 format you want to use to authenticate with the backend server. If you want to use mutual authentication, you need to provide both the client certificate and the client key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#client_key Datastream#client_key}
        :param content_type: The type of the resource passed in the request's custom header. For details, see Additional options in the DataStream user guide. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#content_type Datastream#content_type}
        :param custom_header_name: A human-readable name for the request's custom header, containing only alphanumeric, dash, and underscore characters. For details, see Additional options in the DataStream user guide. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#custom_header_name Datastream#custom_header_name}
        :param custom_header_value: The custom header's contents passed with the request that contains information about the client connection. For details, see Additional options in the DataStream user guide. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#custom_header_value Datastream#custom_header_value}
        :param tls_hostname: The hostname that verifies the server's certificate and matches the Subject Alternative Names (SANs) in the certificate. If not provided, DataStream fetches the hostname from the endpoint URL. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#tls_hostname Datastream#tls_hostname}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85f4a0fcf294f89cef2ca5731138b32a9a827be58e0de3d9ae9879ea78a65249)
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument index_name", value=index_name, expected_type=type_hints["index_name"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument user_name", value=user_name, expected_type=type_hints["user_name"])
            check_type(argname="argument ca_cert", value=ca_cert, expected_type=type_hints["ca_cert"])
            check_type(argname="argument client_cert", value=client_cert, expected_type=type_hints["client_cert"])
            check_type(argname="argument client_key", value=client_key, expected_type=type_hints["client_key"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument custom_header_name", value=custom_header_name, expected_type=type_hints["custom_header_name"])
            check_type(argname="argument custom_header_value", value=custom_header_value, expected_type=type_hints["custom_header_value"])
            check_type(argname="argument tls_hostname", value=tls_hostname, expected_type=type_hints["tls_hostname"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "display_name": display_name,
            "endpoint": endpoint,
            "index_name": index_name,
            "password": password,
            "user_name": user_name,
        }
        if ca_cert is not None:
            self._values["ca_cert"] = ca_cert
        if client_cert is not None:
            self._values["client_cert"] = client_cert
        if client_key is not None:
            self._values["client_key"] = client_key
        if content_type is not None:
            self._values["content_type"] = content_type
        if custom_header_name is not None:
            self._values["custom_header_name"] = custom_header_name
        if custom_header_value is not None:
            self._values["custom_header_value"] = custom_header_value
        if tls_hostname is not None:
            self._values["tls_hostname"] = tls_hostname

    @builtins.property
    def display_name(self) -> builtins.str:
        '''The name of the connector.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#display_name Datastream#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def endpoint(self) -> builtins.str:
        '''The Elasticsearch bulk endpoint URL in the https://hostname.elastic-cloud.com:9243/_bulk/ format. Set indexName in the appropriate field instead of providing it in the URL. You can use Akamaized property hostnames as endpoint URLs. See Stream logs to Elasticsearch.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#endpoint Datastream#endpoint}
        '''
        result = self._values.get("endpoint")
        assert result is not None, "Required property 'endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def index_name(self) -> builtins.str:
        '''The index name of the Elastic cloud where you want to store log files.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#index_name Datastream#index_name}
        '''
        result = self._values.get("index_name")
        assert result is not None, "Required property 'index_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> builtins.str:
        '''The Elasticsearch basic access authentication password.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#password Datastream#password}
        '''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_name(self) -> builtins.str:
        '''The Elasticsearch basic access authentication username.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#user_name Datastream#user_name}
        '''
        result = self._values.get("user_name")
        assert result is not None, "Required property 'user_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ca_cert(self) -> typing.Optional[builtins.str]:
        '''The certification authority (CA) certificate used to verify the origin server's certificate.

        If the certificate is not signed by a well-known certification authority, enter the CA certificate in the PEM format for verification.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#ca_cert Datastream#ca_cert}
        '''
        result = self._values.get("ca_cert")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_cert(self) -> typing.Optional[builtins.str]:
        '''The PEM-formatted digital certificate you want to authenticate requests to your destination with.

        If you want to use mutual authentication, you need to provide both the client certificate and the client key.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#client_cert Datastream#client_cert}
        '''
        result = self._values.get("client_cert")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_key(self) -> typing.Optional[builtins.str]:
        '''The private key in the non-encrypted PKCS8 format you want to use to authenticate with the backend server.

        If you want to use mutual authentication, you need to provide both the client certificate and the client key.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#client_key Datastream#client_key}
        '''
        result = self._values.get("client_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_type(self) -> typing.Optional[builtins.str]:
        '''The type of the resource passed in the request's custom header.

        For details, see Additional options in the DataStream user guide.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#content_type Datastream#content_type}
        '''
        result = self._values.get("content_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_header_name(self) -> typing.Optional[builtins.str]:
        '''A human-readable name for the request's custom header, containing only alphanumeric, dash, and underscore characters.

        For details, see Additional options in the DataStream user guide.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#custom_header_name Datastream#custom_header_name}
        '''
        result = self._values.get("custom_header_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_header_value(self) -> typing.Optional[builtins.str]:
        '''The custom header's contents passed with the request that contains information about the client connection.

        For details, see Additional options in the DataStream user guide.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#custom_header_value Datastream#custom_header_value}
        '''
        result = self._values.get("custom_header_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls_hostname(self) -> typing.Optional[builtins.str]:
        '''The hostname that verifies the server's certificate and matches the Subject Alternative Names (SANs) in the certificate.

        If not provided, DataStream fetches the hostname from the endpoint URL.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#tls_hostname Datastream#tls_hostname}
        '''
        result = self._values.get("tls_hostname")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamElasticsearchConnector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatastreamElasticsearchConnectorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.datastream.DatastreamElasticsearchConnectorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bd8f250f949b8e12ec18bcff419c1c3b4ab8651b92d94bc524d94644d7c35776)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCaCert")
    def reset_ca_cert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaCert", []))

    @jsii.member(jsii_name="resetClientCert")
    def reset_client_cert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCert", []))

    @jsii.member(jsii_name="resetClientKey")
    def reset_client_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientKey", []))

    @jsii.member(jsii_name="resetContentType")
    def reset_content_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentType", []))

    @jsii.member(jsii_name="resetCustomHeaderName")
    def reset_custom_header_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomHeaderName", []))

    @jsii.member(jsii_name="resetCustomHeaderValue")
    def reset_custom_header_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomHeaderValue", []))

    @jsii.member(jsii_name="resetTlsHostname")
    def reset_tls_hostname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsHostname", []))

    @builtins.property
    @jsii.member(jsii_name="mTls")
    def m_tls(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "mTls"))

    @builtins.property
    @jsii.member(jsii_name="caCertInput")
    def ca_cert_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caCertInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCertInput")
    def client_cert_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertInput"))

    @builtins.property
    @jsii.member(jsii_name="clientKeyInput")
    def client_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="customHeaderNameInput")
    def custom_header_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customHeaderNameInput"))

    @builtins.property
    @jsii.member(jsii_name="customHeaderValueInput")
    def custom_header_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customHeaderValueInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="indexNameInput")
    def index_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "indexNameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsHostnameInput")
    def tls_hostname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsHostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="userNameInput")
    def user_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userNameInput"))

    @builtins.property
    @jsii.member(jsii_name="caCert")
    def ca_cert(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "caCert"))

    @ca_cert.setter
    def ca_cert(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbcabc16742e8c109c31c26839165d5e12c7974e8c8009a1a0bf638cbb28eb15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caCert", value)

    @builtins.property
    @jsii.member(jsii_name="clientCert")
    def client_cert(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientCert"))

    @client_cert.setter
    def client_cert(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e830aa9e75a4f43ca823bd82943099670f04acdffdb86c985e048b9fc22e6d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCert", value)

    @builtins.property
    @jsii.member(jsii_name="clientKey")
    def client_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientKey"))

    @client_key.setter
    def client_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a363af39834923508a1b3dac25971d77df85d8064c143910b72831165a5da542)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientKey", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b19bbb70f52b8fb3bedf1abe09e57d42979655abc5828f049f23538742d041a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="customHeaderName")
    def custom_header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customHeaderName"))

    @custom_header_name.setter
    def custom_header_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e21ba10b74e1b1a267cc1bd012b647085ec1a3de3a477b14968ce06b6a0a4b76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customHeaderName", value)

    @builtins.property
    @jsii.member(jsii_name="customHeaderValue")
    def custom_header_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customHeaderValue"))

    @custom_header_value.setter
    def custom_header_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38eab0523cb3cdb7d41845fe1c3af353d10236a01e0bf410b8477e4d07e4f00e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customHeaderValue", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f24559d7ded97f0e22f36f24e7910d14fdfa73e71b068eee6252a94f34586789)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ef7380369a95ad3a50e72d0a6632e7fb6a0056735fd3a0eb040cc8535663dd9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="indexName")
    def index_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "indexName"))

    @index_name.setter
    def index_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65b3b2fe6656993af1afe356af593b4d0faf0bec7372bfb4999fed4f2c0e10c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "indexName", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9f959e812215096d7dbac6afa890665990bbcad74d7cd9c906a519392e8fee5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="tlsHostname")
    def tls_hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsHostname"))

    @tls_hostname.setter
    def tls_hostname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b58ae26f58080939afcf1b2a783ff9150ad14e8ebdcea518909519c08da1c8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsHostname", value)

    @builtins.property
    @jsii.member(jsii_name="userName")
    def user_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userName"))

    @user_name.setter
    def user_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87afae4b1c3213550b0a409d84396174087106b2f6824bc80cf04047669fcc7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DatastreamElasticsearchConnector]:
        return typing.cast(typing.Optional[DatastreamElasticsearchConnector], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatastreamElasticsearchConnector],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e79fe20ddca88361c0e2cb0c765f4b8a170bb3039cddf1fd44a9f6fbadc16e0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.datastream.DatastreamGcsConnector",
    jsii_struct_bases=[],
    name_mapping={
        "bucket": "bucket",
        "display_name": "displayName",
        "private_key": "privateKey",
        "project_id": "projectId",
        "service_account_name": "serviceAccountName",
        "path": "path",
    },
)
class DatastreamGcsConnector:
    def __init__(
        self,
        *,
        bucket: builtins.str,
        display_name: builtins.str,
        private_key: builtins.str,
        project_id: builtins.str,
        service_account_name: builtins.str,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: The name of the storage bucket created in Google Cloud account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#bucket Datastream#bucket}
        :param display_name: The name of the connector. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#display_name Datastream#display_name}
        :param private_key: The contents of the JSON private key generated and downloaded in Google Cloud Storage account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#private_key Datastream#private_key}
        :param project_id: The unique ID of Google Cloud project. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#project_id Datastream#project_id}
        :param service_account_name: The name of the service account with the storage.object.create permission or Storage Object Creator role. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#service_account_name Datastream#service_account_name}
        :param path: The path to the folder within Google Cloud bucket where logs will be stored. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#path Datastream#path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba8d43bd5f33e84923afa821070d9a4a451fd5ba10e13bcd230c589d61d25049)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument private_key", value=private_key, expected_type=type_hints["private_key"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument service_account_name", value=service_account_name, expected_type=type_hints["service_account_name"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket": bucket,
            "display_name": display_name,
            "private_key": private_key,
            "project_id": project_id,
            "service_account_name": service_account_name,
        }
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def bucket(self) -> builtins.str:
        '''The name of the storage bucket created in Google Cloud account.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#bucket Datastream#bucket}
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def display_name(self) -> builtins.str:
        '''The name of the connector.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#display_name Datastream#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def private_key(self) -> builtins.str:
        '''The contents of the JSON private key generated and downloaded in Google Cloud Storage account.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#private_key Datastream#private_key}
        '''
        result = self._values.get("private_key")
        assert result is not None, "Required property 'private_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''The unique ID of Google Cloud project.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#project_id Datastream#project_id}
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_account_name(self) -> builtins.str:
        '''The name of the service account with the storage.object.create permission or Storage Object Creator role.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#service_account_name Datastream#service_account_name}
        '''
        result = self._values.get("service_account_name")
        assert result is not None, "Required property 'service_account_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''The path to the folder within Google Cloud bucket where logs will be stored.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#path Datastream#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamGcsConnector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatastreamGcsConnectorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.datastream.DatastreamGcsConnectorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2eb01841cefd140c2d7088c4723d02bf8dfee7f35d2ae8be08161b251b614f81)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @builtins.property
    @jsii.member(jsii_name="compressLogs")
    def compress_logs(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "compressLogs"))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="privateKeyInput")
    def private_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountNameInput")
    def service_account_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccountNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4bb97846cdf137be6c3d8239e86ead2e0383a64d5b9025f6ce83c83188b0526)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5069ed7f0ed42d32181d81029551215afa80c5db65f054911f08976500b084e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eacbae59b6da9a1214932814360e2cccfa26695945e7c3d1de9288e2abfef413)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="privateKey")
    def private_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateKey"))

    @private_key.setter
    def private_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e0b701ba66dbac061e772920d9aa0e94538613d9df251d556abc5b7b16ebdae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKey", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01bd8da70d1627102ca35af2baa8cd5249d79834c7dac5e9c5216c161e2baf3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccountName")
    def service_account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccountName"))

    @service_account_name.setter
    def service_account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a6fe03d0aa97d333443f009c25228a85d651369e371804274ef62d9eacccf6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccountName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DatastreamGcsConnector]:
        return typing.cast(typing.Optional[DatastreamGcsConnector], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DatastreamGcsConnector]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73415bb77aae34c3bfea9b7b063da1b4c209df805a08392d4aa3c94015e14491)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.datastream.DatastreamHttpsConnector",
    jsii_struct_bases=[],
    name_mapping={
        "authentication_type": "authenticationType",
        "display_name": "displayName",
        "endpoint": "endpoint",
        "ca_cert": "caCert",
        "client_cert": "clientCert",
        "client_key": "clientKey",
        "compress_logs": "compressLogs",
        "content_type": "contentType",
        "custom_header_name": "customHeaderName",
        "custom_header_value": "customHeaderValue",
        "password": "password",
        "tls_hostname": "tlsHostname",
        "user_name": "userName",
    },
)
class DatastreamHttpsConnector:
    def __init__(
        self,
        *,
        authentication_type: builtins.str,
        display_name: builtins.str,
        endpoint: builtins.str,
        ca_cert: typing.Optional[builtins.str] = None,
        client_cert: typing.Optional[builtins.str] = None,
        client_key: typing.Optional[builtins.str] = None,
        compress_logs: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        content_type: typing.Optional[builtins.str] = None,
        custom_header_name: typing.Optional[builtins.str] = None,
        custom_header_value: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        tls_hostname: typing.Optional[builtins.str] = None,
        user_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param authentication_type: Either NONE for no authentication, or BASIC for username and password authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#authentication_type Datastream#authentication_type}
        :param display_name: The name of the connector. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#display_name Datastream#display_name}
        :param endpoint: URL where logs will be stored. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#endpoint Datastream#endpoint}
        :param ca_cert: The certification authority (CA) certificate used to verify the origin server's certificate. If the certificate is not signed by a well-known certification authority, enter the CA certificate in the PEM format for verification. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#ca_cert Datastream#ca_cert}
        :param client_cert: The digital certificate in the PEM format you want to use to authenticate requests to your destination. If you want to use mutual authentication, you need to provide both the client certificate and the client key (in the PEM format). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#client_cert Datastream#client_cert}
        :param client_key: The private key in the non-encrypted PKCS8 format you want to use to authenticate with the back-end server. If you want to use mutual authentication, you need to provide both the client certificate and the client key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#client_key Datastream#client_key}
        :param compress_logs: Indicates whether the logs should be compressed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#compress_logs Datastream#compress_logs}
        :param content_type: Content type to pass in the log file header. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#content_type Datastream#content_type}
        :param custom_header_name: The name of custom header passed with the request to the destination. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#custom_header_name Datastream#custom_header_name}
        :param custom_header_value: The custom header's contents passed with the request to the destination. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#custom_header_value Datastream#custom_header_value}
        :param password: Password set for custom HTTPS endpoint for authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#password Datastream#password}
        :param tls_hostname: The hostname that verifies the server's certificate and matches the Subject Alternative Names (SANs) in the certificate. If not provided, DataStream fetches the hostname from the endpoint URL. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#tls_hostname Datastream#tls_hostname}
        :param user_name: Username used for authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#user_name Datastream#user_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7723146f16e3835acd53d0a64206159f70c32e4fe17c82ddd721ddda468907cd)
            check_type(argname="argument authentication_type", value=authentication_type, expected_type=type_hints["authentication_type"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument ca_cert", value=ca_cert, expected_type=type_hints["ca_cert"])
            check_type(argname="argument client_cert", value=client_cert, expected_type=type_hints["client_cert"])
            check_type(argname="argument client_key", value=client_key, expected_type=type_hints["client_key"])
            check_type(argname="argument compress_logs", value=compress_logs, expected_type=type_hints["compress_logs"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument custom_header_name", value=custom_header_name, expected_type=type_hints["custom_header_name"])
            check_type(argname="argument custom_header_value", value=custom_header_value, expected_type=type_hints["custom_header_value"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument tls_hostname", value=tls_hostname, expected_type=type_hints["tls_hostname"])
            check_type(argname="argument user_name", value=user_name, expected_type=type_hints["user_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "authentication_type": authentication_type,
            "display_name": display_name,
            "endpoint": endpoint,
        }
        if ca_cert is not None:
            self._values["ca_cert"] = ca_cert
        if client_cert is not None:
            self._values["client_cert"] = client_cert
        if client_key is not None:
            self._values["client_key"] = client_key
        if compress_logs is not None:
            self._values["compress_logs"] = compress_logs
        if content_type is not None:
            self._values["content_type"] = content_type
        if custom_header_name is not None:
            self._values["custom_header_name"] = custom_header_name
        if custom_header_value is not None:
            self._values["custom_header_value"] = custom_header_value
        if password is not None:
            self._values["password"] = password
        if tls_hostname is not None:
            self._values["tls_hostname"] = tls_hostname
        if user_name is not None:
            self._values["user_name"] = user_name

    @builtins.property
    def authentication_type(self) -> builtins.str:
        '''Either NONE for no authentication, or BASIC for username and password authentication.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#authentication_type Datastream#authentication_type}
        '''
        result = self._values.get("authentication_type")
        assert result is not None, "Required property 'authentication_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def display_name(self) -> builtins.str:
        '''The name of the connector.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#display_name Datastream#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def endpoint(self) -> builtins.str:
        '''URL where logs will be stored.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#endpoint Datastream#endpoint}
        '''
        result = self._values.get("endpoint")
        assert result is not None, "Required property 'endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ca_cert(self) -> typing.Optional[builtins.str]:
        '''The certification authority (CA) certificate used to verify the origin server's certificate.

        If the certificate is not signed by a well-known certification authority, enter the CA certificate in the PEM format for verification.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#ca_cert Datastream#ca_cert}
        '''
        result = self._values.get("ca_cert")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_cert(self) -> typing.Optional[builtins.str]:
        '''The digital certificate in the PEM format you want to use to authenticate requests to your destination.

        If you want to use mutual authentication, you need to provide both the client certificate and the client key (in the PEM format).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#client_cert Datastream#client_cert}
        '''
        result = self._values.get("client_cert")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_key(self) -> typing.Optional[builtins.str]:
        '''The private key in the non-encrypted PKCS8 format you want to use to authenticate with the back-end server.

        If you want to use mutual authentication, you need to provide both the client certificate and the client key.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#client_key Datastream#client_key}
        '''
        result = self._values.get("client_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def compress_logs(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Indicates whether the logs should be compressed.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#compress_logs Datastream#compress_logs}
        '''
        result = self._values.get("compress_logs")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def content_type(self) -> typing.Optional[builtins.str]:
        '''Content type to pass in the log file header.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#content_type Datastream#content_type}
        '''
        result = self._values.get("content_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_header_name(self) -> typing.Optional[builtins.str]:
        '''The name of custom header passed with the request to the destination.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#custom_header_name Datastream#custom_header_name}
        '''
        result = self._values.get("custom_header_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_header_value(self) -> typing.Optional[builtins.str]:
        '''The custom header's contents passed with the request to the destination.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#custom_header_value Datastream#custom_header_value}
        '''
        result = self._values.get("custom_header_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Password set for custom HTTPS endpoint for authentication.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#password Datastream#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls_hostname(self) -> typing.Optional[builtins.str]:
        '''The hostname that verifies the server's certificate and matches the Subject Alternative Names (SANs) in the certificate.

        If not provided, DataStream fetches the hostname from the endpoint URL.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#tls_hostname Datastream#tls_hostname}
        '''
        result = self._values.get("tls_hostname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_name(self) -> typing.Optional[builtins.str]:
        '''Username used for authentication.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#user_name Datastream#user_name}
        '''
        result = self._values.get("user_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamHttpsConnector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatastreamHttpsConnectorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.datastream.DatastreamHttpsConnectorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0b6ce20caf3f80a114a60fc517cf753fbba9990a5874ceb2434cf888133f3d20)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCaCert")
    def reset_ca_cert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaCert", []))

    @jsii.member(jsii_name="resetClientCert")
    def reset_client_cert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCert", []))

    @jsii.member(jsii_name="resetClientKey")
    def reset_client_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientKey", []))

    @jsii.member(jsii_name="resetCompressLogs")
    def reset_compress_logs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompressLogs", []))

    @jsii.member(jsii_name="resetContentType")
    def reset_content_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentType", []))

    @jsii.member(jsii_name="resetCustomHeaderName")
    def reset_custom_header_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomHeaderName", []))

    @jsii.member(jsii_name="resetCustomHeaderValue")
    def reset_custom_header_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomHeaderValue", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetTlsHostname")
    def reset_tls_hostname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsHostname", []))

    @jsii.member(jsii_name="resetUserName")
    def reset_user_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserName", []))

    @builtins.property
    @jsii.member(jsii_name="mTls")
    def m_tls(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "mTls"))

    @builtins.property
    @jsii.member(jsii_name="authenticationTypeInput")
    def authentication_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authenticationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="caCertInput")
    def ca_cert_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caCertInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCertInput")
    def client_cert_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertInput"))

    @builtins.property
    @jsii.member(jsii_name="clientKeyInput")
    def client_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="compressLogsInput")
    def compress_logs_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "compressLogsInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="customHeaderNameInput")
    def custom_header_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customHeaderNameInput"))

    @builtins.property
    @jsii.member(jsii_name="customHeaderValueInput")
    def custom_header_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customHeaderValueInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsHostnameInput")
    def tls_hostname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsHostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="userNameInput")
    def user_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userNameInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticationType")
    def authentication_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authenticationType"))

    @authentication_type.setter
    def authentication_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4264c448b60000908e010f1a93780bac81dcfe80c6b3da7ba770a043139482c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationType", value)

    @builtins.property
    @jsii.member(jsii_name="caCert")
    def ca_cert(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "caCert"))

    @ca_cert.setter
    def ca_cert(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__367e1e696834a9562ac5de80a6ce7213ad9dc2eade4d30d9bcfa8b8fd2e0a4e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caCert", value)

    @builtins.property
    @jsii.member(jsii_name="clientCert")
    def client_cert(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientCert"))

    @client_cert.setter
    def client_cert(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a443f29d8f1c4a8a6171319ce2c8542c326e0cf6f81e5f5ee28138d29c590be3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCert", value)

    @builtins.property
    @jsii.member(jsii_name="clientKey")
    def client_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientKey"))

    @client_key.setter
    def client_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c20e5673a76dbcd109293e3e2fb252ed2726ee8a3dd50165c256d275ef32871b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientKey", value)

    @builtins.property
    @jsii.member(jsii_name="compressLogs")
    def compress_logs(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "compressLogs"))

    @compress_logs.setter
    def compress_logs(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9db187e1bcf44dfa3360bede57a2503d5cb52610ce1853d215034dac5179a713)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compressLogs", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91a0ba4803f1ffed0f4282c419953c0e9464853d70acf456ecc92ba8bfa055f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="customHeaderName")
    def custom_header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customHeaderName"))

    @custom_header_name.setter
    def custom_header_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdff7a559052ab6cfe0501edd97f2d5aa4385631063f06524d5c37d5bdb52649)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customHeaderName", value)

    @builtins.property
    @jsii.member(jsii_name="customHeaderValue")
    def custom_header_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customHeaderValue"))

    @custom_header_value.setter
    def custom_header_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96c6a37560eca6a07d843f5a1a4b87707fec48553d615e1666027d55df7a096a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customHeaderValue", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4db628fde15b9df35e44a3dcbc2638539fa989463aadf915dfecc48f9b8c20b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd3824b827a424dd1b5ff9fb7cae0f482be4f567df789fcb1d367d986d0a6016)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b2d38dc1381200144e46985f9ef75184c24f90eac6f47728389f2d6eeed6361)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="tlsHostname")
    def tls_hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsHostname"))

    @tls_hostname.setter
    def tls_hostname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d97665069e71c1647846504017dab5eca12ad7d542a9268570a35cff780380f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsHostname", value)

    @builtins.property
    @jsii.member(jsii_name="userName")
    def user_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userName"))

    @user_name.setter
    def user_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__966d6a042b31821aa1fd539c863552a7f3b8317e1b671344d509f23aa885a7f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DatastreamHttpsConnector]:
        return typing.cast(typing.Optional[DatastreamHttpsConnector], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DatastreamHttpsConnector]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba99880f6d2cdd26079c7be46e00103f95b9a172ac73484ab3c544ff0316fcef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.datastream.DatastreamLogglyConnector",
    jsii_struct_bases=[],
    name_mapping={
        "auth_token": "authToken",
        "display_name": "displayName",
        "endpoint": "endpoint",
        "content_type": "contentType",
        "custom_header_name": "customHeaderName",
        "custom_header_value": "customHeaderValue",
        "tags": "tags",
    },
)
class DatastreamLogglyConnector:
    def __init__(
        self,
        *,
        auth_token: builtins.str,
        display_name: builtins.str,
        endpoint: builtins.str,
        content_type: typing.Optional[builtins.str] = None,
        custom_header_name: typing.Optional[builtins.str] = None,
        custom_header_value: typing.Optional[builtins.str] = None,
        tags: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_token: The unique HTTP code for your Loggly bulk endpoint. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#auth_token Datastream#auth_token}
        :param display_name: The name of the connector. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#display_name Datastream#display_name}
        :param endpoint: The Loggly bulk endpoint URL in the https://hostname.loggly.com/bulk/ format. Set the endpoint code in the authToken field instead of providing it in the URL. You can use Akamaized property hostnames as endpoint URLs. See Stream logs to Loggly. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#endpoint Datastream#endpoint}
        :param content_type: The type of the resource passed in the request's custom header. For details, see Additional options in the DataStream user guide. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#content_type Datastream#content_type}
        :param custom_header_name: A human-readable name for the request's custom header, containing only alphanumeric, dash, and underscore characters. For details, see Additional options in the DataStream user guide. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#custom_header_name Datastream#custom_header_name}
        :param custom_header_value: The custom header's contents passed with the request that contains information about the client connection. For details, see Additional options in the DataStream user guide. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#custom_header_value Datastream#custom_header_value}
        :param tags: The tags you can use to segment and filter log events in Loggly. See Tags in the Loggly documentation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#tags Datastream#tags}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e3146f5e5a213c58ca02bc717ea886728de32fc5fff99af91f7e09cbfeeb06d)
            check_type(argname="argument auth_token", value=auth_token, expected_type=type_hints["auth_token"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument custom_header_name", value=custom_header_name, expected_type=type_hints["custom_header_name"])
            check_type(argname="argument custom_header_value", value=custom_header_value, expected_type=type_hints["custom_header_value"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "auth_token": auth_token,
            "display_name": display_name,
            "endpoint": endpoint,
        }
        if content_type is not None:
            self._values["content_type"] = content_type
        if custom_header_name is not None:
            self._values["custom_header_name"] = custom_header_name
        if custom_header_value is not None:
            self._values["custom_header_value"] = custom_header_value
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def auth_token(self) -> builtins.str:
        '''The unique HTTP code for your Loggly bulk endpoint.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#auth_token Datastream#auth_token}
        '''
        result = self._values.get("auth_token")
        assert result is not None, "Required property 'auth_token' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def display_name(self) -> builtins.str:
        '''The name of the connector.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#display_name Datastream#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def endpoint(self) -> builtins.str:
        '''The Loggly bulk endpoint URL in the https://hostname.loggly.com/bulk/ format. Set the endpoint code in the authToken field instead of providing it in the URL. You can use Akamaized property hostnames as endpoint URLs. See Stream logs to Loggly.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#endpoint Datastream#endpoint}
        '''
        result = self._values.get("endpoint")
        assert result is not None, "Required property 'endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_type(self) -> typing.Optional[builtins.str]:
        '''The type of the resource passed in the request's custom header.

        For details, see Additional options in the DataStream user guide.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#content_type Datastream#content_type}
        '''
        result = self._values.get("content_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_header_name(self) -> typing.Optional[builtins.str]:
        '''A human-readable name for the request's custom header, containing only alphanumeric, dash, and underscore characters.

        For details, see Additional options in the DataStream user guide.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#custom_header_name Datastream#custom_header_name}
        '''
        result = self._values.get("custom_header_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_header_value(self) -> typing.Optional[builtins.str]:
        '''The custom header's contents passed with the request that contains information about the client connection.

        For details, see Additional options in the DataStream user guide.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#custom_header_value Datastream#custom_header_value}
        '''
        result = self._values.get("custom_header_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[builtins.str]:
        '''The tags you can use to segment and filter log events in Loggly. See Tags in the Loggly documentation.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#tags Datastream#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamLogglyConnector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatastreamLogglyConnectorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.datastream.DatastreamLogglyConnectorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d6d05f1908e74f8ddf990137e9dfd01e7e7e78a36bb235daed83f024b35c521c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetContentType")
    def reset_content_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentType", []))

    @jsii.member(jsii_name="resetCustomHeaderName")
    def reset_custom_header_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomHeaderName", []))

    @jsii.member(jsii_name="resetCustomHeaderValue")
    def reset_custom_header_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomHeaderValue", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @builtins.property
    @jsii.member(jsii_name="authTokenInput")
    def auth_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="customHeaderNameInput")
    def custom_header_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customHeaderNameInput"))

    @builtins.property
    @jsii.member(jsii_name="customHeaderValueInput")
    def custom_header_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customHeaderValueInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="authToken")
    def auth_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authToken"))

    @auth_token.setter
    def auth_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a4ec9a1152edb665966aa00b4ec3401b5f371eb67b59d8db084439fe9043f2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authToken", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39620e73f54e3379ccf17774f42eb64779ca72f3ce7bab5a1f7b3361b51dab1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="customHeaderName")
    def custom_header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customHeaderName"))

    @custom_header_name.setter
    def custom_header_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa2be8e7349786a90cbbb7910a01bec25fd1ef416328d7ce275c7e295affb96f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customHeaderName", value)

    @builtins.property
    @jsii.member(jsii_name="customHeaderValue")
    def custom_header_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customHeaderValue"))

    @custom_header_value.setter
    def custom_header_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68c62f54a23de7d02531046c346b93b99fc943d16285256b9295b5fb2a6343c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customHeaderValue", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4386cd06a2c2d8e70b4229a9284e778d838edbf66d78f6e401b3f10a4755737c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fbffc1fa7e0a064cfd57cc312f12559141a43714159b31c9db052856c5be923)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ee9a6b190d9f66286d49acde1e8420e8e594ce47c3dae07bcb8d9b94a4d0db5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DatastreamLogglyConnector]:
        return typing.cast(typing.Optional[DatastreamLogglyConnector], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DatastreamLogglyConnector]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c4fbd78a5e5fed5fdc0c416de2818e3034d1c42734d551aaf01606d79b49094)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.datastream.DatastreamNewRelicConnector",
    jsii_struct_bases=[],
    name_mapping={
        "auth_token": "authToken",
        "display_name": "displayName",
        "endpoint": "endpoint",
        "content_type": "contentType",
        "custom_header_name": "customHeaderName",
        "custom_header_value": "customHeaderValue",
    },
)
class DatastreamNewRelicConnector:
    def __init__(
        self,
        *,
        auth_token: builtins.str,
        display_name: builtins.str,
        endpoint: builtins.str,
        content_type: typing.Optional[builtins.str] = None,
        custom_header_name: typing.Optional[builtins.str] = None,
        custom_header_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_token: Your Log API token for your account in New Relic. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#auth_token Datastream#auth_token}
        :param display_name: The name of the connector. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#display_name Datastream#display_name}
        :param endpoint: A New Relic endpoint URL you want to send your logs to. The endpoint URL should follow the https://<newrelic.com>/log/v1/ format format. See Introduction to the Log API https://docs.newrelic.com/docs/logs/log-api/introduction-log-api/ if you want to retrieve your New Relic endpoint URL. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#endpoint Datastream#endpoint}
        :param content_type: The type of the resource passed in the request's custom header. For details, see Additional options in the DataStream user guide. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#content_type Datastream#content_type}
        :param custom_header_name: A human-readable name for the request's custom header, containing only alphanumeric, dash, and underscore characters. For details, see Additional options in the DataStream user guide. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#custom_header_name Datastream#custom_header_name}
        :param custom_header_value: The custom header's contents passed with the request that contains information about the client connection. For details, see Additional options in the DataStream user guide. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#custom_header_value Datastream#custom_header_value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bb21c52f3b3e2c493dd88b2ca8d98dbd2b9f996ae5811fa9ad8b3bfa58945a3)
            check_type(argname="argument auth_token", value=auth_token, expected_type=type_hints["auth_token"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument custom_header_name", value=custom_header_name, expected_type=type_hints["custom_header_name"])
            check_type(argname="argument custom_header_value", value=custom_header_value, expected_type=type_hints["custom_header_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "auth_token": auth_token,
            "display_name": display_name,
            "endpoint": endpoint,
        }
        if content_type is not None:
            self._values["content_type"] = content_type
        if custom_header_name is not None:
            self._values["custom_header_name"] = custom_header_name
        if custom_header_value is not None:
            self._values["custom_header_value"] = custom_header_value

    @builtins.property
    def auth_token(self) -> builtins.str:
        '''Your Log API token for your account in New Relic.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#auth_token Datastream#auth_token}
        '''
        result = self._values.get("auth_token")
        assert result is not None, "Required property 'auth_token' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def display_name(self) -> builtins.str:
        '''The name of the connector.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#display_name Datastream#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def endpoint(self) -> builtins.str:
        '''A New Relic endpoint URL you want to send your logs to.

        The endpoint URL should follow the https://<newrelic.com>/log/v1/ format format. See Introduction to the Log API https://docs.newrelic.com/docs/logs/log-api/introduction-log-api/ if you want to retrieve your New Relic endpoint URL.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#endpoint Datastream#endpoint}
        '''
        result = self._values.get("endpoint")
        assert result is not None, "Required property 'endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_type(self) -> typing.Optional[builtins.str]:
        '''The type of the resource passed in the request's custom header.

        For details, see Additional options in the DataStream user guide.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#content_type Datastream#content_type}
        '''
        result = self._values.get("content_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_header_name(self) -> typing.Optional[builtins.str]:
        '''A human-readable name for the request's custom header, containing only alphanumeric, dash, and underscore characters.

        For details, see Additional options in the DataStream user guide.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#custom_header_name Datastream#custom_header_name}
        '''
        result = self._values.get("custom_header_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_header_value(self) -> typing.Optional[builtins.str]:
        '''The custom header's contents passed with the request that contains information about the client connection.

        For details, see Additional options in the DataStream user guide.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#custom_header_value Datastream#custom_header_value}
        '''
        result = self._values.get("custom_header_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamNewRelicConnector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatastreamNewRelicConnectorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.datastream.DatastreamNewRelicConnectorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2b505f8cb9d76d2a0470cbea6088a9e47b87299e8002e735fe0a618914e0b507)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetContentType")
    def reset_content_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentType", []))

    @jsii.member(jsii_name="resetCustomHeaderName")
    def reset_custom_header_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomHeaderName", []))

    @jsii.member(jsii_name="resetCustomHeaderValue")
    def reset_custom_header_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomHeaderValue", []))

    @builtins.property
    @jsii.member(jsii_name="authTokenInput")
    def auth_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="customHeaderNameInput")
    def custom_header_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customHeaderNameInput"))

    @builtins.property
    @jsii.member(jsii_name="customHeaderValueInput")
    def custom_header_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customHeaderValueInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="authToken")
    def auth_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authToken"))

    @auth_token.setter
    def auth_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__feb03c92b1978e31c484789ecef69c680686b4f436f890b60a996761f768cad3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authToken", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2edf6768128a246d3b412c33cb0783d7375a3b0ea9e0447229f6cec912af9d1f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="customHeaderName")
    def custom_header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customHeaderName"))

    @custom_header_name.setter
    def custom_header_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a1942fda8ba386b9bcbc2e5d8447308cbdff2609cf36ea417f5e03aabb8f847)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customHeaderName", value)

    @builtins.property
    @jsii.member(jsii_name="customHeaderValue")
    def custom_header_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customHeaderValue"))

    @custom_header_value.setter
    def custom_header_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba7d0a5d72eb715a5a951c35edf75bd68fd336984af36b97231705c578a9c87b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customHeaderValue", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__090a5297501f08d8c237f9ec16898a6eb6eeda985e4df80667011b26b7dc5ffd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3aa281de5622bec38b0a33539cc6b116d6a212c9b7e314cebc3a9a109cb82f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DatastreamNewRelicConnector]:
        return typing.cast(typing.Optional[DatastreamNewRelicConnector], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatastreamNewRelicConnector],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b63667e5244b4aa13aab1c800706f387ce87aecd608d2639de7cf547874262b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.datastream.DatastreamOracleConnector",
    jsii_struct_bases=[],
    name_mapping={
        "access_key": "accessKey",
        "bucket": "bucket",
        "display_name": "displayName",
        "namespace": "namespace",
        "path": "path",
        "region": "region",
        "secret_access_key": "secretAccessKey",
    },
)
class DatastreamOracleConnector:
    def __init__(
        self,
        *,
        access_key: builtins.str,
        bucket: builtins.str,
        display_name: builtins.str,
        namespace: builtins.str,
        path: builtins.str,
        region: builtins.str,
        secret_access_key: builtins.str,
    ) -> None:
        '''
        :param access_key: The access key identifier used to authenticate requests to the Oracle Cloud account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#access_key Datastream#access_key}
        :param bucket: The name of the Oracle Cloud Storage bucket. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#bucket Datastream#bucket}
        :param display_name: The name of the connector. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#display_name Datastream#display_name}
        :param namespace: The namespace of Oracle Cloud Storage account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#namespace Datastream#namespace}
        :param path: The path to the folder within your Oracle Cloud Storage bucket where logs will be stored. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#path Datastream#path}
        :param region: The Oracle Cloud Storage region where bucket resides. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#region Datastream#region}
        :param secret_access_key: The secret access key identifier used to authenticate requests to the Oracle Cloud account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#secret_access_key Datastream#secret_access_key}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0016fb68b6e64ed37ddb7e534f6faaa04d6a768bd38a3dcb3dad3ef7f347249d)
            check_type(argname="argument access_key", value=access_key, expected_type=type_hints["access_key"])
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument secret_access_key", value=secret_access_key, expected_type=type_hints["secret_access_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_key": access_key,
            "bucket": bucket,
            "display_name": display_name,
            "namespace": namespace,
            "path": path,
            "region": region,
            "secret_access_key": secret_access_key,
        }

    @builtins.property
    def access_key(self) -> builtins.str:
        '''The access key identifier used to authenticate requests to the Oracle Cloud account.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#access_key Datastream#access_key}
        '''
        result = self._values.get("access_key")
        assert result is not None, "Required property 'access_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bucket(self) -> builtins.str:
        '''The name of the Oracle Cloud Storage bucket.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#bucket Datastream#bucket}
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def display_name(self) -> builtins.str:
        '''The name of the connector.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#display_name Datastream#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''The namespace of Oracle Cloud Storage account.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#namespace Datastream#namespace}
        '''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''The path to the folder within your Oracle Cloud Storage bucket where logs will be stored.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#path Datastream#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''The Oracle Cloud Storage region where bucket resides.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#region Datastream#region}
        '''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def secret_access_key(self) -> builtins.str:
        '''The secret access key identifier used to authenticate requests to the Oracle Cloud account.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#secret_access_key Datastream#secret_access_key}
        '''
        result = self._values.get("secret_access_key")
        assert result is not None, "Required property 'secret_access_key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamOracleConnector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatastreamOracleConnectorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.datastream.DatastreamOracleConnectorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__acdfc281daf629fc338b963b94e767ca986255ba3099252704719decb0d0d084)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="compressLogs")
    def compress_logs(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "compressLogs"))

    @builtins.property
    @jsii.member(jsii_name="accessKeyInput")
    def access_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="secretAccessKeyInput")
    def secret_access_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretAccessKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="accessKey")
    def access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessKey"))

    @access_key.setter
    def access_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e7cdf2ee160e5b9c770e83f5bd3e5663017b73918c59cb5a4a4b1cf6310d589)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessKey", value)

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b43017242febcc51265c05e86ebc9d5678bd354f03086dff859c5f99822cd07)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1bb4f79be249466bfd15b024b960fc15d6087d4a7e4f8a204edb9d572cb7af3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68eaf8da68e650d34037e1fe9a98e9d96ae62e67d438f38149630b127499e625)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9645c5e96eb2c9f14ea427713320d0e06f5fc128c1c530b92afd6b4b9d2073af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__941217a664670a3eb34dbb57870294a4ccc82007d84315ec324deac80ce179d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="secretAccessKey")
    def secret_access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretAccessKey"))

    @secret_access_key.setter
    def secret_access_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb5facfcf6b0d06dc51ca8a4b93ceca017ed89551b4f60bf7db725c2bc4f3b48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretAccessKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DatastreamOracleConnector]:
        return typing.cast(typing.Optional[DatastreamOracleConnector], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DatastreamOracleConnector]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f388cde6002a55ab2d115701e1b029ed0d606f28314e4c3c1c63592bf1e6996)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.datastream.DatastreamS3Connector",
    jsii_struct_bases=[],
    name_mapping={
        "access_key": "accessKey",
        "bucket": "bucket",
        "display_name": "displayName",
        "path": "path",
        "region": "region",
        "secret_access_key": "secretAccessKey",
    },
)
class DatastreamS3Connector:
    def __init__(
        self,
        *,
        access_key: builtins.str,
        bucket: builtins.str,
        display_name: builtins.str,
        path: builtins.str,
        region: builtins.str,
        secret_access_key: builtins.str,
    ) -> None:
        '''
        :param access_key: The access key identifier used to authenticate requests to the Amazon S3 account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#access_key Datastream#access_key}
        :param bucket: The name of the Amazon S3 bucket. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#bucket Datastream#bucket}
        :param display_name: The name of the connector. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#display_name Datastream#display_name}
        :param path: The path to the folder within Amazon S3 bucket where logs will be stored. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#path Datastream#path}
        :param region: The AWS region where Amazon S3 bucket resides. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#region Datastream#region}
        :param secret_access_key: The secret access key identifier used to authenticate requests to the Amazon S3 account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#secret_access_key Datastream#secret_access_key}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d4c9fc462e3c24241267b28b82435bdfd728f52965870d5d6ea735377346d36)
            check_type(argname="argument access_key", value=access_key, expected_type=type_hints["access_key"])
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument secret_access_key", value=secret_access_key, expected_type=type_hints["secret_access_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_key": access_key,
            "bucket": bucket,
            "display_name": display_name,
            "path": path,
            "region": region,
            "secret_access_key": secret_access_key,
        }

    @builtins.property
    def access_key(self) -> builtins.str:
        '''The access key identifier used to authenticate requests to the Amazon S3 account.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#access_key Datastream#access_key}
        '''
        result = self._values.get("access_key")
        assert result is not None, "Required property 'access_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bucket(self) -> builtins.str:
        '''The name of the Amazon S3 bucket.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#bucket Datastream#bucket}
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def display_name(self) -> builtins.str:
        '''The name of the connector.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#display_name Datastream#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''The path to the folder within Amazon S3 bucket where logs will be stored.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#path Datastream#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''The AWS region where Amazon S3 bucket resides.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#region Datastream#region}
        '''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def secret_access_key(self) -> builtins.str:
        '''The secret access key identifier used to authenticate requests to the Amazon S3 account.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#secret_access_key Datastream#secret_access_key}
        '''
        result = self._values.get("secret_access_key")
        assert result is not None, "Required property 'secret_access_key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamS3Connector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatastreamS3ConnectorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.datastream.DatastreamS3ConnectorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0f468febfcc1c357917e469f91e9a9974b6b7661ee48bbc3e0f4ccf29e861238)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="compressLogs")
    def compress_logs(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "compressLogs"))

    @builtins.property
    @jsii.member(jsii_name="accessKeyInput")
    def access_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="secretAccessKeyInput")
    def secret_access_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretAccessKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="accessKey")
    def access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessKey"))

    @access_key.setter
    def access_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a9de5625e364f5213779cf55686c2055e0c77d96cf95ef480e789ff57ded966)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessKey", value)

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72e1d5a1a9c30f5d1492af19f157e16f47dacafd4a5da220e6a3f44e3b80baf9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45a243eacfe4038e3fe529799af446eb8606c7694d3d83e8d59f0d9ed14f717e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2478f48a5a27e8d59160495940d9690f920a1ae0017a4057c5fdb27cc47b4491)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15f881c6aef5603c774c4389579132c9eaf2d13aa7939bcbad905da59f9ff0ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="secretAccessKey")
    def secret_access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretAccessKey"))

    @secret_access_key.setter
    def secret_access_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08dc83627cb8638fc501ea0547784acb883b1c7692059bc0e37b82485037a702)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretAccessKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DatastreamS3Connector]:
        return typing.cast(typing.Optional[DatastreamS3Connector], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DatastreamS3Connector]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80e8319faf857a56b1dba4bac4763680d7d1208aee8f481b8ef3967d7c46db21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.datastream.DatastreamSplunkConnector",
    jsii_struct_bases=[],
    name_mapping={
        "display_name": "displayName",
        "endpoint": "endpoint",
        "event_collector_token": "eventCollectorToken",
        "ca_cert": "caCert",
        "client_cert": "clientCert",
        "client_key": "clientKey",
        "compress_logs": "compressLogs",
        "custom_header_name": "customHeaderName",
        "custom_header_value": "customHeaderValue",
        "tls_hostname": "tlsHostname",
    },
)
class DatastreamSplunkConnector:
    def __init__(
        self,
        *,
        display_name: builtins.str,
        endpoint: builtins.str,
        event_collector_token: builtins.str,
        ca_cert: typing.Optional[builtins.str] = None,
        client_cert: typing.Optional[builtins.str] = None,
        client_key: typing.Optional[builtins.str] = None,
        compress_logs: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        custom_header_name: typing.Optional[builtins.str] = None,
        custom_header_value: typing.Optional[builtins.str] = None,
        tls_hostname: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param display_name: The name of the connector. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#display_name Datastream#display_name}
        :param endpoint: The raw event Splunk URL where logs will be stored. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#endpoint Datastream#endpoint}
        :param event_collector_token: The Event Collector token associated with Splunk account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#event_collector_token Datastream#event_collector_token}
        :param ca_cert: The certification authority (CA) certificate used to verify the origin server's certificate. If the certificate is not signed by a well-known certification authority, enter the CA certificate in the PEM format for verification. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#ca_cert Datastream#ca_cert}
        :param client_cert: The digital certificate in the PEM format you want to use to authenticate requests to your destination. If you want to use mutual authentication, you need to provide both the client certificate and the client key (in the PEM format). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#client_cert Datastream#client_cert}
        :param client_key: The private key in the non-encrypted PKCS8 format you want to use to authenticate with the back-end server. If you want to use mutual authentication, you need to provide both the client certificate and the client key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#client_key Datastream#client_key}
        :param compress_logs: Indicates whether the logs should be compressed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#compress_logs Datastream#compress_logs}
        :param custom_header_name: The name of custom header passed with the request to the destination. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#custom_header_name Datastream#custom_header_name}
        :param custom_header_value: The custom header's contents passed with the request to the destination. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#custom_header_value Datastream#custom_header_value}
        :param tls_hostname: The hostname that verifies the server's certificate and matches the Subject Alternative Names (SANs) in the certificate. If not provided, DataStream fetches the hostname from the endpoint URL. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#tls_hostname Datastream#tls_hostname}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64e0d410a180202099ca8a2711ddc977adbd86089ed0554b86b5ad7daa9a08e0)
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument event_collector_token", value=event_collector_token, expected_type=type_hints["event_collector_token"])
            check_type(argname="argument ca_cert", value=ca_cert, expected_type=type_hints["ca_cert"])
            check_type(argname="argument client_cert", value=client_cert, expected_type=type_hints["client_cert"])
            check_type(argname="argument client_key", value=client_key, expected_type=type_hints["client_key"])
            check_type(argname="argument compress_logs", value=compress_logs, expected_type=type_hints["compress_logs"])
            check_type(argname="argument custom_header_name", value=custom_header_name, expected_type=type_hints["custom_header_name"])
            check_type(argname="argument custom_header_value", value=custom_header_value, expected_type=type_hints["custom_header_value"])
            check_type(argname="argument tls_hostname", value=tls_hostname, expected_type=type_hints["tls_hostname"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "display_name": display_name,
            "endpoint": endpoint,
            "event_collector_token": event_collector_token,
        }
        if ca_cert is not None:
            self._values["ca_cert"] = ca_cert
        if client_cert is not None:
            self._values["client_cert"] = client_cert
        if client_key is not None:
            self._values["client_key"] = client_key
        if compress_logs is not None:
            self._values["compress_logs"] = compress_logs
        if custom_header_name is not None:
            self._values["custom_header_name"] = custom_header_name
        if custom_header_value is not None:
            self._values["custom_header_value"] = custom_header_value
        if tls_hostname is not None:
            self._values["tls_hostname"] = tls_hostname

    @builtins.property
    def display_name(self) -> builtins.str:
        '''The name of the connector.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#display_name Datastream#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def endpoint(self) -> builtins.str:
        '''The raw event Splunk URL where logs will be stored.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#endpoint Datastream#endpoint}
        '''
        result = self._values.get("endpoint")
        assert result is not None, "Required property 'endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_collector_token(self) -> builtins.str:
        '''The Event Collector token associated with Splunk account.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#event_collector_token Datastream#event_collector_token}
        '''
        result = self._values.get("event_collector_token")
        assert result is not None, "Required property 'event_collector_token' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ca_cert(self) -> typing.Optional[builtins.str]:
        '''The certification authority (CA) certificate used to verify the origin server's certificate.

        If the certificate is not signed by a well-known certification authority, enter the CA certificate in the PEM format for verification.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#ca_cert Datastream#ca_cert}
        '''
        result = self._values.get("ca_cert")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_cert(self) -> typing.Optional[builtins.str]:
        '''The digital certificate in the PEM format you want to use to authenticate requests to your destination.

        If you want to use mutual authentication, you need to provide both the client certificate and the client key (in the PEM format).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#client_cert Datastream#client_cert}
        '''
        result = self._values.get("client_cert")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_key(self) -> typing.Optional[builtins.str]:
        '''The private key in the non-encrypted PKCS8 format you want to use to authenticate with the back-end server.

        If you want to use mutual authentication, you need to provide both the client certificate and the client key.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#client_key Datastream#client_key}
        '''
        result = self._values.get("client_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def compress_logs(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Indicates whether the logs should be compressed.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#compress_logs Datastream#compress_logs}
        '''
        result = self._values.get("compress_logs")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def custom_header_name(self) -> typing.Optional[builtins.str]:
        '''The name of custom header passed with the request to the destination.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#custom_header_name Datastream#custom_header_name}
        '''
        result = self._values.get("custom_header_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_header_value(self) -> typing.Optional[builtins.str]:
        '''The custom header's contents passed with the request to the destination.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#custom_header_value Datastream#custom_header_value}
        '''
        result = self._values.get("custom_header_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls_hostname(self) -> typing.Optional[builtins.str]:
        '''The hostname that verifies the server's certificate and matches the Subject Alternative Names (SANs) in the certificate.

        If not provided, DataStream fetches the hostname from the endpoint URL.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#tls_hostname Datastream#tls_hostname}
        '''
        result = self._values.get("tls_hostname")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamSplunkConnector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatastreamSplunkConnectorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.datastream.DatastreamSplunkConnectorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c321fa1d9598a53c8786ee893ebe6bcea4568ea6e26fb208a450787167d7fcc1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCaCert")
    def reset_ca_cert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaCert", []))

    @jsii.member(jsii_name="resetClientCert")
    def reset_client_cert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCert", []))

    @jsii.member(jsii_name="resetClientKey")
    def reset_client_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientKey", []))

    @jsii.member(jsii_name="resetCompressLogs")
    def reset_compress_logs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompressLogs", []))

    @jsii.member(jsii_name="resetCustomHeaderName")
    def reset_custom_header_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomHeaderName", []))

    @jsii.member(jsii_name="resetCustomHeaderValue")
    def reset_custom_header_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomHeaderValue", []))

    @jsii.member(jsii_name="resetTlsHostname")
    def reset_tls_hostname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsHostname", []))

    @builtins.property
    @jsii.member(jsii_name="mTls")
    def m_tls(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "mTls"))

    @builtins.property
    @jsii.member(jsii_name="caCertInput")
    def ca_cert_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caCertInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCertInput")
    def client_cert_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertInput"))

    @builtins.property
    @jsii.member(jsii_name="clientKeyInput")
    def client_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="compressLogsInput")
    def compress_logs_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "compressLogsInput"))

    @builtins.property
    @jsii.member(jsii_name="customHeaderNameInput")
    def custom_header_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customHeaderNameInput"))

    @builtins.property
    @jsii.member(jsii_name="customHeaderValueInput")
    def custom_header_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customHeaderValueInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="eventCollectorTokenInput")
    def event_collector_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventCollectorTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsHostnameInput")
    def tls_hostname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsHostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="caCert")
    def ca_cert(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "caCert"))

    @ca_cert.setter
    def ca_cert(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80ba725eb1536ba6e16668af865ac379df49af203730acf8db68221c3d91b110)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caCert", value)

    @builtins.property
    @jsii.member(jsii_name="clientCert")
    def client_cert(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientCert"))

    @client_cert.setter
    def client_cert(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca92032c000670b43be543519394fef53ca26999ec24997faba1e50e6a9ef04f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCert", value)

    @builtins.property
    @jsii.member(jsii_name="clientKey")
    def client_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientKey"))

    @client_key.setter
    def client_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__158c374c21ea59fb979865202ce64d1309888576deb52f3f16d91b74f8b84053)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientKey", value)

    @builtins.property
    @jsii.member(jsii_name="compressLogs")
    def compress_logs(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "compressLogs"))

    @compress_logs.setter
    def compress_logs(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71532f01982cb3f4aea1543835443e69548d9b64c4f2ae4506d12c658dca8015)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compressLogs", value)

    @builtins.property
    @jsii.member(jsii_name="customHeaderName")
    def custom_header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customHeaderName"))

    @custom_header_name.setter
    def custom_header_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb6c6ec23ff5f1cbf05c58a3c369b2059fef50fa4e48de04076fc116a957c0fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customHeaderName", value)

    @builtins.property
    @jsii.member(jsii_name="customHeaderValue")
    def custom_header_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customHeaderValue"))

    @custom_header_value.setter
    def custom_header_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20d238ec58bd00a0c7f4d69712e37c766cc34bc90ad23c96c2b446681159dfd0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customHeaderValue", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eae62c6892ecdf4de8ea020ac1bb499cf97321a2167676883cd72653b52fb80c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b7849a220d64224f7959dd2ed129806ca7f8f20f944c84274ce21684df18155)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="eventCollectorToken")
    def event_collector_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventCollectorToken"))

    @event_collector_token.setter
    def event_collector_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8efcfd1b36d17446c0d33e6923c098290a5e45ffe0cae1d721d9bd27c125e2f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventCollectorToken", value)

    @builtins.property
    @jsii.member(jsii_name="tlsHostname")
    def tls_hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsHostname"))

    @tls_hostname.setter
    def tls_hostname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7c513d84d461ac8fbdb0fac54a60e0dce77e21ced2f7f43e251f709a4c421d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsHostname", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DatastreamSplunkConnector]:
        return typing.cast(typing.Optional[DatastreamSplunkConnector], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DatastreamSplunkConnector]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4b9507c6182e6a76ae03e15532c9566012d5350904fe9ac26068aa64d47237f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.datastream.DatastreamSumologicConnector",
    jsii_struct_bases=[],
    name_mapping={
        "collector_code": "collectorCode",
        "display_name": "displayName",
        "endpoint": "endpoint",
        "compress_logs": "compressLogs",
        "content_type": "contentType",
        "custom_header_name": "customHeaderName",
        "custom_header_value": "customHeaderValue",
    },
)
class DatastreamSumologicConnector:
    def __init__(
        self,
        *,
        collector_code: builtins.str,
        display_name: builtins.str,
        endpoint: builtins.str,
        compress_logs: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        content_type: typing.Optional[builtins.str] = None,
        custom_header_name: typing.Optional[builtins.str] = None,
        custom_header_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param collector_code: The unique HTTP collector code of Sumo Logic endpoint. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#collector_code Datastream#collector_code}
        :param display_name: The name of the connector. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#display_name Datastream#display_name}
        :param endpoint: The Sumo Logic collection endpoint where logs will be stored. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#endpoint Datastream#endpoint}
        :param compress_logs: Indicates whether the logs should be compressed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#compress_logs Datastream#compress_logs}
        :param content_type: Content type to pass in the log file header. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#content_type Datastream#content_type}
        :param custom_header_name: The name of custom header passed with the request to the destination. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#custom_header_name Datastream#custom_header_name}
        :param custom_header_value: The custom header's contents passed with the request to the destination. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#custom_header_value Datastream#custom_header_value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc524b00660a929d8b90f648f7693317d75a357a64d2db2ee9442c0f6a8c60a5)
            check_type(argname="argument collector_code", value=collector_code, expected_type=type_hints["collector_code"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument compress_logs", value=compress_logs, expected_type=type_hints["compress_logs"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument custom_header_name", value=custom_header_name, expected_type=type_hints["custom_header_name"])
            check_type(argname="argument custom_header_value", value=custom_header_value, expected_type=type_hints["custom_header_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "collector_code": collector_code,
            "display_name": display_name,
            "endpoint": endpoint,
        }
        if compress_logs is not None:
            self._values["compress_logs"] = compress_logs
        if content_type is not None:
            self._values["content_type"] = content_type
        if custom_header_name is not None:
            self._values["custom_header_name"] = custom_header_name
        if custom_header_value is not None:
            self._values["custom_header_value"] = custom_header_value

    @builtins.property
    def collector_code(self) -> builtins.str:
        '''The unique HTTP collector code of Sumo Logic endpoint.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#collector_code Datastream#collector_code}
        '''
        result = self._values.get("collector_code")
        assert result is not None, "Required property 'collector_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def display_name(self) -> builtins.str:
        '''The name of the connector.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#display_name Datastream#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def endpoint(self) -> builtins.str:
        '''The Sumo Logic collection endpoint where logs will be stored.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#endpoint Datastream#endpoint}
        '''
        result = self._values.get("endpoint")
        assert result is not None, "Required property 'endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def compress_logs(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Indicates whether the logs should be compressed.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#compress_logs Datastream#compress_logs}
        '''
        result = self._values.get("compress_logs")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def content_type(self) -> typing.Optional[builtins.str]:
        '''Content type to pass in the log file header.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#content_type Datastream#content_type}
        '''
        result = self._values.get("content_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_header_name(self) -> typing.Optional[builtins.str]:
        '''The name of custom header passed with the request to the destination.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#custom_header_name Datastream#custom_header_name}
        '''
        result = self._values.get("custom_header_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_header_value(self) -> typing.Optional[builtins.str]:
        '''The custom header's contents passed with the request to the destination.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#custom_header_value Datastream#custom_header_value}
        '''
        result = self._values.get("custom_header_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamSumologicConnector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatastreamSumologicConnectorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.datastream.DatastreamSumologicConnectorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__73289e18179ac47a3e79e62fd6ca4e8709bc1681d2f6b676061207162ddf184a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCompressLogs")
    def reset_compress_logs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompressLogs", []))

    @jsii.member(jsii_name="resetContentType")
    def reset_content_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentType", []))

    @jsii.member(jsii_name="resetCustomHeaderName")
    def reset_custom_header_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomHeaderName", []))

    @jsii.member(jsii_name="resetCustomHeaderValue")
    def reset_custom_header_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomHeaderValue", []))

    @builtins.property
    @jsii.member(jsii_name="collectorCodeInput")
    def collector_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "collectorCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="compressLogsInput")
    def compress_logs_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "compressLogsInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="customHeaderNameInput")
    def custom_header_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customHeaderNameInput"))

    @builtins.property
    @jsii.member(jsii_name="customHeaderValueInput")
    def custom_header_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customHeaderValueInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="collectorCode")
    def collector_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "collectorCode"))

    @collector_code.setter
    def collector_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83f97ee5b2251cef847272861069a4bf4353f15fdb1ad22572d6f7b8333aaa6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "collectorCode", value)

    @builtins.property
    @jsii.member(jsii_name="compressLogs")
    def compress_logs(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "compressLogs"))

    @compress_logs.setter
    def compress_logs(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5a78af596a3ea62cc82f65fb168b52ecd22bea907b4c69250a447cdbaeaf298)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compressLogs", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9102f3d71b2e4fdcf656b2f974aae5d52af46bc844486e8895affab3123b1e7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="customHeaderName")
    def custom_header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customHeaderName"))

    @custom_header_name.setter
    def custom_header_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06df082d3dd669584c26fa738f17f5e9346a491c52653c84eaad25f4055c4123)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customHeaderName", value)

    @builtins.property
    @jsii.member(jsii_name="customHeaderValue")
    def custom_header_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customHeaderValue"))

    @custom_header_value.setter
    def custom_header_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6df5b11f8e56a8e2e9fa3781d98428dc43484c7103cb3b1502f0af4b75465cb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customHeaderValue", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd6e125c8484856a2887ba49f90724cc1f13b1bfb0b5bd73e0c6308402574b5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ddcf462a17b1ee7b113df55985a48f0352ff0034012babb3ccd57927f91bc63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DatastreamSumologicConnector]:
        return typing.cast(typing.Optional[DatastreamSumologicConnector], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatastreamSumologicConnector],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67bd59d57bf5a540e188855f39960f206c22abf3ba45c6c9d9907861578bee91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="akamai.datastream.DatastreamTimeouts",
    jsii_struct_bases=[],
    name_mapping={"default": "default"},
)
class DatastreamTimeouts:
    def __init__(self, *, default: typing.Optional[builtins.str] = None) -> None:
        '''
        :param default: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#default Datastream#default}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4ad94f35522cff2172cd4efb33ddeea10df151d9cd7076e2b738ae1700188c8)
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if default is not None:
            self._values["default"] = default

    @builtins.property
    def default(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/akamai/akamai/5.6.0/docs/resources/datastream#default Datastream#default}.'''
        result = self._values.get("default")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastreamTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatastreamTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="akamai.datastream.DatastreamTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8095800784ff32c20ca1b37946cc028741c9ddb0da1db465de670d8ddf078ac9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d4b706cd01ce5805468e85c9030649955dc82c4b4793896d52aed79dd9e1cd7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DatastreamTimeouts]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DatastreamTimeouts]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DatastreamTimeouts]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7faa6a0ab58e72507b292284f55daa18786cfd2d0220b0fc87683455b57ffda3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Datastream",
    "DatastreamAzureConnector",
    "DatastreamAzureConnectorOutputReference",
    "DatastreamConfig",
    "DatastreamDatadogConnector",
    "DatastreamDatadogConnectorOutputReference",
    "DatastreamDeliveryConfiguration",
    "DatastreamDeliveryConfigurationFrequency",
    "DatastreamDeliveryConfigurationFrequencyOutputReference",
    "DatastreamDeliveryConfigurationOutputReference",
    "DatastreamElasticsearchConnector",
    "DatastreamElasticsearchConnectorOutputReference",
    "DatastreamGcsConnector",
    "DatastreamGcsConnectorOutputReference",
    "DatastreamHttpsConnector",
    "DatastreamHttpsConnectorOutputReference",
    "DatastreamLogglyConnector",
    "DatastreamLogglyConnectorOutputReference",
    "DatastreamNewRelicConnector",
    "DatastreamNewRelicConnectorOutputReference",
    "DatastreamOracleConnector",
    "DatastreamOracleConnectorOutputReference",
    "DatastreamS3Connector",
    "DatastreamS3ConnectorOutputReference",
    "DatastreamSplunkConnector",
    "DatastreamSplunkConnectorOutputReference",
    "DatastreamSumologicConnector",
    "DatastreamSumologicConnectorOutputReference",
    "DatastreamTimeouts",
    "DatastreamTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__39c7b6fa10d3cc155a2087a11d80145369c81cc9b39d5da5078a32ae2afd2168(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    active: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    contract_id: builtins.str,
    dataset_fields: typing.Sequence[jsii.Number],
    delivery_configuration: typing.Union[DatastreamDeliveryConfiguration, typing.Dict[builtins.str, typing.Any]],
    group_id: builtins.str,
    properties: typing.Sequence[builtins.str],
    stream_name: builtins.str,
    azure_connector: typing.Optional[typing.Union[DatastreamAzureConnector, typing.Dict[builtins.str, typing.Any]]] = None,
    collect_midgress: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    datadog_connector: typing.Optional[typing.Union[DatastreamDatadogConnector, typing.Dict[builtins.str, typing.Any]]] = None,
    elasticsearch_connector: typing.Optional[typing.Union[DatastreamElasticsearchConnector, typing.Dict[builtins.str, typing.Any]]] = None,
    gcs_connector: typing.Optional[typing.Union[DatastreamGcsConnector, typing.Dict[builtins.str, typing.Any]]] = None,
    https_connector: typing.Optional[typing.Union[DatastreamHttpsConnector, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    loggly_connector: typing.Optional[typing.Union[DatastreamLogglyConnector, typing.Dict[builtins.str, typing.Any]]] = None,
    new_relic_connector: typing.Optional[typing.Union[DatastreamNewRelicConnector, typing.Dict[builtins.str, typing.Any]]] = None,
    notification_emails: typing.Optional[typing.Sequence[builtins.str]] = None,
    oracle_connector: typing.Optional[typing.Union[DatastreamOracleConnector, typing.Dict[builtins.str, typing.Any]]] = None,
    s3_connector: typing.Optional[typing.Union[DatastreamS3Connector, typing.Dict[builtins.str, typing.Any]]] = None,
    splunk_connector: typing.Optional[typing.Union[DatastreamSplunkConnector, typing.Dict[builtins.str, typing.Any]]] = None,
    sumologic_connector: typing.Optional[typing.Union[DatastreamSumologicConnector, typing.Dict[builtins.str, typing.Any]]] = None,
    timeouts: typing.Optional[typing.Union[DatastreamTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__0b0f3666ff22cf6ea1540ade6620249b05bd1f903d48eea8c428829ee0dd604b(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5616c88f95f7eccedc2ddedb799e592570145ea3e1ba1a37045b3eb6ad1b67d0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cf4aabaf2e273d0d908f4ffa736348b6acb5081e7a6f503f53ead2fe996ba6e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f100ab39744218f053b1736bbd9cf989f8d7a9bf44e9e124513054ee4725d85e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2ec26371b1390d6bc90e4b424dde5085c868e45ae6d265ae07ec1ce88d2af1e(
    value: typing.List[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61f286b0021b8745f8a4902eacc8c3b6d3f5e19ca875b2e21679c506b8e7837c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e694ece03329bd5621bff093e8d22fef41c16405b05a1ef4ae6123bb16215707(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b3f3bb6e3a944571147caa1ba6893a86e053a9fa17c13b0e040154bbbb5bdd7(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5afb93c1a290c533da98fac1f91f934d4363ea379eae0bb189478fe203e20e8(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__462eebc52fdaa2d8bde23ff208b881ade325fa90d918363dec78006e1e9d914e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__889176b7a91c186ba74438804fb29033ea2d6856a3f1dfc923acb06e31318b8f(
    *,
    access_key: builtins.str,
    account_name: builtins.str,
    container_name: builtins.str,
    display_name: builtins.str,
    path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c35185cf030e1db2e5bb2d0e4bffb8d9dab7497af52390c6b1d0ea2b56dad408(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__feeb7c9c446111e2578c872ef6b7db5cf7e99aa3866e5da1ca4c8ba5f481459d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6dedced9ff591f528525ae1ea6f3dd909f747163ca4cacffd0449b7dc761ee1c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ed8289fb6906910cfe3c2598554da85d5dceee09ced83f8666791adf2a81cc2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17229af0294d9e033556031c934cff9781c5f6f17140a2ea8a89d1360692838f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1684e8b3dd2814fa540a5e8fe672b1997ce5f3c2285dabda83a407e8f7bb09a3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0732f0eade8e00032b6c277a7b72e929486d6e64eecd2fb41f1a5da56bbf847(
    value: typing.Optional[DatastreamAzureConnector],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c4366ae5518ac295d84409908df1fdcf2dd96da79082b5dc4707feb8338efce(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    active: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    contract_id: builtins.str,
    dataset_fields: typing.Sequence[jsii.Number],
    delivery_configuration: typing.Union[DatastreamDeliveryConfiguration, typing.Dict[builtins.str, typing.Any]],
    group_id: builtins.str,
    properties: typing.Sequence[builtins.str],
    stream_name: builtins.str,
    azure_connector: typing.Optional[typing.Union[DatastreamAzureConnector, typing.Dict[builtins.str, typing.Any]]] = None,
    collect_midgress: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    datadog_connector: typing.Optional[typing.Union[DatastreamDatadogConnector, typing.Dict[builtins.str, typing.Any]]] = None,
    elasticsearch_connector: typing.Optional[typing.Union[DatastreamElasticsearchConnector, typing.Dict[builtins.str, typing.Any]]] = None,
    gcs_connector: typing.Optional[typing.Union[DatastreamGcsConnector, typing.Dict[builtins.str, typing.Any]]] = None,
    https_connector: typing.Optional[typing.Union[DatastreamHttpsConnector, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    loggly_connector: typing.Optional[typing.Union[DatastreamLogglyConnector, typing.Dict[builtins.str, typing.Any]]] = None,
    new_relic_connector: typing.Optional[typing.Union[DatastreamNewRelicConnector, typing.Dict[builtins.str, typing.Any]]] = None,
    notification_emails: typing.Optional[typing.Sequence[builtins.str]] = None,
    oracle_connector: typing.Optional[typing.Union[DatastreamOracleConnector, typing.Dict[builtins.str, typing.Any]]] = None,
    s3_connector: typing.Optional[typing.Union[DatastreamS3Connector, typing.Dict[builtins.str, typing.Any]]] = None,
    splunk_connector: typing.Optional[typing.Union[DatastreamSplunkConnector, typing.Dict[builtins.str, typing.Any]]] = None,
    sumologic_connector: typing.Optional[typing.Union[DatastreamSumologicConnector, typing.Dict[builtins.str, typing.Any]]] = None,
    timeouts: typing.Optional[typing.Union[DatastreamTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12735ef33d8684197e814eb496b60558ee2c19f2f5a5f643597b5b2900b5f131(
    *,
    auth_token: builtins.str,
    display_name: builtins.str,
    endpoint: builtins.str,
    compress_logs: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    service: typing.Optional[builtins.str] = None,
    source: typing.Optional[builtins.str] = None,
    tags: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bbebad2884ed2014dac00dee3f39ce7626c938c3e31f7c5cfbf78453063083f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b34229c187ebadd57d7e51e9f9e788e6e49b213bec25e6635d744ed031f90a89(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9920293f5e0f8455b169f8668fd8861ca0c20fa91b5aa8a1e70ce7ac9c7e7315(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87c619ddd2b8ecb45025bfbaa50955e905322102de50662bbd343da6a1448240(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d8667e72af45163e274a8ef251f5ff23a341440b41e7dfd48ec8188d23ad021(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee6325a72954853d446326f9738f87d2bd5a988185ffc9ff50483345e0532c34(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__208fb39a21607da83b9d7be4712adb56290f6ff4bf6d9488974e9f72cc650904(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd0e7cbd0f9404a51d8f24c17fe4f2cb29591b3a8087cc5e5b4dcce0fe9c30ac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9952b513110f2a8e82c5eebe9c32bef9f0a35c1cd42f23f46e70f140f3f7e76(
    value: typing.Optional[DatastreamDatadogConnector],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9d61e42d9bd2a0c792677b2d5bdde380efff4023265e99dab04933c1b8650bf(
    *,
    format: builtins.str,
    frequency: typing.Union[DatastreamDeliveryConfigurationFrequency, typing.Dict[builtins.str, typing.Any]],
    field_delimiter: typing.Optional[builtins.str] = None,
    upload_file_prefix: typing.Optional[builtins.str] = None,
    upload_file_suffix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3fc16d46e2f85e21f68893d478bd421dee853df32555f5457ffa28b9ba80621(
    *,
    interval_in_secs: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2c477662ec7fc2f3ef204164aeba05eb9e3df5105fd0054befc9315c64e1c70(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__009eae23cef0ef9ff1bbd97ccfdbf1aa809d7f45928377cd44f565b677ea3220(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e56cac2c9d183e209e2be92d058e783ff85cdc7e7e58a2c3f5b2149ec3729c33(
    value: typing.Optional[DatastreamDeliveryConfigurationFrequency],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7d7c15445c8a42a3a3e01ae7291af1221a8a93808b780869970cb294482f8ee(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a308081c0afdc71dea95c0f6812aab2b8de61e5a73a1f5e8834439cf3e0d64a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b322b64d9243e0422b601b927780aeb3d2a7f6f97a29712e2718bacc3bb51409(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94eea5a0697533178d5151d0a1445cd2e8185808bd5eb528a23f256497e06e7c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbc2f8b34db19219cebfee3a82921b08d44b9b1b5adc394be99d33729f95fa5c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82638e8ae6729308c71449e5ebcf171aa4208b0a9fe210d97c4bffad8e2d33c1(
    value: typing.Optional[DatastreamDeliveryConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85f4a0fcf294f89cef2ca5731138b32a9a827be58e0de3d9ae9879ea78a65249(
    *,
    display_name: builtins.str,
    endpoint: builtins.str,
    index_name: builtins.str,
    password: builtins.str,
    user_name: builtins.str,
    ca_cert: typing.Optional[builtins.str] = None,
    client_cert: typing.Optional[builtins.str] = None,
    client_key: typing.Optional[builtins.str] = None,
    content_type: typing.Optional[builtins.str] = None,
    custom_header_name: typing.Optional[builtins.str] = None,
    custom_header_value: typing.Optional[builtins.str] = None,
    tls_hostname: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd8f250f949b8e12ec18bcff419c1c3b4ab8651b92d94bc524d94644d7c35776(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbcabc16742e8c109c31c26839165d5e12c7974e8c8009a1a0bf638cbb28eb15(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e830aa9e75a4f43ca823bd82943099670f04acdffdb86c985e048b9fc22e6d8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a363af39834923508a1b3dac25971d77df85d8064c143910b72831165a5da542(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b19bbb70f52b8fb3bedf1abe09e57d42979655abc5828f049f23538742d041a4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e21ba10b74e1b1a267cc1bd012b647085ec1a3de3a477b14968ce06b6a0a4b76(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38eab0523cb3cdb7d41845fe1c3af353d10236a01e0bf410b8477e4d07e4f00e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f24559d7ded97f0e22f36f24e7910d14fdfa73e71b068eee6252a94f34586789(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ef7380369a95ad3a50e72d0a6632e7fb6a0056735fd3a0eb040cc8535663dd9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65b3b2fe6656993af1afe356af593b4d0faf0bec7372bfb4999fed4f2c0e10c1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9f959e812215096d7dbac6afa890665990bbcad74d7cd9c906a519392e8fee5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b58ae26f58080939afcf1b2a783ff9150ad14e8ebdcea518909519c08da1c8b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87afae4b1c3213550b0a409d84396174087106b2f6824bc80cf04047669fcc7b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e79fe20ddca88361c0e2cb0c765f4b8a170bb3039cddf1fd44a9f6fbadc16e0b(
    value: typing.Optional[DatastreamElasticsearchConnector],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba8d43bd5f33e84923afa821070d9a4a451fd5ba10e13bcd230c589d61d25049(
    *,
    bucket: builtins.str,
    display_name: builtins.str,
    private_key: builtins.str,
    project_id: builtins.str,
    service_account_name: builtins.str,
    path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2eb01841cefd140c2d7088c4723d02bf8dfee7f35d2ae8be08161b251b614f81(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4bb97846cdf137be6c3d8239e86ead2e0383a64d5b9025f6ce83c83188b0526(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5069ed7f0ed42d32181d81029551215afa80c5db65f054911f08976500b084e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eacbae59b6da9a1214932814360e2cccfa26695945e7c3d1de9288e2abfef413(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e0b701ba66dbac061e772920d9aa0e94538613d9df251d556abc5b7b16ebdae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01bd8da70d1627102ca35af2baa8cd5249d79834c7dac5e9c5216c161e2baf3e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a6fe03d0aa97d333443f009c25228a85d651369e371804274ef62d9eacccf6f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73415bb77aae34c3bfea9b7b063da1b4c209df805a08392d4aa3c94015e14491(
    value: typing.Optional[DatastreamGcsConnector],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7723146f16e3835acd53d0a64206159f70c32e4fe17c82ddd721ddda468907cd(
    *,
    authentication_type: builtins.str,
    display_name: builtins.str,
    endpoint: builtins.str,
    ca_cert: typing.Optional[builtins.str] = None,
    client_cert: typing.Optional[builtins.str] = None,
    client_key: typing.Optional[builtins.str] = None,
    compress_logs: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    content_type: typing.Optional[builtins.str] = None,
    custom_header_name: typing.Optional[builtins.str] = None,
    custom_header_value: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    tls_hostname: typing.Optional[builtins.str] = None,
    user_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b6ce20caf3f80a114a60fc517cf753fbba9990a5874ceb2434cf888133f3d20(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4264c448b60000908e010f1a93780bac81dcfe80c6b3da7ba770a043139482c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__367e1e696834a9562ac5de80a6ce7213ad9dc2eade4d30d9bcfa8b8fd2e0a4e6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a443f29d8f1c4a8a6171319ce2c8542c326e0cf6f81e5f5ee28138d29c590be3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c20e5673a76dbcd109293e3e2fb252ed2726ee8a3dd50165c256d275ef32871b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9db187e1bcf44dfa3360bede57a2503d5cb52610ce1853d215034dac5179a713(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91a0ba4803f1ffed0f4282c419953c0e9464853d70acf456ecc92ba8bfa055f3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdff7a559052ab6cfe0501edd97f2d5aa4385631063f06524d5c37d5bdb52649(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96c6a37560eca6a07d843f5a1a4b87707fec48553d615e1666027d55df7a096a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4db628fde15b9df35e44a3dcbc2638539fa989463aadf915dfecc48f9b8c20b3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd3824b827a424dd1b5ff9fb7cae0f482be4f567df789fcb1d367d986d0a6016(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b2d38dc1381200144e46985f9ef75184c24f90eac6f47728389f2d6eeed6361(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d97665069e71c1647846504017dab5eca12ad7d542a9268570a35cff780380f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__966d6a042b31821aa1fd539c863552a7f3b8317e1b671344d509f23aa885a7f3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba99880f6d2cdd26079c7be46e00103f95b9a172ac73484ab3c544ff0316fcef(
    value: typing.Optional[DatastreamHttpsConnector],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e3146f5e5a213c58ca02bc717ea886728de32fc5fff99af91f7e09cbfeeb06d(
    *,
    auth_token: builtins.str,
    display_name: builtins.str,
    endpoint: builtins.str,
    content_type: typing.Optional[builtins.str] = None,
    custom_header_name: typing.Optional[builtins.str] = None,
    custom_header_value: typing.Optional[builtins.str] = None,
    tags: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6d05f1908e74f8ddf990137e9dfd01e7e7e78a36bb235daed83f024b35c521c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a4ec9a1152edb665966aa00b4ec3401b5f371eb67b59d8db084439fe9043f2e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39620e73f54e3379ccf17774f42eb64779ca72f3ce7bab5a1f7b3361b51dab1c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa2be8e7349786a90cbbb7910a01bec25fd1ef416328d7ce275c7e295affb96f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68c62f54a23de7d02531046c346b93b99fc943d16285256b9295b5fb2a6343c6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4386cd06a2c2d8e70b4229a9284e778d838edbf66d78f6e401b3f10a4755737c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fbffc1fa7e0a064cfd57cc312f12559141a43714159b31c9db052856c5be923(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ee9a6b190d9f66286d49acde1e8420e8e594ce47c3dae07bcb8d9b94a4d0db5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c4fbd78a5e5fed5fdc0c416de2818e3034d1c42734d551aaf01606d79b49094(
    value: typing.Optional[DatastreamLogglyConnector],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bb21c52f3b3e2c493dd88b2ca8d98dbd2b9f996ae5811fa9ad8b3bfa58945a3(
    *,
    auth_token: builtins.str,
    display_name: builtins.str,
    endpoint: builtins.str,
    content_type: typing.Optional[builtins.str] = None,
    custom_header_name: typing.Optional[builtins.str] = None,
    custom_header_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b505f8cb9d76d2a0470cbea6088a9e47b87299e8002e735fe0a618914e0b507(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__feb03c92b1978e31c484789ecef69c680686b4f436f890b60a996761f768cad3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2edf6768128a246d3b412c33cb0783d7375a3b0ea9e0447229f6cec912af9d1f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a1942fda8ba386b9bcbc2e5d8447308cbdff2609cf36ea417f5e03aabb8f847(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba7d0a5d72eb715a5a951c35edf75bd68fd336984af36b97231705c578a9c87b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__090a5297501f08d8c237f9ec16898a6eb6eeda985e4df80667011b26b7dc5ffd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3aa281de5622bec38b0a33539cc6b116d6a212c9b7e314cebc3a9a109cb82f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b63667e5244b4aa13aab1c800706f387ce87aecd608d2639de7cf547874262b(
    value: typing.Optional[DatastreamNewRelicConnector],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0016fb68b6e64ed37ddb7e534f6faaa04d6a768bd38a3dcb3dad3ef7f347249d(
    *,
    access_key: builtins.str,
    bucket: builtins.str,
    display_name: builtins.str,
    namespace: builtins.str,
    path: builtins.str,
    region: builtins.str,
    secret_access_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acdfc281daf629fc338b963b94e767ca986255ba3099252704719decb0d0d084(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e7cdf2ee160e5b9c770e83f5bd3e5663017b73918c59cb5a4a4b1cf6310d589(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b43017242febcc51265c05e86ebc9d5678bd354f03086dff859c5f99822cd07(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1bb4f79be249466bfd15b024b960fc15d6087d4a7e4f8a204edb9d572cb7af3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68eaf8da68e650d34037e1fe9a98e9d96ae62e67d438f38149630b127499e625(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9645c5e96eb2c9f14ea427713320d0e06f5fc128c1c530b92afd6b4b9d2073af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__941217a664670a3eb34dbb57870294a4ccc82007d84315ec324deac80ce179d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb5facfcf6b0d06dc51ca8a4b93ceca017ed89551b4f60bf7db725c2bc4f3b48(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f388cde6002a55ab2d115701e1b029ed0d606f28314e4c3c1c63592bf1e6996(
    value: typing.Optional[DatastreamOracleConnector],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d4c9fc462e3c24241267b28b82435bdfd728f52965870d5d6ea735377346d36(
    *,
    access_key: builtins.str,
    bucket: builtins.str,
    display_name: builtins.str,
    path: builtins.str,
    region: builtins.str,
    secret_access_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f468febfcc1c357917e469f91e9a9974b6b7661ee48bbc3e0f4ccf29e861238(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a9de5625e364f5213779cf55686c2055e0c77d96cf95ef480e789ff57ded966(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72e1d5a1a9c30f5d1492af19f157e16f47dacafd4a5da220e6a3f44e3b80baf9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45a243eacfe4038e3fe529799af446eb8606c7694d3d83e8d59f0d9ed14f717e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2478f48a5a27e8d59160495940d9690f920a1ae0017a4057c5fdb27cc47b4491(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15f881c6aef5603c774c4389579132c9eaf2d13aa7939bcbad905da59f9ff0ed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08dc83627cb8638fc501ea0547784acb883b1c7692059bc0e37b82485037a702(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80e8319faf857a56b1dba4bac4763680d7d1208aee8f481b8ef3967d7c46db21(
    value: typing.Optional[DatastreamS3Connector],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64e0d410a180202099ca8a2711ddc977adbd86089ed0554b86b5ad7daa9a08e0(
    *,
    display_name: builtins.str,
    endpoint: builtins.str,
    event_collector_token: builtins.str,
    ca_cert: typing.Optional[builtins.str] = None,
    client_cert: typing.Optional[builtins.str] = None,
    client_key: typing.Optional[builtins.str] = None,
    compress_logs: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    custom_header_name: typing.Optional[builtins.str] = None,
    custom_header_value: typing.Optional[builtins.str] = None,
    tls_hostname: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c321fa1d9598a53c8786ee893ebe6bcea4568ea6e26fb208a450787167d7fcc1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80ba725eb1536ba6e16668af865ac379df49af203730acf8db68221c3d91b110(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca92032c000670b43be543519394fef53ca26999ec24997faba1e50e6a9ef04f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__158c374c21ea59fb979865202ce64d1309888576deb52f3f16d91b74f8b84053(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71532f01982cb3f4aea1543835443e69548d9b64c4f2ae4506d12c658dca8015(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb6c6ec23ff5f1cbf05c58a3c369b2059fef50fa4e48de04076fc116a957c0fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20d238ec58bd00a0c7f4d69712e37c766cc34bc90ad23c96c2b446681159dfd0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eae62c6892ecdf4de8ea020ac1bb499cf97321a2167676883cd72653b52fb80c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b7849a220d64224f7959dd2ed129806ca7f8f20f944c84274ce21684df18155(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8efcfd1b36d17446c0d33e6923c098290a5e45ffe0cae1d721d9bd27c125e2f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7c513d84d461ac8fbdb0fac54a60e0dce77e21ced2f7f43e251f709a4c421d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4b9507c6182e6a76ae03e15532c9566012d5350904fe9ac26068aa64d47237f(
    value: typing.Optional[DatastreamSplunkConnector],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc524b00660a929d8b90f648f7693317d75a357a64d2db2ee9442c0f6a8c60a5(
    *,
    collector_code: builtins.str,
    display_name: builtins.str,
    endpoint: builtins.str,
    compress_logs: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    content_type: typing.Optional[builtins.str] = None,
    custom_header_name: typing.Optional[builtins.str] = None,
    custom_header_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73289e18179ac47a3e79e62fd6ca4e8709bc1681d2f6b676061207162ddf184a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83f97ee5b2251cef847272861069a4bf4353f15fdb1ad22572d6f7b8333aaa6c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5a78af596a3ea62cc82f65fb168b52ecd22bea907b4c69250a447cdbaeaf298(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9102f3d71b2e4fdcf656b2f974aae5d52af46bc844486e8895affab3123b1e7d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06df082d3dd669584c26fa738f17f5e9346a491c52653c84eaad25f4055c4123(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6df5b11f8e56a8e2e9fa3781d98428dc43484c7103cb3b1502f0af4b75465cb8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd6e125c8484856a2887ba49f90724cc1f13b1bfb0b5bd73e0c6308402574b5d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ddcf462a17b1ee7b113df55985a48f0352ff0034012babb3ccd57927f91bc63(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67bd59d57bf5a540e188855f39960f206c22abf3ba45c6c9d9907861578bee91(
    value: typing.Optional[DatastreamSumologicConnector],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4ad94f35522cff2172cd4efb33ddeea10df151d9cd7076e2b738ae1700188c8(
    *,
    default: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8095800784ff32c20ca1b37946cc028741c9ddb0da1db465de670d8ddf078ac9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4b706cd01ce5805468e85c9030649955dc82c4b4793896d52aed79dd9e1cd7d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7faa6a0ab58e72507b292284f55daa18786cfd2d0220b0fc87683455b57ffda3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DatastreamTimeouts]],
) -> None:
    """Type checking stubs"""
    pass
