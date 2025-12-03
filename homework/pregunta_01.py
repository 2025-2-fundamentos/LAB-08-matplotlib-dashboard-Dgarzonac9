# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""
import pandas as pd
import os
import matplotlib.pyplot as plt


def create_visual_for_shippin_per_warehouse(df):
    df = df.copy()
    plt.figure()
    counts = df.Warehouse_block.value_counts()
    counts.plot.bar(
        title="Envios por Warehouse Block",
        xlabel="Warehouse Block",
        ylabel="Record count",
        color="tab:blue",
        fontsize=8,
    )
    save_path = "docs/shipping_per_warehouse.png"
    plt.tight_layout()
    plt.savefig(save_path)
    
def create_visual_for_mode_of_shipment(df):
    df = df.copy()
    plt.figure()
    counts = df.Mode_of_Shipment.value_counts()
    counts.plot.pie(
        title="Envios por Mode of Shipment",
        wedgeprops=dict(width=0.35),
        ylabel="",
        colors=["tab:blue", "tab:orange", "tab:green"],
    )
    save_path = "docs/mode_of_shipment.png"
    plt.tight_layout()
    plt.savefig(save_path)

def create_visual_for_customer_rating(df):
    df = df.copy()
    plt.figure()
    df = (
        df[["Mode_of_Shipment", "Customer_rating"]]
        .groupby("Mode_of_Shipment")
        .describe()
    )
    df.columns = df.columns.droplevel()
    df = df[["mean", "min", "max"]]
    plt.barh(
        y=df.index.values,
        width=df["max"].values - 1,
        left=df["min"].values,
        height=0.9,
        color="lightgray",
        alpha=0.8,
    )
    colors = [
        "tab:green" if value >=3.0 else "tab:orange" for value in df["mean"].values
    ]
    plt.barh(
        y=df.index.values,
        width=df["mean"].values - 1,
        left= df["min"].values,
        color=colors,
        height=0.5,
        alpha=1.0,
    )
    plt.title("Avarage Customer Rating")
    plt.gca().spines["left"].set_color("gray")
    plt.gca().spines["bottom"].set_color("gray")
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)

    plt.tight_layout()
    save_path = "docs/average_customer_rating.png"
    plt.savefig(save_path)


def create_visual_for_weight_in_gms(df):
    df = df.copy()
    plt.figure()
    df.Weight_in_gms.plot.hist(
        title="Weight in gms distribution",
        color="tab:orange",
        edgecolor="black",
    )
    plt.gca().spines["left"].set_visible(False)
    plt.gca().spines["bottom"].set_visible(False)

    plt.tight_layout()
    save_path = "docs/weight_distribution.png"
    plt.savefig(save_path)

def write_html_dashboard():
    html_content = """
    <html>
    <head>
        <title>Shipping Data Dashboard</title>
    </head>
    <body>
        <h1>Shipping Data Dashboard</h1>
        <div style="width:45%; float:left;">
            <img src="shipping_per_warehouse.png" alt="Envios por Warehouse Block" style="width:100%;">
            <img src="mode_of_shipment.png" alt="Envios por Mode of Shipment" style="width:100%;">
        </div>
        <div style="width:45%; float:left;">
            <img src="average_customer_rating.png" alt="Average Customer Rating" style="width:100%;">
            <img src="weight_distribution.png" alt="Weight in gms distribution" style="width:100%;">
        </div>
    </body>
    </html>
    """
    with open("docs/index.html", "w") as f:
        f.write(html_content)


def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """

    df = pd.read_csv("files/input/shipping-data.csv")

    os.makedirs("docs", exist_ok=True)
    create_visual_for_shippin_per_warehouse(df)
    create_visual_for_mode_of_shipment(df)
    create_visual_for_customer_rating(df)
    create_visual_for_weight_in_gms(df)
    write_html_dashboard()

if "__main__" == __name__:
    pregunta_01()