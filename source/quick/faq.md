# Frequently Asked Questions

<details>
<summary><b>Q1) Where can I find the final reduced data?</b></summary>

Answer: all the products of all the datasets and the reductions are saved into the EDPS_data directory, specified when executing the `edps-gui` for the first time. One can decide to export only the final products for selected datasets and only for the desired reduction attempts into another location for further analysis. To do so, proceed as follows:

1. In the `Processing Queue` tab, select the dataset and the dataset for which you want to export the final products. Click on the `Archive` button.
	````{figure} figures/archive.jpg
	:alt: archive
	:name: archive
	```` 

2. Go in the `Archived Data` tab, and click on the `Export` button. A new tab window appear where you can indicate the directory you want to copy your final products to.

	````{figure} figures/export1.jpg
	:alt: export1
	:name: fig_export1
	```` 
	````{figure} figures/export2.jpg
	:alt: export2
	:name: fig_export2
	```` 

</details>

<details>
<summary><b>Q2) How do I stop the application?</b></summary>

Answer: Proceed as follows:

1. Press “Stop EDPS” in the Dashboard.

2. Type Ctrl-C in the terminal where the application is running. If the
application doesn’t terminate, type Ctrl-C again.

3. Alternatively, kill the ‘panel serve’ process on your system, for example:

   		  ps -e | grep panel # get the process ID of the gui (<pid>).
   		  kill -9 <pid>
</details>

<details>
<summary><b>Q3) I have closed the browser window where the application is running. How can I reopen the application?</b></summary>

Answer: Point your browser to: http://localhost:5006/edps-gui

</details>

<details>
<summary><b>Q4) Where can I find some data that I can use to test the application?</b></summary>

Answer: Install the `datademo` package provided with the pipeline installation or download the “Demo Data” package from [href=https://www.eso.org/sci/software/pipe_aem_table.html](https://www.eso.org/sci/software/pipe_aem_table.html). Please note that the demo data can be large (tens of Gigabytes). 

A convenient script to download demo data for any pipeline is also available and can be used from the command line: 

	curl -O https://eso.org/sci/software/apptainer/eso_download_demodata.sh  
	bash ./eso_download_demodata.sh 

</details>

<details>
<summary><b>Q5) How can I start the edps-gui if the following message appears?</b>:

	Cannot start Bokeh server, port 5006 is already in use
</summary>	

Answer: The panel server was not closed properly. Kill it by typing:

   	ps -e | grep panel # get the process ID of the gui (<pid>).
   	kill -9 <pid>


</details>

---
Go to EDPS quick-start guide [index](../quick/index)