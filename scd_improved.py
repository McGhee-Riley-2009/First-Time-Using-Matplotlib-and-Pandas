import custom_module as cm

cm.set_window_size(20, 10)
df = cm.load_data("SteamData.csv")

cm.horizontal_guidelines(df, "negative_reviews", 10000)

cm.plot_certain_columns(df, "game", "positive_reviews")
cm.show_plot()

cm.plot_certain_columns(df, "game", "negative_reviews")

cm.set_labels("Games sorted by reviews")
cm.xticks_config(15)
cm.show_plot()



