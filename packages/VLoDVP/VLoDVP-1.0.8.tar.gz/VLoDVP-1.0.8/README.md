![Banner](./banner.png)
<div align="center">
    </a>
    <br />
    
   [tagoWorks](https://tago.works/) - [Discord](https://tago.works/discord)
   
   ![GitHub last commit](https://img.shields.io/github/last-commit/t-a-g-o/vlod)
   ![GitHub issues](https://img.shields.io/github/issues-raw/t-a-g-o/vlod)
   ![GitHub](https://img.shields.io/github/license/t-a-g-o/vlod)

  Validating License on Discord Validating Package is coded to simplify the process of checking keys in your Python projects. Instead of taking up extra lines it handling decryption and license checking, VLoDVP provides simple functions. You can use the validate function, passing in your email and license key variables. VLoDVP handles all the decryption and checking behind the scenes, allowing you to focus on your main code. For example, you can use `if VLoDVP.validate(emailvar, licensekeyvar) == False:` to quickly check if a license is valid, without worrying about the details of the validation process. To use VLoDVP in your code and license your software please visit https://github.com/t-a-g-o/vlod. View VLoDVP's PyPi page at https://pypi.org/project/VLoDVP

</div>

# How to use VLoDVP

1. Install VLoDVP

   ```sh
   pip install vlodvp
   ```

2. Use VLoDVP
   Import and define
   ```py
   import VLoDVP
   ```

   * To set your private key use `VLoDVP.setkey('12345678901234567890123456789012')`
   * To set your license webserver link use `VLoDVP.setlink('https://yourlink.netlify.app/)`

3. Implement a way to get user input for email and license

4. Check if license exists using VLoDVP.validate()
   ```py
   if VLoDVP.validate(emailvar, licensekeyvar) == False:
      print("Invalid email or key")
   else:
      # Run your main code here
   ```
