# Congressional Record
```
far-right/  
|--congressional-record-archive/
  |--1995to1997.json
  |--1997to2007.json
  |--2007to2017.json
```

List directory contents with AWS CLI
`aws s3 ls s3://far-right/congressional-record-archive/ --profile <credential_profile>` see [`aws configure`](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)

```
2017-02-03 21:30:33    0 Bytes
2017-02-03 21:43:04  608.0 MiB 1995to1997.json
2017-02-03 21:39:39    2.5 GiB 1997to2007.json
2017-02-03 21:33:23    2.1 GiB 2007to2017.json

Total Objects: 4
   Total Size: 5.1 GiB
```

Thanks to @john who donated the congressional [record archive](https://www.congress.gov/congressional-record) 1995-2017.

File contains lines of JSON objects with the below fields:

```
url
title
date
congress
session
issue
volume
start_page
end_page
text
```
