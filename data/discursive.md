# Discursive
```
discursive/  
  |--2017/
    |--1/
      |--1/
        |--1/
          |--tweets-1.json
```

List directory contents with AWS CLI
`aws s3 ls s3://discursive --profile <credential_profile>` see [`aws configure`](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)

Notes on the datasets in this directory:

**Directory structure and content:**
The Discursive tweet collection in S3 follows the pattern of year -> month -> day -> hour -> filename.json

These files are the result of streaming that is executed on a cron job running every fifteen minutes, collecting five thousand tweets per job (as of the creation of this document we have about eleven million). Sometimes, tweets won't be collected resulting in a gap (i.e. an hour is missing from a day, a day is missing from a month, etc.). You should consider this when designing your ingestion process (i.e. workaround failures for a file read). We expect those scenarios to be infrquent. 

**Tweet fields available:**

`name:` screen_name of the user

`message:` tweet text

`description:` user provided description

`loc:` user provided location

`text:` tweet text

`user_created:` date user created (i.e. 2012-01-19 20:28:24)

`followers:` number of followers

`id_str:` tweet ID

`created:` date tweet created (i.e. 2017-01-20 11:08:22)

`retweet_count:` number of retweets (where applicable)

`retweet:` flag for whether this is a retweet

`friends_count:` count of account friends

`topics:` topics used in the stream search

`hashtags:` tweet hashtags

`original_name:` original tweet author
