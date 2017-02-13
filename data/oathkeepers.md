# Oathkeepers
```
far-right/  
|--twitter/
  |--oathkeepers
    |--data-notes.txt
    |--militia.sqlite
    |--oathkeepers-seeds.txt
    |--oathkeepers.sqlite
    |--public-militia-pages.csv
    |--white-nationalist-twitter.sqlite
    |--white-nationalists-twitter-scored.csv
```

List directory contents with AWS CLI
`aws s3 ls s3://far-right/twitter/oathkeepers/ --profile <credential_profile>` see [`aws configure`](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html).  
For aws credentials for read-only access, ping [@bstarling](https://datafordemocracy.slack.com/messages/@bstarling/), [@nick](https://datafordemocracy.slack.com/messages/@nick/), [@sjackson](https://datafordemocracy.slack.com/messages/@sjackson/), [@wwymak](https://datafordemocracy.slack.com/messages/@wwymak/), or [@divya](https://datafordemocracy.slack.com/messages/@divya/).

Notes on the datasets in this directory:

**public-militia-pages.csv**
A hand-curated list of militia groups operating in the US that have public pages on Facebook. I only included groups that had posted at least once in 2016.

**militia.sqlite**
Contains posts, interactions, and comments from the the pages in public-militia-pages.csv.

**oathkeepers.sqlite**
A database of users, tweets, links (friend/follow relationships), and influences (mentions), built from the seed accounts in oathkeepers-seeds.txt. Basically I started with the seeds, which were accounts I'd manually identified as being associated with Oath Keepers (far right separatist/patriot/militia group), then collected people their followers, and the followers of their followers, to build a network of connected accounts. I haven't applied any ranking/scoring/classification to this dataset yet, so some accounts won't be associated with the Oath Keepers.

**white-nationalist-twitter.sqlite**
A database of users, tweets, links (friend/follow relationships), and influences (mentions), built in a similar way to oathkeepers.sqlite. Some accounts won't be white nationalist/alt-right/Nazis, but the white-nationalists-twitter-scored.csv file contains scores assigned to accounts using a 95% accurate LSTM classifier that used account profile text as input data.

**white-nationalists-twitter-scored.csv**
Accounts from white-nationalist-twitter.sqlite scored based on how much their account profile indicated support of white nationalism.
