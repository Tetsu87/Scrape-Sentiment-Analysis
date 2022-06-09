import requests
from bs4 import BeautifulSoup
import json
from tqdm import tqdm
from textblob import TextBlob
from langdetect import detect
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import spacy
nlp = spacy.load('en_core_web_sm')
