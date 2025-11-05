from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

s  = SentimentIntensityAnalyzer()

text_a = "\ntoday is a great day to code!"
text_b = "\nsyntax errors really suck"

print(text_a)
print(s.polarity_scores(text_a))

print(text_b)
print(s.polarity_scores(text_b))
