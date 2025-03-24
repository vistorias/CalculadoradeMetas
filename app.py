import streamlit as st

st.set_page_config(page_title="Calculadora de Metas Trimestrais")
st.title("📊 Calculadora de Metas Trimestrais")

valor_mensal = st.number_input("Digite o valor mensal da meta:", min_value=0.0, step=100.0, format="%.2f")

indicadores = [
    "Produção", "Ticket Médio", "Despesas", "Satisfação Cliente",
    "Pesquisa Clima", "Turnover", "ABS", "Treinamento"
]

meses = ["Janeiro", "Fevereiro", "Março"]

# Inicializa dicionário para guardar seleções e totais perdidos
selecionados = {}
total_perdido = {}

col1, col2, col3 = st.columns(3)

for idx, mes in enumerate(meses):
    with [col1, col2, col3][idx]:
        st.subheader(mes)
        selecionados[mes] = {}
        total_perdido[mes] = 0

        for indicador in indicadores:
            chave = f"{indicador} ({mes})"
            check = st.checkbox(chave, value=True, key=chave)
            valor_indicador = valor_mensal / len(indicadores) if valor_mensal else 0

            if check:
                st.write(f"✅ R$ {valor_indicador:,.2f}")
                selecionados[mes][indicador] = True
            else:
                st.markdown(f"<span style='color:red'>❌ R$ {valor_indicador:,.2f}</span>", unsafe_allow_html=True)
                selecionados[mes][indicador] = False
                total_perdido[mes] += valor_indicador

# Exibe o total perdido por mês
st.markdown("---")
st.subheader("Resumo de valores perdidos por mês:")
for mes in meses:
    st.write(f"**{mes}:** R$ {total_perdido[mes]:,.2f}")
