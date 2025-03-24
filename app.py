import streamlit as st

# 1º COMANDO OBRIGATÓRIO
st.set_page_config(page_title="Calculadora de Metas Trimestrais", layout="wide")

# ESTILO para mudar a cor do checkbox (cinza claro)
st.markdown("""
    <style>
        input[type="checkbox"] {
            accent-color: #d3d3d3;
        }
    </style>
""", unsafe_allow_html=True)

# TÍTULO CENTRALIZADO
st.markdown("<h1 style='text-align: center;'>📊 Calculadora de Metas Trimestrais</h1>", unsafe_allow_html=True)

# ENTRADA DO VALOR MENSAL
valor_mensal = st.number_input("Digite o valor mensal da meta:", min_value=0.0, step=10.0, format="%.2f")

# PESOS POR INDICADOR
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

meses = ["Janeiro", "Fevereiro", "Março"]
colunas = st.columns(3)
indicadores_por_mes = []

# GERANDO AS COLUNAS COM CHECKBOX + VALOR + ÍCONE NA MESMA LINHA
for i, col in enumerate(colunas):
    with col:
        st.subheader(meses[i])
        indicadores = {}
        total_perdido_mes = 0.0

        for indicador, peso in pesos.items():
            valor_ind = valor_mensal * peso
            chave = f"{indicador}_{meses[i]}"
            checked = st.checkbox(f"{indicador} ({meses[i]})", value=True, key=chave)

            icone = "✅" if checked else "❌"
            cor = "green" if checked else "red"

            # Aqui unimos o nome e o valor com ícone na mesma linha
            st.markdown(
                f"<span style='color:{cor}'>{icone} R$ {valor_ind:,.2f}</span>",
                unsafe_allow_html=True
            )

            indicadores[indicador] = checked

            if not checked:
                total_perdido_mes += valor_ind

        st.markdown(
            f"<br><strong>Total perdido em {meses[i]}:</strong> <span style='color:red'>R$ {total_perdido_mes:.2f}</span>",
            unsafe_allow_html=True
        )
        indicadores_por_mes.append(indicadores)

# BOTÃO CALCULAR
if st.button("Calcular"):
    total_perdido = 0.0
    for indicadores in indicadores_por_mes:
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
