ADLS

Lab1

1.	What is the impact of varying batch sizes and why?

| Batch Size | Test Accuracy | Test Loss |
|----------|----------|----------|
| 64| Row 1, Column 2 | Row 1, Column 3 |
| 128 | Row 2, Column 2 | Row 2, Column 3 |
| 256 | Row 3, Column 2 | Row 3, Column 3 |
| 512 | Row 3, Column 2 | Row 3, Column 3 |



Larger batch size means faster training as gpu can be used more efficiently.
Smaller batch size, longer to converge but are more regualrized. 


2.	What is the impact of varying maximum epoch number?


| Batch Size | Test Accuracy | Test Loss |
|----------|----------|----------|
| 64| Row 1, Column 2 | Row 1, Column 3 |
| 128 | Row 2, Column 2 | Row 2, Column 3 |
| 256 | Row 3, Column 2 | Row 3, Column 3 |
| 512 | Row 3, Column 2 | Row 3, Column 3 |


If the epoch number is too low, the model will underfit as the weights have not been adjusted significantly

If the model is trained for too many epochs, the model may overfit and learn the nosie in the data.


3.	What is happening with a large learning and what is happening with a small learning rate and why? What is the relationship between learning rates and batch sizes?


| Batch Size | Test Accuracy | Test Loss |
|----------|----------|----------|
| 64| Row 1, Column 2 | Row 1, Column 3 |
| 128 | Row 2, Column 2 | Row 2, Column 3 |
| 256 | Row 3, Column 2 | Row 3, Column 3 |
| 512 | Row 3, Column 2 | Row 3, Column 3 |



4.Implement a network that has in total around 10x more parameters than the toy network.



5.Test your implementation and evaluate its performance.

