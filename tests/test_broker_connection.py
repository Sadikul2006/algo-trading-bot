from broker.groww_client import GrowwClient

if __name__ == "__main__":
    print("Connecting to Groww API...")

    try:
        client = GrowwClient()
        print("✅ Connection successful!\n")

        print("Fetching profile...")
        profile = client.get_profile()
        print(profile)

        print("\nFetching holdings...")
        holdings = client.get_holdings()
        print(holdings)

        print("\nFetching positions...")
        positions = client.get_positions()
        print(positions)

    except Exception as e:
        print(f"❌ Something went wrong: {e}")