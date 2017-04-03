# Uses tldextract module (https://github.com/john-kurkowski/tldextract)
# import the modukes
import pandas as pd
import tldextract as tld

# Load the url dataset
url_df = pd.read_csv('youtube_urls.csv') # Local or uncomment below line if you want to load from the aws
# df = pd.read_csv('https://s3.amazonaws.com/far-right/fourchan/youtube_urls.csv')

# Let's extract domains
url_list = url_df['url'].tolist()
domain_dict = {}
for url in url_list:
    ext = tld.extract(url)
    domain = ext.domain
    if domain_dict.has_key(domain):
        domain_dict[domain] += 1
    else:
        domain_dict[domain] = 1

# Write the results to a csv file
result_df = pd.DataFrame(domain_dict.items(), columns=['Domain', 'Count'])
result_df.to_csv('domain_counts.csv')
