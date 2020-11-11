import re
from urllib.request import urlopen
from matplotlib import pyplot as plt


def draw_graph(x, y):
    plt.plot(x, y)
    plt.title('Graфik')
    plt.xlabel('День')
    plt.ylabel('Кол-во сорвавшихся')
    plt.grid(True)
    plt.show()


def get_website_statistics():
    html = urlopen("https://dofamin.org/index.php?v=ServerFailStat").read().decode("UTF-8")
    html = html[html.index(">Срывов"):]
    array_of_days = [int(x[x.index(">")+1:]) for x in re.findall(r'a">\d{,8}', html)]
    array_of_quantity = [int(x[x.index(">")+1:]) for x in re.findall(r'b">\d{,8}', html)]
    return array_of_days[:-5], array_of_quantity[:-5]


if __name__ == "__main__":
    a = 8
    b = 100
    x, y = get_website_statistics()
    # print(x)
    draw_graph(x[a:b+1], y[a:b+1])
