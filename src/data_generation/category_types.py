from initial_category import Category, CategoryType

entailment = CategoryType(name='entailment',
                               description='An entailment between two statements (Premise and Hypothesis) occurs when the truth of the hypothesis logically follows from the truth of the premise.\
 In other words, if the premise is true, then the hypothesis must also be true based on the information provided in the premise',
        instances=[Category(premise='The cat is sleeping on the sofa',
                                 hypothesis='The cat is on the sofa')])

neutral = CategoryType(name='neutral',
                               description='a relationship between two text statements (Premise and a Hypothesis) is considered neutral\
 when the truth of the hypothesis neither logically follows from nor contradicts the information provided in the premise.\
 This means that, based on the information in the premise alone, it is impossible to determine whether the hypothesis is true or false',
        instances=[Category(premise='The cat is sleeping on the sofa',
                                 hypothesis='It is raining outside')])

antonym = CategoryType(name='antonym',
                               description='A contradiction based on antonymity means that a contradiction arises\
 between two statements (Premise and Hypothesis) because the hypothesis contains an antonymous word compared to the premise.',
        instances=[Category(premise='Capital punishment is a catalyst for more crime',
                                 hypothesis='Capital punishment is a deterrent to crime')])

negation = CategoryType(name='negation',
                               description='A contradiction based on negation means that a contradiction arises\
 between two statements (Premise and Hypothesis) because a statement from the premise is negated in the hypothesis, or vice versa',
        instances=[Category(premise='A closely divided Supreme Court said that juries and not judges must impose a death sentence',
                                 hypothesis='The Supreme Court decided that only judges can impose the death sentence')])

numeric = CategoryType(name='numeric',
                               description='A contradiction based on a numeric mismatch means that a contradiction arises\
 between two statements (Premise and Hypothesis) because there are mismatching numbers in premise and hypothesis. The contradiction only affects the numerical values and nothing else',
        instances=[Category(premise='The tragedy of the explosion in Qana that killed more than 50 civilians has presented Israel with a dilemma',
                                 hypothesis='An investigation into the strike in Qana found 28 confirmed dead thus far')])

factive_embedded_verb = CategoryType(name='factive_embedding_verb',
                                description='Factive contradiction based on the embedding context has the following characteristics\
 1. There is a mismatch in the embedding context of the verb phrase in the premise and hypothesis which creates the contradictory meaning;\
 2. Contains similar or identical entities in the premise and hypothesis;\
 3. The hypothesis does not contain any negations and any antonyms of the verb phrase of the premise',
        instances=[Category(premise='Sudan accepted U.N. troops in Darfur',
                                hypothesis='Sudan refused to accept U.N. troops'),])

factive_antonym = CategoryType(name='factive_antonym',
                                description='Factive contradiction based on the antonymity of a verb means that a contradiction arises\
 between two statements (Premise and Hypothesis) because the verb phrase in the hypothesis has an opposite or contradictory meaning\
 to the verb phrase in the premise',
        instances=[Category(premise='Sudan refused to allow U.N. troops in Darfur',
                                 hypothesis='Sudan will grant permission for United Nations peacekeeping forces to take up station in Darfur')])

structure = CategoryType(name='structure',
                            description=' A structure contradiction arises from the mismatch in the sentence structure of the premise and hypothesis.\
 The mismatch in the sentence structure has the following characteristics:\
 1. the created hypothesis has the same verb phrase as the premise,\
 2. there are new entities which function as new objects of the same verb in the hypothesis, which creates the contradictory meaning to the meaning of the premise with respect to the premise',
        instances=[Category(premise='The children are smiling and waving at the camera',
                                 hypothesis='The children are smiling and waving to each other')])
        

lexical = CategoryType(name='lexical',
                            description='A lexical contradiction based on the mismatch in the lexical context has the following characteristics:\
 1. the premise and hypothesis have both the same topic or verb subject\
 2. the created hypothesis has a subtly different lexical meaning\
 3. the hypothesis has a contradictory meaning due to the created opposite context of the topic in the premise',
        instances=[Category(premise='Tariq Aziz kept outside the closed circle of Saddam s Sunni Moslem cronies',
                                 hypothesis='Tariq Aziz was in Saddam s inner circle')])

temporal = CategoryType(name='temporal',
                             description = "A temporal contradiction arises when there is an inconsistency between the time frames or chronological events between premise and hypothesis.\
 Hypothetically, if one statement indicates an event happening before another, and the contradictory statement implies the opposite sequence or suggests the events are\
 simultaneous, a temporal mismatch exists",
        instances=[Category(premise="The movie was released two months ago",
                                 hypothesis="The actors are currently filming the sequel")])


wk = CategoryType(name='worldknowledge',
                            description='A contradiction based on the mismatch in world knowledge has the following characteristics:\
 0. the premise contains the well known knowledge about the world\
 1. the facts and knowledge from the hypothesis contradict the world knowledge in the premise',
        instances=[Category(premise='Al-zarqawi was Palestinian',
                                 hypothesis='Al-zarqawi was Jordanian')])