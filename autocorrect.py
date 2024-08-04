from textblob import TextBlob

def correct_text(text):
    """
    Function to correct spelling in a given text.
    :param text: Input text with possible spelling errors
    :return: Corrected text
    """
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Correct the text
    corrected_text = blob.correct()
    
    return str(corrected_text)

def main():
    """
    Main function to run the autocorrect tool.
    """
    print("Welcome to the Autocorrect Tool!")
    while True:
        # Get user input
        user_input = input("Enter text to correct (or type 'exit' to quit): ")
        
        # Exit the loop if user types 'exit'
        if user_input.lower() == 'exit':
            print("Exiting the Autocorrect Tool. Have a great day!")
            break
        
        # Correct the text and print the result
        corrected = correct_text(user_input)
        print(f"Corrected Text: {corrected}")

if __name__ == "__main__":
    main()
