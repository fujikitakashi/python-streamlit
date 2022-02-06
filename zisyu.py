import streamlit as st
import time

#個人作成
"""
# 資産形成計算
"""
slider=st.sidebar.slider('毎月の入金額(万円)',0,30,5)*12
r=st.sidebar.slider('年利(%)',0,10,5)
op=st.sidebar.slider('運用年年数(年)',1,30,5)
r=1+(r/100)
ii=[]
iii=[]
i=0

#資産運用した場合
for nuu in range(op):
    if i==0:
     ii.append(slider*r)
     i=i+1
    else :
       ii.append(round((slider+ii[i-1])*r,1))
       i=i+1

#資産運用しなかった場合
i=0
for nun in range(op):
    if i==0:
        iii.append(round(slider,1))
        i=i+1
    else:
        iii.append(round(slider+iii[i-1],1))
        i=i+1


""" ### 資産運用しなかった場合"""
st.area_chart(iii)
st.write(f'合計金額:{iii[-1]}万円')
""" ### 資産運用した場合"""
st.area_chart(ii)
st.write(f'合計金額:{ii[-1]}万円')

left_column,right_column=st.columns(2)
unyo_nasi=left_column.button('差額計算')
la=st.empty()
bar=st.progress(0)
ku=False

if unyo_nasi:
     for i in range(100):
      la.text(f'{i+1}%計算完了')
      bar.progress(i+1)
      time.sleep(0.02)
      if i+1==100:
          ku=True

if ku:
 st.write(f'{round(ii[-1]-iii[-1],1)}万円です')


