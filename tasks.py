# "If you do your BEST WORK, I'll give you a $10,000 commission!"
from crewai import Task
from textwrap import dedent
from tools import serper_tool,scraper
from agents import sse,recommendor
Product_search=Task(
    description=dedent(
        """
    Search the internet for the below mentioned product and return links of the best matches
    
    If you do your BEST WORK, I'll give you a $10,000 commission!            

    Make sure to use the most recent data as possible.

    Search the following product: {product}
"""
    ),
    # expected_output="""return the top 5 best rated products available on the website:<WEBSITE>https://www.amazon.in/s?k=</WEBSITE>.
    # stop the code loop once 5 products have been provided""",
    expected_output="""return the top 5 best rated products available on the internet.
    stop the code loop once 5 products have been provided""",
    agent=sse,
    tools=[serper_tool],

)

classification_of_products=Task(
    description=dedent(
        """
    scrape the given websites and identify the cheapest 5 products and the bewt rated 5 products
    
    If you do your BEST WORK, I'll give you a $10,000 commission!      

    Make sure to use the most recent data as possible.

"""
    ),
    expected_output="""names of 5 best rated products form the given 15 products. """,
    agent=recommendor,
    tools=[scraper],
    # async_execution=True,

)