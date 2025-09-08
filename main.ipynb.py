import marimo

__generated_with = "0.15.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd   # make sure this is at the top of your notebook

    # If your file is named 'std_rez.xlsx'
    df = pd.read_excel("std_rez.xlsx")

    # Show first 5 rows
    df.head()
    return (df,)


@app.cell
def _(df):
    df.sort_values("Age")  
    df.head()
    return


if __name__ == "__main__":
    app.run()
