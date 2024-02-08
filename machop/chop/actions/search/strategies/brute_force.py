import optuna
import torch
import pandas as pd
import logging
from tabulate import tabulate
import joblib

from functools import partial
from .base import SearchStrategyBase

from chop.passes.module.analysis import calculate_avg_bits_module_analysis_pass

logger = logging.getLogger(__name__)




# !pip install thop
import time
import torch
from thop import profile
from torchmetrics.classification import MulticlassAccuracy
from chop.passes.graph.transforms import (
    quantize_transform_pass,
    summarize_quantization_analysis_pass,
)

class SearchStrategyBruteForce(SearchStrategyBase):
    is_iterative = False

    def _post_init_setup(self):
        self.metric = MulticlassAccuracy(num_classes=5)
        self.num_batches = 5
        self.flop_list = []
        self.recorded_metrics = []
        self.metric = MulticlassAccuracy(num_classes=5)

        

  

    def search(self, search_space):

        for i, config in enumerate(search_space):
            mg, _ = quantize_transform_pass(mg, config)

            acc_avg, loss_avg, latency_avg, model_size, flops = 0, 0, 0, 0, 0
            accs, losses, latencies = [], [], []

            # Calculate the model size (number of parameters)
            model_size = sum(p.numel() for p in mg.model.parameters())

            flops = profile(mg.model, inputs=(xs,), verbose=False)[0]
            self.flop_list.append(flops)
            # Loop over data batches
            for j, inputs in enumerate(self.data_module.train_dataloader()):
                if j > self.num_batches:
                    break

                xs, ys = inputs
                start_time = time.time()

                # Forward pass
                preds = mg.model(xs)
                latency = time.time() - start_time
                latencies.append(latency)

                loss = torch.nn.functional.cross_entropy(preds, ys)
                acc = self.metric(preds, ys)

                accs.append(acc.item())
                losses.append(loss.item())

            acc_avg = sum(accs) / len(accs)
            loss_avg = sum(losses) / len(losses)
            latency_avg = sum(latencies) / len(latencies)
            
            result = {
                "acc_avg": acc_avg,
                "loss_avg": loss_avg,
                "latency_avg": latency_avg,
                "flops": flops,
                "model_size" : model_size,
            }


            self.recorded_metrics.append(result)

        print(tabulate(self.recorded_metrics, headers="keys", tablefmt="pretty"))
        return 


