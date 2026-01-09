import matplotlib.pyplot as plt

def plot_means(monthly_means, cities, years):
    city_monthly = (
        monthly_means[monthly_means["Miejscowość"].isin(cities)]
        .groupby(["Rok", "Miesiąc", "Miejscowość"])["Mean PM25"]
        .mean()
        .reset_index()
    )

    df = city_monthly[city_monthly["Rok"].isin(years)]
    df = df.pivot_table(
        values="Mean PM25",
        index="Miesiąc",
        columns=["Miejscowość", "Rok"]
    )

    plt.figure()
    for city in cities:
        for year in years:
            plt.plot(df.index, df[(city, year)], label=f"{city} {year}")

    plt.legend()
    plt.xlabel("Miesiąc")
    plt.ylabel("Średnia miesięczna wartość PM25")
    plt.title(
        "Trend średnich miesięcznych PM2.5 w Warszawie i Katowicach w latach 2014 i 2024"
    )
    plt.grid(True)
    plt.show()