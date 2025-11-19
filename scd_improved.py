# The Plan is to make my own functions that make the ploting process quicker and simpler to read the code. 
# The only issue is, the new modified module will need to be quick as it is now using an inbetween. 
# Speed may not always be the problem but it always could be


### PROJECT DEBRIEF ###
"""
load_data() is a simple loader that reads your dataset and returns it in a usable structure

plot_positive_reviews() A dedicated visualizer for positive review counts

add_horizontal_guidelines() Draws visual guide lines behind the bars

configure_xticks() Standardizes the layout of long labels

prepare_dataframe() Creates calculatedcolumns once so you don't repeat work

save_plot() Outputs your graph as an image file

analyze correlations() Produces summary numbers you may want to print later

main() The orchestrator of the entire program

validate_columns() Protects you against wrong CSV structure

generate_readme_info() Collects metadata about the project to help populate github README's
"""

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

