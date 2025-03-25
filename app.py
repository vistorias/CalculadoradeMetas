import streamlit as st

# Configurações da página
st.set_page_config(page_title="Calculadora de Metas Trimestrais", layout="wide")
st.markdown("<h1 style='text-align: center;'>📊 Calculadora de Metas Trimestrais</h1>", unsafe_allow_html=True)

# Entrada do valor mensal da meta
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
indicadores = list(pesos.keys())

col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
colunas = [col1, col2, col3]
indicadores_por_mes = []

# Interface de seleção dos indicadores
with col4:
    st.markdown("<h4 style='text-align: center;'>Valor Bônus</h4>", unsafe_allow_html=True)
    bonus_individual = {indicador: 0.0 for indicador in indicadores}

for i, col in enumerate(colunas):
    with col:
        st.subheader(meses[i])
        indicadores_mes = {}
        for indicador in indicadores:
            key = f"{indicador}_{meses[i]}"
            marcado = st.checkbox(f"{indicador} ({meses[i]})", value=True, key=key)
            indicadores_mes[indicador] = marcado
        indicadores_por_mes.append(indicadores_mes)

# Lógica para cálculo dos bônus
bonus_individual = {indicador: 0.0 for indicador in indicadores}
valor_total_perdido_mes = [0.0, 0.0, 0.0]
valor_total_a_receber = 0.0
valor_total_perdido = 0.0

for i, indicadores_mes in enumerate(indicadores_por_mes):
    for indicador, ativo in indicadores_mes.items():
        valor = valor_mensal * pesos[indicador]
        if ativo:
            bonus_individual[indicador] += valor
            valor_total_a_receber += valor
        else:
            valor_total_perdido_mes[i] += valor
            valor_total_perdido += valor

# Exibição dos valores na coluna "Valor Bônus"
with col4:
    for indicador in indicadores:
        valor_bonus = bonus_individual[indicador]
        if valor_bonus < valor_mensal * pesos[indicador] * 3:
            st.markdown(f"❌ R$ {valor_bonus:.2f}")
        else:
            st.markdown(f"✅ R$ {valor_bonus:.2f}")

# Exibir totais perdidos por mês
espaco_medio = "<br>" * 2
st.markdown(espaco_medio, unsafe_allow_html=True)
col_j, col_f, col_m = st.columns(3)
col_j.markdown(f"<div style='text-align: center;'><strong>Total perdido em Janeiro:</strong> <span style='color:red;'>R$ {valor_total_perdido_mes[0]:.2f}</span></div>", unsafe_allow_html=True)
col_f.markdown(f"<div style='text-align: center;'><strong>Total perdido em Fevereiro:</strong> <span style='color:red;'>R$ {valor_total_perdido_mes[1]:.2f}</span></div>", unsafe_allow_html=True)
col_m.markdown(f"<div style='text-align: center;'><strong>Total perdido em Março:</strong> <span style='color:red;'>R$ {valor_total_perdido_mes[2]:.2f}</span></div>", unsafe_allow_html=True)

# Botão para calcular valor final
st.write("")
if st.button("Calcular"):
    st.markdown("""
        <div style='text-align: center; margin-top: 30px;'>
            <p style='font-size:18px;'>💰 <strong>Total perdido no trimestre:</strong> <span style='color:red;'>R$ {:.2f}</span></p>
            <p style='font-size:18px;'>✅ <strong>Valor final da meta a receber:</strong> R$ {:.2f}</p>
        </div>
    """.format(valor_total_perdido, valor_total_a_receber), unsafe_allow_html=True)
