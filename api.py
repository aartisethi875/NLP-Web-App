import paralleldots

paralleldots.set_api_key('IH4OCcC3pwUFU6jRcoyzug4ShpopFEtpLFigQEZImmk')


def Ner(text):
    Ner = paralleldots.Ner(text)
    return Ner