import streamlit as st

# Configuração
st.set_page_config(page_title="Calculadora de Metas Trimestrais", layout="wide")
st.markdown("<h1 style='text-align: center;'>📊 Calculadora de Metas Trimestrais</h1>", unsafe_allow_html=True)

# Entrada do valor mensal da meta
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
col1, col2, col3 = st.columns(3)
colunas = [col1, col2, col3]

indicadores_por_mes = []

# Criação dos checkboxes e exibição dos valores
for i, col in enumerate(colunas):
    mes = meses[i]
    with col:
        st.subheader(mes)
        indicadores = {}
        total_perdido = 0
        for indicador, peso in pesos.items():
            valor_indicador = valor_mensal * peso
            checked = st.checkbox(f"{indicador} ({mes})", value=True, key=f"{indicador}_{mes}")
            if checked:
                st.markdown(f"<span style='color: green;'>✅ R$ {valor_indicador:.2f}</span>", unsafe_allow_html=True)
            else:
                st.markdown(f"<span style='color: red;'>❌ R$ {valor_indicador:.2f}</span>", unsafe_allow_html=True)
                total_perdido += valor_indicador
            indicadores[indicador] = checked
        indicadores_por_mes.append(indicadores)

        # Total perdido no mês
        st.markdown(f"<br><b>Total perdido em {mes}:</b> <span style='color: red;'>R$ {total_perdido:.2f}</span><br><hr>", unsafe_allow_html=True)

# Cálculo final
if st.button("Calcular"):
    total_trimestral = valor_mensal * 3
    total_recebido = total_trimestral

    for indicadores in indicadores_por_mes:
        for indicador, ativo in indicadores.items():
            if not ativo:
                total_recebido -= valor_mensal * pesos[indicador]

    st.success(f"💰 Valor final da meta trimestral: R$ {total_recebido:.2f}")
