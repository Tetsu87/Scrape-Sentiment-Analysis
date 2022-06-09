from textblob import TextBlob
import json
from langdetect import detect
from tqdm import tqdm
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import spacy
nlp = spacy.load('en_core_web_sm')

# open output.json
json_open = open('output.json', 'r')

# load json
json_load = json.load(json_open)

sentences_paragraph = []
sentences_entire = []
num_articles = 0

# extract each content from json and check if the articles are in English
for content in json_load:
    if detect(content['contents']) == 'en':
        num_articles += 1
        sentence = []
        tokens = nlp(content['contents'])
        # split the text into individual sentences
        for sent in tokens.sents:
            sentence.append(sent.text.strip())
        sentences_paragraph.append(sentence)
        sentences_entire.append(tokens.text)

textblob_entire_sentiment = []

# sentiment analysis using the entire content of each article as data
polarity = []
subjectivity = []
titles = []
for s in sentences_entire:
    txt = TextBlob(s)
    a = txt.sentiment.polarity
    b = txt.sentiment.subjectivity
    textblob_entire_sentiment.append([s[:20]+'...', a, b])
    polarity.append(a)
    subjectivity.append(b)
    titles.append('Article: ' + s[:20] + '...')

#  visualize the results by plotting the sentiment using the plotly visualization library
df_textblob = pd.DataFrame(textblob_entire_sentiment, columns=[
                           'Article', 'Polarity', 'Subjectivity'])
fig1 = px.scatter(df_textblob, x="Polarity", y="Subjectivity",
                  width=800, height=600, hover_data=['Article'])
fig1.update_layout(title=dict(text='Sentiment Analysis Using the Entire Content of Each Article'),
                   font=dict(size=16))
fig1.update_traces(marker=dict(size=16))
fig1.update_xaxes(range=[-1, 1])
fig1.update_yaxes(range=[-0.05, 1.05])
fig1.show()

# sentiment analysis of each article broken down to the sentence level
textblob_paragraph_sentiment = []
x = []
y = []

for sentences in sentences_paragraph:
    paragraph = []
    x_sub = []
    y_sub = []
    titles_sub = []
    for sentence in sentences:
        if sentence != '':
            txt = TextBlob(sentence)
            a = txt.sentiment.polarity
            b = txt.sentiment.subjectivity
            paragraph.append([sentence, a, b])
            x_sub.append(a)
            y_sub.append(b)
            titles_sub.append(sentence)
    textblob_paragraph_sentiment.append(paragraph)
    x.append(x_sub)
    y.append(y_sub)

fig2 = make_subplots(
    rows=2,
    cols=5,
    subplot_titles=titles,
    horizontal_spacing=0.03,
    vertical_spacing=0.15
)

# create a graph for each article
for i in range(num_articles):
    if i <= 4:
        fig2.add_trace(
            go.Scatter(
                x=x[i],
                y=y[i],
                mode='markers',
            ), row=1, col=i+1)
        fig2.update_xaxes(title_text="Polarity", row=1, col=i+1,
                          range=[-1, 1], tickvals=[-1, -0.5, 0, 0.5, 1])
        if i == 0:
            fig2.update_yaxes(title_text="Subjectivity",
                              row=1, col=i+1, range=[-0.05, 1.05])
        else:
            fig2.update_yaxes(row=1, col=i+1, range=[-0.05, 1.05])
    else:
        fig2.add_trace(
            go.Scatter(
                x=x[i],
                y=y[i],
                mode='markers',
            ), row=2, col=i-4)
        fig2.update_xaxes(title_text="Polarity", row=2, col=i-4,
                          range=[-1, 1], tickvals=[-1, -0.5, 0, 0.5, 1])
        if i == 5:
            fig2.update_yaxes(title_text="Subjectivity",
                              row=2, col=i-4, range=[-0.05, 1.05])
        else:
            fig2.update_yaxes(row=2, col=i-4, range=[-0.05, 1.05])
    fig2.update_traces(marker=dict(size=12))

fig2.update_layout(
    title="Sentiment Analysis of Each Article in Sentence Level",
    showlegend=False
)
fig2.show()
