Lab2

1. Explain the functionality of report_graph_analysis_pass and its printed jargons such as placeholder, get_attr … You might find the doc of torch.fx useful.

It goes through the graph and counts each operation/variable
A placeholder represnets a funciton input and has a name type and default value
A get_attr will reciece a value from the hierachy of self.module
for example palceholder represnets an input to the graph and is for inputs to be fed into the graph
get_attr

Layer types stores the type of each module in order and then added to abuffer

The buffer is written to a file or the console.


call_module: A node operation representing the invocation of a module in nn.Module. Usually a neural network mdoule such as a layer

2.What are the functionalities of profile_statistics_analysis_pass and report_node_meta_param_analysis_pass respectively?


profile_statistics_analysis_pass takes a graph, set its up for profiling, profiles the activaiton and weights and then computes the staticstscs for each node. The statics are then saved in each nodes metadata.

report_node_meta_param_analysis_pass iterates through each node to gather data on information such as node name, operation type, MASE type, MASE operation, and meta parameters related to common, hardware, and software.






3.Explain why only 1 OP is changed after the quantize_transform_pass .

Only the linear layer is changed and onlu linear is defined in the pas args to optimise


4.Write some code to traverse both mg and ori_mg, check and comment on the nodes in these two graphs. You might find the source code for the implementation of summarize_quantization_analysis_pass useful.

5.Perform the same quantisation flow to the bigger JSC network that you have trained in lab1. You must be aware that now the pass_args for your custom network might be different if you have used more than the Linear layer in your network.

6.Write code to show and verify that the weights of these layers are indeed quantised. You might need to go through the source code of the implementation of the quantisation pass and also the implementation of the Quantized Layers .



.target usually holds a reference to the actual layer or module instance 