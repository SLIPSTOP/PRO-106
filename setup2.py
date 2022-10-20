import plotly.express as px
import csv
import numpy as np


def plotFigure(data_path):
    with open(data_path) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df, x="Coffee in ml", y="sleep in hours")
        fig.show()


def getDataSource(data_path):
    Coffee_in_ml = []
    sleep_in_hours = []
    with open(data_path) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            Coffee_in_ml.append(float(row["Coffee in ml"]))
            sleep_in_hours.append(float(row["sleep in hours"]))

    return {"x": Coffee_in_ml, "y": sleep_in_hours}


def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Coffee and Sleep is :", correlation[0, 1])


def setup():
    data_path = "data2.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)


setup()
