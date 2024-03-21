import tensorflow as tf
import numpy as np
import datetime
from datetime import datetime
from dateutil import relativedelta

class FedaratedCommon():

    def __init__(self, tokenizer, model, max_sequence_len, __MODEL_PATH__):
        self.tokenizer = tokenizer
        self.model = model
        self.max_sequence_len = max_sequence_len
        self.events = []
        self.__MODEL_PATH__ = __MODEL_PATH__

    def add_event(self, message):
        event_time = datetime.now()
        
        day_ordinal = relativedelta.relativedelta(event_time, datetime(event_time.year, event_time.month, 1))
        day_ordinal = day_ordinal.days + 1

        formatted_time = event_time.strftime(f'{day_ordinal} %b %I:%M %p')

        self.events.append({
            'time': formatted_time,
            'message': message
        })

    def preprocess(self, sentences):
        # sentences is a list of strings
        input_sequences = []
        for line in sentences:
            token_list = self.tokenizer.texts_to_sequences([line])[0]

            for i in range(1, len(token_list)):
                n_gram_sequence = token_list[:i + 1]
                input_sequences.append(n_gram_sequence)

        input_sequences = np.array(tf.keras.preprocessing.sequence.pad_sequences(input_sequences, maxlen=self.max_sequence_len, padding='pre'))

        xs, labels = input_sequences[:, :-1], input_sequences[:, -1]
        ys = tf.keras.utils.to_categorical(labels, num_classes=len(self.tokenizer.word_index))

        xs = tf.keras.preprocessing.sequence.pad_sequences(xs, maxlen=self.max_sequence_len, padding='pre')

        return xs, ys, labels
    
    def predict(self, start_string, words_to_generate=1):
        next_word = ""
        for i in range(words_to_generate):
            token_list = self.tokenizer.texts_to_sequences([start_string])[0]
            token_list = tf.keras.preprocessing.sequence.pad_sequences([token_list], maxlen=114, padding='pre')
            predicted= self.model.predict(token_list)
            predicted= np.argmax(predicted,axis=1)
            output_word = ""
            for word, index in self.tokenizer.word_index.items():
                if index == predicted:
                    output_word = word
                    break
            next_word += " " + output_word
            start_string += " " + output_word

        return next_word.strip()
    
    def __train(self, xs, ys, epochs=1):
        self.model.fit(xs, ys, epochs=epochs, verbose=1)

    def train(self, sentences):
        self.add_event('Training started')
        self.model.compile(
            loss=tf.keras.losses.CategoricalCrossentropy(),
            optimizer=tf.keras.optimizers.Adam(learning_rate=0.03),
            metrics=['accuracy']
        )
        xs, ys, labels = self.preprocess(sentences)
        self.__train(xs, ys)
        self.add_event('Training completed')
        self.save_model()

    def get_weights(self):
        return self.model.get_weights()
    
    def save_model(self, ):
        try:
            print("####### Saving model #######")
            self.model.save(self.__MODEL_PATH__)
        except Exception as e:
            print("Error saving model")
            print(e)