import streamlit as st
import pandas as pd
import altair as alt

st.header("Internetzugang: Frauen seltener online als Männer")
st.subheader("")

source = pd.DataFrame({
        'Anteil(%)': [69, 63],
        'Geschlecht': ['Männer', 'Frauen']
})
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Geschlecht:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    2022
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: Schätzung ITU")