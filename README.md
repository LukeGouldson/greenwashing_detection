# Project Notes

## Literature Review Summary

Identifying greenwashing is a small subset of NLP research which has hitherto been largely disconnected due to the fundamental difficulty of defining the term greenwashing. In spite of this difficulty, current research has focused on intermediary stages and resulted in the creation of several tools. There are many transformer architectures which are domain-specific to climate-related texts, such as climateBERT. They exhibit improvements over general-purpose models on downstream tasks such as sentiment analysis. 

(1) Engages in a systematic review of all NLP attempts to detect greenwashing. The three areas of difficulty are: 1) the lack of coherent definition 2) there are significant legal and reputational consequences of being accused of greenwashing 3) there is no 'jurisprudence' for greenwashing that would allow for labelling of data

A formal definition for greenwashing is proposed by (4) which has not yet been employed in the field of NLP. The definition employs the following six point diagnostic tool:

    If a claim is:
    
    RELATED TO THE ENVIRONMENT/CLIMATE
    MADE BY A FIRM
    MARKETING A PRODUCT/SERVICE TOWARDS CONSUMERS
    UNSUBSTANTIATED
    DECEPTIVE
    PURSUING A COMPETITIVE ADVANTAGE

    Then it warrants an accusation of greenwashing.

Elements of this definition have already been intuited by researchers, but without formality and empirical review. It will bring greater cohesion to research if this definition is brought into the field of NLP.

 Much research has already been focused on diagnosing whether a text is climate-related, thus the first point can be considered solved. Difficulties lie in point 5 due to its inherently subjective nature, and point 4 due to the lack of crossover with existing claim-verification research outside the field of greenwashing.

 There is no dataset consisting of labelled 'greenwashing/not' examples. This is due to its lack of definition. This project, in bringing the definition to the field of NLP, allows for work towards creating such a dataset. There are datasets for point 1, for 'green claims' and for 'verifiable claims'


## Overview

The purpose of this project will be to formally bring this diagnostic tool into NLP, and utilise existing transformer models to apply to its points. The users of this research will be corporations themselves, who should wish to avoid greenwashing and should be encouraged to be transparent about environmental impact, both to the benefit of the environment and their own reputations.

In this way, it is not necessary to address all points in the definition. For example, if the tool is used by firms to assess their own reporting, 'made by a firm' is not relevant. Climate-relatedness has already been heavily researched and is fundamentally solved, but still may be useful for combining datasets. This project will focus on two or three of the other points, ideally those with existing datasets.

Much greenwashing occurs not in textual data, but in images or videos, or even in facts (claims vs actual data). This is beyond the scope of NLP and therefore this project.