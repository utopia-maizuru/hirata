# Streamlitライブラリをインポート
import streamlit as st

# 乱数に関するライブラリをインポート
import random

# ページ設定（タブに表示されるタイトル、表示幅）
st.set_page_config(page_title="タイトル", layout="wide")

# タイトルを設定
st.title("おみくじアプリ")

if  st.button("おみくじを引く"):
    results = ["大吉","中吉","小吉","吉","凶","大凶"]
    result = random.choice(results)
    st.write(f"結果:{result}")

    # 結果に応じたコメント
    comments = {
        "大吉":"いい一日になるでしょう",
        "大凶":"外に出ないでください"
    }
comment = comments[result]

