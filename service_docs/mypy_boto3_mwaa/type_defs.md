# Structures for boto3 MWAA module

> [Index](../index.md) > [MWAA](./index.md) > Structures

Auto-generated documentation for [MWAA](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa.html#MWAA)
type annotations stubs module [mypy_boto3_mwaa](https://pypi.org/project/mypy-boto3-mwaa/).

- [Structures for boto3 MWAA module](#structures-for-boto3-mwaa-module)
  - [DimensionTypeDef](#dimensiontypedef)
  - [EnvironmentTypeDef](#environmenttypedef)
  - [LastUpdateTypeDef](#lastupdatetypedef)
  - [LoggingConfigurationTypeDef](#loggingconfigurationtypedef)
  - [ModuleLoggingConfigurationInputTypeDef](#moduleloggingconfigurationinputtypedef)
  - [ModuleLoggingConfigurationTypeDef](#moduleloggingconfigurationtypedef)
  - [NetworkConfigurationTypeDef](#networkconfigurationtypedef)
  - [ResponseMetadata](#responsemetadata)
  - [StatisticSetTypeDef](#statisticsettypedef)
  - [UpdateErrorTypeDef](#updateerrortypedef)
  - [CreateCliTokenResponseTypeDef](#createclitokenresponsetypedef)
  - [CreateEnvironmentOutputTypeDef](#createenvironmentoutputtypedef)
  - [CreateWebLoginTokenResponseTypeDef](#createweblogintokenresponsetypedef)
  - [GetEnvironmentOutputTypeDef](#getenvironmentoutputtypedef)
  - [ListEnvironmentsOutputTypeDef](#listenvironmentsoutputtypedef)
  - [ListTagsForResourceOutputTypeDef](#listtagsforresourceoutputtypedef)
  - [LoggingConfigurationInputTypeDef](#loggingconfigurationinputtypedef)
  - [MetricDatumTypeDef](#metricdatumtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [UpdateEnvironmentOutputTypeDef](#updateenvironmentoutputtypedef)
  - [UpdateNetworkConfigurationInputTypeDef](#updatenetworkconfigurationinputtypedef)

## DimensionTypeDef

```python
from mypy_boto3_mwaa.type_defs import DimensionTypeDef
```


Required fields:
- `Name`: `str`
- `Value`: `str`




## EnvironmentTypeDef

```python
from mypy_boto3_mwaa.type_defs import EnvironmentTypeDef
```




Optional fields:
- `AirflowConfigurationOptions`: `Dict[str, str]`
- `AirflowVersion`: `str`
- `Arn`: `str`
- `CreatedAt`: `datetime`
- `DagS3Path`: `str`
- `EnvironmentClass`: `str`
- `ExecutionRoleArn`: `str`
- `KmsKey`: `str`
- `LastUpdate`: `"LastUpdateTypeDef"`
- `LoggingConfiguration`: `"LoggingConfigurationTypeDef"`
- `MaxWorkers`: `int`
- `MinWorkers`: `int`
- `Name`: `str`
- `NetworkConfiguration`: `"NetworkConfigurationTypeDef"`
- `PluginsS3ObjectVersion`: `str`
- `PluginsS3Path`: `str`
- `RequirementsS3ObjectVersion`: `str`
- `RequirementsS3Path`: `str`
- `ServiceRoleArn`: `str`
- `SourceBucketArn`: `str`
- `Status`: `EnvironmentStatus`
- `Tags`: `Dict[str, str]`
- `WebserverAccessMode`: `WebserverAccessMode`
- `WebserverUrl`: `str`
- `WeeklyMaintenanceWindowStart`: `str`


## LastUpdateTypeDef

```python
from mypy_boto3_mwaa.type_defs import LastUpdateTypeDef
```




Optional fields:
- `CreatedAt`: `datetime`
- `Error`: `"UpdateErrorTypeDef"`
- `Status`: `UpdateStatus`


## LoggingConfigurationTypeDef

```python
from mypy_boto3_mwaa.type_defs import LoggingConfigurationTypeDef
```




Optional fields:
- `DagProcessingLogs`: `"ModuleLoggingConfigurationTypeDef"`
- `SchedulerLogs`: `"ModuleLoggingConfigurationTypeDef"`
- `TaskLogs`: `"ModuleLoggingConfigurationTypeDef"`
- `WebserverLogs`: `"ModuleLoggingConfigurationTypeDef"`
- `WorkerLogs`: `"ModuleLoggingConfigurationTypeDef"`


## ModuleLoggingConfigurationInputTypeDef

```python
from mypy_boto3_mwaa.type_defs import ModuleLoggingConfigurationInputTypeDef
```


Required fields:
- `Enabled`: `bool`
- `LogLevel`: `LoggingLevel`




## ModuleLoggingConfigurationTypeDef

```python
from mypy_boto3_mwaa.type_defs import ModuleLoggingConfigurationTypeDef
```




Optional fields:
- `CloudWatchLogGroupArn`: `str`
- `Enabled`: `bool`
- `LogLevel`: `LoggingLevel`


## NetworkConfigurationTypeDef

```python
from mypy_boto3_mwaa.type_defs import NetworkConfigurationTypeDef
```




Optional fields:
- `SecurityGroupIds`: `List[str]`
- `SubnetIds`: `List[str]`


## ResponseMetadata

```python
from mypy_boto3_mwaa.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## StatisticSetTypeDef

```python
from mypy_boto3_mwaa.type_defs import StatisticSetTypeDef
```




Optional fields:
- `Maximum`: `float`
- `Minimum`: `float`
- `SampleCount`: `int`
- `Sum`: `float`


## UpdateErrorTypeDef

```python
from mypy_boto3_mwaa.type_defs import UpdateErrorTypeDef
```




Optional fields:
- `ErrorCode`: `str`
- `ErrorMessage`: `str`


## CreateCliTokenResponseTypeDef

```python
from mypy_boto3_mwaa.type_defs import CreateCliTokenResponseTypeDef
```




Optional fields:
- `CliToken`: `str`
- `WebServerHostname`: `str`


## CreateEnvironmentOutputTypeDef

```python
from mypy_boto3_mwaa.type_defs import CreateEnvironmentOutputTypeDef
```




Optional fields:
- `Arn`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateWebLoginTokenResponseTypeDef

```python
from mypy_boto3_mwaa.type_defs import CreateWebLoginTokenResponseTypeDef
```




Optional fields:
- `WebServerHostname`: `str`
- `WebToken`: `str`


## GetEnvironmentOutputTypeDef

```python
from mypy_boto3_mwaa.type_defs import GetEnvironmentOutputTypeDef
```




Optional fields:
- `Environment`: `"EnvironmentTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListEnvironmentsOutputTypeDef

```python
from mypy_boto3_mwaa.type_defs import ListEnvironmentsOutputTypeDef
```


Required fields:
- `Environments`: `List[str]`



Optional fields:
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListTagsForResourceOutputTypeDef

```python
from mypy_boto3_mwaa.type_defs import ListTagsForResourceOutputTypeDef
```




Optional fields:
- `Tags`: `Dict[str, str]`
- `ResponseMetadata`: `"ResponseMetadata"`


## LoggingConfigurationInputTypeDef

```python
from mypy_boto3_mwaa.type_defs import LoggingConfigurationInputTypeDef
```




Optional fields:
- `DagProcessingLogs`: `"ModuleLoggingConfigurationInputTypeDef"`
- `SchedulerLogs`: `"ModuleLoggingConfigurationInputTypeDef"`
- `TaskLogs`: `"ModuleLoggingConfigurationInputTypeDef"`
- `WebserverLogs`: `"ModuleLoggingConfigurationInputTypeDef"`
- `WorkerLogs`: `"ModuleLoggingConfigurationInputTypeDef"`


## MetricDatumTypeDef

```python
from mypy_boto3_mwaa.type_defs import MetricDatumTypeDef
```


Required fields:
- `MetricName`: `str`
- `Timestamp`: `datetime`



Optional fields:
- `Dimensions`: `List["DimensionTypeDef"]`
- `StatisticValues`: `"StatisticSetTypeDef"`
- `Unit`: `Unit`
- `Value`: `float`


## PaginatorConfigTypeDef

```python
from mypy_boto3_mwaa.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## UpdateEnvironmentOutputTypeDef

```python
from mypy_boto3_mwaa.type_defs import UpdateEnvironmentOutputTypeDef
```




Optional fields:
- `Arn`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateNetworkConfigurationInputTypeDef

```python
from mypy_boto3_mwaa.type_defs import UpdateNetworkConfigurationInputTypeDef
```


Required fields:
- `SecurityGroupIds`: `List[str]`


