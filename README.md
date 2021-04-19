# Legislator-Press-Release-Crawling-And-Translation

    Almost everyone who wants to use machine learning algorithms in practical applications will face the problem of Domain Adaptation. It means we have established a model in a  source domain, but hope to expand our model to different target domains.

    In machine translation, we always train the model with some popular open datasets,e.g., WMT( Workshop on Statistical Machine Translation ) or IWSLT( International Workshop on Spoken Language Translation ). But if we use our model on some special domain data,e.g., press releases, the model will be very weak because the domain is quite different. 

    This program can help you to download the press releases on Legislative Yuan websites automatically. And if you are doing a machine translation task, you can also call fuctions in googleTranslate.py. There are some function which will help you translate the press releases from chinese to english through the google api. You can use chinese and english  pairs to do machine translation or back translation. Enjoy it!


## Requirement

beautifulsoup4 == 4.9.3

bs4 == 0.0.1

requests == 2.25.1

googletrans == 4.0.0rc1

## Run

Use the Instruction shown as below to download press releases on the websites of legislators.

```sh
python crawling.py
```

Then, call the translate function. 

```sh
python googleTranslate.py
```
