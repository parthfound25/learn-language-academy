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
("le pays","country","luh pay-ee","/lə pɛ.i/","Tu viens de quel pays ?"),
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
("lundi","Monday","luhn-dzee (approx.)","[lœ̃.d͡zi]","Je travaille lundi."),
("mardi","Tuesday","mahr-dzee (approx.)","[maʁ.d͡zi]","À mardi !"),
("mercredi","Wednesday","mehr-kruh-dzee (approx.)","[mɛʁ.kʁə.d͡zi]","Le cours est mercredi."),
("jeudi","Thursday","zhuh-dzee (approx.)","[ʒø.d͡zi]","Jeudi, je suis libre."),
("vendredi","Friday","vahn-druh-dzee (approx.)","[vɑ̃.dʁə.d͡zi]","C'est vendredi."),
("samedi","Saturday","sahm-dzee (approx.)","[sam.d͡zi]","Samedi, je me repose."),
("dimanche","Sunday","dee-mahnsh","[di.mɑ̃ʃ]","Dimanche est calme."),
("janvier","January","zhahn-vyay","[ʒɑ̃.vje]","En janvier, il fait froid."),
("février","February","feh-vree-yay","[fe.vʁi.je]","Mon anniversaire est en février."),
("mars","March","mahrs","[maʁs]","Le printemps commence en mars."),
("avril","April","ah-vreel","[a.vʁil]","En avril, il pleut souvent."),
("mai","May","meh","[mɛ]","Le mois de mai."),
("juin","June","zhweh(n) (approx.)","[ʒɥɛ̃]","En juin, les jours sont longs."),
("juillet","July","zhwee-yèh","[ʒɥi.jɛ]","Juillet est un mois d'été."),
("août","August","oot","[ut]","En août, je voyage.")
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
("grand / grande","tall; big","grahn / grahnd","masc. /ɡʁɑ̃/; fém. /ɡʁɑ̃d/","Il est grand."),
("petit / petite","short; small","puh-tee / puh-teet","masc. /pə.ti/; fém. /pə.tit/","La petite maison."),
("jeune","young","zhuhn","/ʒœn/","Elle est jeune."),
("vieux / vieille","old","vyuh / vyay","masc. /vjø/; fém. /vjɛj/","Un vieil ami."),
("beau / belle","beautiful; handsome","boh / bell","masc. /bo/; fém. /bɛl/","C'est une belle ville."),
("joli / jolie","pretty","zho-lee","/ʒɔ.li/","Une jolie robe."),
("gentil / gentille","kind","zhahn-tee / zhahn-teey","masc. /ʒɑ̃.ti/; fém. /ʒɑ̃.tij/","Il est gentil."),
("sympathique","nice; friendly","san-pah-teek","/sɛ̃.pa.tik/","Elle est sympathique."),
("intelligent / intelligente","intelligent","an-tell-ee-zhahn / ahnt","masc. /ɛ̃.te.li.ʒɑ̃/; fém. /ɛ̃.te.li.ʒɑ̃t/","Un étudiant intelligent."),
("drôle","funny","drohl","/dʁol/","Mon ami est drôle."),
("sérieux / sérieuse","serious","say-ree-uh / say-ree-uhz","masc. /se.ʁjø/; fém. /se.ʁjøz/","Elle est sérieuse."),
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
("vert / verte","green","vair / vair-tuh","masc. /vɛʁ/; fém. /vɛʁt/","Une porte verte."),
("jaune","yellow","zhohn","/ʒon/","Un livre jaune."),
("noir / noire","black","nwahr / nwahr","/nwaʁ/","Une voiture noire."),
("blanc / blanche","white","blahn / blahnsh","masc. /blɑ̃/; fém. /blɑ̃ʃ/","Une chemise blanche."),
("gris / grise","grey","gree / greez","masc. /ɡʁi/; fém. /ɡʁiz/","Un mur gris."),
("orange","orange","oh-rahnzh","/ɔ.ʁɑ̃ʒ/","Des fleurs orange."),
("rose","pink","rohz","/ʁoz/","Une robe rose."),
("violet / violette","purple","vee-oh-lay / vee-oh-let","masc. /vjɔ.lɛ/; fém. /vjɔ.lɛt/","Une boîte violette."),
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
    """Create a balanced set of meaning-to-French and French-to-meaning questions."""
    forward = []
    reverse = []
    meanings = [entry[1] for entry in vocabulary]
    words = [entry[0] for entry in vocabulary]
    for index, (word, meaning, *_rest) in enumerate(vocabulary):
        distractors = []
        for step in range(1, len(vocabulary)):
            candidate = meanings[(index + step) % len(vocabulary)]
            if candidate != meaning and candidate not in distractors:
                distractors.append(candidate)
            if len(distractors) == 3:
                break
        options = [meaning] + distractors
        correct_position = index % len(options)
        options = options[correct_position:] + options[:correct_position]
        forward.append((f"What does “{word}” mean?", options, (len(options) - correct_position) % len(options), f"{word} means {meaning}."))
    for index, (word, meaning, *_rest) in enumerate(vocabulary):
        distractors = []
        for step in range(1, len(vocabulary)):
            candidate = words[(index + step) % len(vocabulary)]
            if candidate != word and candidate not in distractors:
                distractors.append(candidate)
            if len(distractors) == 3:
                break
        options = [word] + distractors
        correct_position = (index + 1) % len(options)
        options = options[correct_position:] + options[:correct_position]
        reverse.append((f"Which French expression means “{meaning}”?", options, (len(options) - correct_position) % len(options), f"The correct French expression is {word}."))
    questions = []
    seen_prompts = set()
    for index in range(max(len(forward), len(reverse))):
        for bank, position in ((forward, index), (reverse, index)):
            if position < len(bank):
                question = bank[position]
                if question[0] not in seen_prompts:
                    questions.append(question)
                    seen_prompts.add(question[0])
    return questions[:count]


# Expanded teaching material: added after the first content review so each chapter
# includes the explanation, contrast, examples and guided practice expected of a textbook.
LESSON_EXPANSIONS = {
2: {
"vocabulary":[
("bonne nuit","good night (when going to sleep)","bun nwee","/bɔn nɥi/","Bonne nuit, tout le monde !"),
("bienvenue","welcome","byan-vuh-nü","/bjɛ̃.və.ny/","Bienvenue au Québec."),
("excusez-moi","excuse me (formal)","ex-kü-zay mwah","/ɛks.ky.ze mwa/","Excusez-moi, où est la gare ?"),
("pardon","sorry; pardon","par-dohn","/paʁ.dɔ̃/","Pardon, je n'ai pas compris."),
("ça va","how's it going; it's okay","sah vah","/sa va/","Salut ! Ça va ?"),
("très bien","very well","treh byan","/tʁɛ bjɛ̃/","Je vais très bien, merci."),
("comme ci, comme ça","so-so","kom see kom sah","/kɔm si kɔm sa/","Aujourd'hui, ça va comme ci, comme ça."),
("à plus tard","see you later","ah plü tar","/a ply taʁ/","À plus tard, les amis !")
],
"grammar":[
("The difference between bonjour, bonsoir and bonne nuit","Bonjour is the everyday daytime greeting and bonsoir is used when greeting someone in the evening. Bonne nuit is not normally a greeting when you arrive; it is a farewell said when someone is going to bed. To wish someone a pleasant evening while leaving, say bonne soirée. This distinction prevents a common beginner mistake."),
("Building a polite exchange","A natural short exchange often follows this order: greeting, question about wellbeing, answer, return question, and farewell. For example: Bonjour. Comment allez-vous ? Très bien, merci. Et vous ? Très bien. Bonne journée ! Practise the whole sequence rather than memorising isolated questions."),
("Tu and vous: agreement across the sentence","Tu is singular and informal; vous is used for politeness or for more than one person. The choice changes the verb: tu vas / vous allez, tu es / vous êtes, tu as / vous avez. Do not combine tu with a vous verb. In Quebec, as elsewhere in French-speaking communities, the social situation and relationship guide the choice."),
("Question patterns for greetings","Comment ça va ? and Ça va ? are common spoken questions. Comment allez-vous ? is more formal. A statement can become a yes/no question through rising intonation, while est-ce que creates an explicit question: Est-ce que vous allez bien ? In conversation, short forms are frequent; in careful writing, use complete punctuation and accents.")
],
"expressions":[
("Bonne soirée !","Have a good evening!","A farewell, not usually an arrival greeting."),
("Bonne nuit !","Good night!","Use when someone is going to sleep."),
("Je vais bien, merci.","I'm well, thank you.","A complete answer to a wellbeing question."),
("Pas mal, merci.","Not bad, thanks.","Relaxed, everyday response."),
("Ravi(e) de vous rencontrer.","Pleased to meet you.","A slightly more formal introduction.")
],
"examples":[
("Bonsoir, madame. Comment allez-vous ce soir ?","Good evening, ma'am. How are you this evening?","Bonsoir sets the evening context; vous is polite."),
("Ça va bien, merci. Et toi ?","I'm doing well, thanks. And you?","Toi is the stressed form used after et."),
("Je vais très bien aujourd'hui.","I'm doing very well today.","Très strengthens the adjective bien."),
("Bonne soirée et à demain !","Have a good evening and see you tomorrow!","Two natural farewell expressions."),
("Pardon, monsieur. Vous êtes dans la bonne file ?","Excuse me, sir. Are you in the correct line?","Excusez-moi and pardon can politely get attention.")
],
"conversations":[
("At a neighbour's door",[("A","Bonsoir ! Vous êtes la nouvelle voisine ?"),("B","Oui, bonsoir. Je m'appelle Nadia."),("A","Enchanté. Moi, c'est Luc. Bienvenue dans l'immeuble !"),("B","Merci beaucoup. Bonne soirée !"),("A","À bientôt !")],"A: Good evening! Are you the new neighbour? B: Yes, good evening. My name is Nadia. A: Nice to meet you. I'm Luc. Welcome to the building! B: Thank you very much. Have a good evening! A: See you soon!"),
("A quick phone call",[("A","Allô, bonjour !"),("B","Bonjour, est-ce que Léa est là ?"),("A","Oui, un instant, s'il vous plaît."),("B","Merci."),("A","Léa, c'est pour toi !")],"A: Hello! B: Hello, is Léa there? A: Yes, one moment, please. B: Thank you. A: Léa, it's for you!")
],
"exercises":[("Which subject pronoun completes the formal question 'Comment ___ appelez-vous ?'?", ["vous", "tu", "nous", "ils"], 0, "Use vous in this formal question: Comment vous appelez-vous ?"),("Which farewell means 'Have a good evening'?", ["Bonne nuit", "Bonne soirée", "Bonjour", "À demain"], 1, "Bonne soirée wishes someone a pleasant evening; bonne nuit is for bedtime."),("Complete the informal sentence: Comment ___ t'appelles ?", ["vous", "tu", "te", "toi"], 1, "The subject pronoun tu comes before t'appelles in this familiar spoken question."),("Choose the natural phone greeting.", ["Bonjour", "Allô", "Bonne nuit", "Enchanté"], 1, "Allô is the conventional greeting when answering the telephone.")],
"speaking":[
"Say a daytime greeting, an evening greeting and a bedtime farewell; explain when each is appropriate.",
"Perform the same introduction twice, first with vous and then with tu, changing every matching verb.",
"Practise a six-line greeting exchange without looking at the English translation.",
"Record no audio: simply read bonjour, bonsoir, bonne soirée and bonne nuit aloud and notice the different final sounds."
],
"summary":[
"Bonjour and bonsoir greet people; bonne soirée and bonne nuit are farewells with different contexts.",
"Use vous for politeness or plural people and tu for one familiar person.",
"Match the verb to the pronoun: tu vas / vous allez.",
"A complete greeting exchange includes a greeting, a wellbeing question, a response and a farewell."
]
},
3: {
"vocabulary":[
("le prénom","first name","luh pray-nohn","/lə pʁe.nɔ̃/","Mon prénom est Alex."),
("le nom de famille","surname; family name","luh nohn duh fah-mee-yuh","/lə nɔ̃ də fa.mij/","Quel est votre nom de famille ?"),
("l'adresse","address (f.)","lah-dress","/la.dʁɛs/","Quelle est ton adresse ?"),
("le courriel","email address/email (Canadian usage)","luh koo-ree-yell","/lə ku.ʁjɛl/","Mon courriel est simple."),
("le téléphone portable","mobile phone","luh tay-lay-fohn por-tahbl","/lə te.le.fɔn pɔʁ.tabl/","Voici mon téléphone portable."),
("la nationalité","nationality","lah nah-syo-nah-lee-tay","/la na.sjɔ.na.li.te/","Quelle est votre nationalité ?"),
("célibataire","single","say-lee-bah-tair","/se.li.ba.tɛʁ/","Je suis célibataire."),
("marié / mariée","married","mah-ryay","/ma.ʁje/","Elle est mariée."),
("apprendre","to learn","ah-prahn-druh","/a.pʁɑ̃dʁ/","J'apprends le français."),
("parler","to speak","par-lay","/paʁ.le/","Nous parlons anglais.")
],
"grammar":[
("Je m'appelle and the reflexive pronoun","The infinitive is s'appeler, literally to call oneself. The small reflexive word changes with the subject: je m'appelle, tu t'appelles, il/elle s'appelle, nous nous appelons, vous vous appelez, ils/elles s'appellent. The apostrophe in m'appelle and t'appelles appears because me and te lose their vowel before a vowel sound."),
("Asking for a name politely","Use Comment vous appelez-vous ? in a formal setting and Comment tu t'appelles ? in a familiar setting. The inverted form repeats the subject pronoun after the verb. A simpler spoken question is Vous vous appelez comment ? or Tu t'appelles comment ? Keep the pronoun and verb agreement consistent."),
("Age, origin and residence are built differently","French uses avoir for age: J'ai vingt ans. Use venir de for origin: Je viens d'Angola; use habiter à for a city: J'habite à Luanda. The preposition before a country changes with grammatical gender and number: au Canada, en Angola, aux États-Unis, and de/d'/du/des for origin. Learn the country together with its preposition."),
("Saying which languages you speak","Use parler + language: Je parle anglais; Je parle français. Language names are normally lowercase in French. To say you are learning a language, use apprendre: J'apprends le français. Do not use être to translate the English phrase 'I am 20' or 'I am from…' word for word."),
("Nationality adjectives and agreement","Nationality adjectives usually begin with a lowercase letter: canadien, angolaise, français. They agree with the person described: Il est canadien; Elle est canadienne. When naming a person as a noun, the form may be capitalised: un Canadien, une Canadienne. Distinguish the adjective from the people noun.")
],
"expressions":[
("Je suis originaire de…","I am originally from…","A natural way to give your background."),
("J'habite à…","I live in…","Use à before a city."),
("Je parle un peu français.","I speak a little French.","Useful when describing your level."),
("Je suis débutant(e).","I am a beginner.","The ending agrees with the speaker."),
("Comment ça s'écrit ?","How is that spelled?","Ask someone to spell a name or place.")
],
"examples":[
("Je m'appelle Daniel, mais mon prénom usuel est Dan.","My name is Daniel, but the name I usually go by is Dan.","Prénom refers to a first name."),
("Mon nom de famille est Oliveira.","My family name is Oliveira.","Nom de famille is the surname."),
("Je viens d'Angola et j'habite à Luanda.","I come from Angola and live in Luanda.","D' is used before a vowel-starting country name."),
("Elle parle portugais et elle apprend le français.","She speaks Portuguese and is learning French.","Language names are lowercase."),
("Nous sommes étudiants et nous habitons à Québec.","We are students and we live in Quebec City.","Étudiants agrees with a masculine or mixed group."),
("Comment vous appelez-vous ? — Je m'appelle Amina.","What is your name? — My name is Amina.","Formal question and reflexive answer.")
],
"conversations":[
("Meeting a classmate",[("A","Bonjour ! Comment tu t'appelles ?"),("B","Je m'appelle Inès. Et toi ?"),("A","Moi, c'est Karim. Tu viens d'où ?"),("B","Je viens d'Angola. J'habite à Luanda."),("A","Tu parles français ?"),("B","Un peu. J'apprends le français à l'école.")],"A: Hi! What's your name? B: My name is Inès. And you? A: I'm Karim. Where are you from? B: I'm from Angola. I live in Luanda. A: Do you speak French? B: A little. I'm learning French at school."),
("Completing a registration form",[("A","Quel est votre prénom ?"),("B","Mireille."),("A","Et votre nom de famille ?"),("B","Bouchard. B-O-U-C-H-A-R-D."),("A","Quelle est votre adresse ?"),("B","J'habite au 18, rue des Érables.")],"A: What is your first name? B: Mireille. A: And your family name? B: Bouchard, spelled B-O-U-C-H-A-R-D. A: What is your address? B: I live at 18 Maple Street.")
],
"exercises":[("Complete: Je ___ vingt ans.", ["suis", "es", "ai", "as"], 2, "Age uses avoir: j'ai vingt ans."),("Choose the correct origin phrase: I come from Angola.", ["Je viens en Angola", "Je viens d'Angola", "Je suis Angola", "J'habite d'Angola"], 1, "Use venir de; d' appears before the vowel in Angola."),("Complete: Elle ___ à Luanda.", ["habite", "habites", "habitons", "habitez"], 0, "Elle takes the third-person singular form habite."),("Choose the correct feminine nationality adjective.", ["canadien", "canadienne", "canadiens", "canadiennes"], 1, "A feminine singular person is canadienne.")],
"speaking":[
"Give a 30-second introduction with your first name, surname, age, origin, city and languages.",
"Spell your first and family names using French letter names.",
"Ask a partner the same five personal questions using tu, then repeat politely with vous.",
"Practise saying country names with the correct preposition: en, au, aux or à."
],
"summary":[
"Use s'appeler with matching reflexive pronouns to give and ask for names.",
"French expresses age with avoir, origin with venir de and residence with habiter à.",
"Country prepositions depend on the country's grammatical form.",
"Language names are lowercase; nationality adjectives agree in gender and number."
]
},
4: {
"vocabulary":[
("zéro","zero","zay-roh","/ze.ʁo/","Il y a zéro erreur."),
("onze","eleven","ohnz","/ɔ̃z/","J'ai onze livres."),
("douze","twelve","dooz","/duz/","Elle a douze ans."),
("treize","thirteen","trez","/tʁɛz/","Le bus arrive à treize heures."),
("quatorze","fourteen","kah-torz","/ka.tɔʁz/","Quatorze élèves sont présents."),
("quinze","fifteen","kanz","/kɛ̃z/","Il coûte quinze dollars."),
("seize","sixteen","sez","/sɛz/","J'ai seize crayons."),
("dix-sept","seventeen","dee-set","/dis sɛt/","Elle a dix-sept ans."),
("dix-huit","eighteen","deez-weet","/di.zɥit/","Le cours commence à dix-huit heures."),
("dix-neuf","nineteen","deez-nuhf","/diz nœf/","Il y a dix-neuf personnes."),
("vingt et un","twenty-one","van-tay-uhn","/vɛ̃.te.œ̃/","J'ai vingt et un ans."),
("trente","thirty","trahnt","/tʁɑ̃t/","Le billet coûte trente dollars."),
("quarante","forty","kah-rahnt","/ka.ʁɑ̃t/","La classe compte quarante élèves."),
("cinquante","fifty","sank-ahnt","/sɛ̃.kɑ̃t/","Il a cinquante ans."),
("soixante","sixty","swah-sahnt","/swa.sɑ̃t/","Le trajet dure soixante minutes."),
("soixante-dix","seventy","swah-sahnt-dees","/swa.sɑ̃t.dis/","Il y a soixante-dix pages."),
("quatre-vingts","eighty","kah-truh-van","/ka.tʁə.vɛ̃/","Il y a quatre-vingts personnes dans la salle."),
("quatre-vingt-dix","ninety","kah-truh-van-dees","/ka.tʁə.vɛ̃.dis/","Le livre a quatre-vingt-dix pages."),
("cent","one hundred","sahn","/sɑ̃/","Le billet coûte cent dollars."),
("mille","one thousand","meel","/mil/","La ville compte mille habitants.")
],
"grammar":[
("Numbers 0–16 must be learned individually","French number words from zéro through seize do not follow one fully predictable pattern, so learn them as a sequence. Practise them forward, backward and in random order. Pay attention to the nasal vowels in onze, onze-like forms and quinze; the final consonants are not always pronounced the way an English speaker expects."),
("Building numbers from 17 to 69","From 17 to 19, combine dix with the unit: dix-sept, dix-huit, dix-neuf. The tens are vingt, trente, quarante, cinquante and soixante. Most numbers combine tens and units with a hyphen: vingt-deux, trente-cinq, cinquante-neuf. With 21, 31, 41, 51 and 61, use et un: vingt et un."),
("The traditional French counting pattern from 70 to 99","In standard French used in Quebec, 70 is soixante-dix (60+10), 71 is soixante et onze, 72 is soixante-douze, and 80 is quatre-vingts (four twenties). 90 is quatre-vingt-dix. In Quebec and France, soixante-dix and quatre-vingt-dix are the standard forms to learn. You may encounter septante and nonante in Belgium and Switzerland."),
("When vingt and cent take an s","Quatre-vingts takes an s when it means exactly eighty and nothing follows it: quatre-vingts. It loses the s when another number follows: quatre-vingt-deux. Cent takes an s when multiplied and not followed by another number: trois cents, but trois cent cinq. Mille is invariable in number names: deux mille."),
("Using numbers in age, prices, dates and time","Use avoir + number + ans for age. Use euros or dollars after a price, and use à before a clock time. Dates use cardinal numbers except for the first day of the month: le premier mai, le deux mai. In Quebec, prices are commonly expressed in dollars and cents; practise hearing numbers in realistic price contexts.")
],
"expressions":[
("Combien ?","How many? / How much?","A short question when context is clear."),
("Combien ça coûte ?","How much does it cost?","Shopping and price questions."),
("Quel âge as-tu ?","How old are you?","Informal age question."),
("J'ai vingt ans.","I am twenty years old.","Age uses avoir."),
("Il y a…","There is / there are…","Introduce a quantity."),
("C'est le numéro…","It is number…","Give a number or room reference.")
],
"examples":[
("J'ai dix-huit ans et mon frère a vingt et un ans.","I am eighteen and my brother is twenty-one.","Age uses avoir; 21 has et un."),
("Le livre coûte soixante-douze dollars.","The book costs seventy-two dollars.","72 is 60 + 12."),
("Nous avons quatre-vingts questions.","We have eighty questions.","Vingt takes s at exactly 80."),
("Il y a quatre-vingt-deux élèves dans les deux classes.","There are eighty-two students in the two classes.","Vingt loses s before a following number."),
("Le rendez-vous est le premier juin à neuf heures.","The appointment is on June first at nine o'clock.","Use premier for the first day."),
("Mille personnes visitent le musée chaque année.","One thousand people visit the museum each year.","Mille is not pluralised.")
],
"conversations":[
("Buying a notebook",[("A","Bonjour. Combien coûte ce cahier ?"),("B","Il coûte douze dollars."),("A","Et les trois stylos ?"),("B","Les stylos coûtent cinq dollars chacun."),("A","Alors, ça fait vingt-sept dollars ?"),("B","Exactement.")],"A: Hello. How much is this notebook? B: It costs twelve dollars. A: And the three pens? B: The pens cost five dollars each. A: So that's twenty-seven dollars? B: Exactly."),
("Asking about a class",[("A","À quelle heure commence le cours ?"),("B","À dix-huit heures trente."),("A","Combien d'étudiants sont dans la classe ?"),("B","Vingt-deux étudiants."),("A","Merci !"),("B","De rien.")],"A: What time does the class start? B: At 6:30 p.m. A: How many students are in the class? B: Twenty-two students. A: Thank you! B: You're welcome.")
],
"exercises":[("How do you say 21?", ["vingt-un", "vingt et un", "vingt-et-une", "deux-un"], 1, "The standard form includes et: vingt et un."),("Choose the correct spelling for exactly 80.", ["quatre-vingt", "quatre-vingts", "quatre-vingt-dix", "huitante"], 1, "Quatre-vingts takes s when it stands for exactly eighty."),("How is 72 formed in standard French?", ["soixante-douze", "septante-deux", "quatre-vingt-deux", "soixante et deux"], 0, "Seventy-two is sixty plus twelve: soixante-douze."),("Complete the age sentence: Elle a ___ ans.", ["vingt et un", "vingt et une", "vingt-un", "vingt-et-une"], 0, "Ans is masculine, and 21 is vingt et un.")],
"speaking":[
"Count from zéro to vingt, then count backward from vingt to zéro.",
"Say the tens from vingt to soixante and create five random two-digit numbers.",
"Practise 70, 71, 80, 81, 90 and 95 slowly; explain how each is constructed.",
"Say your age, a friend's age, three prices and a meeting time in French.",
"Read a shopping receipt aloud, grouping each amount into tens and units."
],
"summary":[
"Memorise 0–16 and build 17–69 with tens and units.",
"Remember the traditional French patterns: 70 = 60+10, 80 = 4×20 and 90 = 80+10.",
"Quatre-vingts and cents take s only in specific exact-multiple contexts.",
"Use numbers with avoir for age, with prices, with dates and after à for time."
]
},
5: {
"vocabulary":[
("septembre","September","sep-tahmbr","[sɛp.tɑ̃bʁ]","La rentrée est en septembre."),
("octobre","October","ok-tohbr","[ɔk.tɔbʁ]","Les feuilles changent en octobre."),
("novembre","November","noh-vahmbr","[nɔ.vɑ̃bʁ]","Il fait froid en novembre."),
("décembre","December","day-sahmbr","[de.sɑ̃bʁ]","Décembre est le dernier mois."),
("la date","date (f.)","lah dat","[la dat]","Quelle est la date aujourd'hui ?")
],
"grammar":[
("Quebec French pronunciation: affrication of t and d","In much of Quebec French, /t/ and /d/ can be pronounced [t͡s] and [d͡z] before the high vowels /i/ and /y/ and the glide /ɥ/. That is why the final syllable of lundi, mardi, mercredi, jeudi, vendredi and samedi can sound like 'dzee'. This is a common regional feature, not a different spelling. The IPA in square brackets here shows a common Quebec-style pronunciation; pronunciation varies by speaker and region."),
("Days and months are not capitalised","French weekdays and months normally begin with lowercase letters: lundi, janvier, décembre. Capitalise them only when they begin a sentence or appear in a title. This differs from English and is a frequent writing error."),
("Using le with a weekday","Use a weekday without an article for one particular upcoming or understood day: Je pars lundi (I'm leaving Monday). Use le + weekday for a repeated routine: Je travaille le lundi (I work on Mondays). The plural les lundis can also describe recurring Mondays."),
("Dates use le and cardinal numbers","Ask Quelle est la date aujourd'hui ? Answer Nous sommes le vingt-sept novembre or On est le vingt-sept novembre. The first day of a month is special: le premier mai. Other dates use cardinal numbers: le deux mai, le quinze juin."),
("Months and seasons use en","Use en + month: en janvier, en juillet. Use en + season for spring, summer and autumn: au printemps is the important exception; en été, en automne. Winter is en hiver. In Quebec, seasonal vocabulary is especially useful because winter weather is a major part of everyday conversation."),
("Asking and answering about birthdays","Use Quand est ton anniversaire ? for an informal question and Quand est votre anniversaire ? politely. Answer Mon anniversaire est le trois août. To say the year, add the year after the date: le trois août deux mille vingt-six. Do not add an English-style ordinal ending to every date.")
],
"expressions":[
("Quel jour sommes-nous ?","What day is it?","Ask for the weekday."),
("Quelle est la date aujourd'hui ?","What's today's date?","Ask for the full date."),
("On est lundi.","It's Monday.","Common spoken way to state the day."),
("en hiver","in winter","Season phrase; en is used here."),
("au printemps","in spring","Remember the special preposition au."),
("la semaine prochaine","next week","Useful time expression.")
],
"examples":[
("Nous sommes le vingt-sept novembre.","Today is November twenty-seventh.","French uses day before month."),
("Mon anniversaire est le premier juillet.","My birthday is July first.","Premier is used for the first day."),
("Je fais du sport le samedi.","I play sports on Saturdays.","Le samedi expresses a routine."),
("Je vais à Montréal mardi prochain.","I'm going to Montreal next Tuesday.","No article before a specific weekday."),
("Au printemps, les journées deviennent plus longues.","In spring, the days become longer.","Au printemps is the exception to en + season."),
("En janvier, il fait souvent très froid au Québec.","In January, it is often very cold in Quebec.","A natural Canadian French seasonal sentence.")
],
"conversations":[
("Planning a meeting",[("A","Quel jour sommes-nous ?"),("B","Nous sommes jeudi."),("A","Tu es libre samedi ?"),("B","Oui, samedi après-midi."),("A","Parfait. On se voit le vingt-neuf ?"),("B","D'accord !")],"A: What day is it? B: It's Thursday. A: Are you free Saturday? B: Yes, Saturday afternoon. A: Perfect. Shall we meet on the twenty-ninth? B: Okay!"),
("Talking about birthdays",[("A","Quand est ton anniversaire ?"),("B","Le premier octobre. Et toi ?"),("A","Le douze février."),("B","Tu aimes l'hiver ?"),("A","Oui, mais je préfère l'été !")],"A: When is your birthday? B: October first. And yours? A: February twelfth. B: Do you like winter? A: Yes, but I prefer summer!")
],
"exercises":[("Choose the correct French date phrase for May 1st.", ["le un mai", "le premier mai", "en premier mai", "la première mai"], 1, "Use le premier for the first day of a month."),("Which phrase means 'I work on Mondays' as a routine?", ["Je travaille lundi", "Je travaille le lundi", "Je travaille à lundi", "Je travaille en lundi"], 1, "Le + weekday expresses a repeated routine."),("Complete: ___ printemps, il fait plus doux.", ["En", "Au", "À", "Le"], 1, "The standard expression is au printemps."),("Which words are normally lowercase in French?", ["Months and weekdays", "Only months", "Only weekdays", "Neither"], 0, "French months and weekdays normally begin with lowercase letters.")],
"speaking":[
"Say all seven weekdays in order, then say them backward.",
"Say all twelve months in order and group them into four seasons.",
"State today's date using a full French sentence.",
"Describe one weekly routine using le + weekday.",
"Describe your favourite season and give two reasons."
],
"summary":[
"Weekdays and months are lowercase in French.",
"Use a bare weekday for a specific day and le + weekday for a repeated routine.",
"Dates use le + day + month; use premier for the first day.",
"Use en with most months and seasons, but say au printemps."
]
},
6: {
"vocabulary":[
("l'heure","time; hour (f.)","luhr","/lœʁ/","Quelle heure est-il ?"),
("la minute","minute (f.)","lah mee-nüt","/la mi.nyt/","Attends cinq minutes."),
("la seconde","second (f.)","lah suh-gohnd","/la sə.ɡɔ̃d/","Une seconde, s'il vous plaît."),
("midi","noon","mee-dee","/mi.di/","Il est midi."),
("minuit","midnight","mee-nwee","/mi.nɥi/","Il est minuit."),
("et quart","quarter past","ay kar","/e kaʁ/","Il est deux heures et quart."),
("et demie","half past","ay duh-mee","/e də.mi/","Il est trois heures et demie."),
("moins le quart","quarter to","mwan luh kar","/mwɛ̃ lə kaʁ/","Il est cinq heures moins le quart."),
("le matin","morning","luh mah-tan","/lə ma.tɛ̃/","Je travaille le matin."),
("l'après-midi","afternoon","lah-preh-mee-dee","/la.pʁɛ.mi.di/","Je lis l'après-midi."),
("le soir","evening","luh swahr","/lə swaʁ/","Nous sortons le soir."),
("la nuit","night","lah nwee","/la nɥi/","Je dors la nuit."),
("aujourd'hui","today","oh-zhoor-dwee","/o.ʒuʁ.dɥi/","Aujourd'hui, je suis occupé."),
("demain","tomorrow","duh-man","/də.mɛ̃/","À demain matin."),
("hier","yesterday","ee-air","/jɛʁ/","Hier, j'étais à la maison."),
("tôt","early","toh","/to/","Je me lève tôt."),
("tard","late","tar","/taʁ/","Le film finit tard."),
("souvent","often","soo-vahn","/su.vɑ̃/","Je lis souvent."),
("parfois","sometimes","par-fwah","/paʁ.fwa/","Je cuisine parfois."),
("d'habitude","usually","dah-bee-tüd","/da.bi.tyd/","D'habitude, je prends le bus.")
],
"grammar":[
("Asking and telling the time","Ask Quelle heure est-il ? The standard answer begins Il est… Use Il est une heure for one o'clock, but Il est deux heures, trois heures and so on for other hours. French uses the 24-hour clock frequently in timetables and official contexts, while everyday speech also uses context to clarify morning or evening."),
("Minutes after and before the hour","For common spoken times, add minutes after the hour: Il est trois heures dix (3:10). You can say et quart for :15 and et demie for :30. For :45, use moins le quart with the next hour: Il est quatre heures moins le quart (3:45). In digital schedules, the number can simply be read as hours and minutes."),
("Midi, minuit and the article","Midi and minuit are used without heures: Il est midi; Il est minuit. For noon and midnight exactly, these are the natural expressions. To say 12:30, say Il est midi et demi; to say 00:30, say Il est minuit et demi."),
("À + clock time, le matin and du soir","Use à before a specific time: Le cours commence à neuf heures. Add du matin, de l'après-midi or du soir when context needs clarification. For example, vingt heures is 8 p.m. in the 24-hour system. Do not translate 'at 8' without the preposition à."),
("Frequency and time expressions in a sentence","Expressions such as toujours, souvent, parfois, rarement and jamais usually appear after a conjugated verb in a simple present sentence: Je travaille souvent le soir. Time phrases can appear at the beginning or end: Le matin, je bois du café; Je bois du café le matin. Put the time phrase where it makes the sentence easiest to understand.")
],
"expressions":[
("À quelle heure… ?","At what time…?","Ask when an event happens."),
("Il est quelle heure ?","What time is it?","Common spoken alternative."),
("à huit heures pile","at exactly eight o'clock","Pile emphasises exact time."),
("dans cinq minutes","in five minutes","A future time interval."),
("tout de suite","right away","Immediate timing."),
("de temps en temps","from time to time","Frequency expression.")
],
"examples":[
("Il est une heure et demie.","It is half past one.","Une heure is singular; et demie agrees with heure."),
("Le train part à dix-huit heures quarante-cinq.","The train leaves at 6:45 p.m.","24-hour time is common in schedules."),
("Je prends mon petit-déjeuner à sept heures du matin.","I eat breakfast at seven in the morning.","À marks the clock time."),
("D'habitude, nous étudions le soir.","Usually, we study in the evening.","D'habitude introduces a routine."),
("Le samedi, je me lève tard, mais en semaine je me lève tôt.","On Saturdays I get up late, but on weekdays I get up early.","Tôt and tard contrast."),
("Il est midi et quart; le rendez-vous commence dans quinze minutes.","It is 12:15; the appointment starts in fifteen minutes.","Dans + duration means from now.")
],
"conversations":[
("Arranging a call",[("A","À quelle heure est-ce qu'on s'appelle ?"),("B","Vers sept heures du soir."),("A","Sept heures pile ?"),("B","Oui, ou sept heures et quart au plus tard."),("A","Parfait. À tout à l'heure !")],"A: What time shall we call each other? B: Around seven in the evening. A: Exactly seven? B: Yes, or 7:15 at the latest. A: Perfect. Talk to you later!"),
("Describing a weekday",[("A","À quelle heure tu te lèves ?"),("B","Je me lève à six heures et demie."),("A","Et tu commences le travail à quelle heure ?"),("B","À huit heures. Je finis à seize heures."),("A","Tu te couches tôt ?"),("B","Oui, vers vingt-deux heures.")],"A: What time do you get up? B: I get up at 6:30. A: And what time do you start work? B: At eight. I finish at four p.m. A: Do you go to bed early? B: Yes, around ten p.m.")
],
"exercises":[("Choose the correct answer to Quelle heure est-il ? at 1:00.", ["Il est un heure", "Il est une heure", "C'est une heure", "Il sont une heure"], 1, "Une heure is feminine, so use une."),("How do you say 3:30?", ["trois heures et demi", "trois heures et demie", "trois heure demie", "trois heures moins demie"], 1, "The expression is trois heures et demie; demie agrees with heure."),("Complete: Le train part ___ huit heures.", ["en", "à", "de", "dans"], 1, "Use à before a specific clock time."),("What does dans dix minutes mean?", ["For ten minutes", "Ten minutes ago", "In ten minutes", "At ten o'clock"], 2, "Dans + duration means a period from now.")],
"speaking":[
"Read clock times at every five-minute interval from 1:00 to 2:00.",
"Say 3:15, 3:30 and 3:45 using et quart, et demie and moins le quart.",
"Convert five digital times into spoken 24-hour French.",
"Describe your weekday from the time you wake up until bedtime.",
"Make five sentences with toujours, souvent, parfois, rarement and jamais."
],
"summary":[
"Ask Quelle heure est-il ? and answer Il est…",
"Use et quart, et demie and moins le quart for common clock times.",
"Use midi and minuit without heures.",
"Use à before a specific clock time and frequency words to describe routines."
]
},
7: {
"vocabulary":[
("un livre","a book","uhn leevr","/œ̃ livʁ/","C'est un livre."),
("une table","a table","ün tabl","/yn tabl/","La table est grande."),
("un stylo","a pen","uhn stee-loh","/œ̃ sti.lo/","J'ai un stylo."),
("une chaise","a chair","ün shez","/yn ʃɛz/","La chaise est confortable."),
("un ordinateur","a computer","uhn or-dee-nah-tuhr","/œ̃ ɔʁ.di.na.tœʁ/","L'ordinateur est neuf."),
("une école","a school","ün ay-kol","/yn e.kɔl/","L'école est proche."),
("l'homme","the man","lom","/lɔm/","L'homme est professeur."),
("la femme","the woman","lah fam","/la fam/","La femme est médecin."),
("un ami / une amie","a friend","uhn ah-mee / ün ah-mee","/œ̃ a.mi/","Mon amie arrive."),
("des enfants","some children","day-zahn-fahn","/de.zɑ̃.fɑ̃/","Les enfants jouent."),
("le problème","the problem (masculine)","luh pro-blem","/lə pʁɔ.blɛm/","Le problème est simple."),
("la voiture","the car","lah vwah-tür","/la vwa.tyʁ/","La voiture est rouge.")
],
"grammar":[
("Every French noun has grammatical gender","A noun is masculine or feminine whether it refers to a person, object or abstract idea. Gender is a grammatical category, not a reliable clue about real-world sex. Learn each noun with its article: un livre, une table. The article helps you remember the noun's gender and choose matching adjectives later."),
("Indefinite articles un, une and des","Use un before a masculine singular noun, une before a feminine singular noun, and des for plural nouns of either gender: un livre, une chaise, des livres, des chaises. These often mean a/an or some. The plural article does not change according to gender."),
("Definite articles le, la, l' and les","Use le for masculine singular, la for feminine singular, l' before a vowel or silent h, and les for plural: le livre, la table, l'école, les amis. Definite articles can mean the, but French also uses them when speaking generally about a category: J'aime le café (I like coffee)."),
("Contractions with à and de","When à is followed by le, they combine into au; à + les becomes aux. De + le becomes du; de + les becomes des. There is no contraction with la or l': à la, à l'école, de la, de l'eau. These contractions are required in standard written French."),
("Recognising gender patterns without overgeneralising","Endings can offer clues: -tion and -sion nouns are often feminine (la nation, la décision); -age and -ment nouns are often masculine (le village, le changement). These are tendencies, not guarantees. There are exceptions, so use a dictionary and memorise the article whenever you meet a new noun."),
("Plural formation basics","Most nouns form the plural by adding -s, which is usually silent: un livre → des livres. Nouns ending in -s, -x or -z often keep the same written form in the plural. The article tells you whether the noun is singular or plural: le nez / les nez.")
],
"expressions":[
("C'est un… / C'est une…","It's a…","Identify a singular object."),
("Ce sont des…","These are… / They are…","Identify plural things or people."),
("J'aime le… / la…","I like…","Use the definite article for general preferences."),
("Il y a un / une…","There is a…","Introduce something present."),
("Combien de… ?","How many…?","Ask about quantity.")
],
"examples":[
("C'est un ordinateur et c'est une souris.","It is a computer and it is a mouse.","Un is masculine; une is feminine."),
("L'école est près de la maison.","The school is near the house.","L' is used before the vowel in école."),
("Les livres sont sur la table.","The books are on the table.","Les marks plural for both genders."),
("J'aime le chocolat, mais je préfère la vanille.","I like chocolate, but I prefer vanilla.","Use le/la for general likes."),
("Nous allons au cinéma et à la bibliothèque.","We are going to the cinema and to the library.","À + le contracts to au; à + la stays separate."),
("Elle parle des étudiants et de l'école.","She talks about the students and the school.","De + les contracts to des; de + l' stays separate.")
],
"conversations":[
("In a classroom",[("A","Qu'est-ce que c'est ?"),("B","C'est un dictionnaire."),("A","Et là, ce sont des cahiers ?"),("B","Oui, ce sont les cahiers des étudiants."),("A","Merci !")],"A: What is this? B: It's a dictionary. A: And there, are those notebooks? B: Yes, they are the students' notebooks. A: Thank you!"),
("Describing a room",[("A","Il y a une table dans la chambre ?"),("B","Oui, et il y a aussi un lit."),("A","Où sont les chaises ?"),("B","Les chaises sont près de la fenêtre."),("A","La chambre est très jolie !")],"A: Is there a table in the bedroom? B: Yes, and there is also a bed. A: Where are the chairs? B: The chairs are near the window. A: The room is very pretty!")
],
"exercises":[("Choose the correct indefinite article: ___ chaise.", ["un", "une", "le", "l'"], 1, "Chaise is feminine singular: une chaise."),("Choose the correct definite article: ___ école.", ["le", "la", "l'", "les"], 2, "École begins with a vowel, so la becomes l'école."),("Complete the contraction: à + le cinéma = ___.", ["à le cinéma", "au cinéma", "aux cinéma", "du cinéma"], 1, "À + le contracts to au."),("Which noun is feminine?", ["livre", "problème", "voiture", "ordinateur"], 2, "Voiture is feminine: la voiture.")],
"speaking":[
"Learn ten new nouns with their article, not as isolated words.",
"Sort a list of objects into masculine and feminine groups.",
"Change five singular nouns into plural phrases with des and les.",
"Say six sentences identifying objects with c'est un, c'est une and ce sont des.",
"Practise au, aux, du and des in short phrases."
],
"summary":[
"Every French noun has grammatical gender; learn it with un or une.",
"Use un/une/des for indefinite nouns and le/la/l'/les for definite nouns.",
"French articles show number and gender; plural articles are the same for both genders.",
"Remember required contractions: au, aux, du and des."
]
},
8: {
"vocabulary":[
("je","I","zhuh","/ʒə/","Je suis étudiant."),
("tu","you (singular informal)","tü","/ty/","Tu es gentil."),
("il","he; it (masculine)","eel","/il/","Il est canadien."),
("elle","she; it (feminine)","ell","/ɛl/","Elle est professeure."),
("on","one; we; people","ohn","/ɔ̃/","On est prêts."),
("nous","we","noo","/nu/","Nous sommes ici."),
("vous","you (formal or plural)","voo","/vu/","Vous êtes en classe."),
("ils","they (masculine or mixed)","eel","/il/","Ils sont amis."),
("elles","they (all feminine)","ell","/ɛl/","Elles sont étudiantes."),
("être","to be","eh-truh","/ɛtʁ/","Je veux être prêt."),
("suis","am","swee","/sɥi/","Je suis à la maison."),
("es","are (tu)","ay","/ɛ/","Tu es mon ami."),
("est","is","eh","/ɛ/","Elle est ici."),
("sommes","are (nous)","som","/sɔm/","Nous sommes contents."),
("êtes","are (vous)","ett","/ɛt/","Vous êtes gentils."),
("sont","are (ils/elles)","sohn","/sɔ̃/","Ils sont au travail.")
],
"grammar":[
("The complete present tense of être","Être is irregular and must be memorised: je suis, tu es, il/elle/on est, nous sommes, vous êtes, ils/elles sont. Do not try to add regular endings. Say the forms aloud as a rhythm and connect each one to its subject pronoun."),
("Subject pronouns and when French uses them","French normally includes a subject pronoun before a conjugated verb: Je parle, Elle travaille. Unlike English, il and elle can refer to things as well as people, and the pronoun follows the noun's grammatical gender. On is very common in everyday French to mean we or people in general; its verb is always third-person singular: on est."),
("Choosing nous or on in everyday Canadian French","Nous is standard and common in formal writing, careful speech and when emphasis is needed. On is extremely frequent in everyday conversation and often means we: On est prêts. Although it means we, on takes the same verb form as il/elle. The adjective after on may still describe the people meant, so context matters."),
("Negation with être","Place ne before the verb and pas after it: Je ne suis pas fatigué; Elle n'est pas ici. Before a vowel, ne becomes n': Il n'est pas prêt. In casual spoken French, ne is often dropped (Je suis pas prêt), especially in informal Canadian speech, but learn and use the complete form in careful writing."),
("Adjectives after être must agree","The adjective or nationality after être agrees with the person or noun described: Il est canadien; Elle est canadienne; Ils sont canadiens; Elles sont canadiennes. Many feminine forms add -e and many plural forms add -s, but spelling and pronunciation do not always change together. Learn the common pairs."),
("C'est versus il/elle est","Use c'est + noun with an article or name to identify: C'est un professeur; C'est Marie. Use il/elle est + adjective or profession in many descriptions: Elle est gentille; Il est professeur. The distinction becomes more complex later, but this beginner pattern is a reliable starting point.")
],
"expressions":[
("Je suis…","I am…","Give identity, condition or location."),
("Tu es prêt(e) ?","Are you ready?","Informal question."),
("Nous sommes ici.","We are here.","State where a group is."),
("On est d'accord.","We agree.","Very common spoken use of on."),
("Ce n'est pas grave.","It's not a big deal.","Reassuring expression."),
("Qui est-ce ?","Who is it?","Ask who someone is.")
],
"examples":[
("Je suis débutant, mais je suis motivé.","I am a beginner, but I am motivated.","Être describes identity and state."),
("Elle est angolaise et elle habite à Luanda.","She is Angolan and lives in Luanda.","Feminine nationality agreement."),
("Nous sommes en classe, mais ils sont au travail.","We are in class, but they are at work.","Different subject pronouns require different être forms."),
("On est prêts pour le cours.","We're ready for the class.","On takes est; prêts describes the group."),
("Ce ne sont pas des livres; ce sont des cahiers.","These are not books; they are notebooks.","Plural c'est becomes ce sont."),
("Vous êtes professeur ou étudiant ?","Are you a teacher or a student?","Vous can be formal singular or plural.")
],
"conversations":[
("A new class",[("A","Bonjour ! Vous êtes dans le cours de français ?"),("B","Oui, je suis dans le groupe A."),("A","Nous sommes dans le même groupe !"),("B","Super. On est prêts à commencer ?"),("A","Oui, nous sommes prêts.")],"A: Hello! Are you in the French class? B: Yes, I'm in group A. A: We're in the same group! B: Great. Are we ready to start? A: Yes, we're ready."),
("Introducing friends",[("A","Qui est cette personne ?"),("B","C'est mon ami, Lucas."),("A","Il est canadien ?"),("B","Oui, il est de Québec. Et voici Amélie."),("A","Elle est aussi dans notre classe ?"),("B","Oui, nous sommes tous étudiants.")],"A: Who is that person? B: That's my friend, Lucas. A: Is he Canadian? B: Yes, he's from Quebec City. And here is Amélie. A: Is she also in our class? B: Yes, we're all students.")
],
"exercises":[("Complete: Nous ___ contents.", ["êtes", "sont", "sommes", "sommes être"], 2, "The nous form of être is sommes."),("Choose the correct form: On ___ prêts.", ["sommes", "êtes", "est", "sont"], 2, "On always takes the third-person singular verb est."),("Make the sentence negative: Elle est ici.", ["Elle pas est ici", "Elle ne est pas ici", "Elle n'est pas ici", "Elle est ne pas ici"], 2, "Ne becomes n' before est: Elle n'est pas ici."),("Choose the correct sentence.", ["Elles est canadiennes", "Elles sont canadiennes", "Elles sommes canadiennes", "Elles êtes canadiennes"], 1, "Elles takes sont, and the adjective is feminine plural.")],
"speaking":[
"Recite all six être forms without looking, then add the subject pronoun.",
"Make one positive and one negative sentence for each of je, tu, il/elle, nous and vous.",
"Describe three people using nationality or personality adjectives with correct agreement.",
"Say the same sentence with nous and then with on, keeping the correct verb form.",
"Practise the difference between C'est un professeur and Il est professeur."
],
"summary":[
"Memorise all forms of être: suis, es, est, sommes, êtes, sont.",
"French normally uses subject pronouns; on is a common spoken equivalent of we.",
"Negation surrounds the conjugated verb: ne…pas.",
"Adjectives and nationalities agree with the person or noun described.",
"Use c'est to identify with a noun phrase and il/elle est for many descriptions."
]
},
9: {
"vocabulary":[
("avoir","to have","ah-vwahr","/a.vwaʁ/","Je veux avoir un chien."),
("j'ai","I have","zhay","/ʒe/","J'ai un frère."),
("tu as","you have","tü ah","/ty a/","Tu as un stylo."),
("il a / elle a","he has / she has","eel ah / ell ah","/il a/","Elle a une voiture."),
("nous avons","we have","noo-zah-vohn","/nu.za.vɔ̃/","Nous avons du temps."),
("vous avez","you have","voo-zah-vay","/vu.za.ve/","Vous avez une question."),
("ils ont / elles ont","they have","eel-zohn / ell-zohn","/il.zɔ̃/","Ils ont deux enfants."),
("l'âge","age","lahzh","/laʒ/","Quel âge as-tu ?"),
("faim","hunger","fan","/fɛ̃/","J'ai faim."),
("soif","thirst","swahf","/swaf/","Elle a soif."),
("peur","fear","puhr","/pœʁ/","Il a peur du noir."),
("raison","reason; correctness","reh-zohn","/ʁɛ.zɔ̃/","Tu as raison."),
("tort","wrongness","tor","/tɔʁ/","Vous avez tort."),
("besoin","need","buh-zwan","/bə.zwɛ̃/","J'ai besoin d'aide."),
("envie","desire; urge","ahn-vee","/ɑ̃.vi/","J'ai envie de dormir."),
("chance","luck","shahns","/ʃɑ̃s/","Nous avons de la chance.")
],
"grammar":[
("The complete present tense of avoir","Avoir is irregular: j'ai, tu as, il/elle/on a, nous avons, vous avez, ils/elles ont. Notice the liaison in nous avons and vous avez when speaking naturally. Memorise the forms as complete chunks; they are among the most frequently used verbs in French."),
("Avoir for age and possession","Use avoir for possession: J'ai un livre (I have a book). French also uses avoir for age: J'ai vingt ans. Do not say Je suis vingt ans. Ask Quel âge as-tu ? or Quel âge avez-vous ? depending on familiarity and politeness."),
("Common feelings and needs use avoir","Several expressions that use 'to be' in English use avoir in French: avoir faim (be hungry), avoir soif (be thirsty), avoir peur (be afraid), avoir chaud/froid (feel hot/cold), avoir sommeil (be sleepy). Learn each as a fixed expression with avoir."),
("Avoir besoin de and avoir envie de","Avoir besoin de means to need; avoir envie de means to feel like or want. Before a noun, the de form contracts: besoin d'eau, envie de café. Before an infinitive, keep de + verb: J'ai envie de sortir. These phrases are followed by de, not à."),
("Negating avoir and using questions","Put ne…pas around the conjugated verb: Je n'ai pas de voiture; Nous n'avons pas faim. For a question, use rising intonation (Tu as un frère ?), est-ce que (Est-ce que tu as un frère ?) or inversion in formal language (Avez-vous une question ?). After a negative, un/une/des often become de/d'."),
("Liaison and pronunciation of avoir","In nous avons and vous avez, the normally silent final s links to the vowel at the start of avons/avez and sounds like /z/. In ils ont, the final s also links as /z/. Practise the whole phrase rather than pronouncing each word separately.")
],
"expressions":[
("J'ai faim.","I'm hungry.","Avoir + faim."),
("J'ai soif.","I'm thirsty.","Avoir + soif."),
("J'ai besoin de…","I need…","Follow with de + noun or infinitive."),
("J'ai envie de…","I feel like…","Express a desire."),
("Tu as raison.","You're right.","Fixed avoir expression."),
("J'ai de la chance.","I'm lucky.","Use avoir with chance.")
],
"examples":[
("Nous avons deux cours aujourd'hui.","We have two classes today.","Avoir expresses possession or scheduled events."),
("Elle a vingt-cinq ans et elle a un frère.","She is twenty-five and she has a brother.","Age and possession both use avoir."),
("J'ai faim, mais je n'ai pas soif.","I'm hungry, but I'm not thirsty.","Negation surrounds ai."),
("Vous avez besoin d'un dictionnaire ?","Do you need a dictionary?","Besoin de + noun; de + un contracts to d'un."),
("Ils ont envie de visiter Québec.","They feel like visiting Quebec City.","Envie de + infinitive."),
("Tu as raison : nous avons assez de temps.","You're right: we have enough time.","Avoir raison is a fixed expression.")
],
"conversations":[
("At lunchtime",[("A","Tu as faim ?"),("B","Oui, j'ai très faim. Et toi ?"),("A","J'ai soif. Tu veux de l'eau ?"),("B","Oui, merci. Nous avons aussi du pain ?"),("A","Oui, il y en a dans le sac.")],"A: Are you hungry? B: Yes, I'm very hungry. And you? A: I'm thirsty. Do you want water? B: Yes, thanks. Do we also have bread? A: Yes, there's some in the bag."),
("Asking for help",[("A","Excusez-moi, vous avez un dictionnaire ?"),("B","Oui, j'ai un dictionnaire."),("A","Merci. J'ai besoin de vérifier un mot."),("B","Pas de problème. Vous avez besoin d'autre chose ?"),("A","Non, merci beaucoup.")],"A: Excuse me, do you have a dictionary? B: Yes, I have one. A: Thank you. I need to check a word. B: No problem. Do you need anything else? A: No, thank you very much.")
],
"exercises":[("Complete: Vous ___ une question ?", ["avez", "avons", "ont", "as"], 0, "The vous form of avoir is avez."),("How do you say 'I am hungry'?", ["Je suis faim", "J'ai faim", "Je fais faim", "Je faim"], 1, "French uses avoir faim."),("Complete: J'ai besoin ___ aide.", ["à", "de", "d'", "du"], 2, "Besoin de becomes besoin d' before a vowel sound: besoin d'aide."),("Choose the correct negative sentence.", ["Je ne ai pas faim", "Je n'ai pas faim", "Je pas ai faim", "Je n'ai faim pas"], 1, "Ne becomes n' before ai and pas follows the verb.")],
"speaking":[
"Recite avoir in all six subject forms and pay attention to the linking /z/ sounds.",
"Say your age and describe three things you have.",
"Make sentences with faim, soif, peur, chaud, froid and sommeil.",
"Practise J'ai besoin de… and J'ai envie de… with five nouns and five infinitives.",
"Turn five positive avoir sentences into negative sentences."
],
"summary":[
"Avoir is irregular: j'ai, tu as, il a, nous avons, vous avez, ils ont.",
"Use avoir for possession, age and many physical feelings.",
"Memorise avoir faim, avoir soif, avoir besoin de and avoir envie de.",
"Use ne…pas around avoir; un/une/des often become de after a negative."
]
},
10: {
"vocabulary":[
("grand / grande","tall; big","grahn / grahnd","/ɡʁɑ̃/","C'est une grande maison."),
("petit / petite","small; short","puh-tee / puh-teet","/pə.ti/","Un petit café."),
("jeune","young","zhuhn","/ʒœn/","Elle est jeune."),
("vieux / vieille","old","vyuh / vyay","/vjø/","Un vieil homme."),
("beau / belle","beautiful; handsome","boh / bell","/bo / bɛl/","Une belle journée."),
("joli / jolie","pretty","zho-lee","/ʒɔ.li/","Une jolie fleur."),
("gentil / gentille","kind","zhahn-tee / zhahn-teey","/ʒɑ̃.ti/","Il est gentil."),
("sympathique","friendly; nice","sam-pah-teek","/sɛ̃.pa.tik/","Ma collègue est sympathique."),
("intelligent / intelligente","intelligent","an-tel-ee-zhahn / ahnt","/ɛ̃.te.li.ʒɑ̃/","C'est une personne intelligente."),
("drôle","funny","drohl","/dʁol/","Mon frère est drôle."),
("sérieux / sérieuse","serious","say-ree-uh / say-ree-uhz","/se.ʁjø/","Elle est sérieuse."),
("fatigué / fatiguée","tired","fah-tee-gay","/fa.ti.ɡe/","Je suis fatigué."),
("content / contente","happy; pleased","kohn-tahn / kohn-tahnt","/kɔ̃.tɑ̃/","Nous sommes contents."),
("sportif / sportive","sporty; athletic","spor-teef / spor-teev","/spɔʁ.tif/","Elle est sportive."),
("calme","calm","kalm","/kalm/","Il est calme."),
("bavard / bavarde","talkative","bah-var / bah-vard","/ba.vaʁ/","Mon ami est bavard.")
],
"grammar":[
("Adjective agreement: masculine and feminine","Most French adjectives agree with the noun or person they describe. A common pattern adds -e for the feminine: grand → grande, petit → petite, content → contente. If the masculine form already ends in -e, the written feminine may be identical: jeune, calme. Agreement is grammatical even when the final sound does not change."),
("Plural adjective agreement","Add -s to most adjectives describing plural nouns or people: un garçon intelligent, des garçons intelligents; une fille intelligente, des filles intelligentes. The s is usually silent. Some adjectives have special plural forms, and adjectives ending in -s or -x may not change in the masculine plural."),
("Common irregular feminine forms","Some frequent adjectives change more than by adding -e: beau → belle, vieux → vieille, nouveau → nouvelle, gentil → gentille, sportif → sportive, sérieux → sérieuse. Learn these pairs together. Before a masculine singular noun beginning with a vowel or silent h, beau, vieux and nouveau can take special forms: bel, vieil, nouvel."),
("Where adjectives are placed","Many descriptive adjectives follow the noun: une voiture rouge, un étudiant intelligent. A common group of short, frequent adjectives often comes before the noun, including beauty, age, goodness and size words: un beau livre, une jeune femme, un bon ami, une grande maison. Meaning can sometimes change with position, so learn common phrases as chunks."),
("Using être to describe people","Use être + adjective: Elle est gentille; Ils sont sérieux. The adjective agrees with the subject, not with the speaker. To ask about personality or appearance, use Comment est-il ? / Comment est-elle ? For a plural group, use Comment sont-ils ?"),
("C'est très… and intensifiers","Place très before an adjective to mean very: très gentil, très grande. Assez means fairly or enough depending on context; vraiment means really; un peu means a little. These words do not change for gender or number: Elle est très gentille; Ils sont très gentils.")
],
"expressions":[
("Il est de taille moyenne.","He is of average height.","Describe height neutrally."),
("Elle a les cheveux…","She has … hair.","Use avoir for physical features."),
("Il a l'air…","He looks…","Avoir l'air introduces an impression."),
("très gentil(le)","very kind","Intensifier + adjective."),
("un peu timide","a little shy","Un peu softens a description."),
("à mon avis","in my opinion","Introduce a personal impression.")
],
"examples":[
("Mon frère est grand et ma sœur est petite.","My brother is tall and my sister is short.","Adjectives agree with each person."),
("C'est une personne très sympathique.","She/He is a very friendly person.","Personne is feminine, so the adjective is feminine."),
("Ils sont sérieux, mais ils sont aussi très drôles.","They are serious, but they are also very funny.","Masculine plural agreement for a mixed or masculine group."),
("Elle porte une belle robe rouge.","She is wearing a beautiful red dress.","Belle comes before the noun; rouge follows it."),
("Mon vieil ami est calme et généreux.","My old friend is calm and generous.","Vieil is used before a masculine vowel-starting noun."),
("À mon avis, cette professeure est vraiment gentille.","In my opinion, this teacher is really kind.","Intensifiers do not change form.")
],
"conversations":[
("Describing a new colleague",[("A","Comment est ta nouvelle collègue ?"),("B","Elle est jeune, intelligente et très sympathique."),("A","Elle est sérieuse ?"),("B","Oui, mais elle est aussi drôle."),("A","Elle a l'air agréable !")],"A: What is your new colleague like? B: She's young, intelligent and very friendly. A: Is she serious? B: Yes, but she's also funny. A: She seems pleasant!"),
("Choosing a gift",[("A","Tu aimes ce petit sac ?"),("B","Oui, il est joli, mais il est un peu cher."),("A","Et cette grande boîte ?"),("B","Elle est belle et pratique."),("A","Alors, prenons la boîte !")],"A: Do you like this small bag? B: Yes, it's pretty, but it's a little expensive. A: And this large box? B: It's beautiful and practical. A: Then let's take the box!")
],
"exercises":[("Choose the correct feminine form of beau.", ["beau", "beaux", "belle", "bel"], 2, "The feminine form is belle."),("Choose the correct phrase.", ["une maison grand", "une grand maison", "une grande maison", "un grande maison"], 2, "Maison is feminine, and grande agrees with it."),("Where does the colour adjective normally go?", ["Before the noun", "After the noun", "Before the article", "It must be first"], 1, "Most colour adjectives follow the noun: une voiture rouge."),("Complete: Ils sont ___.", ["gentil", "gentille", "gentils", "gentilles"], 2, "For a masculine or mixed plural group, use gentils.")],
"speaking":[
"Describe yourself with five adjectives and make every adjective agree correctly.",
"Describe two people: one masculine, one feminine, then describe them together as a plural group.",
"Practise beau/belle, vieux/vieille, nouveau/nouvelle and gentil/gentille.",
"Describe an object using one adjective before the noun and one after it.",
"Give a short opinion using à mon avis, très, vraiment and un peu."
],
"summary":[
"Adjectives agree in gender and number with the noun or person they describe.",
"Many feminine adjectives add -e and many plural adjectives add -s.",
"Learn irregular pairs such as beau/belle and vieux/vieille.",
"Many common adjectives follow the noun, while frequent size, age and beauty adjectives often precede it."
]
},
11: {
"vocabulary":[
("les parents","parents","lay pah-rahn","/le pa.ʁɑ̃/","Mes parents habitent ici."),
("le père","father","luh pair","/lə pɛʁ/","Mon père travaille."),
("la mère","mother","lah mehr","/la mɛʁ/","Ma mère cuisine."),
("le fils","son","luh fees","/lə fis/","Leur fils est étudiant."),
("la fille","daughter; girl","lah fee-yuh","/la fij/","Sa fille a dix ans."),
("le frère","brother","luh frair","/lə fʁɛʁ/","J'ai un frère."),
("la sœur","sister","lah suhr","/la sœʁ/","Ma sœur est gentille."),
("le grand-père","grandfather","luh grahn pair","/lə ɡʁɑ̃ pɛʁ/","Mon grand-père est calme."),
("la grand-mère","grandmother","lah grahn mehr","/la ɡʁɑ̃ mɛʁ/","Ma grand-mère habite à Québec."),
("l'oncle","uncle","lohnkl","/lɔ̃kl/","Mon oncle arrive demain."),
("la tante","aunt","lah tahnt","/la tɑ̃t/","Ma tante est drôle."),
("le cousin / la cousine","cousin","luh koo-zan / lah koo-zeen","/ku.zɛ̃/","Ma cousine est médecin."),
("le mari","husband","luh mah-ree","/lə ma.ʁi/","Son mari est professeur."),
("la femme / l'épouse","wife","lah fam / lay-pooz","/la fam/","Son épouse travaille ici."),
("les enfants","children","lay-zahn-fahn","/le.zɑ̃.fɑ̃/","Les enfants jouent dehors."),
("les grands-parents","grandparents","lay grahn-pah-rahn","/le ɡʁɑ̃.pa.ʁɑ̃/","Mes grands-parents sont gentils.")
],
"grammar":[
("Possessive adjectives agree with the thing owned","Mon, ma and mes mean my; ton, ta and tes mean your (informal); son, sa and ses mean his/her. The possessive agrees with the noun that follows, not with the owner: son père (his or her father), sa mère, ses parents. This is why son can refer to a woman’s father."),
("The full possessive set","For one owner, learn the pattern: mon/ma/mes, ton/ta/tes, son/sa/ses. For nous, use notre/nos; for vous, votre/vos; for ils/elles, leur/leurs. The plural form is based on the number of things owned: leur enfant but leurs enfants."),
("Mon before a feminine vowel-starting noun","Before a feminine singular noun beginning with a vowel or silent h, use mon rather than ma to avoid two vowel sounds: mon amie, mon école. The noun remains feminine; the special form is for pronunciation only. The plural remains mes: mes amies."),
("Family relationships with être and avoir","Use avoir to say you have a family member: J'ai deux sœurs. Use être to describe someone: Ma sœur est gentille. To say whose family member someone is, use the correct possessive: mon frère, ta tante, leurs enfants."),
("C'est, ce sont and possessive phrases","Use C'est mon frère to identify one person and Ce sont mes cousins for a plural group. Do not say C'est mes cousins in careful standard French. Use Qui est-ce ? to ask who someone is and C'est qui, lui ? in familiar conversation."),
("Gender-neutral and varied family descriptions","Family structures differ. French vocabulary can describe parents, grandparents, children, step-relatives and spouses; choose the word that accurately fits the relationship. For a blended or mixed group, masculine plural forms are traditionally used in standard grammar, while context identifies the people.")
],
"expressions":[
("Dans ma famille…","In my family…","Introduce a family description."),
("Je suis fils unique / fille unique.","I am an only child.","Choose the form matching the speaker."),
("Nous sommes proches.","We are close.","Describe a close relationship."),
("Il a deux enfants.","He has two children.","Avoir describes family members."),
("C'est ma cousine.","She is my cousin.","Possessive agrees with cousine."),
("Ils habitent près de chez nous.","They live near our home.","Chez nous means at our home/our place.")
],
"examples":[
("Mon père s'appelle André et ma mère s'appelle Lise.","My father's name is André and my mother's name is Lise.","Mon and ma agree with père and mère."),
("Mes grands-parents habitent à Québec.","My grandparents live in Quebec City.","Mes is used with a plural noun."),
("Ma sœur a deux enfants : ce sont mon neveu et ma nièce.","My sister has two children: they are my nephew and my niece.","Mon and ma agree separately with neveu and nièce."),
("Mon amie et son frère étudient à Montréal.","My friend and her brother study in Montreal.","Mon amie is used before a feminine vowel-starting noun."),
("Leurs parents sont très gentils.","Their parents are very kind.","Leurs agrees with plural parents."),
("Nous sommes une famille unie et nous nous aidons.","We are a close-knit family and we help one another.","Unie agrees with famille.")
],
"conversations":[
("Talking about family",[("A","Tu as des frères et des sœurs ?"),("B","Oui, j'ai un frère et deux sœurs."),("A","Comment s'appellent-ils ?"),("B","Mon frère s'appelle Paul et mes sœurs s'appellent Julie et Ana."),("A","Ils habitent près de chez toi ?"),("B","Oui, ils habitent dans la même ville.")],"A: Do you have brothers and sisters? B: Yes, I have one brother and two sisters. A: What are their names? B: My brother is called Paul and my sisters are called Julie and Ana. A: Do they live near you? B: Yes, they live in the same city."),
("Introducing grandparents",[("A","Qui sont ces personnes ?"),("B","Ce sont mes grands-parents."),("A","Ils habitent au Québec ?"),("B","Oui. Ma grand-mère habite à Québec et mon grand-père habite avec elle."),("A","Ils ont l'air heureux !"),("B","Oui, ils sont très gentils.")],"A: Who are these people? B: These are my grandparents. A: Do they live in Quebec? B: Yes. My grandmother lives in Quebec City and my grandfather lives with her. A: They look happy! B: Yes, they are very kind.")
],
"exercises":[("Complete: ___ mère s'appelle Marie. (my)", ["Mon", "Ma", "Mes", "Son"], 1, "Mère is feminine singular, so use ma."),("Choose the correct phrase before amie.", ["ma amie", "mon amie", "mes amie", "moi amie"], 1, "Use mon before a feminine singular noun beginning with a vowel sound."),("Complete: Ce sont ___ parents. (their)", ["leur", "leurs", "son", "sa"], 1, "Parents is plural, so use leurs."),("Which sentence is correct?", ["C'est mes cousins", "Ce sont mes cousins", "Ce sont mon cousins", "C'est ma cousins"], 1, "Use ce sont to identify a plural group.")],
"speaking":[
"Draw or imagine a family tree and introduce at least six relatives in French.",
"Describe who owns each relationship using mon, ma, mes, son, sa and ses.",
"Practise mon amie, mon école and mes amies to hear the vowel-linking reason.",
"Give a short family description using avoir for relationships and être for descriptions.",
"Say two sentences about a family member's routine or home."
],
"summary":[
"Possessive adjectives agree with the noun owned, not with the owner.",
"Use mon/ma/mes, ton/ta/tes, son/sa/ses, notre/nos, votre/vos and leur/leurs.",
"Use mon before a feminine singular noun beginning with a vowel or silent h.",
"Use avoir to say you have relatives and être to describe them."
]
},
12: {
"vocabulary":[
("noir / noire","black","nwahr","/nwaʁ/","Un manteau noir."),
("blanc / blanche","white","blahn / blahnsh","/blɑ̃/","Une chemise blanche."),
("rouge","red","roozh","/ʁuʒ/","Une voiture rouge."),
("bleu / bleue","blue","bluh","/blø/","Un ciel bleu."),
("vert / verte","green","vair / vair-tuh","/vɛʁ/","Une porte verte."),
("jaune","yellow","zhohn","/ʒon/","Un citron jaune."),
("orange","orange","oh-rahnzh","/ɔ.ʁɑ̃ʒ/","Une fleur orange."),
("rose","pink","rohz","/ʁoz/","Un sac rose."),
("violet / violette","purple","vee-oh-lay / vee-oh-let","/vjɔ.lɛ/","Une robe violette."),
("gris / grise","grey","gree / greez","/ɡʁi/","Un chat gris."),
("marron","brown","mah-rohn","/ma.ʁɔ̃/","Des chaussures marron."),
("clair / claire","light; pale","klair","/klɛʁ/","Un bleu clair."),
("foncé / foncée","dark","fohn-say","/fɔ̃.se/","Une veste bleue foncée."),
("l'objet","object (m.)","loh-zhay","/lɔb.ʒɛ/","Quel est cet objet ?"),
("la couleur","colour","lah koo-luhr","/la ku.lœʁ/","Quelle est ta couleur préférée ?"),
("la fenêtre","window","lah fuh-netr","/la fə.nɛtʁ/","La fenêtre est ouverte.")
],
"grammar":[
("Colour adjectives usually follow the noun","In French, a colour normally comes after the noun: une voiture rouge, un livre bleu, des fleurs jaunes. This is the opposite of the usual English order. The colour agrees with the noun in gender and number when it is an ordinary adjective."),
("Masculine, feminine and plural colour forms","Many colours add -e for feminine and -s for plural: vert/verte/verts/vertes; noir/noire/noirs/noires. Some have the same written masculine and feminine form, such as rouge and jaune, but still add -s in the plural. Learn each colour's forms rather than assuming all behave identically."),
("Invariable colour words and compound colours","Some colour words derived from nouns are commonly invariable: orange and marron do not usually change for gender or number. Compound colour expressions are also generally invariable: bleu clair, vert foncé, bleu-vert. This is a useful exception to the usual agreement rule."),
("Demonstrative adjectives ce, cet, cette and ces","Use ce before a masculine singular noun beginning with a consonant: ce livre. Use cet before a masculine singular noun beginning with a vowel or silent h: cet objet. Use cette for feminine singular and ces for plural: cette table, ces objets. These forms mean this, that, these or those depending on context."),
("C'est quelle couleur ? and describing objects","Ask De quelle couleur est… ? or Quelle est la couleur de… ? Answer Le sac est rouge or C'est un sac rouge. Use être to describe the colour and c'est + noun phrase to identify the object. For multiple objects, the adjective becomes plural when it agrees."),
("Adjective position and intensifiers in descriptions","Colour adjectives follow the noun even when other adjectives appear before it: une jolie petite boîte rouge. Use très, assez or vraiment before the colour or descriptive adjective: un bleu très foncé. These intensifiers do not agree.")
],
"expressions":[
("De quelle couleur est… ?","What colour is…?","Ask about an object's colour."),
("Ma couleur préférée, c'est…","My favourite colour is…","Give a preference."),
("C'est de quelle taille ?","What size is it?","Ask about dimensions."),
("un peu plus clair","a little lighter","Compare shades."),
("bleu foncé","dark blue","Compound shade expression."),
("cet objet","this/that object","Cet before a masculine vowel-starting noun.")
],
"examples":[
("La voiture rouge est devant la maison blanche.","The red car is in front of the white house.","Colour adjectives follow and agree with nouns."),
("J'aime les chemises bleues et les pantalons noirs.","I like blue shirts and black trousers.","Both colours are plural."),
("Elle porte une robe orange et des chaussures marron.","She is wearing an orange dress and brown shoes.","Orange and marron are invariable."),
("Cet objet est petit, mais cette boîte est grande.","This object is small, but this box is big.","Cet and cette agree with the noun."),
("Nous préférons les couleurs claires au printemps.","We prefer light colours in spring.","Claires agrees with couleurs."),
("Le mur est vert foncé.","The wall is dark green.","Compound colour remains unchanged.")
],
"conversations":[
("Choosing a shirt",[("A","Tu préfères la chemise bleue ou la chemise blanche ?"),("B","Je préfère la bleue."),("A","Et le pantalon noir ?"),("B","Il est joli, mais je cherche quelque chose de plus clair."),("A","Regarde ce pantalon gris !"),("B","Bonne idée.")],"A: Do you prefer the blue shirt or the white shirt? B: I prefer the blue one. A: And the black trousers? B: They're nice, but I'm looking for something lighter. A: Look at these grey trousers! B: Good idea."),
("Describing a picture",[("A","Qu'est-ce qu'il y a sur la photo ?"),("B","Il y a une maison blanche avec une porte rouge."),("A","Et les arbres ?"),("B","Ils sont verts et très grands."),("A","Le ciel est bleu ?"),("B","Oui, il est bleu clair.")],"A: What's in the picture? B: There is a white house with a red door. A: And the trees? B: They are green and very tall. A: Is the sky blue? B: Yes, it is light blue.")
],
"exercises":[("Choose the correct phrase.", ["une robe violet", "une robe violette", "une violette robe", "un robe violette"], 1, "Robe is feminine; violet becomes violette."),("Which colour is normally invariable?", ["vert", "blanc", "orange", "violet"], 2, "Orange is generally invariable when used as a colour adjective."),("Complete: ___ objet est petit.", ["Ce", "Cet", "Cette", "Ces"], 1, "Cet is used before a masculine singular noun beginning with a vowel or silent h."),("Choose the correct plural phrase.", ["des voiture rouge", "des voitures rouges", "des voitures rouge", "des voiture rouges"], 1, "Both the noun and the regular colour adjective take plural marking.")],
"speaking":[
"Name ten colours and give the masculine, feminine and plural forms where they change.",
"Describe five objects around you using a noun followed by a colour.",
"Practise the invariable colours orange and marron and compound shades.",
"Use ce, cet, cette and ces to point out four objects.",
"Describe a photograph or imagined room using at least six colours."
],
"summary":[
"Colour adjectives normally follow the noun and agree in gender and number.",
"Orange and marron are generally invariable; compound shades are also usually invariable.",
"Use ce, cet, cette and ces to say this/that/these/those.",
"Ask De quelle couleur est… ? to ask about an object's colour."
]
},
13: {
"vocabulary":[
("le petit-déjeuner","breakfast","luh puh-tee day-zhuh-nay","/lə pə.ti de.ʒœ.ne/","Je prends le petit-déjeuner."),
("le déjeuner","lunch","luh day-zhuh-nay","/lə de.ʒœ.ne/","Nous prenons le déjeuner à midi."),
("le dîner","dinner","luh dee-nay","/lə di.ne/","Le dîner est prêt."),
("le souper","evening meal; supper (common in Quebec)","luh soo-pay","/lə su.pe/","On soupe à six heures."),
("le pain","bread","luh pan","/lə pɛ̃/","Je voudrais du pain."),
("le fromage","cheese","luh froh-mahzh","/lə fʁɔ.maʒ/","J'aime le fromage."),
("le lait","milk","luh lay","/lə lɛ/","Elle boit du lait."),
("l'eau","water","loh","/lo/","Une bouteille d'eau."),
("le jus","juice","luh zhü","/lə ʒy/","Un jus d'orange."),
("le café","coffee","luh kah-fay","/lə ka.fe/","Je prends un café."),
("le thé","tea","luh tay","/lə te/","Vous voulez du thé ?"),
("la viande","meat","lah vyahnd","/la vjɑ̃d/","Je ne mange pas de viande."),
("le poulet","chicken","luh poo-lay","/lə pu.lɛ/","Le poulet est délicieux."),
("le poisson","fish","luh pwah-sohn","/lə pwa.sɔ̃/","Nous mangeons du poisson."),
("les légumes","vegetables","lay lay-güm","/le le.ɡym/","Les légumes sont frais."),
("les fruits","fruit","lay frwee","/le fʁɥi/","Je mange des fruits.")
],
"grammar":[
("Partitive articles du, de la, de l' and des","Use a partitive article for an unspecified amount of food or drink: du pain, de la soupe, de l'eau, des légumes. It often means some or any in English, but English may omit the word. The article depends on the noun's gender and first sound: du for masculine, de la for feminine, de l' before a vowel or silent h, and des for plural."),
("Definite articles for general likes and dislikes","Use le, la, l' or les when talking about a food category in general: J'aime le fromage; Je déteste les olives. Use the partitive when describing an amount you eat or drink: Je mange du fromage. Compare J'aime le café (I like coffee) with Je bois du café (I drink some coffee)."),
("Partitives after negation","In a negative sentence, du, de la, de l' and des usually become de or d': Je mange du pain → Je ne mange pas de pain; Je bois de l'eau → Je ne bois pas d'eau. The verb être is an important exception: Ce n'est pas du café. Also, the verb aimer keeps the definite article in a negative: Je n'aime pas le café."),
("Ordering politely with vouloir","Use je voudrais + noun to make a polite request: Je voudrais un café; Je voudrais de l'eau. Je veux is more direct and can sound abrupt in a service interaction. Use s'il vous plaît to add politeness and merci after receiving the order."),
("Meals and Canadian French usage","Meal names differ by region and family. In much of France, déjeuner is lunch and dîner is the evening meal. In Quebec, déjeuner commonly means breakfast, dîner means lunch, and souper means the evening meal. Pay attention to local context and clarify politely if a meal time is important."),
("Asking for and understanding a restaurant bill","Use L'addition, s'il vous plaît to ask for the bill. To ask what is included, say Qu'est-ce qui est compris ? For a table, ask Une table pour deux, s'il vous plaît. In Quebec, pourboire means tip; service and tipping customs vary by venue.")
],
"expressions":[
("Je voudrais…","I would like…","Polite way to order."),
("L'addition, s'il vous plaît.","The bill, please.","Ask for the bill."),
("Bon appétit !","Enjoy your meal!","Said before eating."),
("C'est délicieux.","It's delicious.","Compliment food."),
("Je suis végétarien / végétarienne.","I'm vegetarian.","Choose the matching form."),
("sans…","without…","State an ingredient to leave out.")
],
"examples":[
("Au petit-déjeuner, je prends du pain et du café.","For breakfast, I have bread and coffee.","Partitive articles express an amount."),
("J'aime le fromage, mais je ne mange pas de viande.","I like cheese, but I don't eat meat.","Definite article for preference; de after negation."),
("Je voudrais une soupe et de l'eau, s'il vous plaît.","I would like a soup and some water, please.","Une counts a serving; de l'eau is uncounted."),
("Au Québec, le dîner est souvent le repas du midi.","In Quebec, dîner is often the midday meal.","Regional meal vocabulary differs."),
("Nous prenons le souper à sept heures.","We have supper at seven.","Souper is common Canadian French usage."),
("Le pourboire est compris ?","Is the tip included?","Pourboire is masculine, so the adjective is compris.")
],
"conversations":[
("Ordering at a café",[("A","Bonjour ! Vous désirez ?"),("B","Je voudrais un café et un croissant, s'il vous plaît."),("A","Sur place ou pour emporter ?"),("B","Pour emporter, merci."),("A","Voilà. Bonne journée !"),("B","Merci, bonne journée !")],"A: Hello! What would you like? B: I'd like a coffee and a croissant, please. A: For here or to go? B: To go, thank you. A: Here you are. Have a good day! B: Thank you, have a good day!"),
("At a restaurant in Quebec",[("A","Bonsoir. Une table pour deux, s'il vous plaît."),("B","Bien sûr. Voici le menu."),("A","Qu'est-ce que vous recommandez ?"),("B","La soupe et le poulet sont excellents."),("A","Parfait. Je voudrais la soupe et du poulet."),("B","Très bien. Et comme boisson ?"),("A","De l'eau, merci.")],"A: Good evening. A table for two, please. B: Of course. Here is the menu. A: What do you recommend? B: The soup and chicken are excellent. A: Perfect. I would like the soup and some chicken. B: Very good. And to drink? A: Water, thank you.")
],
"exercises":[("Choose the partitive article: ___ eau.", ["du", "de la", "de l'", "des"], 2, "Eau begins with a vowel sound, so use de l'eau."),("Which sentence expresses a general preference?", ["Je bois du café", "J'aime le café", "Je prends du café", "Je voudrais du café"], 1, "Use the definite article when expressing a general like: J'aime le café."),("Complete the negative sentence: Je ne mange pas ___ viande.", ["de", "du", "la", "des"], 0, "Partitive or indefinite articles usually become de after a negative."),("Which meal word is commonly used in Quebec for the evening meal?", ["déjeuner", "dîner", "souper", "goûter"], 2, "Souper is common Canadian French usage for the evening meal.")],
"speaking":[
"Name your usual breakfast, lunch and evening meal using natural French meal names.",
"Order a drink, a main dish and a side using je voudrais and s'il vous plaît.",
"Make five sentences with du, de la, de l' and des.",
"Change positive food sentences into negative sentences and apply de/d'.",
"Role-play a café visit from entering to paying the bill."
],
"summary":[
"Use partitive articles for unspecified amounts: du, de la, de l' and des.",
"Use definite articles with general likes and dislikes: J'aime le café.",
"After negation, partitives usually become de or d'; aimer keeps the definite article.",
"Je voudrais is a polite way to order.",
"Quebec meal names often use déjeuner for breakfast, dîner for lunch and souper for supper."
]
},
14: {
"vocabulary":[
("se lever","to get up","suh luh-vay","/sə lə.ve/","Je me lève à sept heures."),
("se réveiller","to wake up","suh ray-vay-yay","/sə ʁe.ve.je/","Elle se réveille tôt."),
("se laver","to wash oneself","suh lah-vay","/sə la.ve/","Nous nous lavons."),
("s'habiller","to get dressed","sah-bee-yay","/sa.bi.je/","Il s'habille rapidement."),
("prendre","to take; have (meal)","prahn-druh","/pʁɑ̃dʁ/","Je prends le bus."),
("faire","to do; make","fair","/fɛʁ/","Nous faisons du sport."),
("aller","to go","ah-lay","/a.le/","Tu vas à l'école."),
("venir","to come","vuh-neer","/və.niʁ/","Ils viennent demain."),
("partir","to leave","par-teer","/paʁ.tiʁ/","Je pars à huit heures."),
("arriver","to arrive","ah-ree-vay","/a.ʁi.ve/","Le train arrive."),
("étudier","to study","ay-tü-dee-yay","/e.ty.dje/","Elle étudie le français."),
("travailler","to work","trah-vah-yay","/tʁa.va.je/","Je travaille le lundi."),
("manger","to eat","mahn-zhay","/mɑ̃.ʒe/","Nous mangeons ensemble."),
("boire","to drink","bwahr","/bwaʁ/","Vous buvez de l'eau."),
("lire","to read","leer","/liʁ/","Il lit un livre."),
("écrire","to write","ay-kreer","/e.kʁiʁ/","J'écris un message."),
("regarder","to watch; look at","ruh-gar-day","/ʁə.ɡaʁ.de/","Je regarde un film."),
("écouter","to listen","ay-koo-tay","/e.ku.te/","Elle écoute la radio."),
("dormir","to sleep","dor-meer","/dɔʁ.miʁ/","Les enfants dorment.")
],
"grammar":[
("Regular -ER verbs in the present","For most regular -ER verbs, remove -er and add -e, -es, -e, -ons, -ez, -ent: parler → je parle, tu parles, il parle, nous parlons, vous parlez, ils parlent. The -ent ending is silent. The singular forms often sound alike, so the subject pronoun is important."),
("Common irregular verbs: aller, faire, prendre and venir","These high-frequency verbs do not follow the regular -ER pattern. Learn each complete set: aller (vais, vas, va, allons, allez, vont); faire (fais, fais, fait, faisons, faites, font); prendre (prends, prends, prend, prenons, prenez, prennent); venir (viens, viens, vient, venons, venez, viennent). Use them in meaningful sentences every day."),
("Reflexive verbs and daily routines","A reflexive verb describes an action done to oneself. The reflexive pronoun changes with the subject: je me lève, tu te lèves, il se lève, nous nous levons, vous vous levez, ils se lèvent. Before a vowel, me, te and se shorten to m', t' and s': je m'habille. The pronoun belongs before the conjugated verb."),
("Negation with reflexive verbs","In a negative reflexive sentence, ne comes before the reflexive pronoun and pas after the conjugated verb: Je ne me lève pas tôt; Elle ne s'habille pas rapidement. In casual speech the ne may disappear, but the full form is best for writing and careful speech."),
("Present tense for habits and current actions","The present tense can describe a routine (Je travaille le lundi), something happening now (Je travaille maintenant) or a general fact (L'eau bout à 100 degrés). Add time and frequency expressions to make the intended meaning clear: tous les jours, le matin, souvent, parfois, rarement."),
("Making a simple connected paragraph","Connect routine actions with puis, ensuite, après, avant and enfin. For example: Je me réveille à sept heures. Ensuite, je me lève et je prends le petit-déjeuner. Puis, je pars au travail. Use the same subject consistently and avoid translating English word order mechanically.")
],
"expressions":[
("tous les jours","every day","Describe a daily habit."),
("d'abord… ensuite… enfin…","first… next… finally…","Organise a sequence."),
("Je suis en train de…","I am in the middle of…","Emphasises an action in progress."),
("Je rentre à la maison.","I return home.","Common routine expression."),
("Ça dépend.","It depends.","Natural response about routines."),
("après le travail","after work","Time phrase.")
],
"examples":[
("Je me réveille à six heures, puis je me lève.","I wake up at six, then I get up.","Two reflexive routine verbs."),
("Nous prenons le bus et nous arrivons au travail à huit heures.","We take the bus and arrive at work at eight.","Prendre and arriver in the present."),
("Elle étudie le français tous les soirs.","She studies French every evening.","Regular -ER verb with elle."),
("Ils ne se couchent pas tard pendant la semaine.","They do not go to bed late during the week.","Negation surrounds the reflexive verb phrase."),
("Le samedi, je fais du sport et je retrouve mes amis.","On Saturdays, I exercise and meet my friends.","Faire du sport is a fixed expression."),
("Après le dîner, nous lisons ou nous regardons un film.","After dinner, we read or watch a film.","Present tense describes routine activities.")
],
"conversations":[
("Talking about a daily routine",[("A","À quelle heure tu te réveilles ?"),("B","Je me réveille à six heures et demie."),("A","Qu'est-ce que tu fais ensuite ?"),("B","Je me lève, je me lave et je prends le petit-déjeuner."),("A","Tu pars au travail à quelle heure ?"),("B","Je pars à huit heures.")],"A: What time do you wake up? B: I wake up at 6:30. A: What do you do next? B: I get up, wash and have breakfast. A: What time do you leave for work? B: I leave at eight."),
("Making weekend plans",[("A","Qu'est-ce que tu fais samedi ?"),("B","Le matin, je fais les courses."),("A","Et l'après-midi ?"),("B","Je retrouve des amis et nous regardons un film."),("A","Tu veux prendre un café dimanche ?"),("B","Oui, avec plaisir !")],"A: What are you doing Saturday? B: In the morning, I do the shopping. A: And in the afternoon? B: I meet friends and we watch a film. A: Would you like to have coffee on Sunday? B: Yes, gladly!")
],
"exercises":[("Choose the correct -ER form: Nous ___ français.", ["parle", "parles", "parlons", "parlent"], 2, "The nous ending for regular -ER verbs is -ons: nous parlons."),("Complete: Je ___ à sept heures.", ["me lève", "te lèves", "se lève", "nous levons"], 0, "With je, the reflexive pronoun is me: je me lève."),("Choose the correct form of aller: Ils ___ à l'école.", ["allez", "allons", "vont", "va"], 2, "The ils/elles form of aller is vont."),("Choose the correct negative reflexive sentence.", ["Je ne me lève pas tôt", "Je me ne lève pas tôt", "Je ne lève me pas tôt", "Je me lève ne pas tôt"], 0, "Ne comes before the reflexive pronoun; pas follows the conjugated verb.")],
"speaking":[
"Describe your morning routine with at least six present-tense verbs.",
"Conjugate parler, étudier and travailler for all six subject forms.",
"Practise aller, faire, prendre and venir in short sentences.",
"Describe a routine using three reflexive verbs and make one sentence negative.",
"Speak for one minute about a weekday and a weekend day, using sequence words."
],
"summary":[
"Regular -ER verbs use -e, -es, -e, -ons, -ez and -ent endings.",
"Memorise common irregular verbs such as aller, faire, prendre and venir.",
"Reflexive verbs use me, te, se, nous, vous and se before the verb.",
"Use the present tense for routines, current actions and general facts.",
"Connect activities with d'abord, ensuite, puis, après and enfin."
]
},
15: {
"vocabulary":[
("réviser","to revise; review","ray-vee-zay","/ʁe.vi.ze/","Je révise mes leçons."),
("comprendre","to understand","kohn-prahn-druh","/kɔ̃.pʁɑ̃dʁ/","Je comprends la question."),
("répéter","to repeat","ray-pay-tay","/ʁe.pe.te/","Pouvez-vous répéter ?"),
("expliquer","to explain","ex-plee-kay","/ɛks.pli.ke/","Le professeur explique la règle."),
("la réponse","answer (f.)","lah ray-pohns","/la ʁe.pɔ̃s/","La réponse est correcte."),
("la question","question (f.)","lah kes-tyohn","/la kɛs.tjɔ̃/","Je comprends la question."),
("correct / correcte","correct","koh-rekt","/kɔ.ʁɛkt/","C'est une réponse correcte."),
("faux / fausse","false; incorrect","foh / fohs","/fo/","Cette réponse est fausse."),
("facile","easy","fah-seel","/fa.sil/","L'exercice est facile."),
("difficile","difficult","dee-fee-seel","/di.fi.sil/","La prononciation est difficile."),
("la leçon","lesson","lah luh-sohn","/la lə.sɔ̃/","La leçon est terminée."),
("le progrès","progress","luh pro-gray","/lə pʁɔ.ɡʁɛ/","Je vois mes progrès.")
],
"grammar":[
("Build a complete self-introduction","Combine the A1 structures in a natural order: greeting, name, origin, residence, languages, age and a closing phrase. Example structure: Bonjour, je m'appelle… Je viens de… J'habite à… Je parle… J'apprends… Use a connector such as et or mais to make the introduction flow."),
("Choose être or avoir accurately","Être describes identity, nationality, condition and many locations: Je suis étudiant; Elle est canadienne. Avoir describes possession, age and fixed feelings: J'ai un frère; J'ai vingt ans; J'ai faim. Do not translate English 'to be' mechanically; learn the French expression."),
("Articles, gender and adjective agreement together","A complete noun phrase must keep its parts consistent: un petit livre rouge, une grande maison blanche, des voitures noires. Choose the article from noun gender and number, then make adjectives agree. Remember that colour adjectives usually follow the noun."),
("Present-tense sentence building","A simple French sentence usually follows subject + conjugated verb + complement: Je parle français; Nous habitons à Luanda. Add a time phrase at the beginning or end: Le matin, je prends le bus. In a negative sentence, place ne before the verb and pas after it."),
("Questions and useful question words","Use est-ce que or rising intonation for yes/no questions. Learn qui (who), que/qu'est-ce que (what), où (where), quand (when), comment (how), pourquoi (why) and combien (how much/many). Match the question word to the information you need: Où habites-tu ?; Pourquoi apprends-tu le français ?"),
("Canadian French foundations and regional awareness","The grammar taught so far is broadly understood French. In Quebec, you will hear everyday words and expressions that may differ from France, such as souper for the evening meal and courriel for email. Learn the standard forms first, then notice local vocabulary and pronunciation without assuming every speaker uses exactly the same expressions.")
],
"expressions":[
("Je suis en train d'apprendre.","I am in the process of learning.","Describe current learning."),
("Pouvez-vous parler plus lentement ?","Can you speak more slowly?","Ask for a slower pace politely."),
("Je n'ai pas compris.","I didn't understand.","Ask for clarification."),
("Comment dit-on… en français ?","How do you say… in French?","Ask for a translation."),
("Je voudrais pratiquer.","I would like to practise.","State a learning goal."),
("Petit à petit.","Little by little.","Encouraging expression.")
],
"examples":[
("Bonjour, je m'appelle Sara. Je viens d'Angola et j'habite à Luanda.","Hello, my name is Sara. I'm from Angola and I live in Luanda.","Greeting, name, origin and residence."),
("J'ai vingt ans et je suis étudiante.","I am twenty and I am a student.","Avoir for age; être for identity."),
("Ma famille est grande et nous sommes très proches.","My family is large and we are very close.","Agreement and être."),
("Le samedi, je fais les courses et je prépare le dîner.","On Saturdays, I shop and prepare dinner.","Present-tense routine."),
("Je voudrais de l'eau, mais je ne veux pas de café.","I would like water, but I don't want coffee.","Polite request and negative article."),
("À quelle heure commence le cours et où est la salle ?","What time does the class start and where is the room?","Two question patterns in one exchange.")
],
"conversations":[
("A complete beginner introduction",[("A","Bonjour ! Comment vous appelez-vous ?"),("B","Je m'appelle Amélie. Et vous ?"),("A","Je m'appelle David. Vous venez d'où ?"),("B","Je viens du Canada, mais j'habite à Luanda."),("A","Vous parlez quelles langues ?"),("B","Je parle anglais et j'apprends le français."),("A","Enchanté !"),("B","Enchantée !")],"A: Hello! What is your name? B: My name is Amélie. And you? A: My name is David. Where are you from? B: I'm from Canada, but I live in Luanda. A: What languages do you speak? B: I speak English and I'm learning French. A: Nice to meet you! B: Nice to meet you!"),
("A practical day in Quebec",[("A","Bonjour. Une table pour deux, s'il vous plaît."),("B","Bien sûr. Vous désirez quelque chose à boire ?"),("A","De l'eau et deux cafés, merci."),("B","Et pour manger ?"),("A","Je voudrais une soupe et un sandwich."),("B","Parfait. Je vous apporte ça tout de suite."),("A","Merci beaucoup !")],"A: Hello. A table for two, please. B: Of course. Would you like something to drink? A: Water and two coffees, thank you. B: And to eat? A: I would like a soup and a sandwich. B: Perfect. I'll bring that right away. A: Thank you very much!")
],
"exercises":[("Choose the correct sentence for age and identity.", ["Je suis vingt ans et j'ai étudiant", "J'ai vingt ans et je suis étudiant", "Je suis vingt ans et je suis étudiant", "J'ai vingt ans et j'ai étudiant"], 1, "Use avoir for age and être for identity."),("Choose the correct noun phrase.", ["une grand maison blanche", "une grande maison blanc", "une grande maison blanche", "un grande maison blanche"], 2, "Maison is feminine; grande and blanche both agree."),("Choose the correct routine sentence.", ["Le lundi, je travaille.", "Le lundi, je travailles.", "À lundi, je travaille.", "En lundi, je travaille."], 0, "Le + weekday expresses a repeated routine. The subject je takes travaille, not travailles."),("Which is the polite request in a café?", ["Je veux un café", "Je voudrais un café", "Je suis un café", "J'ai un café"], 1, "Je voudrais is a polite way to order.")],
"speaking":[
"Give a one-minute introduction using name, age, origin, residence, languages and one personal detail.",
"Describe your family and two people using possessives and adjective agreement.",
"Explain your weekday routine using present-tense and reflexive verbs.",
"Role-play ordering food in a Quebec café and asking for the bill.",
"Ask and answer ten questions using qui, quoi, où, quand, comment, pourquoi and combien."
],
"summary":[
"You can greet people, introduce yourself and exchange personal information.",
"You can use numbers, dates, time and common daily expressions.",
"You can choose articles, recognise noun gender and make basic adjective agreements.",
"You can use être and avoir in common present-tense patterns.",
"You can describe family, colours, food and everyday routines.",
"You can ask basic questions, order politely and recognise selected Quebec vocabulary."
]
}
}

def build_lesson(lesson_id):
    source = LESSON_DATA[lesson_id]
    expansion = LESSON_EXPANSIONS.get(lesson_id, {})
    # Expansion content can intentionally refine an original entry; keep the
    # latest version of each French headword so generated quizzes do not repeat it.
    vocabulary_by_term = {}
    for entry in source["vocab"] + expansion.get("vocabulary", []):
        vocabulary_by_term[entry[0].strip().casefold()] = entry
    vocab = list(vocabulary_by_term.values())
    grammar = source["grammar"] + expansion.get("grammar", [])
    expressions = source["expressions"] + expansion.get("expressions", [])
    examples = source["examples"] + expansion.get("examples", [])
    conversations = source["conversations"] + expansion.get("conversations", [])
    speaking = source["speaking"] + expansion.get("speaking", [])
    summary = source["summary"] + expansion.get("summary", [])
    question_bank = _make_questions(vocab, len(vocab) * 2)
    exercises = question_bank[:12] + expansion.get("exercises", [])
    assessment = question_bank[12:]
    return {
        "id": lesson_id,
        "title": source["title"],
        "goal": source["goal"],
        "vocabulary": vocab,
        "grammar": grammar,
        "expressions": expressions,
        "examples": examples,
        "conversations": conversations,
        "exercises": exercises,
        "speaking": speaking,
        "summary": summary,
        "assessment": assessment,
    }

A1_LESSONS = {lesson_id: build_lesson(lesson_id) for lesson_id in LESSON_DATA}
