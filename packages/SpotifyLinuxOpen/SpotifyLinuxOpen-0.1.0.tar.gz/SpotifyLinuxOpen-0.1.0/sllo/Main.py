from sllo.Classes import Interface


def main() -> None:
    interface = Interface()
    try:
        interface.open()
    except ValueError as error:
        print(f"\n{error}")
        interface.help()


if __name__ == "__main__":
    main()
