import streamlit as st

# Configuração da página
st.set_page_config(page_title="Calculadora de Metas Trimestrais", layout="wide")
st.markdown("<h1 style='text-align: center;'>📊 Calculadora de Metas Trimestrais</h1>", unsafe_allow_html=True)

# Entrada do valor mensal da meta
valor_mensal = st.number_input("Digite o valor mensal da meta:", min_value=0.0, step=100.0, format="%.2f")

# Pesos por indicador
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

# Criar os blocos por mês
for i, col in enumerate(colunas):
    mes = meses[i]
    with col:
        st.subheader(mes)
        indicadores = {}
        total_perdido_mes = 0.0
        for indicador, peso in pesos.items():
            valor_indicador = valor_mensal * peso
            key_checkbox = f"{indicador}_{mes}"
            checked = st.checkbox(f"{indicador} ({mes})", value=True, key=key_checkbox)

            if checked:
                st.markdown(f"<span style='color: green;'>✅ R$ {valor_indicador:,.2f}</span>", unsafe_allow_html=True)
            else:
                st.markdown(f"<span style='color: red;'>❌ R$ {valor_indicador:,.2f}</span>", unsafe_allow_html=True)
                total_perdido_mes += valor_indicador

            indicadores[indicador] = checked

        indicadores_por_mes.append(indicadores)
        st.markdown(f"**Total perdido em {mes}:** <span style='color: red;'>R$ {total_perdido_mes:,.2f}</span>", unsafe_allow_html=True)

# Botão para calcular valor final da meta
if st.button("Calcular"):
    valor_trimestre = valor_mensal * 3
    valor_total_perdido = 0.0

    for i, indicadores in enumerate(indicadores_por_mes):
        for indicador, ativo in indicadores.items():
            if not ativo:
                valor_total_perdido += valor_mensal * pesos[indicador]

    valor_receber = valor_trimestre - valor_total_perdido

    st.markdown("---")
    st.markdown(f"<h4 style='text-align: center;'>💰 <strong>Total perdido no trimestre:</strong> <span style='color: red;'>R$ {valor_total_perdido:,.2f}</span></h4>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align: center;'>✅ <strong>Valor final da meta a receber:</strong> R$ {valor_receber:,.2f}</h3>", unsafe_allow_html=True)
