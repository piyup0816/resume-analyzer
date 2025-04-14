import os
from dotenv import load_dotenv
import openai

# Load variables from .env
load_dotenv()

# Set the API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")
