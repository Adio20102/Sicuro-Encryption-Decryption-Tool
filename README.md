# SICURO: Encryption and Decryption application
<p><strong>SICURO</strong> is a Python-based encryption and decryption application designed to provide users with a secure and user-friendly way to protect their messages and files. Leveraging the Tkinter GUI library, it offers a seamless interface for encryption and decryption operations. This application utilizes the robust Fernet symmetric encryption scheme from the <code>cryptography</code> library, ensuring the confidentiality and integrity of sensitive data.</p>

<h3>Key Features:</h3>
<ul><li><p><strong>Fernet Encryption:</strong> SICURO employs the Fernet symmetric encryption scheme to securely encrypt and decrypt messages and files, offering strong protection against unauthorized access.</p></li><li><p><strong>Versatile Usage:</strong> Users can encrypt both messages and files, selecting their preferred mode through the intuitive GUI. Whether it's securing personal messages or confidential documents, SICURO provides a versatile solution.</p></li><li><p><strong>Dynamic Key Generation:</strong> Each session generates a unique encryption key, enhancing security by ensuring that encryption keys are not reused. This dynamic key generation mechanism adds an extra layer of protection to the encryption process.</p></li><li><p><strong>User-Friendly Interface:</strong> With a simple and intuitive interface, SICURO allows users to encrypt and decrypt their data effortlessly. The application's design prioritizes ease of use, making it accessible to users of all technical backgrounds.</p></li></ul>

<h3>Fernet:</h3>
<p><strong>Fernet</strong> is a symmetric encryption method which makes sure that the data encrypted cannot be manipulated/read without the key.Fernet uses the Advanced Encryption Standard(AES) algorithm to encode and decode messages. It uses a 32-byte long key, making it highly resistant to brute-force attacks.</p>

<h3>Working:</h3>
<h3><strong>Message Encryption/Decryption:</strong></h3>
<h4>Encryption Steps:</h4>
<ol> <li> Input your message in the designated text area</li>
     <li> Either use the automatically generated key displayed in the <code>Generated Key</code> entry field or edit it if desired.</li>
     <li> Select the <code>Encrypt</code> radio button to specify that you want to encrypt the message.</li>
     <li>Click the <code>Show Message</code> button to initiate the encryption process.</li>
     <li>After clicking the <code>Show Message</code> button, the script will encode the message to bytes, encrypt it using the  key, and display the encrypted result in the <code>Result</code> text entry field</li><br>
<img alt="" class="bg hc hd c" width="650" height="350" src="https://i.ibb.co/x1t6R3F/ED1.png"></img></ol>
<h4>Decryption Steps:</h4>
<ol> <li> Paste the encrypted message into the <code>Enter the Message</code> text area.</li>
     <li> Enter the key that was used to encrypt the message into the <code>Generated Key</code> entry field.Make sure the key is correct.</li>
     <li>  Choose the <code>Decrypt</code> radio button to indicate that you want to decrypt the message.</li>
     <li>  Click on the <code>Show Message</code> button.</li>
<p><i><u>If the key is incorrect a pop-up message is recieved that the decryption failed due to an incorrect key.</u></i></p>
<img alt="" class="bg hc hd c" width="650" height="350" src="https://i.ibb.co/hYdVbTL/IK.png"></img>
<br>
<p><i><u>If the key is correct, the script will decrypt the entered message using the provided key and display the decrypted result in the <code>Result</code> text area.</u></i></p>
<img alt="" class="bg hc hd c" width="650" height="350" src="https://i.ibb.co/fr9mw6H/IK2.png"></img>
</ol>

# 

<h3><strong>Files Encryption/Decryption:</strong></h3>
<h4>Encryption Steps:</h4>
<ol> <li> Click on the <code>Browse</code> button and choose the file you want to encrypt. The file path will be displayed in the <code>Select File</code> entry field.</li>
     <li> Either use the automatically generated key displayed in the <code>Generated Key</code> entry field or edit it if desired.</li>
     <li> Select the <code>Encrypt</code> radio button to specify that you want to encrypt the message.</li>
     <li>Click the <code>Show Message</code> button to initiate the encryption process.</li>
     <li>After clicking the <code>Show Message</code> button, The script will encrypt the selected file using the generated or custom key and save the encrypted file with a <code>.enc</code> extension.</li><br>
<img alt="" class="bg hc hd c" width="650" height="350" src="https://i.ibb.co/QKbC3hs/FE1.png"></img></ol>
<h4>Decryption Steps:</h4>
<ol> <li> Click on the <code>Browse</code> button and choose the encrypted file you want to decrypt. The file path will be displayed in the <code>Select File</code> entry field.</li>
     <li> Enter the key that was used to encrypt the file into the <code>Generated Key</code> entry field.Make sure the key is correct.</li>
     <li>  Choose the <code>Decrypt</code> radio button to indicate that you want to decrypt the message.</li>
     <li>  Click on the <code>Show Message</code> button.</li>
<p><i><u>If the key is incorrect a pop-up message is recieved that the decryption failed due to an incorrect key.</u></i></p>
<img alt="" class="bg hc hd c" width="650" height="350" src="https://i.ibb.co/Snxzftv/FE2.png"></img>
<br>
<p><i><u>If the key is correct, the script will decrypt the entered message using the provided key and display the decrypted result in the <code>Result</code> text area.</u></i></p>
<img alt="" class="bg hc hd c" width="650" height="350" src="https://i.ibb.co/QKbC3hs/FE1.png"></img>
</ol>










