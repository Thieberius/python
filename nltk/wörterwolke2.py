from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = "Love Love Love Love Love Love Love Love Love Love Love Love Love Love Love Love Love Love Love Love Love Love Love Love Love Love Love Love Love Love Love Love Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate Hate Kitty Kitty Kitty Kitty Kitty Kitty Kitty Kitty Kitty Kitty Kitty Kitty Kitty Kitty Kitty Kitty Kitty Kitty Kitty Kitty Kitty Kitty Kitty Kitty Kitty Kitty Kitty Kitty Kitty Kitty Kitty Kitty Kitty Kitty Kitty Kitty Kitty Friendship Friendship Friendship Friendship Friendship Friendship Friendship Friendship Friendship Friendship Friendship Friendship Friendship Friendship Friendship Friendship Friendship Friendship Friendship"

# Generate a word cloud image
wordcloud = WordCloud().generate(text)

plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
