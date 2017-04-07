# About PubMed Topic Modeler

**Table of Contents**
* [Introduction to the project](#Introduction-to-the-project)
* [Latent Semantic Analysis](#Latent-Semantic-Analysis)
* [LSA and it's application to research text](#LSA-and-it's-application-to-research-text)
* [General Schema of the project](### General-Schema-of-the-project)

### Introduction to the project

As an Insight fellow, my main project was [Happy Helper](www.happyhelper.site). This project allowed me to get my start on [natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing)(NLP). There, I did some document classification, specifically of reddit posts from support forums for anxiety and depression.

I want to get deeper into NLP exploring other methods to model linguistic information. One interesting thing to do in NLP try to find latent [topics](https://en.wikipedia.org/wiki/Topic_model) from a set of documents. For example, on a reddit forum for depression, there may exist several latent topics. There might be posts about therapists, there might be post about how someone was feeling that day, there might be posts about how someone has treated their depression. If you are building a large corpora in a specific domain, there may exist sub-domains within the corpus. You could easily sift through the corpus by hand, but that is time consuming. There are machine learning algorithms that will help do this for you.

### Latent Semantic Analysis
[Latent Semantic Analysis](https://en.wikipedia.org/wiki/Latent_semantic_analysis)(LSA) is a method whereby vectorized text data is decomposed to separate matrices using Singular Value Decomposition, which yields topic scores that are linear cominbations of certain words (this is a gross oversimplication). One way to think about LSA is that it is simply principal components analysis for vectorized text. LSA will yield *n-topics* which will show linear combinations of words that contribute to a topic.

### LSA and it's application to research text
I wanted to apply LSA to the straightforward scenario where a researcher may be asked to scrape a number of journal articles, and determine what percentage of articles belong to x,y,z categories.

This is the goal for PubMed Topic Modeler. PubMed Topic Modeler will query PubMed, use various NLP to cleanse the text, and generate topics that are contained within the texts queried.

It is my hope that the topic modeler can provide a better, finer grained, method to categorize abstracts. If not, it's still an interesting little exercise in using PubMed abstracts as a source of information for different NLP and machine learning techniques.

This project was a part of the Insight Computer Science mini-specialization program.

## General Schema of the project

![Alt Text](https://github.com/mjtat/PubMed-Topic-Modeler/blob/master/images/schema.png?raw=true)


**REQUIRED MODULES**
You will need to download `nltk`, `gensim`, and `pandas` to run these scripts. To do that, you can type the following in terminal / console:

`pip install nltk` or `conda install nltk` (if you have Anaconda)

`pip install gensim` or `conda install gensim` (if you have Anaconda)

`pip install gensim` or `conda install gensim` (if you have Anaconda)

`pip install pandas` (pandas is already included in Anaconda)

* pubmed_query.py
* preprocess.py
* topic_modeling.py
* figure_plotting.py
* execute.py

pubmed_query, preprocess, and topic_modeling are placed within the folder. It is not necessary for you to run them unless you choose to. All you need to run is execute.py script.

1. *pubmed_query.py* makes use of the PubMed open-source API, and retrieves abstracts. It also retrieves other information, such as date of publication, and Pubmed IDs (PMID).

* The query process can be invoked with the following syntax: ```pubmed_query(email, terms, author, number_of_articles).return_abstracts()``` It will return a dictionary with all abstracts.

2. *preprocess.py* primarily does data cleaning. It removes low information words, tokenizes, then lemmatizes each word.

* The cleaning process can be invoked with the following syntax: ``` cleaned_text(dict_here).clean() ```. It will return a dictionary of cleaned text, which can be queried as follows: ``` dictionary[key][3] ```

3. *topic_modeling.py* makes use of the `gensim` package to covert text into a large corpora, vectorize the text using term-frequency inverse-document frequency (TF-IDF), and extract topics using latent semantic analysis (also known as latent semantic indexing).


4. *execute.py* is a wrapper that runs all three functions sequentially, such that you do not have to inspect the scripts individually. `execute.py` can also be run on the command line.

**The modeling process can be invoked with the following syntax, specifically from the execute.py file:** ```topic, scores = run_modeler(email, keyword args, number of abstracts to return, number of topics to model)```. Note that email and keywords are strings, and number of abstracts / topics are ints.

**If you want to run it from the command line, here's some example syntax.** ```python execute.py tatinthehat@gmail.com anxiety depression 5 2``` *tatinthehat@gmail.com* is a required email argument, *anxiety depress* are keywords (right now you MUST enter two keywords), *5* is the number of articles to search, and *2* is the number of topics to generate. Below is a screen case of how this works on the command line.

4. *execute.py* is a wrapper that runs all three functions sequentially, such that you do not have to inspect the scripts individually. `execute.py` can also be run on the command line.

**The modeling process can be invoked with the following syntax, specifically from the execute.py file:** ```topic, scores = run_modeler(email, keyword args, number of abstracts to return, number of topics to model)```. Note that email and keywords are strings, and number of abstracts / topics are ints.

**If you want to run it from the command line, here's some example syntax.** ```python execute.py tatinthehat@gmail.com anxiety depression 5 2``` *tatinthehat@gmail.com* is a required email argument, *anxiety depress* are keywords (right now you MUST enter two keywords), *5* is the number of articles to search, and *2* is the number of topics to generate. Below is a screen case of how this works on the command line.


### Terminal Example (click to view)

[![asciicast](https://asciinema.org/a/9gf2fwd157l23dw8poh467kj6.png)](https://asciinema.org/a/9gf2fwd157l23dw8poh467kj6)


### Here's an example of running execute.py in an IDE (Spyder).


```
In [1]: topics, scores = run_modeler('tatinthehat@gmail.com', 'anxiety', 50, 5).execute()

 Successfully retrieved 50 abstracts.

 Successfully cleaned and tokenized abstracts.


            ###########
            # TOPIC 1 #
            ###########


.222*"patient" + -0.173*"depression" + -0.171*"m" + -0.125*"child" + -0.112*"group" + -0.110*"disorder" + -0.109*"epilepsy" + -0.107*"health" + -0.106*"symptom" + -0.104*"control


            ###########
            # TOPIC 2 #
            ###########


360*"child" + 0.210*"irritability" + 0.183*"parent" + -0.172*"patient" + 0.163*"worry" + -0.149*"m" + 0.144*"disorder" + 0.128*"externalizing" + 0.114*"father" + 0.108*"youth


            ###########
            # TOPIC 3 #
            ###########


.230*"pregnancy" + 0.197*"epilepsy" + -0.195*"resident" + -0.191*"sleep" + 0.183*"m" + -0.162*"fear" + -0.138*"woman" + -0.122*"training" + -0.121*"student" + 0.106*"validity


            ###########
            # TOPIC 4 #
            ###########


.252*"m" + 0.194*"pain" + 0.181*"patient" + 0.157*"aromatherapy" + -0.137*"fatigue" + 0.134*"dressing" + -0.127*"life" + 0.125*"resident" + 0.121*"tmj" + 0.120*"burn


            ###########
            # TOPIC 5 #
            ###########


252*"pregnancy" + 0.205*"epilepsy" + 0.200*"sleep" + 0.172*"hads" + 0.157*"=" + -0.154*"student" + 0.153*"item" + 0.131*"woman" + 0.113*"panic" + -0.110*"cancer

5 topics successfully extracted.


        #########################
        # PMIDs by Topic Scores #
        #########################

26760456 [-0.16269468873233456, 0.13170000409084304, -0.077061502163991574, 0.05485085086986357, -0.10245198648905388]
27882638 [-0.19982357242179111, -0.098511768078196962, 0.052945318459882318, -0.070791214352409981, -0.20369555788178917]
26424720 [-0.29365866758270681, 0.40413112454508815, 0.13525149445042811, -0.031783057201560022, 0.073277337800915276]
28289297 [-0.14682160613342821, -0.033709352039959443, -0.2196406250467339, 0.11548905105551635, -0.23880404307742895]
26999442 [-0.23475857955664714, -0.039523388946133838, 0.0012147440004630723, -0.031365002081094426, -0.13948267776742854]
27461268 [-0.2381527223101029, -0.11763635498962295, 0.098742668028078226, 0.021235144549070058, -0.14624906514352695]
26806805 [-0.41110645184665545, -0.25642587379889409, 0.19503619750677981, -0.33326605521631625, -0.14929680917358243]
27555224 [-0.17458065771201225, 0.020542314382916971, 0.0081422286163761754, 0.14109891767097929, -0.003480736063994403]
27852349 [-0.28856297354942939, 0.39896945989259619, -0.090281467074758731, -0.073657981539321932, -0.06972865014936408]
26851749 [-0.16859863495658661, 0.033899233952747194, -0.053471480302243801, -0.15184447508967952, -0.061859990652063566]
26703910 [-0.19422498424365961, 0.44754083394604555, -0.11915584623276404, -0.043722522521951836, -0.077042491609365146]
27984808 [-0.25485852932189113, 0.037398967818635311, 0.28147153967526967, 0.11116112844004254, 0.1903835675087307]
27697449 [-0.19745637021957091, 0.033847687701357904, -0.09814570001369996, -0.099663726585370649, 0.037772753318999396]
26680108 [-0.11180445514982895, 0.031791739826562297, -0.032741250446002429, 0.082422075136444131, 0.033824375552323961]
26306610 [-0.16006906227063686, 0.37596328280927105, -0.070717739384044548, -0.085812542528753227, -0.11301774540480924]
27133235 [-0.13726277803484555, -0.10276724641488709, -0.35537722338867944, 0.19600462642463104, -0.065033556362620926]
27779764 [-0.29233083233687029, -0.19808901551518951, -0.31878863841130234, -0.20018149254684728, 0.46415035301126423]
27219913 [-0.36217067284904031, -0.12400769112201247, 0.30007591708651205, -0.14273444107515279, 0.019794499448406128]
27460276 [-0.20868706417717073, -0.058018454486891399, -0.028040154955297963, -0.065596743758537981, 0.028787085402273496]
27263418 [-0.2168230276873945, -0.16349013894259956, 0.059433371472869145, 0.36128754030042259, -0.034573910886703217]
26756925 [-0.27505228926695774, -0.17459254520528933, 0.15797045019475636, -0.29948642341989845, -0.1965558180600788]
27115070 [-0.16695614266809186, -0.00044119129064418977, -0.34289329006828095, -0.039165173461498351, 0.26121662172257232]
27277894 [-0.20586774263449187, 0.094697533348121532, -0.10000888348043308, -0.12239868445672529, 0.0422638901824774]
27555145 [-0.15872247273638435, -0.078211634338035338, -0.11732795021843839, 0.090837662246658707, -0.042147665746163784]
27582026 [-0.10737566513814896, -0.024772260143126702, -0.048276167980059501, 0.10647154309584249, -0.066974017370638697]
27502925 [-0.11680948093048542, -0.1105215085580081, -0.30759971397119279, 0.20642731608333964, -0.10898432663497287]
26519118 [-0.25878236462508369, -0.13930204321532041, 0.067360591222333677, 0.27560816620582457, -0.037371621501967447]
27861713 [-0.16819096582602044, -0.10469314363069575, -0.36333685961265072, -0.18408385303295799, 0.36385109109709146]
26384978 [-0.175097973347138, 0.17285821913265353, -0.070753723087125034, 0.0074991138256965337, -0.082464509593760379]
27514366 [-0.20136707735264964, -0.11774223946701531, -0.034956342726128652, -0.078061934753936454, -0.071252495441610192]
27166222 [-0.13093336986081655, 0.058705716426332599, -0.021903391744982074, 0.027576619178518707, -0.062935121169162694]
26969819 [-0.18209354852763399, -0.0051769625919299098, 0.00056926049228198659, -0.092517201413238201, -0.052385468350109814]
27760092 [-0.21055212445851992, -0.15163019318454313, -0.033559305431660628, 0.20007976403071381, -0.062159747912419343]
27515871 [-0.15929119217749668, -0.070347503414330076, -0.067865236097998161, 0.17034870114542972, -0.036340079985786283]
27842529 [-0.2400892210038657, 0.12436690717576045, -0.066813511125529884, 0.072890444883453392, -0.14078729186003436]
26695011 [-0.17988649476747787, 0.39157292445016401, -0.12807538862396714, -0.097344275333087593, -0.10655253982335446]
27810788 [-0.11212405496656616, -0.036470467606117253, 0.0011294419169240802, 0.067158699330465393, -0.096526140214700643]
27915110 [-0.2945612724693859, 0.13266501400840489, 0.29268955453862272, 0.057375015188858076, 0.35963464714325399]
27784316 [-0.20922200595891563, -0.045485509898343227, -0.18313404899919278, 0.086400081759860484, -0.26621161861998804]
26978668 [-0.1192349879919547, 0.047748703230863006, -0.084874221288678858, 0.11306659519475337, -0.042939447994637621]
27718424 [-0.11598015871308325, 0.029518340834236677, -0.029223182286603054, 0.044563260802827777, -0.10175565145513543]
26340079 [-0.17690758778622273, 0.065924110158279717, 0.036649467732689206, 0.064220990772193551, -0.034196830025358289]
27692017 [-0.24806020800404122, 0.05812228970889928, 0.081685261326050487, 0.12887379971933446, 0.23166650450839371]
27500660 [-0.21907925631490982, -0.19220778931472554, -0.2539685908562509, -0.21551599417271486, 0.12151776145979931]
27153141 [-0.26135036019843699, -0.13563019230001694, -0.015992233470295235, 0.062723652782889966, 0.23183773785287889]
27575673 [-0.22457132138066818, -0.15473625954085182, 0.085950833718466624, 0.35654151990568073, -0.019059017648826691]
27334010 [-0.23051872680140481, -0.16444112837490829, 0.031486292006676658, 0.19047041627281047, -0.069260780304743072]
27919483 [-0.30807495387565959, -0.16669823205771536, 0.14558384573752106, -0.40459857008007422, -0.21488251279536102]
25847548 [-0.19813026864219918, 0.14680430938542705, -0.10127127823103986, 0.13291234470641466, -0.039248361486841563]
26906494 [-0.319363957045112, 0.16284856806486558, 0.31417947320228784, 0.20355904841278608, 0.31383147212121859]
```

**Additionally, an barplot will be generated, saved in the directory execute.py resides in.** This barplot represents the relative topic score by PubMed article. The query 'anxiety' and num_topics = 5 yields the plot below. Numbers on the legend represent each topic number (from the values printed above). Note the scores are absolute values to interpret the magnitude of the scores more easily.

![Alt Text](https://github.com/mjtat/PubMed-Topic-Modeler/blob/master/images/barplot.png?raw=true)
# PubMed-Topic-Modeler
