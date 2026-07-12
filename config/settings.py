import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()


class Settings:
    """
    Centralized configuration class.
    All required environment variables are loaded here,
    and the rest of the codebase imports from this single source.
    """

    GROWW_API_KEY: str = os.getenv("GROWW_API_KEY", "")
    GROWW_API_SECRET: str = os.getenv("GROWW_API_SECRET", "")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

    TELEGRAM_BOT_TOKEN: str = os.getenv("TELEGRAM_BOT_TOKEN", "")
    TELEGRAM_CHAT_ID: str = os.getenv("TELEGRAM_CHAT_ID", "")

    @classmethod
    def validate(cls) -> None:
        """
        Ensures all required values are set in the .env file.
        If anything is missing, the program fails immediately
        with a clear error message (fail-fast principle).
        """
        missing = []
        if not cls.GROWW_API_KEY:
            missing.append("GROWW_API_KEY")
        if not cls.GROWW_API_SECRET:
            missing.append("GROWW_API_SECRET")

        if missing:
            raise ValueError(
                f"Missing required environment variables: {', '.join(missing)}. "
                f"Please check your .env file."
            )


# Singleton instance, so other files can import it directly
settings = Settings()