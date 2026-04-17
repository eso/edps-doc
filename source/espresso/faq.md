# Frequently Asked Questions


<details>
<summary><b>Q1) Where can I find the final reduced 
data?</b></summary>

Answer: All the products of all the datasets and the reductions 
are saved in the EDPS_data directory, specified when executing 
the `edps-gui` for the first time. One can decide to export 
only the final products for selected datasets and only for the 
desired reduction attempts into another location for further 
analysis. To do so, proceed as follows:

1. In the `Reduction Queue` tab, select the dataset for which 
you want to export the final products and click on the `Archive` 
button.

2. Go to the `Reduction Archive` tab and click on the `Export` 
button. A new tab window appears where you can indicate the 
directory to which you want to copy your final products; 
finally, press `Export` to copy the data.

</details>



<details>
<summary><b>Q2) How do I stop the application?</b></summary>

Answer:

1. Press “Stop EDPS” in the Dashboard.

2. Type Ctrl-C in the terminal where the application is 
running. If the application doesn’t terminate, type Ctrl-C 
again.

3. Alternatively, kill the ‘panel serve’ process on your 
system, for example:

   		  ps -e | grep panel # get the process ID of the gui (<pid>).
   		  kill -9 <pid>

</details>



<details>
<summary><b>Q3) I have closed the browser window where the 
application is running. How can I reopen the 
application?</b></summary>

Answer: Point your browser to: http://localhost:5006/edps-gui.
If you have used a different port than 5006, you may have to 
edit the URL accordingly. 
</details>



<details>
<summary><b>Q4) Where can I find some data that I can use to 
test the application?</b></summary>

Answer: Install the `datademo` package provided with the 
pipeline installation or download the “Demo Data” package
from [here](https://www.eso.org/sci/software/pipe_aem_table.html).
Please note that the demo data can be large (tens of 
gigabytes).

A convenient script to download demo data for any pipeline 
is also available and can be used from the command line:

	curl -O https://eso.org/sci/software/apptainer/eso_download_demodata.sh  
	bash ./eso_download_demodata.sh 

</details>



<details>
<summary><b>Q5) How can I start the edps-gui if the following 
message appears:</b>:

	Cannot start Bokeh server, port 5006 is already in use

</summary>	

Answer: The panel server was not closed properly. Kill it by 
typing:

   	ps -e | grep panel # get the process ID of the gui (<pid>).
   	kill -9 <pid>

</details>



<details>
<summary><b>Q6) How do I get additional support on EDPS or data 
reduction in general?</b>
</summary>

Answer: For suggestions, questions, or feedback in general, 
please open a ticket with the EDPS Support team. This 
[link](https://support.eso.org/new-ticket?ticket%5Bticket_field_13%5D%5Bdata%5D=227) 
should take you directly to a webpage for creating and an EDPS 
feedback ticket, but in case you want to navigate there 
"manually", go to [https://support.eso.org](https://support.eso.org), login, click 
on "Submit Helpdesk Ticket", and specify the Help topic: 
"Post Observations", "ESO Data Processing System EDPS".

</details>



<details>
<summary><b>Q7) I have a lot of disk space, but when I install 
EDPS with pip or an ESO pipeline with `Homebrew` I get the error 
message: Cannot mkdir: No space left on device. How do I fix 
it?</b>
</summary>

Answer: This depends on how much disk space is allocated to the 
/home, /var, and /tmp directories. The final solution would be 
to resize the space allocated to the filesystem. However, we 
list here a few tricks that might do the job.

(1) Clearing the pip `.cache` to make space for new packages. Type 
the command:

   	pip cache purge

before installing EDPS.


(2) Redirect the cache, Homebrew temporary build directories 
into a partition with enough space. Set some of the following 
environmental variables in your `.bashrc` file:

   	export HOMEBREW_CACHE=<path_to_new_cache_directory>
   	export XDG_CACHE_HOME=<path_to_new_cache_directory>
   	export HOMEBREW_TEMP=<path_to_new_temporary_directory>
   	export TMPDIR=<path_to_new_temporary_directory>

The first moves only the location of Homebrew cache, the second 
moves the cache of most applications (instead of the default 
/home/username/.cache), the third moves the directory where 
homebrew builds, extracts, and saves temporary files (instead 
of the defaults /tmp and /var/tmp), and the last changes the 
global system temporary directory and affects most of the Linux 
commands.

(3) As an extreme measure, one can move the 
/home/linuxbrew/.linuxbrew 
directory somewhere else, and create a symbolic link in 
/home/linuxbrew. For example:

   	cd /home/linuxbrew
   	mv -f .linuxbrew <path_to_new_directory>
   	ln -s <path_to_new_directory> .linuxbrew

Important note: this operation might break some internal links. 
Recipes requiring external packages such as telluriccorr might 
not work (this impacts on KMOS, X-shooter, FORS, and Molecfit 
pipelines).

</details>



<details>
<summary><b>Q8) I have re-triggered the creation of datasets after 
having added a new directory in the input data dir. Some of the 
previously reduced datasets are labelled as new, despite the newly 
added files should have no impact. What's happening and how do I 
fix it?</b>
</summary>

Answer: This is a known bug that will be fixed in the next release. 
The cause is that the input data directory contains two files with 
the same properties and the same mjd-obs, but with different names 
(e.g., the same static calibration that is present in two places). 
Since their mjd-obs is the same, EDPS sometimes adds one file, 
sometimes the other. When a different file is associated, the 
dataset is labelled as new.

</details>



<details>
<summary><b>Q9) How can I manually run the recipes executed by EDPS, 
like it was possible with Esoreflex?</b>
</summary>

Answer: This is possible. 
EDPS saves the data products in $HOME/EDPS_data. it has sub-directories 
for each instrument.
The next sub-level of the directory structure contains directories 
for tasks (dark, bias, ... science).
Each of these contains sub-directories by data sets, e.g., 
b6db864b-ab35-4167-8c4a-3b11a4276f92.
These contain a command line script `cmdline.sh` and all necessary 
list of input files and of recipe parameters to reproduce that 
particular reduction step. 

</details>



<details>
<summary><b>Q10) Can I use different sets of bias frames (or any 
other calibrations) to calibrate my flat frames and science 
data?</b>
</summary>

Answer: To avoid ambiguity, users should remove the unwanted 
calibrations from the input directory and place there the 
calibrations that they want to use. 
</details>



<details>
<summary><b>Q11) How can I include my analysis scripts and 
algorithms into the workflow?</b>
</summary>

Answer: Please refer to the instructions on the EDPS web 
[page](https://www.eso.org/sci/software/edps.html) and to the 
EDPS workflow writing 
[tutorial](https://ftp.eso.org/pub/dfs/pipelines/libraries/edps/edps_workflow_design_guide0.9.pdf). 
</details>



<details>
<summary><b>Q12) The workflow fails, what can I do?</b>
</summary>

Answer: Common reasons why this is happening may be: 

(1) Some raw files are still compressed. In this case they will 
have names ending in **fits.Z**; use the command `uncompress *Z`
on them.

(2) Some calibration files may be too few (e.g., there must be 
at least 5 raw bias and dark frames, at least 10 raw flats) or
they can be missing altogether. Verify that all necessary 
calibrations are present.


</details>

---
Go to ESPRESSO tutorial [index](../espresso/index)