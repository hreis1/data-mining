# Trabalho de Mineração de Dados e Aplicações na Engenharia

Este projeto explora a aplicação de técnicas de Análise de Componentes Principais (PCA) e Análise de Componentes Independentes (ICA) para reduzir artefatos em sinais de Eletrocardiograma (ECG) obtidos por dispositivos vestíveis. O estudo utiliza dados do conjunto **ScientISST MOVE** para avaliar a eficácia dessas técnicas em ambientes dinâmicos.

![ECG Processado com PCA e ICA](Documentos/Figure_1.png)  
*Figura 1: Comparação do sinal original de ECG com os resultados de PCA e ICA.*

---

## Sumário
1. [Visão Geral do Projeto](#visão-geral-do-projeto)
2. [Fundamentação Teórica](#fundamentação-teórica)
3. [Metodologia](#metodologia)
4. [Resultados](#resultados)
5. [Discussão e Conclusão](#discussão-e-conclusão)
6. [Como Reproduzir o Estudo](#como-reproduzir-o-estudo)
7. [Reconhecimentos e Direitos Autorais](#reconhecimentos-e-direitos-autorais)
8. [Copyright/License](#copyright/license)
---

## Visão Geral do Projeto
**Objetivo**:  
Reduzir artefatos de movimento em sinais de ECG coletados por dispositivos vestíveis, aprimorando a precisão para diagnóstico clínico.

**Problema**:  
Dispositivos ambulatoriais enfrentam interferências (e.g., movimentos corporais), que distorcem os sinais de ECG.  

**Técnicas Utilizadas**:  
- **PCA**: Simplifica os dados identificando componentes de maior variância.
- **ICA**: Separa fontes estatisticamente independentes no sinal.

**Base de Dados**:  
[ScientISST MOVE](https://physionet.org/content/scientisst-move-biosignals/1.0.0/) (PhysioNet), contendo registros de ECG, EMG, PPG e acelerômetros durante atividades cotidianas.

---

## Fundamentação Teórica
### PCA (Análise de Componentes Principais)
- **Função**: Reduz dimensionalidade preservando a variância máxima.
- **Aplicação no ECG**: Identifica padrões dominantes (e.g., batimentos cardíacos) e atenua ruídos de baixa variância.

### ICA (Análise de Componentes Independentes)
- **Função**: Isola fontes independentes misturadas no sinal.
- **Aplicação no ECG**: Separa o sinal cardíaco de interferências (e.g., movimento muscular).

---

## Metodologia
### Fluxo do Projeto
1. **Coleta de Dados**:  
   - Dados do ScientISST MOVE (10.5 horas de registros de 17 voluntários).
   - Atividades: caminhar, correr, gestos, etc.

2. **Pré-processamento**:  
   - Normalização do sinal.
   - Filtragem para remoção de ruído de alta frequência.

3. **Aplicação de PCA e ICA**:  
   - **PCA**: Seleção de componentes principais que explicam 95% da variância.
   - **ICA**: Uso do algoritmo FastICA para extrair componentes independentes.

---

## Resultados
### Comparação Visual dos Sinais
- **PCA**: Preserva a estrutura geral do ECG, mas suaviza detalhes.
- **ICA**: Isola efetivamente o sinal cardíaco de artefatos (e.g., movimento).

![Sinal Original vs. Processado](Documentos/Figure_1.png)

---

## Discussão e Conclusão
**Principais Conclusões**:  
- **PCA**: Ideal para simplificação rápida, mas perde detalhes sutis.
- **ICA**: Superior na separação de fontes, porém computacionalmente intensivo.

**Trabalho Futuro**:  
- Combinação de PCA/ICA com redes neurais para classificação de anomalias.

---

## Como Reproduzir o Estudo
### Requisitos
- Python 3.13
- Bibliotecas: `mne`, `numpy`, `scikit-learn`, `matplotlib`

### Passos
1. **Clonar o Repositório**:  
   ```bash
   git clone https://github.com/hreis1/data-mining.git
   cd data-mining
   ```

2. **Executar o Código**:  
   ```bash
   python3.13 Codigos/main.py
   ```
---

## Reconhecimentos e Direitos Autorais

- **@autor**: Paulo Henrique Reis | Renata Costa Rocha
- **@contato**: hreispaulo1@gmail.com | renata.rocha@discente.ufma.br
- **@data última versão**: 30/01/2025
- **@versão**: 0.1
- **outros repositórios**: [ScientISST-MOVE](https://github.com/scientisst/ScientISST-MOVE)
- **Agradecimentos**: Universidade Federal do Maranhão (UFMA), Professor Doutor Thales Levi Azevedo Valente, e colegas de curso.
---

## Copyright/License

Este material é resultado de um trabalho acadêmico para a disciplina **Mineração de Dados e Aplicações na Engenharia,** sob a orientação do professor **Dr. Thales Levi Azevedo Valente,** semestre letivo **2024.2,** curso **Engenharia da Computação,** na **Universidade Federal do Maranhão (UFMA)**.

Este material é resultado de um trabalho acadêmico para a disciplina MINERAÇÃO DE DADOS E APLICAÇÕES NA ENGENHARIA, sob a orientação do professor Dr. THALES LEVI AZEVEDO VALENTE, semestre letivo 2024.2, curso Engenharia da Computação, na Universidade Federal do Maranhão (UFMA). Todo o material sob esta licença é software livre: pode ser usado para fins acadêmicos e comerciais sem nenhum custo. Não há papelada, nem royalties, nem restrições de "copyleft" do tipo GNU. Ele é licenciado sob os termos da Licença MIT, conforme descrito abaixo, e, portanto, é compatível com a GPL e também se qualifica como software de código aberto. É de domínio público. Os detalhes legais estão abaixo. O espírito desta licença é que você é livre para usar este material para qualquer finalidade, sem nenhum custo. O único requisito é que, se você usá-los, nos dê crédito.

Licenciado sob a Licença MIT. Permissão é concedida, gratuitamente, a qualquer pessoa que obtenha uma cópia deste software e dos arquivos de documentação associados (o "Software"), para lidar no Software sem restrição, incluindo sem limitação os direitos de usar, copiar, modificar, mesclar, publicar, distribuir, sublicenciar e/ou vender cópias do Software, e permitir pessoas a quem o Software é fornecido a fazê-lo, sujeito às seguintes condições:

Este aviso de direitos autorais e este aviso de permissão devem ser incluídos em todas as cópias ou partes substanciais do Software.

O SOFTWARE É FORNECIDO "COMO ESTÁ", SEM GARANTIA DE QUALQUER TIPO, EXPRESSA OU IMPLÍCITA, INCLUINDO MAS NÃO SE LIMITANDO ÀS GARANTIAS DE COMERCIALIZAÇÃO, ADEQUAÇÃO A UM DETERMINADO FIM E NÃO INFRINGÊNCIA. EM NENHUM CASO OS AUTORES OU DETENTORES DE DIREITOS AUTORAIS SERÃO RESPONSÁVEIS POR QUALQUER RECLAMAÇÃO, DANOS OU OUTRA RESPONSABILIDADE, SEJA EM AÇÃO DE CONTRATO, TORT OU OUTRA FORMA, DECORRENTE DE, FORA DE OU EM CONEXÃO COM O SOFTWARE OU O USO OU OUTRAS NEGOCIAÇÕES NO SOFTWARE.

Para mais informações sobre a Licença MIT: https://opensource.org/licenses/MIT
