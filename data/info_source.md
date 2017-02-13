# Info Source
```
far-right/  
|--info-source/
  |--daily
    |--<date>
      |--<Source1>
      |--<Source2>
    |--<date2>
      |--<Source1>
      |--<Source2>
    |--<date3>
      |--<Source1>
      |--<Source2>
  |--archive
    |--breitbart
      |--<historic_file1.json>
      |--<historic_file2.json>
      |--<historic_file3.json>
    |--stormfront
      |--<historic_file1.json>
      |--<historic_file2.json>
      |--<historic_file3.json>
```
`aws s3 ls s3://far-right/info-source/ --profile <credential_profile>`
see [`aws configure`](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)  
For aws credentials for read-only access, ping [@bstarling](https://datafordemocracy.slack.com/messages/@bstarling/), [@nick](https://datafordemocracy.slack.com/messages/@nick/), [@sjackson](https://datafordemocracy.slack.com/messages/@sjackson/), [@wwymak](https://datafordemocracy.slack.com/messages/@wwymak/), or [@divya](https://datafordemocracy.slack.com/messages/@divya/).

`daily` has one folder per day (UTC time), inside that folder there is a folder for each source.
* `breitbart` folder will have a file for each news category containing most recent ~30-35 articles for that category. Originally posted every four hours, now posted every twelve hours.
  * naming convention `<category>_<time>.json` where time is the UTC time snapshot was taken.
  * Since this process dumps the most recent articles without knowledge snapshot `big-government_1200.json` and `big-government_1600.json` could be the same if no new articles were published between 1200 hours and 1600 hours (UTC).
  * These files will need to be combined and de-duped before real analysis can start.
* `stormfront`
  * TBD - still gathering historic activity. 
* `radix`
  * Running 2x daily (noon and midnight UTC)
* `americanren`
  * Running 2x daily (noon and midnight UTC)
* `4chan`
  * Running 2x daily (noon and midnight UTC)

`archive` folder contains historic results (much larger files).
* `breitbart`:
  * one file per news category. Entire collection is ~240k articles starting in early 2012.
  * Should not have dupes unless an article appeared in multiple categories (TBD)
* `stormfront`
  * In progress, new sources posted daily. One file per sub-forum
