from typing import List
import torch.nn.functional as F
import torch
from tqdm import tqdm
import os
from transformers import (
    AutoConfig,
    AutoModelForSeq2SeqLM,
    AutoTokenizer
)

class HighlightsCoverageEvaluator:
    def __init__(self, alignment_covered_thr: float = 0.75) -> None:
        """
        alignment_covered_thr: thr for an alignment to be covered when calculating #cover alignments in cluster
        """

        self.model_path = "lovodkin93/multi-review-fic-coverage-evaluator" 
        self.source_max_length =  800
        self.num_beams = 1
        self.config = AutoConfig.from_pretrained(self.model_path)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path, model_max_length=self.source_max_length, use_fast=True)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_path, config=self.config)
        self.summary_delim = "<extra_id_4>"
        self.output_max_length = 4
        self.positive_tkn = "yes"
        self.negative_tkn = "no"
        self.positive_tkn_id = self.tokenizer.encode(self.positive_tkn)[0]
        self.negative_tkn_id = self.tokenizer.encode(self.negative_tkn)[0]
        self.alignment_covered_thr = alignment_covered_thr

    def to(self, device: str) -> None:
        self.model = self.model.to(device)

    def create_input(self, alignments, pred):
        inputs = []
        for align in alignments:
            curr_input = f"{align} {self.summary_delim} {pred}"
            inputs.append(curr_input)
        return inputs


    def get_scores(self, curr_inputs):
        input_ids = self.tokenizer.batch_encode_plus(curr_inputs, 
                                                     padding=True, 
                                                     truncation=True,
                                                     return_tensors="pt")["input_ids"].to(self.model.device)
        
        outputs = self.model.generate(input_ids,
                                      min_length=1,
                                      max_new_tokens=self.output_max_length,
                                      output_scores=True,
                                      return_dict_in_generate=True,
                                      early_stopping=True,
                                      num_beams=self.num_beams)

        outputs_scores = F.softmax(outputs.scores[0], dim=1)
        outputs_scores_positive = outputs_scores[:,self.positive_tkn_id]
        return outputs_scores_positive

    def get_cluster_score(self, curr_scores):
        covered_alignments = curr_scores>self.alignment_covered_thr
        return len([elem for elem in covered_alignments if elem])/len(curr_scores)


    def evaluate(self, review_side_alignments: List[List[str]], predictions: List[str]) -> List:
        """
        review_side_alignments: a list of lists, where each sub-list consists of all unique alignments of an instance
        predictins: a list of the predictions
        return: coverage score for each instance
        """
        inputs = [self.create_input(aligns, predictions[i]) for i,aligns in enumerate(review_side_alignments)]
        results = [self.get_scores(curr_inputs) for curr_inputs in tqdm(inputs, unit="instances")]
        final_scores = [torch.mean(final_scores_lst).cpu().item() for final_scores_lst in results]
        return {"coverage_score" : final_scores}
