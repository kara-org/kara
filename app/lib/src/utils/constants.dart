/// ###################################################
/// STRING`S
/// ###################################################

const errorPadrao = 'Favor verificar conexão com a rede';
const errorPadaoCampoSemDado = 'Campo sem dados';
const errorCampoLoginOrSenhaNull = 'Login e/ou senha vazios';
const errorCampoIdentificadorNull = 'Identificador vazio';
const DESCRIPTION_APP_TITLE = 'Kara Doações';
const DESCRIPTION_OK = 'Entendi';
const DESCRIPTION_HOW_WORKS = 'Como funciona';
const DESCRIPTION_ENTER = "Entrar";
const DESCRIPTION_MISSING_FIELD = "Campo obrigatório";
const DESCRIPTION_LOGIN = 'Login';
const DESCRIPTION_LOGIN_HINT = 'Insira seu login';
const DESCRIPTION_EMAIL = 'Email';
const DESCRIPTION_SEARCH = 'Buscar';
const DESCRIPTION_HELP_BY_DONATE = 'Ajude o próximo';
const DESCRIPTION_SEARCH_DEMANDS = 'Encontre demandas e faça sua doação!';
const DESCRIPTION_SEARCH_HINT = 'Digite aqui sua busca';
const DESCRIPTION_EMAIL_HINT = 'Insira seu email';
const DESCRIPTION_INVALID_EMAIL = 'Formato de email inválido';
const DESCRIPTION_PASSWORD = 'Senha';
const DESCRIPTION_PASSWORD_HINT = 'Insira sua senha';
const DESCRIPTION_INVALID_PASSWORD =
    'Senha deve conter pelo menos 4 caracteres';
const DESCRIPTION_INVALID_NUMBER = 'Formato de número inválido';
const DESCRIPTION_BUTTON_FORGOT_PASSWORD = 'Esqueci minha senha';
const DESCRIPTION_APP_BAR_LOGIN = 'Login';
const DESCRIPTION_APP_BAR_HOME = 'Home';
const DESCRIPTION_HIDE_TOOLTIP = 'Ocultar Senha';
const DESCRIPTION_PHONE = 'Telefone';
const DESCRIPTION_PHONE_HINT = 'Insira seu Telefone';
const DESCRIPTION_INVALID_PHONE = 'Formato de telefone inválido';
const DESCRIPTION_NAME = 'Nome';
const DESCRIPTION_NAME_HINT = 'Insira seu nome';
const DESCRIPTION_CPF = 'CPF';
const DESCRIPTION_CPF_HINT = 'Insira seu CPF';
const DESCRIPTION_INVALID_CPF = 'Formato de CPF inválido';
const DESCRIPTION_CNPJ = 'CNPJ';
const DESCRIPTION_CNPJ_HINT = 'Insira o CNPJ da ONG';
const DESCRIPTION_INVALID_CNPJ = 'Formato de CNPJ inválido';
const DESCRIPTION_DESCRIPTION = 'Descrição';
const DESCRIPTION_DESCRIPTION_HINT = 'Insira uma descrição';
const DESCRIPTION_STREET = 'Rua';
const DESCRIPTION_STREET_HINT = 'Insira uma rua';
const DESCRIPTION_CEP = 'CEP';
const DESCRIPTION_CEP_HINT = 'Insira um CEP';
const DESCRIPTION_INVALID_CEP = 'Formato de CEP inválido';
const DESCRIPTION_DISTRICT = 'Bairro';
const DESCRIPTION_DISTRICT_HINT = 'Insira um bairro';
const DESCRIPTION_CITY = 'Cidade';
const DESCRIPTION_CITY_HINT = 'Insira uma cidade';
const DESCRIPTION_STATE = 'Estado';
const DESCRIPTION_STATE_HINT = 'Insira um estado';
const DESCRIPTION_ABOUT_PAGE =
    'Aplicativo que possibilita a interação entre doadores e ONGs';
const DESCRIPTION_CONTACTS = 'Entre em contato';
const DESCRIPTION_LABEL_CONTACT = 'Fale Conosco';
const DESCRIPTION_EMAIL_CONTACT = 'mailto:cxpostalmobile@ufs.br';
const DESCRIPTION_LABEL_SIGAA = 'Visite o Kara Doações WEB';
const DESCRIPTION_RATING = 'Deixe sua avaliação';
const DESCRIPTION_LABEL_GOOGLE_PLAY = 'Avalie o Kara Doações no Google Play';
const DESCRIPTION_ABOUT_OUR_WORK = 'Mais sobre nosso trabalho';
const DESCRIPTION_CURRENT_VERSION_LABEL = 'Versão Atual';
const DESCRIPTION_LOG_TITLE = 'Novidades!';
const DESCRIPTION_CURRENT_VERSION = 'Versão 1.0.0 - Horários';
const DESCRIPTION_CHANGE_LOG = <String>[];
const DESCRIPTION_DIALOG_ERROR = 'Ocorreu um erro';
const DESCRIPTION_SEARCH_ERROR = 'Erro na busca';
const DESCRIPTION_ERROR_DEFAULT = 'Favor verificar sua conexão com a internet';
const DESCRIPTION_TRY_AGAIN = 'Tentar novamente';
const DESCRIPTION_DEMANDS = "Demandas";
const DESCRIPTION_DONATES = "Doações";
const DESCRIPTION_DONATE = "Doar";
const DESCRIPTION_ONGS = "ONGs";
const DESCRIPTION_PROFILE = "Perfil";
const DESCRIPTION_ABOUT_KARA = "Sobre o Kara Doações";
const DESCRIPTION_LEAVE = 'SAIR';
const DESCRIPTION_PROFILE_DONATOR_BUTTON = "Perfil do doador";
const DESCRIPTION_PROFILE_ONG_BUTTON = "Perfil da ONG";
const DESCRIPTION_SEMANTIC_ONG_ADDRESS = "Endereço:";
const DESCRIPTION_SEMANTIC_PHONE = "Telefone:";
const DESCRIPTION_SEMANTIC_DONATES_ITEMS = "Itens de doação:";
const DESCRIPTION_SEMANTIC_ONGS = "ONGs:";
const DESCRIPTION_SEMANTIC_DONATOR = "Doador:";
const DESCRIPTION_SUBJECT = "Disciplinas";
const DESCRIPTION_SEMANTIC_DELIVERED_SUBJECTS = "Entregue:";
const DESCRIPTION_SEMANTIC_CANCELED_SUBJECTS = "Cancelada:";
const DESCRIPTION_LEVEL = "Nível:";
const DESCRIPTION_HOURS = "Horas";
const DESCRIPTION_PROMISE_QUANTITY = "Quantidade prometida:";
const DESCRIPTION_REAL_QUANTITY = "Quantidade efetivada:";
const DESCRIPTION_REQUESTED_QUANTITY = "Quantidade solicitada:";
const DESCRIPTION_CATEGORY_QUANTITY = "Categoria:";
const DESCRIPTION_SITUATION = "Situação:";
const DESCRIPTION_UNTIL = "até as";
const DESCRIPTION_ONG_LOCATION = "Local da ONG:";

const DESCRIPTION_MONDAY = "SEGUNDA";
const DESCRIPTION_TUESDAY = "TERÇA";
const DESCRIPTION_WEDNESDAY = "QUARTA";
const DESCRIPTION_THURSDAY = "QUINTA";
const DESCRIPTION_FRIDAY = "SEXTA";
const DESCRIPTION_SATURDAY = "SÁBADO";
const DESCRIPTION_SUNDAY = "DOMINGO";

const DESCRIPTION_MON = "SEG";
const DESCRIPTION_TUE = "TER";
const DESCRIPTION_WED = "QUA";
const DESCRIPTION_THU = "QUI";
const DESCRIPTION_FRI = "SEX";
const DESCRIPTION_SAT = "SÁB";
const DESCRIPTION_SUN = "DOM";

const DESCRIPTION_DEMANDS_ONG_EMPTY = 'SEM DEMANDAS PARA ONG';
const DESCRIPTION_ONGS_DEMAND_EMPTY = 'SEM ONGS PARA DEMANDA';
const DESCRIPTION_DONATIONS_EMPTY = 'SEM DOAÇÕES';
const DESCRIPTION_DEMANDS_EMPTY = 'SEM DEMANDAS';
const DESCRIPTION_ONGS_EMPTY = 'SEM ONGS';

/// ###################################################
/// Endpoints
/// ###################################################
const ENDPOINT_ONG = "ong";
const ENDPOINT_USER = "usuario";
const ENDPOINT_ITEM = "item";
const ENDPOINT_AUTH = "auth";
const ENDPOINT_DONATOR = "doador";
const ENDPOINT_DONATION = "doacao";
const ENDPOINT_DONATIONS = "doacoes";
const ENDPOINT_DEMAND = "demanda";
const ENDPOINT_DEMANDS = "demandas";
const ENDPOINT_CANCELATION = "cancelar";
const ENDPOINT_CONFIRMATION = "confirmar";

/// ###################################################
/// TEXTS
/// ###################################################
const DESCRIPTION_TUTORIAL_1 =
    'Primeiro, você precisa buscar uma demanda na nossa barra de busca, experimente digitar "Arroz" e clicar no botão buscar.';
const DESCRIPTION_TUTORIAL_2 =
    'Inicie uma conversa por telefone ou email para combinar o encontro com a ONG.';
const DESCRIPTION_TUTORIAL_3 =
    'Agora é só entregar sua doação e aproveitar pra conhecer o projeto que você está apoiando!';

/// ###################################################
/// PAGES
/// ###################################################
const DESCRIPTION_PAGE_ABOUT = 'AboutPage';
const DESCRIPTION_PAGE_SPLASH = 'SplashPage';
const DESCRIPTION_PAGE_LOGIN = 'LoginPage';
const DESCRIPTION_PAGE_REGISTER = 'RegisterPage';
const DESCRIPTION_NAV_BAR = 'NavBar';
const DESCRIPTION_PAGE_HOME = 'HomePage';
const DESCRIPTION_PAGE_PROFILE = 'ProfilePage';
const DESCRIPTION_PAGE_DEMANDS = 'DemandsPage';

/// ###################################################
/// ASSETS
/// ###################################################

const DESCRIPTION_VIDEO_BG = 'assets/gifs/video_bg1.gif';
const DESCRIPTION_KARA_LOGO = 'assets/images/kara_logo.svg';
const DESCRIPTION_KARA_LOGO_PNG = 'assets/images/kara_logo.png';
const DESCRIPTION_LADY_PC = 'assets/images/lady_pc.svg';
const DESCRIPTION_HAPPY_LADY = 'assets/images/happy_lady.svg';
const DESCRIPTION_MAN = 'assets/images/man.svg';

/// ###################################################
/// LINKS
/// ###################################################
const DESCRIPTION_KARA_URL = 'https://karadoacoes.tk/';
const URL_API = "http://10.0.2.2:8000/api";
