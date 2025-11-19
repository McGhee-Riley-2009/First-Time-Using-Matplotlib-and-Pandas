import improved_module_scd as ims

ims.set_window_size(20, 10)
df = ims.load_data("SteamData.csv")

ims.horizontal_guidelines(df, "negative_reviews", 10000)

ims.plot_certain_columns(df, "game", "positive_reviews")
ims.show_plot()

ims.plot_certain_columns(df, "game", "negative_reviews")

ims.set_labels("Games sorted by reviews")
ims.xticks_config(15)
ims.show_plot()


