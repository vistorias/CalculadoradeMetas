import streamlit as st

# Esta linha deve ser a primeira do script
st.set_page_config(page_title="Calculadora de Metas Trimestrais", layout="wide")

st.markdown("<h1 style='text-align: center;'>📊 Calculadora de Metas Trimestrais</h1>", unsafe_allow_html=True)

# Entrada do valor mensal da meta
valor_mensal = st.number_input("Digite o valor mensal da meta:", min_value=0.0, step=10.0, format="%.2f")

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
col1, col2, col3 = st.columns(3)
colunas = [col1, col2, col3]
indicadores_por_mes = []

# Interface dos indicadores
for idx, col in enumerate(colunas):
    with col:
        st.markdown(f"### {meses[idx]}")
        indicadores_mes = {}
        total_perdido = 0
        for indicador, peso in pesos.items():
            valor = valor_mensal * peso
            key = f"{indicador}_{meses[idx]}"
            checked = st.checkbox(f"{indicador} ({meses[idx]})", value=True, key=key)

            if checked:
                indicadores_mes[indicador] = True
                st.markdown(f"<span style='color: green;'>✅ R$ {valor:.2f}</span>", unsafe_allow_html=True)
            else:
                indicadores_mes[indicador] = False
                st.markdown(f"<span style='color: red;'>❌ R$ {valor:.2f}</span>", unsafe_allow_html=True)
                total_perdido += valor

        indicadores_por_mes.append(indicadores_mes)
        st.markdown(f"<br><strong>Total perdido em {meses[idx]}:</strong> <span style='color:red'>R$ {total_perdido:.2f}</span>", unsafe_allow_html=True)

# Botão calcular
if st.button("Calcular"):
    total_trimestre = valor_mensal * 3
    total_receber = total_trimestre

    for idx, indicadores_mes in enumerate(indicadores_por_mes):
        for indicador, ativo in indicadores_mes.items():
            if not ativo:
                total_receber -= valor_mensal * pesos[indicador]

    total_perdido = total_trimestre - total_receber

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(
        f"<div style='text-align: center; font-size: 18px;'><br>"
        f"💰 <strong>Total perdido no trimestre:</strong> <span style='color:red'>R$ {total_perdido:.2f}</span><br><br>"
        f"✅ <strong>Valor final da meta a receber:</strong> <span style='color:green'>R$ {total_receber:.2f}</span></div>",
        unsafe_allow_html=True
    )
