import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("SteamData.csv")               # This loads the data in a form that is malleable

plt.figure(figsize=(20, 10))                    # This line sets the window size
plt.bar(df["game"], df["price"])     # This sets the x axis to look at the first column (which holds the game names) and the y to look at the positive reviews column.

### I decided that the graph was a little hard to correlate the numbers, so I added horizontal lines every 100k reviews.
max_val = df["price"].max()
for y in range int((0, max_val +100000, 100000)):
    plt.axhline(y, linestyle="--", linewidth=0.7)


plt.title("Positive Reviews by Game")           # This is a title that goes above ALL other content
plt.xlabel("Game Name")                         # This is the title of the x axis and appears on the bottom
plt.ylabel("# Of Positive Reviews")             # This is the title of the y axis and appears on the left

plt.xticks(rotation=30, ha="right")             # Keeps Longer names readable.
plt.tight_layout()                              # Adjusts spacing to keep it minimal, but still get the point accross.
plt.show()                                      # This line actually brings up the graph and shows the information to the user.

# I had issues when it came to making the program plot the prices, as they were float, and the range() omly uses integars. 
# My solution was to convert the price to int before plugging into the code for the horizontal guidelines.
