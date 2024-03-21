import json
import pytz
import spacy
import statistics
import email.utils
import numpy as np
import pandas as pd
from xhtml2pdf import pisa
from trustplutusmr.utils.logs import loga
import trustplutusmr.config.constants as ct
from pydantic import BaseModel
from tzlocal import get_localzone
from transformers import pipeline
from nlpretext import Preprocessor
from trustplutusmr.config.constants import json_path
# from utils.secretStore import SecretStore
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from xhtml2pdf import pisa

def convert_html_to_pdf(html_string, pdf_path):
    with open(pdf_path, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(html_string, dest=pdf_file)
    return not pisa_status.err

class Var(BaseModel):

    @staticmethod
    def read(keys: list):
        f = open(json_path)
        json_ = json.load(f)
        result = [json_.get(key) for key in keys]
        f.close()
        return result

    @staticmethod
    def add(key_value: dict):
        with open(json_path, 'w+') as f:
            json.dump(key_value, indent=4, sort_keys=True, fp=f)


class SentimentAnalysis(BaseModel):
    sent_models: list[str] = [ct.sent_model_1, ct.sent_model_2, ct.sent_model_3]
    labels: list[float] = []
    label: int = 0
    # @loga
    def get_sentiment(self, text):
        for i in self.sent_models:
            tokenizer = AutoTokenizer.from_pretrained(i)
            model = AutoModelForSequenceClassification.from_pretrained(i)
            nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
            results = nlp(text)
            self.labels.append(results[0]["label"].lower())

        mv_label = statistics.mode(self.labels)
        if mv_label == "positive":
            self.label = 1
        elif mv_label == "negative":
            self.label = 0
        elif mv_label == "neutral":
            self.label = 0.5


# Text cleaner
def clean_text(text):
    preprocessor = Preprocessor()
    return preprocessor.run(text)


class TextChunk(BaseModel):
    # Initialize the clusters lengths list and final texts list
    clusters_lens: list = []
    final_texts: list = []

    @staticmethod
    # Divide text into sentences and generate vector embeddings
    def process(text):

        # Load the Spacy model -> python -m spacy download en_core_web_lg
        nlp = spacy.load('en_core_web_lg')
        doc = nlp(text)
        sents = list(doc.sents)
        vecs = np.stack([sent.vector / sent.vector_norm for sent in sents])
        return sents, vecs

    @staticmethod
    def cluster_text(sents, vecs, threshold):
        clusters = [[0]]
        for i in range(1, len(sents)):
            if np.dot(vecs[i], vecs[i - 1]) < threshold:
                clusters.append([])
            clusters[-1].append(i)
        return clusters

    def get_chunks(self, data):

        # Process the chunk
        sents, vecs = self.process(data)

        # Cluster the sentences
        clusters = self.cluster_text(sents=sents, vecs=vecs, threshold=0.3)

        for cluster in clusters:
            cluster_txt = clean_text(' '.join([sents[i].text for i in cluster]))
            cluster_len = len(cluster_txt)

            # Check if the cluster is too short
            if cluster_len < 60:
                continue

            # Check if the cluster is too long
            elif cluster_len > 1000:
                sents_div, vecs_div = self.process(cluster_txt)
                reclusters = self.cluster_text(sents=sents_div, vecs=vecs_div, threshold=0.6)

                for subcluster in reclusters:
                    div_txt = clean_text(' '.join([sents_div[i].text for i in subcluster]))
                    print(div_txt)
                    print("----------")
                    div_len = len(div_txt)

                    if div_len < 60 or div_len > 3000:
                        continue

                    self.clusters_lens.append(div_len)
                    self.final_texts.append(div_txt)

            else:
                self.clusters_lens.append(cluster_len)
                self.final_texts.append(cluster_txt)


# class GenerateGraph(BaseModel):
#     path = ct.graph_path
#
#     @staticmethod
#     def utc_to_local(data):
#         utc_dt = email.utils.parsedate_to_datetime(data["date"])
#         local_tz = get_localzone()
#         local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
#         data["date_parsed"] = local_dt
#         return data
                
# Utility function
def convert_html_to_pdf(source_html, output_filename):
    # open output file for writing (truncated binary)
    result_file = open(output_filename, "w+b")

    # convert HTML to PDF
    pisa_status = pisa.CreatePDF(
            source_html,                # the HTML to convert
            dest=result_file)           # file handle to recieve result

    # close output file
    result_file.close()                 # close output file

    # return False on success and True on errors
    return pisa_status.err

def convertToPdf(data, outFile):
    
    # file = open(fileName+'.txt', 'rb')
    # data = pickle.load(file)
    # file.close()
    
    result = pd.DataFrame.from_dict(data)
    result["title"]=result.title.str.encode('latin-1', 'ignore')
    result["title"]=result.title.str.decode('latin-1')
    result["text"]=result.text.str.encode('latin-1', 'ignore')
    result["text"]=result.text.str.decode('latin-1')
    result["summary"]=result.summary.str.encode('latin-1', 'ignore')
    result["summary"]=result.summary.str.decode('latin-1')

    html_text = ''
    for index, row in result.iterrows():
        html_text+=row[6]
    
    convert_html_to_pdf(html_text,'C:\\Users\\rolfl\\Downloads\\'+outFile+".pdf")