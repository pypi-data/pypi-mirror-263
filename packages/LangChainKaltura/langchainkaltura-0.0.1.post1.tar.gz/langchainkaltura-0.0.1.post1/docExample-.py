import os

from LangChainKaltura import \
    KalturaCaptionLoader

captionLoader = KalturaCaptionLoader(
    os.getenv('PARTNERID'),
    os.getenv('APPTOKENID'),
    os.getenv('APPTOKENVALUE'),
    KalturaCaptionLoader.FilterType(
        os.getenv('FILTERTYPE')),
    os.getenv('FILTERVALUE'),
    os.getenv('URLTEMPLATE'))

documents = captionLoader.load()
print(documents)
