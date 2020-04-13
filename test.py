from urllib.request import urlopen
h = urlopen("https://dofamin.org/index.php?v=ServerFailStat").read().decode("UTF-8")
h = h[h.index("""<div class="fail-stat__column fail-stat__column_b">Срывов</div>"""):]

print(h)
