import seaborn as sns

from tabulate import tabulate


def plot_countplot(series_):
    """
    https://stackoverflow.com/questions/46623583/seaborn-countplot-order-categories-by-count
    :param series_:
    :return:
    """
    sns.set_style("whitegrid", {'axes.grid': False})
    headers = [series_.name, 'Count', 'Percentage']
    value_counts = series_.value_counts()
    value_counts_norm = series_.value_counts(normalize=True)
    table = [[
        v, value_counts[v], round(value_counts_norm[v], 3)
    ] for v in value_counts.index]
    print(tabulate(table, headers, tablefmt="psql"))
    sns.countplot(y=series_, orient='horizontal', order=value_counts.index)
