import streamlit as st
# from langchain.chat_models import ChatOpenAI
# from langchain.schema import SystemMessage, HumanMessage
from langchain.llms import OpenAI, OpenAIChat
# import os
# os.environ["OPENAI_API_KEY"]


st.title("献立づくりチャットボット")

st.write("センス抜群の私めが、お料理を提案いたしましょう！")

# =======　サイドバー　=======

st.sidebar.write("条件")

genre = st.sidebar.selectbox(
    "ジャンルは？",
    list(["","和食","中華","洋食","イタリアン"])
    )

type = st.sidebar.selectbox(
    "味のタイプは？",
    list(["","さっぱり","がっつり","こってり","とにかく美味い"])
    )

mood = st.sidebar.text_area("今の気分は？")

condition = st.sidebar.slider("今のお腹の空き具合は？", 0, 10, 5)

# =======　メインエリア　=======

# "ジャンル：", genre
# "味のタイプ：", type
# "今の気分：", mood
# "お腹の空き具合：", condition

# =======　コード　=======
if st.sidebar.button("生成"):
    # chat = ChatOpenAI(model_name="gpt-4")
    # result = chat([
    #     SystemMessage(content="あなたはセンス抜群の料理人。与えられた条件でレシピを考案し、料理名とレシピを日本語で回答しなさい。"),
    #     HumanMessage(content="食べたい料理の条件は、ジャンルが{genre}、味のタイプが{type}。今の気分は{mood}で、今のお腹の空き具合は、最大を10とすると{condition}くらい")
    #     ])

    chat = OpenAIChat(model_name="gpt-4")
    result = chat(f"""
        あなたはセンス抜群の料理人です。
        {condition}/10くらいお腹が空いている{mood}という気分のお客様が、{type}系の{genre}が食べたいと言っています。
        このお客様にふさわしい料理のレシピを考案し、料理名と超簡単なレシピを日本語で回答しなさい。
        """)

    st.write(f"腹{10-condition}分目のあなたにはこの料理を提案します。")
    st.write("   =================   ")
    st.write(result)
