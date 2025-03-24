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

# Interface
for i, col in enumerate(colunas):
    mes = meses[i]
    with col:
        st.subheader(mes)
        indicadores = {}
        total_perdido_mes = 0.0
        for indicador, peso in pesos.items():
            valor_indicador = valor_mensal * peso
            key = f"{indicador}_{mes}"

            # Monta o texto com status e valor
            texto_exibicao = f"{indicador} ({mes}) — R$ {valor_indicador:,.2f}"
            ativo = st.checkbox(texto_exibicao, value=True, key=key)

            if not ativo:
                total_perdido_mes += valor_indicador

            indicadores[indicador] = ativo

        indicadores_por_mes.append(indicadores)
        st.markdown(f"**Total perdido em {mes}:** <span style='color: red;'>R$ {total_perdido_mes:,.2f}</span>", unsafe_allow_html=True)

# Botão de cálculo final
if st.button("Calcular"):
    valor_trimestre = valor_mensal * 3
    valor_total_perdido = 0.0

    for i, indicadores in enumerate(indicadores_por_mes):
        for indicador, ativo in indicadores.items():
            if not ativo:
                valor_total_perdido += valor_mensal * pesos[indicador]

    valor_receber = valor_trimestre - valor_total_perdido

    st.markdown("---")
    st.markdown(
        f"<h4 style='text-align: center;'>💰 Total perdido no trimestre: <span style='color: red;'>R$ {valor_total_perdido:,.2f}</span></h4>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"<h3 style='text-align: center;'>✅ Valor final da meta a receber: R$ {valor_receber:,.2f}</h3>",
        unsafe_allow_html=True
    )
