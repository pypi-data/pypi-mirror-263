from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch.nn.functional as F
import json 
from collections import defaultdict
import re
from tqdm import tqdm
from typing import List, Tuple, Dict
import torch
import numpy as np
import spacy
import logging
logging.basicConfig(level=logging.WARNING)

class HighlightsFaithfulnessEvaluator:
        def __init__(self, model_name: str = "google/flan-t5-xxl", batch_size: int = 5, entailment_word: str = "Entailment", contradiction_word: str = "Contradiction", neutral_word: str = "Neutral") -> None:
            """
            model_name: name of model to prompt in a zero-shot setting
            batch_size: size of inference batch
            entailment_word: word used by model to indicate entailment
            contradiction_word: word used by model to indicate contradiction
            neutral_word: word used by model to indicate neutral

            """
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name, device_map="auto")
            self.entailment = entailment_word
            self.contradiction = contradiction_word
            self.neutral = neutral_word
            self.entailment_tkn_ids = self.tokenizer.encode(self.entailment, add_special_tokens=False)
            self.contradiction_tkn_ids = self.tokenizer.encode(self.contradiction, add_special_tokens=False)
            self.neutral_tkn_ids = self.tokenizer.encode(self.neutral, add_special_tokens=False)
            self.max_special_tkn_len = max(len(self.entailment_tkn_ids), len(self.contradiction_tkn_ids), len(self.neutral_tkn_ids))
            self.batch_size = batch_size
            self.nlp = spacy.load("en_core_web_sm")

        def to(self, device: str) -> None:
            self.model = self.model.to(device)



        def get_special_tokens_constants(self) -> dict:
            """
            Constants used as highlights
            """
            special_tokens_constants = {}
            special_tokens_constants['highlight_start'] = "<extra_id_1>"
            special_tokens_constants['highlight_end'] = "<extra_id_2>"
            return special_tokens_constants


        def get_prompt(self, premise, hypothesis):
            prompt = f"""
                            ### Instruction: Read the following and determine if the hypothesis can be inferred from the premise. 
                            Options: Entailment, Contradiction, or Neutral 

                            ### Input: 
                            Premise: {premise}
                            Hypothesis: {hypothesis} 

                            ### Response (choose only one of the options from above):
                        """
            return re.sub(' +', ' ', prompt.strip()) # replace consecutive spaces with a single space

        def get_scores(self, curr_inputs):
            n_batches = int(np.ceil(len(curr_inputs) / self.batch_size))
            all_outputs = []
            for batch_i in range(n_batches):
                input_ids = self.tokenizer.batch_encode_plus(curr_inputs[batch_i*self.batch_size:(batch_i+1)*self.batch_size], 
                                                                padding=True, 
                                                                truncation=True,
                                                                return_tensors="pt")["input_ids"].to(self.model.device)
                
                outputs = self.model.generate(input_ids,
                                            min_length=1,
                                            max_new_tokens=self.max_special_tkn_len,
                                            output_scores=True,
                                            return_dict_in_generate=True,
                                            early_stopping=True,
                                            num_beams=1)
                all_outputs.append(outputs)
            all_scores = [torch.cat([curr_output.scores[i] for curr_output in all_outputs]) for i in range(self.max_special_tkn_len)]
            outputs_scores = [F.softmax(all_scores[i], dim=1) for i in range(self.max_special_tkn_len)]
            outputs_scores_entailment = torch.prod(torch.stack([outputs_scores[i][:, tkn_id] for i,tkn_id in enumerate(self.entailment_tkn_ids)]), dim=0)

            return outputs_scores_entailment

        def evaluate(self, predictions: List[str], concatenated_highlights: List[str]):
            """
            clustered_reviews_alignments: a list of predictions (str)
            concatenated_highlights: a list of concatenated highlights (sts)
            return: faithfulness scores for each instance
            """
            predictions_sentences = [[sent.text for sent in self.nlp(prediction).sents] for prediction in predictions]
            model_inputs = [[self.get_prompt(premise=concatenated_highlights[i], hypothesis=sent) for sent in instance] for i,instance in enumerate(predictions_sentences)]
            scores = [self.get_scores(instance) for instance in tqdm(model_inputs, unit="instances")]

            return {"faithfulness_score" : [torch.mean(instance).item() for instance in scores]}