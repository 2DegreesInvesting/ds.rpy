
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

-   Use a specific, and complex Python environment from RStudio.
-   Run complex Python code in an rmarkdown document from Rstudio.
-   Run complex Python code in an interactive console from RStudio.

## Demo

## Setup

-   [Anaconda](https://docs.continuum.io/anaconda/) is a collection of
    software for data science with Python and R. It contains a package
    and environment manager, which helps users manage a collection of
    over 7,500+ open-source packages.

-   [reticulate](https://rstudio.github.io/reticulate/) is an R package
    that enables the interface between R and Python. If available it’s
    automatically used by rmakrkdown and RStudio.

-   `RETICULATE_PYTHON` is an optional environment variable to control
    which copy of Python reticulate chooses to bind to. It should be set
    to the path to a Python interpreter, and that interpreter can either
    be:

    -   A standalone system interpreter,
    -   Part of a virtual environment,
    -   Part of a Conda environment.

``` r
Sys.setenv(RETICULATE_PYTHON = "/home/mauro/anaconda3/bin/python")
reticulate::py_config()
#> python:         /home/mauro/anaconda3/bin/python
#> libpython:      /home/mauro/anaconda3/lib/libpython3.9.so
#> pythonhome:     /home/mauro/anaconda3:/home/mauro/anaconda3
#> version:        3.9.12 (main, Apr  5 2022, 06:56:58)  [GCC 7.5.0]
#> numpy:          /home/mauro/anaconda3/lib/python3.9/site-packages/numpy
#> numpy_version:  1.21.5
#> 
#> NOTE: Python version was forced by RETICULATE_PYTHON
```

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
