## Social Media Sentiment Analysis Pipeline

![googleimage](https://lh4.googleusercontent.com/TMZSmMLMbRY8xn8Pa3wS-Ndt8ox3wS6v6PKwd5gGzEzKt7FNWu5_lAVw7L_e0PwCZgusz9yguPLuh5sxJuGLwiAIscR29kV-VFBwWxY3xEzYgBwJgTM_Uh1ITEMS-g)
image [credit](http://melbourne.resbaz.edu.au/post/80232473657/sentiment-analysis-tools-for-humanities)

### The problem

Showing aggregated social media feeds in real-time to indicate mood, sentiment, likely-hood of performing actions, opinion or belonging to some class.

### Data Source

Social media. Twitter, FB, Instagram, Snapchat, Pinterest, etc.

### NLP, Sentiment Analysis

Twitter, and to a larger degree, all of social media can be mined in real-time, the data is fed to Eventador where NLP and Sentiment Analysis can take place to create time-series, singleton gauges, or other graphics based on the sentiment of a group on a particular a topic (or array of hashtags). Eventador.io allows for mutation, cleansing, aggregation, and processing algorithms to be run in real time against the stream. This data can ultimately power applications to compel and explain. For instance:

Wouldn't this be cool if it was real time showing interest right now?
https://www.google.com/trends/explore?q=Donald%20Trump,hillary%20clinton

What about this project, but not just for the convention, but all the time?
http://time.com/4410941/republican-convention-mood/

### Status

Eventador.io and the D4D:Assemble team are currently working on wiring up a constant real-time twitter feed. The broad components so far are:

- Twitter Feed
- Processing Framework (Storm on Eventador)
- Ad Hoc SQL components (Presto on Eventador)
- Real time endpoint: (WIP)
- Front end components: (In scope?)
