import plotly.express as px
from die import Die



die = Die()

# results = []
# for roll_num in range(1000):
#     result = die.roll()
#     results.append(result)

# frequencies = []
# poss_results = range(1, die.num_sides + 1)

# for value in poss_results:
#     frequency = results.count(value)
#     frequencies.append(frequency)

# title = "Results of rolling a D6 1000 times"
# labels = {"x": "Result", "y": "Frequency"}

# fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
# fig.show()


## Two dice rolls

die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(100):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
poss_results = range(2, die_1.num_sides + die_2.num_sides + 1)

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)   

title = "Results of rolling two D6 1000 times"
labels = {"x": "Result", "y": "Frequency"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()
