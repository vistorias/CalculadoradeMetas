import streamlit as st

# 🛠️ Configuração da página – precisa vir primeiro!
st.set_page_config(page_title="Calculadora de Metas Trimestrais", layout="wide")

# 🎨 Estilo para alterar a cor da checkbox para cinza claro
st.markdown("""
    <style>
        div[data-baseweb="checkbox"] input[type="checkbox"] {
            accent-color: #d3d3d3 !important;
        }
    </style>
""", unsafe_allow_html=True)

# 📌 Pesos por indicador
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

# 🖼️ Título
st.markdown("<h1 style='text-align: center;'>📊 Calculadora de Metas Trimestrais</h1>", unsafe_allow_html=True)

# 💰 Entrada do valor mensal da meta
valor_mensal = st.number_input("Digite o valor mensal da meta:", min_value=0.0, step=10.0, format="%.2f")

# 🗓️ Meses
meses = ["Janeiro", "Fevereiro", "Março"]
colunas = st.columns(3)
indicadores_por_mes = []

for i, col in enumerate(colunas):
    with col:
        st.subheader(meses[i])
        indicadores = {}
        total_perdido = 0.0
        for indicador, peso in pesos.items():
            key = f"{indicador} ({meses[i]})"
            checked = st.checkbox(key, value=True, key=key)
            valor_indicador = valor_mensal * peso
            if checked:
                st.markdown(f"<span style='color: green;'>✅ R$ {valor_indicador:.2f}</span>", unsafe_allow_html=True)
            else:
                st.markdown(f"<span style='color: red;'>❌ R$ {valor_indicador:.2f}</span>", unsafe_allow_html=True)
                total_perdido += valor_indicador
            indicadores[indicador] = checked
        st.markdown(f"<strong>Total perdido em {meses[i]}:</strong> <span style='color: red;'>R$ {total_perdido:.2f}</span>", unsafe_allow_html=True)
        indicadores_por_mes.append(indicadores)

# 🔘 Botão de cálculo
if st.button("Calcular"):
    total_perdido = 0.0
    for i in range(3):
        for indicador, ativo in indicadores_por_mes[i].items():
            if not ativo:
                total_perdido += valor_mensal * pesos[indicador]

    valor_total = (valor_mensal * 3) - total_perdido

    st.markdown("---")
    st.markdown(f"<h4 style='text-align: center;'>💰 <span style='color: black;'>Total perdido no trimestre:</span> <span style='color: red;'>R$ {total_perdido:.2f}</span></h4>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='text-align: center;'>✅ <span style='color: black;'>Valor final da meta a receber:</span> <span style='color: green;'>R$ {valor_total:.2f}</span></h4>", unsafe_allow_html=True)
