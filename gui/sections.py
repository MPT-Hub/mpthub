import dash_html_components as html
from dash_bootstrap_components import Table


def _section_1():

    materials = html.Div(children=[
        html.H4("Materials"),
        html.Ul(children=[
            html.Li("8-well polystyrene medium chamber"),
            html.Img(src="/assets/8_well.png", alt="8-well chamber"),
            html.Li("Hank's Balanced Salt Solution (HBSS);"),
            html.Li("Purified mucin preparation;"),
            html.Li("Spatula;"),
            html.Li("Weigh boat;"),
            html.Li("Scale;"),
            html.Li("Micropipette/tips;"),
            html.Li("Fluorescence microscope;")])])

    mucin_preparation = html.Div(children=[
        html.H4("Preparation of Purified Mucin samples"),
        html.Ul(children=[
            html.Li(children=[
                "Purified mucin samples are prepared from purified mucin ",
                "type II gastric mucin from porcine stomach ",
                "(Sigma Aldich, St. Louis, MO);",
                html.Ul(html.Li(children=[
                        "Keep Purified type II gastric mucin product stored ",
                        "in the refrigerator;"]))]),
            html.Li(children=[
                "The purified mucin product is reconstituted in ",
                "Hank’s Balanced Salt Solution (HBSS) at 30 mg/ml;"]),
            html.Li(children=[
                "Prepare 1 ml mucin sample by adding 30 mg of the purified ",
                "mucin product to 1 ml of HBSS in a 2 ml eppendorf tube;"]),
            html.Li(children=[
                "Vortex the solution until it appears homogeneous. ",
                html.Strong("NOTE: "), "Make sure there are ",
                "no clumps of mucin stuck to the sides of the tube;"]),
            html.Li(children=[
                "Allow the mucin preparations to equilibrate ",
                "for approximately 30 minutes at room temperature ",
                "before addition of diluted nanoparticle solutions;"])])])

    nanoparticle_preparation = html.Div(children=[
        html.H4("Preparation of Nanoparticle solutions"),
        html.Ul(children=[
            html.Li(children=[
                "Particle solutions are prepared using ",
                "yellow-green fluorescent FluoSpheres ",
                "(Invirogen Molecular Probes, Carlsbad, CA);",
                html.Ul(html.Li(children=[
                    "Keep particle solutions covered with aluminum foil ",
                    "and stored in the refrigerator;"]))]),
            html.Li(children=[
                "200 nm amine-, carboxylate-, and sulfate-modified ",
                "microsphere solutions (2% solids in distilled water ",
                "with 2 mM azide) are diluted in HBSS to yield a final ",
                "particle concentration of approximately 0.0025% wt/vol."]),
            html.Li(children=[
                "Serial dilutions are used to prepare the solutions ",
                "as follows:",
                html.Ul(html.Li(children=[
                    "Prepare in 2 ml eppendorf tubes:",
                    html.Ul(children=[
                        html.Li(children=[
                            "Dilution 1 (D1): 990 ", u"\u03BC",
                            "l HBSS + 10 ", u"\u03BC",
                            "l nanoparticle solution"]),
                        html.Li(children=[
                            "Dilution 2 (D2): 875 ", u"\u03BC",
                            "l HBSS + 125 ", u"\u03BC", "l D1;"])])]))])])])

    protocol = html.Div(children=[
        html.H4("Experimental Protocol"),
        html.Ul(children=[
            html.Li(children=[
                "Pipette 200 ", u"\u03BC", "l aliquots of purified mucus ",
                "samples into 4 wells of the 8-well polystyrene medium ",
                "chamber device;"]),
            html.Li(children=[
                "Pipette 200 ", u"\u03BC", "l aliquots of distilled H2O into ",
                "4 wells of the 8-well polystyrene medium chamber device;"]),
            html.Li(children=[
                "Pipette 10 ", u"\u03BC", "l of nanoparticle solution D2 on "
                "top of the solution in each well. ",
                html.Strong("NOTE: "), "Be sure NOT to ",
                "inject the pipette tip into the mucus sample – ",
                "avoid any unnecessary perturbation of mucin structure."]),
            html.Li(children=[
                "Multiple particle and mucus types can be analyzed at the ",
                "same time using the 8-well chambers. Be sure to indicate ",
                "in your laboratory notebook which chambers contain which ",
                "types of mucus and nanoparticles;"]),
            html.Li(children=[
                "Cover the device (make sure it is not exposed to light) ",
                "and let the samples sit at room temperature for 2 hours ",
                "prior to vídeo microscopy – this allows the particles ",
                "to disperse and the sample to equilibrate."])])])

    section = html.Div(children=[
        materials,
        mucin_preparation,
        nanoparticle_preparation,
        protocol])

    return section


def _section_2():

    config = html.Div(children=[
        html.H4("Microscope configuration (LAS):"),
        html.Ul(children=[
            html.Li("Acquisition tab: x, y, t;"),
            html.Li("Enable auto save"),
            html.Li("Video resolution: 512x512"),
            html.Li("Binning: 2x2"),
            html.Li("Light intensity: max"),
            html.Li("Exposure time: 20 ms"),
            html.Li(children=[
                "Time interval: ",
                "33 ms / frame = 30 FPS (Frames per second)."]),
            html.Li("Video length: 20 s")]),
        html.P(children=[
            html.Strong("NOTE: "),
            "With the configuration above, ",
            "the video should have 606 frames:"]),
        Table(children=[
            html.Thead(children=[
                html.Tr(children=[
                    html.Th("Configuration"),
                    html.Th("Value"),
                    html.Th("Observation")])]),
            html.Tbody(children=[
                html.Tr(children=[
                    html.Td("FPS"),
                    html.Td("30"),
                    html.Td("Setup we need for better video quality")]),
                html.Tr(children=[
                    html.Td("Time interval"),
                    html.Td("33 ms (0.033 s)"),
                    html.Td("")]),
                html.Tr(children=[
                    html.Td("Video length"),
                    html.Td("20 s"),
                    html.Td("= 1 s/FPS = 0.0333333 s")]),
                html.Tr(children=[
                    html.Td("Frames"),
                    html.Td("606"),
                    html.Td(children=[
                        "= vídeo length / time interval =", html.Br(),
                        "= vídeo length * FPS =", html.Br(),
                        "= 600", html.Br(),
                        "We get 606 due to the rounded value ",
                        "of time interval"])])])],
              className="table-hover")])

    section = html.Div(children=[
        config])

    return section


def _section_3():

    section = html.Div(children=[
        html.P(children=[
            "The microscope allows saving the vídeo file in 2 file formats:"]),
        html.Ul(children=[
            html.Li(children=[
                "lif (Leica Image File): ",
                "A project containing several vídeos;"]),
            html.Li(children=[
                "tif (Tagged Image File): ",
                "Each vídeo is represented by one file."])]),
        html.P(children=[
            "The Mosaic Plugin allows us to use either one of these ",
            "formats, but we usually use the 'tif' format. Therefore, ",
            "I will only detail the use of this file format for now. ",
            "When we open the ImageJ (Fiji) application, ",
            "we see the following window."]),
        html.P(html.Img(
            src="/assets/ImageJ_Fiji.png",
            alt="ImageJ/Fiji",
            style={"max-width": "75%"})),
        html.P(children=[
            "From menu ", html.Strong("Particle Tracker 2D/3D"),
            ", under menu ", html.Strong("Plugins > Mosaic"),
            ", open the Mosaic plugin window."]),
        html.P(html.Img(
            src="/assets/Fiji_Mosaic_menu.png",
            alt="Mosaic plugin menu",
            style={"max-width": "75%"})),
        html.P(children=[
            "The plugin configuration used for this research ",
            "was as shown in the image below."]),
        html.P(html.Img(
            src="/assets/Fiji_Mosaic_configuration.png",
            alt="Mosaic plugin default configuration",
            style={"max-width": "75%"})),
        html.P(children=[
            "After clicking 'Ok' button, the video analysis starts. ",
            "Once it concludes, the following ",
            html.Strong("Results"),
            " window will show."]),
        html.P(html.Img(
            src="/assets/Fiji_results.png",
            alt="Mosaic plugin results window",
            style={"max-width": "75%"})),
        html.P(children=[
            "The previous protocol used the ",
            html.Strong("Save Full Report"), " button (1) ",
            "to export a 'txt' report file. ",
            "This is a file containing the detailed report of ",
            "the video analysis."]),
        html.P(children=[
            "This detailed report has hundreds of thousand lines of data, "
            "being less than half of the lines trajectory data.", ]),
        html.P(children=[
            "Nevertheless, since the publication of the Crater Protocol, ",
            "the Mosaic Plugin received new functionalities, such as the ",
            "button", html.Strong("All Trajectories to Table"),
            " (2), which allows to export a 'csv' file with only the ",
            "trajectories data. Clicking on this button will open a ",
            html.Strong("Results"), " window with the trajectories table."]),
        html.P(html.Img(
            src="/assets/Fiji_results_table.png",
            alt="Mosaic plugin results table window",
            style={"max-width": "75%"})),
        html.P(children=[
            "From menu ", html.Strong("Save As"),
            ", under menu ", html.Strong("File"), ", ",
            "a dialog will open to save the 'csv' file."]),
        html.P(html.Img(
            src="/assets/Fiji_results_table_save_as.png",
            alt="'Save as' Mosaic plugin menu on results table window",
            style={"max-width": "75%"})),
        html.P(children=[
            "Once we have all the 'csv' files, from all the captured videos, ",
            "we can proceed to the data analysis using the MPT App."])])

    return section


def _section_4():

    app_installation = html.Div(children=[
        html.H4("App installation"),
        html.P(children=[
            "Just download the latest version for your ",
            "Operating System and use. No need for installation."])])

    app_use = html.Div(children=[
        html.H4("App usage"),
        html.P(children=[
            "This application reads an ImageJ report. ",
            "It only accept the file generated by ",
            "'All Trajectories to Table' button on the Mosaic plugin. ",
            "As this is a '.csv' file, just this file format is allowed. ",
            "If, however, any other file is used, ",
            "the application should just ignore."])])

    app_workflow = html.Div(children=[
        html.H4("The workflow"),
        html.H5("1. Review configuration"),
        html.P(children=[
            "There are some configurations that need to exist ",
            "in order to allow the app to make its calculations. ",
            "There are 3 main configuration groups:"]),

        html.H6("1.1. App configuration"),
        html.P(children=[
            "The App configuration basically means input and output folder. ",
            "The App saves this folder's path in a way to make it easy ",
            "for the user."]),
        html.P(children=[
            "We understand that the user may have a specific folder with ",
            "result files (from ImageJ) and a different one for report files ",
            "(from this App)."]),
        html.P("The default configurations are:"),
        Table(children=[
            html.Thead(
                html.Tr(children=[
                    html.Th("Operating System"),
                    html.Th("Input folder"),
                    html.Th("Output folder")])),
            html.Tbody(children=[
                html.Tr(children=[
                    html.Td("Windows"),
                    html.Td("Linux"),
                    html.Td("Mac OS")]),
                html.Tr(children=[
                    html.Td("C:\\Users\\<username>\\.mpt"),
                    html.Td("/home/<username>/.mpt"),
                    html.Td("/Users/<username>/.mpt")]),
                html.Tr(children=[
                    html.Td("C:\\Users\\<username>\\.mpt\\export"),
                    html.Td("/home/<username>/.mpt/export"),
                    html.Td("/Users/<username>/.mpt/export")])])],
              className="table-hover"),
        html.P(children=[
            "If those folders don't exist, ",
            "they will be created at first App use."]),
        html.P(
            html.Em(
                html.Strong(
                    "The values are saved each time the user uses the App."))),

        html.H6("1.2. Analysis configuration"),
        html.P(children=[
            "This configurations relate to the video acquisition parameters ",
            "(except for the particle size, that usually comes from ",
            "known particle size provided by manufacturer)."]),
        html.P("The default values are:"),
        Table(children=[
            html.Thead(
                html.Tr(children=[
                    html.Th("Configuration"),
                    html.Th("Description"),
                    html.Th("Default value")])),
            html.Tbody(children=[
                html.Tr(children=[
                    html.Td("Size"),
                    html.Td("Particle size (in SI unit nm)"),
                    html.Td("200")]),
                html.Tr(children=[
                    html.Td("Filter"),
                    html.Td(children=[
                        "Minimum number of consecutive frames a trajectory ",
                        "must have to be considered valid for analysis."]),
                    html.Td("590")]),
                html.Tr(children=[
                    html.Td("FPS"),
                    html.Td("Frames per second used for video acquisition."),
                    html.Td("30")]),
                html.Tr(children=[
                    html.Td("Total frames"),
                    html.Td("Total number of frames in video."),
                    html.Td("606")]),
                html.Tr(children=[
                    html.Td("Width (px)"),
                    html.Td("Width of the acquired video, in pixels."),
                    html.Td("512")]),
                html.Tr(children=[
                    html.Td(children=[
                        "Width (", u"\u03BC", "m)"]),
                    html.Td(children=[
                        "Width of the acquired video, in SI unit ",
                        u"\u03BC", "m"]),
                    html.Td("160")])])],
              className="table-hover"),
        html.P(children=[
            "Those values are pre-defined based on previous experiment ",
            "and can be changed in the App."]),
        html.P("The values can be changed, as seen in the screenshot bellow."),
        html.P(html.Img(
            src="/assets/general_config.png",
            alt="General configuration")),

        html.H6("1.3. Diffusivity ranges configuration"),
        html.P(children=[
            "As one of the report generated by the App ",
            "is about diffusivity, the ",
            html.Em("Transport Mode Characterization"),
            " ranges are essential."]),
        html.P("The default values are:"),
        Table(children=[
            html.Thead(children=[
                html.Tr(children=[
                    html.Th("Transport Mode"),
                    html.Th("Lower value"),
                    html.Th("Higher value")])]),
            html.Tbody(children=[
                html.Tr(children=[
                    html.Td("Immobile"),
                    html.Td("0.0"),
                    html.Td("0.199")]),
                html.Tr(children=[
                    html.Td("Sub-diffusive"),
                    html.Td("0.2"),
                    html.Td("0.899")]),
                html.Tr(children=[
                    html.Td("Diffusive"),
                    html.Td("0.9"),
                    html.Td("1.199")]),
                html.Tr(children=[
                    html.Td("Active"),
                    html.Td("1.2"),
                    html.Td("1.2+")])])],
              className="table-hover"),
        html.P("The values can be changed, as seen in the screenshot bellow."),
        html.P(html.Img(
            src="/assets/diffusivity_config.png",
            alt="Diffusivity ranges configuration")),

        html.H5("2. Read the file(s)"),
        html.P(children=[
            "By clicking on the 'Open files' sub-menu, ",
            "under 'File' menu, a dialog appears. ",
            "This dialog allows the user to open multiple files."]),
        html.P(html.Img(
            src="/assets/File_menu_open.png",
            alt="File menu (Open files)")),
        html.P(children=[
            "After reading the files, a summary table will show at ",
            "the main window. This table shows the file name, ",
            "total trajectories and valid trajectories. ",
            "At the bottom of the list, a total is displayed. ",
            "For statistical purposes, approximately 100 valid trajectories ",
            "must exist."]),
        html.P(html.Img(
            src="/assets/files_summary.png",
            alt="Files summary")),

        html.H5("3. Start analysis"),
        html.P(children=[
            "Configuration reviewed, reports loaded to app, ",
            "it is time to make some math."]),
        html.P(children=[
            "Under 'Tools' menu, 'Analyze' sub-menu starts analysis. ",
            "This sub-menu is disable at startup and only becomes enabled ",
            "if the previous step occurs with no errors."]),

        # TODO: Add image (before/after menu)

        html.P(children=[
            "The app must process the data from those files and do a ",
            "series of calculations, described bellow:"]),
        html.Ul(children=[
            html.Li(children=[
                "Keep only those trajectories longer than the minimum frame ",
                "number defined by the filter configuration."]),
            html.Li(children=[
                "Compute MSD (mean squared displacement) for the group ",
                "of results (near 100 trajectories)"]),
            html.Li(children=[
                "Compute D",
                html.Sub("eff"),
                " (effective diffusivity) for the group of results ",
                "(near 100 trajectories)"]),
            html.Li(children=[
                "Compute the slope (",
                html.Em(u"\u03B1"),
                ") for each trajectory"])]),
        html.P(children=[
            "Along the process, the statusbar shows info about ",
            "the overall process."]),
        html.P("When it's done, a dialog informs the user."),

        html.H5("4. Export reports"),
        html.P(children=[
            "Now that analysis has been done, ",
            "the user may export the reports. ",
            "As before, the 'Save' sub-menu, ",
            "under 'File' menu is disabled at ",
            "startup. It becomes enabled only after analysis, if ok."]),

        # TODO: Add image (before/after menu)

        html.P("There are currently 3 reports available:"),

        html.H6("4.1. Individual Particle Analysis"),
        html.P("This report contains 5 sheets, described bellow:"),
        html.P(html.Img(
            src="/assets/Individual_Particle_Analysis-sheets.png",
            alt="Individual Particle Analysis report sheets")),

        html.P(html.Strong("4.1.1. Data")),
        html.P(children=[
            "This sheet contains the data from each valid trajectory ",
            "Mean-squared Displacement (MSD) and Diffusivity efficiency ",
            "coefficient (D",
            html.Sub("eff"),
            ")."]),
        html.P(html.Img(
            src="/assets/Individual_Particle_Analysis-data.png",
            alt="Individual Particle Analysis report data",
            style={"max-width": "100%"})),

        html.P(html.Strong("4.1.2. <MSD> vs Time")),
        html.P(children=[
            "This sheet contains the Ensemble Mean-squared Displacement ",
            "(<MSD>) plot."]),
        html.P(html.Img(
            src="/assets/Ensemble_MSD_plot.png",
            alt="Ensemble MSD plot",
            style={"max-width": "75%"})),

        html.P(html.Strong("4.1.3. MSD vs Time")),
        html.P(children=[
            "This sheet contains the MSD (mean squared displacement) ",
            "plot with all trajectories."]),
        html.P(html.Img(
            src="/assets/Individual_MSD_plot.png",
            alt="Individual MSD plot",
            style={"max-width": "75%"})),

        html.P(html.Strong("4.1.4. <Deff> vs Time")),
        html.P(children=[
            "This sheet contains the Ensemble effective diffusivity (<",
            html.Em(children=[
                "D", html.Sub("eff")]),
            ">) chart."]),
        html.P(html.Img(
            src="/assets/Ensemble_Deff_plot.png",
            alt="Ensemble Deff plot",
            style={"max-width": "75%"})),

        html.P(html.Strong("4.1.5. Deff vs Time")),
        html.P(children=[
            "This sheet contains the effective diffusivity (",
            html.Em(children=[
                "D", html.Sub("eff")]),
            ") plot with all trajectories."]),
        html.P(html.Img(
            src="/assets/Individual_Deff_plot.png",
            alt="Individual Deff plot",
            style={"max-width": "75%"})),

        html.H6("4.2. Transport Mode Characterization"),
        html.P("This report have 3 sheets, described bellow:"),
        html.P(html.Img(
            src="/assets/Transport_Mode_Characterization-sheets.png",
            alt="Transport Mode Characterization report sheets")),

        html.P(html.Strong("4.2.1. Data")),
        html.P(children=[
            "This sheet contains the data from each valid trajectory ",
            "Mean-squared Displacement (MSD) in logarithm scale."]),
        html.P(html.Img(
            src="/assets/Transport_Mode_Characterization-data.png",
            alt="Transport Mode Characterization report data",
            style={"max-width": "100%"})),

        html.P(html.Strong("4.2.2. MSD vs Time")),
        html.P(children=[
            "This sheet contains the Mean-squared Displacement (MSD) ",
            "log-log plot with all trajectories."]),
        html.P(html.Img(
            src="/assets/Transport_Mode_Characterization-plot.png",
            alt="Transport Mode Characterization report MSD plot (log-log)",
            style={"max-width": "75%"})),

        html.P(html.Strong("4.2.3. Characterization")),
        html.P("This sheet contains:"),
        html.Ul(children=[
            html.Li("List os all valid trajectories slopes;"),
            html.Li("Transport Mode Characterization table count;"),
            html.Li("Summary information:"),
            html.Ul(children=[
                html.Li(children=[
                    html.Strong("<slope>"),
                    ": Slope average;"]),
                html.Li(children=[
                    html.Strong("N"),
                    ": Number of slopes ",
                    "(equal number of valid trajectories);"]),
                html.Li(children=[
                    html.Strong("STD"),
                    ": Standard Deviation."])])]),
        html.P(html.Img(
            src="/assets/Transport_Mode_Characterization-characterization.png",
            alt="Transport Mode Characterization report sheets",
            style={"max-width": "75%"})),

        html.H6("4.3. Einstein-Stokes Calculation - D0_Dw-Microviscosity"),
        html.P(children=[
            "This report have only 1 sheet, named ",
            html.Em(html.Strong("Microviscosity")), "."]),
        html.P(children=[
            "It contains the data for calculating microviscosity, ",
            html.Em(children=["D", html.Sub("0"), "/D", html.Sub("W")]),
            " ratio and some other intermediate calculations."]),
        html.P(children=[
            "For the Einstein-Stokes, ",
            "the particle size is considered to be of ",
            html.Em("200 nm"), "*."]),
        html.P(html.Strong(children=[
            "The particle size can be changed, as mentioned on item ",
            html.Em("1.2. Analysis configuration")]))

        # TODO: Add image (print)
    ])

    section = html.Div(children=[
        app_installation,
        app_use,
        app_workflow])

    return section
