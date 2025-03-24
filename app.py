import streamlit as st

# Configuração da página
st.set_page_config(page_title="Calculadora de Metas Trimestrais", layout="wide")

# CSS para mudar a cor da checkbox para cinza claro
st.markdown("""
    <style>
        input[type="checkbox"] {
            accent-color: lightgray !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>📊 Calculadora de Metas Trimestrais</h1>", unsafe_allow_html=True)

# Valor mensal da meta
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
colunas = st.columns(3)
indicadores_por_mes = []

for idx, col in enumerate(colunas):
    with col:
        st.subheader(meses[idx])
        indicadores = {}
        total_perdido = 0
        for indicador, peso in pesos.items():
            chave = f"{indicador}_{meses[idx]}"
            marcado = st.checkbox(f"{indicador} ({meses[idx]})", value=True, key=chave)
            valor_indicador = valor_mensal * peso
            if marcado:
                st.markdown(f"<span style='color: green;'>✅ R$ {valor_indicador:,.2f}</span>", unsafe_allow_html=True)
            else:
                st.markdown(f"<span style='color: red;'>❌ R$ {valor_indicador:,.2f}</span>", unsafe_allow_html=True)
                total_perdido += valor_indicador
            indicadores[indicador] = marcado
        indicadores_por_mes.append(indicadores)
        st.markdown(f"<b>Total perdido em {meses[idx]}:</b> <span style='color: red;'>R$ {total_perdido:,.2f}</span>", unsafe_allow_html=True)

# Botão para calcular
if st.button("Calcular"):
    total_meta = valor_mensal * 3
    total_receber = total_meta
    total_perda_trimestre = 0

    for i, mes in enumerate(meses):
        for indicador, ativo in indicadores_por_mes[i].items():
            if not ativo:
                perda = valor_mensal * pesos[indicador]
                total_receber -= perda
                total_perda_trimestre += perda

    st.markdown("---")
    st.markdown(f"<div style='text-align: center;'><b>💰 Total perdido no trimestre:</b> <span style='color: red;'>R$ {total_perda_trimestre:,.2f}</span></div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: center;'><span style='color: green;'>✅ Valor final da meta a receber: R$ {total_receber:,.2f}</span></div>", unsafe_allow_html=True)
