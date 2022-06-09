# Scrape-Sentiment-Analysis

1. Web Scraping  
(INSTRUCTIONS)  
Run scrapy.py to output the results of web scraping as output.json.  
(Description)  
The web scraping code is described in scrape.py. In this program, Beautiful Soup was used to scrape the ten most recent news items listed at https://www.aljazeera.com/where/mozambique/. The json contains the title, subtitle,contents, image(url link), figcaption, date, and data source.  

2. Sentiment Analysis  
(INSTRUCTIONS)  
Run sentiment.py to compute the sentiment of each news article and display the results of the sentiment analysis in the browser.  
(Description)  
Sentiment analysis was performed using TextBlob. After extracting contents from the json containing the web scraping results and confirming that it was in English, sentiment analysis was performed on the entire article (Entire.png) or each sentence in the article (Sentence.png).
Entire.png provides an overview of the overall sentiment trends of aljazeera news in Mozambique, while Sentence.png provides a more detailed sentiment analysis of each article.  

3. Total operation time  
4 hours