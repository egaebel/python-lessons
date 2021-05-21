import csv
import matplotlib.pyplot as plt
import numpy as np

"""
Lesson 1: Reading data from csv files and plotting it.

CSV file header:
Currency,Date,Closing Price (USD),24h Open (USD),24h High (USD),24h Low (USD)

Relevant documentation:
    argparse package (official Python3.8 docs): https://docs.python.org/3.8/library/argparse.html
    csv package (official Python 3.8 docs): https://docs.python.org/3.8/library/csv.html
    Matplotlib pyplot: https://matplotlib.org/stable/tutorials/introductory/pyplot.html
    Matplotlib plot_date: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot_date.html
    Numpy documentation (arange specifically): https://numpy.org/doc/stable/reference/generated/numpy.arange.html

Assignment:
    1. Read through all the code here and comments too.
    2. Generalize this. Use Python functions to generalize this charting and then run it on the
        Ethereum data in 'ethereum-data--coindesk.csv'.
    3. Use your generalized code to plot the Bitcoin data and Ethereum data in the same chart.
        Make the chart pretty!
    4. Update the code to take a command line argument that specifies a csv file containing crypto
        data in the expected format and reads from that specified file. Use the Python 'argparse'
        library to do this.
"""

# Open the given csv file in "read" mode.
csv_file = open("bitcoin-data--coindesk.csv", "r")
# Create a csv reader and specify that the file does use commas for delimiting. By default the csv
# reader will assume commas, but you can set it to something else like tabs, spaces, or anything
# else.
# The csv_reader object is an iterator. It does not have a known length and will just keep
# returning things from it until it runs out of things to return. It behaves similarly to the Java
# iterator.
csv_reader = csv.reader(csv_file, delimiter=",")
# Create an empty list. We'll use this list to hold the data we read from the csv file.
crypto_data_list = list()

# Read the first row of the csv file by explicitly invoking 'next' on the iterator. This will
# advance the iterator one position, so that the next time we read from it it will read the second
# row of the file. Note the weird method name with two underscores before and after.
#
# The first row is the header, which we don't want to store in our data, but it can be helpful for
# validating that we're reading the right thing.
header_row = csv_reader.__next__()
# Print the header_row for a sanity check and just nice confirmation that the program is doing the
# right stuff. We're using a special kind of string formatting here called an 'f-string' (the f
# stands for formatting I think?). When you make a string an f-string (done by prefixing the quotes
# with the letter f) then variables and code placed within curly braces in the string will be
# evaluated. We could even have put our "csv_reader.next()" line from above here instead of the
# variable 'header_row'.
print(f"Reading data from csv file, header is: {header_row}")
# Loop over the remaining rows in the csv file.
for row in csv_reader:
    # Each 'row' object that's returned is a list. Convert the 'row' list to a tuple and store it
    # in our 'crypto_data_list'. A tuple is a very handy data structure Python provides, it can
    # contain any type of data or combination of types of data, but that data is immutable, meaning
    # you can't change anything about a tuple once you create it. We're using the 'tuple' fuction
    # here to convert a list to a tuple, but you can create a tuple manually by using parentheses
    # like this:
    #
    # (1, 2, 3)
    row_tuple = tuple(row)
    crypto_data_list.append(row_tuple)

# In Python instead of there being a 'size' method on collections like tuples, lists, maps, etc
# there is a universal 'len' function that will get the length of any collection. This next part
# is not really necessary to know, but these collections all define a method named: '__len__' which
print(f"Read '{len(crypto_data_list)}' rows of data from csv file!")

# Let's do another sanity check to make sure our data is being pulled from the csv file in the
# format we expect, we'll take some samples from throughout the list.
#
# Below we're going to slice our 'crypto_data_list' to take the first 'num_samples' samples from
# it. Python supports slicing lists to extract a range of elements (0->N) from anywhere in a list.
# You can specify where you want to start and/or end, but if you leave either off Python will go
# from/to the start or end, respectively. You can even leave off the start/end arguments altogether
# and Python will just copy the whole list, e.g. crypo_data_list[:] When you slice a list, the
# result is a brand new list, so you are copying data every time you slice.
#
# This stackoverflow post has a pretty comprehensive rundown of python slicing notation:
# https://stackoverflow.com/questions/509211/understanding-slice-notation
num_starting_samples = 10
crypto_data_starting_samples = crypto_data_list[:num_starting_samples]
# When we take a slice, in addition to providing the starting/ending values you can provide a step
# size by adding an extra colon and adding the step value onto the end. If you haven't provided
# start/end values then it would be: crypto_data_list[::1000]
crypto_data_middle_samples = crypto_data_list[
    num_starting_samples : len(crypto_data_list) : 1000
]
# Python collections support negative indexes too! Negative indexes start at 1 and correspond to
# the end of the collection. So -1 refers to the last element in the list, -2 the second to last,
# etc. You can think of indexing as being circular, where 0 is the first element in the list, 1
# is the second, -1 is the last, etc.
crypto_data_final_sample = crypto_data_list[-1:]
# Note below that we're appending these three strings together without any plus signs. Python
# automatically concatenates strings that are adjacent to one another.
print(
    f"\nSampled '{num_starting_samples}' data points from the start of 'crypto_data_list': '{crypto_data_starting_samples}'\n\n"
    f"Sampled '{len(crypto_data_middle_samples)}' data points throughout the middle of 'crypto_data_list': '{crypto_data_middle_samples}'\n\n"
    f"And sampled 1 data point from the end of 'crypto_data_list': '{crypto_data_final_sample}'\n\n"
)

# Extract "Date" and "Closing Price (USD)" (see header format above) to be our x and y here.
#
# Let's do some functional programming! Just a little though.
#
# So, crypto_data_list is the list holding all of our data and we want to extract the Date and
# Closing Price (USD) columns to plot in something pretty. So for every single row of our data we
# want to grab just one column. This is a simple data transformation, so we're going to use 'map'.
# The 'map' function takes two arguments, an iterable (like a list), and a function. You can pass
# a fully fleshed out and defined Python function here, or if you're doing something simple you can
# define what's called (across programming languages) a 'lambda' function. A 'lambda' function is
# defined in place, usually in one or only a few lines. In Python all you need to do to define one
# is to write 'lambda <variable 1 name>, <variable 2 name>, :' and that's it. After the colon you
# write the code you want the function to execute and your lambda function is fully defined.
# Lambdas are super useful for simple data transformations like this.
crypto_data_date_list = list(map(lambda x: x[1], crypto_data_list))
# You can also assign lambda functions to variables.
my_lambda_that_grabs_the_closing_price = lambda x: float(x[2])
# To use the lambda attached to the variable you just pass in the variable like any other.
crypto_data_closing_price_list = list(
    map(my_lambda_that_grabs_the_closing_price, crypto_data_list)
)

print(f"Plotting '{len(crypto_data_list)}' points with matplotlib.....")
# Let's plot some stuff.
#
# We'll be using matplotlib's pyplot package to do this. It copied matlab's plotting functions,
# they even admit this in their docs. So we'll first pass in our x and y data that we want to plot
# and then we'll make some formatting changes, and then we'll show our nice plot.
plt.plot_date(crypto_data_date_list, crypto_data_closing_price_list)

# You may have noticed that there's a bunch of data points in our csv file, 2,790 to be exact, and
# each data point has a really long date associated with it. Aint nobody got room on their x-axis
# for all that. Crypto is also volatile as hell, so there are massive price swings. Aint nobody got
# room on their y-axis for that either!!
#
# So, let's use our data to come up with sensible x and y axis ticks and labels.
#
# First, the dates, that'll be simpler because they're monotonically increasing. This is also a
# great time to introduce a Python-favorite, list comprehensions! A list comprehension is a way to
# define a list inline by iterating over one or more lists, computing something, and maybe
# including a filtering condition. This is actually very similar to the 'map' function above
# (except map doesn't let you filter), but there are times when list comprehensions will be quicker
# for you to add.
#
# So, what we're going to do in our list comprehension is to first call 'enumerate' which will add
# an index to each element in our list. Note that we can accommodate this index by just adding the
# variable 'i' and a comma in our for-loop syntax. Now that we have our handy index we're going to
# take every 30th element of our list with the condition: i % 30 == 0. Remember, the percent sign
# indicates the modulus operation (taking the remainder from division). Why 30? Because I ran this
# code a bunch of times and 30 is the lowest number we can use without the chart looking bad and it
# corresponds to approximately a month, so that's nice.
x_axis_ticks = [x for i, x in enumerate(crypto_data_date_list) if i % 30 == 0]

# Now let's come up with a sensible way to divy up the price data.
# We'll use numpy for the first time here, specifically the arange function which takes a starting
# number, an ending number, and an optional 'step' parameter to create a sequence from start-end
# jumping 'step' on each element. This is the first time we've used an optional parameter in
# Python! Optional function parameters are great, they let you specify default values for them
# when you define your function and then callers don't have to specify them unless they want to
# change from their default.
y_axis_ticks = np.arange(0, max(crypto_data_closing_price_list) + 10000, step=2000)
# We're going to use another optional parameter here. The 'rotation' parameter will rotate the
# x-axis labels by the specified number of degrees. This will let us pack more dates into the
# x-axis of our chart.
plt.xticks(x_axis_ticks, rotation=45)
plt.yticks(y_axis_ticks)

# Let's show the plot! This will open up a GUI window and will keep it up indefinitely (unless
# Windows breaks that for some reason. I vaguely recall that it might). To close the program press
# ctrl+c in your terminal.
plt.show()
print("Plotted data!")