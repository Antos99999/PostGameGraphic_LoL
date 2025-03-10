import matplotlib.pyplot as plt
import numpy as np

def GraphCreate(Minuts, GoldPerMinutBlue, GoldPerMinutRed):

    y_final_blue = []
    y_final_red = []

    y_diff = []
    y_diff_add = []
    y_diff_odd = []

    y_temp_blue = GoldPerMinutBlue
    y_temp_red = GoldPerMinutRed

    x = Minuts

    for element in zip(*y_temp_blue):
        y_final_blue.append(sum(element))

    for element in zip(*y_temp_red):
        y_final_red.append(sum(element))

    for a, b in zip(y_final_blue, y_final_red):
        # Obliczenie różnicy i dodanie do listy differences
        y_diff.append(a - b)


    for i in range(len(y_diff)):
        if y_diff[i] >= 0:
            y_diff_add.append(y_diff[i])
            y_diff_odd.append(0)
        elif y_diff[i] <= 0:
            y_diff_odd.append(y_diff[i])
            y_diff_add.append(0)


    max_val = np.round(max(y_diff_add)/500)*500
    min_val = np.round(min(y_diff_odd)/500)*500


    plt.figure(figsize=(20, 6))

    plt.xlim(0, len(x))
    plt.xticks(range(0, len(x) - 1))
    plt.yticks(range(int(min_val)-500, int(max_val)+500,500))

    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)

    plt.tick_params(axis='both', colors='white')

    # Usuwanie kresk (ticks) na osi x
    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=True)

    # Usuwanie kresk (ticks) na osi y
    plt.tick_params(axis='y', which='both', left=False, right=False, labelleft=True, pad=10)

    plt.plot(x, y_diff_add,marker = '.', color = 'goldenrod')
    plt.fill_between(x, y_diff_add, 0, color = 'goldenrod')
    plt.plot(x, y_diff_odd,marker = '.', color = 'darkred') #slategrey
    plt.fill_between(x, y_diff_odd, 0, color = 'darkred')
    plt.savefig('Graphs/Gold.png',bbox_inches='tight',facecolor='none',transparent=True)
    #plt.show()

if "__main__" == __name__:
    GraphCreate()