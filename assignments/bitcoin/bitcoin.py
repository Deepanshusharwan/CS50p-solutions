import requests
import sys


def main():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        current_price = response.json()["bpi"]["USD"]["rate_float"]

    except requests.RequestException:
        sys.exit("There was a problem connecting to the server")

    if len(sys.argv) == 1:
        sys.exit("Please provide a valid argument.")

    try:
        count = float(sys.argv[1])
    except ValueError:
        sys.exit("Please provide a valid argument")

    amount = count * current_price
    print(f"${amount:,.4f}")


if __name__ == "__main__":
    main()
