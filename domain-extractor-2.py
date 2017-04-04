import pandas as pd
import tldextract
df = pd.read_csv('https://s3.amazonaws.com/far-right/fourchan/youtube_urls.csv')

# split URLs into subdomain, domain and suffix
df['subdomain'],df['domain'],df['suffix'] = zip(*df['url'].map(tldextract.extract))
del df['subdomain'], df['suffix']

# rename youtube variants and misspellings
df['domain'] = df.domain.str.replace(r'(^.*youtu.*$)', 'youtube')

# list unique values with their count
df['domain'].value_counts()
