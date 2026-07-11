from data.historical_data import fetch_historical_data

if __name__ == "__main__":
    data = fetch_historical_data("RELIANCE", period="6mo", interval="1d")

    print(f"Total rows: {len(data)}")
    print("\nFirst 3 rows:")
    print(data.head(3))
    print("\nLast 3 rows:")
    print(data.tail(3))