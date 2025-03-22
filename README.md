# CyberBot
Cybersecurity Threat Intelligence Bot

# Cybersecurity Threat Intelligence Bot

A cutting-edge, agentic cybersecurity threat intelligence bot using a Retrieval-Augmented Generation (RAG) pipeline. This project combines real-time data scraping from CVE feeds, US-CERT alerts, and Reddit posts with advanced vector retrieval (FAISS) and GPT‑4 advisory generation. The sleek, responsive interface built with Flask and Bootstrap provides a live threat dashboard and generates actionable security advisories.

## Features

- **Real-Time Data Collection:** 
  - **CVE Data:** Scrapes the latest CVEs via the CIRCL API.
  - **US-CERT Alerts:** Parses recent security alerts.
  - **Reddit Posts:** Retrieves posts from the NetSec subreddit.
- **Retrieval-Augmented Generation (RAG):** 
  - Combines vector search and GPT‑4 to generate detailed security advisories.
- **Vector Database with FAISS:** 
  - Efficiently stores and retrieves semantic embeddings.
- **Agent Collaboration:** 
  - Background agents continuously collect and process data.
- **Modern Web Interface:** 
  - A responsive, Bootstrap-enhanced dashboard to query and visualize threat data.

## Installation
1. **Clone the Repository:**
   ```bash
   git clone <your_repository_url>
   cd cybersec_agent

2. **Install Dependencies:**
  ```bash
pip install -r requirements.txt
  ```

3. **Open config.py and replace "your_openai_api_key_here" with your actual OpenAI API key.**

4. **Run the Application:**
  ```bash
  python main.py
  ```
Then open your browser and navigate to http://127.0.0.1:5000 to access the dashboard.

## Usage
  **Threat Advisory:**
  - Enter a query (e.g., "latest vulnerability in XYZ") into the input field and click the Generate Advisory button to receive a detailed security advisory along with an assessment of threat severity.

  **Threat Dashboard:
  - View the most recent data entries scraped from various sources in the real-time dashboard.


