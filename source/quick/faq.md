# Frequently Asked Questions

<details>
<summary><b>Q1) Where can I find the final reduced data?</b></summary>

Answer: all the products of all the datasets and the reductions are saved into the EDPS_data directory, specified when
executing the `edps-gui` for the first time. One can decide to export only the final products for selected datasets and
only for the desired reduction attempts into another location for further analysis. To do so, proceed as follows:

1. In the `Reduction Queue` tab, select the dataset and the dataset for which you want to export the final products.
   Click on the `Archive` button.
   ````{figure} figures/archive.jpg
   :alt: archive
   :name: archive
   ```` 

2. Go in the `Reduction Archive` tab, 

   ````{figure} figures/export1.jpg
   :alt: export1
   :name: fig_export1
   ```` 

   and click on the `Export` button. A new tab window appear where you can indicate the
   directory you want to copy your final products; finally press "Export" to copy the data.


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

Answer: Install the `datademo` package provided with the pipeline installation or download the “Demo Data” package
from [href=https://www.eso.org/sci/software/pipe_aem_table.html](https://www.eso.org/sci/software/pipe_aem_table.html).
Please note that the demo data can be large (tens of Gigabytes).

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

<details>
<summary><b>Q6) How do I get additional support on EDPS or data reduction in general?</b>
</summary>

Answer: For suggestions, questions, or feedback in general, please open a ticket with the EDPS Support
team. This [link](https://support.eso.org/new-ticket?ticket%5Bticket_field_13%5D%5Bdata%5D=227) should take you directly to a webpage for creating and EDPS feedback ticket, but
incase you want to navigate there ’manually’, go to [https://support.eso.org](https://support.eso.org), login, click on
"Submit Helpdesk Ticket", and specify the Help topic: "Post Observations", "ESO Data Processing
System [EDPS]".

</details>

<details>
<summary><b>Q7) I have a lot of disk space, but when I install EDPS with pip or an ESO pipeline with `Homebrew` I 
get the error message: Cannot mkdir: No space left on device. How do I fix it?</b>
</summary>

Answer: This depends on how much disk space is allocated to the `/home`, `/var`, and `/tmp` directories. The final solution would be
to resize the space allocated to the in the organization of the filesystem. However, we list here few tricks that might do the job.

   - Clearing the pip .cache to make space for new packages. Type the command:

          pip cache purge

     before installing edps.

   - Redirect the cache, Homebrew temporary build directories into a partition with enough space. Set 
     some of the following environmental variables in your .bashrc file:

         export HOMEBREW_CACHE=<path_to_new_cache_directory>
         export XDG_CACHE_HOME=<path_to_new_cache_directory>
         export HOMEBREW_TEMP=<path_to_new_temporary_directory>
         export TMPDIR=<path_to_new_temporary_directory>

     The first moves only the location of Homebrew cache, the second the cache of most applications (instead of the default /home/username/.cache), the third moves
     the directory where homebrew builds, extracts, and saves temporary files (instead of the defaults /tmp and /var/tmp).
     The last changes the global system temporary directory and affects most of the linux commands.

   - As extreme measure, one can move the /home/linuxbrew/.linuxbrew directory somewhere else, and create a symbolic link in /home/linuxbrew. For example:

         cd /home/linuxbrew
         mv -f .linuxbrew <path_to_new_directory>
         ln -s <path_to_new_directory> .linuxbrew

     Note: this might require sudo priviliges. If packages are not installed via Homebrew, make sure that the
     installation directory is located into a disk with enough space.

</details>

---
Go to EDPS quick-start guide [index](../quick/index)