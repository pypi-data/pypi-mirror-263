from .common import FedaratedCommon
import tensorflow as tf

class FederatedClient(FedaratedCommon):
    # server will maintain a global model, a list of connected clients, a tokenizer

    def __init__(self, base_model, tokenizer, max_sequence_len, name, __MODEL_PATH__):
        super().__init__(tokenizer, base_model, max_sequence_len, __MODEL_PATH__)
        self.name = name
    
    def aggregate(self, client_model, base_model_weight=0.7, client_model_weight=0.3):
        base_model_weightage = tf.constant(base_model_weight, dtype=tf.float32)
        client_model_weightage = tf.constant(client_model_weight, dtype=tf.float32)
        blended_weights = []

        for base_layer, client_layer in zip(self.model.layers, client_model.layers):
            base_weights = base_layer.get_weights()
            client_weights = client_layer.get_weights()

            base_weights = [tf.convert_to_tensor(w, dtype=tf.float32) for w in base_weights]
            client_weights = [tf.convert_to_tensor(w, dtype=tf.float32) for w in client_weights]

            weighted_base_weights = [w * base_model_weightage for w in base_weights]
            weighted_client_weights = [w * client_model_weightage for w in client_weights]

            blended_layer_weights = [tf.add(wb, wc) for wb, wc in zip(weighted_base_weights, weighted_client_weights)]

            blended_weights.append(blended_layer_weights)

        for base_layer, blended_layer_weights in zip(self.model.layers, blended_weights):
            base_layer.set_weights(blended_layer_weights)

        self.save_model()
        