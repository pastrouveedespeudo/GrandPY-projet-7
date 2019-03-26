import wikipediaapi

def wikipédia(element):
    wiki_wiki = wikipediaapi.Wikipedia('fr')
    page_py = wiki_wiki.page('{}'.format(element))
    existe = page_py.exists()
    print(existe)
    print(page_py.title)
    return page_py.title

wikipédia("Cité Paradis")
