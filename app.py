import streamlit as st

st.set_page_config(page_title="Calculadora de Metas Trimestrais", layout="wide")
st.markdown("<h1 style='text-align: center;'>📊 Calculadora de Metas Trimestrais</h1>", unsafe_allow_html=True)

valor_mensal = st.number_input("Digite o valor mensal da meta:", min_value=0.0, step=100.0, format="%.2f")

# Pesos dos indicadores
pesos = {
    'Produção': 0.15,
    'Ticket Médio': 0.15,
    'Despesas': 0.15,
    'Satisfação Cliente': 0.275,
    'Pesquisa Clima': 0.0688,
    'Turnover': 0.0688,
    'ABS': 0.0688,
    'Treinamento': 0.0688
}

meses = ["Janeiro", "Fevereiro", "Março"]
colunas = st.columns(3)
indicadores_por_mes = []
total_perdido_geral = 0

for i, col in enumerate(colunas):
    with col:
        st.subheader(meses[i])
        indicadores = {}
        total_perdido_mes = 0

        for indicador, peso in pesos.items():
            valor_indicador = valor_mensal * peso
            chave = f"{indicador} ({meses[i]})"
            checked = st.checkbox(chave, value=True, key=chave)

            if checked:
                st.markdown(f"<span style='color: green;'>✅ R$ {valor_indicador:.2f}</span>", unsafe_allow_html=True)
            else:
                st.markdown(f"<span style='color: red;'>❌ R$ {valor_indicador:.2f}</span>", unsafe_allow_html=True)
                total_perdido_mes += valor_indicador

            indicadores[indicador] = checked

        indicadores_por_mes.append(indicadores)
        total_perdido_geral += total_perdido_mes
        st.markdown(f"<b>Total perdido em {meses[i]}:</b> <span style='color: red;'>R$ {total_perdido_mes:.2f}</span>", unsafe_allow_html=True)

# Botão para calcular valor final da meta
if st.button("Calcular"):
    valor_final = valor_mensal * 3 - total_perdido_geral
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:18px;'>💰 <b>Total perdido no trimestre:</b> <span style='color: red;'>R$ {total_perdido_geral:.2f}</span></p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:20px;'>✅ <b>Valor final da meta a receber:</b> R$ {valor_final:,.2f}</p>", unsafe_allow_html=True)
