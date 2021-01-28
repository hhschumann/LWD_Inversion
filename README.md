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





