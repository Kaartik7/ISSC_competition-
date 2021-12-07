import matplotlib.pyplot as plt

giardiasis = [469, 456, 419, 370, 397, 396, 414, 359, 390, 401, 429]
influenza = [2601, 1249, 1565, 1017, 2096, 2521, 3546, 2698, 3136,
             4231, 2672]
paratyphoid_fever = [21, 17, 9, 18, 11, 18, 6, 13, 11, 4, 6]
malaria = [82, 81, 98, 90, 89, 81, 73, 61, 67, 66, 10]
tuberclosis = [292, 276, 302, 317, 289, 288, 254, 262, 300, 286, 293]


def visualise(lst: list, name: str):

    # x axis values
    x = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
    # corresponding y axis values
    # plotting the points
    plt.plot(x, lst, color='green', linestyle='dashed', linewidth=3,
             marker='o', markerfacecolor='blue', markersize=12)

    # naming the x axis
    plt.xlabel('year')
    # naming the y axis
    plt.ylabel('cases')

    # giving a title to my graph
    plt.title('Cases v/s Year')

    # function to show the plot
    plt.show()
