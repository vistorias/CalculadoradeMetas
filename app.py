import streamlit as st

# Configuração da página
st.set_page_config(page_title="Calculadora de Metas Trimestrais", layout="wide")
st.markdown("<h1 style='text-align: center;'>📊 Calculadora de Metas Trimestrais</h1>", unsafe_allow_html=True)

# Entrada do valor mensal
valor_mensal = st.number_input("Digite o valor mensal da meta:", min_value=0.0, step=100.0, format="%.2f")

# Pesos por indicador
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

# Meses e colunas
meses = ["Janeiro", "Fevereiro", "Março"]
col1, col2, col3 = st.columns(3)
colunas = [col1, col2, col3]

for i, col in enumerate(colunas):
    mes = meses[i]
    total_perdido = 0.0

    with col:
        st.subheader(mes)
        for indicador, peso in pesos.items():
            valor_indicador = valor_mensal * peso
            ativo = st.checkbox(f"{indicador} ({mes})", value=True, key=f"{indicador}_{mes}")

            cor = "green" if ativo else "red"
            icone = "✅" if ativo else "❌"
            valor_formatado = f"R$ {valor_indicador:.2f}"
            texto = f"<span style='color:{cor};'>{icone} {indicador} ({mes}) — {valor_formatado}</span>"

            st.markdown(texto, unsafe_allow_html=True)

            if not ativo:
                total_perdido += valor_indicador

        st.markdown(f"<br><b>Total perdido em {mes}:</b> <span style='color:red;'>R$ {total_perdido:.2f}</span>", unsafe_allow_html=True)
