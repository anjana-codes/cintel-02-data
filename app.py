import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins #This package provides Palmer Penguins Dataset

#Use the built-in function to load Palmer Penguins Dataset
penguins_df= palmerpenguins.load_penguins()

ui.page_opts(title="Penguins Data - Anjana", fillable=True)
with ui.layout_columns():

    @render_plotly
    def plot1():
        return px.histogram(px.data.tips(), y="tip")
        

    @render_plotly
    def plot2():
        return px.histogram(px.data.tips(), y="total_bill")
