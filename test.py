
from operator import itemgetter
from keras.models import load_model
from inputHandler import word_embed_meta_data, create_test_data
from model import SiameseBiLSTM
from config import siamese_config
from operator import itemgetter
from keras.models import load_model
from model import SiameseBiLSTM
from inputHandler import word_embed_meta_data, create_test_data
from config import siamese_config
import pandas as pd
import numpy as np
############ Data Preperation ##########
def test(refrance_ans,student_ans):
	correct="correct"
	incorrect="incorrect"
	df = pd.read_csv('FinalTraining.csv', error_bad_lines=False)
	df['referenceAnswer'] = df['referenceAnswer'].astype(str)
	df['studentAnswer'] = df['studentAnswer'].astype(str)
	#df["accuracy"] = df["accuracy"].astype(int)
	df['accuracy'] = df['accuracy'].replace({correct: 1, incorrect: 0})
	sentences1 = list(df['referenceAnswer'])
	sentences2 = list(df['studentAnswer'])
	model = load_model('lstm_50_50_0.17_0.25.h5')
	del df

	######## Word Embedding ############

	tokenizer, embedding_matrix = word_embed_meta_data(sentences1 + sentences2,  siamese_config['EMBEDDING_DIM'])

	embedding_meta_data = {
		'tokenizer': tokenizer,
		'embedding_matrix': embedding_matrix
	}

	## creating sentence pairs
	sentences_pair = [(x1, x2) for x1, x2 in zip(sentences1, sentences2)]
	del sentences1
	del sentences2
	test_sentence_pairs = [(refrance_ans, student_ans)]

	test_data_x1, test_data_x2, leaks_test = create_test_data(tokenizer,test_sentence_pairs,  siamese_config['MAX_SEQUENCE_LENGTH'])
	preds = (model.predict([test_data_x1, test_data_x2, leaks_test])*100)


	print(preds*100,'%')
	results = [(x, y, z) for (x, y), z in zip(test_sentence_pairs, preds)]
	results.sort(key=itemgetter(2), reverse=True)
	print (results)
	return preds
