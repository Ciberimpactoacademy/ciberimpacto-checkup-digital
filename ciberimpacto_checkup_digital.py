import streamlit as st
from datetime import datetime
import pandas as pd
import io
from pathlib import Path


# ==========================================================
# CIBERIMPACTO CHECK-UP DIGITAL
# Aplicação simples em Python/Streamlit para sensibilização
# de empresas sobre ataques informáticos.
# ==========================================================

st.set_page_config(
    page_title="CiberImpacto Check-Up Digital",
    page_icon="🔐",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# -------------------------
# ESTILO VISUAL - CORES CIBERIMPACTO
# -------------------------
CORES = {
    "azul_principal": "#1482FF",
    "azul_profundo": "#0A62FF",
    "azul_claro": "#40BDF9",
    "turquesa": "#12E9CA",
    "verde_agua": "#0BE7C4",
    "preto": "#000000",
    "branco": "#FFFFFF",
}

LOGO_FICHEIROS = [
    "logo_ciberimpacto.png",
    "logo_ciberimpacto.jpg",
    "logo_ciberimpacto.jpeg",
    "logo_ciberimpacto.webp",
]

st.markdown(
    """
    <style>
    :root {
        --ci-blue: #1482FF;
        --ci-blue-dark: #0A62FF;
        --ci-blue-light: #40BDF9;
        --ci-turquoise: #12E9CA;
        --ci-mint: #0BE7C4;
        --ci-black: #000000;
        --ci-white: #FFFFFF;
        --ci-soft: #F3FAFF;
        --ci-text: #111827;
        --ci-muted: #5B6B7D;
    }

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(18, 233, 202, 0.18) 0%, transparent 28%),
            radial-gradient(circle at top right, rgba(20, 130, 255, 0.18) 0%, transparent 30%),
            linear-gradient(180deg, #F7FCFF 0%, #FFFFFF 45%, #F8FBFF 100%);
    }

    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2.5rem;
        max-width: 980px;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #020817 0%, #071A3A 55%, #0A62FF 100%);
        color: white;
    }

    [data-testid="stSidebar"] * {
        color: white !important;
    }

    .brand-row {
        display: flex;
        align-items: center;
        gap: 14px;
        margin-bottom: 18px;
    }

    .brand-logo-fallback {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 14px 16px;
        border-radius: 18px;
        background: rgba(255,255,255,0.92);
        border: 1px solid rgba(20,130,255,0.15);
        box-shadow: 0 16px 40px rgba(10, 98, 255, 0.12);
        width: fit-content;
        margin-bottom: 18px;
    }

    .brand-logo-fallback .bulb {
        width: 42px;
        height: 42px;
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: linear-gradient(135deg, var(--ci-blue-dark), var(--ci-turquoise));
        color: white;
        font-size: 1.45rem;
    }

    .brand-logo-fallback .brand-name {
        color: var(--ci-text);
        font-weight: 900;
        font-size: 1.25rem;
        letter-spacing: -0.03em;
        line-height: 1.05;
    }

    .brand-logo-fallback .brand-subtitle {
        color: var(--ci-muted);
        font-size: 0.78rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }

    .hero {
        position: relative;
        overflow: hidden;
        padding: 34px;
        border-radius: 28px;
        background:
            radial-gradient(circle at 12% 0%, rgba(18, 233, 202, 0.34), transparent 28%),
            radial-gradient(circle at 90% 20%, rgba(64, 189, 249, 0.26), transparent 30%),
            linear-gradient(135deg, #020817 0%, #082B66 46%, #0A62FF 100%);
        color: white;
        box-shadow: 0 24px 70px rgba(10, 98, 255, 0.24);
        margin-bottom: 22px;
        border: 1px solid rgba(255,255,255,0.12);
    }

    .hero:after {
        content: "";
        position: absolute;
        width: 260px;
        height: 260px;
        right: -90px;
        bottom: -110px;
        background: rgba(18, 233, 202, 0.22);
        border-radius: 999px;
        filter: blur(2px);
    }

    .hero h1 {
        font-size: 2.35rem;
        line-height: 1.1;
        margin-bottom: 0.75rem;
        letter-spacing: -0.04em;
        max-width: 760px;
    }

    .hero p {
        font-size: 1.08rem;
        line-height: 1.65;
        max-width: 760px;
        opacity: 0.96;
    }

    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 8px 12px;
        border-radius: 999px;
        background: rgba(255,255,255,0.13);
        border: 1px solid rgba(255,255,255,0.18);
        color: white;
        font-size: 0.85rem;
        font-weight: 700;
        margin-bottom: 14px;
    }

    .card {
        padding: 24px;
        border-radius: 24px;
        background: rgba(255,255,255,0.94);
        box-shadow: 0 14px 42px rgba(10, 98, 255, 0.08);
        border: 1px solid rgba(20,130,255,0.12);
        margin-bottom: 18px;
    }

    .card h3 {
        color: var(--ci-text);
        letter-spacing: -0.02em;
    }

    .mini-card {
        padding: 16px 18px;
        border-radius: 18px;
        background: linear-gradient(135deg, #FFFFFF 0%, #F2FBFF 100%);
        border: 1px solid rgba(64,189,249,0.28);
        margin-bottom: 10px;
        box-shadow: 0 8px 20px rgba(10, 98, 255, 0.045);
    }

    .metric-card {
        padding: 18px;
        border-radius: 20px;
        background: white;
        border: 1px solid rgba(20,130,255,0.12);
        box-shadow: 0 10px 30px rgba(10, 98, 255, 0.06);
    }

    .risk-low, .risk-medium, .risk-high, .risk-critical {
        padding: 22px;
        border-radius: 24px;
        box-shadow: 0 14px 36px rgba(0,0,0,0.06);
        margin-bottom: 10px;
    }

    .risk-low {
        background: linear-gradient(135deg, #E9FFF8 0%, #FFFFFF 100%);
        border-left: 9px solid #0BE7C4;
    }

    .risk-medium {
        background: linear-gradient(135deg, #FFF8E1 0%, #FFFFFF 100%);
        border-left: 9px solid #F9A825;
    }

    .risk-high {
        background: linear-gradient(135deg, #FFF1E8 0%, #FFFFFF 100%);
        border-left: 9px solid #EF6C00;
    }

    .risk-critical {
        background: linear-gradient(135deg, #FFECEC 0%, #FFFFFF 100%);
        border-left: 9px solid #D32F2F;
    }

    .small-text {
        font-size: 0.92rem;
        color: var(--ci-muted);
    }

    .highlight-line {
        height: 5px;
        width: 120px;
        border-radius: 999px;
        background: linear-gradient(90deg, var(--ci-blue), var(--ci-turquoise));
        margin: 14px 0 18px 0;
    }

    .footer {
        margin-top: 34px;
        color: #607086;
        font-size: 0.86rem;
        text-align: center;
    }

    .footer strong {
        color: var(--ci-blue-dark);
    }

    div.stButton > button:first-child,
    div.stFormSubmitButton > button:first-child {
        border-radius: 16px;
        border: 0px;
        background: linear-gradient(135deg, var(--ci-blue-dark), var(--ci-turquoise));
        color: white;
        padding: 0.78rem 1.25rem;
        font-weight: 800;
        box-shadow: 0 12px 28px rgba(10, 98, 255, 0.22);
        transition: all 0.2s ease;
    }

    div.stButton > button:first-child:hover,
    div.stFormSubmitButton > button:first-child:hover {
        transform: translateY(-1px);
        box-shadow: 0 16px 34px rgba(10, 98, 255, 0.28);
        color: white;
    }

    div.stDownloadButton > button:first-child {
        border-radius: 16px;
        border: 1px solid var(--ci-blue);
        background: white;
        color: var(--ci-blue-dark);
        padding: 0.78rem 1.25rem;
        font-weight: 800;
    }

    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, var(--ci-blue), var(--ci-turquoise));
    }

    div[data-baseweb="radio"] label {
        background: white;
        border: 1px solid rgba(20,130,255,0.18);
        border-radius: 14px;
        padding: 8px 10px;
        margin-right: 8px;
    }

    a {
        color: var(--ci-blue-dark);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------
# DADOS DA APLICAÇÃO
# -------------------------
DIAGNOSTICO = [
    {
        "pergunta": "A empresa tem regras claras para criação e utilização de passwords?",
        "tema": "Passwords",
        "peso": 2,
    },
    {
        "pergunta": "Os colaboradores usam autenticação multifator nos acessos principais?",
        "tema": "Autenticação multifator",
        "peso": 3,
    },
    {
        "pergunta": "Existe formação ou sensibilização regular sobre phishing e emails fraudulentos?",
        "tema": "Phishing",
        "peso": 3,
    },
    {
        "pergunta": "Os colaboradores sabem a quem reportar um email, link ou anexo suspeito?",
        "tema": "Reporte de incidentes",
        "peso": 3,
    },
    {
        "pergunta": "A empresa realiza backups regulares da informação crítica?",
        "tema": "Backups",
        "peso": 3,
    },
    {
        "pergunta": "Os computadores e softwares são atualizados regularmente?",
        "tema": "Atualizações",
        "peso": 2,
    },
    {
        "pergunta": "Existe cuidado com a partilha de dados pessoais ou informação confidencial?",
        "tema": "Proteção de dados",
        "peso": 2,
    },
    {
        "pergunta": "A empresa tem um procedimento simples para agir em caso de incidente informático?",
        "tema": "Resposta a incidentes",
        "peso": 3,
    },
]

SIMULACOES = [
    {
        "titulo": "Email urgente da Microsoft",
        "categoria": "Phishing",
        "cenario": "Recebe um email com o assunto: 'A sua conta Microsoft será bloqueada hoje. Clique aqui para validar os seus dados'.",
        "opcoes": [
            "Clico no link para evitar o bloqueio da conta.",
            "Respondo ao email a pedir mais informação.",
            "Verifico o remetente, não clico no link e reporto internamente.",
            "Encaminho para todos os colegas para avisar.",
        ],
        "correta": 2,
        "explicacao": "Emails com urgência, ameaça de bloqueio e links de validação são sinais comuns de phishing. O comportamento seguro é validar o remetente e reportar.",
        "recomendacao": "Criar um procedimento simples: não clicar, validar, reportar.",
    },
    {
        "titulo": "Password mais segura",
        "categoria": "Passwords",
        "cenario": "Qual destas passwords apresenta melhor prática de segurança?",
        "opcoes": [
            "Empresa2026",
            "Ciber123",
            "Verissimo@2026",
            "CaféAzul!Rio77#Porta",
        ],
        "correta": 3,
        "explicacao": "Passwords longas, únicas e menos previsíveis são mais seguras. O ideal é usar gestor de passwords e autenticação multifator.",
        "recomendacao": "Promover passwords longas, únicas e MFA nos serviços críticos.",
    },
    {
        "titulo": "Fatura suspeita em anexo",
        "categoria": "Malware/Ransomware",
        "cenario": "Recebe uma fatura de uma empresa desconhecida com o ficheiro 'Fatura_urgente.exe'.",
        "opcoes": [
            "Abro o ficheiro para confirmar se é verdadeiro.",
            "Apago ou reporto como suspeito sem abrir.",
            "Envio a um colega para abrir noutro computador.",
            "Guardo no ambiente de trabalho para analisar mais tarde.",
        ],
        "correta": 1,
        "explicacao": "Ficheiros executáveis podem instalar malware ou ransomware. Nunca devem ser abertos sem validação.",
        "recomendacao": "Sensibilizar equipas para anexos perigosos e extensões suspeitas.",
    },
    {
        "titulo": "Pedido do diretor por WhatsApp",
        "categoria": "Engenharia social",
        "cenario": "Recebe uma mensagem a dizer: 'Sou o diretor. Preciso que faças uma transferência urgente. Não ligues, estou em reunião'.",
        "opcoes": [
            "Faço a transferência porque parece urgente.",
            "Peço dados bancários completos por mensagem.",
            "Valido o pedido por outro canal oficial antes de agir.",
            "Encaminho para outro colega tratar.",
        ],
        "correta": 2,
        "explicacao": "Ataques de engenharia social exploram urgência, autoridade e pressão. Pedidos financeiros devem ser sempre confirmados por canal alternativo.",
        "recomendacao": "Definir regra interna: pagamentos urgentes exigem dupla validação.",
    },
    {
        "titulo": "Wi-Fi público",
        "categoria": "Teletrabalho",
        "cenario": "Está num café e precisa de aceder a documentos internos da empresa através de uma rede Wi-Fi pública.",
        "opcoes": [
            "Uso a rede pública sem problema.",
            "Acedo apenas se usar ligação segura/VPN e evitar informação sensível.",
            "Peço a password do Wi-Fi a outro cliente.",
            "Envio os documentos para o meu email pessoal para abrir depois.",
        ],
        "correta": 1,
        "explicacao": "Redes públicas aumentam o risco de interceção. Deve usar ligação segura, VPN quando aplicável, e evitar dados sensíveis.",
        "recomendacao": "Criar boas práticas para teletrabalho, acessos remotos e dispositivos pessoais.",
    },
    {
        "titulo": "Cliquei num link suspeito",
        "categoria": "Resposta a incidentes",
        "cenario": "Um colaborador percebe que clicou num link suspeito e introduziu a password da empresa.",
        "opcoes": [
            "Não diz nada para evitar problemas.",
            "Muda a password e reporta imediatamente ao responsável interno.",
            "Continua a trabalhar normalmente.",
            "Desliga o computador e só fala no dia seguinte.",
        ],
        "correta": 1,
        "explicacao": "Reportar rapidamente permite reduzir impacto, bloquear acessos e evitar propagação do ataque.",
        "recomendacao": "Promover uma cultura sem culpa: reportar cedo é proteger a empresa.",
    },
]

NIVEIS_RESPOSTA = {
    "Sim": 1.0,
    "Parcialmente": 0.5,
    "Não": 0.0,
    "Não sei": 0.0,
}

# -------------------------
# LOGÓTIPO
# -------------------------
def encontrar_logo_local():
    """Procura automaticamente um ficheiro de logótipo na mesma pasta da aplicação."""
    for ficheiro in LOGO_FICHEIROS:
        caminho = Path(ficheiro)
        if caminho.exists():
            return str(caminho)
    return None


def mostrar_logo(largura=240, sidebar=False):
    """Mostra o logótipo da CiberImpacto se existir. Caso contrário, mostra uma versão textual elegante."""
    logo_bytes = st.session_state.get("logo_bytes")
    logo_local = encontrar_logo_local()

    if logo_bytes:
        st.image(io.BytesIO(logo_bytes), width=largura)
        return

    if logo_local:
        st.image(logo_local, width=largura)
        return

    # Fallback caso ainda não exista um ficheiro de logótipo carregado
    if sidebar:
        st.markdown(
            """
            <div style="padding:14px 0 8px 0;">
                <div style="font-size:1.45rem;font-weight:900;line-height:1;color:white;">💡 CiberImpacto</div>
                <div style="font-size:0.75rem;opacity:.86;text-transform:uppercase;letter-spacing:.08em;margin-top:6px;">Formação e Eventos</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div class="brand-logo-fallback">
                <div class="bulb">💡</div>
                <div>
                    <div class="brand-name">CiberImpacto</div>
                    <div class="brand-subtitle">Formação e Eventos</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# -------------------------
# FUNÇÕES
# -------------------------
def init_state():
    defaults = {
        "etapa": "inicio",
        "empresa": "",
        "nome": "",
        "email": "",
        "perfil": "Gestor/RH",
        "colaboradores": 1,
        "diagnostico": {},
        "simulacao_atual": 0,
        "respostas_simulacao": [],
        "feedback_atual": None,
        "terminado": False,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def reset_app():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()


def calcular_pontuacao_diagnostico():
    total_possivel = sum(item["peso"] for item in DIAGNOSTICO)
    total_obtido = 0
    pontos_fracos = []

    for i, item in enumerate(DIAGNOSTICO):
        resposta = st.session_state.diagnostico.get(i, "Não sei")
        valor = NIVEIS_RESPOSTA.get(resposta, 0)
        total_obtido += valor * item["peso"]
        if valor < 1:
            pontos_fracos.append(item["tema"])

    percentagem = round((total_obtido / total_possivel) * 100) if total_possivel else 0
    return percentagem, pontos_fracos


def calcular_pontuacao_simulacoes():
    total = len(SIMULACOES)
    certas = sum(1 for r in st.session_state.respostas_simulacao if r.get("correta") is True)
    percentagem = round((certas / total) * 100) if total else 0
    return percentagem, certas, total


def calcular_risco(percentagem_final):
    if percentagem_final >= 85:
        return "Baixo", "risk-low", "✅", "A empresa demonstra boas práticas, mas deve manter sensibilização regular."
    if percentagem_final >= 65:
        return "Médio", "risk-medium", "⚠️", "Existem boas práticas, mas ainda há fragilidades que podem ser exploradas."
    if percentagem_final >= 45:
        return "Alto", "risk-high", "🚨", "A empresa apresenta exposição relevante a riscos digitais e deve atuar rapidamente."
    return "Crítico", "risk-critical", "🛑", "A empresa apresenta fragilidades significativas e necessita de medidas urgentes."


def gerar_recomendacoes(pontos_fracos, simulacoes_erradas):
    recomendacoes = []

    if "Phishing" in pontos_fracos or "Phishing" in simulacoes_erradas:
        recomendacoes.append("Realizar uma sessão prática sobre phishing, emails fraudulentos, links e anexos suspeitos.")
    if "Passwords" in pontos_fracos or "Passwords" in simulacoes_erradas:
        recomendacoes.append("Implementar regras de passwords longas, únicas e autenticação multifator nos acessos principais.")
    if "Reporte de incidentes" in pontos_fracos or "Resposta a incidentes" in pontos_fracos or "Resposta a incidentes" in simulacoes_erradas:
        recomendacoes.append("Criar um procedimento simples para reporte de incidentes: quem contactar, como reportar e o que fazer nos primeiros minutos.")
    if "Backups" in pontos_fracos:
        recomendacoes.append("Validar se existem backups regulares, testados e protegidos contra ransomware.")
    if "Proteção de dados" in pontos_fracos:
        recomendacoes.append("Reforçar boas práticas de proteção de dados pessoais, partilha segura e confidencialidade da informação.")
    if "Teletrabalho" in simulacoes_erradas:
        recomendacoes.append("Definir regras para teletrabalho, redes Wi-Fi públicas, dispositivos pessoais e acesso remoto seguro.")
    if "Engenharia social" in simulacoes_erradas:
        recomendacoes.append("Sensibilizar chefias e equipas administrativas para fraudes por identidade falsa, pressão e pedidos urgentes.")

    if not recomendacoes:
        recomendacoes.append("Manter campanhas regulares de sensibilização para consolidar boas práticas e reduzir o risco humano.")

    return recomendacoes


def criar_relatorio_texto(percentagem_final, nivel, mensagem, pontos_fracos, recomendacoes):
    data = datetime.now().strftime("%d/%m/%Y %H:%M")
    simulacao_percentagem, certas, total = calcular_pontuacao_simulacoes()
    diagnostico_percentagem, _ = calcular_pontuacao_diagnostico()

    relatorio = f"""
RELATÓRIO DE CHECK-UP DIGITAL
CiberImpacto – Formação e Eventos
Data: {data}

DADOS DA EMPRESA
Empresa: {st.session_state.empresa or 'Não indicado'}
Contacto: {st.session_state.nome or 'Não indicado'}
Email: {st.session_state.email or 'Não indicado'}
Perfil: {st.session_state.perfil}
Número aproximado de colaboradores: {st.session_state.colaboradores}

RESULTADO GLOBAL
Nível de risco: {nivel}
Pontuação final: {percentagem_final}%
Mensagem: {mensagem}

PONTUAÇÕES
Diagnóstico da empresa: {diagnostico_percentagem}%
Simulações práticas: {simulacao_percentagem}%
Respostas corretas nas simulações: {certas}/{total}

PRINCIPAIS PONTOS A MELHORAR
{chr(10).join('- ' + p for p in sorted(set(pontos_fracos))) if pontos_fracos else '- Sem pontos críticos identificados no diagnóstico.'}

RECOMENDAÇÕES
{chr(10).join('- ' + r for r in recomendacoes)}

SUGESTÃO CIBERIMPACTO
Recomenda-se uma ação prática de sensibilização em cibersegurança de 4h ou uma formação certificada de 10h,
adaptada à realidade da empresa, com foco em phishing, passwords, engenharia social, proteção de dados e reporte de incidentes.

CONTACTO
CiberImpacto – Formação e Eventos
Email: catia.verissimo@ciberimpacto.pt
Website: www.ciberimpacto.pt
"""
    return relatorio.strip()


def criar_csv_respostas():
    linhas = []

    for i, item in enumerate(DIAGNOSTICO):
        linhas.append(
            {
                "tipo": "Diagnóstico",
                "tema": item["tema"],
                "questao": item["pergunta"],
                "resposta": st.session_state.diagnostico.get(i, "Não respondido"),
                "correta": "N/A",
            }
        )

    for resposta in st.session_state.respostas_simulacao:
        linhas.append(
            {
                "tipo": "Simulação",
                "tema": resposta["categoria"],
                "questao": resposta["titulo"],
                "resposta": resposta["resposta"],
                "correta": "Sim" if resposta["correta"] else "Não",
            }
        )

    df = pd.DataFrame(linhas)
    buffer = io.StringIO()
    df.to_csv(buffer, index=False, sep=";")
    return buffer.getvalue()

# -------------------------
# ECRÃS
# -------------------------
def ecra_inicio():
    mostrar_logo(largura=260)
    st.markdown(
        """
        <div class="hero">
            <div class="hero-badge">🔐 Check-Up Digital para Empresas</div>
            <h1>A sua empresa está preparada para evitar ataques informáticos?</h1>
            <p>Uma experiência simples, visual e intuitiva para sensibilizar colaboradores sobre phishing, passwords, ransomware, engenharia social e resposta a incidentes.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="card">
            <h3>Descubra em poucos minutos o nível de exposição da sua empresa</h3>
            <div class="highlight-line"></div>
            <p>O utilizador responde a perguntas simples, passa por simulações práticas e recebe um resultado visual com recomendações.</p>
            <p class="small-text">Ideal para usar em reuniões comerciais, campanhas de sensibilização, ações internas de RH ou como diagnóstico inicial antes de uma formação.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("form_inicio"):
        st.subheader("Dados iniciais")
        col1, col2 = st.columns(2)
        with col1:
            empresa = st.text_input("Nome da empresa", placeholder="Ex.: Empresa XPTO")
            nome = st.text_input("Nome do contacto", placeholder="Ex.: Ana Silva")
        with col2:
            email = st.text_input("Email", placeholder="Ex.: contacto@empresa.pt")
            colaboradores = st.number_input("N.º aproximado de colaboradores", min_value=1, max_value=10000, value=10)

        perfil = st.radio("Perfil", ["Gestor/RH", "Colaborador", "Direção", "Outro"], horizontal=True)
        submitted = st.form_submit_button("Começar check-up")

        if submitted:
            st.session_state.empresa = empresa
            st.session_state.nome = nome
            st.session_state.email = email
            st.session_state.colaboradores = colaboradores
            st.session_state.perfil = perfil
            st.session_state.etapa = "diagnostico"
            st.rerun()


def ecra_diagnostico():
    st.title("1. Diagnóstico rápido da empresa")
    st.write("Responda de forma simples. O objetivo é perceber o nível de maturidade atual, não fazer uma auditoria técnica.")

    st.progress(0.25)

    with st.form("form_diagnostico"):
        for i, item in enumerate(DIAGNOSTICO):
            st.markdown(f"<div class='mini-card'><strong>{i+1}. {item['pergunta']}</strong></div>", unsafe_allow_html=True)
            resposta = st.radio(
                label="Escolha uma opção:",
                options=["Sim", "Parcialmente", "Não", "Não sei"],
                horizontal=True,
                key=f"diag_{i}",
                label_visibility="collapsed",
            )
            st.session_state.diagnostico[i] = resposta

        submitted = st.form_submit_button("Avançar para simulações práticas")
        if submitted:
            st.session_state.etapa = "simulacoes"
            st.session_state.simulacao_atual = 0
            st.session_state.respostas_simulacao = []
            st.session_state.feedback_atual = None
            st.rerun()


def ecra_simulacoes():
    idx = st.session_state.simulacao_atual
    total = len(SIMULACOES)
    item = SIMULACOES[idx]

    st.title("2. Simulações práticas")
    st.write("Leia a situação e escolha o comportamento mais seguro.")
    st.progress(0.25 + ((idx + 1) / total) * 0.5)

    st.markdown(
        f"""
        <div class="card">
            <p class="small-text">Simulação {idx + 1} de {total} · {item['categoria']}</p>
            <h3>{item['titulo']}</h3>
            <p>{item['cenario']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    escolha = st.radio("O que faria?", item["opcoes"], index=None)

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Validar resposta", disabled=escolha is None):
            indice_escolha = item["opcoes"].index(escolha)
            correta = indice_escolha == item["correta"]
            st.session_state.feedback_atual = {
                "correta": correta,
                "resposta": escolha,
                "explicacao": item["explicacao"],
                "recomendacao": item["recomendacao"],
            }

    if st.session_state.feedback_atual:
        feedback = st.session_state.feedback_atual
        if feedback["correta"]:
            st.success("Resposta correta. Boa decisão de segurança!")
        else:
            st.error("Resposta incorreta. Esta situação pode representar risco para a empresa.")

        st.info(feedback["explicacao"])
        st.markdown(f"**Recomendação:** {feedback['recomendacao']}")

        with col2:
            if st.button("Seguinte"):
                st.session_state.respostas_simulacao.append(
                    {
                        "titulo": item["titulo"],
                        "categoria": item["categoria"],
                        "resposta": feedback["resposta"],
                        "correta": feedback["correta"],
                    }
                )
                st.session_state.feedback_atual = None

                if idx + 1 < total:
                    st.session_state.simulacao_atual += 1
                    st.rerun()
                else:
                    st.session_state.etapa = "resultado"
                    st.rerun()


def ecra_resultado():
    diagnostico_percentagem, pontos_fracos = calcular_pontuacao_diagnostico()
    simulacao_percentagem, certas, total = calcular_pontuacao_simulacoes()
    percentagem_final = round((diagnostico_percentagem * 0.45) + (simulacao_percentagem * 0.55))
    nivel, classe, icone, mensagem = calcular_risco(percentagem_final)

    simulacoes_erradas = [r["categoria"] for r in st.session_state.respostas_simulacao if not r["correta"]]
    recomendacoes = gerar_recomendacoes(pontos_fracos, simulacoes_erradas)
    relatorio = criar_relatorio_texto(percentagem_final, nivel, mensagem, pontos_fracos, recomendacoes)
    csv_respostas = criar_csv_respostas()

    st.title("3. Resultado do check-up")
    st.progress(1.0)

    st.markdown(
        f"""
        <div class="{classe}">
            <h2>{icone} Risco {nivel}</h2>
            <p>{mensagem}</p>
            <h3>Pontuação final: {percentagem_final}%</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    col1, col2, col3 = st.columns(3)
    col1.metric("Diagnóstico", f"{diagnostico_percentagem}%")
    col2.metric("Simulações", f"{simulacao_percentagem}%")
    col3.metric("Respostas certas", f"{certas}/{total}")

    st.subheader("Principais pontos a melhorar")
    if pontos_fracos or simulacoes_erradas:
        temas = sorted(set(pontos_fracos + simulacoes_erradas))
        for tema in temas:
            st.markdown(f"- **{tema}**")
    else:
        st.markdown("- Não foram identificados pontos críticos, mas recomenda-se sensibilização contínua.")

    st.subheader("Recomendações práticas")
    for rec in recomendacoes:
        st.markdown(f"✅ {rec}")

    st.markdown(
        """
        <div class="card">
            <h3>Sugestão CiberImpacto</h3>
            <p>Recomenda-se uma ação prática de sensibilização em cibersegurança de <strong>4h</strong> ou uma formação certificada de <strong>10h</strong>, adaptada à realidade da empresa.</p>
            <p class="small-text">Temas sugeridos: phishing, passwords, autenticação multifator, engenharia social, proteção de dados, teletrabalho e reporte de incidentes.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("Gerar relatório")
    col_a, col_b = st.columns(2)
    with col_a:
        st.download_button(
            label="Descarregar relatório TXT",
            data=relatorio,
            file_name="relatorio_checkup_digital_ciberimpacto.txt",
            mime="text/plain",
        )
    with col_b:
        st.download_button(
            label="Descarregar respostas CSV",
            data=csv_respostas,
            file_name="respostas_checkup_digital.csv",
            mime="text/csv",
        )

    with st.expander("Ver relatório completo"):
        st.text(relatorio)

    col_reset, _ = st.columns([1, 2])
    with col_reset:
        if st.button("Reiniciar check-up"):
            reset_app()


def sidebar():
    with st.sidebar:
        mostrar_logo(largura=190, sidebar=True)
        st.write("**Check-Up Digital**")
        st.caption("Ferramenta de sensibilização e diagnóstico inicial.")

        uploaded_logo = st.file_uploader(
            "Carregar logótipo",
            type=["png", "jpg", "jpeg", "webp"],
            help="Opcional. Para ficar permanente no GitHub, coloque o ficheiro com o nome logo_ciberimpacto.png na mesma pasta da aplicação.",
        )
        if uploaded_logo is not None:
            st.session_state.logo_bytes = uploaded_logo.getvalue()
            st.success("Logótipo carregado nesta sessão.")

        st.divider()
        st.write("**Percurso:**")
        st.write("1. Dados iniciais")
        st.write("2. Diagnóstico rápido")
        st.write("3. Simulações práticas")
        st.write("4. Resultado e relatório")
        st.divider()
        if st.button("Recomeçar"):
            reset_app()

# -------------------------
# EXECUÇÃO
# -------------------------
init_state()
sidebar()

if st.session_state.etapa == "inicio":
    ecra_inicio()
elif st.session_state.etapa == "diagnostico":
    ecra_diagnostico()
elif st.session_state.etapa == "simulacoes":
    ecra_simulacoes()
elif st.session_state.etapa == "resultado":
    ecra_resultado()

st.markdown(
    """
    <div class="footer">
        <strong>CiberImpacto – Formação e Eventos</strong> · Segurança digital com impacto real
    </div>
    """,
    unsafe_allow_html=True,
)
