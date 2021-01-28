# LWD Inversion

This project aims to use gamma ray loging while drilling (LWD) measurements to invert for the position of a geologic interval relative to the wellbore. Traditionally, geosteerers use a gamma ray log from a nearby vertical "pilot" well as a guide and formation indicator while they direct the drilling path of a new horizontal well and manually interpret the LWD measurements. However, by formulating the location of the borehole relative to a given geologic interval as an nonlinear inverse problem, which can potentially automate part of this process reducing the time, expense, and bias when trying to map the location of the wellbore relative to the target

## Introduction

***Motivation***

Unconventional wells have become a major part of US oil production over the past decade and a constant struggle for petroleum companies is finding ways to minimize the expenses of this drilling. In order to maximize the contact between the wellbore and the reservoir and optimize production, these unconventional wells are drilled directionally to land laterally within the target formation. Geologists and engineers work together during drilling to steer the wellbore within the target zone using a variety of data such as seismic, directional measurements, and well logs. This process is time-consuming, expensive, and can be influenced by human biases. We can reduce the time it takes to drill a given well, and therefore the well’s cost, by automating the guiding the wellbore position drilling process using data that was already planned to be collected. As such, the location of the wellbore within a reservoir can be formulated as an inverse problem, which could reduce the time, expense, and bias when trying to map the location of the wellbore relative to the target.

***Problem***

When considering the drilling industry, the field of geosteering is moving in the direction of automated guidance. The wide practice of Logging While Drilling (LWD) has presented a plethora of log data that can be used for this purpose. For our work, we use the gamma ray log, obtained in real time from LWD measurements along a directional well, to invert for the distance  of the well bore from the top of a particular geologic strata of interest. Gamma ray logs have been used previously in fast forward algorithms to obtain similar results in real time [4]. However, in this report we build a linearized inversion algorithm using Tikhonov regularization method to solve this nonlinear problem.

***Data***

For our real data example, we used a LWD gamma ray log from a horizontal unconventional well in addition to a gamma ray log from a vertical pilot well nearby. This dataset is not publically available so we cannot share explicit details about location. However, we would like to note that the reservoir consists of chalk and both the underburden and overburden consist of marls. Since chalks typically have a lower gamma response than marls, this stratigraphy results in variations in the gamma radiation which is crucial for the inversion to be able to determine a solution. Additionally, we know from seismic data that there is not significant dipping or faulting in the area. Therefore, our model objective function, which is a combination of the smallest and flattest model, is well suited for this study region.

## Methods

***Assumptions***

When setting up this test, a number of assumptions were made to simplify the inversion process. The assumptions simplify the geological considerations and put a limit on the extent to which our inversion algorithm can perform.

![Image](https://github.com/hhschumann/LWD_inversion/blob/main/Figures/diagram.png)

**Figure 1.** Diagram showing the formulation of the inverse problem and the assumptions.

Firstly, when defining our examples we assumed there were no faults. This first assumption allows us to simplify the inversion by not having to account for sharp changes in the model’s geometry or its respective gamma response. Secondly, we assume that the interval, who’s top we are inverting for, maintains a constant thickness across the model space. In doing this, we make it so that we only have to minimize one distance, the distance from the wellbore to the top of the reservoir, as opposed to having to invert for the distance to the bottom of the reservoir as well. The third assumption for our examples is that the vertical pilot well gamma ray response of the target interval is representative of the whole interval. This is the main assumption that allows us to use the gamma response of the directional well through the model to locate the position of the wellbore in the subsurface interval. All of these assumptions can be visualized in Figure 1. In Figure 1 the pilot well, type gamma log, is propagated across the model, and at any given distance from the interval top the gamma response within the interval is constant. This represents the third assumption. Also in Figure 1, the assumptions of constant thickness and lack of faulting can be visualized. The last two assumptions we make have to do with the provided data. For this inversion to be applicable to real world cases, we have to assume that both the gamma response of the pilot well and the directional survey data are accurate.

***Formulations***

The inversion was set up as a linearized solution of a nonlinear inverse problem using Tikhonov regularization. The formulation of the inverse problem is shown in equation 1.

![Image](https://github.com/hhschumann/LWD_inversion/blob/main/Figures/eq_1.png)

The gradient of the data misfit was calculated according to equation 2.

![Image](https://github.com/hhschumann/LWD_inversion/blob/main/Figures/eq_2.png)

The gradient of the smallest and flattest model objective function was calculated using equation 3.

![Image](https://github.com/hhschumann/LWD_inversion/blob/main/Figures/eq_3.png)

The gradient of the total objective function was calculated using equation 4.

![Image](https://github.com/hhschumann/LWD_inversion/blob/main/Figures/eq_4.png)

The system of linear equations shown with equations 5 and 6 was used to solve for the model perturbation Δh.

![Image](https://github.com/hhschumann/LWD_inversion/blob/main/Figures/eq_5_6.png)

***Parameter Estimation***

The estimation of the optimal beta inversion parameter for the Tikhonov regularization was performed through the application of the L-curve criterion. The perturbation parameter and scaling factors were found by experimenting with different ranges of values to find the ones that optimized our results.

***Forward Modeling*** 

The forward modeling for our synthetic case was performed by using our pilot well gamma data and our known true model to calculate the gamma response at the locations of our synthetic wellbore.

***Synthetic Test***

In our synthetic data case we constructed the simple pilot well data seen in Figure 2 (E). We created a gamma log response for our synthetic pilot well and used that data to forward model the gamma response of a well drilled through a simple dipping layer with the synthetic gamma profile. We added random Gaussian noise with a standard deviation of 1 and mean of zero to this forward modelled gamma response in order to better emulate real data seen in Figure 2 (B). We used a flat layer reservoir model as our initial model, with no dip, as shown in Figure 2 (C).

Viewing Figure 2 (C) and Figure 2 (D), we can see the direction and amounts of the model perturbations. These perturbations from the initial model resulted in a predicted model that reflects the general structure of the true model, shown in Figure 2 (A) , with both the predicted and true models dipping to the right. The predicted model also maintains a relatively consistent slope, reflecting the true model’s constant flat slope. Despite the gaussian noise added to our synthetic observed gamma response, our predicted gamma response resulted in reasonable gamma values as seen in Figure 2 (B).

## Discussion

***Analysis of Results***

Both the synthetic and real data examples showed some positive results. The synthetic
case, in which we have the true model, shows the ability of the inversion to predict a relatively
accurate model from observed data and a reference pilot log, even when random noise is added
to the data. The real data case showed that our inversion method can also recover similar
geometric characteristics to models created by geologists and geophysicists using even more data
than our inversion used. For example, our predicted model indicates that the well was drilled out
of zone similarly to that of the driller’s model in Figure 3 (A) . Additionally, the predicted data
mirrored closely the gamma response of the observed data as shown in Figure 3 (B) .

***Comparison to Literature***

This specific inversion is considered to be very difficult to solve with conventional
deterministic methods. This inversion problem is very complex and suffers from the local
minimum trap issue. Noise in the pilot well log can also be a significant issue because it can
cause errors in the forward model. To try to overcome these difficulties the inversion problem
has been formulated as a probabilistic inverse problem. One method used by Winkler involves
defining discrete random variables over the well log, structure, and wellbore positions [5]. These
random variables were then arranged into a Bayesian network. Shen, et al. used a stochastic
Hybrid Monte Carlo method to treat the problem similarly [6][7].

## Conclusions

In this work, we explored the use of regularized Tikhonov inversion to solve the
geosteering inverse problem. The method was applied to both a simple synthetic data case and an
example from real data taken from a pilot well and a directional well. The results for the
synthetic case fit well with our true model, and for the real data case the results had some
similarities to the interpretation we were provided. Geosteering is an important part of producing
from an unconventional well and inversion methods have the potential to streamline the process
and allow for better well placement.

There is plenty of additional work that should be explored and may improve the results of
the inversion. First, data cleaning and error estimation could play an important role in improving
inversion results. Well logs are typically processed to identify and compensate for sources of
noise like drilling mud or borehole breakouts. So, improving the quality of the log data and better
estimating the remaining error could improve the results of our inversion as well. Additionally,
our approach made several assumptions about dip, faulting, thickness, and lateral isotropy of the
gamma response within the reservoir.

Possible future work for this project could include formulating this as a probabilistic
inversion to attempt to address the issues we faced with our more conventional deterministic
method.

## References

[1] Alyaev, S., Bratvold, R. B., Luo, X., Suter, E., & Vefring, E. H. (2018). An Interactive
Decision Support System for Geosteering Operations. SPE Norway One Day Seminar . doi:
10.2118/191337-ms

[2] Arbus, T., & Wilson, S. (2019). Cybersteering: Automated Geosteering by Way of
Distributed Computing and Graph Databases in the Cloud. Proceedings of the 7th
Unconventional Resources Technology Conference . doi: 10.15530/urtec-2019-335

[3] Pollock, J., Stoecker-Sylvia, Z., Veedu, V., Panchal, N., & Elshahawi, H. (2018).
Machine Learning for Improved Directional Drilling. Offshore Technology Conference . doi:
10.4043/28633-ms

[4] Qin, Z., Pan, H., Wang, Z., Wang, B., Huang, K., Liu, S., … Fang, S. (2017). A fast
forward algorithm for real-time geosteering of azimuthal gamma-ray logging. Applied Radiation
and Isotopes , 123 , 114–120. doi: 10.1016/j.apradiso.2017.02.042

[5] Winkler, Hugh. “Geosteering by Exact Inference on a Bayesian Network.” Geophysics,
vol. 82, no. 5, 2017, doi:10.1190/geo2016-0569.1.

[6] Shen, Q., Wu, X., Chen, J., & Han, Z. (2017). Distributed Markov Chain Monte Carlo
Method on Big-Data Platform for Large-Scale Geosteering Inversion Using Directional
Electromagnetic Well Logging Measurements. ACES, vol. 32, no. 5, 2017

[7] Shen, Q., Wu, X., Chen, J., Han, Z., & Huang, Y. (2017). Solving geosteering inverse
problems by stochastic Hybrid Monte Carlo method. Journal of Petroleum Science and
Engineering. doi: doi:10.1016/j.petrol.2017.11.031


