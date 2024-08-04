from tasks import Product_search,classification_of_products
from agents import sse,recommendor
from crewai import Crew
from crewai import Process
import streamlit as st

# sse=CustomAgents.senior_sales_executive()
sse=sse
# sp=CustomTasks.search_product(agent=sse,product="Nike Jordan Air 1")
Product_search=Product_search

def get_crew_response(Product):
    crew=Crew(
        agents=[sse,recommendor],
        tasks=[Product_search,classification_of_products],
        process=Process.sequential,
        full_output=True,
        
    )

    res=crew.kickoff(inputs={'product':{Product}})
    return res

def main():
    st.set_page_config(
        page_title="ShopAIssistant",
        page_icon="z6u3pfnl.png"
        
    )
    st.image("z6u3pfnl.png")
    user_input = st.text_input("Enter product details")
    if st.button("Generate"):
        response=get_crew_response(user_input)
        st.write(response)
        print(response)
    # user_input = input("Enter product details")
    # response=get_crew_response(user_input)
    # print(response)



if __name__=="__main__":
    main()
