# Lab 3

#### 1. Explore additional metrics that can serve as quality metrics for the search process. For example, you can consider metrics such as latency, model size, or the number of FLOPs (floating-point operations) involved in the model.

#### 2. Implement some of these additional metrics and attempt to combine them with the accuracy or loss quality metric. It's important to note that in this particular case, accuracy and loss actually serve as the same quality metric (do you know why?).

the acc is claucalted using metric. metrix is defined as metric = MulticlassAccuracy(num_classes=5)

loss uses the cross entroy using torch.nn.functional.cross_entropy
They vary by the amount but they both sevre to demosntrate howa ccruate the moel is




#### 3. Implement the brute-force search as an additional search method within the system, this would be a new search strategy in MASE.

#### 4. Compare the brute-force search with the TPE based search, in terms of sample efficiency. Comment on the performance difference between the two search methods.


# Lab 4


#### 1. Can you edit your code, so that we can modify the above network to have layers expanded to double their sizes? Note: you will have to change the ReLU also.

#### 2. In lab3, we have implemented a grid search, can we use the grid search to search for the best channel multiplier value?

#### 3. You may have noticed, one problem with the channel multiplier is that it scales all layers uniformly, ideally, we would like to be able to construct networks like the following:


#### 4. Integrate the search to the chop flow, so we can run it from the command line.

