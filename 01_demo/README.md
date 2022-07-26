
# Demo

## R

The [reticulate](https://rstudio.github.io/reticulate/) package allows
using Python from R and RStudio. Some key features work automatically.

``` r
# You may want to specify which copy of Python reticulate chooses to bind to
readLines(here::here(".Renviron"))
#> [1] "RETICULATE_PYTHON=\"/home/mauro/anaconda3/bin/python\""
#> [2] ""

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

## Python

[Anaconda](https://docs.continuum.io/anaconda/) is a collection of
software for data science with Python and R. It contains Python itself,
many Python packages, and a tool called `conda` that manages it all.

Example:

This packages came with Anaconda

``` python
import nltk
import spacy
```

``` python
sent = "Please book my flight to California."

tokenized_sent_nltk = nltk.sent_tokenize(sent)
[nltk.pos_tag(nltk.word_tokenize(word)) for word in tokenized_sent_nltk]

# This failed and I had to install en_core_web_sm with:
#   conda install -c conda-forge spacy-model-en_core_web_sm
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
