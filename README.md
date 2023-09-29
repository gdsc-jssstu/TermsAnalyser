# TermsAnalyser 📃⚖️

## Project Structure :-

The Terms and Conditions Analysis App is a Flutter application designed to analyze terms and conditions documents of various apps and provide users with valuable insights. The app employs natural language processing (NLP) techniques to extract summaries, identify problematic statements, and enable users to ask questions about the terms and conditions of different services and applications.

Key Features:

Document Analysis: The app can analyze terms and conditions documents in formats, including PDFs, text .
Summarization: It generates concise summaries of lengthy terms and conditions documents, making it easier for users to understand their contents.
Problematic Statement Detection: The app uses NLP to identify potentially problematic or unusual clauses within the terms and conditions, highlighting areas that may require further attention.
Question-Answering: Users can ask questions about specific sections or clauses in the terms and conditions, and the app provides relevant answers, enhancing user comprehension.

## Tech stack used:-

- Python 3.11.3
- Flask 2.3.3
- Flutter

### `Before contributing look into `[CONTRIBUTING GUIDELINES](./CONTRIBUTING.md)

## Project Setup:-

```
git clone https://github.com/gdsc-jssstu/TermsAnalyser.git

```

### Flutter part:-
## Project Structure

-**my_flutter_app/**<br/>
  -**MLapi/**:       The ml api<br />
  -**android/**:       Native Android code and configuration<br />
  -**ios/**:           Native iOS code and configuration<br />
  -**lib/**:           Dart code for the application<br />
  -**main.dart**:   Entry point of the Flutter app<br />
  -**test/**:           Unit and widget tests<br />
  -**assets/**:         Static assets like images, fonts, and JSON files<br />
  -**build/**:         Build artifacts (automatically generated)<br />
  -**doc/**:            Documentation (if any)<br />
  -**web/**:           Web-specific code and assets (if applicable)<br />
  -**.gitignore**:    Git ignore file for specifying ignored files and directories<br />
  -**pubspec.yaml**:   Flutter project configuration<br />
-**README.md**:      Project-specific documentation (this file)<br />


<hr>
<hr>

## Project setup instructions:
 
- **Fork the repository** to your GitHub account by clicking the "Fork" button at the top-right corner of this page. This will create a copy of the repository under your account.

- **Clone your forked repository** to your local machine using Git. Replace `your-username` with your GitHub username:

   `
   https://github.com/gdsc-jssstu/TermsAnalyser.git
   `
   
- **Install project dependencies** using (Flutter Package Manager): `flutter pub get`

- **Create a new branch** for your contribution. Replace *'feature/your-feature-name'* with a descriptive branch name related to your contribution:

### Development

- Make your changes or additions to the codebase. Test your changes to ensure they work as expected. To run the website on your Emulator
 

- Commit your changes with a descriptive commit message:
   `git commit -m "Add your descriptive message here" `

### Push Changes

- Push your changes to your forked repository on GitHub:
`git push origin feature/your-feature-name`

<hr>

### ML part:-

After making sure you have python 3.11.3 installed on your system,if not then install it from [here](https://www.python.org/downloads/)

Now change the directory to MLapi by running the following command in the terminal

```
cd MLapi

```

Now install all the dependencies by running the following command in the terminal

```
pip install -r requirements.txt

```

This might take a while to install all the dependencies


Now run the following command in the terminal to start the server
Make sure you are in the MLapi directory

```
flask --app app run

```
First time running this command might take a while as it will download the models and store them in the cache folder pls be patient

Now your server is up and running on port 5000 and the output in terminal should look like this

```
PS D:\TermsAnalyser\MLapi> flask --app app run
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit

```

Now you can test the api by sending a post request to the following url

```
http://127.0.0.1:5000

``` 

This api still experimental so might not give proper results , But it will not affect your Flutter contributions .
### Routes available by MLapi :-

http://127.0.0.1:5000/summarypdf  -->summary of the pdf file
http://127.0.0.1:5000/summaryfor=<data>  -->summary of the text sent through the post request
http://127.0.0.1:5000/classifierpdf   -->classifications of the pdf file
http://127.0.0.1:5000/classifierfor=<data>  -->classifications of the text sent through the post request
http://127.0.0.1:5000//chatfor=<data>    -->get the answer of the question asked through the post request


![image](https://github.com/gdsc-jssstu/TermsAnalyser/assets/97246168/2eabf074-f786-44ae-9406-d6b88648a103)

![image](https://github.com/gdsc-jssstu/TermsAnalyser/assets/97246168/dc72cd68-005a-4e6e-b2fe-af1fa2006646)

![image](https://github.com/gdsc-jssstu/TermsAnalyser/assets/97246168/18623052-4eea-40df-8f54-595f22ca1efb)

![image](https://github.com/gdsc-jssstu/TermsAnalyser/assets/97246168/7c1d079b-1681-4078-98b9-b8aee05d8b4f)

![image](https://github.com/gdsc-jssstu/TermsAnalyser/assets/97246168/80b8e116-1855-4ee4-833b-166ea48beadd)

![image](https://github.com/gdsc-jssstu/TermsAnalyser/assets/97246168/d467b328-958a-4d9e-8014-87dc77b78c6d)


















