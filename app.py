import streamlit as st

# Configuração da página
st.set_page_config(page_title="Calculadora de Metas Trimestrais", layout="wide")
st.markdown("<h1 style='text-align: center;'>📊 Calculadora de Metas Trimestrais</h1>", unsafe_allow_html=True)

# Entrada do valor mensal
valor_mensal = st.number_input("Digite o valor mensal da meta:", min_value=0.0, step=10.0, format="%.2f")

# Pesos dos indicadores
pesos = {
    "Produção": 0.15,
    "Ticket Médio": 0.15,
    "Despesas": 0.15,
    "Satisfação Cliente": 0.275,
    "Pesquisa Clima": 0.0688,
    "Turnover": 0.0688,
    "ABS": 0.0688,
    "Treinamento": 0.0688,
}

# Meses e colunas
meses = ["Janeiro", "Fevereiro", "Março"]
colunas = st.columns(3)
indicadores_por_mes = []

# Interface principal
for i, col in enumerate(colunas):
    with col:
        st.subheader(meses[i])
        indicadores = {}
        total_perdido_mes = 0.0

        for indicador, peso in pesos.items():
            valor_ind = valor_mensal * peso
            chave = f"{indicador}_{meses[i]}"
            checked = st.checkbox(f"{indicador} ({meses[i]})", value=True, key=chave)
            indicadores[indicador] = checked

            icone = "✅" if checked else "❌"
            cor = "green" if checked else "red"
            if not checked:
                total_perdido_mes += valor_ind

            texto_formatado = f"<span style='color:{cor}'>{icone} R$ {valor_ind:.2f}</span>"
            st.markdown(
                f"<div style='margin-left: 25px; margin-top: -12px;'>{texto_formatado}</div>",
                unsafe_allow_html=True
            )

        st.markdown(f"<br><strong>Total perdido em {meses[i]}:</strong> <span style='color:red'>R$ {total_perdido_mes:.2f}</span>", unsafe_allow_html=True)
        indicadores_por_mes.append(indicadores)

# Botão Calcular
if st.button("Calcular"):
    total_perdido = 0.0
    for i, indicadores in enumerate(indicadores_por_mes):
        for indicador, ativo in indicadores.items():
            if not ativo:
                total_perdido += valor_mensal * pesos[indicador]

    valor_receber = (valor_mensal * 3) - total_perdido

    st.markdown("---")
    st.markdown(
        f"""
        <div style='text-align:center; font-size: 18px;'>
            <p>💰 <strong>Total perdido no trimestre:</strong> <span style='color:red'>R$ {total_perdido:.2f}</span></p>
            <p>✅ <strong>Valor final da meta a receber:</strong> <span style='color:green'>R$ {valor_receber:,.2f}</span></p>
        </div>
        """,
        unsafe_allow_html=True
    )
