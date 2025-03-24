import streamlit as st

# Configuração da página
st.set_page_config(page_title="Calculadora de Metas Trimestrais", layout="wide")

# Estilo CSS para ajustar a coluna de bônus
st.markdown("""
    <style>
        .bonus-col {
            width: 120px;
            text-align: left;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>📊 Calculadora de Metas Trimestrais</h1>", unsafe_allow_html=True)

valor_mensal = st.number_input("Digite o valor mensal da meta:", min_value=0.0, step=10.0, format="%.2f")

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
indicadores = list(pesos.keys())

checkbox_states = {mes: {} for mes in meses}
col1, col2, col3, col4 = st.columns([2, 2, 2, 1.5])

with col1:
    st.subheader("Janeiro")
    for indicador in indicadores:
        key = f"{indicador}_Janeiro"
        checkbox_states["Janeiro"][indicador] = st.checkbox(indicador + " (Janeiro)", value=True, key=key)

with col2:
    st.subheader("Fevereiro")
    for indicador in indicadores:
        key = f"{indicador}_Fevereiro"
        checkbox_states["Fevereiro"][indicador] = st.checkbox(indicador + " (Fevereiro)", value=True, key=key)

with col3:
    st.subheader("Março")
    for indicador in indicadores:
        key = f"{indicador}_Março"
        checkbox_states["Março"][indicador] = st.checkbox(indicador + " (Março)", value=True, key=key)

with col4:
    st.subheader("Valor Bônus")
    valores_individuais = []
    for mes in meses:
        for indicador in indicadores:
            valor = valor_mensal * pesos[indicador]
            ativo = checkbox_states[mes][indicador]
            status = "✅" if ativo else "❌"
            cor = "green" if ativo else "red"
            valores_individuais.append(valor if ativo else 0)
            st.markdown(
                f"<div class='bonus-col'><span style='color:{cor}'>{status} R$ {valor:.2f}</span></div>",
                unsafe_allow_html=True
            )

if st.button("Calcular"):
    total_meta = valor_mensal * 3
    total_recebido = sum(valores_individuais)
    total_perdido = total_meta - total_recebido

    st.markdown("---")
    st.markdown(f"<h5 style='text-align: center;'>💰 <b>Total perdido no trimestre:</b> <span style='color:red;'>R$ {total_perdido:.2f}</span></h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center;'>✅ <b>Valor final da meta a receber:</b> R$ {total_recebido:.2f}</h5>", unsafe_allow_html=True)
