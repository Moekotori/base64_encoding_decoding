import base64

# Infinite loop until the user chooses to exit
while True:
    # Prompt the user to choose an action: encrypt, decrypt, or exit
    z = input("Do you need to encrypt or decrypt? Enter 1 for encryption, 2 for decryption, or 0 to exit: ")

    # If the user inputs 1, perform encryption
    if z == '1':
        # Get the content the user wants to encrypt
        zoe2 = input("Please enter the content you want to encrypt: ")
        # Encode the user input to UTF-8, then base64 encode it, and decode back to a UTF-8 string for display
        zoe2_encoded = base64.b64encode(zoe2.encode('utf-8')).decode('utf-8')
        # Print the encrypted content
        print("The encrypted content is:", zoe2_encoded)

    # If the user inputs 2, perform decryption
    elif z == '2':
        # Get the content the user wants to decrypt
        zoe3 = input("Please enter the content you want to decrypt: ")
        try:
            # Attempt to base64 decode the user input, then decode back to a UTF-8 string
            zoe3_decoded = base64.b64decode(zoe3).decode("utf-8")
            # Print the decrypted content
            print("The decrypted content is:", zoe3_decoded)
        except Exception as e:
            # If there is an error during the decoding, print an error message
            print("Decryption failed, please ensure you have entered the correct encrypted content. Error message:", str(e))

    # If the user inputs 0, exit the program
    elif z == '0':
        # Print an exit message
        print("Exiting the program.")
        # Break out of the loop, causing the program to end
        break

    # If the user input is not 1, 2, or 0, print an error message
    else:
        # Print an error message
        print("Input error, please enter 1 or 2 to encrypt or decrypt, or 0 to exit.")