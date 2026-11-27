"""A2 authored lessons for Learn Language Academy by Parth.

Lessons are added progressively. Each chapter follows the nine-part teaching format.
"""
LESSON_DATA = {
16: {
"title": "Regular -ER, -IR and -RE Verbs",
"goal": "Recognise three major regular verb families and conjugate common verbs in the present tense to describe everyday actions.",
"vocab": [
("parler","to speak","par-lay","/paʁ.le/","Je parle français."),
("aimer","to like; to love","eh-may","/e.me/","J'aime la musique."),
("habiter","to live; to reside","ah-bee-tay","/a.bi.te/","Nous habitons à Montréal."),
("travailler","to work","trah-vah-yay","/tʁa.va.je/","Elle travaille le samedi."),
("étudier","to study","ay-tü-dee-yay","/e.ty.dje/","Vous étudiez le français."),
("regarder","to watch; to look at","ruh-gar-day","/ʁə.ɡaʁ.de/","Ils regardent un film."),
("finir","to finish","fee-neer","/fi.niʁ/","Je finis mes devoirs."),
("choisir","to choose","shwah-zeer","/ʃwa.ziʁ/","Tu choisis un livre."),
("réussir","to succeed; to pass","ray-ü-seer","/ʁe.y.siʁ/","Elle réussit son examen."),
("grandir","to grow","grahn-deer","/ɡʁɑ̃.diʁ/","Les enfants grandissent vite."),
("remplir","to fill","rahn-pleer","/ʁɑ̃.pliʁ/","Nous remplissons le formulaire."),
("vendre","to sell","vahn-druh","/vɑ̃dʁ/","Ils vendent leur voiture."),
("attendre","to wait","ah-tahn-druh","/a.tɑ̃dʁ/","J'attends l'autobus."),
("répondre","to answer","ray-pohn-druh","/ʁe.pɔ̃dʁ/","Vous répondez à la question."),
("perdre","to lose","pehr-druh","/pɛʁdʁ/","Il perd ses clés."),
("entendre","to hear","ahn-tahn-druh","/ɑ̃.tɑ̃dʁ/","J'entends la radio."),
("une terminaison","ending","ün tair-mee-nay-zohn","/yn tɛʁ.mi.ne.zɔ̃/","La terminaison change selon le sujet."),
("un infinitif","infinitive","uhn an-fee-nee-teef","/œ̃ ɛ̃.fi.ni.tif/","Parler est un infinitif."),
("un sujet","subject","uhn sü-zhay","/œ̃ sy.ʒɛ/","Le sujet est nous."),
("une conjugaison","conjugation","ün kohn-zhü-gay-zohn","/yn kɔ̃.ʒy.ɡe.zɔ̃/","La conjugaison de finir est régulière.")
],
"grammar": [
("What makes a verb regular?","A regular verb follows a predictable pattern when its ending changes to match the subject. The infinitive is the dictionary form: parler, finir or vendre. Remove the infinitive ending (-er, -ir or -re), then add the endings for the subject. Regular patterns are useful, but not every verb ending in these letters is regular. Learn the verb family as well as the infinitive."),
("Regular -ER verbs: the largest family","For a typical regular -ER verb, remove -er and add -e, -es, -e, -ons, -ez, -ent. Parler becomes je parle, tu parles, il/elle parle, nous parlons, vous parlez, ils/elles parlent. The final -ent is silent. The je, tu, il/elle and ils/elles forms often sound identical, so the subject pronoun carries important information."),
("Regular -IR verbs with -issons","Many regular -IR verbs use -is, -is, -it, -issons, -issez, -issent. Finir becomes je finis, tu finis, il finit, nous finissons, vous finissez, ils finissent. The -iss- in the nous, vous and ils/elles forms is a useful clue. Not every infinitive ending in -ir follows this pattern: partir and venir are irregular and will be studied separately."),
("Regular -RE verbs","For a typical regular -RE verb, remove -re and add -s, -s, no ending, -ons, -ez, -ent. Vendre becomes je vends, tu vends, il vend, nous vendons, vous vendez, ils vendent. Notice that the third-person singular form has no written ending after the stem. The final consonants are often silent, so several forms may sound alike."),
("The three patterns side by side","Compare parler: je parle / nous parlons; finir: je finis / nous finissons; vendre: je vends / nous vendons. The endings are different, especially in the plural. Identify the infinitive first, choose its verb family, then attach the correct subject ending. Do not choose an ending based only on the English meaning."),
("Subject pronouns and verb agreement","The verb must agree with its subject: Marie parle, mes amis parlent, and vous parlez. A noun subject can replace a pronoun, but it still controls the verb form. A single person or thing uses il/elle; a group uses ils/elles. Vous takes the vous form whether it means one person politely or several people."),
("Negation with regular verbs","Place ne before the conjugated verb and pas after it: Je ne parle pas allemand; Nous ne finissons pas tard; Il ne vend pas sa maison. Before a vowel sound, ne becomes n': Je n'écoute pas. In casual speech, many speakers omit ne, but learn and use the complete form in careful writing and formal situations."),
("Questions with regular verbs","You can ask a yes/no question with rising intonation (Tu travailles ?) or est-ce que (Est-ce que tu travailles ?). You can also use inversion in more formal speech: Travaillez-vous ? For an information question, place a question word at the beginning: Où habitez-vous ? / Pourquoi choisissent-ils ce cours ? Keep the verb ending matched to the subject."),
("Spelling changes are not the same as irregular conjugation","Some common -ER verbs make small spelling adjustments to preserve pronunciation, such as manger (nous mangeons) and commencer (nous commençons). These are spelling changes within otherwise regular patterns. This lesson focuses on the core patterns; learn each spelling adjustment with its verb rather than applying a new ending blindly."),
("Canadian French note: clear forms and everyday speech","The conjugation patterns in this lesson are shared across French-speaking regions, including Quebec and other Canadian communities. In fast informal speech, subject pronouns and sounds may be reduced, but the written verb forms remain the same. Build accurate full sentences first; later lessons will introduce more conversational contractions and regional pronunciation.")
],
"expressions": [
("Qu'est-ce que tu fais ?","What are you doing? / What do you do?","A common question about an activity or routine."),
("Je travaille à temps plein.","I work full-time.","Temps plein means full-time."),
("Je finis à cinq heures.","I finish at five o'clock.","Useful for talking about a schedule."),
("Je choisis celui-ci.","I'll choose this one.","Celui-ci means this one; the demonstrative pronoun is introduced here as a useful phrase."),
("Ça dépend.","It depends.","A natural short response."),
("Je ne sais pas.","I don't know.","A frequent everyday expression."),
("Tu peux répéter ?","Can you repeat?","Informal request; polite form: Vous pouvez répéter ?"),
("Je suis d'accord.","I agree.","Useful in everyday conversation."),
("Je préfère rester ici.","I prefer to stay here.","Préférer is a common -ER verb with an accent change."),
("À quelle heure tu finis ?","What time do you finish?","Common spoken word order; formal: À quelle heure finissez-vous ?")
],
"examples": [
("Je parle anglais et j'étudie le français.","I speak English and study French.","Parler and étudier are regular -ER verbs; je takes -e."),
("Nous parlons avec le professeur.","We speak with the teacher.","Nous takes -ons in the regular -ER pattern."),
("Vous regardez souvent des films ?","Do you often watch films?","Vous takes -ez; rising intonation makes this a question."),
("Elle finit ses devoirs avant le dîner.","She finishes her homework before dinner.","Finir is a regular -IR verb; elle finit."),
("Nous choisissons un restaurant près d'ici.","We choose a restaurant near here.","Choisir uses -issons with nous."),
("Les enfants grandissent rapidement.","The children grow quickly.","Grandir uses -issent with ils/elles."),
("Je vends mon ancien vélo.","I am selling my old bicycle.","Vendre is a regular -RE verb; je vends."),
("Ils attendent l'autobus devant l'école.","They are waiting for the bus in front of the school.","Attendre uses -ent with ils; the ending is silent."),
("Tu ne réponds pas à la question.","You are not answering the question.","Negation surrounds the conjugated verb."),
("Est-ce que vous choisissez cette couleur ?","Are you choosing this colour?","Est-ce que introduces a yes/no question.")
],
"conversations": [
("Talking about a language class", [("A","Tu étudies le français depuis longtemps ?"),("B","Non, j'étudie depuis quelques mois."),("A","Tu comprends les verbes ?"),("B","Oui, mais je finis encore mes exercices lentement."),("A","Nous choisissons un sujet pour pratiquer ?"),("B","Bonne idée !")], "A: Have you been studying French for a long time? B: No, I've been studying for a few months. A: Do you understand the verbs? B: Yes, but I still finish my exercises slowly. A: Shall we choose a topic to practise? B: Good idea!"),
("At a small shop", [("A","Bonjour. Vous vendez des cahiers ?"),("B","Oui. Nous vendons plusieurs modèles."),("A","Je cherche un cahier bleu."),("B","Vous choisissez celui-ci ?"),("A","Oui, merci. Je prends aussi deux stylos."),("B","Parfait. Ça fait huit dollars.")], "A: Hello. Do you sell notebooks? B: Yes. We sell several styles. A: I'm looking for a blue notebook. B: Are you choosing this one? A: Yes, thank you. I'll also take two pens. B: Perfect. That comes to eight dollars."),
("Making plans after work", [("A","À quelle heure tu finis aujourd'hui ?"),("B","Je finis à cinq heures."),("A","Tu attends l'autobus ou tu marches ?"),("B","J'attends l'autobus. Et toi ?"),("A","Je marche. On se retrouve au café ?"),("B","Oui, avec plaisir !")], "A: What time do you finish today? B: I finish at five. A: Are you waiting for the bus or walking? B: I'm waiting for the bus. And you? A: I'm walking. Shall we meet at the café? B: Yes, gladly!"),
],
"exercises": [
("Choose the correct form: Nous ___ français en classe.", ["parle","parles","parlons","parlez"], 2, "Nous takes -ons with a regular -ER verb: nous parlons."),
("Complete: Tu ___ tes devoirs.", ["finis","finit","finissons","finissez"], 0, "Tu takes -is in the regular -IR pattern: tu finis."),
("Choose the correct form: Elles ___ leurs vieux livres.", ["vend","vends","vendez","vendent"], 3, "Elles takes -ent with a regular -RE verb: elles vendent."),
("Which is the correct nous form of choisir?", ["choisissons","choisont","choisisez","choisissent"], 0, "Regular -IR verbs such as choisir use -issons with nous."),
("Complete: Il ___ à la question.", ["réponds","répond","répondez","répondent"], 1, "The il form of répondre is répond; there is no extra ending after the stem."),
("Choose the correct negative sentence.", ["Je ne parle pas espagnol.","Je parle ne pas espagnol.","Je ne pas parle espagnol.","Je pas ne parle espagnol."], 0, "Ne comes before the conjugated verb and pas after it."),
("Which infinitive belongs to the regular -IR pattern taught here?", ["partir","venir","finir","dormir"], 2, "Finir follows the -is, -is, -it, -issons, -issez, -issent pattern."),
("Choose the correct vous form: Vous ___ la télévision.", ["regardons","regardez","regardent","regarde"], 1, "The vous ending for regular -ER verbs is -ez."),
("Complete: Les étudiants ___ leurs exercices.", ["finit","finis","finissent","finissez"], 2, "Les étudiants is plural, so use the ils/elles form finissent."),
("Which sentence uses the regular -RE pattern correctly?", ["Nous vendons des livres.","Nous vendez des livres.","Nous vendent des livres.","Nous vendre des livres."], 0, "Nous takes -ons in the regular -RE pattern: nous vendons."),
("Choose the correct subject-verb agreement.", ["Marie et Paul parle.","Marie et Paul parlent.","Marie et Paul parlons.","Marie et Paul parlez."], 1, "Two people form a plural subject: ils parlent."),
("Which question is correctly formed with est-ce que?", ["Est-ce que tu travailles ?","Est-ce tu que travailles ?","Est-ce que travailles tu ?","Que est-ce tu travailles ?"], 0, "Place est-ce que before the subject and conjugated verb."),
("Complete: Je ___ mes clés. (perdre)", ["perds","perd","perdez","perdent"], 0, "The je form of perdre is je perds."),
("Choose the correct sentence for 'We do not finish late.'", ["Nous ne finissons pas tard.","Nous ne pas finissons tard.","Nous finissons ne pas tard.","Nous pas finissons ne tard."], 0, "Use ne + conjugated verb + pas."),
("Which sentence describes a repeated routine?", ["Le lundi, je travaille.","Le lundi, je travailles.","Le lundi, je travailler.","Le lundi, je travaillons."], 0, "Je takes the -e ending: je travaille."),
("Choose the correct form: Vous ___ à la question. (répondre)", ["réponds","répond","répondez","répondent"], 2, "The vous form of répondre is répondez.")
],
"speaking": [
"Conjugate parler aloud with all six subject pronouns. Keep the subject pronoun clear because several forms sound alike.",
"Repeat the same drill with finir and vendre. Notice the -issons family in finir and the -ons plural form in vendre.",
"Describe your weekday using at least six regular verbs: study, work, watch, finish, choose and wait.",
"Say five negative sentences using ne…pas. Keep ne before the verb and pas after it.",
"Ask and answer five questions with est-ce que, then repeat them using rising intonation.",
"Read the three conversations aloud, switching roles. Aim for a connected rhythm rather than stressing every word equally.",
"Make a short comparison: what do you do on weekdays, and what do your friends or family do?",
"Canadian French awareness: listen for the same verb endings in Quebec speech, even when the surrounding pronunciation is faster or more informal."
],
"summary": [
"Regular -ER verbs use -e, -es, -e, -ons, -ez, -ent.",
"Many regular -IR verbs such as finir use -is, -is, -it, -issons, -issez, -issent.",
"Typical regular -RE verbs use -s, -s, no ending, -ons, -ez, -ent.",
"Choose the verb family from the infinitive, then match the ending to the subject.",
"Use ne…pas around the conjugated verb for a standard negative sentence.",
"Form questions with rising intonation, est-ce que or inversion.",
"Some verbs have spelling adjustments or irregular forms; do not assume every -ir or -re verb is regular."
],
"assessment": [
("What is the infinitive form of a verb?", ["The dictionary form","The past participle","The plural form","The negative form"], 0, "The infinitive is the basic dictionary form, such as parler or finir."),
("Choose the correct je form of parler.", ["je parles","je parle","je parlons","je parlent"], 1, "A regular -ER verb uses -e with je: je parle."),
("Choose the correct nous form of finir.", ["nous finons","nous finissons","nous finissez","nous finissent"], 1, "Regular -IR verbs such as finir use -issons with nous."),
("Choose the correct ils form of vendre.", ["ils vends","ils vend","ils vendez","ils vendent"], 3, "Regular -RE verbs use -ent with ils/elles."),
("Which ending belongs to vous with a regular -ER verb?", ["-e","-es","-ez","-ent"], 2, "The vous ending is -ez."),
("Which form is correct for elle + choisir?", ["elle choisit","elle choisissons","elle choisissez","elle choisissent"], 0, "Elle takes -it in the regular -IR pattern."),
("Choose the correct nous form of vendre.", ["nous vendons","nous vendez","nous vendent","nous vends"], 0, "Nous takes -ons in the regular -RE pattern."),
("Which sentence is correct?", ["Les enfants grandit.","Les enfants grandissent.","Les enfants grandissons.","Les enfants grandissez."], 1, "Les enfants is plural, so use grandissent."),
("Complete: Tu ___ la radio. (écouter)", ["écoutes","écoute","écoutons","écoutez"], 0, "Tu takes -es with a regular -ER verb."),
("Choose the correct third-person singular form of répondre.", ["il réponds","il répond","il répondez","il répondent"], 1, "The third-person singular regular -RE form has no ending after the stem."),
("Which verb is a regular -IR example in this lesson?", ["venir","partir","finir","dormir"], 2, "Finir follows the regular -IR pattern taught here."),
("Choose the correct negative form.", ["Elle ne vend pas sa voiture.","Elle vend ne pas sa voiture.","Elle ne pas vend sa voiture.","Elle pas vend ne sa voiture."], 0, "Ne precedes the conjugated verb and pas follows it."),
("Which question is correctly formed?", ["Est-ce que vous choisissez ?","Est-ce vous que choisissez ?","Est-ce que choisissez vous ?","Que est-ce vous choisissez ?"], 0, "Est-ce que comes before the subject."),
("Complete: Nous ___ à Montréal. (habiter)", ["habitez","habitent","habitons","habite"], 2, "Nous takes -ons in the regular -ER pattern."),
("Choose the correct form: Ils ___ l'autobus. (attendre)", ["attends","attend","attendez","attendent"], 3, "Ils takes -ent in the regular -RE pattern."),
("Which statement about -ent in ils parlent is correct?", ["It is normally silent","It is pronounced like English ent","It changes to -ez","It is always a separate syllable"], 0, "The -ent ending is silent in the present tense."),
("Choose the correct subject-verb agreement.", ["Vous travaille","Vous travailles","Vous travaillez","Vous travaillent"], 2, "Vous takes -ez with a regular -ER verb."),
("Which sentence means 'I am not answering'?", ["Je ne réponds pas.","Je ne répond pas.","Je pas réponds.","Je réponds ne pas."], 0, "Je réponds is the first-person form; ne…pas surrounds the verb."),
("What is the correct form for 'we finish'?", ["Nous finissent","Nous finissons","Nous finissez","Nous finis"], 1, "Nous finissons is the correct first-person plural form."),
("Which is the safest way to conjugate a new verb?", ["Guess from the English meaning","Identify its infinitive family and match the subject ending","Always add -ent","Use the same ending for every subject"], 1, "Identify the verb family first, then choose the ending for the subject.")
]
}
A2_LESSONS = {lesson_id: data for lesson_id, data in LESSON_DATA.items()}
