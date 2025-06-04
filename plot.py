import matplotlib.pyplot as plt

def plot_driver_points(df1, df2, name1, name2):
    plt.figure(figsize=(10, 6))

    plt.plot(df1['year'], df1['points'], marker='o', label=name1)
    plt.plot(df2['year'], df2['points'], marker='o', label=name2)

    plt.title("Season Points Comparison")
    plt.xlabel("Year")
    plt.ylabel("Points")
    plt.legend()
    plt.grid(True)

    for x, y in zip(df1['year'], df1['points']):
        plt.text(x, y, str(y), ha='right', va='bottom', fontsize=9)
    for x, y in zip(df2['year'], df2['points']):
        plt.text(x, y, str(y), ha='left', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.show()
