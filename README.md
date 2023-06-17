# web-uplift

This repository allows you to uplift biological files from one genome assembly to another as a web service. It is based on the pyliftover package, which is a python wrapper for the UCSC liftOver tool. 

## Supported file formats

The following file formats are currently supported:

* Bed
* Gff / Gff3 / Gtf
* Wig

## Usage

Example API call:

```bash
curl -X POST -F "file=@test_data/hg19.bed" "<base_url>/uplift?from=hg19&to=hg38&type=bed"
```

### Parameters

| Parameter | Description                                                                | Default                                 |
| --------- | -------------------------------------------------------------------------- | --------------------------------------- |
| from      | The source genome assembly                                                 | hg19                                    |
| to        | The target genome assembly                                                 | hg38                                    |
| type      | The file type                                                              | The file extension of the uploaded file |
| file      | The file to uplift: Has to be provided as form data with "file" as the key | None                                    |
