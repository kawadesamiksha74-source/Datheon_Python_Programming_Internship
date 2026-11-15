import csv
from datetime import datetime

GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BOLD = "\033[1m"


def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print(RED + "Please enter a number greater than 0." + RESET)
                continue
            return value
        except ValueError:
            print(RED + "Invalid input. Enter a valid number." + RESET)


def main():

    print("\n" + CYAN + "=" * 65 + RESET)
    print(BOLD + GREEN + "          STOCK PORTFOLIO PERFORMANCE TRACKER" + RESET)
    print(BOLD + YELLOW + "                   INVESTMENT DASHBOARD" + RESET)
    print(CYAN + "=" * 65 + RESET)

    print("\nEnter your stock investment details below.")
    print(YELLOW + "Note: Enter the latest market price manually.\n" + RESET)

    portfolio = []

    while True:

        ticker = input("Stock ticker symbol: ").strip().upper()

        if not ticker:
            print(RED + "Ticker cannot be empty." + RESET)
            continue

        buy_price = get_positive_number("Buy price per share: ")
        quantity = get_positive_number("Number of shares: ")
        current_price = get_positive_number("Current market price: ")

        invested = buy_price * quantity
        market_value = current_price * quantity
        gain_loss = market_value - invested
        percentage = (gain_loss / invested) * 100

        portfolio.append({
            "ticker": ticker,
            "buy_price": buy_price,
            "quantity": quantity,
            "current_price": current_price,
            "invested": invested,
            "market_value": market_value,
            "gain_loss": gain_loss,
            "gain_loss_percent": percentage
        })

        print(GREEN + "\nStock added successfully!" + RESET)

        more = input("\nAdd another stock? (y/n): ").strip().lower()

        if more != "y":
            break

        print()

    total_invested = sum(x["invested"] for x in portfolio)
    total_value = sum(x["market_value"] for x in portfolio)
    total_profit = total_value - total_invested
    total_percentage = (total_profit / total_invested) * 100

    print("\n" + CYAN + "=" * 95 + RESET)
    print(BOLD + "                    PORTFOLIO PERFORMANCE REPORT" + RESET)
    print(CYAN + "=" * 95 + RESET)

    print(
        f"{'STOCK':<10}{'BUY PRICE':>13}{'SHARES':>10}"
        f"{'CURRENT':>13}{'INVESTED':>15}{'VALUE':>15}{'P/L %':>12}"
    )

    print("-" * 95)

    for item in portfolio:

        color = GREEN if item["gain_loss"] >= 0 else RED

        print(
            f"{item['ticker']:<10}"
            f"{item['buy_price']:>13.2f}"
            f"{item['quantity']:>10g}"
            f"{item['current_price']:>13.2f}"
            f"{item['invested']:>15.2f}"
            f"{item['market_value']:>15.2f}"
            + color + f"{item['gain_loss_percent']:>11.2f}%" + RESET
        )

    print("-" * 95)

    print(BOLD + CYAN + "\n                PORTFOLIO SUMMARY" + RESET)
    print("-" * 45)

    print(f"Total Investment      : {total_invested:.2f}")
    print(f"Current Portfolio Value: {total_value:.2f}")

    if total_profit >= 0:
        print(GREEN + f"Total Profit           : +{total_profit:.2f}" + RESET)
    else:
        print(RED + f"Total Loss             : {total_profit:.2f}" + RESET)

    print(f"Overall Return         : {total_percentage:.2f}%")

    filename = "portfolio_summary.csv"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, "w", newline="", encoding="utf-8") as file:

        fields = [
            "timestamp", "ticker", "buy_price", "quantity",
            "current_price", "invested", "market_value",
            "gain_loss", "gain_loss_percent"
        ]

        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()

        for item in portfolio:
            row = {"timestamp": timestamp}
            row.update(item)
            writer.writerow(row)

        writer.writerow({
            "timestamp": timestamp,
            "ticker": "TOTAL",
            "buy_price": "",
            "quantity": "",
            "current_price": "",
            "invested": round(total_invested, 2),
            "market_value": round(total_value, 2),
            "gain_loss": round(total_profit, 2),
            "gain_loss_percent": round(total_percentage, 2)
        })

    print(CYAN + "\n" + "=" * 65 + RESET)
    print(GREEN + BOLD + "       PORTFOLIO REPORT SAVED SUCCESSFULLY!" + RESET)
    print(YELLOW + f"       File: {filename}" + RESET)
    print(CYAN + "=" * 65 + RESET)

    print("\n" + YELLOW + "Thank you for using Portfolio Tracker!" + RESET)
    print("Note: This is a learning tool, not financial advice.")


if __name__ == "__main__":
    main()
