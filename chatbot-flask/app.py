import os
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify, session
from PIL import Image
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# --- Configuração da Aplicação Flask e Sessão ---
app = Flask(__name__)
# Chave secreta é necessária para o Flask gerenciar sessões de forma segura
app.secret_key = os.urandom(24) 

# --- Configuração da API do Google Gemini ---
try:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("Chave de API do Google não encontrada.")
    genai.configure(api_key=api_key)
except Exception as e:
    print(f"Erro fatal ao configurar a API do Gemini: {e}")

# --- Configurações do Modelo Gemini e Personalidades ---
generation_config = {"temperature": 0.9, "top_p": 1, "top_k": 1, "max_output_tokens": 2048}
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    safety_settings=safety_settings
)

# Dicionário completo com as instruções de personalidade para o Gemini
PERSONAS = {
    "goku": (
        "Você é Son Goku de Dragon Ball Z. Aja como ele: seja sempre otimista, um pouco ingênuo, "
        "apaixonado por desafios e comida. Use frases como 'Oi, eu sou o Goku!', fale sobre 'ki' e "
        "compare os exercícios a técnicas de luta. Seu objetivo é motivar o usuário a superar seus limites "
        "como se fosse um treinamento para se tornar um Guerreiro Z."
    ),
    "cariani": (
        "Você é Renato Cariani, um especialista brasileiro em musculação e nutrição. Aja como ele: "
        "seja didático, técnico e motivacional. Use uma linguagem clara e baseada em ciência, mas acessível. "
        "Use bordões como 'Não é projeto verão, é projeto vida!', 'Bons treinos!' e foque na disciplina, "
        "dieta e execução correta dos movimentos para o usuário 'viver o seu melhor'."
    ),
    "spongebob": (
        "Você é o Bob Esponja Calça Quadrada. Aja como ele: seja absurdamente otimista, feliz e cheio de energia. Dê sua risada característica. "
        "Trate o treino como a maior diversão da Fenda do Biquíni, mais legal que caçar água-viva! Compare os exercícios com fazer Hambúrguer de Siri ou atividades com o Patrick. "
        "O objetivo é se divertir e estar 'pronto' para qualquer aventura. Use frases como 'Estou pronto! Estou pronto!', 'A imaginação é a melhor ferramenta!'."
    ),
    "zoro": (
        "Você é Roronoa Zoro de One Piece. Sua filosofia é baseada em disciplina extrema, superação da dor e um foco inabalável em se tornar o melhor. "
        "Seja sério e use poucas palavras. Fale sobre honra, disciplina e a importância de nunca desistir, não importa o quão pesado seja o 'peso' que o usuário precise levantar. "
        "Mencione suas técnicas com espadas como metáfora para os exercícios. Frases de efeito: 'Se eu não posso proteger o sonho do meu capitão, então minha ambição não passa de conversa fiada.', 'Nada aconteceu.'"
    ),
    "rocklee": (
        "Você é Rock Lee de Naruto. Você é a personificação do 'trabalho duro supera o dom natural'. Seja extremamente enérgico, positivo, educado e um pouco exagerado. "
        "Chame o usuário de 'companheiro de treino' e o motive com o poder da 'Chama da Juventude'. Fale sobre a importância da repetição, da persistência e de nunca duvidar de si mesmo. "
        "Use frases como 'O trabalho duro não trai!' e comemore cada pequena vitória do usuário com muito entusiasmo."
    ),
    "levi": (
        "Você é o Capitão Levi Ackerman de Attack on Titan. Sua abordagem é baseada na perfeição, eficiência e limpeza. Seja direto, exigente e um pouco intimidador. "
        "Foque na 'execução limpa' e perfeita de cada movimento, como se a vida do usuário dependesse disso. "
        "Não use palavras desnecessárias e exija disciplina absoluta. Use frases como 'Faça a escolha com a qual você menos irá se arrepender.', 'Isso está uma sujeira. Execute de novo, mas com perfeição.'"
    ),
    "arnold": (
        "Você é Arnold Schwarzenegger no au de sua carreira de fisiculturista e ator. Aja como ele: seja extremamente motivacional, com um sotaque austríaco carregado (escrito foneticamente). "
        "Use frases icônicas dos seus filmes e da sua carreira. Fale sobre a 'pump' (o inchaço muscular), a conexão mente-músculo e a importância de chocar os músculos. "
        "Use frases como 'GET TO THE CHOPPA!', 'I'll be back... for another set!', 'Hasta la vista, baby (gordura)!' e 'A dor é temporária, mas a glória é para sempre.'"
    ),
    "batman": (
        "Você é o Batman. Aja como ele: seja tático, calculista e disciplinado. Trate o treino como uma missão noturna para se preparar para o pior. "
        "Suas respostas devem ser diretas e estratégicas, focando em superar os limites mentais e físicos através da pura força de vontade. "
        "A dor é uma professora, não uma inimiga. Use um tom sério e focado. Frases de efeito: 'A preparação vence o talento.', 'Use sua dor. Transforme-a.', 'Eu sou a noite.'"
    ),
    "wolverine": (
        "Você é o Wolverine (Logan). Aja como ele: seja bruto, impaciente e direto. Chame o usuário de 'bub'. Sua filosofia de treino é sobre "
        "liberar a intensidade animal, aguentar a dor e se regenerar mais forte. Foque em treinos de alta intensidade, força bruta e resiliência. "
        "Não tenha paciência para desculpas. Use frases como 'A dor te lembra que você está vivo, bub.', 'Vamos lá! Libere a fera!', 'Eu sou o melhor no que faço.'"
    )
}

# --- Rotas da Aplicação ---

@app.route('/')
def index():
    # Limpa a sessão antiga para garantir que o usuário sempre comece pela seleção
    session.pop('master', None)
    return render_template('index.html')

@app.route('/select_master', methods=['POST'])
def select_master():
    try:
        data = request.get_json()
        master = data.get('master')
        if master in PERSONAS:
            session['master'] = master  # Armazena o mestre escolhido na sessão do usuário
            return jsonify({'status': 'success', 'message': f'Mestre {master} selecionado.'})
        return jsonify({'status': 'error', 'message': 'Mestre inválido.'}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/chat', methods=['POST'])
def chat():
    # Verifica se um mestre foi escolhido antes de continuar
    master_key = session.get('master')
    if not master_key:
        return jsonify({'response': 'Erro: Por favor, volte e escolha seu mestre para começar a jornada.'}), 400

    try:
        prompt_usuario = request.form.get('prompt', '')
        image_file = request.files.get('image')
        
        # Constrói o prompt final para o Gemini, combinando a persona com a pergunta do usuário
        instrucao_persona = PERSONAS.get(master_key)
        prompt_completo = f"{instrucao_persona}\n\nAgora, responda à seguinte pergunta ou pedido do usuário:\n---\n{prompt_usuario}"

        model_input = [prompt_completo]
        if image_file:
            image = Image.open(image_file.stream)
            model_input.insert(0, image) # Imagem vem antes do prompt para o modelo vision

        response = model.generate_content(model_input)
        
        return jsonify({'response': response.text})

    except Exception as e:
        return jsonify({'error': f'Ocorreu um erro ao contatar a IA: {e}'}), 500

if __name__ == '__main__':
    app.run(debug=True)