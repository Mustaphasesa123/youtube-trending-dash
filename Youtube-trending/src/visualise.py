import matplotlib.pyplot as plt
from collections import Counter


def plot_category_pie(data: list[dict]) -> None:
    counts = Counter(row.get("category_id", 0) for row in data)
    labels = [str(k) for k in counts.keys()]
    sizes = list(counts.values())

    plt.figure()
    plt.title("Video Distribution by Category")
    plt.pie(sizes, labels=labels, autopct="%1.1f%%")
    plt.show()


def plot_histogram(data: list[dict], metric: str) -> None:
    if metric not in {"views", "likes", "comment_count"}:
        raise ValueError("Metric must be: views, likes, comment_count")

    values = [int(row.get(metric, 0)) for row in data]

    plt.figure()
    plt.title(f"Histogram of {metric}")
    plt.xlabel(metric)
    plt.ylabel("Frequency")
    plt.hist(values, bins=20)
    plt.show()