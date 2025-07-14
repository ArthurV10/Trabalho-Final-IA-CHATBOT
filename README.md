# GYM MASTERS - Personal Trainer AI

<p align="center">
  <img src="https://pa1.aminoapps.com/6481/aa4533bd25e33cdd5ac323ca0bddc4619afffb12_hq.gif" alt="Goku Training" width="300"/>
</p>

<p align="center">
  <strong>Um chatbot de treino inovador que traz as personalidades mais icônicas para te motivar na academia!</strong>
</p>

---

## 🚀 Demonstração ao Vivo

O projeto está implantado e pode ser acessado no seguinte endereço:

➡️ **[Acessar GYM MASTERS](https://trabalho-final-ia-chatbot.onrender.com)**

**Observação:** O projeto está hospedado no plano gratuito do Render. Por isso, ao acessar o link pela primeira vez, pode levar alguns instantes (cerca de 1 a 2 minutos) para o aplicativo "acordar" e ficar disponível. Tenha um pouco de paciência! Além disso, caso ocorra algum problema no site, pode ter ocorrido de ter chegado as 50 requisições diárias, então aguarde até algum outro momento que esteja disponível

---

## 🌟 Sobre o Projeto

**GYM MASTERS** é uma aplicação web construída com Flask que utiliza a poderosa API **Google Gemini** para criar uma experiência de coaching de fitness única. O usuário pode escolher um "mestre" dentre várias personalidades famosas do universo da ficção e do esporte. Cada mestre possui um estilo de comunicação e motivação próprio, transformando o seu treino em uma jornada épica e divertida.

### Principais Funcionalidades

* **Seleção de Mestres**: Escolha entre 9 personalidades icônicas para ser seu guia de treino.
* **Chat Interativo**: Converse com seu mestre, faça perguntas sobre exercícios, peça dicas de motivação ou rotinas de treino.
* **Análise de Imagem**: Envie uma foto (de um exercício, por exemplo) para que seu mestre a analise e dê um feedback no seu estilo característico.
* **Interface Dinâmica**: Uma interface web estilizada e responsiva que separa a seleção do mestre da tela de chat.

---

## 💪 Os Mestres

Escolha a lenda que irá te guiar rumo ao seu melhor shape!

| Mestre | Filosofia | Especialidades |
| :--- | :--- | :--- |
| **Goku** | Superação e otimismo de um Guerreiro Z. | `Motivação`, `Superação`, `Energia` |
| **Renato Cariani** | Ciência, disciplina e foco em resultados. | `Ciência`, `Disciplina`, `Técnica` |
| **Bob Esponja** | A diversão e a energia da Fenda do Biquíni. | `Diversão`, `Energia`, `Cardio` |
| **Roronoa Zoro** | Disciplina absoluta e superação da dor. | `Disciplina`, `Resistência`, `Força` |
| **Rock Lee** | O poder do trabalho duro e da "Chama da Juventude". | `Energia`, `Dedicação`, `Cardio` |
| **Levi Ackerman** | Perfeição, eficiência e execução limpa. | `Perfeição`, `Técnica`, `Agilidade` |
| **Arnold** | Motivação icônica, pump e treinos lendários. | `Pump`, `Massa`, `Lenda` |
| **Batman** | Disciplina tática e superação da dor. | `Tática`, `Disciplina`, `Vontade` |
| **Wolverine** | Intensidade animal, força bruta e regeneração. | `Intensidade`, `Força`, `Regeneração` |

---

## 🛠️ Tecnologias Utilizadas

* **Backend**: Flask
* **Inteligência Artificial**: Google Gemini (gemini-1.5-flash)
* **Frontend**: HTML, CSS, JavaScript
* **Bibliotecas Python**:
    * `google-generativeai`
    * `Pillow` (para processamento de imagem)
    * `python-dotenv` (para gerenciamento de variáveis de ambiente)
* **Deployment**: Gunicorn, Render

---

## ⚙️ Como Rodar o Projeto Localmente

Para executar o projeto em sua máquina local, siga os passos abaixo.

1.  **Clone o repositório:**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd trabalho-final-ia-chatbot/chatbot-flask
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Crie o ambiente virtual
    python -m venv venv

    # Ative o ambiente no Windows
    .\venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    Com o ambiente virtual ativado, instale todas as bibliotecas necessárias.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as variáveis de ambiente:**
    Para que a aplicação se conecte à API do Google Gemini, é necessário configurar sua chave de API.

    * Crie um arquivo chamado `.env` na raiz do diretório `chatbot-flask`.
    * Dentro do arquivo `.env`, adicione a seguinte linha, substituindo `SUA_CHAVE_API_AQUI` pela sua chave de API real do Google:
        ```
        GOOGLE_API_KEY=SUA_CHAVE_API_AQUI
        ```
    O arquivo `.gitignore` já está configurado para ignorar o arquivo `.env`.

5.  **Execute a aplicação:**
    Após instalar as dependências e configurar a chave de API, você pode iniciar o servidor Flask:
    ```bash
    flask run
    ```
    Ou, alternativamente:
    ```bash
    python app.py
    ```

6.  **Acesse no navegador:**
    Abra seu navegador e acesse `http://127.0.0.1:5000` para interagir com o chatbot.
