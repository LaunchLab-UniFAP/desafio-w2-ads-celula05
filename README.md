## 🚀 LaunchLab UniFAP — Guia de Execução do Desafio Semanal
Este é um repositório corporativo e pedagógico de alto desempenho. A sua célula deve seguir rigorosamente as diretrizes contidas neste documento para validar as competências e conquistar a certificação da semana.


## 🛠️ 1. Instruções Iniciais de Configuração (Proibido dar FORK)
O ecossistema do LaunchLab simula o ambiente de engenharia de software do mercado real. Por questões de governança de TI e compliance corporativo, o fluxo de clonagem do projeto deve seguir regras estritas:

1. NÃO DEIXE UM FORK: É terminantemente proibido utilizar o botão Fork do GitHub neste repositório. O fork vincula seu código publicamente ao perfil do professor, quebrando o isolamento das equipes.
2. USE O TEMPLATE: O integrante líder da célula deve clicar exclusivamente no botão verde "Use this template" ➔ "Create a new repository".
3. ALTERE O OWNER: Na tela de criação do novo repositório, mude obrigatoriamente o campo Owner (Dono) do seu perfil pessoal para a organização oficial do programa: LaunchLab-UniFAP.
4. NOMENCLATURA PADRÃO: Nomeie o repositório utilizando estritamente a tag da sua bancada: desafio-w[NUMERO_DA_SEMANA]-[CURSO]-celula[NUMERO_DA_BANCADA]. (Exemplo: desafio-w2-ads-celula04).
5. CONVITE AO PARCEIRO E MONITOR: Vá em Settings ➔ Collaborators ➔ Add people e convide o outro membro da sua dupla e o usuário do GitHub do seu Embaixador.


## 👥 2. Matriz de Papéis e Responsabilidades na Célula
As células operam como equipes autônomas focadas na identidade e no orgulho de cada curso. Ninguém trabalha isolado.
## 🚀 O Papel do Desenvolvedor de ADS

* Missão: Construir o motor operacional, a mecânica lógica e a estabilidade das funções do software.
* Responsabilidade: Implementar algoritmos limpos, garantir o tratamento completo de exceções em tempo de execução e assegurar o sucesso nos testes de integração automatizados do sistema.

## 💼 O Papel do Desenvolvedor de SI

* Missão: Desenvolver a arquitetura estrutural de dados, governança de TI e regras estratégicas de negócio do projeto.
* Responsabilidade: Estruturar os metadados corporativos, implementar funções de validação de viabilidade econômica/processos e redigir as seções de conformidade, compliance legal e impacto do sistema.

## 🛡️ O Papel do Aluno Embaixador

* Missão: Atuar como Líder Técnico e monitor preventivo de ritmo ao longo da semana.
* Responsabilidade: Auditar os gráficos de commits, remover impedimentos de versionamento de código e responder às Issues abertas pelas células utilizando exclusivamente o método socrático.


## ⚠️ 3. Política de Compliance e Uso de Inteligência Artificial (IA)
O uso de ferramentas de IA (como ChatGPT, GitHub Copilot ou Claude) no LaunchLab UniFAP é regulado por normas estritas de ética profissional:

* 🟢 O que é PERMITIDO (Uso como Assistente): Utilizar a IA para explicar mensagens de erro retornadas pelo console do terminal, sugerir conceitos de sintaxe estruturada ou auxiliar na formatação de arquivos markdown.
* 🔴 O que é PROIBIDO (Sujeito a Retenção de Medalha - ND): Gerar o código-fonte por completo via prompts, copiar e colar funções inteiras sem compreender a mecânica, ou utilizar robôs para redigir as análises textuais do relatório.
* A Auditoria Docente: O professor pode realizar inspeções e arguições orais surpresa. Se um aluno for questionado em sala e não souber explicar a arquitetura ou o funcionamento do código assinado por ele, a competência será marcada imediatamente como Não Desenvolvida (ND) para toda a célula, acionando o Contrato de Convivência.


## 📑 4. Relatório de Entrega da Célula (Preenchimento Obrigatório)
Instrução: Edite as seções abaixo preenchendo as evidências críticas da dupla até o prazo limite estipulado no ciclo semanal.
## 📂 Identificação

* Curso: Análise e Desenvolvimento de Sistemas (ADS) e Sistemas de Informação (SI)
* Membro 1 (Nome & GitHub): @PedroLuucas - Pedro Lucas Pereira Silva — ADS
* Membro 2 (Nome & GitHub): @iltan483 - Iltan Brito Teixeira — SI
* Embaixador Vinculado: @The-Saul - Saul Damasceno Gonçalves

## 🌍 Seção de Análise Crítica (Formação Geral)

Com base no cenário proposto da semana, descreva qual o impacto humano, social, ético ou ambiental da tecnologia que sua célula colocou em produção. Como as decisões de código impactam o mundo físico e a vida do cidadão/empresa?
💬 RESPOSTA DA CÉLULA: [Escreva sua análise crítica aqui]

## 💻 Seção de Engenharia e Governança de TI

Justifique a decisão de arquitetura técnica adotada pela célula nesta entrega. Como as regras de negócio de ADS e as estruturas de dados de SI foram construidas para garantir que a solução seja escalável e de fácil manutenção?
💬 RESPOSTA DA CÉLULA:

A prioridade foi deixar o motor fácil de alterar e manter sem comprometer seu funcionamento, principalmente porque parâmetros como o limite da frota e o piso de ociosidade representam regras de negócio que podem mudar com o tempo.

Para mudar o limite de 50 para 70, basta alterar o valor da constante `LIMITE_MAXIMO_M3` no início do arquivo, sem precisar procurar dentro da lógica da função. A diferença em relação ao template é que agora esse valor está como uma constante de módulo, seguindo a convenção de maiúsculas do Python, e também pode ser importado por outros módulos. Porém, percebi que o valor 50 também está definido no `governanca_si.py`, então o ideal seria centralizar essa configuração em um único lugar para evitar que os dois arquivos fiquem com valores diferentes — o que faria o motor considerar 70 m³ enquanto a auditoria ainda calcularia a ociosidade sobre 50 m³.

Separar o `print` do laço deixa a lógica mais organizada, porque primeiro o código percorre os dados e define se o limite foi atingido, e só depois informa o resultado final. Isso evita que a mensagem de status fique misturada com as mensagens de processamento. A ordem não é exigida pelo teste automatizado, mas colocar o `Volume Total` antes do `Status` deixa a saída de acordo com o formato descrito no enunciado e mais previsível para uma automação que precise consumir esses dados.

A trava de 1000 leituras foi mantida como proteção adicional. Hoje ela pode não ser atingida por causa das outras condições de parada, mas se alguém alterar uma delas no futuro, por exemplo trocando o `>=` por `==`, o laço poderia não parar quando o volume ultrapassasse o limite. Nesse caso, a trava garante que o processo tenha um limite máximo de execução. Ela custa apenas uma variável e uma comparação, enquanto evita o risco de um processo ficar executando indefinidamente e consumindo recursos, principalmente em um servidor.

[SI — a preencher: justificativa das estruturas de dados do `governanca_si.py` (dicionário de metadados de compliance) sob a mesma ótica de escalabilidade e manutenção]

## 🛠️ Diário de Bordo da Bancada

* Maior travamento técnico superado pela dupla durante a semana:

Considerando a dificuldade de diagnóstico, o maior travamento foi entender o problema do `EOFError`. O problema do nome do arquivo foi identificado de forma imediata ao comparar o workflow com o conteúdo do `src/`, enquanto o `EOFError` exigiu ler o tratamento de exceções e perceber que o `except` capturava apenas `ValueError`. Depois confirmei a hipótese reproduzindo o cenário com `"20" | python src/coleta_ads.py`, que gerou o traceback.

* Como a intervenção ou a Issue aberta para o Embaixador ajudou a destravar a célula:

Não abrimos Issue para o Embaixador nesta semana. Foi possível resolver os problemas analisando diretamente o código e o CI, identificando primeiro o problema do nome do arquivo e depois a lacuna no tratamento de exceções, reproduzindo os cenários localmente e validando as correções.

* Declaração de uso de IA:

A IA foi utilizada durante o trabalho, inclusive para geração de código, além de explicação de conceitos e apoio na análise.



## Lembrete de Fechamento: Garanta que todo o projeto esteja commitado na branch principal ('main') e responda ao Micro Simulado individual no AVA antes do prazo limite.

