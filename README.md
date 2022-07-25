
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

### Example code

``` python
import nltk
import spacy

sent = "Please book my flight to California."

tokenized_sent_nltk = nltk.sent_tokenize(sent)
[nltk.pos_tag(nltk.word_tokenize(word)) for word in tokenized_sent_nltk]

nlp = spacy.load("en_core_web_sm")
spacy_doc = nlp(sent)
for token in spacy_doc:
    print(token.text, token.pos_)
```

-   Install `python` must be installed.

``` r
Sys.which("python")
#>            python 
#> "/usr/bin/python"
```

-   Install the R package [reticulate: R interface to
    Python](https://rstudio.github.io/reticulate/).

``` r
# install.packages("reticulate")
library(reticulate)
```

Running python code interactive triggers:

``` r
> reticulate::repl_python()
No non-system installation of Python could be found.
Would you like to download and install Miniconda?
Miniconda is an open source environment management system for Python.
See https://docs.conda.io/en/latest/miniconda.html for more details.
```

Maybe pyhton is not discovered by rstudio?

``` python
1
#> 1
```

### Create a Python environment

### TODO

-   Install Python packages from RStudio.
-   Use a Python environment.
-   Run an rmarkdown document from Rstudio – with both R and Python.
-   Run a Python script from RStudio.
-   Run Python code interactively from RStudio.

## Resources

-   YouTube [playlist](https://bit.ly/ds-incubator-videos).
-   The
    [ds-incubator](https://github.com/2DegreesInvesting/ds-incubator#ds-incubator)
    project.
-   [Ideas](https://bit.ly/dsi-ideas) for future meetups.
-   [RStudio: A single home for R & Python
    (webinar)](https://rstudio.com/resources/webinars/rstudio-a-single-home-for-r-and-python/).
