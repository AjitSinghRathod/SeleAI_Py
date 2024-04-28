import spacy

# Load the English language model
nlp = spacy.load('en_core_web_sm')

# Function to generate test cases from text input
def generate_test_cases(text):
    doc = nlp(text)
    test_cases = []
    
    for token in doc:
        if token.pos_ == 'VERB':
            test_cases.append(f"Perform action: {token.text}")
    
    return test_cases

# Example text input
text_input = "Open the browser, click on the submit button, verify the success message"
test_cases = generate_test_cases(text_input)

for test_case in test_cases:
    print(test_case)