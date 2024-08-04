from dotenv import load_dotenv
load_dotenv()
import os
import ollama
from crewai_tools import SerperDevTool,SeleniumScrapingTool,WebsiteSearchTool,ScrapeWebsiteTool


serper_tool=SerperDevTool()
# scraper=SeleniumScrapingTool()
scraper=ScrapeWebsiteTool()
# scraper=WebsiteSearchTool(
#     config=dict(
#         llm=dict(
#             provider="ollama", # or google, openai, anthropic, llama2, ...
#             config=dict(
#                 model="llama2",
#                 # temperature=0.5,
#                 # top_p=1,
#                 # stream=true,
#             ),
#         ),
#         embedder=dict(
#             provider="google", # or openai, ollama, ...
#             config=dict(
#                 model="models/embedding-001",
#                 task_type="retrieval_document",
#                 # title="Embeddings",
#             ),
#         ),
#     )
# )
