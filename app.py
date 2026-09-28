import streamlit as st
import pandas as pd
import os

# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================

st.set_page_config(
    page_title="Essenza Perfumaria",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)

ARQUIVO = "produtos.csv"


# =========================================================
# IMAGENS
# =========================================================

IMAGEM_HERO = (
    "https://images.unsplash.com/"
    "photo-1594035910387-fea47794261f"
    "?auto=format&fit=crop&w=1800&q=90"
)

IMAGEM_LOJA = (
    "https://images.unsplash.com/"
    "photo-1547887538-e3a2f32cb1cc"
    "?auto=format&fit=crop&w=1200&q=85"
)


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap'
);

html,
body,
[class*="css"] {
    font-family: 'Poppins', sans-serif;
}


/* =========================================================
FUNDO
========================================================= */

.stApp {
    background:
        linear-gradient(
            135deg,
            #F9F2F4 0%,
            #F2E4E8 50%,
            #E8D5DC 100%
        );
}


/* =========================================================
ÁREA PRINCIPAL
========================================================= */

.block-container {
    max-width: 1400px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* =========================================================
SIDEBAR
========================================================= */

[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #3A1727,
            #5A263B
        );

    border-right:
        2px solid #C99AA8;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}


/* =========================================================
LOGO
========================================================= */

.logo-title {
    font-size: 28px;
    font-weight: 800;
    color: #FFFFFF !important;
    margin-bottom: 5px;
}

.logo-subtitle {
    font-size: 11px;
    font-weight: 700;
    color: #E8C5CF !important;
    letter-spacing: 1px;
}


/* =========================================================
TÍTULOS
========================================================= */

.page-title {
    font-size: 38px;
    font-weight: 800;
    color: #3A1727 !important;
    margin-bottom: 5px;
}

.page-subtitle {
    font-size: 17px;
    color: #694653 !important;
    margin-bottom: 30px;
}


/* =========================================================
HERO
========================================================= */

.hero-container {
    position: relative;
    height: 430px;
    width: 100%;
    border-radius: 28px;
    overflow: hidden;
    margin-bottom: 35px;

    background-size: cover;
    background-position: center;

    box-shadow:
        0 15px 35px rgba(70,25,45,0.22);
}

.hero-overlay {
    position: absolute;
    inset: 0;

    background:
        linear-gradient(
            90deg,
            rgba(48,18,34,0.97) 0%,
            rgba(48,18,34,0.82) 45%,
            rgba(48,18,34,0.12) 100%
        );
}

.hero-content {
    position: absolute;
    top: 50%;
    left: 7%;

    transform: translateY(-50%);

    max-width: 580px;
}

.hero-number {
    font-size: 70px;
    font-weight: 800;
    color: #E8B7C5 !important;
    line-height: 1;
}

.hero-title {
    font-size: 46px;
    font-weight: 800;
    color: #FFFFFF !important;

    margin-top: 12px;
    line-height: 1.1;
}

.hero-text {
    font-size: 17px;
    color: #F7E8ED !important;

    margin-top: 20px;
    line-height: 1.7;
}

.hero-badge {
    display: inline-block;

    margin-top: 24px;

    padding: 10px 22px;

    border-radius: 30px;

    background: #9A4D68;

    color: #FFFFFF !important;

    font-size: 14px;
    font-weight: 700;
}


/* =========================================================
CARDS
========================================================= */

.info-card {
    background: #FFFFFF;

    border-radius: 22px;

    padding: 28px;

    min-height: 170px;

    border:
        1px solid rgba(154,77,104,0.25);

    box-shadow:
        0 10px 25px rgba(70,25,45,0.08);
}

.card-icon {
    font-size: 32px;
}

.card-number {
    font-size: 34px;
    font-weight: 800;

    color: #3A1727 !important;

    margin-top: 10px;
}

.card-label {
    font-size: 14px;
    font-weight: 700;

    color: #765260 !important;

    margin-top: 5px;
}


/* =========================================================
CARD ESCURO
========================================================= */

.dark-card {
    background:
        linear-gradient(
            135deg,
            #3A1727,
            #652C44
        );

    border-radius: 24px;

    padding: 30px;

    box-shadow:
        0 12px 30px rgba(70,25,45,0.16);
}

.dark-card h2 {
    color: #FFFFFF !important;
    margin-top: 0;
}

.dark-card p {
    color: #F3DFE6 !important;
    line-height: 1.7;
}


/* =========================================================
FORMULÁRIO
========================================================= */

[data-testid="stForm"] {
    background:
        rgba(255,255,255,0.88);

    padding: 30px;

    border-radius: 25px;

    border:
        1px solid #D7B2BF;

    box-shadow:
        0 10px 30px rgba(70,25,45,0.08);
}


/* =========================================================
LABELS
========================================================= */

[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] label,
[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] span,
.stTextInput label,
.stNumberInput label,
.stSelectbox label,
.stTextArea label {
    color: #3A1727 !important;

    opacity: 1 !important;

    font-size: 15px !important;

    font-weight: 700 !important;
}


/* =========================================================
INPUTS
========================================================= */

.stTextInput input,
.stNumberInput input,
.stTextArea textarea {
    background-color: #FFFFFF !important;

    color: #30232A !important;

    -webkit-text-fill-color:
        #30232A !important;

    border:
        2px solid #B98798 !important;

    border-radius: 12px !important;

    font-size: 16px !important;

    font-weight: 500 !important;
}

.stTextInput input:focus,
.stNumberInput input:focus,
.stTextArea textarea:focus {
    border:
        2px solid #8C3F5C !important;

    box-shadow:
        0 0 0 3px rgba(140,63,92,0.15) !important;
}

input::placeholder,
textarea::placeholder {
    color: #77656C !important;
    opacity: 1 !important;
}


/* =========================================================
SELECTBOX
========================================================= */

[data-baseweb="select"] > div {
    background-color: #3D2630 !important;

    border:
        2px solid #9D6177 !important;

    border-radius: 12px !important;
}

[data-baseweb="select"] > div * {
    color: #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;

    opacity: 1 !important;
}

[data-baseweb="select"] input {
    color: #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;
}

[data-baseweb="select"] [class*="singleValue"] {
    color: #FFFFFF !important;
}

[data-baseweb="select"] svg {
    fill: #FFFFFF !important;
    color: #FFFFFF !important;
}

[data-baseweb="select"] > div:hover {
    border-color: #D49AAD !important;
}


/* =========================================================
MENU DO SELECTBOX
========================================================= */

[data-baseweb="popover"] {
    background-color: #3D2630 !important;
}

[data-baseweb="menu"] {
    background-color: #3D2630 !important;
}

[role="option"] {
    background-color: #3D2630 !important;

    color: #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;
}

[role="option"]:hover {
    background-color: #713A51 !important;

    color: #FFFFFF !important;
}


/* =========================================================
BOTÕES
========================================================= */

.stButton > button,
div[data-testid="stFormSubmitButton"] > button {
    background:
        linear-gradient(
            135deg,
            #803D59,
            #B05D7C
        ) !important;

    color: #FFFFFF !important;

    border: none !important;

    border-radius: 14px !important;

    min-height: 54px;

    font-family:
        'Poppins', sans-serif !important;

    font-size: 15px !important;

    font-weight: 700 !important;

    box-shadow:
        0 8px 18px rgba(128,61,89,0.25);
}

.stButton > button:hover,
div[data-testid="stFormSubmitButton"] > button:hover {
    background:
        linear-gradient(
            135deg,
            #682D46,
            #934B68
        ) !important;

    color: #FFFFFF !important;

    transform:
        translateY(-1px);
}


/* =========================================================
TABELA
========================================================= */

[data-testid="stDataFrame"] {
    background: #FFFFFF;

    border-radius: 18px;

    overflow: hidden;

    border:
        1px solid #D7B2BF;
}


/* =========================================================
RODAPÉ
========================================================= */

.footer {
    margin-top: 50px;

    text-align: center;

    color: #765260 !important;

    font-size: 14px;

    font-weight: 600;
}


/* =========================================================
RESPONSIVO
========================================================= */

@media (max-width: 768px) {

    .hero-container {
        height: 500px;
    }

    .hero-content {
        left: 8%;
        right: 8%;
    }

    .hero-title {
        font-size: 34px;
    }

    .hero-number {
        font-size: 55px;
    }

    .page-title {
        font-size: 30px;
    }
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# FUNÇÕES
# =========================================================

def carregar_dados():

    colunas = [
        "Categoria",
        "Marca",
        "Produto",
        "Volume",
        "Fragrância",
        "Quantidade",
        "Valor",
        "Observações"
    ]

    if os.path.exists(ARQUIVO):

        try:
            dados = pd.read_csv(ARQUIVO)

            return dados

        except Exception:
            return pd.DataFrame(columns=colunas)

    return pd.DataFrame(columns=colunas)


def salvar_dados(dados):

    dados.to_csv(
        ARQUIVO,
        index=False
    )


# =========================================================
# CARREGAR DADOS
# =========================================================

df = carregar_dados()


colunas_necessarias = [
    "Categoria",
    "Marca",
    "Produto",
    "Volume",
    "Fragrância",
    "Quantidade",
    "Valor",
    "Observações"
]

for coluna in colunas_necessarias:

    if coluna not in df.columns:
        df[coluna] = ""


df["Valor"] = pd.to_numeric(
    df["Valor"],
    errors="coerce"
).fillna(0)

df["Quantidade"] = pd.to_numeric(
    df["Quantidade"],
    errors="coerce"
).fillna(0)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown(
"""
<div class="logo-title">
🌸 Essenza
</div>

<div class="logo-subtitle">
PERFUMARIA & COSMÉTICOS
</div>
""",
    unsafe_allow_html=True
)

st.sidebar.markdown("<br>", unsafe_allow_html=True)


menu = st.sidebar.radio(
    "NAVEGAÇÃO",
    [
        "🏠 Dashboard",
        "➕ Cadastrar Produto",
        "🌸 Produtos Cadastrados"
    ]
)


st.sidebar.markdown("---")

st.sidebar.caption(
    "Essenza Perfumaria • 2026"
)


# =========================================================
# DASHBOARD
# =========================================================

if menu == "🏠 Dashboard":

    st.markdown(
f"""
<div class="hero-container"
style="background-image: url('{IMAGEM_HERO}');">

<div class="hero-overlay"></div>

<div class="hero-content">

<div class="hero-number">
01.
</div>

<div class="hero-title">
Seu perfume.<br>
Sua essência.
</div>

<div class="hero-text">
Tenha todos os produtos da sua perfumaria organizados
em um único lugar. Controle seu estoque, consulte seus
produtos e acompanhe suas vendas de forma simples.
</div>

<div class="hero-badge">
🌸 EXPERIÊNCIA & ELEGÂNCIA
</div>

</div>

</div>
""",
        unsafe_allow_html=True
    )


    st.markdown(
"""
<div class="page-title">
📊 Visão geral da perfumaria
</div>

<div class="page-subtitle">
Acompanhe seus produtos e mantenha seu estoque organizado.
</div>
""",
        unsafe_allow_html=True
    )


    total_produtos = len(df)

    quantidade_total = df["Quantidade"].sum()

    valor_total = (
        df["Valor"] * df["Quantidade"]
    ).sum()


    col1, col2, col3 = st.columns(3)


    with col1:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
🌸
</div>

<div class="card-number">
{total_produtos}
</div>

<div class="card-label">
PRODUTOS CADASTRADOS
</div>

</div>
""",
            unsafe_allow_html=True
        )


    with col2:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
📦
</div>

<div class="card-number">
{quantidade_total:,.0f}
</div>

<div class="card-label">
ITENS EM ESTOQUE
</div>

</div>
""",
            unsafe_allow_html=True
        )


    with col3:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
💰
</div>

<div class="card-number">
R$ {valor_total:,.2f}
</div>

<div class="card-label">
VALOR DO ESTOQUE
</div>

</div>
""",
            unsafe_allow_html=True
        )


    st.markdown("<br>", unsafe_allow_html=True)


    coluna1, coluna2 = st.columns([1.1, 1])


    with coluna1:

        st.markdown(
"""
<div class="dark-card">

<h2>
✨ Sua perfumaria organizada
</h2>

<p>
A Essenza Perfumaria permite manter seus perfumes,
cosméticos e produtos de beleza organizados em um
único lugar.
</p>

<p>
Cadastre produtos, consulte o estoque, pesquise por
marca ou categoria e acompanhe o valor total da loja.
</p>

</div>
""",
            unsafe_allow_html=True
        )


    with coluna2:

        st.image(
            IMAGEM_LOJA,
            use_container_width=True
        )


# =========================================================
# CADASTRAR PRODUTO
# =========================================================

elif menu == "➕ Cadastrar Produto":

    st.markdown(
"""
<div class="page-title">
➕ Novo produto
</div>

<div class="page-subtitle">
Adicione um novo produto ao estoque da Essenza Perfumaria.
</div>
""",
        unsafe_allow_html=True
    )


    with st.form(
        "cadastro_produto",
        clear_on_submit=True
    ):

        col1, col2 = st.columns(2)


        with col1:

            categoria = st.selectbox(
                "🏷️ Categoria",
                [
                    "Perfume",
                    "Body Splash",
                    "Hidratante",
                    "Desodorante",
                    "Óleo Corporal",
                    "Perfume para Cabelo",
                    "Kit Presente",
                    "Aromatizador",
                    "Vela Aromática",
                    "Sabonete",
                    "Outro"
                ]
            )


            marca = st.text_input(
                "🏢 Marca"
            )


            produto = st.text_input(
                "🌸 Nome do Produto"
            )


            volume = st.selectbox(
                "🧴 Volume",
                [
                    "30 ml",
                    "50 ml",
                    "75 ml",
                    "100 ml",
                    "150 ml",
                    "200 ml",
                    "250 ml",
                    "500 ml",
                    "Outro"
                ]
            )


        with col2:

            fragrancia = st.selectbox(
                "🌺 Família Olfativa",
                [
                    "Floral",
                    "Frutado",
                    "Cítrico",
                    "Amadeirado",
                    "Oriental",
                    "Gourmand",
                    "Aromático",
                    "Aquático",
                    "Chipre",
                    "Outro"
                ]
            )


            quantidade = st.number_input(
                "📦 Quantidade em Estoque",
                min_value=0,
                value=1,
                step=1
            )


            valor = st.number_input(
                "💰 Preço de Venda",
                min_value=0.0,
                value=0.0,
                step=5.0
            )


            observacoes = st.text_area(
                "📝 Observações"
            )


        cadastrar = st.form_submit_button(
            "💾 CADASTRAR PRODUTO"
        )


    if cadastrar:

        if (
            marca.strip()
            and produto.strip()
        ):

            novo_produto = pd.DataFrame(
                [{
                    "Categoria": categoria,
                    "Marca": marca.strip(),
                    "Produto": produto.strip(),
                    "Volume": volume,
                    "Fragrância": fragrancia,
                    "Quantidade": int(quantidade),
                    "Valor": float(valor),
                    "Observações": observacoes.strip()
                }]
            )


            df = pd.concat(
                [
                    df,
                    novo_produto
                ],
                ignore_index=True
            )


            salvar_dados(df)


            st.success(
                "🌸 Produto cadastrado com sucesso!"
            )


            st.rerun()


        else:

            st.warning(
                "⚠️ Preencha Marca e Nome do Produto."
            )


# =========================================================
# PRODUTOS CADASTRADOS
# =========================================================

elif menu == "🌸 Produtos Cadastrados":

    st.markdown(
"""
<div class="page-title">
🌸 Minha perfumaria
</div>

<div class="page-subtitle">
Consulte e pesquise todos os produtos cadastrados.
</div>
""",
        unsafe_allow_html=True
    )


    if df.empty:

        st.markdown(
"""
<div class="dark-card">

<h2>
🌸 Nenhum produto cadastrado
</h2>

<p>
Seu estoque ainda está vazio.
Cadastre seu primeiro produto para começar.
</p>

</div>
""",
            unsafe_allow_html=True
        )


    else:

        busca = st.text_input(
            "🔎 Pesquisar produto",
            placeholder="Digite marca, produto, categoria ou fragrância..."
        )


        if busca:

            mascara = (
                df.astype(str)
                .apply(
                    lambda coluna:
                    coluna.str.contains(
                        busca,
                        case=False,
                        na=False
                    )
                )
                .any(axis=1)
            )

            df_filtrado = df[mascara]

        else:

            df_filtrado = df


        st.dataframe(
            df_filtrado,
            use_container_width=True,
            hide_index=True
        )


        st.markdown("<br>", unsafe_allow_html=True)


        opcoes_produtos = df.index.tolist()


        produto_excluir = st.selectbox(
            "🗑️ Selecione um produto para excluir",
            options=opcoes_produtos,
            format_func=lambda indice:
                f"{df.loc[indice, 'Marca']} "
                f"{df.loc[indice, 'Produto']} - "
                f"{df.loc[indice, 'Volume']}"
        )


        if st.button(
            "🗑️ EXCLUIR PRODUTO"
        ):

            df = df.drop(
                produto_excluir
            )

            df = df.reset_index(
                drop=True
            )


            salvar_dados(df)


            st.success(
                "🌸 Produto excluído com sucesso!"
            )


            st.rerun()


# =========================================================
# RODAPÉ
# =========================================================

st.markdown(
"""
<div class="footer">

🌸 Essenza Perfumaria<br>
Sua essência, seu estilo.

</div>
""",
    unsafe_allow_html=True
)
