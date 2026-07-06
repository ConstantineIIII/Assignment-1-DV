import matplotlib.pyplot as plt

# Questions:
# Which games sold the most units?
# Which genre earned the most revenue?
# Which platform performed the best worldwide?
# Which region generated the most revenue?
# Does higher marketing spend seem connected to higher revenue?
# Which games had high ratings but low sales?
# Which games had strong sales despite lower ratings?

sales_data = [
    ["2023-01-30", "Game A", "PC", "North America", "Action", 1000, 50000],
    ["2023-01-30", "Game B", "PS4", "Europe", "Adventure", 1600, 77000],
    ["2023-01-30", "Game C", "PS4", "Europe", "Sports", 1700, 80000],
    ["2023-02-15", "Game D", "Xbox", "North America", "Racing", 900, 43000],
    ["2023-02-15", "Game E", "Switch", "Asia", "Puzzle", 1200, 56000],
    ["2023-03-12", "Game F", "PC", "Europe", "Strategy", 700, 39000],
    ["2023-03-12", "Game G", "Switch", "North America", "Adventure", 1400, 68000],
    ["2023-04-08", "Game H", "Xbox", "Asia", "Sports", 800, 41000],
    ["2023-04-08", "Game I", "PC", "South America", "Action", 600, 31000],
    ["2023-05-20", "Game J", "PS4", "North America", "RPG", 1500, 72000],
    ["2023-02-15", "Game K", "PC", "North America", "Strategy", 1300, 56200],
    ["2023-02-15", "Game L", "PS4", "North America", "Strategy", 700, 34900],
    ["2023-02-15", "Game M", "PC", "North America", "Action", 1100, 48100],
    ["2023-02-15", "Game N", "PC", "Europe", "Strategy", 1800, 78100],
    ["2023-02-15", "Game O", "Xbox", "North America", "RPG", 1000, 51600],
    ["2023-02-15", "Game P", "Xbox", "Asia", "Adventure", 1100, 57700],
    ["2023-02-15", "Game Q", "PC", "North America", "Racing", 800, 36500],
    ["2023-02-15", "Game R", "Xbox", "North America", "Strategy", 1900, 91300],
    ["2023-03-12", "Game S", "Switch", "North America", "Puzzle", 1400, 75100],
    ["2023-03-12", "Game T", "Xbox", "Europe", "Strategy", 700, 28300],
    ["2023-03-12", "Game U", "Xbox", "North America", "RPG", 1200, 63700],
    ["2023-03-12", "Game V", "Switch", "Asia", "Racing", 1600, 67700],
    ["2023-03-12", "Game W", "Xbox", "Europe", "Strategy", 1300, 66400],
    ["2023-03-12", "Game X", "PS4", "Europe", "Adventure", 1900, 87800],
    ["2023-03-12", "Game Y", "PS4", "Asia", "RPG", 600, 25800],
    ["2023-03-12", "Game Z", "Xbox", "South America", "Sports", 700, 31000],
    ["2023-03-12", "Game AA", "Xbox", "Europe", "Strategy", 2000, 92700],
    ["2023-04-08", "Game AB", "PS4", "Asia", "Adventure", 1200, 62000],
    ["2023-04-08", "Game AC", "Xbox", "South America", "Puzzle", 1700, 76800],
    ["2023-04-08", "Game AD", "PS4", "South America", "Action", 600, 31900],
    ["2023-04-08", "Game AE", "PS4", "Europe", "RPG", 1800, 88300],
    ["2023-04-08", "Game AF", "Switch", "South America", "Puzzle", 1900, 91600],
    ["2023-04-08", "Game AG", "PC", "North America", "Strategy", 1300, 68100],
    ["2023-04-08", "Game AH", "PC", "Asia", "Racing", 1000, 47000],
    ["2023-04-08", "Game AI", "Xbox", "Europe", "Puzzle", 800, 42800],
    ["2023-04-08", "Game AJ", "PS4", "Europe", "Sports", 1000, 48800],
    ["2023-05-20", "Game AK", "PC", "Asia", "Racing", 500, 21000],
    ["2023-05-20", "Game AL", "Xbox", "Europe", "Action", 1200, 65700],
    ["2023-05-20", "Game AM", "PC", "North America", "Strategy", 2000, 106100],
    ["2023-05-20", "Game AN", "PS4", "Europe", "Strategy", 2000, 96200],
    ["2023-05-20", "Game AO", "Xbox", "South America", "Adventure", 1100, 56500],
    ["2023-05-20", "Game AP", "Switch", "Asia", "Racing", 1900, 78200],
    ["2023-05-20", "Game AQ", "PS4", "North America", "Sports", 500, 25300],
    ["2023-05-20", "Game AR", "PS4", "Europe", "Action", 700, 35700],
    ["2023-05-20", "Game AS", "PS4", "North America", "Action", 1500, 62300],
    ["2023-06-14", "Game AT", "PS4", "Asia", "Strategy", 2000, 86800],
    ["2023-06-14", "Game AU", "PS4", "South America", "Adventure", 2000, 104600],
    ["2023-06-14", "Game AV", "PS4", "North America", "Action", 1800, 81600],
    ["2023-06-14", "Game AW", "Switch", "South America", "RPG", 600, 30100],
    ["2023-06-14", "Game AX", "PC", "South America", "Strategy", 1500, 78100],
    ["2023-06-14", "Game AY", "PS4", "Europe", "Adventure", 1900, 80400],
    ["2023-06-14", "Game AZ", "PS4", "Asia", "Racing", 1200, 63700],
    ["2023-06-14", "Game BA", "Switch", "North America", "Action", 500, 20800],
    ["2023-06-14", "Game BB", "PS4", "South America", "Racing", 2000, 86600],
    ["2023-07-09", "Game BC", "PC", "Europe", "Racing", 500, 23400],
    ["2023-07-09", "Game BD", "Switch", "Asia", "Racing", 2000, 84300],
    ["2023-07-09", "Game BE", "Xbox", "Europe", "Action", 600, 31100],
    ["2023-07-09", "Game BF", "PC", "North America", "Puzzle", 2000, 96800],
    ["2023-07-09", "Game BG", "PS4", "North America", "Puzzle", 700, 37300],
    ["2023-07-09", "Game BH", "PC", "North America", "Strategy", 1200, 55300],
    ["2023-07-09", "Game BI", "PS4", "North America", "Puzzle", 700, 33100],
    ["2023-07-09", "Game BJ", "Xbox", "Asia", "Adventure", 1500, 64900],
    ["2023-07-09", "Game BK", "Switch", "Europe", "Strategy", 1400, 66300],
    ["2023-08-22", "Game BL", "PC", "North America", "Racing", 800, 33600],
    ["2023-08-22", "Game BM", "PS4", "Asia", "Adventure", 1600, 86500],
    ["2023-08-22", "Game BN", "PS4", "Asia", "Sports", 1000, 47800],
    ["2023-08-22", "Game BO", "Xbox", "North America", "Strategy", 1400, 75700],
    ["2023-08-22", "Game BP", "PS4", "Asia", "Action", 800, 41600],
    ["2023-08-22", "Game BQ", "PS4", "Asia", "Sports", 1100, 56600],
    ["2023-08-22", "Game BR", "PS4", "Asia", "Puzzle", 2000, 88000],
    ["2023-08-22", "Game BS", "PC", "South America", "RPG", 1300, 52000],
    ["2023-08-22", "Game BT", "Xbox", "Europe", "Strategy", 1300, 55300],
    ["2023-09-17", "Game BU", "Switch", "North America", "Action", 700, 38000],
    ["2023-09-17", "Game BV", "PC", "Asia", "Puzzle", 900, 41600],
    ["2023-09-17", "Game BW", "PC", "Asia", "Sports", 600, 32900],
    ["2023-09-17", "Game BX", "PS4", "Europe", "Strategy", 800, 36800],
    ["2023-09-17", "Game BY", "Switch", "Europe", "Adventure", 1000, 52200],
    ["2023-09-17", "Game BZ", "Switch", "North America", "Adventure", 1500, 78600],
    ["2023-09-17", "Game CA", "PS4", "Asia", "Adventure", 800, 36800],
    ["2023-09-17", "Game CB", "Switch", "Europe", "Adventure", 1900, 85900],
    ["2023-09-17", "Game CC", "PS4", "Europe", "Action", 1100, 51100],
    ["2023-10-05", "Game CD", "Xbox", "North America", "RPG", 1300, 59300],
    ["2023-10-05", "Game CE", "Switch", "Asia", "Action", 800, 43600],
    ["2023-10-05", "Game CF", "PS4", "Asia", "Action", 800, 39800],
    ["2023-10-05", "Game CG", "Xbox", "Asia", "Racing", 800, 37700],
    ["2023-10-05", "Game CH", "PS4", "Asia", "Action", 1800, 72800],
    ["2023-10-05", "Game CI", "PS4", "Asia", "Racing", 700, 35500],
    ["2023-10-05", "Game CJ", "Xbox", "North America", "Strategy", 1400, 67600],
    ["2023-10-05", "Game CK", "Switch", "Asia", "Racing", 1400, 67400],
    ["2023-10-05", "Game CL", "PS4", "South America", "Strategy", 1700, 85200],
    ["2023-11-11", "Game CM", "Xbox", "South America", "Puzzle", 500, 22400],
    ["2023-11-11", "Game CN", "PS4", "South America", "RPG", 1500, 71200],
    ["2023-11-11", "Game CO", "Switch", "Europe", "Puzzle", 2000, 104200],
    ["2023-11-11", "Game CP", "PC", "Asia", "Puzzle", 1500, 61800],
    ["2023-11-11", "Game CQ", "Xbox", "Europe", "RPG", 1100, 46200],
    ["2023-11-11", "Game CR", "PC", "Europe", "Racing", 700, 33500],
    ["2023-11-11", "Game CS", "PS4", "South America", "Racing", 1700, 73300],
    ["2023-11-11", "Game CT", "PC", "North America", "RPG", 1800, 77600],
    ["2023-11-11", "Game CU", "Switch", "North America", "Puzzle", 1200, 64900],
    ["2023-12-03", "Game CV", "Switch", "Europe", "RPG", 1900, 95800],
]

genre_totals = {}

for each_game in sales_data:
    genre = each_game[4]
    units = each_game[5]
    genre_totals[genre] = genre_totals.get(genre, 0) + units
plt.pie(genre_totals.values(), labels=genre_totals.keys(), autopct="%1.1f%%")
plt.title("Share of Units Sold by Genre")
plt.show()


genre_revenue = {}

for each_game in sales_data:
    genre = each_game[4]  # Genre column
    revenue = each_game[6]  # Revenue column

    genre_revenue[genre] = genre_revenue.get(genre, 0) + revenue

# Find highest earning genre
top_genre = max(genre_revenue, key=genre_revenue.get)

print("Revenue by genre:")
print(genre_revenue)

print("\nGenre with the highest revenue:")
print(top_genre, "-", "$" + str(genre_revenue[top_genre]))

# Optional graph
plt.figure()
plt.bar(genre_revenue.keys(), genre_revenue.values())
plt.xticks(rotation=45)
plt.title("Revenue by Genre")
plt.ylabel("Revenue ($)")
plt.show()
