import streamlit as st

st.set_page_config(page_title="Calculadora de Metas Trimestrais", layout="wide")
st.markdown("<h1 style='text-align: center;'>📊 Calculadora de Metas Trimestrais</h1>", unsafe_allow_html=True)

# Valor da meta mensal
valor_mensal = st.number_input("Digite o valor mensal da meta:", min_value=0.0, step=10.0, format="%.2f")

# Pesos de cada indicador
pesos = {
    "Produção": 0.15,
    "Ticket Médio": 0.15,
    "Despesas": 0.15,
    "Satisfação Cliente": 0.275,
    "Pesquisa Clima": 0.0688,
    "Turnover": 0.0688,
    "ABS": 0.0688,
    "Treinamento": 0.0688
}

meses = ["Janeiro", "Fevereiro", "Março"]
indicadores = list(pesos.keys())

col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

# Armazenar seleções
selecoes = {indicador: {} for indicador in indicadores}
total_perdido_por_mes = {mes: 0.0 for mes in meses}

with col1:
    st.subheader("Janeiro")
    for indicador in indicadores:
        key = f"{indicador}_Janeiro"
        selecoes[indicador]["Janeiro"] = st.checkbox(f"{indicador} (Janeiro)", value=True, key=key)

with col2:
    st.subheader("Fevereiro")
    for indicador in indicadores:
        key = f"{indicador}_Fevereiro"
        selecoes[indicador]["Fevereiro"] = st.checkbox(f"{indicador} (Fevereiro)", value=True, key=key)

with col3:
    st.subheader("Março")
    for indicador in indicadores:
        key = f"{indicador}_Março"
        selecoes[indicador]["Março"] = st.checkbox(f"{indicador} (Março)", value=True, key=key)

with col4:
    st.subheader("Valor Bônus")
    total_bonificado = 0
    for indicador in indicadores:
        total = 0
        penalidades = 0
        for mes in meses:
            valor_indicador = valor_mensal * pesos[indicador]
            if selecoes[indicador][mes]:
                total += valor_indicador
            else:
                penalidades += valor_indicador
                total_perdido_por_mes[mes] += valor_indicador

        total_bonificado += total

        if penalidades > 0:
            st.markdown(f"❌ R$ {total:.2f}", unsafe_allow_html=True)
        else:
            st.markdown(f"✅ R$ {total:.2f}", unsafe_allow_html=True)

# Mostrar total perdido por mês
coluna_mensal = st.columns(3)
for i, mes in enumerate(meses):
    with coluna_mensal[i]:
        perdido = total_perdido_por_mes[mes]
        st.markdown(f"**Total perdido em {mes}:** <span style='color:red;'>R$ {perdido:.2f}</span>", unsafe_allow_html=True)

# Botão de cálculo
if st.button("Calcular"):
    total_perdido = sum(total_perdido_por_mes.values())
    valor_total = valor_mensal * 3
    valor_final = valor_total - total_perdido

    st.markdown("<hr>", unsafe_allow_html=True)
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown(f"<span style='color:#e69500;'>💰 Total perdido no trimestre:</span> <span style='color:red;'>R$ {total_perdido:.2f}</span>", unsafe_allow_html=True)
    with col_b:
        st.markdown(f"<span style='color:green;'>✅ Valor final da meta a receber: R$ {valor_final:.2f}</span>", unsafe_allow_html=True)
