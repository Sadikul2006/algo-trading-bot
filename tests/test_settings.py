from config.settings import settings

def mask(value: str) -> str:
    """
    Masks a sensitive string, showing only the first 4 characters.
    Used so we never print full secrets, even during testing.
    """
    if not value:
        return "NOT SET"
    return value[:4] + "*" * (len(value) - 4)


if __name__ == "__main__":
    print("Testing settings.py configuration...")
    print(f"ENVIRONMENT: {settings.ENVIRONMENT}")
    print(f"GROWW_API_KEY: {mask(settings.GROWW_API_KEY)}")
    print(f"GROWW_API_SECRET: {mask(settings.GROWW_API_SECRET)}")

    try:
        settings.validate()
        print("✅ All required settings are present.")
    except ValueError as e:
        print(f"❌ Validation failed: {e}")