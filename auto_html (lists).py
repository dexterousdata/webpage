def generate_html(concept_title, concept_description):
    '''generates html for given title and description'''
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def single_concept_html(concept):
    '''extracts title and description from concept list and generates\
    html for single concept'''
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_html(concept_title, concept_description)

def multiple_concepts_html(list_of_concepts):
    '''extracts title and description from concept list and generates\
    html for a list of concepts'''
    html = ""
    for concept in list_of_concepts:
        html = html + single_concept_html(concept)
    return html

concept = [["test title1", "test description1"],
           ["test title2", "test description2"],
           ["test title3", "test description3"]] 
           

print multiple_concepts_html(concept)
