# Streamlitライブラリをインポート
import streamlit as st

# 乱数に関するライブラリをインポート
import random

# ページ設定（タブに表示されるタイトル、表示幅）
st.set_page_config(page_title="タイトル", layout="wide")


# レシピリスト
recipes = [
    "ハンバーガー",
    "チーズバーガー",
    "ダブルチーズバーガー",
    "チキンフィレオ",
    "照り焼きチキンフィレオ",
    "月見バーガー",
    "照り焼きバーガー",
    "マクポ",
    "エグチ",
    "チキチー",
    "フィッシュフィレオ",
    "エビシュリンプ",
    # 他にも好きなレシピを追加
]

# Streamlitアプリケーションのタイトルと説明
st.title("I love mac")
st.write("ランダムにマックのバーガーを提案します。")

# レシピをランダムに選択するボタン
if st.button("今日のハンバーガーを決める"):
    selected_recipe = random.choice(recipes)
    st.write(f"提案されたレシピ: {selected_recipe}")



