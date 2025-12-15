# List of workflow tasks
This is the list of all the tasks and associated recipes in the XSHOOTER workflow. 
Only some of them are needed for scientific reduction, they are indicated by the flag "yes" (triggered by default) or "optional" (triggered only if requested
by a workflow parameter). Other tasks are not used for scientific reduction (they are indicated by the flag "no"), they are mainly used
for instrument monitoring and they can be executed only by specifying them as target. Note that, when a task is specified as target, all the 
tasks that generate the calibrations needed for it are automatically executed.

| TASK                       | 	RECIPE                  | Used in  <br/>  science reduction | 	Notes                          |
|----------------------------|--------------------------|-----------------------------------|----------------------------------|
| detmon_optical             | detmon_opt_lg  	         | no	                               | Note 1.                          |
| detmon_nir	                | detmon_ir_lg 	           | no	                               | Note 2.                          |
| bias	                      | xsh_mbias 	              | yes	                              | Note 2.                          |
| dark	                      | xsh_mdark 	              | optional	                         | Note 2.                          |
| order_prediction	          | xsh_predict 	            | yes	                              | Note 2.                          |
| order_definition	          | xsh_orderpos 	           | yes	                              | Note 2.                          |
| lamp_flat	                 | xsh_mflat 	              | yes	                              | Note 2.                          |
| lamp_flat_hc	              | xsh_mflat 	              | yes	                              | Note 2.                          |
| acquisition_camera_flat	   | xsh_mflat 	              | yes	                              | Note 2.                          |
| wavelength_calibration_2d	 | xsh_2dmap 	              | yes	                              | Note 2.                          |
| arc	                       | xsh_wavecal 	            | yes	                              | Note 2.                          |
| flats_science	             | - 	                      | yes	                              | Note 2.                          |
| flats_standard	            | - 	                      | optional	                         | Note 2.                          |
| flexures	            | xsh_flexcomp 	           | yes	                              | Note 2.                          |
| response_offset	            | xsh_respon_slit_offset 	 | yes	                              | Note 2.                          |
| response_slit_stare	            | xsh_respon_slit_stare 	  | yes	                              | Note 2.                          |
| response_slit_nod	            | xsh_respon_slit_nod 	    | yes	                              | Note 2.                          |
| flux_standard_slit_offset	            | xsh_scired_slit_offset 	 | yes	                              | Note 2.                          |
| science_slit_nod	            | xsh_scired_slit_nod 	    | yes	                              | Note 2.                          |
| flux_standard_slit_stare	            | xsh_scired_slit_stare 	  | yes	                              | Note 2.                          |
| science_slit_offset	            | xsh_scired_slit_offset 	 | yes	                              | Note 2.                          |
| telluric_standard_slit_offset	            | xsh_scired_slit_offset 	 | yes	                              | Note 2.                          |
| telluric_standard_slit_stare	            | xsh_scired_slit_stare 	  | yes	                              | Note 2.                          |
| telluric_standard_slit_nod	            | xsh_scired_slit_nod 	    | yes	                              | Note 2.                          |
| flux_standard_slit_nod	            | xsh_scired_slit_nod 	    | yes	                              | Note 2.                          |
| science_slit_stare	            | xsh_scired_slit_stare 	  | yes	                              | Note 2.                          |
| atmospheric_model_on_science_flux_standard_offset	            | xsh_molecfit_model 	     | optional	                         | Note 2.                          |
| atmospheric_model_on_science_science_nod	            | xsh_molecfit_model 	     | optional	                         | Note 2.                          |
| atmospheric_model_on_science_flux_standard_stare	            | xsh_molecfit_model 	     | optional	                         | Note 2.                          |
| atmospheric_model_on_science_science_offset	            | xsh_molecfit_model 	     | optional	                         | Note 2.                          |
| atmospheric_model_on_science_telluric_standard_offset	            | xsh_molecfit_model 	     | optional	                         | Note 2.                          |
| atmospheric_model_on_science_telluric_standard_stare	            | xsh_molecfit_model 	     | optional	                         | Note 2.                          |
| atmospheric_model_on_science_telluric_standard_nod	            | xsh_molecfit_model 	     | optional	                         | Note 2.                          |
| atmospheric_model_on_science_flux_standard_nod	            | xsh_molecfit_model 	     | optional	                         | Note 2.                          |
| atmospheric_model_on_science_science_stare	            | xsh_molecfit_model 	     | optional	                         | Note 2.                          |
| atmospheric_model_on_standard_offset	            | xsh_molecfit_model 	     | optional	                         | Note 2.                          |
| atmospheric_model_on_standard_stare	            | xsh_molecfit_model 	     | optional	                         | Note 2.                          |
| atmospheric_model_on_standard_nod	            | xsh_molecfit_model 	     | optional	                         | Note 2.                          |
| atmospheric_transmission_for_science_offset	            | xsh_molecfit_calctrans 	 | optional	                         | Note 2.                          |
| atmospheric_transmission_for_telluric_standard_offset	            | xsh_molecfit_calctrans 	 | optional	                         | Note 2.                          |
| atmospheric_transmission_for_flux_standard_offset	            | xsh_molecfit_calctrans 	 | optional	                         | Note 2.                          |
| atmospheric_transmission_for_science_nod	            | xsh_molecfit_calctrans 	 | optional	                         | Note 2.                          |
| atmospheric_transmission_for_telluric_standard_nod	            | xsh_molecfit_calctrans 	 | optional	                         | Note 2.                          |
| atmospheric_transmission_for_flux_standard_stare	            | xsh_molecfit_calctrans 	 | optional	                         | Note 2.                          |
| atmospheric_transmission_for_telluric_standard_stare	            | xsh_molecfit_calctrans 	 | optional	                         | Note 2.                          |
| atmospheric_transmission_for_flux_standard_nod	            | xsh_molecfit_calctrans 	 | optional	                         | Note 2.                          |
| atmospheric_transmission_for_science_stare	            | xsh_molecfit_calctrans 	 | optional	                         | Note 2.                          |
| telluric_corrected_science_offset	            | xsh_molecfit_calctrans 	 | optional	                         | Note 2.                          |
| telluric_corrected_telluric_standard_offset	            | xsh_molecfit_calctrans 	 | optional	                         | Note 2.                          |
| telluric_corrected_flux_standard_offset	            | xsh_molecfit_calctrans 	 | optional	                         | Note 2.                          |
| telluric_corrected_science_nod	            | xsh_molecfit_calctrans 	 | optional	                         | Note 2.                          |
| telluric_corrected_telluric_standard_nod	            | xsh_molecfit_calctrans 	 | optional	                         | Note 2.                          |
| telluric_corrected_flux_standard_stare	            | xsh_molecfit_calctrans 	 | optional	                         | Note 2.                          |
| telluric_corrected_telluric_standard_stare	            | xsh_molecfit_calctrans 	 | optional	                         | Note 2.                          |
| telluric_corrected_flux_standard_nod	            | xsh_molecfit_calctrans 	 | optional	                         | Note 2.                          |
| telluric_corrected_science_stare	            | xsh_molecfit_calctrans 	 | optional	                         | Note 2.                          |
| select_telluric_standard_to_combine	            | - 	                      | yes	                         | Note 2.                          |
| select_flux_standard_to_combine	            | - 	                      | yes	                         | Note 2.                          |
| select_science_to_combine	            | - 	                      | yes	                         | Note 2.                          |
| telluric_standard_combination	            | - 	                      | yes	                         | Note 2.                          |
| flux_standard_combination	            | - 	                      | yes	                         | Note 2.                          |
| science_combination	            | - 	                      | yes	                              | Note 2.                          |