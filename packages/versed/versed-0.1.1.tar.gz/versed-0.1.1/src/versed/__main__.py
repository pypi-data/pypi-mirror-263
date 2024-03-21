import requests
import typer
import os

app = typer.Typer()


@app.command()
def init():
    if os.path.exists(".versed"):
        print("Versed configuration has already been initialized.")
    else:
        with open(".versed", "w") as f:
            pass
        print("Initialized new Versed configuration file.")


@app.command()
def select_verse(scripture_reference: str):
    url_str = f"https://api.esv.org/v3/passage/text/?q={scripture_reference.replace(' ', '+')}"
    if os.path.exists(".versed"):
        with open(".versed", "r") as f:
            token = f.read()
        headers = {"Authorization": token}
        res = requests.get(url=url_str, headers=headers)
        print(res.text)
    else:
        print(
            "No Versed configuration found. Please run python -m versed init and put your API token in the .versed configuration file that is created"
        )


if __name__ == "__main__":
    app()
