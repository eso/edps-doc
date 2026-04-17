# Overview of all the data reduction configuration options  <a name="configuration"></a>

## Selection of most appropriate calibrations

```{include} ../common/appropriate_calibrations.md
```

## Configuration of parameters: the configuration editor
```{include} ../common/configure_reduction.md
```
## Quality reports
```{include} ../common/quality_plots.md
```

## Radial Velocity Computation <a name="rad_vel_comp"> </a>

The ESPRESSO data reduction library contains a cross-correlation 
module that 
computes the cross-correlation function (CCF) of an S2D spectrum
with respect to a binary template (mask) of a given spectral 
type. The radial velocity (RV) is then obtained from a Gaussian 
fit to the CCF. This technique has been successfully used on the 
ELODIE, CORALIE, HARPS, SOPHIE, and HARPS-N spectrographs (see
Baranne et al. 1996, A&AS 119, 373, and Pepe et al. 2002, A&A 
388, 632). One of its main advantages is that CCFs can be 
computed automatically using an absorption line mask. Line masks 
are simply lists of central wavelengths and depths of spectral 
lines, and can be created for various spectral types. We note 
here that the CCFs of slowly rotating stars are extremely well 
approximated by Gaussian profiles with a flat continuum. 
However, the particular fitting function does not matter much; 
the crucial aspect is to fit the CCFs of a given star always 
with the same function to avoid systematic effects on the 
derived radial velocities. As such, it is fundamental to reduce
all the spectra with the same mask and CCF parameters, as 
comparisons between reductions with different parameters will 
be affected by systematics.

The main steps of the algorithm are:

(1) Compare the global flux distribution in the S2D spectrum to 
a static flux template that approximately corresponds to the 
spectral type of the star. The S2D flux is scaled accordingly 
to match the flux distribution of the template. In this way, 
spectra of any given star are always brought to the same flux 
distribution, which ensures that variable atmospheric 
conditions will not induce systematic effects in the CCF 
computation.

(2) Shift the wavelength scale of the S2D spectrum to the 
Solar-System barycenter using the barycentric correction.

(3) Define a uniform radial velocity grid that is approximately 
centered on the radial velocity of the star.

(4) For a given RV value in the grid, shift the line mask by 
the corresponding Doppler shift, project the line mask onto 
the S2D spectrum using a specified line width (about one 
pixel), and sum the S2D flux that goes through the so-defined 
mask holes. The flux from partial pixels is computed via 
simple linear interpolation. The sum is actually a weighted 
sum, using line depths as weights to optimally extract the 
Doppler information. During this process, the S2D spectrum is 
locally blaze corrected to remove any continuum slope around 
spectral lines. This produces one point of the CCF.

(5) Loop over all RV values in the grid.

(6) Fit a Gaussian profile to the CCF to derive RV, FWHM, and 
contrast.

Note that, by construction, CCFs are simply co-added spectral 
lines in velocity space, weighted by their depth and continuum 
flux, and corrected for the transmission of the grating (blaze 
function). As such they can be considered as a master spectral 
line for the star.


---
Go to [top](#configuration)


## Removal of cosmic rays <a name="cosm_rays"> </a>

Cosmic rays (CRs) are identified via a k-sigma rejection when 
extracting the one-dimensional spectrum from a single order. 
In each recipe that does it, the clipping is regulated by a 
dedicated parameter. In the science recipe, **espr_sci_red** 
the clipping is regulated by the parameter **ksigma_cosmic**. 
A value of -1 turns off the k-sigma clipping.

The science recipe has also an additional algorithm to detect 
CRs, that exploits L.A.Cosmic (van Dokkum 2001, PASP, 113, 
1420). The algorithm is applied to the so-called 
detector-cleaned frames, i.e., the raw science where the 
overscan regions have been trimmed, and their contribution 
subtracted. Cosmics identified in this way are masked during 
the extraction of the one-dimensional spectra.

Both algorithms can be run simultaneously.

The L.A.Cosmic algorithm is regulated by the following parameters: 

(1) **cosmic_detection_sw**: It turns L.A.Cosmic on (if set to 1) 
or off (if set to 0). By default, its value is taken by the input 
instrument configuration table. The algorithm is turned on for 
SKY mode, and it is turned off for FP-mode observations.

(2) **lacosmic.post-filter-mode**: dilate/dilute. It specifies 
whether CRs has to be dilated (i.e., expanded) or diluted (i.e., 
shrunk). It takes effect only if the post-filter-x/y values are 
positive.

(3) **lacosmic.post-filter-x**: X size of the post-filtering 
kernel. The mask is dilated or diluted by this amount along 
x-direction. Default: 0.

(4) **lacosmic.post-filter-y**: Y size of the post-filtering 
kernel. The mask is dilated or diluted by this amount along 
y-direction. Default: 0.

(5) **lacosmic.sigma_lim**: L.A.Cosmic Poisson fluctuation 
threshold. 
It is the minimum value of the fluctuation image, obtained by
dividing the Laplacian image (a second order derivative of the 
original image along x and y) by the noise model. High values
of **sigma_lim** detect the more intense cosmics, and have  
less risk of detecting false positives. Low values are more 
efficient in finding also faint cosmics, but have a higher 
risk of detecting false positives. The default values are 
taken from the input instrument configuration table: 5 
(SHR-SKY, 2x1), 7 (SHR-FP, 2x1), 7 (SHR 4x2), 8 (SUHR 1x1), 
10 (MHR 4x2), 8 (MHR 8x6).

(6) **lacosmic.f_lim**: L.A.Cosmic minimum contrast between 
the Laplacian image (see above) and the fine-structure image 
(created from the original image by a combination of median 
filters). High values of **f_lim** detect the more intense 
cosmics, and have less risk of detecting false positives. Low 
values are more efficient in finding also faint cosmics, but 
have higher risk of detecting false positives. The default 
values are taken from the input instrument configuration table: 
5 (SHR-SKY, 2x1), 5 (SHR-FP, 2x1), 5 (SHR 4x2), 8 (SUHR 1x1), 
4 (MHR 4x2), 5 (MHR 8x6).

(7) **lacosmic.max_iter**: L.A.Cosmic maximum number of 
iterations; default: 5.

(8) **extra_products_sw**: Set to TRUE to create extra 
products to inspect L.A.Cosmic results; default: FALSE.


 ---
Go to [top](#configuration)

 ---
Go to ESPRESSO EDPS tutorial [index](../espresso/index)