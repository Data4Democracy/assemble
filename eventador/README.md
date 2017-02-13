
# Eventador README

### Use Cases

Eventador.io is a real-time data streaming platform. It allows for rich capture, mutation, aggregation, and delivery to various end-points. It's not an 'do everything' database, but rather a platform for when real-time data compels, enriches, or tells a story in a way that batch one-off data just can't.

## Getting Started

Eventador.io is a real time data processing platform that is available to the project free of charge. To use it do the following:

- Sign up for Eventador.io [here](https://console.eventador.io/register)
- In the #assemble Slack channel, ping @kgorman or @erikbeebe to add you to the D4D account OR
- Email Eventador [Support](mailto:support@eventador.io) and request access.

## Using Eventador.io

In order to partition work out for a variety of use cases, project contributors should use unique topic's for discrete workloads. This will allow everyone to utilize the system and not have data collisions or a general data mess.

To create a topic:

- Login to Eventador.io [here](http://www.eventador.io/login)
- Click on the Deployment you would like to use (initially there is one called 'assemble').
- Select the 'add Topic' button.
- Name your Topic something descriptive.
- Use this Topic when publishing data to Eventador.io

**NOTE** you will need to open an ACL to your client interface in order to connect. Eventador is closed by default, and must have an IP whitelist created for your IP or IP range in order to use it.

To create an ACL:

- [ACL's in Eventador](http://www.eventador.io/acls.html)

## Links

Here are some (hopefully) helpful resources:

- [Examples](https://github.com/Eventador/examples)
- [Command Line](http://www.kennygorman.com/tactical-kafka)
- [Getting Connected](http://www.eventador.io/getting-connected.html)

## When Eventador.io makes sense for your project

Eventador.io is best used when creating stories around real-time data or data that has high
value in it's immediate form. It's great when your source of data is dynamic, and the resulting analysis, report, graphic, dashboard or whatever is also dynamic.

## Examples and Hypothetical use Cases

These are pie in the sky type scenarios where the Eventador.io platform would be a meaningful component allowing the Data Scientist to simple worry about the data itself and not sweat the finer points of real-time data distribution. Hopefully these use cases give you inspiration and ideas. Please contribute!

A list of potential use-cases, and created pipelines is available here: https://github.com/Data4Democracy/assemble/tree/master/eventador/pipelines
