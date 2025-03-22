SCRAPE_URLS = {
    # Latest CVE data (JSON) from CIRCL
    "cve": "https://cve.circl.lu/api/last",
    # US-CERT alerts page (HTML)
    "reports": "https://www.us-cert.gov/ncas/alerts",
    # Reddit NetSec subreddit for forum posts (HTML)
    "forums": "https://www.reddit.com/r/netsec/"
}
# OpenAI API key for GPT-based advisory generation
OPENAI_API_KEY = "your_openai_api_key_here"  # Replace with your actual OpenAI API key

# Sentence Transformer model for generating embeddings
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

FAISS_INDEX_FILE = "faiss_index.index"
