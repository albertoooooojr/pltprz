"""
PLATAFORMA DE GESTÃO PRIORIZE - VERSÃO DEMONSTRATIVA
Sistema de Gestão de Riscos Psicossociais - NR-01
Versão: APRESENTAÇÃO - Dados fictícios para demonstração
"""

import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
import uuid
import random

# ============================================
# CONFIGURAÇÕES
# ============================================

st.set_page_config(
    page_title="Priorize - Gestão de Riscos Psicossociais",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# DADOS FICTÍCIOS - EMPRESAS
# ============================================

EMPRESAS_FICTICIAS = pd.DataFrame([
    {
        'id': 'EMP001',
        'nome': 'Tech Solutions Brasil',
        'razao_social': 'TECH SOLUTIONS BRASIL LTDA',
        'cnpj': '12.345.678/0001-90',
        'email': 'contato@techsolutions.com.br',
        'telefone': '(11) 3456-7890',
        'data_cadastro': '2025-01-15',
        'status': 'Ativo'
    },
    {
        'id': 'EMP002',
        'nome': 'Indústria Nova Friburgo',
        'razao_social': 'NOVA FRIBURGO INDÚSTRIA S.A.',
        'cnpj': '23.456.789/0001-01',
        'email': 'rh@novafriburgo.ind.br',
        'telefone': '(21) 4567-8901',
        'data_cadastro': '2025-02-10',
        'status': 'Ativo'
    },
    {
        'id': 'EMP003',
        'nome': 'Farmácia Bem Estar',
        'razao_social': 'BEM ESTAR FARMÁCIAS LTDA',
        'cnpj': '34.567.890/0001-12',
        'email': 'gestao@bemestar.com.br',
        'telefone': '(31) 5678-9012',
        'data_cadastro': '2025-03-05',
        'status': 'Ativo'
    },
    {
        'id': 'EMP004',
        'nome': 'Logística Rápida',
        'razao_social': 'LOGÍSTICA RÁPIDA TRANSPORTES S.A.',
        'cnpj': '45.678.901/0001-23',
        'email': 'rh@logisticarapida.com.br',
        'telefone': '(41) 6789-0123',
        'data_cadastro': '2025-04-20',
        'status': 'Prospect'
    },
    {
        'id': 'EMP005',
        'nome': 'Construção Civil Sigma',
        'razao_social': 'SIGMA CONSTRUÇÃO CIVIL LTDA',
        'cnpj': '56.789.012/0001-34',
        'email': 'contato@sigma.com.br',
        'telefone': '(51) 7890-1234',
        'data_cadastro': '2025-05-12',
        'status': 'Inativo'
    }
])

# ============================================
# DADOS FICTÍCIOS - PSICÓLOGOS
# ============================================

PSICOLOGOS_FICTICIOS = pd.DataFrame([
    {'id': 'PSI001', 'nome': 'Dra. Ana Paula Mendes', 'email': 'ana.mendes@psi.com', 'telefone': '(11) 99999-1111',
     'especialidade': 'Psicologia Organizacional', 'status': 'Ativo', 'data_cadastro': '2024-10-10'},
    {'id': 'PSI002', 'nome': 'Dr. Carlos Roberto Silva', 'email': 'carlos.silva@psi.com', 'telefone': '(11) 99999-2222',
     'especialidade': 'Psicologia Clínica', 'status': 'Ativo', 'data_cadastro': '2024-11-15'},
    {'id': 'PSI003', 'nome': 'Dra. Fernanda Lima', 'email': 'fernanda.lima@psi.com', 'telefone': '(11) 99999-3333',
     'especialidade': 'Neuropsicologia', 'status': 'Ativo', 'data_cadastro': '2025-01-20'},
    {'id': 'PSI004', 'nome': 'Dr. Ricardo Alves', 'email': 'ricardo.alves@psi.com', 'telefone': '(11) 99999-4444',
     'especialidade': 'Psicologia Social', 'status': 'Inativo', 'data_cadastro': '2024-09-05'},
    {'id': 'PSI005', 'nome': 'Dra. Mariana Costa', 'email': 'mariana.costa@psi.com', 'telefone': '(11) 99999-5555',
     'especialidade': 'Psicologia Organizacional', 'status': 'Ativo', 'data_cadastro': '2025-02-28'}
])

# ============================================
# DADOS FICTÍCIOS - CONTRATOS
# ============================================

hoje = datetime.now()

CONTRATOS_FICTICIOS = pd.DataFrame([
    {
        'id': 'CTR001',
        'id_empresa': 'EMP001',
        'nome_empresa': 'Tech Solutions Brasil',
        'tipo_servico': 'NR1 - Diagnóstico Psicossocial Completo',
        'limite_entrevistas': 45,
        'entrevistas_realizadas': 38,
        'data_inicio': '2025-06-01',
        'data_fim': (hoje + timedelta(days=25)).strftime("%Y-%m-%d"),
        'status': 'Ativo',
        'valor': 22500.00
    },
    {
        'id': 'CTR002',
        'id_empresa': 'EMP002',
        'nome_empresa': 'Indústria Nova Friburgo',
        'tipo_servico': 'NR1 - Programa de Saúde Mental',
        'limite_entrevistas': 80,
        'entrevistas_realizadas': 52,
        'data_inicio': '2025-07-15',
        'data_fim': (hoje + timedelta(days=95)).strftime("%Y-%m-%d"),
        'status': 'Ativo',
        'valor': 42000.00
    },
    {
        'id': 'CTR003',
        'id_empresa': 'EMP003',
        'nome_empresa': 'Farmácia Bem Estar',
        'tipo_servico': 'NR1 - Acompanhamento Contínuo',
        'limite_entrevistas': 30,
        'entrevistas_realizadas': 30,
        'data_inicio': '2025-08-10',
        'data_fim': (hoje - timedelta(days=15)).strftime("%Y-%m-%d"),
        'status': 'Encerrado',
        'valor': 15000.00
    },
    {
        'id': 'CTR004',
        'id_empresa': 'EMP004',
        'nome_empresa': 'Logística Rápida',
        'tipo_servico': 'NR1 - Diagnóstico Inicial',
        'limite_entrevistas': 25,
        'entrevistas_realizadas': 0,
        'data_inicio': (hoje - timedelta(days=5)).strftime("%Y-%m-%d"),
        'data_fim': (hoje + timedelta(days=355)).strftime("%Y-%m-%d"),
        'status': 'Ativo',
        'valor': 12500.00
    },
    {
        'id': 'CTR005',
        'id_empresa': 'EMP005',
        'nome_empresa': 'Construção Civil Sigma',
        'tipo_servico': 'NR1 - Programa Completo',
        'limite_entrevistas': 60,
        'entrevistas_realizadas': 18,
        'data_inicio': '2025-09-01',
        'data_fim': (hoje + timedelta(days=60)).strftime("%Y-%m-%d"),
        'status': 'Suspenso',
        'valor': 35000.00
    }
])

# ============================================
# DADOS FICTÍCIOS - ENTREVISTAS
# ============================================

entrevistas_lista = []
id_counter = 1

psicologos_nomes = PSICOLOGOS_FICTICIOS[PSICOLOGOS_FICTICIOS['status'] == 'Ativo']['nome'].tolist()

# Setores e cargos fictícios por empresa
setores_por_empresa = {
    'Tech Solutions Brasil': ['Desenvolvimento', 'Suporte Técnico', 'Vendas', 'Marketing', 'RH'],
    'Indústria Nova Friburgo': ['Produção', 'Manutenção', 'Logística', 'Qualidade', 'Administração'],
    'Farmácia Bem Estar': ['Farmácia', 'Atendimento', 'Administração', 'Estoque'],
    'Logística Rápida': ['Transporte', 'Armazenagem', 'Expedição', 'Frota'],
    'Construção Civil Sigma': ['Obras', 'Engenharia', 'Projetos', 'Compras']
}

cargos_por_empresa = {
    'Tech Solutions Brasil': ['Analista', 'Coordenador', 'Desenvolvedor', 'Suporte', 'Gerente'],
    'Indústria Nova Friburgo': ['Operador', 'Técnico', 'Supervisor', 'Inspetor', 'Analista'],
    'Farmácia Bem Estar': ['Farmacêutico', 'Atendente', 'Auxiliar', 'Coordenador'],
    'Logística Rápida': ['Motorista', 'Auxiliar', 'Coordenador', 'Analista'],
    'Construção Civil Sigma': ['Pedreiro', 'Mestre de Obras', 'Engenheiro', 'Auxiliar']
}

for _, contrato in CONTRATOS_FICTICIOS.iterrows():
    empresa = contrato['nome_empresa']
    limite = contrato['limite_entrevistas']
    realizadas = contrato['entrevistas_realizadas']

    setores = setores_por_empresa.get(empresa, ['Setor Geral'])
    cargos = cargos_por_empresa.get(empresa, ['Cargo Geral'])

    for i in range(realizadas):
        data_entrevista = datetime.now() - timedelta(days=random.randint(1, 180))

        entrevistas_lista.append({
            'id': f'ENT{id_counter:04d}',
            'id_empresa': contrato['id_empresa'],
            'id_contrato': contrato['id'],
            'nome_empresa': empresa,
            'id_psicologo': f'PSI{random.randint(1, 3):03d}',
            'psicologo': random.choice(psicologos_nomes),
            'data_entrevista': data_entrevista.strftime("%Y-%m-%d"),
            'setor': random.choice(setores),
            'cargo': random.choice(cargos),
            'status': 'Realizada'
        })
        id_counter += 1

# Adicionar algumas entrevistas futuras agendadas
for i in range(15):
    empresa_ativa = random.choice([c for c in CONTRATOS_FICTICIOS.iterrows() if c[1]['status'] == 'Ativo'])[1]
    data_futura = datetime.now() + timedelta(days=random.randint(1, 30))

    entrevistas_lista.append({
        'id': f'ENT{id_counter:04d}',
        'id_empresa': empresa_ativa['id_empresa'],
        'id_contrato': empresa_ativa['id'],
        'nome_empresa': empresa_ativa['nome_empresa'],
        'id_psicologo': f'PSI00{random.randint(1, 3)}',
        'psicologo': random.choice(psicologos_nomes),
        'data_entrevista': data_futura.strftime("%Y-%m-%d"),
        'setor': random.choice(setores_por_empresa.get(empresa_ativa['nome_empresa'], ['Setor Geral'])),
        'cargo': random.choice(cargos_por_empresa.get(empresa_ativa['nome_empresa'], ['Cargo Geral'])),
        'status': 'Agendada'
    })
    id_counter += 1

ENTREVISTAS_FICTICIAS = pd.DataFrame(entrevistas_lista)

# ============================================
# DADOS FICTÍCIOS - ATIVIDADES
# ============================================

atividades_lista = []
hoje = datetime.now()

atividades_exemplo = [
    {'titulo': '📊 Reunião de Resultados', 'descricao': 'Apresentação do diagnóstico de riscos psicossociais',
     'tipo': 'reuniao', 'dias': 3, 'empresa': 'Tech Solutions Brasil'},
    {'titulo': '📝 Entrevistas Diagnósticas', 'descricao': 'Aplicação de entrevistas com colaboradores',
     'tipo': 'entrevista', 'dias': 5, 'empresa': 'Indústria Nova Friburgo'},
    {'titulo': '📋 Vencimento de Contrato', 'descricao': 'Prazo final para reavaliação', 'tipo': 'prazo', 'dias': 25,
     'empresa': 'Tech Solutions Brasil'},
    {'titulo': '🎓 Treinamento - Gestão do Estresse', 'descricao': 'Workshop de inteligência emocional para líderes',
     'tipo': 'treinamento', 'dias': 10, 'empresa': 'Indústria Nova Friburgo'},
    {'titulo': '📝 Reavaliação Diagnóstica', 'descricao': 'Reaplicação do DRPS (5 meses após inicial)',
     'tipo': 'entrevista', 'dias': 30, 'empresa': 'Farmácia Bem Estar'},
    {'titulo': '🎓 Treinamento - Comunicação Assertiva', 'descricao': 'Programa de comunicação não violenta',
     'tipo': 'treinamento', 'dias': 7, 'empresa': 'Tech Solutions Brasil'},
    {'titulo': '📊 Análise de Resultados', 'descricao': 'Análise dos dados coletados', 'tipo': 'reuniao', 'dias': 15,
     'empresa': 'Logística Rápida'},
    {'titulo': '📋 Renovação de Contrato', 'descricao': 'Proposta de renovação', 'tipo': 'prazo', 'dias': 45,
     'empresa': 'Indústria Nova Friburgo'},
    {'titulo': '🎓 Workshop - Saúde Mental', 'descricao': 'Palestra sobre prevenção ao burnout', 'tipo': 'treinamento',
     'dias': 20, 'empresa': 'Construção Civil Sigma'},
]

for i, ativ in enumerate(atividades_exemplo, 1):
    data_atividade = hoje + timedelta(days=ativ['dias'])
    atividades_lista.append({
        'id': f'ACT{i:03d}',
        'titulo': ativ['titulo'],
        'descricao': ativ['descricao'],
        'data': data_atividade.strftime("%Y-%m-%d"),
        'hora': f"{random.randint(8, 17)}:00",
        'tipo': ativ['tipo'],
        'status': 'pendente',
        'id_empresa': EMPRESAS_FICTICIAS[EMPRESAS_FICTICIAS['nome'] == ativ['empresa']]['id'].values[0],
        'empresa_nome': ativ['empresa']
    })

# Adicionar atividades concluídas
atividades_concluidas = [
    {'titulo': '📊 Entrega de Relatório', 'descricao': 'Diagnóstico final entregue', 'dias': -10,
     'empresa': 'Farmácia Bem Estar'},
    {'titulo': '📝 Entrevistas Iniciais', 'descricao': 'Coleta de dados concluída', 'dias': -15,
     'empresa': 'Tech Solutions Brasil'},
]

for i, ativ in enumerate(atividades_concluidas, len(atividades_exemplo) + 1):
    data_atividade = hoje + timedelta(days=ativ['dias'])
    atividades_lista.append({
        'id': f'ACT{i:03d}',
        'titulo': ativ['titulo'],
        'descricao': ativ['descricao'],
        'data': data_atividade.strftime("%Y-%m-%d"),
        'hora': f"{random.randint(8, 17)}:00",
        'tipo': 'reuniao',
        'status': 'concluido',
        'id_empresa': EMPRESAS_FICTICIAS[EMPRESAS_FICTICIAS['nome'] == ativ['empresa']]['id'].values[0],
        'empresa_nome': ativ['empresa']
    })

ATIVIDADES_FICTICIAS = pd.DataFrame(atividades_lista)


# ============================================
# FUNÇÕES AUXILIARES
# ============================================

def formatar_moeda(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def calcular_tempo_restante(data_fim):
    try:
        fim = datetime.strptime(data_fim, "%Y-%m-%d")
        dias = (fim - datetime.now()).days
        if dias > 0:
            return f"{dias} dias restantes"
        elif dias == 0:
            return "Vence hoje!"
        else:
            return f"Vencido há {abs(dias)} dias"
    except:
        return "Data inválida"


# ============================================
# PÁGINAS
# ============================================

def pagina_inicio():
    st.title("🏢 Plataforma de Gestão Priorize")
    st.markdown("---")

    # KPIs
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric("Empresas Ativas", len(EMPRESAS_FICTICIAS[EMPRESAS_FICTICIAS['status'] == 'Ativo']))
    with col2:
        st.metric("Contratos Ativos", len(CONTRATOS_FICTICIOS[CONTRATOS_FICTICIOS['status'] == 'Ativo']))
    with col3:
        st.metric("Psicólogos Ativos", len(PSICOLOGOS_FICTICIOS[PSICOLOGOS_FICTICIOS['status'] == 'Ativo']))
    with col4:
        st.metric("Entrevistas Realizadas", len(ENTREVISTAS_FICTICIAS[ENTREVISTAS_FICTICIAS['status'] == 'Realizada']))
    with col5:
        total_faturamento = CONTRATOS_FICTICIOS['valor'].sum()
        st.metric("Faturamento Total", formatar_moeda(total_faturamento))

    st.markdown("---")

    # Gráficos
    col1, col2 = st.columns(2)

    with col1:
        faturamento_empresa = CONTRATOS_FICTICIOS.groupby('nome_empresa')['valor'].sum().reset_index()
        fig = px.bar(faturamento_empresa, x='nome_empresa', y='valor',
                     title='💰 Faturamento por Empresa',
                     labels={'valor': 'Valor (R$)', 'nome_empresa': ''},
                     text='valor', color_discrete_sequence=['#2E8B57'])
        fig.update_traces(texttemplate='R$ %{text:,.0f}', textposition='outside')
        fig.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        entrevistas_empresa = ENTREVISTAS_FICTICIAS[ENTREVISTAS_FICTICIAS['status'] == 'Realizada'].groupby(
            'nome_empresa').size().reset_index(name='Quantidade')
        fig = px.pie(entrevistas_empresa, values='Quantidade', names='nome_empresa',
                     title='📊 Entrevistas Realizadas por Empresa',
                     color_discrete_sequence=px.colors.qualitative.Set2)
        st.plotly_chart(fig, use_container_width=True)

    # Contratos próximos do vencimento
    st.subheader("⚠️ Contratos Próximos do Vencimento (30 dias)")
    contratos_vencendo = []
    for _, row in CONTRATOS_FICTICIOS.iterrows():
        if row['status'] == 'Ativo':
            dias = calcular_tempo_restante(row['data_fim'])
            if 'dias restantes' in dias:
                dias_num = int(dias.split()[0])
                if 0 <= dias_num <= 30:
                    contratos_vencendo.append({
                        'Empresa': row['nome_empresa'],
                        'Vencimento': row['data_fim'],
                        'Status': dias
                    })

    if contratos_vencendo:
        st.dataframe(pd.DataFrame(contratos_vencendo), use_container_width=True)
    else:
        st.success("✅ Nenhum contrato próximo do vencimento!")


def pagina_empresas():
    st.title("🏭 Gestão de Empresas")
    st.markdown("---")

    # Resumo
    st.subheader("📊 Resumo das Empresas")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total", len(EMPRESAS_FICTICIAS))
    with col2:
        st.metric("Ativas", len(EMPRESAS_FICTICIAS[EMPRESAS_FICTICIAS['status'] == 'Ativo']))
    with col3:
        st.metric("Prospect", len(EMPRESAS_FICTICIAS[EMPRESAS_FICTICIAS['status'] == 'Prospect']))

    st.markdown("---")

    # Lista de empresas
    st.subheader("📋 Empresas Cadastradas")

    for _, row in EMPRESAS_FICTICIAS.iterrows():
        with st.container():
            col1, col2, col3, col4 = st.columns([2, 2, 1, 1])
            with col1:
                st.markdown(f"**{row['nome']}**")
                st.caption(f"CNPJ: {row['cnpj']}")
            with col2:
                st.caption(f"📧 {row['email']}")
                st.caption(f"📞 {row['telefone']}")
            with col3:
                status_cor = {"Ativo": "🟢", "Inativo": "🔴", "Prospect": "🟡"}.get(row['status'], "⚪")
                st.markdown(f"{status_cor} **{row['status']}**")
            with col4:
                st.caption(f"📅 {row['data_cadastro']}")
            st.markdown("---")


def pagina_contratos():
    st.title("📄 Gestão de Contratos")
    st.markdown("---")

    for _, row in CONTRATOS_FICTICIOS.iterrows():
        with st.container():
            col1, col2, col3, col4 = st.columns([2, 2, 1, 1])
            with col1:
                st.markdown(f"**{row['nome_empresa']}**")
                st.caption(f"{row['tipo_servico']}")
            with col2:
                st.caption(f"📊 {row['entrevistas_realizadas']}/{row['limite_entrevistas']} entrevistas")
                progresso = row['entrevistas_realizadas'] / row['limite_entrevistas'] if row[
                                                                                             'limite_entrevistas'] > 0 else 0
                st.progress(progresso)
            with col3:
                st.markdown(f"💰 {formatar_moeda(row['valor'])}")
                st.caption(f"📅 {row['data_inicio']} → {row['data_fim']}")
            with col4:
                status_cor = {"Ativo": "🟢", "Encerrado": "🔴", "Suspenso": "🟡"}.get(row['status'], "⚪")
                st.markdown(f"{status_cor} **{row['status']}**")
            st.markdown("---")


def pagina_psicologos():
    st.title("👥 Equipe de Psicólogos")
    st.markdown("---")

    st.subheader("📊 Equipe por Especialidade")
    especialidades = PSICOLOGOS_FICTICIOS['especialidade'].value_counts().reset_index()
    especialidades.columns = ['Especialidade', 'Quantidade']

    fig = px.bar(especialidades, x='Especialidade', y='Quantidade',
                 title='Distribuição por Especialidade',
                 color='Quantidade', color_continuous_scale='Teal')
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    for _, row in PSICOLOGOS_FICTICIOS.iterrows():
        with st.container():
            col1, col2, col3 = st.columns([2, 2, 1])
            with col1:
                st.markdown(f"**{row['nome']}**")
                st.caption(f"{row['especialidade']}")
            with col2:
                st.caption(f"📧 {row['email']}")
                st.caption(f"📞 {row['telefone']}")
            with col3:
                status_cor = "🟢" if row['status'] == 'Ativo' else "🔴"
                st.markdown(f"{status_cor} {row['status']}")
            st.markdown("---")


def pagina_entrevistas():
    st.title("📝 Gestão de Entrevistas")
    st.markdown("---")

    # Filtros
    col1, col2 = st.columns(2)
    with col1:
        empresas = ["Todas"] + sorted(ENTREVISTAS_FICTICIAS['nome_empresa'].unique().tolist())
        filtro_empresa = st.selectbox("🏢 Filtrar por Empresa", empresas)
    with col2:
        status_opcoes = ["Todos"] + sorted(ENTREVISTAS_FICTICIAS['status'].unique().tolist())
        filtro_status = st.selectbox("📌 Filtrar por Status", status_opcoes)

    # Aplicar filtros
    df_filtrado = ENTREVISTAS_FICTICIAS.copy()
    if filtro_empresa != "Todas":
        df_filtrado = df_filtrado[df_filtrado['nome_empresa'] == filtro_empresa]
    if filtro_status != "Todos":
        df_filtrado = df_filtrado[df_filtrado['status'] == filtro_status]

    st.markdown("---")

    # KPIs de entrevistas
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total de Entrevistas", len(df_filtrado))
    with col2:
        st.metric("Realizadas", len(df_filtrado[df_filtrado['status'] == 'Realizada']))
    with col3:
        st.metric("Agendadas", len(df_filtrado[df_filtrado['status'] == 'Agendada']))

    st.markdown("---")

    # Lista de entrevistas
    st.subheader("📋 Entrevistas")
    st.dataframe(df_filtrado[['data_entrevista', 'nome_empresa', 'psicologo', 'setor', 'cargo', 'status']].sort_values(
        'data_entrevista', ascending=False), use_container_width=True)


def pagina_calendario():
    st.title("📅 Agenda de Atividades")
    st.markdown("---")

    pendentes = ATIVIDADES_FICTICIAS[ATIVIDADES_FICTICIAS['status'] == 'pendente']
    concluidas = ATIVIDADES_FICTICIAS[ATIVIDADES_FICTICIAS['status'] == 'concluido']

    col1, col2 = st.columns(2)
    with col1:
        st.metric("🟡 Atividades Pendentes", len(pendentes))
    with col2:
        st.metric("✅ Atividades Concluídas", len(concluidas))

    st.markdown("---")

    st.subheader("🟡 Próximas Atividades")
    if not pendentes.empty:
        for _, row in pendentes.iterrows():
            with st.container():
                col1, col2, col3 = st.columns([2, 2, 1])
                with col1:
                    st.markdown(f"**{row['titulo']}**")
                    st.caption(row['descricao'])
                with col2:
                    st.caption(f"📅 {row['data']} às {row['hora']}")
                    st.caption(f"🏢 {row['empresa_nome']}")
                with col3:
                    st.caption(f"🔖 {row['tipo']}")
                st.markdown("---")
    else:
        st.info("Nenhuma atividade pendente")

    st.subheader("✅ Atividades Concluídas")
    if not concluidas.empty:
        for _, row in concluidas.iterrows():
            st.markdown(f"~~**{row['titulo']}**~~ - {row['empresa_nome']} - {row['data']}")
    else:
        st.info("Nenhuma atividade concluída")


def pagina_relatorios():
    st.title("📊 Relatórios Gerenciais")
    st.markdown("---")

    # Resumo executivo
    st.subheader("📋 Resumo Executivo")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Empresas", len(EMPRESAS_FICTICIAS))
    with col2:
        st.metric("Contratos Ativos", len(CONTRATOS_FICTICIOS[CONTRATOS_FICTICIOS['status'] == 'Ativo']))
    with col3:
        st.metric("Psicólogos", len(PSICOLOGOS_FICTICIOS))
    with col4:
        st.metric("Entrevistas", len(ENTREVISTAS_FICTICIAS))

    st.markdown("---")

    # Gráfico de faturamento
    st.subheader("💰 Faturamento por Empresa")
    faturamento = CONTRATOS_FICTICIOS.groupby('nome_empresa')['valor'].sum().reset_index()
    fig = px.bar(faturamento, x='nome_empresa', y='valor',
                 title='Faturamento por Cliente',
                 labels={'valor': 'Valor (R$)', 'nome_empresa': ''},
                 text='valor', color='valor', color_continuous_scale='Teal')
    fig.update_traces(texttemplate='R$ %{text:,.0f}', textposition='outside')
    fig.update_layout(height=500, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

    # Progresso de entrevistas
    st.subheader("📊 Progresso de Entrevistas por Contrato")
    progresso = CONTRATOS_FICTICIOS[CONTRATOS_FICTICIOS['status'] == 'Ativo'].copy()
    progresso['percentual'] = (progresso['entrevistas_realizadas'] / progresso['limite_entrevistas'] * 100).round(1)

    fig = px.bar(progresso, x='nome_empresa', y='percentual',
                 title='Percentual de Entrevistas Realizadas',
                 labels={'percentual': '% Realizado', 'nome_empresa': ''},
                 text='percentual', color='percentual', color_continuous_scale='Teal')
    fig.update_traces(texttemplate='%{text}%', textposition='outside')
    fig.update_layout(height=500, yaxis_range=[0, 100])
    st.plotly_chart(fig, use_container_width=True)

    # Tabela de indicadores
    st.subheader("📊 Indicadores por Empresa")

    indicadores = []
    for _, empresa in EMPRESAS_FICTICIAS.iterrows():
        contratos_empresa = CONTRATOS_FICTICIOS[CONTRATOS_FICTICIOS['nome_empresa'] == empresa['nome']]
        entrevistas_empresa = ENTREVISTAS_FICTICIAS[ENTREVISTAS_FICTICIAS['nome_empresa'] == empresa['nome']]

        indicadores.append({
            'Empresa': empresa['nome'],
            'Status': empresa['status'],
            'Contratos': len(contratos_empresa),
            'Entrevistas': len(entrevistas_empresa),
            'Faturamento': formatar_moeda(contratos_empresa['valor'].sum() if not contratos_empresa.empty else 0)
        })

    st.dataframe(pd.DataFrame(indicadores), use_container_width=True)


# ============================================
# MENU PRINCIPAL
# ============================================

def main():
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/000000/mental-health.png", width=80)
        st.title("Priorize")
        st.markdown("---")

        menu = st.radio(
            "📌 Navegação",
            ["🏠 Início", "🏭 Empresas", "📄 Contratos", "👥 Psicólogos", "📝 Entrevistas", "📅 Calendário", "📊 Relatórios"],
            index=0
        )

        st.markdown("---")
        st.caption("📢 **Versão Demonstrativa**")
        st.caption("📅 Dados fictícios para apresentação")
        st.caption("🔒 Conformidade NR-01")

    if menu == "🏠 Início":
        pagina_inicio()
    elif menu == "🏭 Empresas":
        pagina_empresas()
    elif menu == "📄 Contratos":
        pagina_contratos()
    elif menu == "👥 Psicólogos":
        pagina_psicologos()
    elif menu == "📝 Entrevistas":
        pagina_entrevistas()
    elif menu == "📅 Calendário":
        pagina_calendario()
    elif menu == "📊 Relatórios":
        pagina_relatorios()


if __name__ == "__main__":
    main()
