# How to use biocolabsdk ?

**The package only allows data submission via BioStudio private server. Please configure your tokens in the `User Settings` page.**

</br>
<img alt="setting" src="https://cdn.bioturing.com/documentation/md/user-setting.png" width="100%">
</br>

## 1. Access to BBrowserX private server via biocolabsdk:

### 1.1. Test the connection to BBrowserX private server:

```python

from biocolabsdk import EConnector

connector = EConnector(
  private_host="https://yourcompany/t2d_index_tool/",
  private_token="<input your token here>"
)

connector.get_bbrowserx().test_connection()
```

Example output:

```
Connecting to host at https://yourcompany/t2d_index_tool/api/v1/test_connection
Connection successful
```

### 1.2. Get user groups available for your token in BBrowserX private server:

```python

from biocolabsdk import EConnector

connector = EConnector(
  private_host="https://yourcompany/t2d_index_tool/",
  private_token="<input your token here>"
)

user_groups = connector.get_bbrowserx().get_user_groups()
print(user_groups)
```

Example output:

```
[{'id': 'all_members', 'name': 'All members'}, {'id': 'personal', 'name': 'Personal workspace'}]
```

### 1.3. Submit your data to BBrowserX private server:

```python

from biocolabsdk import EConnector
from bioturing_connector.typing import InputMatrixType
from bioturing_connector.typing import Species
from bioturing_connector.typing import StudyType

connector = EConnector(
  private_host="https://yourcompany/t2d_index_tool/",
  private_token="<input your token here>"
)

# Call this function first to get available groups and their id.
user_groups = connector.get_bbrowserx().get_user_groups()
# Example: user_groups is now [{'id': 'all_members', 'name': 'All members'}, {'id': 'personal', 'name': 'Personal workspace'}]

# Submitting the scanpy object from s3:
batch_info = [{
    'matrix': 's3_path/GSE128223_1.h5ad',
}, {
    'matrix': 's3_path/GSE128223_2.h5ad',
}]

connector.get_bbrowserx().submit_study_from_s3(
  group_id='personal',
  batch_info=batch_info,
  study_id='GSE128223',
  name='This is my first study',
  authors=['Huy Nguyen'],
  species=Species.HUMAN.value,
  input_matrix_type=InputMatrixType.RAW.value,
  study_type=StudyType.H5AD.value
)

# Submitting the scanpy object from local machine:
batch_info = [{
    'matrix': 'local_path/GSE128223_1.h5ad',
}, {
    'matrix': 'local_path/GSE128223_2.h5ad',
}]

connector.get_bbrowserx().submit_study_from_local(
  group_id='personal',
  batch_info=batch_info,
  study_id='GSE128223',
  name='This is my first study',
  authors=['Huy Nguyen'],
  species=Species.HUMAN.value,
  input_matrix_type=InputMatrixType.RAW.value,
  study_type=StudyType.H5AD.value
)
```

## 2. Access Talk2Data public server via biocolabsdk:

```python

from biocolabsdk import EConnector

connector = EConnector(
  public_token="<input your token here>"
)

connector.get_talk2data().test_connection()
```

Example output:

```
Connecting to host at https://talk2data.bioturing.com/t2d_index_tool/api/v1/test_connection
Connection successful
```

You can utilize all the features in a similar way to accessing a BBroserX private server.

## 3. Access bioflex public server via biocolabsdk:

You can obtain a bioflex token by submiting a request in the `User Settings` page.

### Create a connection using access token:

```python
from biocolabsdk import EConnector

connector = EConnector(
  bioflex_token="<input your token here>"
)
```

### List available databases:

```python
databases = connector.get_bioflex().databases()
```
>```
> [DataBase(id="5010c7d573ae4ff2b9691422b99aa2cd",
>           name="BioTuring database",species="human",version=1),
> DataBase(id="5010c7d573ae4ff2b9691422b99aa2cd",
>           name="BioTuring database",species="human",version=2),
> DataBase(id="5010c7d573ae4ff2b9691422b99aa2cd",
>           name="BioTuring database",species="human",version=3)]

### Get database cell types gene expression summary

```python
database = databases[2]
database.get_celltypes_expression_summary(['CD3D', 'CD3E'])
```

>```
> {'CD3D': [Summary(name="B cell",sum=707108874.0,mean=4192.7096,rate=0.035,count=168652.0,total=4812967),
> 	Summary(name="CD4-positive, alpha-beta T cell",sum=9489987442.0,mean=4657.5619,rate=0.5283,count=2037544.0,total=3856590),
> 	...
> 	Summary(name="corneal progenitor",sum=0.0,mean=0.0,rate=0.0,count=0.0,total=3973),
> 	Summary(name="nucleus pulposus progenitor cell",sum=0.0,mean=0.0,rate=0.0,count=0.0,total=2310)]}


### Create study instance, using study hash ID from [BioTuring studies](https://talk2data.bioturing.com/studies/):

```python
study = database.get_study('GSE96583_batch2')
study
```
>```
> Study(id="GSE96583_batch2",
>       title="Multiplexed droplet single-cell RNA-sequencing using natural genetic variation (Batch 2)",
>       reference="https://www.nature.com/articles/nbt.4042")

### Take a peek at study metadata:

```python
study.metalist
```
>```
> [Metadata(id=0,name="Number of mRNA transcripts",type="Numeric"),
>  Metadata(id=1,name="Number of genes",type="Numeric"),
>  Metadata(id=2,name="Batch id",type="Category"),
>  Metadata(id=3,name="Stimulation",type="Category"),
>  Metadata(id=4,name="Author's cell type",type="Category")]

### Fetch a study metadata:

```python
metadata = study.metalist[4]
metadata
```
>```
>Metadata(id=4,name="Author's cell type",type="Category")
```python
metadata.fetch()
metadata.values
```
>```
> array(['CD8 T cells', 'Dendritic cells', 'CD4 T cells', ...,
>        'CD8 T cells', 'B cells', 'CD4 T cells'], dtype='<U17')

### Query genes:

```python
exp_mtx = study.query_genes(['CD3D', 'CD3E'], bioflex.UNIT_LOGNORM)
exp_mtx
```
>```
> <29065x2 sparse matrix of type '<class 'numpy.float32'>'
>     with 15492 stored elements in Compressed Sparse Column format>

### Get study barcodes:

```python
study.barcodes()
```
>```
> ['GSM2560249_AAACATACCAAGCT-1',
>  'GSM2560249_AAACATACCCCTAC-1',
>  ...
>  'GSM2560249_AATTGTGATTCACT-1',
>  'GSM2560249_AATTGTGATTTCGT-1',
>  ...]

### Get study features:

```python
study.features()
```
>```
> ['5S_RRNA',
>  '5_8S_RRNA',
>  ...
>  'AC006273',
>  'AC006277',
>  ...]

### Get study full matrix:

```python
study.matrix(bioflex.UNIT_LOGNORM)
```
>```
> <29065x64642 sparse matrix of type '<class 'numpy.float32'>'
> 	with 17570739 stored elements in Compressed Sparse Column format>

### Export Study:

```python
study.export_study(bioflex.EXPORT_H5AD)
```
>```
>{'download_link': 'https://talk2data.bioturing.com/api/export/a1003bad3dd146b28c7bda913a2fc3f0',
> 'study_hash_id': 'GSE96583_batch2'}

----
For further information please check the [documentation](https://studio.bioturing.com/document/biocolabsdk).