# Description: This file contains the code for the server side of the application.

# Importing the required libraries.(dont change anything here)----------------------------------------------------------------------------------------------------
from flask import Flask
API_TOKEN="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"
API_URL = "https://api-inference.huggingface.co/models/remzicam/privacy_intent"
headers = {"Authorization": f"Bearer {API_TOKEN}"}  
from transformers import pipeline
import requests
summarizer = pipeline("summarization", model="knkarthick/MEETING_SUMMARY")
from pdfminer.high_level import extract_text
from sentence_transformers import SentenceTransformer, util,CrossEncoder
# from text_generation import Client
# Importing the required libraries.-------------------------------------------------------------------------------------------------------------------------------


#chat (dont change anything here)--------------------------------------------------------------------------------------------------------------------------------------
def embed(fname,window_size,step_size):
    text=extract_text(fname)
    text=" ".join(text.split())
    text_tokens=text.split()

    sentences = []
    for i in range(0, len(text_tokens), step_size):
        window=text_tokens[i:i+window_size]
        if len(window)<window_size:
            break
        sentences.append(window)

    paragraphs=[" ".join(s) for s in sentences]

    model=SentenceTransformer('sentence-transformers/all-mpnet-base-v2')
    model.max_seq_length=512
    cross_encoder=CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

    embeddings=model.encode(paragraphs,show_progress_bar=True,convert_to_tensor=True)
    return model,cross_encoder,embeddings,paragraphs
def search(query,model,cross_encoder,embeddings,paragraphs,top_k=32):
    query_embedding=model.encode(query,convert_to_tensor=True)
    # query_embedding=query_embedding.cuda()
    hits=util.semantic_search(query_embedding,embeddings,top_k=top_k)[0]

    cross_input=[[query,paragraphs[hit['corpus_id']]] for hit in hits]
    cross_scores=cross_encoder.predict(cross_input)

    for idx in range(len(hits)):
        hits[idx]['cross_score']=cross_scores[idx]

    results=[]
    hits=sorted(hits,key=lambda hit:hit['cross_score'],reverse=True)
    for hit in hits[:5]:
        results.append(paragraphs[hit['corpus_id']].replace("\n"," "))
    return results

#chat ------------------------------------------------------------------------------------------------------------------------------------------------------------


app=Flask(__name__)


#routes------------------------------------------------------------------------------------------------------------------------------------------------------------
@app.route("/")  #route for home page
def home():
    return "Welcome to the api"

@app.route("/summarypdf")  #route for summarizing pdf
def summarize():
    try:
        data=extract_text('data.pdf')     #extracting text from pdf
    except:
        return "Pdf not uploaded"
    ans=[]
    n=int(len(data)/1024)          #splitting the text into 1024 word chunks
    for i in range(n):
        ans.append(summarizer(data[i*1024:(i+1)*1024]))
    
    ansstr=""          #combining the chunks into a single string
    for i in ans:
        ansstr+=i[0]['summary_text']
    return ansstr         #returning the summary

@app.route("/summaryfor=<data>")                            #route for summarizing text
def summarizefor(data):
    return summarizer(data)[0]['summary_text']               #returning the summary

@app.route("/classifierpdf")
def classifypdf():                                #route for classifying pdf
    try:
        data=extract_text('data.pdf')                       #extracting text from pdf
    except:
        return {'error':"Pdf not uploaded"}
    data=data.split('.')
    sdata={'inputs':data}
    response = requests.post(API_URL, headers=headers, json=sdata)               #sending the json object to the api

    store=[]                                                         #storing the labels
    for i in response.json():
        for j in i:
            if j['score']>0.5:
                store.append(j['label'])

    dsrd=[]                                               #storing the data according to the labels
    dcu=[]
    dsp=[]
    dsd=[]
    other=[]

    for i in range(len(store)):                                   #segregating the data according to the labels
        if store[i]=='data-storage-retention-deletion':
            dsrd.append(data[i])
        elif store[i]=='data-collection-usage':
            dcu.append(data[i])
        elif store[i]=='data-security-protection':
            dsp.append(data[i])
        elif store[i]=='data-sharing-disclosure':
            dsd.append(data[i])
        else:
            other.append(data[i])                                     #returning the data

    

    return {"data-storage-retention-deletion":dsrd,"data_collection_usage":dcu,"data-security-protection":dsp,"data-sharing-disclosure":dsd,"other":other}


@app.route("/classifierfor=<data>")
def classify(data):                                        #route for classifying text
    classdata=data.split('.')
    classdata={'inputs':classdata}                     #creating a json object

    response = requests.post(API_URL, headers=headers, json=classdata)            #sending the json object to the api
    return response.json()                                          #returning the response

@app.route("/chatfor=<data>")
def chat(data):                                       #route for chatbot
    try:
        model,cross_encoder,embeddings,paragraphs=embed('data.pdf',129,100)          #extracting text from pdf
    except:
        return "Pdf not uploaded"
    results=search(data,model,cross_encoder,embeddings,paragraphs,32)               #searching for the query
    return results[0]                                       #returning the response


@app.route("/pdfu",methods=['POST'])
def pdfu():                                                    #route for uploading pdf
    pdf=requests.files['pdf']                                    #extracting the pdf
    try:
        pdf.save('data.pdf')                                     #saving the pdf
        return "success"                                                    #returning success
    except:
        return "Pdf not uploaded"

#routes------------------------------------------------------------------------------------------------------------------------------------------------------------