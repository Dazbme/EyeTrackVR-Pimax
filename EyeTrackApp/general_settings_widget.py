import PySimpleGUI as sg

from config import EyeTrackSettingsConfig
from osc import EyeId
from queue import Queue
from threading import Event

class SettingsWidget:
    def __init__(self, widget_id: EyeId, main_config: EyeTrackSettingsConfig, osc_queue: Queue):

        self.gui_flip_x_axis_left = f"-FLIPXAXISLEFT{widget_id}-"
        self.gui_flip_x_axis_right = f"-FLIPXAXISRIGHT{widget_id}-"
        self.gui_flip_y_axis = f"-FLIPYAXIS{widget_id}-"
        self.gui_general_settings_layout = f"-GENERALSETTINGSLAYOUT{widget_id}-"
        self.gui_osc_address = f"-OSCADDRESS{widget_id}-"
        self.gui_osc_port = f"-OSCPORT{widget_id}-"
        self.gui_osc_receiver_port = f"OSCRECEIVERPORT{widget_id}-"
        self.gui_osc_recenter_address = f"OSCRECENTERADDRESS{widget_id}-"
        self.gui_osc_recalibrate_address = f"OSCRECALIBRATEADDRESS{widget_id}-"
        self.gui_BLOB = f"-BLOBFALLBACK{widget_id}-"
        self.gui_HSF = f"-HSF{widget_id}-"
        self.gui_DADDY = f"-DADDY{widget_id}-"
        self.gui_DADDYP = f"-DADDYP{widget_id}-"
        self.gui_RANSAC3D = f"-RANSAC3D{widget_id}-"
        self.gui_BLINK = f"-BLINK{widget_id}-"
        self.gui_IBO = f"-IBO{widget_id}-"
        self.gui_HSRAC = f"-HSRAC{widget_id}-"
        self.gui_HSF_radius = f"-HSFRADIUS{widget_id}-"
        self.gui_blob_maxsize = f"-BLOBMAXSIZE{widget_id}-"
        self.gui_blob_minsize = f"-BLOBMINSIZE{widget_id}-"
        self.gui_speed_coefficient = f"-SPEEDCOEFFICIENT{widget_id}-"
        self.gui_min_cutoff = f"-MINCUTOFF{widget_id}-"
        self.gui_eye_falloff = f"-EYEFALLOFF{widget_id}-"
        self.gui_skip_autoradius = f"-SKIPAUTORADIUS{widget_id}-"
        self.gui_HSRACP = f"-HSRACP{widget_id}-"
        self.gui_RANSAC3DP = f"-RANSAC3DP{widget_id}-"
        self.gui_HSFP = f"-HSFP{widget_id}-"
        self.gui_BLOBP = f"-BLOBP{widget_id}-"
        self.gui_thresh_add = f"-THRESHADD{widget_id}-"
        self.gui_ROSC = f"-ROSC{widget_id}-"
        self.gui_vrc_native = f"-VRCNATIVE{widget_id}-"
        self.gui_circular_crop_left = f"-CIRCLECROPLEFT{widget_id}-"
        self.gui_circular_crop_right = f"-CIRCLECROPRIGHT{widget_id}-"
        self.gui_update_check = f"-UPDATECHECK{widget_id}-"
        self.gui_threshold_slider = f"-BLOBTHRESHOLD{widget_id}-"
        self.gui_video_scale = f"-VIDEOSCALE{widget_id}-"
        self.main_config = main_config
        self.config = main_config.settings
        self.osc_queue = osc_queue

        # Define the window's contents
        self.general_settings_layout = [
           
            [
                sg.Checkbox(
                    "Flip Left Eye X Axis",
                    default=self.config.gui_flip_x_axis_left,
                    key=self.gui_flip_x_axis_left,
                    background_color='#424042',
                    tooltip = "Flips the left eye's X axis.",
                ),
                sg.Checkbox(
                    "Flip Right Eye X Axis",
                    default=self.config.gui_flip_x_axis_right,
                    key=self.gui_flip_x_axis_right,
                    background_color='#424042',
                    tooltip = "Flips the right eye's X axis.",
                ),

           # ],
            #[
            sg.Checkbox(
                    "Flip Y Axis",
                    default=self.config.gui_flip_y_axis,
                    key=self.gui_flip_y_axis,
                    background_color='#424042',
                    tooltip = "Flips the eye's Y axis.",
                ),
            ],
            [sg.Checkbox(
                    "VRC Native Eyetracking",
                    default=self.config.gui_vrc_native,
                    key=self.gui_vrc_native,
                    background_color='#424042',
                    tooltip = "Toggle VRCFT output or VRC native",
                ),
                sg.Checkbox(
                    "Dual Eye Falloff",
                    default=self.config.gui_eye_falloff,
                    key=self.gui_eye_falloff,
                    background_color='#424042',
                    tooltip = "If one eye stops tracking, we send tracking data from your other eye.",
                ),
            ],
            [sg.Checkbox(
                    "Check For Updates",
                    default=self.config.gui_update_check,
                    key=self.gui_update_check,
                    background_color='#424042',
                    tooltip = "Toggle update check on launch.",
                ),
            ],
            [
                sg.Text("Video Scaling:", background_color='#424042'),
                sg.Slider(
                    range=(5, 100),
                    default_value=self.config.gui_video_scale,
                    orientation="h",
                    key=self.gui_video_scale,
                    background_color='#424042',
                    tooltip = "The Percentage to downscale the pimax video feeds to. 100 being full-res",
                ),
            ],
            [
                sg.Text("One Euro Filter Paramaters:", background_color='#242224'),
            ],
            [
                
                sg.Text("Min Frequency Cutoff", background_color='#424042'),
                sg.InputText(
                    self.config.gui_min_cutoff,
                    key=self.gui_min_cutoff,
                    size=(0,10),
                ),
            #],
            #[
                sg.Text("Speed Coefficient", background_color='#424042'),
                sg.InputText(
                    self.config.gui_speed_coefficient, 
                    key=self.gui_speed_coefficient,
                    size=(0,10),
                ),
            ],
             [
                sg.Text("OSC Settings:", background_color='#242224'),
            ],
            [
                sg.Text("Address:", background_color='#424042'),
                sg.InputText(
                    self.config.gui_osc_address, 
                    key=self.gui_osc_address,
                    size=(0,20),
                    tooltip = "IP address we send OSC data to.",
                ),
                
          #  ],
          #  [
                sg.Text("Port:", background_color='#424042'),
                sg.InputText(
                    self.config.gui_osc_port, 
                    key=self.gui_osc_port,
                    size=(0,10),
                    tooltip = "OSC port we send data to.",
                ),
            ],
            [
                sg.Text("Receive functions", background_color='#424042'),
                sg.Checkbox(
                    "",
                    default=self.config.gui_ROSC,
                    key=self.gui_ROSC,
                    background_color='#424042',
                    size=(0,10),
                    tooltip = "Toggle OSC receive functions.",
                ),
            ],
            [
                sg.Text("Receiver Port:", background_color='#424042'),
                sg.InputText(
                    self.config.gui_osc_receiver_port, 
                    key=self.gui_osc_receiver_port,
                    size=(0,10),
                    tooltip = "Port we receive OSC data from (used to recalibrate or recenter app from within VRChat.",
                ),
            #],
           # [
                sg.Text("Recenter Address:", background_color='#424042'),
                sg.InputText(
                    self.config.gui_osc_recenter_address, 
                    key=self.gui_osc_recenter_address,
                    size=(0,10),
                    tooltip = "OSC Address used for recentering your eye.",
                    ),
            ],
            [
                sg.Text("Recalibrate Address:", background_color='#424042'),
                sg.InputText(
                    self.config.gui_osc_recalibrate_address, 
                    key=self.gui_osc_recalibrate_address,
                    size=(0,10),
                    tooltip = "OSC address we use for recalibrating your eye",
                    ),
            ]

        ]

        
        self.widget_layout = [
            [   
                sg.Text("General Settings:", background_color='#242224'),
            ],
            [
                sg.Column(self.general_settings_layout, key=self.gui_general_settings_layout, background_color='#424042' ),
            ],
        ]

        self.cancellation_event = Event() # Set the event until start is called, otherwise we can block if shutdown is called.
        self.cancellation_event.set()
        self.image_queue = Queue()


    def started(self):
        return not self.cancellation_event.is_set()

    def start(self):
        # If we're already running, bail
        if not self.cancellation_event.is_set():
            return
        self.cancellation_event.clear()

    def stop(self):
        # If we're not running yet, bail
        if self.cancellation_event.is_set():
            return
        self.cancellation_event.set()

    def render(self, window, event, values):
        # If anything has changed in our configuration settings, change/update those.
        changed = False

        if self.config.gui_osc_port != int(values[self.gui_osc_port]):
            print(self.config.gui_osc_port, values[self.gui_osc_port])
            try: 
                int(values[self.gui_osc_port])
                if len(values[self.gui_osc_port]) <= 5:
                    self.config.gui_osc_port = int(values[self.gui_osc_port])
                    changed = True
                else:
                    print("\033[91m[ERROR] OSC port value must be an integer 0-65535\033[0m")
            except:
                print("\033[91m[ERROR] OSC port value must be an integer 0-65535\033[0m")

        if self.config.gui_osc_receiver_port != int(values[self.gui_osc_receiver_port]):
            try: 
                int(values[self.gui_osc_receiver_port])
                if len(values[self.gui_osc_receiver_port]) <= 5:
                    self.config.gui_osc_receiver_port = int(values[self.gui_osc_receiver_port])
                    changed = True
                else:
                    print("\033[91m[ERROR] OSC receive port value must be an integer 0-65535\033[0m")
            except:
                print("\033[91m[ERROR] OSC receive port value must be an integer 0-65535\033[0m")

        if self.config.gui_osc_address != values[self.gui_osc_address]:
            self.config.gui_osc_address = values[self.gui_osc_address]
            changed = True

        if self.config.gui_osc_recenter_address != values[self.gui_osc_recenter_address]:
            self.config.gui_osc_recenter_address = values[self.gui_osc_recenter_address]
            changed = True

        if self.config.gui_osc_recalibrate_address != values[self.gui_osc_recalibrate_address]:
            self.config.gui_osc_recalibrate_address = values[self.gui_osc_recalibrate_address]
            changed = True

        if self.config.gui_min_cutoff != values[self.gui_min_cutoff]:
            self.config.gui_min_cutoff = values[self.gui_min_cutoff]
            changed = True
            
        if self.config.gui_speed_coefficient != values[self.gui_speed_coefficient]:
            self.config.gui_speed_coefficient = values[self.gui_speed_coefficient]
            changed = True

        if self.config.gui_flip_x_axis_right != values[self.gui_flip_x_axis_right]:
            self.config.gui_flip_x_axis_right = values[self.gui_flip_x_axis_right]
            changed = True

        if self.config.gui_flip_x_axis_left != values[self.gui_flip_x_axis_left]:
            self.config.gui_flip_x_axis_left = values[self.gui_flip_x_axis_left]
            changed = True

        if self.config.gui_vrc_native != values[self.gui_vrc_native]:
            self.config.gui_vrc_native = values[self.gui_vrc_native]
            changed = True
        
        if self.config.gui_update_check != values[self.gui_update_check]:
            self.config.gui_update_check = values[self.gui_update_check]
            changed = True

        if self.config.gui_video_scale != values[self.gui_video_scale]:
            self.config.gui_video_scale = int(values[self.gui_video_scale])
            changed = True

        if self.config.gui_flip_y_axis != values[self.gui_flip_y_axis]:
            self.config.gui_flip_y_axis = values[self.gui_flip_y_axis]
            changed = True
            
        if self.config.gui_eye_falloff != values[self.gui_eye_falloff]:
            self.config.gui_eye_falloff = values[self.gui_eye_falloff]
            changed = True

        if self.config.gui_ROSC != values[self.gui_ROSC]:
            self.config.gui_ROSC = values[self.gui_ROSC]
            changed = True

        if changed:
            self.main_config.save()
        self.osc_queue.put((EyeId.SETTINGS))