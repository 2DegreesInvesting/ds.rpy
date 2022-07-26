
# Using Python from RStudio

The goal of this meetup is to help you to use Python from RStudio.

## Who is the audience?

Anyone who wants to use Python from RStudio.

## Why is this important?

Many Data Science teams today are bilingual, leveraging both R and
Python in their work. Typically, each language is used from a different
IDE but switching IDE is painful, and many of us at 2DII are already
familiar with RStudio. We would like RStudio to be the single home for
both R and Python.

Objectives:

-   Create a Python environment.
-   Install Python packages from RStudio.
-   Use a Python environment.
-   Run an rmarkdown document from Rstudio – with both R and Python.
-   Run a Python script from RStudio.
-   Run Python code interactively from RStudio.

## Demo

## Setup

Use the R interface to Python

``` r
# install.packages("reticulate")
library(reticulate)

Sys.setenv(RETICULATE_PYTHON = "/home/mauro/anaconda3/bin/python")
```

-   Install a package and environment manager

> Anaconda is a Python/R data science distribution that contains a
> package and environment manager, which helps users manage a collection
> of over 7,500+ open-source packages.

– <https://docs.continuum.io/anaconda/>

### Example code

``` python
import nltk
import spacy
# conda install -c conda-forge spacy-model-en_core_web_sm

sent = "Please book my flight to California."

tokenized_sent_nltk = nltk.sent_tokenize(sent)
[nltk.pos_tag(nltk.word_tokenize(word)) for word in tokenized_sent_nltk]
#> [[('Please', 'NNP'), ('book', 'NN'), ('my', 'PRP$'), ('flight', 'NN'), ('to', 'TO'), ('California', 'NNP'), ('.', '.')]]
nlp = spacy.load("en_core_web_sm")
spacy_doc = nlp(sent)

print(spacy_doc)
#> Please book my flight to California.
for token in spacy_doc:
    print(token.text, token.pos_)
#> Please INTJ
#> book VERB
#> my PRON
#> flight NOUN
#> to ADP
#> California PROPN
#> . PUNCT
```

## Resources

-   YouTube [playlist](https://bit.ly/ds-incubator-videos).
-   The
    [ds-incubator](https://github.com/2DegreesInvesting/ds-incubator#ds-incubator)
    project.
-   [Ideas](https://bit.ly/dsi-ideas) for future meetups.
-   [RStudio: A single home for R & Python
    (webinar)](https://rstudio.com/resources/webinars/rstudio-a-single-home-for-r-and-python/).
