import streamlit as st
# from langchain.chat_models import ChatOpenAI
# from langchain.schema import SystemMessage, HumanMessage
from langchain.llms import OpenAI, OpenAIChat


st.title("献立提案AI　テスト")

st.write("料理センス抜群の私めが、一品提案いたしましょう。")

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

mood = st.sidebar.text_input("今の気分は？")

condition = st.sidebar.slider("今のお腹の空き具合は？", 0, 10, 5)

import os
os.environ["OPENAI_API_KEY"] = st.sidebar.text_input("OPENAIのAPI_KEYを入力してください", type="password")
# os.environ["OPENAI_API_KEY"] = st.sidebar.file_uploader("OPENAIのAPI_KEYのファイルを選んでください")

if st.sidebar.button("生成"):

    # =======　メインエリア　=======

    # "ジャンル：", genre
    # "味のタイプ：", type
    # "今の気分：", mood
    # "お腹の空き具合：", condition

    # =======　コード　=======

    # chat = ChatOpenAI(model_name="gpt-4")
    # result = chat([
    #     SystemMessage(content="あなたはセンス抜群の料理人。与えられた条件でレシピを考案し、料理名とレシピを日本語で回答しなさい。"),
    #     HumanMessage(content="食べたい料理の条件は、ジャンルが{genre}、味のタイプが{type}。今の気分は{mood}で、今のお腹の空き具合は、最大を10とすると{condition}くらい")
    #     ])


    chat = OpenAIChat(model_name="gpt-4")
    result = chat(f"""
        あなたはセンス抜群の料理人です。
        お腹の空き具合が10段階中{condition}で{mood}な気分のお客様が、{type}系の{genre}を食べたいと言っています。
        このお客様にふさわしい、かつ簡単に作れる料理のレシピを考案し、料理名とレシピを日本語で提案しなさい。
        """)

    st.write(f"あなたにはこの料理を提案します。")
    st.write("   =================   ")
    st.write(result)
