from crewai import Agent
from textwrap import dedent
from langchain_community.llms import Ollama
from tools import serper_tool,scraper

llm=Ollama(model="falcon2")

sse=Agent(
    role="Senior online sales executive",
    backstory=dedent("""20 years of experience as an online sales expert."""),
    goal=dedent(f"""Search the internet and return the top products matching the users description."""),
    tools=[serper_tool],
    allow_delegation=False,
    verbose=True,
    llm=llm,
    max_iter=5
)

recommendor=Agent(
    role="Product recommendor",
    goal=dedent("""scrape all the provided links by the senior sales executive and identify the cheapest 5 and best rated 5 products."""),
    backstory=dedent("""decades of experience as a product classifier."""),
    tools=[scraper],
    llm=llm,
    allow_delegation=False,
    verbose=True,
    max_iter=1
)