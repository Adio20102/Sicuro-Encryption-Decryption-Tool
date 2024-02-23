# SICURO: Encryption and Decryption Tool
<p><strong>SICURO</strong> is a Python-based encryption and decryption tool designed to provide users with a secure and user-friendly way to protect their messages and files. Leveraging the Tkinter GUI library, it offers a seamless interface for encryption and decryption operations. This tool utilizes the robust Fernet symmetric encryption scheme from the <code>cryptography</code> library, ensuring the confidentiality and integrity of sensitive data.</p>

<h3>Key Features:</h3>
<ul><li><p><strong>Fernet Encryption:</strong> SICURO employs the Fernet symmetric encryption scheme to securely encrypt and decrypt messages and files, offering strong protection against unauthorized access.</p></li><li><p><strong>Versatile Usage:</strong> Users can encrypt both messages and files, selecting their preferred mode through the intuitive GUI. Whether it's securing personal messages or confidential documents, SICURO provides a versatile solution.</p></li><li><p><strong>Dynamic Key Generation:</strong> Each session generates a unique encryption key, enhancing security by ensuring that encryption keys are not reused. This dynamic key generation mechanism adds an extra layer of protection to the encryption process.</p></li><li><p><strong>User-Friendly Interface:</strong> With a simple and intuitive interface, SICURO allows users to encrypt and decrypt their data effortlessly. The tool's design prioritizes ease of use, making it accessible to users of all technical backgrounds.</p></li></ul>

<h3>Fernet:</h3>
<p><strong>Fernet</strong> is a symmetric encryption method which makes sure that the data encrypted cannot be manipulated/read without the key.Fernet uses the Advanced Encryption Standard(AES) algorithm to encode and decode messages. It uses a 32-byte long key, making it highly resistant to brute-force attacks.</p>

<h3>Working:</h3>
<strong>Message Encryption/Decryption:</strong>
<ol> <li> Input your message in the designated text area</li>
<li> Either use the automatically generated key displayed in the <code>Generated Key</code> entry field or edit it if desired.</li>
<li> Select the <code>Encrypt</code> radio button to specify that you want to encrypt the message.</li>
<li>Click the <code>Show Message</code> button to initiate the encryption process.</li>
<li>After clicking the <code>Show Message</code> button, the script will encode the message to bytes, encrypt it using the  key, and display the encrypted result in the <code>Result</code> text entry field.</li>
