Lab2

1. Explain the functionality of report_graph_analysis_pass and its printed jargons such as placeholder, get_attr … You might find the doc of torch.fx useful.

2.What are the functionalities of profile_statistics_analysis_pass and report_node_meta_param_analysis_pass respectively?



3.Explain why only 1 OP is changed after the quantize_transform_pass .

4.Write some code to traverse both mg and ori_mg, check and comment on the nodes in these two graphs. You might find the source code for the implementation of summarize_quantization_analysis_pass useful.

5.Perform the same quantisation flow to the bigger JSC network that you have trained in lab1. You must be aware that now the pass_args for your custom network might be different if you have used more than the Linear layer in your network.

6.Write code to show and verify that the weights of these layers are indeed quantised. You might need to go through the source code of the implementation of the quantisation pass and also the implementation of the Quantized Layers .

