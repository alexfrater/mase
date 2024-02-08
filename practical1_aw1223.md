ADLS

# Lab1

#### 1.	What is the impact of varying batch sizes and why?

| Batch Size | Test Accuracy | Test Loss |
|----------|----------|----------|
| 64| 0.5499944090843201 |  1.2155122756958008|
| 128 | 0.5313737988471985 | 1.2644456624984741 |
| 256 | 0.5126265287399292 | 1.326629400253296 |
| 512 | 0.4699992835521698 | 1.411876916885376  |

10 epochs


Larger batch size means faster training as gpu can be used more efficiently.
Smaller batch size, longer to converge but are more regualrized. 


#### 2.	What is the impact of varying maximum epoch number?


| Epoch Number | Test Accuracy | Test Loss |
|----------|----------|----------|
| 1|   |  |
| 2 | Row 2, Column 2 | Row 2, Column 3 |
| 3 | Row 3, Column 2 | Row 3, Column 3 |
| 4 | Row 3, Column 2 | Row 3, Column 3 |
| 5 | Row 3, Column 2 | Row 3, Column 3 |
|6|||
| 7 ||  |
| 8 |  |  |
| 9 |0.5087048411369324| 1.3385382890701294 |
| 10 | 0.5122921466827393 | 1.3265289068222046 |


If the epoch number is too low, the model will underfit as the weights have not been adjusted significantly. If the model is trained for too many epochs, the model may overfit and learn the nosie in the data.


#### 3.	What is happening with a large learning and what is happening with a small learning rate and why? What is the relationship between learning rates and batch sizes?


| Learning Rate | Test Accuracy | Test Loss |
|----------|----------|----------|
| 1e-06| Row 1, Column 2 | Row 1, Column 3 |
| 128 | Row 2, Column 2 | Row 2, Column 3 |
| 256 | Row 3, Column 2 | Row 3, Column 3 |
| 512 | Row 3, Column 2 | Row 3, Column 3 |



#### 4.Implement a network that has in total around 10x more parameters than the toy network.



#### 5.Test your implementation and evaluate its performance.






# Lab2

#### 1. Explain the functionality of report_graph_analysis_pass and its printed jargons such as placeholder, get_attr … You might find the doc of torch.fx useful.

It goes through the graph and counts each operation/variable
A placeholder represnets a funciton input and has a name type and default value
A get_attr will reciece a value from the hierachy of self.module
for example palceholder represnets an input to the graph and is for inputs to be fed into the graph
get_attr

Layer types stores the type of each module in order and then added to abuffer

The buffer is written to a file or the console.


call_module: A node operation representing the invocation of a module in nn.Module. Usually a neural network mdoule such as a layer

#### 2.What are the functionalities of profile_statistics_analysis_pass and report_node_meta_param_analysis_pass respectively?


profile_statistics_analysis_pass takes a graph, set its up for profiling, profiles the activaiton and weights and then computes the staticstscs for each node. The statics are then saved in each nodes metadata.

report_node_meta_param_analysis_pass iterates through each node to gather data on information such as node name, operation type, MASE type, MASE operation, and meta parameters related to common, hardware, and software.






### 3.Explain why only 1 OP is changed after the quantize_transform_pass .

Only the linear layer is changed and only linear is defined in the pas args to optimise


#### 4.Write some code to traverse both mg and ori_mg, check and comment on the nodes in these two graphs. You might find the source code for the implementation of summarize_quantization_analysis_pass useful.

#### 5.Perform the same quantisation flow to the bigger JSC network that you have trained in lab1. You must be aware that now the pass_args for your custom network might be different if you have used more than the Linear layer in your network.

#### 6.Write code to show and verify that the weights of these layers are indeed quantised. You might need to go through the source code of the implementation of the quantisation pass and also the implementation of the Quantized Layers .



.target usually holds a reference to the actual layer or module instance 