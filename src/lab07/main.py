from app import ApartmentApp
from cli import ApartmentCLI
from storage import load_apartments


STORAGE_PATH = "apartments.json"


def main() -> None:
    apartments = load_apartments(STORAGE_PATH)

    app = ApartmentApp(apartments)
    cli = ApartmentCLI(app, STORAGE_PATH)

    cli.run()


if __name__ == "__main__":
    main()