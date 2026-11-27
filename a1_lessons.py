"""Authored A1 lesson content for Learn Language Academy by Parth.

Every lesson uses the same nine-part teaching structure. Pronunciation spellings are
approximations for English speakers; IPA is supplied where practical.
"""

LESSON_DATA = {
2: {
"title":"Greetings and Basic Introductions",
"goal":"Greet people naturally, choose formal or informal language, and manage a short first conversation.",
"vocab":[
("bonjour","hello; good morning","bohn-zhoor","/bɔ̃.ʒuʁ/","Bonjour, madame !"),
("bonsoir","good evening","bohn-swahr","/bɔ̃.swaʁ/","Bonsoir, tout le monde !"),
("salut","hi; bye (informal)","sah-lü","/sa.ly/","Salut, Paul !"),
("allô","hello (on the phone)","ah-loh","/a.lo/","Allô ? Qui est à l'appareil ?"),
("au revoir","goodbye","oh ruh-vwahr","/o ʁə.vwaʁ/","Au revoir et bonne journée."),
("à bientôt","see you soon","ah byan-toh","/a bjɛ̃.to/","À bientôt, Sophie !"),
("à demain","see you tomorrow","ah duh-man","/a də.mɛ̃/","À demain matin."),
("s'il vous plaît","please (formal/plural)","seel voo pleh","/sil vu plɛ/","Un café, s'il vous plaît."),
("s'il te plaît","please (informal)","seel tuh pleh","/sil tə plɛ/","Aide-moi, s'il te plaît."),
("merci","thank you","mehr-see","/mɛʁ.si/","Merci pour votre aide."),
("de rien","you're welcome","duh ree-ehn","/də ʁjɛ̃/","— Merci ! — De rien !"),
("enchanté / enchantée","nice to meet you","ahn-shahn-tay","/ɑ̃.ʃɑ̃.te/","Enchantée, je m'appelle Léa.")
],
"grammar":[
("Formal vous and informal tu","Use vous with strangers, people you do not know well, in professional situations, and when showing respect. Use tu with friends, children, family and people who invite you to use it. When unsure, begin with vous."),
("Bonjour versus bonsoir","Bonjour is the normal daytime greeting. Bonsoir is used in the evening. Salut is friendly and informal; it can mean either hi or bye."),
("Asking how someone is","Comment allez-vous ? is the polite form. Comment vas-tu ? is informal. Ça va ? is common in everyday conversation. A natural answer is Ça va bien, merci."),
("French questions and intonation","A rising voice can make a short statement a question: Vous allez bien ? The phrase est-ce que can introduce a clear question: Est-ce que vous allez bien ?")
],
"expressions":[("Comment allez-vous ?","How are you?","Polite; suitable for a first meeting."),("Comment ça va ?","How's it going?","Common, conversational; neutral to informal."),("Ça va bien, merci.","I'm well, thank you.","A complete polite response."),("Et vous ?","And you?","Returns the question politely."),("Bonne journée !","Have a good day!","Often said when leaving a shop or service interaction."),("Pas de problème.","No problem.","Natural response to thanks or a small request.")],
"examples":[("Bonjour, madame. Comment allez-vous ?","Hello, ma'am. How are you?","Bonjour is polite; vous keeps the exchange respectful."),("Ça va bien, merci. Et vous ?","I'm well, thank you. And you?","The short question returns the greeting."),("Salut, Thomas ! Ça va ?","Hi, Thomas! How's it going?","Salut and ça va are informal."),("Enchantée. Je m'appelle Nadia.","Nice to meet you. My name is Nadia.","Enchantée is written with -e when the speaker is female."),("Au revoir et bonne journée !","Goodbye and have a good day!","A natural way to close a daytime interaction."),("Allô ? C'est Marc.","Hello? It's Marc.","Allô is used when answering the telephone.")],
"conversations":[("Meeting someone politely",[("A","Bonjour, monsieur."),("B","Bonjour, madame. Comment allez-vous ?"),("A","Très bien, merci. Et vous ?"),("B","Très bien, merci. Enchanté." )],"A: Hello, sir. B: Hello, ma'am. How are you? A: Very well, thank you. And you? B: Very well, thank you. Nice to meet you."),("Two friends meeting",[("A","Salut, Amélie ! Ça va ?"),("B","Oui, ça va bien. Et toi ?"),("A","Ça va, merci ! À bientôt !"),("B","À demain !")],"A: Hi, Amélie! How's it going? B: Yes, I'm doing well. And you? A: I'm good, thanks! See you soon! B: See you tomorrow!")],
"speaking":["Say bonjour, bonsoir and salut aloud; keep the final consonants in bonjour and bonsoir clear.","Practise vous and tu in pairs of sentences; change the verb form when you change the pronoun.","Link the words in s'il vous plaît smoothly without inserting pauses between every word.","Role-play meeting a neighbour formally, then greeting a close friend informally.","Read both dialogues aloud twice, changing roles."],
"summary":["Use bonjour during the day and bonsoir in the evening.","Use salut with people you know well; use bonjour in polite situations.","Choose vous for formality and tu for familiarity.","Ask Comment allez-vous ? or Comment ça va ? and return the question with Et vous ? or Et toi ?."]
},
3:{
"title":"Personal Information and Introducing Yourself","goal":"Give and ask for basic personal details, including name, age, origin, residence and languages.",
"vocab":[
("je m'appelle","my name is","zhuh mah-pell","/ʒə ma.pɛl/","Je m'appelle David."),
("comment vous appelez-vous ?","what is your name? (formal)","koh-mahn voo zah-play voo","/kɔ.mɑ̃ vu za.ple vu/","Comment vous appelez-vous ?"),
("j'ai ... ans","I am ... years old","zhay ... ahn","/ʒe ... ɑ̃/","J'ai vingt ans."),
("l'âge (m.)","age","lahzh","/laʒ/","Quel âge as-tu ?"),
("je viens de","I come from","zhuh vyan duh","/ʒə vjɛ̃ də/","Je viens d'Angola."),
("j'habite à","I live in","zhah-beet ah","/ʒa.bit a/","J'habite à Luanda."),
("le pays","country","luh pay-ee","/lə pɛ.i/","Quel est ton pays ?"),
("la ville","city","lah veel","/la vil/","La ville est grande."),
("la langue","language","lah lahng","/la lɑ̃ɡ/","Quelle langue parles-tu ?"),
("je parle","I speak","zhuh parl","/ʒə paʁl/","Je parle anglais."),
("l'étudiant / l'étudiante","student","lay-tü-dyan / lay-tü-dyant","/le.ty.djɑ̃/","Elle est étudiante."),
("le numéro de téléphone","phone number","luh nü-may-roh duh tay-lay-fohn","/lə ny.me.ʁo də te.le.fɔn/","Voici mon numéro de téléphone.")
],
"grammar":[
("Introducing yourself with s'appeler","Je m'appelle means my name is. The verb s'appeler is reflexive: je m'appelle, tu t'appelles, il/elle s'appelle, nous nous appelons, vous vous appelez, ils/elles s'appellent. Learn the phrase as a unit at this stage."),
("Age uses avoir","French says J'ai vingt ans (literally, I have twenty years), not Je suis vingt ans. Use avoir + number + ans. Ask Quel âge as-tu ? informally or Quel âge avez-vous ? formally."),
("Origin with venir de","Use venir de to say where you come from: Je viens du Canada (masculine country), de France (feminine country), des États-Unis (plural), d'Angola (before a vowel)."),
("Residence with habiter","Use habiter à before a city: J'habite à Montréal. Use en with many feminine countries, au with masculine countries, and aux with plural countries. Country names have exceptions, so learn common combinations.")
],
"expressions":[("Je m'appelle…","My name is…","A standard introduction."),("Et vous, comment vous appelez-vous ?","And you, what is your name?","Polite follow-up."),("Je viens de…","I come from…","State your origin."),("J'habite à…","I live in…","Give your city."),("Je parle un peu français.","I speak a little French.","Useful honest language-level statement."),("Ravi(e) de vous rencontrer.","Pleased to meet you.","Polite, slightly more formal than enchanté(e).")],
"examples":[("Je m'appelle Daniel.","My name is Daniel.","Je m'appelle is the fixed first-person form."),("J'ai vingt-deux ans.","I am twenty-two years old.","Age uses avoir."),("Je viens d'Angola.","I come from Angola.","De becomes d' before a vowel."),("J'habite à Toronto.","I live in Toronto.","Use à before a city."),("Je parle anglais et un peu français.","I speak English and a little French.","Un peu means a little."),("Quelle langue parlez-vous ?","What language do you speak?","Parlez-vous is the formal inversion form.")],
"conversations":[("First introduction",[("A","Bonjour ! Je m'appelle Nadia. Et vous ?"),("B","Je m'appelle Lucas. Enchanté."),("A","Enchantée. Vous venez d'où ?"),("B","Je viens du Canada. Et vous ?"),("A","Je viens d'Angola.")],"A: Hello! My name is Nadia. And you? B: My name is Lucas. Nice to meet you. A: Nice to meet you. Where are you from? B: I'm from Canada. And you? A: I'm from Angola."),("At a language class",[("A","Tu habites où ?"),("B","J'habite à Montréal. Et toi ?"),("A","J'habite à Québec."),("B","Tu parles quelles langues ?"),("A","Je parle anglais et français.")],"A: Where do you live? B: I live in Montreal. And you? A: I live in Quebec City. B: Which languages do you speak? A: I speak English and French.")],
"speaking":["Introduce yourself in four sentences: name, age, origin and city.","Ask Quel âge avez-vous ? with a clear liaison between avez and vous.","Practise country phrases: d'Angola, du Canada, de France, des États-Unis.","Spell your first name aloud using French letter names from Lesson 1.","Perform both dialogues without reading the English translation."],
"summary":["Use Je m'appelle to give your name.","Use avoir, not être, to state your age.","Use venir de for origin and habiter à for a city.","Use parler to describe languages you speak."]
},
4:{
"title":"Numbers, Counting and Basic Mathematics","goal":"Count, understand numbers used in daily life, and perform simple arithmetic in French.",
"vocab":[
("zéro","zero","zay-roh","/ze.ʁo/","Zéro plus un égale un."),
("un / une","one","uhn / ün","/œ̃/","Un livre et une table."),
("deux","two","duh","/dø/","J'ai deux stylos."),
("trois","three","trwah","/tʁwa/","Trois personnes arrivent."),
("quatre","four","katr","/katʁ/","Quatre cafés, s'il vous plaît."),
("cinq","five","sank","/sɛ̃k/","Cinq jours."),
("six","six","seess","/sis/","Six étudiants."),
("sept","seven","set","/sɛt/","Sept heures."),
("huit","eight","weet","/ɥit/","Huit livres."),
("neuf","nine","nurf","/nœf/","Neuf dollars."),
("dix","ten","deess","/dis/","Dix minutes."),
("vingt","twenty","van","/vɛ̃/","Vingt personnes."),
("trente","thirty","trahnt","/tʁɑ̃t/","Trente jours."),
("cent","one hundred","sahn","/sɑ̃/","Cent dollars."),
("mille","one thousand","meel","/mil/","Mille habitants.")
],
"grammar":[
("Numbers 0–16","Memorise zéro, un, deux, trois, quatre, cinq, six, sept, huit, neuf, dix, onze, douze, treize, quatorze, quinze, seize. These forms are the foundation for larger numbers."),
("Building 17–69","Seventeen to nineteen are dix-sept, dix-huit, dix-neuf. Twenty to sixty are vingt, trente, quarante, cinquante, soixante. Combine with a hyphen: vingt-deux, trente-cinq, cinquante-neuf. Add et un in forms such as vingt et un."),
("Numbers 70–99","In standard French used in Quebec, 70 is soixante-dix, 71 soixante et onze, 80 quatre-vingts, 81 quatre-vingt-un, and 90 quatre-vingt-dix. Quebec speakers may also use septante in some contexts, but soixante-dix is widely understood."),
("Hundreds and thousands","Cent means 100 and mille means 1,000. Use deux cents when exactly 200, but deux cent un for 201 (cent loses its plural s before another number). Mille does not take a plural s: deux mille."),
("Basic arithmetic","Plus means plus, moins means minus, fois means times, divisé par means divided by, and égale/égalent means equals. Example: trois plus deux égale cinq.")
],
"expressions":[("Combien ?","How many? / How much?","Ask about quantity or price."),("Quel numéro ?","Which number?","Ask for a number."),("Ça coûte combien ?","How much does it cost?","Useful when shopping."),("plus","plus","Addition."),("moins","minus","Subtraction."),("fois","times","Multiplication.")],
"examples":[("Douze plus huit égale vingt.","Twelve plus eight equals twenty.","Addition uses plus and égale."),("Trente moins cinq égale vingt-cinq.","Thirty minus five equals twenty-five.","The result is vingt-cinq."),("J'ai trois frères.","I have three brothers.","Numbers do not change for gender here."),("Il est huit heures.","It is eight o'clock.","The number huit is used with heures."),("Ce livre coûte vingt dollars.","This book costs twenty dollars.","Cost can be expressed with coûter."),("La ville compte cent mille habitants.","The city has one hundred thousand inhabitants.","Cent mille is 100,000.")],
"conversations":[("Buying three items",[("A","Combien coûtent ces stylos ?"),("B","Trois dollars chacun."),("A","J'en prends trois, s'il vous plaît."),("B","Ça fait neuf dollars.")],"A: How much are these pens? B: Three dollars each. A: I'll take three, please. B: That comes to nine dollars."),("Simple maths in class",[("A","Combien font sept plus huit ?"),("B","Quinze."),("A","Exactement ! Et dix fois deux ?"),("B","Vingt.")],"A: What is seven plus eight? B: Fifteen. A: Exactly! And ten times two? B: Twenty.")],
"speaking":["Count from zéro to vingt slowly, then backwards from vingt to zéro.","Practise the difference between un and une; connect each with a noun.","Say 21, 32, 48, 57, 71, 80, 86 and 95 aloud.","Read five arithmetic sums aloud and say the result in French.","Say your phone number digit by digit, grouping it naturally."],
"summary":["Memorise 0–16 before building larger numbers.","Build 17–69 with tens and units joined by hyphens.","Learn the special patterns for 70, 80 and 90.","Use cent and mille for larger quantities.","Use plus, moins, fois and divisé par for arithmetic."]
},
5:{
"title":"Days, Months, Seasons and Dates","goal":"Name weekdays, months and seasons, and ask or give a calendar date.",
"vocab":[
("lundi","Monday","luhn-dee","/lœ̃.di/","Je travaille lundi."),
("mardi","Tuesday","mahr-dee","/maʁ.di/","À mardi !"),
("mercredi","Wednesday","mehr-kruh-dee","/mɛʁ.kʁə.di/","Le cours est mercredi."),
("jeudi","Thursday","zhuh-dee","/ʒø.di/","Jeudi, je suis libre."),
("vendredi","Friday","vahn-druh-dee","/vɑ̃.dʁə.di/","C'est vendredi."),
("samedi","Saturday","sahm-dee","/sam.di/","Samedi, je me repose."),
("dimanche","Sunday","dee-mahnsh","/di.mɑ̃ʃ/","Dimanche est calme."),
("janvier","January","zhahn-vyay","/ʒɑ̃.vje/","En janvier, il fait froid."),
("février","February","fay-vree-ay","/fe.vʁi.je/","Mon anniversaire est en février."),
("mars","March","mars","/maʁs/","Le printemps commence en mars."),
("avril","April","ah-vreel","/a.vʁil/","En avril, il pleut souvent."),
("mai","May","may","/mɛ/","Le mois de mai."),
("juin","June","zhwan","/ʒɥɛ̃/","En juin, les jours sont longs."),
("juillet","July","zhwee-yay","/ʒɥi.jɛ/","Juillet est un mois d'été."),
("août","August","oot","/ut/","En août, je voyage.")
],
"grammar":[
("Weekdays are masculine","Days of the week are masculine nouns: le lundi, le mardi, etc. Unlike English, French weekdays are normally written in lowercase."),
("A recurring day versus one specific day","Use le + weekday for a repeated routine: Le lundi, j'étudie (On Mondays, I study). Without le, it can refer to one upcoming or understood day: Je pars lundi (I'm leaving on Monday)."),
("Months and seasons with en","Use en with months and most seasons: en janvier, en été, en automne, en hiver, au printemps. Month names are lowercase."),
("Giving a date","Use le + number + month: le 14 juillet. The first day of a month is le premier: le premier mai. Ask Quelle est la date aujourd'hui ?"),
("Ordinal numbers for dates","For calendar dates, use cardinal numbers except the first: le deux mai, le quinze juin, but le premier avril. The year follows the date: le 14 juillet 2026.")
],
"expressions":[("Quel jour sommes-nous ?","What day is it?","Ask for the weekday."),("On est quel jour ?","What day is it?","Common spoken alternative."),("Quelle est la date aujourd'hui ?","What's today's date?","Ask for the full date."),("le week-end","the weekend","Saturday and Sunday."),("la semaine prochaine","next week","Future time expression."),("le mois dernier","last month","Past time expression.")],
"examples":[("Aujourd'hui, nous sommes lundi.","Today is Monday.","Use sommes with nous."),("Mon anniversaire est le 3 mai.","My birthday is May 3.","Use le before the date."),("Je pars en juillet.","I'm leaving in July.","Use en before a month."),("En hiver, il neige souvent.","In winter, it often snows.","En hiver means in winter."),("Le samedi, je fais du sport.","On Saturdays, I do sport.","Le + weekday expresses a routine."),("Le premier janvier est un jour férié.","January first is a public holiday.","Premier is used for the first day.")],
"conversations":[("Planning a meeting",[("A","Tu es libre vendredi ?"),("B","Oui, vendredi après-midi."),("A","On se retrouve le 12 juin ?"),("B","D'accord. À vendredi !")],"A: Are you free Friday? B: Yes, Friday afternoon. A: Shall we meet on June 12? B: Okay. See you Friday!"),("Talking about a birthday",[("A","C'est quand, ton anniversaire ?"),("B","Le 8 octobre."),("A","Ah, en automne !"),("B","Oui, exactement.")],"A: When is your birthday? B: October 8. A: Ah, in autumn! B: Yes, exactly.")],
"speaking":["Say all seven weekdays in order, then backwards.","Practise the months from janvier to décembre without translating.","Say today's date using le + number + month.","Describe your favourite season with En… and one simple reason.","Read a weekly schedule aloud using le + weekday for recurring activities."],
"summary":["Weekdays and months are lowercase in French.","Use le + weekday for repeated routines.","Use en before most months and seasons, but au printemps.","Use le premier for the first day of a month."]
},
6:{
"title":"Time, Clock and Daily Expressions","goal":"Ask and tell the time, describe parts of the day and use common time expressions.",
"vocab":[
("l'heure (f.)","time; hour","luhr","/lœʁ/","Quelle heure est-il ?"),
("une heure","one o'clock; one hour","ün uhr","/yn œʁ/","Il est une heure."),
("midi","noon","mee-dee","/mi.di/","À midi, je mange."),
("minuit","midnight","mee-nwee","/mi.nɥi/","Il est minuit."),
("et quart","quarter past","ay kar","/e kaʁ/","Il est deux heures et quart."),
("et demie","half past","ay duh-mee","/e də.mi/","Il est trois heures et demie."),
("moins le quart","quarter to","mwan luh kar","/mwɛ̃ lə kaʁ/","Il est cinq heures moins le quart."),
("le matin","morning","luh mah-tan","/lə ma.tɛ̃/","Je travaille le matin."),
("l'après-midi (m.)","afternoon","lah-preh-mee-dee","/la.pʁe.mi.di/","Je lis l'après-midi."),
("le soir","evening","luh swahr","/lə swaʁ/","Je rentre le soir."),
("tôt","early","toh","/to/","Je me lève tôt."),
("tard","late","tar","/taʁ/","Il est tard."),
("maintenant","now","man-tuh-nahn","/mɛ̃t.nɑ̃/","Je pars maintenant."),
("bientôt","soon","byan-toh","/bjɛ̃.to/","À bientôt !"),
("demain","tomorrow","duh-man","/də.mɛ̃/","À demain.")
],
"grammar":[
("The basic question","Ask Quelle heure est-il ? (What time is it?). The standard answer begins Il est…: Il est deux heures. For one o'clock, say Il est une heure."),
("Minutes after the hour","Say Il est deux heures dix (2:10), deux heures et quart (2:15), and deux heures et demie (2:30). Heure is singular after une and plural after other numbers."),
("Minutes before the next hour","Use moins: Il est trois heures moins dix (2:50). Il est quatre heures moins le quart means 3:45. In everyday Quebec speech, digital-style time is also common."),
("Noon and midnight","Use Il est midi and Il est minuit, not midi heures or minuit heures. To specify a time of day, add du matin, de l'après-midi or du soir."),
("At a particular time","Use à before a clock time: à huit heures, à midi, à minuit. Use vers for approximately: vers huit heures (around eight).")
],
"expressions":[("Quelle heure est-il ?","What time is it?","Standard question."),("Il est quelle heure ?","What time is it?","Common spoken word order."),("à l'heure","on time","Opposite of en retard."),("en avance","early; ahead of time","Arrive before the expected time."),("en retard","late","Arrive after the expected time."),("tout de suite","right away","Immediate action.")],
"examples":[("Il est sept heures du matin.","It is seven in the morning.","Use du matin to clarify."),("Le film commence à huit heures et demie.","The film starts at 8:30.","À marks the scheduled time."),("Je déjeune à midi.","I have lunch at noon.","Midi is used without heures."),("Le train arrive vers dix-huit heures.","The train arrives around 6 p.m.","Vers means approximately."),("Nous sommes en retard de cinq minutes.","We are five minutes late.","En retard describes lateness."),("Je rentre tard le soir.","I come home late in the evening.","Tard is an adverb meaning late.")],
"conversations":[("Asking for the time",[("A","Excusez-moi, quelle heure est-il ?"),("B","Il est trois heures et quart."),("A","Merci beaucoup !"),("B","Je vous en prie.")],"A: Excuse me, what time is it? B: It is 3:15. A: Thank you very much! B: You're welcome."),("Arranging a call",[("A","On se parle à quelle heure ?"),("B","Vers dix-neuf heures ?"),("A","Parfait. À tout à l'heure !"),("B","À plus tard !")],"A: What time shall we talk? B: Around 7 p.m.? A: Perfect. See you later today! B: See you later!")],
"speaking":["Read digital times aloud: 1:00, 2:15, 4:30, 6:45 and 9:50.","Practise the difference between midi and minuit.","Say your normal wake-up time using Je me lève à…","Describe one morning, afternoon and evening activity.","Role-play asking a stranger for the time politely."],
"summary":["Ask Quelle heure est-il ? and answer Il est…","Use une heure for 1:00 and heures for other hours.","Use et quart, et demie and moins le quart for common clock times.","Use à before a specific time and vers for an approximate time."]
},
7:{
"title":"Nouns, Gender and Articles","goal":"Recognise masculine and feminine nouns and choose definite, indefinite and plural articles.",
"vocab":[
("un livre","a book (masculine)","uhn leevr","/œ̃ livʁ/","C'est un livre."),
("une table","a table (feminine)","ün tahbl","/yn tabl/","La table est grande."),
("un garçon","a boy","uhn gar-sohn","/œ̃ ɡaʁ.sɔ̃/","Le garçon lit."),
("une fille","a girl","ün fee-yuh","/yn fij/","La fille parle."),
("un ami","a male friend","uhn ah-mee","/œ̃ a.mi/","C'est un ami."),
("une amie","a female friend","ün ah-mee","/yn a.mi/","C'est une amie."),
("l'école (f.)","school","lay-kohl","/le.kɔl/","L'école est près d'ici."),
("l'hôtel (m.)","hotel","loh-tell","/lo.tɛl/","L'hôtel est grand."),
("des livres","some books","day leevr","/de livʁ/","J'ai des livres."),
("les maisons","the houses","lay may-zohn","/le mɛ.zɔ̃/","Les maisons sont belles."),
("le chat","the cat","luh shah","/lə ʃa/","Le chat dort."),
("la voiture","the car","lah vwah-tür","/la vwa.tyʁ/","La voiture est neuve.")
],
"grammar":[
("Every noun has grammatical gender","French nouns are masculine or feminine, even when they refer to objects. Learn each noun with its article: un livre, une table. Gender is grammatical, not necessarily related to physical sex."),
("Definite articles: le, la, l', les","Use le with masculine singular nouns, la with feminine singular nouns, l' before a vowel or silent h, and les for plural nouns of either gender: le livre, la table, l'école, les livres."),
("Indefinite articles: un, une, des","Use un for masculine singular, une for feminine singular, and des for plural when introducing unspecified things: un livre, une voiture, des amis."),
("Plural formation","Most written nouns form the plural by adding -s, which is usually silent: un livre → des livres. Words ending in -s, -x or -z often stay unchanged. There are exceptions, such as un cheval → des chevaux, which can be learned later."),
("Elision before vowels","Le and la become l' before a vowel sound or silent h: l'école, l'hôtel. The apostrophe replaces the missing vowel. Do not elide before an aspirated h in words such as le héros.")
],
"expressions":[("C'est un / une…","It is a…","Identify one thing."),("Ce sont des…","These are…","Identify plural things."),("Qu'est-ce que c'est ?","What is it?","Ask what something is."),("C'est quoi ?","What's that?","Informal spoken alternative."),("un peu de","a little of","Quantity expression; later article changes are studied."),("beaucoup de","a lot of","Common quantity phrase.")],
"examples":[("C'est un livre.","It is a book.","Livre is masculine, so use un."),("C'est une chaise.","It is a chair.","Chaise is feminine, so use une."),("L'école est grande.","The school is big.","École begins with a vowel, so use l'."),("Les étudiants arrivent.","The students are arriving.","Les is plural for both genders."),("J'ai des amis à Montréal.","I have friends in Montreal.","Des introduces an unspecified plural."),("L'hôtel est près de la gare.","The hotel is near the station.","Hôtel is masculine but takes l' because of its initial vowel.")],
"conversations":[("Identifying objects",[("A","Qu'est-ce que c'est ?"),("B","C'est une table."),("A","Et ça ?"),("B","Ce sont des livres.")],"A: What is it? B: It is a table. A: And that? B: Those are books."),("At school",[("A","Où est le professeur ?"),("B","Le professeur est dans l'école."),("A","Et les étudiants ?"),("B","Les étudiants sont dans la classe.")],"A: Where is the teacher? B: The teacher is in the school. A: And the students? B: The students are in the classroom.")],
"speaking":["Say each noun with its article; never practise livre alone, practise un livre or le livre.","Sort ten objects around you into masculine and feminine groups after checking a dictionary.","Read aloud le, la, l' and les with example nouns.","Practise singular-to-plural pairs: un livre/des livres; une voiture/des voitures.","Ask Qu'est-ce que c'est ? and answer with C'est… or Ce sont…"],
"summary":["Every French noun has grammatical gender.","Use un/une/des for indefinite articles.","Use le/la/l'/les for definite articles.","Use les and des with plural nouns of either gender.","Learn nouns together with their article."]
},
8:{
"title":"Subject Pronouns and the Verb ÊTRE","goal":"Use subject pronouns and conjugate être to identify people, describe identity and say where someone is.",
"vocab":[
("je","I","zhuh","/ʒə/","Je suis étudiant."),
("tu","you (singular informal)","tü","/ty/","Tu es gentil."),
("il","he; it (masculine)","eel","/il/","Il est ici."),
("elle","she; it (feminine)","ell","/ɛl/","Elle est prête."),
("on","one; we; people","ohn","/ɔ̃/","On est à la maison."),
("nous","we","noo","/nu/","Nous sommes amis."),
("vous","you (formal or plural)","voo","/vu/","Vous êtes professeur."),
("ils","they (masculine or mixed)","eel","/il/","Ils sont canadiens."),
("elles","they (all feminine)","ell","/ɛl/","Elles sont étudiantes."),
("être","to be","ehtr","/ɛtʁ/","Je veux être prêt."),
("ici","here","ee-see","/i.si/","Je suis ici."),
("fatigué(e)","tired","fah-tee-gay","/fa.ti.ɡe/","Elle est fatiguée.")
],
"grammar":[
("Subject pronouns","Je = I; tu = informal singular you; il/elle = he/she; on = one/people/colloquial we; nous = we; vous = formal or plural you; ils/elles = they. Use vous for politeness or when addressing more than one person."),
("Être in the present tense","The forms are je suis, tu es, il/elle/on est, nous sommes, vous êtes, ils/elles sont. Memorise the forms because être is irregular and extremely common."),
("When to use être","Use être for identity, profession (often without an article), nationality, descriptions and location: Je suis canadien; Elle est médecin; Nous sommes ici. Professions and nationalities agree with the person where appropriate."),
("Adjective agreement","Many adjectives add -e in the feminine and -s in the plural: étudiant/étudiante, canadien/canadienne, fatigué/fatiguée. Some forms are irregular. The verb stays the same; the adjective changes."),
("Contractions and spoken French","Je becomes j' before a vowel: je suis, but j'aime (covered in later lessons). In spoken Quebec French, tu may have additional colloquial uses; at A1, learn standard tu as the informal subject pronoun.")
],
"expressions":[("Je suis…","I am…","Introduce or describe yourself."),("Tu es…","You are…","Informal singular."),("Il est / Elle est…","He is / She is…","Describe another person."),("Nous sommes…","We are…","Use with nous."),("Vous êtes…","You are…","Formal or plural."),("C'est…","It is… / This is…","Very common identification phrase.")],
"examples":[("Je suis étudiant.","I am a student.","Être uses suis with je."),("Tu es très gentil.","You are very kind.","Es agrees with tu; gentil describes a male person."),("Elle est canadienne.","She is Canadian.","The adjective has feminine agreement."),("Nous sommes à Luanda.","We are in Luanda.","Être can express location."),("Vous êtes professeur ?","Are you a teacher?","A rising intonation can form a spoken question."),("Ils sont contents.","They are happy.","Sont is the ils/elles form.")],
"conversations":[("At a class",[("A","Bonjour ! Je suis Lina."),("B","Enchanté. Je suis Marc."),("A","Vous êtes professeur ?"),("B","Non, je suis étudiant.")],"A: Hello! I'm Lina. B: Nice to meet you. I'm Marc. A: Are you a teacher? B: No, I'm a student."),("Introducing friends",[("A","Qui est-ce ?"),("B","C'est mon ami, Paul."),("A","Il est canadien ?"),("B","Oui, il est de Montréal.")],"A: Who is that? B: That's my friend, Paul. A: Is he Canadian? B: Yes, he's from Montreal.")],
"speaking":["Conjugate être aloud without looking: suis, es, est, sommes, êtes, sont.","Say one sentence for each subject pronoun.","Practise the contrast tu es and vous êtes.","Describe three people using être plus an adjective with correct agreement.","Read the conversations and make your voice rise naturally for yes/no questions."],
"summary":["Know all six present-tense forms of être.","Choose tu for informal singular and vous for formal or plural.","Use être for identity, profession, nationality, description and location.","Make adjectives agree in gender and number."]
},
9:{
"title":"The Verb AVOIR and Possession","goal":"Conjugate avoir, express possession and age, and use common avoir expressions.",
"vocab":[
("avoir","to have","ah-vwahr","/a.vwaʁ/","J'aime avoir du temps."),
("j'ai","I have","zhay","/ʒe/","J'ai un frère."),
("tu as","you have","tü ah","/ty a/","Tu as un livre."),
("il / elle a","he / she has","eel ah / ell ah","/il a/","Elle a une voiture."),
("nous avons","we have","noo zah-vohn","/nu za.vɔ̃/","Nous avons une maison."),
("vous avez","you have","voo zah-vay","/vu za.ve/","Vous avez une question."),
("ils / elles ont","they have","eel ohn / ell ohn","/il ɔ̃/","Ils ont deux enfants."),
("un frère","a brother","uhn frair","/œ̃ fʁɛʁ/","J'ai un frère."),
("une sœur","a sister","ün suhr","/yn sœʁ/","Elle a une sœur."),
("un animal","an animal","uhn ah-nee-mal","/œ̃ a.ni.mal/","Nous avons un animal."),
("faim","hunger","fan","/fɛ̃/","J'ai faim."),
("soif","thirst","swahf","/swaf/","Tu as soif ?")
],
"grammar":[
("Avoir in the present tense","The forms are j'ai, tu as, il/elle/on a, nous avons, vous avez, ils/elles ont. Avoir is irregular and must be memorised."),
("Possession","Use avoir + noun: J'ai un téléphone (I have a phone). French uses an article in many places where English may use a possessive or omit one. Possessive adjectives are introduced in a later lesson."),
("Age","French expresses age with avoir: Elle a dix-huit ans. The question is Quel âge as-tu ? or Quel âge avez-vous ? Never translate I am 18 as Je suis 18."),
("Common avoir expressions","Avoir faim = to be hungry; avoir soif = to be thirsty; avoir chaud = to feel hot; avoir froid = to feel cold; avoir sommeil = to be sleepy; avoir peur = to be afraid."),
("Être or avoir","Use être for identity and descriptions (Je suis canadien) and avoir for possession and age (J'ai un frère; J'ai vingt ans). Compare the meaning, not the English verb alone.")
],
"expressions":[("J'ai faim.","I'm hungry.","Literally, I have hunger."),("J'ai soif.","I'm thirsty.","Literally, I have thirst."),("J'ai chaud.","I'm hot.","Describes how you feel."),("J'ai froid.","I'm cold.","Describes how you feel."),("J'ai sommeil.","I'm sleepy.","Common everyday phrase."),("Tu as raison.","You're right.","Fixed avoir expression.")],
"examples":[("J'ai deux sœurs.","I have two sisters.","Avoir expresses family relationships."),("Nous avons une petite maison.","We have a small house.","Avons is the nous form."),("Vous avez quel âge ?","How old are you?","A common spoken question."),("Il a très faim.","He is very hungry.","French uses avoir faim."),("Elles ont un chien.","They have a dog.","Ont is pronounced differently from sont."),("J'ai froid en hiver.","I feel cold in winter.","Avoir froid describes a sensation.")],
"conversations":[("Talking about family",[("A","Tu as des frères et sœurs ?"),("B","Oui, j'ai un frère et deux sœurs."),("A","Quel âge a ton frère ?"),("B","Il a vingt ans.")],"A: Do you have brothers and sisters? B: Yes, I have one brother and two sisters. A: How old is your brother? B: He is twenty."),("At a café",[("A","Tu as soif ?"),("B","Oui, j'ai très soif."),("A","Tu veux de l'eau ?"),("B","Oui, merci !")],"A: Are you thirsty? B: Yes, I'm very thirsty. A: Do you want some water? B: Yes, thank you!")],
"speaking":["Recite avoir: j'ai, tu as, il a, nous avons, vous avez, ils ont.","Say your age and the ages of two people you know (use fictional details if preferred).","Practise j'ai faim, j'ai soif, j'ai chaud and j'ai froid.","Contrast Elle a and Elle est in two different sentences.","Read the family and café dialogues aloud."],
"summary":["Memorise the six present-tense forms of avoir.","Use avoir for possession and age.","Learn common expressions such as avoir faim and avoir soif.","Do not confuse avoir with être."]
},
10:{
"title":"Common Adjectives and Describing People","goal":"Describe appearance, personality and feelings while placing and agreeing common adjectives correctly.",
"vocab":[
("grand / grande","tall; big","grahn / grahnd","/ɡʁɑ̃/","Il est grand."),
("petit / petite","short; small","puh-tee / puh-teet","/pə.ti/","La petite maison."),
("jeune","young","zhuhn","/ʒœn/","Elle est jeune."),
("vieux / vieille","old","vyuh / vyay","/vjø/","Un vieil ami."),
("beau / belle","beautiful; handsome","boh / bell","/bo/","C'est une belle ville."),
("joli / jolie","pretty","zho-lee","/ʒɔ.li/","Une jolie robe."),
("gentil / gentille","kind","zhahn-tee / zhahn-teey","/ʒɑ̃.ti/","Il est gentil."),
("sympathique","nice; friendly","san-pah-teek","/sɛ̃.pa.tik/","Elle est sympathique."),
("intelligent / intelligente","intelligent","an-tell-ee-zhahn / ahnt","/ɛ̃.te.li.ʒɑ̃/","Un étudiant intelligent."),
("drôle","funny","drohl","/dʁol/","Mon ami est drôle."),
("sérieux / sérieuse","serious","say-ree-uh / say-ree-uhz","/se.ʁjø/","Elle est sérieuse."),
("fatigué / fatiguée","tired","fah-tee-gay","/fa.ti.ɡe/","Je suis fatigué.")
],
"grammar":[
("Adjective agreement","Adjectives usually agree with the noun or person described. Many add -e for feminine and -s for plural: petit, petite, petits, petites. Some have irregular feminine forms: beau/belle, vieux/vieille, gentil/gentille."),
("Adjective position","Many common adjectives come after the noun: une voiture rouge, un étudiant intelligent. A group of frequent short adjectives often comes before the noun, including beau, joli, jeune, vieux, grand and petit: une belle maison."),
("Masculine and feminine forms","For a masculine person, say Il est grand. For a feminine person, say Elle est grande. The spoken ending may be silent in the masculine and audible in the feminine, as in petit/petite."),
("Être + adjective","Use être + adjective to describe a person: Je suis content; Elle est sympathique; Ils sont sérieux. The adjective agrees with the subject."),
("Describing more than one quality","Join adjectives with et: Elle est intelligente et drôle. Use très before an adjective for very: Il est très gentil. Très does not change form.")
],
"expressions":[("Il est comment ?","What is he like?","Ask about a man's character or appearance."),("Elle est comment ?","What is she like?","Ask about a woman's character or appearance."),("Il a l'air…","He looks…","Avoir l'air introduces an impression."),("très sympa","very nice","Common informal shortening of sympathique."),("pas mal","not bad; pretty good","Context-dependent spoken expression."),("à mon avis","in my opinion","Introduce a personal view.")],
"examples":[("Mon frère est grand et sportif.","My brother is tall and athletic.","Both adjectives describe a masculine person."),("Ma sœur est petite et drôle.","My sister is short and funny.","Petite agrees with sœur."),("C'est une belle maison.","It is a beautiful house.","Belle comes before the noun."),("Le professeur est très sympathique.","The teacher is very friendly.","Très intensifies the adjective."),("Les enfants sont fatigués.","The children are tired.","Plural agreement adds -s in writing."),("À mon avis, elle est intelligente.","In my opinion, she is intelligent.","À mon avis introduces an opinion.")],
"conversations":[("Describing a friend",[("A","Comment est ton ami ?"),("B","Il est grand, drôle et sympathique."),("A","Il est sérieux aussi ?"),("B","Oui, mais il aime plaisanter.")],"A: What is your friend like? B: He is tall, funny and friendly. A: Is he serious too? B: Yes, but he likes joking."),("Choosing a gift",[("A","Tu aimes cette jolie robe ?"),("B","Oui, elle est très belle."),("A","La couleur est magnifique !"),("B","Je suis d'accord.")],"A: Do you like this pretty dress? B: Yes, it is very beautiful. A: The colour is magnificent! B: I agree.")],
"speaking":["Describe yourself with three adjectives, checking feminine or masculine agreement as needed.","Describe two fictional people using at least four adjectives each.","Practise adjective pairs: petit/petite, grand/grande, beau/belle, vieux/vieille.","Read sentences with pre-noun adjectives and post-noun adjectives.","Give a simple opinion using À mon avis…"],
"summary":["Adjectives agree in gender and number with the person or noun.","Many adjectives follow the noun; common beauty, age and size adjectives often precede it.","Use être + adjective for descriptions.","Use très to intensify an adjective and et to connect qualities."]
},
11:{
"title":"Family Members and Relationships","goal":"Name close and extended family members and describe family relationships with simple sentences.",
"vocab":[
("la famille","family","lah fah-mee-yuh","/la fa.mij/","Ma famille est grande."),
("les parents","parents","lay pah-rahn","/le pa.ʁɑ̃/","Mes parents habitent ici."),
("la mère","mother","lah mehr","/la mɛʁ/","Ma mère est gentille."),
("le père","father","luh pehr","/lə pɛʁ/","Mon père travaille."),
("le frère","brother","luh frair","/lə fʁɛʁ/","J'ai un frère."),
("la sœur","sister","lah suhr","/la sœʁ/","Ma sœur est jeune."),
("le fils","son","luh fees","/lə fis/","Leur fils est étudiant."),
("la fille","daughter; girl","lah fee-yuh","/la fij/","Sa fille a dix ans."),
("le grand-père","grandfather","luh grahn-pehr","/lə ɡʁɑ̃.pɛʁ/","Mon grand-père est drôle."),
("la grand-mère","grandmother","lah grahn-mehr","/la ɡʁɑ̃.mɛʁ/","Ma grand-mère aime lire."),
("le mari","husband","luh mah-ree","/lə ma.ʁi/","Son mari est médecin."),
("la femme","wife; woman","lah fam","/la fam/","Sa femme parle français."),
("le cousin / la cousine","cousin","koo-zan / koo-zeen","/ku.zɛ̃/","Ma cousine habite à Ottawa."),
("l'oncle (m.)","uncle","lohnkl","/lɔ̃kl/","Mon oncle arrive demain."),
("la tante","aunt","lah tahnt","/la tɑ̃t/","Ma tante est sympathique.")
],
"grammar":[
("Family nouns and gender","Family words have grammatical gender: le père, la mère, le frère, la sœur. Learn the article with the noun. Some words have a masculine and feminine pair, such as cousin/cousine."),
("Possessive adjectives: my","Use mon with a masculine singular noun, ma with a feminine singular noun, and mes with plural nouns: mon père, ma mère, mes parents. Before a feminine noun beginning with a vowel sound, use mon for easier pronunciation: mon amie."),
("His, her and their","Son, sa and ses mean his or her depending on the noun possessed, not the owner's gender: son père can mean his father or her father; sa mère means his/her mother; ses parents means his/her parents."),
("Talking about family with avoir","Use avoir to state family relationships: J'ai deux frères; Elle a une sœur. Use être to describe them: Mon frère est gentil."),
("Plural family groups","Use les parents for parents, les grands-parents for grandparents and les enfants for children. A mixed group of brothers and sisters can be called les frères et sœurs.")
],
"expressions":[("Voici ma famille.","Here is my family.","Introduce family members."),("C'est mon frère.","This is my brother.","Identify a masculine family member."),("Je suis fils unique / fille unique.","I'm an only child.","Fils unique for a male speaker; fille unique for a female speaker."),("Nous sommes très proches.","We are very close.","Describe a close relationship."),("On s'entend bien.","We get along well.","Common everyday expression."),("J'ai deux enfants.","I have two children.","State how many children you have.")],
"examples":[("Ma mère s'appelle Claire.","My mother's name is Claire.","Ma agrees with the feminine noun mère."),("Mon père est très drôle.","My father is very funny.","Mon is used with masculine père."),("Mes grands-parents habitent au Canada.","My grandparents live in Canada.","Mes is plural."),("Sa sœur a vingt ans.","His/her sister is twenty.","Sa agrees with sœur, not the owner's gender."),("Nous avons trois enfants.","We have three children.","Avoir expresses family relationships."),("Mon amie est médecin.","My female friend is a doctor.","Mon is used before amie because it begins with a vowel sound.")],
"conversations":[("Talking about siblings",[("A","Tu as des frères et sœurs ?"),("B","Oui, j'ai une sœur et deux frères."),("A","Ils habitent près de toi ?"),("B","Oui, nous sommes dans la même ville.")],"A: Do you have brothers and sisters? B: Yes, I have one sister and two brothers. A: Do they live near you? B: Yes, we're in the same city."),("Showing a family photo",[("A","Qui est cette personne ?"),("B","C'est ma grand-mère."),("A","Elle est très souriante !"),("B","Oui, elle est toujours heureuse.")],"A: Who is this person? B: This is my grandmother. A: She is very smiley! B: Yes, she is always happy.")],
"speaking":["Describe your family or an imaginary family using at least six family words.","Practise mon père, ma mère, mes parents and mes grands-parents.","Say three sentences with son/sa/ses and explain which noun controls the form.","Read the two dialogues aloud, paying attention to liaison in mes amis if you add that phrase.","Describe one family relationship with On s'entend bien."],
"summary":["Learn family nouns with their gender and article.","Use mon, ma, mes according to the noun possessed.","Son, sa and ses agree with the thing possessed, not the owner.","Use avoir for family relationships and être for descriptions."]
},
12:{
"title":"Colours, Objects and Describing Things","goal":"Name everyday objects, use common colours and demonstrate adjective agreement and position.",
"vocab":[
("rouge","red","roozh","/ʁuʒ/","Une pomme rouge."),
("bleu / bleue","blue","bluh / bluh","/blø/","Un sac bleu."),
("vert / verte","green","vair / vair-tuh","/vɛʁ/","Une porte verte."),
("jaune","yellow","zhohn","/ʒon/","Un livre jaune."),
("noir / noire","black","nwahr / nwahr","/nwaʁ/","Une voiture noire."),
("blanc / blanche","white","blahn / blahnsh","/blɑ̃/","Une chemise blanche."),
("gris / grise","grey","gree / greez","/ɡʁi/","Un mur gris."),
("orange","orange","oh-rahnzh","/ɔ.ʁɑ̃ʒ/","Des fleurs orange."),
("rose","pink","rohz","/ʁoz/","Une robe rose."),
("violet / violette","purple","vee-oh-lay / vee-oh-let","/vjɔ.lɛ/","Une boîte violette."),
("un sac","a bag","uhn sak","/œ̃ sak/","Mon sac est noir."),
("une clé","a key","ün clay","/yn kle/","Voici une clé.")
],
"grammar":[
("Colour adjectives agree","Most colour adjectives agree in gender and number: un sac vert, une porte verte, des sacs verts, des portes vertes. Learn irregular spellings such as blanc/blanche."),
("Invariable colour names","Some colour words derived from nouns are often invariable, including orange and marron: des chaussures orange, des yeux marron. Compound colour adjectives are also generally invariable."),
("Adjective position","Colours usually follow the noun: une voiture rouge, un pantalon noir. This contrasts with many common size/beauty adjectives that can come before the noun."),
("Demonstrative adjectives","Ce means this/that before a masculine singular noun, cet before a masculine singular noun beginning with a vowel or silent h, cette before feminine singular, and ces before plural: ce livre, cet objet, cette table, ces clés."),
("Identifying objects with c'est","Use C'est + singular noun and Ce sont + plural noun: C'est un téléphone; Ce sont des clés. Use Ça, c'est… to point something out in conversation.")
],
"expressions":[("De quelle couleur ?","What colour?","Ask about colour."),("C'est de quelle couleur ?","What colour is it?","Conversational question."),("J'aime cette couleur.","I like this colour.","Express preference."),("Ça, c'est…","That is…","Point something out."),("ceci / cela","this / that","More formal demonstratives; ça is common in speech."),("de toutes les couleurs","in all colours","Describe variety.")],
"examples":[("Le sac est bleu.","The bag is blue.","Bleu follows the noun."),("La porte est verte.","The door is green.","Verte agrees with feminine porte."),("J'aime cette robe noire.","I like this black dress.","Cette agrees with robe; noire agrees too."),("Ce sont des clés jaunes.","These are yellow keys.","Ce sont introduces a plural."),("Cet objet est très petit.","This object is very small.","Cet is used before a masculine vowel-starting noun."),("Les murs sont blancs.","The walls are white.","Blanc becomes blancs in masculine plural.")],
"conversations":[("Describing a lost bag",[("A","Vous cherchez quelque chose ?"),("B","Oui, mon sac."),("A","Il est de quelle couleur ?"),("B","Il est noir avec une petite étiquette rouge.")],"A: Are you looking for something? B: Yes, my bag. A: What colour is it? B: It is black with a small red label."),("Choosing an object",[("A","Tu préfères ce stylo bleu ou ce stylo vert ?"),("B","Je préfère le bleu."),("A","Pourquoi ?"),("B","J'aime cette couleur.")],"A: Do you prefer this blue pen or this green pen? B: I prefer the blue one. A: Why? B: I like this colour.")],
"speaking":["Name five objects around you and describe each with a colour.","Practise feminine colour forms: verte, blanche, noire, violette.","Point to objects and say ce, cet, cette or ces + noun.","Describe a fictional room using at least six colours.","Read the lost-bag dialogue with clear adjective agreement."],
"summary":["Most colour adjectives follow the noun and agree in gender and number.","Remember irregular forms such as blanc/blanche and violet/violette.","Orange and marron are commonly invariable when used as colours.","Use ce, cet, cette and ces to say this/that/these/those."]
},
13:{
"title":"Food, Drinks and Basic Restaurant Vocabulary","goal":"Name common foods and drinks, express preferences, order politely and understand a simple café interaction.",
"vocab":[
("le pain","bread","luh pan","/lə pɛ̃/","Je mange du pain."),
("le fromage","cheese","luh froh-mahzh","/lə fʁɔ.maʒ/","J'aime le fromage."),
("le poulet","chicken","luh poo-lay","/lə pu.lɛ/","Le poulet est prêt."),
("le poisson","fish","luh pwah-sohn","/lə pwa.sɔ̃/","Je préfère le poisson."),
("le riz","rice","luh ree","/lə ʁi/","Nous mangeons du riz."),
("les légumes","vegetables","lay lay-güm","/le le.ɡym/","Les légumes sont frais."),
("les fruits","fruit","lay frwee","/le fʁɥi/","Je mange des fruits."),
("une pomme","an apple","ün pom","/yn pɔm/","Je voudrais une pomme."),
("l'eau (f.)","water","loh","/o/","Un verre d'eau."),
("le lait","milk","luh lay","/lə lɛ/","Je bois du lait."),
("le café","coffee","luh kah-fay","/lə ka.fe/","Un café, s'il vous plaît."),
("le thé","tea","luh tay","/lə te/","Je prends du thé."),
("le menu","menu","luh muh-nü","/lə mə.ny/","Le menu, s'il vous plaît."),
("l'addition (f.)","the bill","lah-dee-syohn","/la.di.sjɔ̃/","L'addition, s'il vous plaît."),
("délicieux / délicieuse","delicious","day-lee-syuh / syuhz","/de.li.sjø/","C'est délicieux !")
],
"grammar":[
("Meals and food preferences","Use aimer + definite article to talk about food in general: J'aime le fromage; Je n'aime pas le poisson. Use adorer for love and préférer for prefer."),
("Partitive articles","Use du with masculine singular, de la with feminine singular, de l' before a vowel, and des with plural to mean some: du pain, de la soupe, de l'eau, des légumes. These forms express an unspecified quantity."),
("Ordering politely with je voudrais","Je voudrais means I would like and is more polite than je veux. Follow it with a noun: Je voudrais un café. You can also say Je prends… (I'll have…)."),
("Quantities and containers","Use un verre de (a glass of), une bouteille de (a bottle of), une tasse de (a cup of), and un morceau de (a piece of). The article after de depends on the expression and quantity."),
("At a restaurant","Useful phrases include Une table pour deux, s'il vous plaît; La carte, s'il vous plaît; L'addition, s'il vous plaît. In Quebec, déjeuner usually means breakfast, dîner lunch, and souper supper/dinner; usage differs from France.")
],
"expressions":[("Je voudrais…","I would like…","Polite way to order."),("La carte, s'il vous plaît.","The menu, please.","Ask for the menu."),("Qu'est-ce que vous conseillez ?","What do you recommend?","Ask the server for advice."),("C'est délicieux !","It's delicious!","Compliment the food."),("L'addition, s'il vous plaît.","The bill, please.","Ask to pay."),("Bon appétit !","Enjoy your meal!","Said before eating.")],
"examples":[("Je voudrais un café et un croissant.","I would like a coffee and a croissant.","Je voudrais is a polite request."),("Je mange du pain avec du fromage.","I eat bread with cheese.","Du is a partitive article."),("Elle boit de l'eau.","She drinks water.","De l' appears before a vowel sound."),("Nous aimons les fruits.","We like fruit.","Use the definite article for general preferences."),("Est-ce que vous avez une table pour deux ?","Do you have a table for two?","A polite restaurant question."),("Tout est délicieux, merci.","Everything is delicious, thank you.","A natural compliment.")],
"conversations":[("Ordering at a café",[("A","Bonjour. Qu'est-ce que vous désirez ?"),("B","Je voudrais un café et un sandwich, s'il vous plaît."),("A","Sur place ou à emporter ?"),("B","À emporter, merci." )],"A: Hello. What would you like? B: I would like a coffee and a sandwich, please. A: For here or to go? B: To go, thank you."),("Asking for the bill",[("A","Tout était très bon."),("B","Je suis ravi que ça vous ait plu."),("A","L'addition, s'il vous plaît."),("B","Bien sûr. Voilà.")],"A: Everything was very good. B: I'm glad you enjoyed it. A: The bill, please. B: Of course. Here you are.")],
"speaking":["Order three items using Je voudrais… and s'il vous plaît.","Practise du, de la, de l' and des with food nouns.","Say what you like and dislike using J'aime and Je n'aime pas.","Role-play asking for a menu, ordering and requesting the bill.","Practise Quebec meal words déjeuner, dîner and souper in context."],
"summary":["Use aimer + definite article for general food preferences.","Use du, de la, de l' and des for unspecified quantities.","Use Je voudrais to order politely.","Learn restaurant phrases and note Quebec meal-name differences."]
},
14:{
"title":"Present Tense and Everyday Activities","goal":"Talk about routines and everyday activities using common present-tense verbs and simple time phrases.",
"vocab":[
("parler","to speak","par-lay","/paʁ.le/","Je parle français."),
("aimer","to like; to love","eh-may","/e.me/","J'aime la musique."),
("habiter","to live","ah-bee-tay","/a.bi.te/","J'habite en ville."),
("travailler","to work","trah-vah-yay","/tʁa.va.je/","Je travaille le matin."),
("étudier","to study","ay-tü-dee-yay","/e.ty.dje/","Nous étudions le français."),
("manger","to eat","mahn-zhay","/mɑ̃.ʒe/","Je mange à midi."),
("regarder","to watch; look at","ruh-gar-day","/ʁə.ɡaʁ.de/","Je regarde un film."),
("écouter","to listen","ay-koo-tay","/e.ku.te/","Elle écoute la radio."),
("jouer","to play","zhoo-ay","/ʒwe/","Ils jouent au football."),
("lire","to read","leer","/liʁ/","Tu lis un livre."),
("écrire","to write","ay-kreer","/e.kʁiʁ/","J'écris un message."),
("dormir","to sleep","dor-meer","/dɔʁ.miʁ/","Je dors huit heures."),
("se lever","to get up","suh luh-vay","/sə lə.ve/","Je me lève tôt."),
("prendre","to take; have","prahn-dr","/pʁɑ̃dʁ/","Je prends le bus."),
("aller","to go","ah-lay","/a.le/","Nous allons à l'école.")
],
"grammar":[
("What the present tense expresses","The présent describes current actions, habits, general facts and near-future scheduled events: Je travaille maintenant; Je travaille chaque jour; L'eau bout à 100 degrés."),
("Regular -ER verbs","For most -ER verbs, remove -er and add -e, -es, -e, -ons, -ez, -ent: parler → je parle, tu parles, il parle, nous parlons, vous parlez, ils parlent. The -ent ending is silent."),
("Spelling changes in common -ER verbs","Some verbs adjust spelling to preserve pronunciation. Manger has nous mangeons; commencer has nous commençons. At this level, learn these common forms as vocabulary."),
("Useful irregular verbs","Être, avoir and aller are irregular and must be memorised. Aller: je vais, tu vas, il va, nous allons, vous allez, ils vont. Lire, écrire, prendre and dormir also have irregular forms."),
("Negation preview","Place ne before the conjugated verb and pas after it: Je ne travaille pas. In everyday spoken Quebec French, ne is often dropped, but learners should recognise and practise the standard written form."),
("Frequency and time phrases","Use souvent (often), toujours (always), parfois (sometimes), rarement (rarely), jamais (never), chaque jour (every day), le matin (in the morning). Frequency adverbs usually follow the conjugated verb.")
],
"expressions":[("D'habitude…","Usually…","Introduce a routine."),("Tous les jours","Every day","Describe a regular habit."),("De temps en temps","From time to time","Describe occasional activity."),("Je suis occupé(e).","I'm busy.","Describe your current state."),("Je n'ai pas le temps.","I don't have time.","Common everyday expression."),("Ça dépend.","It depends.","Useful natural response.")],
"examples":[("Je travaille du lundi au vendredi.","I work from Monday to Friday.","Present tense describes a routine."),("Nous étudions le français chaque soir.","We study French every evening.","Étudier uses the regular -ER pattern."),("Elle prend le bus à huit heures.","She takes the bus at eight.","Prendre is irregular."),("Ils vont au travail en voiture.","They go to work by car.","Aller is irregular."),("Je ne regarde pas la télévision le matin.","I don't watch television in the morning.","Ne…pas surrounds the verb."),("Parfois, je lis avant de dormir.","Sometimes I read before sleeping.","Parfois is a frequency adverb.")],
"conversations":[("Talking about a routine",[("A","Qu'est-ce que tu fais le matin ?"),("B","Je me lève à sept heures et je prends le petit-déjeuner."),("A","Tu travailles ensuite ?"),("B","Oui, je travaille de neuf heures à cinq heures.")],"A: What do you do in the morning? B: I get up at seven and have breakfast. A: Do you work afterwards? B: Yes, I work from nine to five."),("After work",[("A","Qu'est-ce que tu fais après le travail ?"),("B","Je rentre à la maison et je prépare le dîner."),("A","Tu regardes la télévision ?"),("B","Parfois, mais je préfère lire.")],"A: What do you do after work? B: I go home and prepare dinner. A: Do you watch television? B: Sometimes, but I prefer reading.")],
"speaking":["Describe your weekday in six present-tense sentences.","Conjugate parler for all six subject pronouns.","Say three activities you do souvent, parfois and rarement.","Practise the irregular verbs aller, prendre, lire and écrire in short sentences.","Describe a routine using first, then and finally: d'abord, ensuite, enfin."],
"summary":["Use the present tense for current actions, routines and facts.","Regular -ER verbs use -e, -es, -e, -ons, -ez, -ent.","Memorise common irregular verbs such as être, avoir and aller.","Use frequency adverbs to describe how often you do something.","Standard negation places ne…pas around the conjugated verb."]
},
15:{
"title":"A1 Comprehensive Revision and Assessment","goal":"Bring together the A1 foundations: introductions, numbers, dates, time, articles, être, avoir, descriptions, family, colours, food and everyday routines.",
"vocab":[
("bonjour","hello; good morning","bohn-zhoor","/bɔ̃.ʒuʁ/","Bonjour, je m'appelle Alex."),
("je m'appelle","my name is","zhuh mah-pell","/ʒə ma.pɛl/","Je m'appelle Alex."),
("vingt-cinq","twenty-five","van-sank","/vɛ̃ sɛ̃k/","J'ai vingt-cinq ans."),
("lundi","Monday","luhn-dee","/lœ̃.di/","Je travaille lundi."),
("à midi","at noon","ah mee-dee","/a mi.di/","Je mange à midi."),
("une maison","a house","ün may-zohn","/yn mɛ.zɔ̃/","C'est une maison."),
("je suis","I am","zhuh swee","/ʒə sɥi/","Je suis étudiant."),
("j'ai","I have","zhay","/ʒe/","J'ai une sœur."),
("gentille","kind (feminine)","zhahn-tee-yuh","/ʒɑ̃.tij/","Ma sœur est gentille."),
("la famille","family","lah fah-mee-yuh","/la fa.mij/","Ma famille est grande."),
("bleu","blue","bluh","/blø/","Le sac est bleu."),
("du pain","some bread","dü pan","/dy pɛ̃/","Je mange du pain."),
("je travaille","I work","zhuh trah-vye","/ʒə tʁa.vaj/","Je travaille le matin.")
],
"grammar":[
("Build a complete introduction","Combine phrases from Lessons 2–3: Bonjour, je m'appelle…; J'ai … ans; Je viens de…; J'habite à…; Je parle… Keep the order natural and add Enchanté(e) when meeting someone."),
("Choose the correct present-tense helper","Être: je suis, tu es, il est, nous sommes, vous êtes, ils sont. Avoir: j'ai, tu as, il a, nous avons, vous avez, ils ont. Use être for identity/location and avoir for possession/age and set expressions."),
("Articles and noun gender","Choose un/une/des for indefinite nouns and le/la/l'/les for definite nouns. Gender belongs to the noun; memorise article + noun as a unit."),
("Adjective agreement and position","Make adjectives agree with the noun or person. Most colours follow the noun; common size and beauty adjectives can come before it. Review grand/grande, petit/petite, beau/belle and blanc/blanche."),
("Numbers, dates and time","Review numbers 0–100, hundreds and thousands; use le + date, en + month/season, and Il est… for time. Remember Il est une heure, midi and minuit."),
("Present-tense routines","Use regular -ER endings and common irregular verbs. Add time and frequency expressions: le matin, à midi, souvent, parfois, tous les jours.")
],
"expressions":[("Enchanté(e) !","Nice to meet you!","Introduction."),("J'ai … ans.","I am … years old.","Age."),("Je viens de…","I come from…","Origin."),("Quelle heure est-il ?","What time is it?","Time."),("C'est un / une…","It is a…","Identify an object."),("Je voudrais…","I would like…","Polite ordering."),("À mon avis…","In my opinion…","Simple opinion."),("D'habitude…","Usually…","Routine.")],
"examples":[("Bonjour, je m'appelle Élodie et j'habite à Montréal.","Hello, my name is Élodie and I live in Montreal.","Greeting, name and residence."),("J'ai vingt ans et je parle anglais.","I am twenty and I speak English.","Avoir for age; parler for language."),("Nous sommes en classe à neuf heures.","We are in class at nine o'clock.","Être for location/state; à for clock time."),("Ma sœur est grande et sympathique.","My sister is tall and friendly.","Feminine agreement."),("Les clés sont sur la table.","The keys are on the table.","Plural definite article and être."),("Je voudrais de l'eau et du pain.","I would like some water and bread.","Polite request and partitive articles."),("Le samedi, je lis et je regarde un film.","On Saturdays, I read and watch a film.","Le + weekday for a routine."),("Il est huit heures et demie.","It is half past eight.","Time expression.")],
"conversations":[("A new student",[("A","Bonjour ! Je m'appelle Samira. Et vous ?"),("B","Je m'appelle Julien. Enchanté."),("A","Vous venez d'où ?"),("B","Je viens du Québec, mais j'habite à Ottawa."),("A","Vous parlez anglais ?"),("B","Oui, et j'apprends le français.")],"A: Hello! My name is Samira. And you? B: My name is Julien. Nice to meet you. A: Where are you from? B: I'm from Quebec, but I live in Ottawa. A: Do you speak English? B: Yes, and I'm learning French."),("At a family café",[("A","Bonjour. Une table pour trois, s'il vous plaît."),("B","Bien sûr. Vous désirez quelque chose à boire ?"),("A","Je voudrais de l'eau et un café."),("B","Et pour manger ?"),("A","Du pain et du fromage, merci."),("B","Parfait. Voilà votre commande.")],"A: Hello. A table for three, please. B: Of course. Would you like something to drink? A: I would like water and a coffee. B: And to eat? A: Bread and cheese, thank you. B: Perfect. Here is your order.")],
"speaking":["Give a 30-second self-introduction using name, age, origin, city and languages.","Describe your family and two people using être, avoir and adjectives.","Say today's date and the current time in French.","Describe a typical weekday using at least five present-tense verbs.","Role-play a café order from greeting to asking for the bill."],
"summary":["You can greet people and introduce yourself politely.","You can give personal details, count, say dates and tell the time.","You can choose articles and use être and avoir in the present.","You can describe people, family members, colours and objects.","You can order basic food and describe everyday routines."]
}
}

def _make_questions(vocabulary, count=20):
    questions = []
    meanings = [entry[1] for entry in vocabulary]
    for index, entry in enumerate(vocabulary):
        word, meaning = entry[0], entry[1]
        distractors = [meanings[(index + step) % len(meanings)] for step in range(1, min(4, len(meanings)))]
        options = [meaning] + distractors[:3]
        correct_position = index % len(options)
        options = options[correct_position:] + options[:correct_position]
        questions.append((f"What does “{word}” mean?", options, 0, f"{word} means {meaning}."))
    # Add reverse recognition items so the assessment tests both directions.
    for index, entry in enumerate(vocabulary):
        word, meaning = entry[0], entry[1]
        distractors = [vocabulary[(index + step) % len(vocabulary)][0] for step in range(1, 4)]
        options = [word] + distractors
        correct_position = (index + 1) % len(options)
        options = options[correct_position:] + options[:correct_position]
        questions.append((f"Which French expression means “{meaning}”?", options, 0, f"The correct French expression is {word}."))
    return questions[:count]

def build_lesson(lesson_id):
    source = LESSON_DATA[lesson_id]
    vocab = source["vocab"]
    exercises = _make_questions(vocab, 12)
    assessment = _make_questions(vocab, 20)
    return {
        "id": lesson_id,
        "title": source["title"],
        "goal": source["goal"],
        "vocabulary": vocab,
        "grammar": source["grammar"],
        "expressions": source["expressions"],
        "examples": source["examples"],
        "conversations": source["conversations"],
        "exercises": exercises,
        "speaking": source["speaking"],
        "summary": source["summary"],
        "assessment": assessment,
    }

A1_LESSONS = {lesson_id: build_lesson(lesson_id) for lesson_id in LESSON_DATA}
