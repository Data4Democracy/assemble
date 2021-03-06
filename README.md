## Assemble

**Slack:** [#assemble](https://datafordemocracy.slack.com/messages/assemble/)

**Project Description:** Assemble is a [data for democracy](https://github.com/Data4Democracy) community working to build tools and infrastructure to enable the study of online communities and their characteristics. We have several active [repositories](#infrastructure-repositories), our goal is to build a toolkit which takes care of common tasks so researchers do not have to reinvent the wheel with each new project.  

[**Project Leads:**](https://github.com/Data4Democracy/read-this-first/blob/master/lead-role-description.md)
* [@bstarling](https://datafordemocracy.slack.com/messages/@bstarling/)
* [@nick](https://datafordemocracy.slack.com/messages/@nick/)

[**Maintainers:**](./roles/project_maintainer.md) Maintainers have write access to the repository. They are responsible for reviewing pull requests, providing feedback and ensuring consistency.

* [@sjackson](https://datafordemocracy.slack.com/messages/@sjackson/) (Subject Matter Knowledge)
* [@wwymak](https://datafordemocracy.slack.com/messages/@wwymak/) (Community Detection, NLP)
* [@henripal](https://datafordemocracy.slack.com/messages/@henripal/) (Assemble, Community Detection, NLP)
* [@alarcj](https://datafordemocracy.slack.com/messages/@alarcj/) (collect-social, onboarding, tutorials, twitter-analysis)


[**Project Ambassadors:**](https://github.com/Data4Democracy/assemble/blob/master/roles/project_ambassador.md)

* [@ccarey](https://datafordemocracy.slack.com/messages/@ccarey/)

## Getting Started:
* For a list of first steps, please visit our [community guide](community-guide.md).
* Read about how we use issue [labels](issue-labels-explained.md)


### Things you should know

* **"First-timers" are welcome!** Whether you're trying to learn data science, hone your coding skills, or get started collaborating over the web, we're happy to help. *(Sidenote: with respect to Git and GitHub specifically, our [github-playground](https://github.com/Data4Democracy/github-playground) repo and the [#github-help](https://datafordemocracy.slack.com/messages/github-help/) Slack channel are good places to start.)*
* **We believe good code is reviewed code.** All commits to this repository are approved by project maintainers and/or leads (listed above). The goal here is *not* to criticize or judge your abilities! Rather, sharing insights and achievements. Code reviews help us continually refine the project's scope and direction, as well as encourage the discussion we need for it to thrive.
* **This README belongs to everyone.** If we've missed some crucial information or left anything unclear, edit this document and submit a pull request. We welcome the feedback! Up-to-date documentation is critical to what we do, and changes like this are a great way to make your first contribution to the project.


### Currently utilized skills
Take a look at this list to get an idea of the tools and knowledge we're leveraging. If you're good with any of these, or if you'd like to get better at them, this might be a good project to get involved with!

If you would like to get started with any of these skills, check out the [tutorials](https://github.com/Data4Democracy/tutorials) and chat about it in [#learning](https://datafordemocracy.slack.com/messages/learning/).

* **Python 3** (scripting, web scraping, analysis, Jupyter notebooks, visualization)
* **Data extraction/ETL**
* **Data cleaning**

## Project Areas

### Infrastructure
If you like the idea of building tools that will help enable analysis across many domains these projects are a great place to start. If you have an idea for a dataset you would like to collect please file a proposal via GitHub issue with the label `proposal`.  


### Curation
Leveraging the Infrastructure group's fantastic work, the Curation team makes available repositories of information about online communities. The data is "analysis ready" and has been curated to support downstream analytical objectives, and the team works closely with the data.world staff.  

### Infrastructure Repositories
* [town-council](https://github.com/bstarling/town-council): Tools to scrape and centralize the text of meeting agendas & minutes from local city governments.
* [smtk](https://github.com/Data4Democracy/smtk): Ambitious attempt to combine all below projects + more into single toolkit.
* [Discursive](https://github.com/Data4Democracy/discursive): Framework for searching or streaming tweets storing them in Elasticsearch and S3.
* [Collect-Social](https://github.com/Data4Democracy/collect-social): This project aims to make that collection process as simple as possible, by making some common-sense assumptions about what most researchers need, and how they like to work with their data. For example, tasks like grabbing all the posts and comments from a handful of Facebook pages, and dumping the results into a sqlite database.
* [Reddit-Api-Miner](https://github.com/Data4Democracy/reddit-api-miner) No longer active. Reddit integration is on the roadmap for smtk.

#### Data pipeline  
We are looking for people to take our raw data and curate it so that it is analysis ready. You will work closely with the the person(s) who gathered the data to understand methodologies for how the data was gathered to help document the end to end data cleaning process for future analysts. [Eventador](http://eventador.io/) has gracioulsy donated infrastructure to assist with this effort.

**Additional Resources:**
* Getting started with [Eventador](./eventador/README.md)
* See [DATA GOVERNANCE](https://github.com/Data4Democracy/read-this-first/blob/master/governance.md).

**Raw data:**
* [Info Source](./data/info_source.md)
* [Congressional Record](./data/congressional-record.md)
* [Discursive](./data/discursive.md)
* Have data to add? Check our [how-to guide](./data/how_to_submit_dataset.md)

### Curation Projects
* [Oathkeepers](./data/oathkeepers.md) - Militia and white nationalist twitter data

### Tutorials and Example Notebooks:
We need people who would like to write [tutorials](https://github.com/Data4Democracy/tutorials) or script examples on how to do common tasks.  
* Do not worry if you are not an expert. Tutorials from the perspective of a beginner are great for other beginners.  

### Examples of work that has inspired us:   
* [Bot or not](http://truthy.indiana.edu/botornot/)
* [Alt-Right](https://www.washingtonpost.com/news/the-intersect/wp/2016/09/26/these-charts-show-exactly-how-racist-and-radical-the-alt-right-has-gotten-this-year/?utm_term=.def874e48329)
* [politwoops](https://projects.propublica.org/politwoops/)  



Special thanks to the drug-spending team for writing such a great README we borrowed liberally from it
