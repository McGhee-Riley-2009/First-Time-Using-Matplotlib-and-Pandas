import matplotlib.pyplot as plt
import pandas as pd


def load_data(csv_name):
    df = pd.read_csv(csv_name)
    return df

def set_window_size(width, height):
    plt.figure(figsize=(width, height))


def plot_certain_columns(chosen_df, x_column, y_column):
    plt.bar(chosen_df[x_column], chosen_df[y_column])

def horizontal_guidelines(chosen_df, y_column, guideline_gap):
    max_val = int(chosen_df[y_column].max()) + 2
    for y in range (0, max_val +guideline_gap, guideline_gap):
        plt.axhline(y, linestyle="--", linewidth=0.7, color="red")

def set_labels(title, x_label="x-axis", y_label="y-axis"):
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

def xticks_config(degrees, horizontal_alignment="right"):
    plt.xticks(rotation=degrees, ha=horizontal_alignment)

def show_plot():
    plt.tight_layout()
    plt.show()
