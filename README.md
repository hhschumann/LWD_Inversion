# LWD Inversion

Unconventional wells have become a major part of US oil production over the past
decade and a constant struggle for petroleum companies is finding ways to minimize the
expenses of this drilling. In order to maximize the contact between the wellbore and the reservoir
and optimize production, these unconventional wells are drilled directionally to land laterally
within the target formation. Geologists and engineers work together during drilling to steer the
wellbore within the target zone using a variety of data such as seismic, directional measurements,
and well logs. This process is time-consuming, expensive, and can be influenced by human
biases. We can reduce the time it takes to drill a given well, and therefore the well’s cost, by
automating the guiding the wellbore position drilling process using data that was already planned
to be collected. As such, the location of the wellbore within a reservoir can be formulated
as an inverse problem, which could reduce the time, expense, and bias when trying to map the
location of the wellbore relative to the target.

When considering the drilling industry, the field of geosteering is moving in the direction
of automated guidance. The wide practice of Logging While Drilling (LWD) has presented a
plethora of log data that can be used for this purpose. For our work, we use the gamma ray log,
obtained in real time from LWD measurements along a directional well, to invert for the distance 
of the well bore from the top of a particular geologic strata of interest. Gamma ray logs have
been used previously in fast forward algorithms to obtain similar results in real time [4].
However, in this report we build a linearized inversion algorithm using Tikhonov regularization
method to solve this nonlinear problem.

For our real data example, we used a LWD gamma ray log from a horizontal
unconventional well in addition to a gamma ray log from a vertical pilot well nearby. This
dataset is not publically available so we cannot share explicit details about location. However,
we would like to note that the reservoir consists of chalk and both the underburden and
overburden consist of marls. Since chalks typically have a lower gamma response than marls,
this stratigraphy results in variations in the gamma radiation which is crucial for the inversion to
be able to determine a solution. Additionally, we know from seismic data that there is not
significant dipping or faulting in the area. Therefore, our model objective function, which is a
combination of the smallest and flattest model, is well suited for this study region.

When setting up this test, a number of assumptions were made to simplify the inversion
process. The assumptions simplify the geological considerations and put a limit on the extent to
which our inversion algorithm can perform.

![Image](http://url/a.png)
