"""
Code to generate kymographs of an image file and analyse them to generate a flow/velocity profile (based on Thouvenin et al. 2020)
"""

import cv2
import tiffcapture as tc
import numpy as np
from scipy.signal import wiener, savgol_filter
import matplotlib.pyplot as plt
import os
from skimage.measure import label, regionprops
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec
from matplotlib.widgets import Slider
from tqdm import tqdm
from aicsimageio import AICSImage
from aicsimageio import readers
import cerebroflow.readers as reader


class Kymo:
    """
    Class Constructor: Kymo
    -----------------------
    Initializes the Kymo class object.

    INPUTS:
    - path (str): Path to the image file.
    - pixel_size (float): Pixel size in micrometers.
    - frame_time (float): Frame time in seconds.
    - filter_size (tuple or None): Optional filter size for image filtering.

    OUTPUTS:
    - None
    """
    def __init__(self,path, pixel_size, frame_time, dv_thresh=0.3, filter_size=None, use_metadata=False):
        np.seterr(all="ignore")
        self.path = path
        self.pixel_size = pixel_size    # in um
        self.frame_time = frame_time    # in s
        self.rect = {}  # rectangles for kept blobs
        self.images = []
        self.dv_thresh = dv_thresh  # threshold at which dv axis will define 0
        self.filtered_images = []
        self.kymo = []
        self.raw_kymo = []
        self.mean_velocities = []
        self.se_velocities = []
        self.binary_kymo = []
        self.cc_location = None
        self.use_metadata = use_metadata
        
        # get the pixel size from meta data (will override any passed values)
        if self.use_metadata:
            try:
                self.pixel_size,_ = self.get_meta_pix_size()[0]
                print("Pixel size from metadata: ",self.pixel_size,"um")
            except:
                print("Pixel size could not be extracted from metadata, using the default manual input value")
                
        # open the data
        self.data, self.name = self.open_tiff()
        self.name = os.path.basename(self.name)
        # get some information about the data
        _, self.first_img = self.data.retrieve()
        self.dv_pos,self.width = np.shape(self.first_img)
        print("problem:",np.shape(self.first_img))
        self.N_images = self.data.length

        # check the if a .npy was created if not create one
        self.read_data()

        # convert to numpy array
        self.images = np.array(self.images,dtype='>u2')
        print(np.shape(self.images))
        if filter_size != None:

            # if filter size is passed, filter images
            self.filtered_images = np.zeros_like(self.images)   # pre allocate to be faster
            self.filtered_images = self.filter_wiener(self.images, filter_size)

            # generate kymograph
            self.kymo = self.swap_axes(self.filtered_images)

        else:

            # generate kymograph
            self.kymo = self.swap_axes(self.images)
        
    def test_filter(self):
        """
        Generates an interactive plot to test the Wiener filter effects on an image slice.

        INPUTS:
        -------
        None

        OUTPUTS:
        --------
        None
        """

        # Define initial parameters
        thresh_init = 5
        slice_init = 0

        # Create the figure 
        plt.style.use('Solarize_Light2')
        fig, ax = plt.subplots()
        fig.suptitle("Wiener Filter Test",size=20)
        ax.text(0,0,"Move sliders to begin display")
        

        # adjust the main plot to make room for the sliders
        fig.subplots_adjust(left=0.25, bottom=0.25)

        # Make a horizontal slider to control the slice.
        axslice = fig.add_axes([0.25, 0.1, 0.65, 0.03])
        slice_slider = Slider(
            ax=axslice,
            label='Frames',
            valmin=0,
            valmax=self.N_images,
            valinit=slice_init,
            valstep=1
        )

        # Make a vertically oriented slider to control the filter size
        axthresh = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
        thresh_slider = Slider(
            ax=axthresh,
            label="Filter size",
            valmin=0,
            valmax=50,
            valinit=thresh_init,
            orientation="vertical",
            valstep=1
        )

        # initial plot
        filter_size = (thresh_init,thresh_init)
        display = wiener(self.images[slice_init],filter_size)
        ax.imshow(display)

        # The function to be called anytime a slider's value changes
        def update(val):

            if thresh_slider.val == 0:
                display = self.images[slice_slider.val].copy()
            else:
                filter_size = (thresh_slider.val,thresh_slider.val)
                display = wiener(self.images[slice_slider.val],filter_size)
            
            ax.clear()
            ax.imshow(display)
            
            fig.canvas.draw_idle()


        # register the update function with each slider
        slice_slider.on_changed(update)
        thresh_slider.on_changed(update)


        plt.show()

        
    def test_threshold(self):
        """
        Generates an interactive plot to test thresholding and binarization effects on an image slice.

        INPUTS:
        -------
        None

        OUTPUTS:
        --------
        None
        """
        # find the intensity of the central canal (based on the max of the mean intensities along the dv axis)
        means = []
        dv_length = len(self.kymo)
        for dv in range(dv_length):
            means.append(np.mean(self.kymo[dv,:,:]))

        # Define initial parameters
        thresh_init = 0.5
        slice_init = 0

        # Create the figure and the line that we will manipulate
        plt.style.use('Solarize_Light2')
        fig, ax = plt.subplots()
        fig.suptitle("Test threshold",size=20)
        ax.text(0,0,"Move sliders to begin display")
        

        # adjust the main plot to make room for the sliders
        fig.subplots_adjust(left=0.25, bottom=0.25)

        # Make a horizontal slider to control the slice.
        axslice = fig.add_axes([0.25, 0.1, 0.65, 0.03])
        slice_slider = Slider(
            ax=axslice,
            label='d-v slice',
            valmin=0,
            valmax=self.dv_pos,
            valinit=slice_init,
            valstep=1
        )

        # Make a vertically oriented slider to control the threshold
        axthresh = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
        thresh_slider = Slider(
            ax=axthresh,
            label="Threshold",
            valmin=0,
            valmax=1,
            valinit=thresh_init,
            orientation="vertical"
        )


        # The function to be called anytime a slider's value changes
        def update(val,kymo=self.kymo,means=means):

            central_canal = [np.max(means), np.argmax(means)]   # returns the max intensity and location of th cc
            min = np.quantile(kymo[central_canal[1]], thresh_slider.val) # calculate the min value based on the threshold at the cc position
            kymo_min = kymo.copy()[slice_slider.val]
            kymo_min[kymo_min < min]  = min # all values smaller than min become min
            kymo_min = self.rescale(kymo_min,1,2) # rescaling between 1 and 2

            # next we normalize the kymograph by the average value with respect to time
            avg_vs_time = kymo_min.mean().transpose()
            kymo_min = np.divide(kymo_min,avg_vs_time)

            # Generate binary image every pixel that is 1% above the min signal is equal to 1
            binary = np.where(kymo_min > 1.01,1,0)
            ax.clear()
            ax.imshow(binary)
            fig.canvas.draw_idle()

        # register the update function with each slider
        slice_slider.on_changed(update)
        thresh_slider.on_changed(update)

        plt.show()

    def generate_kymo(self, threshold: float, thresholding_method = "Quantile", filtering_method="Smooth", save_profile=False, save_display=False, filter_size = None, init_slice= 0, output_folder= None, dash=False, gol_parms=(20,3)):
        """
        Performs CSF flow analysis on kymograph data.

        INPUTS:
        -------
        threshold: float
            Threshold value for thresholding.
        thresholding_method: str
            Thresholding method ("Hardcore" or "Quantile").
        save_profile: bool
            Flag to save the flow profile figure.
        save_display: bool
            Flag to save the display figure.
        filter_size: tuple or None
            Optional filter size for image filtering.
        init_slice: int
            Initial d-v slice index.

        OUTPUTS:
        --------
        mean_velocities: array
            Array of mean velocities.
        se_velocities: array
            Array of standard errors of velocities.
        """
        print(f'Analyzing {self.name}:')
        print(f'threshold: \t{threshold} \nmethod: \t{thresholding_method} \nfilter size: \t{filter_size}')

        self.threshold = threshold
        
        if filter_size != None:

            # if filter size is passed, filter images
            self.filtered_images = np.zeros_like(self.images)   # pre allocate
            self.filtered_images = self.filter_wiener(self.images, filter_size)

            # generate kymograph
            self.kymo = self.swap_axes(self.filtered_images).copy()
            
        else:
            self.kymo = self.swap_axes(self.images).copy()

        self.raw_kymo = np.zeros_like(self.kymo)    # pre allocate to be faster
        self.raw_kymo = self.kymo.copy()    # keep a copy of the non normalized kymograph

        # threshold 
        self.kymo = self.thresholding(self.kymo, threshold = threshold, method = thresholding_method).copy()

        # convert to binary
        self.binary_kymo = self.binary(self.kymo)

        # detect blobs
        self.velocities = self.get_velocities(self.binary_kymo)

        # process the mean and sd of all the velocities
        self.mean_velocities, self.se_velocities = self.get_mean_vel(self.velocities, gol_parms, filtering_parms=filtering_method)
        print(f"Detected {len(self.mean_velocities)} traces.")

        # show plot
        if dash:
            self.plot(save_display=save_display, save_profile=save_profile, filter_size=filter_size, init_slice=init_slice, output_folder=output_folder, dash=dash) 

        
        print("Done! ")
       
        print()
        return self.mean_velocities, self.se_velocities
    
    def plot(self, save_profile: bool, save_display: bool,  init_slice=0,filter_size=None, output_folder=None, plot_create=False, dash=False):
        """
        Sets up and displays a multi-panel figure to visualize CSF flow analysis results.

        INPUTS:
        -------
        save_profile: bool
            Flag to save the flow profile figure.
        save_display: bool
            Flag to save the display figure.
        init_slice: int
            Initial d-v slice index.
        filter_size: tuple or None
            Optional filter size for image filtering.

        OUTPUTS:
        --------
        None
        """
        # calculate dv_axis
        self.dv_axis, warn = get_dv_axis(self.mean_velocities,self.dv_thresh,self.pixel_size)
        if warn:
            print(f"WARNING: {self.name} dv_axis origin is at first non-zero value") 


        with plt.style.context('default'):
            fig = plt.figure(layout="constrained", figsize=(10,6))
            gs = GridSpec(3, 3, figure=fig)
            plot1 = fig.add_subplot(gs[0, :])
            plot2 = fig.add_subplot(gs[1, :])
            plot3 = fig.add_subplot(gs[2, -1])
            plot4 = fig.add_subplot(gs[-1, 0])
            plot5 = fig.add_subplot(gs[-1, -2])
            fig.suptitle("CSF Profiler",size=20)

            # set titles
            plot1.title.set_text("1.Flow profile")
            plot2.title.set_text(f"2.Raw image wiener={str(filter_size)}")
            plot3.title.set_text("5.Kept blobs")
            plot4.title.set_text("3.Raw kymograph")
            plot5.title.set_text(f"4.Binary kymograph threshold={str(np.round(self.threshold,1))}")
            if filter_size != None:
                plot2.imshow(self.filtered_images[init_slice])
            else:
                plot2.imshow(self.images[init_slice])  
            plot4.imshow(self.raw_kymo[init_slice])
            plot5.imshow(self.binary_kymo[init_slice])
            plot3.imshow(self.labeled_img_array[init_slice])
            
            # set labels
            plot1.set_xlabel(r"Dorso-ventral position [$\mu$m]")
            plot1.set_ylabel(r"Average rostro-caudal velocity [$\mu$m/s]")
            plot2.set_xlabel(r"R-C axis [frames]")
            plot2.set_ylabel(r"D-V axis [frames]")
            plot4.set_ylabel(f"Time [{self.frame_time} s]")
            plot4.set_xlabel(r"R-C axis [frames]")
            plot5.set_ylabel(f"Time [{self.frame_time} s]")
            plot5.set_xlabel(r"R-C axis [frames]")

            # plot 1 Dashboard
            for region in regionprops(self.labeled_img_array[init_slice]):
                # take regions with large enough areas
                if (region.area < 100) and (region.area >= 15) and (region.eccentricity>0.9) and (np.degrees(region.orientation)>-95) and (np.degrees(region.orientation)<95) and (np.round(region.orientation,1)!= 0.0):         
                    # draw rectangle around good blobs
                    minr, minc, maxr, maxc = region.bbox
                    rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                            fill=False, edgecolor='red', linewidth=1)
                    plot3.add_patch(rect)
           
            # generate the x-axis in um
            try:
                # plot the velocities
                plot1.plot(self.dv_axis,self.mean_velocities) 
                
                # Plot grey bands for the standard error
                plot1.fill_between(self.dv_axis, self.mean_velocities - self.se_velocities, self.mean_velocities + self.se_velocities, color='grey', alpha=0.3, label='Standard Error')
            except:
                print("WARNING: Problem with velocity detection")
                pass

            # interactivity
            axtime = fig.add_axes([0.08, 0.35, 0.2, 0.03])
            time_slider = Slider(
                ax=axtime,
                label='Frame',
                valmin=0,
                valmax=self.N_images,
                valinit=0,
                valstep=1
            )
            # Make a vertical slider to control d-v slices
            axslice = fig.add_axes([0.03, 0.35, 0.02, 0.29])
            slice_slider = Slider(
                ax=axslice,
                label='d-v slice',
                valmin=0,
                valmax=self.dv_pos-1,
                valinit=0,
                valstep=1,
                orientation="vertical"
            )
            def update(val,images=self.images):
                plot2.imshow(images[time_slider.val])
                
                fig.canvas.draw_idle()

            def update_slice(val,images=self.images):
                plot4.imshow(self.raw_kymo[slice_slider.val])
                plot5.imshow(self.binary_kymo[slice_slider.val])
                plot3.clear()
                plot3.title.set_text("5.Kept blobs")
                plot3.imshow(self.binary_kymo[slice_slider.val])
                plot2.clear()
                plot2.imshow(images[time_slider.val])
                plot2.hlines(slice_slider.val,0,self.width-1, colors=['red'],label="Current slice")
                plot2.legend()
                for i in self.rect[slice_slider.val]:
                    plot3.add_patch(i)
                fig.canvas.draw_idle()
                

            # register the update function with each slider
            time_slider.on_changed(update)
            slice_slider.on_changed(update_slice)
                
            if save_display:
                if output_folder:
                    fig.savefig(os.path.join(output_folder,self.name.split(".")[0]+"_display_threshold"+str(np.round(self.threshold,1))+"_filter"+str(filter_size)+'.png'),dpi=fig.dpi)
                else:
                    fig.savefig(self.name.split(".")[0]+"_display_threshold"+str(np.round(self.threshold,1))+"_filter"+str(filter_size)+'.png',dpi=fig.dpi)
                plt.close(fig)

            if save_profile:
                print("Saving individual profile plot...")
                fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
                ax.set_xlabel(r"Dorso-ventral position [$\mu$m]")
                ax.set_ylabel(r"Average rostro-caudal velocity [$\mu$m/s]")
                ax.set_title(str(self.name))
                try:
                    ax.plot(self.dv_axis,self.mean_velocities) 
                    # Plot grey bands for the standard error
                    ax.fill_between(self.dv_axis, self.mean_velocities - self.se_velocities, self.mean_velocities + self.se_velocities, color='grey', alpha=0.3, label='Standard Error')
                    ax.legend()
                except:
                    print("ERROR: No traces detected")
                if output_folder:
                    fig.savefig(os.path.join(output_folder,self.name.split(".")[0]+"_threshold"+str(np.round(self.threshold,1))+"_filter"+str(filter_size)+'.png'))   # save the figure to file
                else:
                    fig.savefig(self.name.split(".")[0]+"_threshold"+str(np.round(self.threshold,1))+"_filter"+str(filter_size)+'.png')   # save the figure to file
                
                plt.close(fig)    # close the figure window

            if plot_create: # creates and returns a plot
                fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
                plt.style.use('Solarize_Light2')
                ax.set_xlabel(r"Dorso-ventral position [$\mu$m]")
                ax.set_ylabel(r"Average rostro-caudal velocity [$\mu$m/s]")
                ax.set_title(str(self.name))
                try:
                    ax.plot(self.dv_axis,self.mean_velocities) 
                    # Plot grey bands for the standard error
                    ax.fill_between(self.dv_axis, self.mean_velocities - self.se_velocities, self.mean_velocities + self.se_velocities, color='grey', alpha=0.3, label='Standard Error')
                    ax.legend()
                except:
                    print("ERROR: No traces detected")
                return fig,ax
            if dash:
                plt.show()
                
            del fig

    def filter_wiener(self,images: np.ndarray, filter_size: tuple):
        """
        Applies the Wiener filter to a sequence of images.

        INPUTS:
        -------
        images: ndarray
            Array of images to be filtered.
        filter_size: tuple
            Size of the Wiener filter.

        OUTPUTS:
        --------
        filtered_images: ndarray
            Filtered images after applying the Wiener filter.
        """
        out = np.zeros_like(images)
        for ind,im in enumerate(images):
            print(f"Filtering image {np.round((ind+1)/self.N_images*100,1)}%",end = "\r")
            out[ind] = wiener(im,filter_size)
           
        return out

    def swap_axes(self,images):
        """
        Swaps the axes of a sequence of images to generate a kymograph.

        INPUTS:
        -------
        images: ndarray
            Array of images.

        OUTPUTS:
        --------
        kymo: ndarray
            Kymograph generated from the input images.
        """

        kymo = np.swapaxes(images,0,1).copy()
        return kymo

    def thresholding(self,kymo: np.ndarray, method: str, threshold):  
        """
        Performs thresholding and rescaling on kymograph data.

        INPUTS:
        -------
        kymo: ndarray
            Input kymograph data.
        method: str
            Thresholding method ("Hardcore" or "Quantile").
        threshold: float
            Threshold value for thresholding.

        OUTPUTS:
        --------
        kymo: ndarray
            Thresholded and normalized kymograph data.
        """

        
        if method == "Hardcore":
            # rescale the intensities directly
            print("Rescaling kymograph")
            for i in tqdm(range(len(kymo))):
                kymo[i,:,:] = self.rescale(kymo[i,:,:],0,1)
                #print(f"Rescaling kymograph: {np.round(i/len(kymo)*100)}%",end = "\r")
            
            return kymo

        if method == "Quantile":
            # find the intensity of the central canal (based on the max of the mean intensities along the dv axis)
            means = []
            dv_length = len(kymo)
            for dv in range(dv_length):
                means.append(np.mean(kymo[dv,:,:]))
            
            central_canal = [np.max(means), np.argmax(means)]   # returns the max intensity and location of th cc
            self.cc_location = central_canal[1]
            min = np.quantile(kymo[central_canal[1]], threshold) # calculate the min value based on the threshold at the cc position
            kymo[kymo < min]  = min # all values smaller than min become min
            kymo = self.rescale(kymo,1,2) # rescaling between 1 and 2

            # next we normalize the kymograph by the average value with respect to time
            print("self.width:",self.width)
            avg_vs_time = np.tile(kymo.mean(axis=(0,2)),(self.width,1)).transpose()
            print("Normalizing kymograph:")
            for i in tqdm(range(kymo.shape[0])):
                kymo[i,:,:] = np.divide(kymo[i,:,:],avg_vs_time)
            
            # Next we pre-allocate some memory
            # TODO...

            # Next we perform the moving average of along the d-v axis (through the stack of kymographs)
            # This will "link" the trajectories
            self.N_avg = 3

            # TODO pre allocate to save some time
            kymo_avg = []
            print("Linking trajectories:")
            for i in tqdm(range(0,self.dv_pos-self.N_avg)):
                kymo_avg.append(np.mean(kymo[i:i+self.N_avg,:,:],0))
            kymo_avg = np.array(kymo_avg)
            return kymo_avg.copy()
        
    def binary(self, kymo: np.ndarray):
        """
        Generates a binary image from thresholded kymograph data.

        INPUTS:
        -------
        kymo: ndarray
            Thresholded kymograph data.

        OUTPUTS:
        --------
        binary: ndarray
            Binary image generated from the thresholded kymograph.
        """

        # Generate binary image, every pixel that is 1% above the min signal is set to 1
        binary = np.where(kymo > 1.01,1,0)
        return binary

    def get_velocities(self, binary_kymo: np.ndarray):
        """
        Detects and processes blobs in binary kymograph data to obtain velocities.

        INPUTS:
        -------
        binary_kymo: ndarray
            Binary kymograph data.

        OUTPUTS:
        --------
        keepers_vel: list
            List of velocities for each dorso-ventral position.
        """
        # Find all the blobs
        self.labeled_img_array = []
        keepers_vel = []
        

        # iterate over every d-v pos (from ventral to dorsal)
        print(f"Detecting blobs and calculating velocitiesfor d-v positions:")
        for i in tqdm(range(self.dv_pos-self.N_avg-1,-1,-1)):
            good = []
            rects = []
            # detect blobs
            #print(f"Detecting and processing blobs for d-v positions: {np.round(i/(self.dv_pos-self.N_avg)*100)}%",end = "\r")
            
            _, labeled_img, stats, centroids = cv2.connectedComponentsWithStats(binary_kymo[i].astype(np.uint8), connectivity=8)
            # labeled_img = label(binary_kymo[i],background=0)
            self.labeled_img_array.append(labeled_img)
            
            # iterate over every blob
            #print("Calculating velocities:")
            for region in regionprops(labeled_img):
            # take regions with large enough areas good eccentricity and orientation
                if (region.area >= 15) and (region.eccentricity>0.9) and (np.abs(np.sin(region.orientation))>0.1) and (np.abs(np.cos(region.orientation))>0.1) and (region.area <= 150):
                    # if valid calculate the speed from the blob's orientation 
                    # note: no need to convert to rad as np takes rad directly and regionprops returns the orientation angle (between the vertical 0th axis and the major axis of the blob) in rad 
                    speed = -(np.tan(-region.orientation))*(self.pixel_size/self.frame_time)  
                    good.append(speed)
                    minr, minc, maxr, maxc = region.bbox
                    rects.append(mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                                fill=False, edgecolor='red', linewidth=1))
            self.rect[i] = rects
            # if more than five events detected append to the keepers
            if len(good) < 5:
                keepers_vel.append(0)
            else:
                keepers_vel.append(good)
        print()
        return keepers_vel
    

    
    def get_mean_vel(self, velocities: np.ndarray, gol_parms, filtering_parms):
        """
        Computes mean velocities and standard errors from a list of velocities.

        INPUTS:
        -------
        velocities: list
            List of velocities for each dorso-ventral position.
        gol_parms: tuple
            Tuple of the widow length and polyorder for the savitzky golay filter
        filtering_parms: "Golay" or "Smooth"

        OUTPUTS:
        --------
        mean_velocities: array
            Array of mean velocities.
        se_velocities: array
            Array of standard errors of velocities.
        """
        def smooth(a,WSZ=5):
            # a: NumPy 1-D array containing the data to be smoothed
            # WSZ: smoothing window size needs, which must be odd number,
            # as in the original MATLAB implementation
            out0 = np.convolve(a,np.ones(WSZ,dtype=int),'valid')/WSZ    
            r = np.arange(1,WSZ-1,2)
            start = np.cumsum(a[:WSZ-1])[::2]/r
            stop = (np.cumsum(a[:-WSZ:-1])[::2]/r)[::-1]
            return np.concatenate((  start , out0, stop  ))
        
        # compute the mean velocities and se
        #print(f"\rSmoothing parameters:\twindow:{gol_parms[0]}\tpolyorder:{gol_parms[1]}")
        print("Smoothing: ",filtering_parms)
        if filtering_parms == "Golay":
            mean_velocities = savgol_filter([np.average(i) for i in velocities],gol_parms[0],gol_parms[1]) # compute the mean velocities for every dv position and smooth them
            se_velocities = savgol_filter([np.std(i) / np.sqrt(np.size(i)) for i in velocities],gol_parms[0],gol_parms[1]) # compute the se for every dv position and smooth them
        elif filtering_parms == "Smooth":
            mean_velocities = smooth([np.average(i) for i in velocities]) # compute the mean velocities for every dv position and smooth them
            se_velocities = smooth([np.std(i) / np.sqrt(np.size(i)) for i in velocities]) # compute the se for every dv position and smooth them
        elif filtering_parms == "Combine":
            mean_velocities = savgol_filter(smooth([np.average(i) for i in velocities]),gol_parms[0],gol_parms[1]) # compute the mean velocities for every dv position and smooth them
            se_velocities = savgol_filter(smooth([np.std(i) / np.sqrt(np.size(i)) for i in velocities]),gol_parms[0],gol_parms[1]) # compute the se for every dv position and smooth them

        return mean_velocities, se_velocities

    # helper functions
    def open_tiff(self):
        """
        Opens a TIFF image file using the tiffcapture library.

        INPUTS:
        -------
        None

        OUTPUTS:
        --------
        tiff: tc.TiffCapture
            TiffCapture object for the image file.
        name: str
            Name of the image file.
        """
        if self.path.endswith(".ims"):
            tiff = reader.read_ims_file(self.path)
        else:
            tiff = tc.opentiff(self.path) #open img
        name = self.path.split("\\")[-1]
        
        return tiff,name
    
    def get_meta_pix_size(self):
        """
        Opens a TIFF image file using the aicsimageio library.

        INPUTS:
        -------
        None

        OUTPUTS:
        --------
        pixel_size: An array containing x and y pixel sizes
        metadata:    A string containing the metadata of the image file
        """
        # Get an AICSImage object (I should use it for also reading the tiffs)
        img = AICSImage(self.path,reader=readers.TiffReader)
        pixel_size = [img.physical_pixel_sizes.X,img.physical_pixel_sizes.Y]
        metadata = img.metadata
        #print(metadata)

        return pixel_size,metadata

    def read_data(self):
        """
        Initializes image data by processing time-lapse images to an array (self.images).

        INPUTS:
        -------
        None

        OUTPUTS:
        --------
        None
        """

        print(f"Input file: {self.name}\n")
        print("Processing images:")  
        
        for ind,im in tqdm(enumerate(self.data)):
            #print(f"Processing images {np.round(ind/self.N_images*100,1)}%",end = "\r")
            self.images.append(im)
        

    def rescale(self,array,min,max):
        """
        Performs min-max scaling on the input array.

        INPUTS:
        -------
        array: ndarray
            Input array for scaling.
        min: float
            Minimum value after scaling.
        max: float
            Maximum value after scaling.

        OUTPUTS:
        --------
        scaled_matrix: ndarray
            Scaled array.
        """
        # Perform min-max scaling
        min_val = np.min(array)
        max_val = np.max(array)
        scaled_matrix = (max-min)*(array - min_val) / (max_val - min_val) + max
        
        return scaled_matrix
    

def get_dv_axis(profile,thresh,pixel_size,bias=-15):
        """
        Finds the start of the central canal along the dv_axis based on a given threshold and bias

        Returns:
        -------
        an array
        """
        warn=False
        try:
            dv_axis = np.arange(-(len(profile)-(len(profile)-np.argwhere(profile>thresh)[0][0]))-bias,len(profile)-np.argwhere(profile>thresh)[0][0]-bias)*pixel_size # find start of canal based on first speed over arbitrary threshold
        except:
            try:
                print("WARNING: Weird profile encountered. Origin will be set at first non-zero value.\nCheck the input image :p")
                thresh = 0
                dv_axis = np.arange(-(len(profile)-(len(profile)-np.argwhere(profile>thresh)[0][0]))-bias,len(profile)-np.argwhere(profile>thresh)[0][0]-bias)*pixel_size 
            except:
                print("WARNING: Setting origin at first non-zero failed. Dv-axis origin will be set arbitrarily at position 30.")
                dv_axis = np.arange(-(len(profile)-(len(profile)-29)),len(profile)-29)*pixel_size 
            warn = True
        return dv_axis,warn
    
