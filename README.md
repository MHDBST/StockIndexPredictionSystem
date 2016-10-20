# Stock_Index_Prediction_System
Predicting  Value at Risk of Iranian bourse data using one parametric and one none parametric method



In this project, I use one parametric and one non-parametric method for predicting the Value at Risk (VaR) of Iran Bourse data between 2009 to 2014. The implementation is done using Python.


1.
For parametric method, I implement a historical VaR for data based on the logarithm of returns. The logarithm of returns for day #t is calculated with this formula:

<math>
Ln(I(t+1)/I((t))
<math>

In which I(t) is the value of stack index in day t.
of VaR is the lowest limit of the logarithm of returns. Which means with confidence interval <code>(1-alpha)%</code> the logarithm of returns in day #t is more than the predicted value VaR in day #t. 

First I calculate the mean value of the data, then the variance is calculated. With these parameters, I select 1000 samples using Normal distribution. Then these samples are sorted. With defined <code>alpha</code> and prefered confidence interval, I select <code>Z_index_alpha</code> samples. 
To evaluate this method, 1000 times for different time intervals, the logarithm of returns is compared with the threshold. (1-alpha)% times of these 1000 times, the value should be greater than the predicted value. And I see this is true. (for more information contact the author)

This code is developed in historical.py 


2.
The second model is a non-parametric model. For this model I used the Garch method. The Garch model is a non-parametric model used for predecting the time series problems. For this problem, I used GARCH(1,1). Then with the maximum likelihood method, I find the parameters. Then the variance is being mesured and the logarithm of returns can be find easily. For finding prefered confidence interval, I use Monte-Carlo experiments. It means I created 1000 samples. Then the <code>alpha</code>'th sample will be the VaR. 
For evaluating this method I select 1000 samples randomly from different time intervals. If the calculated VaR for <code>(1-alpha)% </code> be greated than the measured value my hypothesis is correct.  
This implmentation is in Garch.py file


