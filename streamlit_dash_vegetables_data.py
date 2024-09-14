import streamlit as st
import pandas as pd
import plotly.express as px

# CSVファイルの読み込み（アップロードされたファイルを使用）
df = pd.read_csv('./data/市場別/2015-2024_rev2.csv')

# 日付列をdatetime型に変換
df['日付'] = pd.to_datetime(df['日付'])

# タイトル
st.title("複数の野菜を比較するダッシュボード")

# 都市の選択
city = st.selectbox('都市を選択してください', df['都市名'].unique())

# 複数の野菜を選択
selected_items = st.multiselect('比較する品目を選択してください', df['品目名'].unique())

# フィルタリングされたデータ
filtered_data = df[(df['都市名'] == city) & (df['品目名'].isin(selected_items))]

# フィルタリングされたデータを表示
st.write(f"選択された都市: {city}")
st.write(filtered_data)

if not selected_items:
    st.warning("比較する品目を選んでください。")
else:
    # Plotlyを使って数量と価格の折れ線グラフを作成
    fig_quantity = px.line(filtered_data, x='日付', y='数量', color='品目名',
                           title=f'{city}の選択された品目の数量推移',
                           hover_data=['日付', '数量', '価格'])
    fig_price = px.line(filtered_data, x='日付', y='価格', color='品目名',
                        title=f'{city}の選択された品目の価格推移',
                        hover_data=['日付', '数量', '価格'])

    # グラフをStreamlitで表示
    st.plotly_chart(fig_quantity)
    st.plotly_chart(fig_price)
