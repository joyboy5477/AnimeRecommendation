from secret_key import openapi_key
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
from langchain.chains import LLMChain

import os

os.environ["OPENAI_API_KEY"] = openapi_key

llm = OpenAI(temperature=0.6)


def animeandplot(genre):
    # genre chain 1
    suggest_anime_name = PromptTemplate(
        input_variables=["genre"],
        template="Suggest a best {genre} anime name."
    )

    anime_name = LLMChain(llm=llm, prompt=suggest_anime_name, output_key="anime_name")

    # desc chain 2
    plot = PromptTemplate(
        input_variables=["anime_name"],
        template="""Plot of {anime_name} anime."""
    )

    story = LLMChain(llm=llm, prompt=plot, output_key="desc")

    chain = SequentialChain(
        chains=[anime_name, story],
        input_variables=["genre"],
        output_variables=["anime_name", "desc"],
        verbose=True
    )
    response = chain({"genre": "Isekai"})
    return response


if __name__ == "main":
    print(animeandplot("Isekai"))
