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
colunas = st.columns(3)

totais_perdidos = {}

for i, col in enumerate(colunas):
    mes = meses[i]
    total_perdido = 0.0

    with col:
        st.subheader(mes)

        for indicador, peso in pesos.items():
            valor_indicador = valor_mensal * peso
            key = f"{indicador}_{mes}"
            ativo = st.checkbox(f"{indicador} ({mes})", value=True, key=key)

            icone = "✅" if ativo else "❌"
            cor = "green" if ativo else "red"
            if not ativo:
                total_perdido += valor_indicador

            st.markdown(
                f"<div style='display: flex; align-items: center; gap: 5px;'>"
                f"<span style='color:{cor}; font-size:15px;'>{icone} {indicador} ({mes}) — R$ {valor_indicador:,.2f}</span>"
                f"</div>",
                unsafe_allow_html=True
            )

        st.markdown(
            f"<br><b>Total perdido em {mes}:</b> <span style='color:red;'>R$ {total_perdido:,.2f}</span>",
            unsafe_allow_html=True
        )
        totais_perdidos[mes] = total_perdido

# Total perdido no trimestre
total_geral = sum(totais_perdidos.values())
st.markdown("---")
st.markdown(
    f"<h3 style='text-align: center;'>💰 Total perdido no trimestre: <span style='color:red;'>R$ {total_geral:,.2f}</span></h3>",
    unsafe_allow_html=True
)
