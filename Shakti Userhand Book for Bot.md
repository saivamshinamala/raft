#### **CHAPTER – I**

## **LEADING PARTICULARS AND GENERAL DATA**

- **1.1 Introduction**.Shakti is a ship-borne advanced EW suite with the capability to intercept and identify modern exotic radars including LPI emitters. The EW system is designed for capital ships of Indian Navy with Electronic Support (ES) system covering the frequency band from 175 MHz to 40 GHz and Electronic Attack (EA) System covering threat radar frequency band of 6 to 40 GHz. The ES system also provides integral Radar Finger Printing System (RFPS) for fine grain intra pulse analysis and inter pulse analysis of the emitters that operate in the frequency range of 0.175 to 40 GHz. It is manufactured by Bharat Electronics Ltd and it is Designed and developed by DLRL, Hyderabad.
- 1.1.1 The ES System provides automatic and instantaneous detection, direction finding, analysis, classification and identification of pulsed or continuous wave (CW) radar emissions in 0.175 to 40 GHz frequency band with 360 degrees coverage in azimuth. The ES system has broad band and narrow band operation to meet the tactical and strategic needs of the Navy. Broad band operation is achieved by employing a Wide Open Receiver, which achieves 100% Probability of Intercept (POI), whereas the narrow band receiver helps in achieving higher sensitivity and better Range Advantage Factor (RAF) against Low Probability of Intercept (LPI) radars.
- 1.1.2 The EA system covering frequency band of 6-40 GHz employs high power jammers with state of art technologies using Digital RF Memory (DRFM) and associated techniques generator and Microwave Power Modules (MPMs) to effectively counter the modern radars. The EA system is split into two bands, 6-18 GHz and 18-40 GHz band. The EA system is configured into two identical sub-systems, each covering 180˚ sector on the ship platform one each on Port & Starboard sides. These are supported by a common EA processor for interface with ES system, control and power management of total EA system. The system is capable of handling ten (10) threats simultaneously covering 360 (i.e., four threats per sector of 180 in 6-18 GHz band and one threat per sector of 180 in 18-40 GHz band).
- 1.1.3 The system has high speed signal processing capability to enable detection, measurement, analysis, identification and jamming in the shortest possible time. The system provides highly interactive Human-Machine Interface (HMI) features in the Operation Console. The system is also equipped with Built-in-Test Equipment (BITE) facility for continuous health monitoring of system and fault identification up to Module / PCB level. The operational status of various sections of the system is presented on the Operation console. Separate indications and controls are provided on individual

SHAKTI : UHB\Ch1 Page 1 of 614

subsystems for status monitoring as well as for local operations.

1.1.4 This chapter describes about the Functionality, System Configuration, Features/Facilities, Technical Specifications, Power Supply Requirements, Environmental Specifications, EMC/EMI Specifications and Dimensions & Weights of the Shakti System.

#### **1.2 Brief Functions**. The System performs the following functions:

- (a) **ES**. Automatic and instantaneous detection, direction finding, analysis, classification and identification of pulsed or continuous wave (CW) radar emissions in 0.175 to 40 GHz frequency band with 360º coverage in azimuth. The information displayed includes Frequency in MHz, Pulse Width (PW) in µs, Pulse Repetition Frequency (PRF) in Hz, Direction of Arrival (DOA) in degrees, Antenna Scan Period (ASP) in seconds, Amplitude in dBm etc. The system provides very accurate system parameters within its frequency and dynamic range.
- (b) **LPI Search and Analysis**. Automatic search, intercept and identification of low power LPI radars with exotic emissions, namely, chirp, FM-CW, Barker codes etc. (Eg. ELTA MK-III Radar in LPI mode, Fregat on LPI, Garpoon BAL-II etc.).
- (c) **Library Upload/ Download/ Configuration and Emitter Match**. Upload/download /configure a series of libraries (emitter/operator) that can be used to identify the emitters detected by the system.
- (d) **Radar Finger Printing**. The system supports built-in Radar Finger Printing unit for Inter and Intra-pulse analysis and identification of an emitter chosen by the operator.
- (e) **EA**. Intercept and initiate Jamming in co-ordination with ESM system in semiauto, auto & manual mode of operation. Tracking and jamming often (10) threats simultaneously in time sharing mode covering 360 (i.e four threats per sector of 180 in 6-18 GHz band and one threat per sector of 180 in 18-40 GHz band) and also covering even in overlap sectors. It is configured with noise and deception jamming techniques to handle against coherent (modern Pulse compression (PC)/ Pulse Doppler radars) and non-coherent threats having an ERP of 50 KW in 6-18 GHz band and 10 KW in 18-40 GHz band.
- (f) **Self-Test/BITE**. The system verifies its own operational status by carrying out a self-test. The operator is provided with a diagnostic report on each of the system modules. The built-in BITE assists maintainers in quick diagnosis/identification of faults and thereby reduces the down time of the system.

SHAKTI : UHB\Ch1 Page 2 of 614

- (g) **Interfacing with Onboard Units**. The system provides interface with onboard units like Gyro, GPS, CMS, LRSAM, KAVACH (Chaff), Own radar blanking and Printer.
- (h) **Training**. The system has training mode to facilitate operator training (the simulator mode for testing the system in stand-alone mode with required parameter generation, which can be generated by simulator).
- **1.3 System Configuration**.To meet the operational requirements, Shakti EW System for Capital Ships is configured to cover the radar frequency band of 0.175–40 GHz for ES System and 6–40 GHz for EA System. The EW system block diagram is as shown in Figure 1.1.
- **1.3.1 ES Segment**. The frequency coverage of 0.175 40 GHz is achieved in the split bands of 0.175-0.5 GHz, 0.5 - 2 GHz, 2-6 GHz, 6-18 GHz, 2.2-18 GHz and 18-40 GHz as shown in Shakti ES configuration diagram in Figure 1.2.
  - (a) The parameters measured by the receivers are:
    - (i) Frequency
    - (ii) Direction of arrival (DOA)
    - (iii) Amplitude
    - (iv) Pulse width
    - (v) Time of arrival etc.
    - (vi) These parameters measured are formatted into Pulse Descriptor Words (PDWs) and sent to ESM Processor over fiber optic links.
  - (b) Narrow Band Receiver of 0.175 to 0.5 GHz measures Direction of Arrival (DOA) using phase comparison technique.
  - (c) Wide open Receivers are essential for providing high POI (≈100%) to meet tactical operational requirements in 2.2-40 GHz frequency band.
    - (i) Homodyne Receivers (2.2-18 GHz) operating in wide-band mode employ Base Line Interferometer (BLI) technique in 2.2-18 GHz band for interception, analysis and high accuracy DOA measurement.
    - (ii) Four set of Omni antennas are placed with a baseline distance of 10 mtrs square to measure direction of arrival by TDOA technique.

SHAKTI : UHB\Ch1 Page 3 of 614

- (d) Narrow Band Receivers with instantaneous bandwidth of 40 MHz/ 500 MHz are employed in 0.5 – 2 GHz, 2-6 GHz & 6-18 GHz Bands and instantaneous bandwidth of 500 MHz is employed in 4 to 18 GHz bands to provide high sensitivity and high parameter accuracy. Use of state of the art Super het Receivers & Digital Receivers enables detection and analysis of LPI & Complex radar signals and also processing of simultaneous (time coincidence) signals with enhanced parameter accuracies.
- (e) The system also employs 2.2 18 GHz & 18 40 GHz Omni channels for standalone Radar Finger Printing facility. The RFPS will carry out both inter and intra pulse analysis in offline mode. It performs data acquisition, processing and analysis of Finger Printing data and displays the results in an independent RFPS monitor, in operator selectable format as per the User approved MMI.
- (f) **ES Processor**. Its de-interleaves the PDWs, builds the emitter tracks and sends Emitter Track data to System Controller over Ethernet.

## (g) **System Controller & Display**:

- (i) It presents the ESM track data on Display to operator.
- (ii) It also controls the subsystems of Shakti for ESM operation and provides HMI to EW operator for system operation.
- (iii) It also supports for operation of Shakti in CMS Controlled Integrated mode and play back for mission analysis.

#### (h) **RFPS**:

- (i) It caters for the requirement of inter/intra pulse analysis and emitter identification for an emitter designated by the operator from System Controller & Display.
- (ii) There is a separate display for RFPS to present fine grain parameters and emitter identification results.
- (iii) RF Tuner down converts multiplexed RF from Broad Band Receiver or Narrow Band Receiver to IF (Instantaneous Frequency) for radar finger printing.
- (j) The Operator console has two control monitors. First one is a primary monitor which shows the HMI Presentation and second monitor is an auxiliary monitor which shows RFPS analyzed data.

SHAKTI : UHB\Ch1 Page 4 of 614

- (k) The system has a Mission Library (20,000 radar entries) for emitter identification purpose. Out of these 20,000 radars entries, the first 500 will be Warner (Threats), the next 11,500 will be Priority and the rest 8,000 will be Non-Priority radar entries. Mission Library shall be provided by EWOSC (Navy). Moreover, operator can add newly detected emitters provided there is space in Mission Library (i.e. less 20,000 entries).
- **1.3.2 EA Segment**.The frequency coverage of 6 40 GHz is achieved in the two split bands of 6-18 GHz and 18-40 GHz as shown in Shakti EA configuration diagram in **Figure 1.3.**
  - (a) **6-18 Jammer**. The main constituents of a 6-18 GHz Jammer are MB2- Front End Assy, Low power Unit (MB2) and MB2-Transmitter unit. The MB2-Tx Unit along with MB2-FE Assy will be mounted on a single-axis Servo pedestal controlled by single-axis servo controller, so that the main lobe of the jammer will always be pointing towards the emitter. The MB2-Tx Unit and LP Unit (MB2) will be cooled using heat exchanger Unit by taking cooled water from the ship. The Microwave Power Modules (MPMs) are used as high power amplifiers in MB2-Tx Unit which requires 270 V DC. There will be two 6-18 GHz Jammers which are identical, one for the port side and other for the starboard side.
  - (b) **18-40 Jammer**. The main constituents of an 18-40 GHz Jammer are Front End Unit (HB), Low power Unit (HB), Transmitter Unit (HB), and Transmitter Power Supply (HB). Front End Unit (HB) and Transmitter Unit (HB) will be mounted on a two-axis Servo pedestal controlled by two-axis servo controller. The LP Unit (HB) will be cooled using heat exchanger Unit by taking cooled water from the ship. Transmitter Power Supply (HB) generates the DC Voltages which are required for the Transmitter-HVPS Unit in the Transmitter Unit (HB).In the Transmitter Unit, the high voltages will be generated in the Transmitter-HVPS Unit which is required for the TWT. There will be two 18-40 GHz Jammers which are identical, one for the port side and other for the starboard side.
  - (c) **EA Processor**. All the four jammers (two 6-18 GHz jammers and two 18-40 GHz jammers) will be controlled by a common EA Processor. This EA Processor will interact with the ES System through ES processor or System controller and Display (SCD) to get the information regarding the threat to be engaged by the EA system and to pass on the operational status of the EA System.

SHAKTI : UHB\Ch1 Page 5 of 614

**1.3.3 Equipment List**. The Shakti System has 18 major assemblies/units as listed in **Table 1.1**.

**Table-1.1: Units / Sub-units**

| Ser | BEL Part No.  | Sub System Description             | Qty |  |  |
|-----|---------------|------------------------------------|-----|--|--|
|     | ES SUB-SYSTEM |                                    |     |  |  |
| 1   | 172300352518  | ES AHU-1                           | 1   |  |  |
| 1.1 | 172300685616  | LB(175-500 MHz) ANTENNA ARRAY      | 1   |  |  |
| 1.2 | 172300676983  | ASU (LB1-SHAKTI)                   | 1   |  |  |
| 2   | 172300352615  | ES AHU-2                           | 1   |  |  |
| 2.1 | 172300347377  | OMNI Rx MODULE                     | 2   |  |  |
| 2.2 | 172300347474  | OMNI MASS MODULE                   | 1   |  |  |
| 2.3 | 172300646331  | BB & NB Rx(LB2-MB)                 | 1   |  |  |
| 3   | 172300352712  | ES AHU-3                           | 4   |  |  |
| 4   | 172300352809  | ES AHU-4                           | 1   |  |  |
| 5   | 172300352906  | ES RACK-1                          | 1   |  |  |
| 5.1 | 172300347668  | RX PROCESSOR LRU                   | 1   |  |  |
| 5.2 | 172300347765  | ESM PROCESSOR                      | 1   |  |  |
| 5.3 | 172300348056  | CONTROL UNIT(ES RACK-1)            | 1   |  |  |
| 6   | 172300353003  | ES RACK-2                          | 1   |  |  |
| 6.1 | 172300683482  | Multi Channel RF Unit (LB1-SHAKTI) | 1   |  |  |
| 6.2 | 172300683385  | Receiver Processor (LB1)           | 1   |  |  |
| 6.3 | 172300347862  | LVPS-1                             | 1   |  |  |
| 6.4 | 172300347959  | LVPS-2                             | 1   |  |  |
| 6.5 | 172300654285  | RFPS WBT & Processor LRU           | 1   |  |  |
| 6.6 | 172300705792  | Power Supply (AHU 1-LB1)           | 1   |  |  |

SHAKTI : UHB\Ch1 Page 6 of 614

| Ser  | BEL Part No. | Sub System Description          | Qty |
|------|--------------|---------------------------------|-----|
| 7    | 172300353197 | System Controller & Display     | 1   |
| 7.1  | 172300348153 | SCD Processor                   | 1   |
| 7.2  | 480678060143 | Wired Console Assembly          | 1   |
| 8    | 172300353488 | Rugged Ethernet Switch (TYPE-1) | 2   |
| 9    | 172300353585 | Rugged Ethernet Switch (TYPE-2) | 2   |
| 11   | 172300353391 | Field Data Loader (FDL)         | 1   |
| 12   | 172300353682 | Fault Diagnostic Rack (FDR)     | 1   |
|      |              | EA SUB-SYSTEM                   |     |
| 13   | 172300353779 | EA RACK-1                       | 1   |
| 13.1 | 172300346989 | EA Control Panel                | 1   |
| 13.2 | 172300441176 | Low Voltage Power Supply(MB2)   | 2   |
| 13.3 | 172300441273 | Low Voltage Power Supply(HB)    | 1   |
| 14   | 172300353876 | EA RACK-2                       | 1   |
| 14.1 | 172300452428 | Servo Control Unit (1-AXIS)     | 1   |
| 14.2 | 172300452525 | Servo Control Unit (2-AXIS)     | 1   |
| 15   | 172300353973 | MB2 JAMMER                      | 2   |
| 15.1 | 172300346407 | Low Power Unit (MB2)            | 1   |
| 15.2 | 172300785526 | MB2-Tx Unit                     | 1   |
| 15.3 | 172300785429 | MB2-Front End Assy              | 1   |
| 15.4 | 172300452234 | Servo Drive Assembly (1-AXIS)   | 1   |
| 16   | 172300354070 | HB JAMMER                       | 2   |
| 16.1 | 172300346601 | Front End Unit (HB)             | 1   |
| 16.2 | 172300346795 | Low Power Unit (HB)             | 1   |
| 16.3 | 172300346892 | Transmitter Unit (HB)           | 1   |

SHAKTI : UHB\Ch1 Page 7 of 614

| Ser  | BEL Part No. | Sub System Description         | Qty |
|------|--------------|--------------------------------|-----|
| 16.4 | 172300452719 | Transmitter-HVPS (HB)          | 1   |
| 16.5 | 172300452622 | Transmitter Power Supply(HB)   | 1   |
| 16.6 | 172300452331 | Servo Drive Assembly (2-AXIS)  | 1   |
| 17   | 172300354264 | Transmitter-Power Supply (MB2) |     |
| 18   | 172300354167 | Heat Exchanger Unit            | 2   |

- **1.4 Technical Specifications**.The Technical Specifications of Shakti EW System are as follows.
- **1.4.1 Technical Specifications of Shakti ES & EA Segment**.The technical specifications of Shakti ES & EA Segment are given in Table -1.2.

**Table-1.2: Technical Specifications of ES & EA Segments**

| Ser | Requirements                               |                                 | Specification                                                                     |
|-----|--------------------------------------------|---------------------------------|-----------------------------------------------------------------------------------|
|     |                                            |                                 | ES System<br>:                                                                    |
| 1   |                                            | Frequency Coverage              | 0.175 –<br>40 GHz                                                                 |
| 2   | DF Accuracy                                |                                 | 0.175-2.2 GHz =<br>3°RMS<br>2.2-18 GHz<br>=<br>2° RMS<br>18-40 GHz<br>=<br>3° RMS |
| 3   | Frequency<br>Measurement<br>Accuracy (RMS) |                                 | 2 MHz, 500 KHz in RFPS                                                            |
| 4   | Spatial Coverage                           |                                 | Azimuth<br>= 360˚<br>Elevation = -10° to +30°                                     |
| 5   | Probability of Intercept                   |                                 | 100%                                                                              |
| 6   |                                            | Sensitivity (in radiation mode) |                                                                                   |
| 6.1 | Narrow                                     | 0.175 –<br>0.5 GHz              | -45 ± 5 dBm                                                                       |
|     | Band                                       | 0.5 –<br>2.2 GHz                | -60 ± 5 dBm                                                                       |
|     |                                            | 2.2 –<br>6 GHz                  | -75 ± 5 dBm (Pulsed)<br>-85 ± 5 dBm (CW)                                          |
|     |                                            | 6-18 GHz                        | -80 ± 5 dBm (Pulsed)<br>-90 ± 5 dBm (CW)                                          |

SHAKTI : UHB\Ch1 Page 8 of 614

| Ser |                                 | Requirements          | Specification                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-----|---------------------------------|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 6.2 | Wide                            | 2–<br>18 GHz          | -60 ± 5 dBm                                                                                                                                                                                                                                                                                                                                                                                                                      |
|     | Band<br>18 –<br>40 GHz,         |                       | -55± 5 dBm                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 7   | Sensitivity Flatness            |                       | + 5 dB over frequency & temperature                                                                                                                                                                                                                                                                                                                                                                                              |
| 8   | Dynamic Range                   |                       | 60 dB in Wide band                                                                                                                                                                                                                                                                                                                                                                                                               |
|     |                                 |                       | 40 dB in Narrow band                                                                                                                                                                                                                                                                                                                                                                                                             |
| 9   | Automatic Tracking              |                       | 500                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 10  | Signal Types                    |                       | Frequency Types -<br>Pulse, CW, Frequency<br>Agile (Agile: Random, Periodic, Ramp & Fix,<br>Agile Batch: up to 16 values, 8-512 pulses<br>for batch), FMCW, Chirp, Phase coded &<br>phase modulated.<br>PRI types -<br>Fixed, Jitter(30%), Staggered(16<br>levels),Dwell & Switch( up to 16 values, 10<br>to<br>100<br>m<br>sec<br>dwell<br>time),Sliding<br>PRI,<br>Wobulated PRI<br>Pulse Compression.<br>Amplitude modulated. |
| 11  | Pulse Density                   |                       | 0.175-2.2 GHz ≥ 500 kpps (kilo pulses per<br>second).<br>2.2-18 GHz ≥ 1.0 million pulses per second<br>(mpps)<br>18-40 GHz ≥ 500 kpps                                                                                                                                                                                                                                                                                            |
| 12  | Scan Types                      |                       | Circular,<br>Sector,<br>Complex<br>&<br>Lock-on,<br>Raster, Uni-bi directional, AESA and Track<br>While Scan                                                                                                                                                                                                                                                                                                                     |
| 13  | Antenna Weight                  |                       | < 320 Kg                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 14  | Provisioning of Map<br>Overlays |                       | Moving Map Feature                                                                                                                                                                                                                                                                                                                                                                                                               |
| 15  | Interfaces                      |                       | CMS, Radar, GPS, Gyro, Chaff, LRSAM and<br>Printer                                                                                                                                                                                                                                                                                                                                                                               |
| 16  |                                 | Radar Finger Printing | Integrated<br>RFPS<br>(over<br>entire<br>range<br>of<br>RFPS) for detailed inter and intra pulse<br>analysis<br>with<br>separate display on<br>same<br>console, with a facility to store and modify                                                                                                                                                                                                                              |

SHAKTI : UHB\Ch1 Page 9 of 614

| Ser | Requirements               | Specification                                                                                                                                                                                        |
|-----|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     |                            | the RFPS emitter database on line and<br>offline.<br>RFPS<br>data<br>base<br>shall<br>be<br>capable<br>of<br>uploading / down loading data on LAN /<br>external hardware                             |
| 17  | Polarisation               | Slant, Vertical, Horizontal, LH Circular, RH<br>Circular Polarisation.                                                                                                                               |
| 18  | Additional Features        | FMOP (Frequency Modulation on Pulse)<br>detection                                                                                                                                                    |
|     |                            | Audio<br>and<br>visual<br>warning<br>required<br>for<br>Locked-<br>on,<br>FCR,<br>Missile<br>Illuminators,<br>Active Missile seekers                                                                 |
|     |                            | Alarm<br>for<br>threat<br>Warner<br>library<br>match.<br>Operator has to configure this option.                                                                                                      |
|     |                            | Recording capability                                                                                                                                                                                 |
|     |                            | Post<br>Mission<br>Data<br>Analysis<br>&<br>Mission<br>Planning facility                                                                                                                             |
|     |                            | Programmable blanking of ES sub systems<br>and programmable blanking of transmission<br>of EA sub system to cater for simultaneous<br>operation of EA and other FCRs and radio<br>emitters on board. |
|     |                            | Indication of pulse density & Blanking rate                                                                                                                                                          |
|     |                            | In built training simulator                                                                                                                                                                          |
| 19  | Additional Issues          | Capability to handle modern radars with<br>adequate RAF                                                                                                                                              |
|     |                            | Should<br>provide<br>RAF<br>against<br>LPI<br>based<br>Navigational radars with range of 25 Nm (Tx<br>power of the order of 1 Watt)                                                                  |
| 20  | Pulse Width Range          |                                                                                                                                                                                                      |
|     | 0.175 –<br>2.2 GHz         | 200ns –<br>1ms                                                                                                                                                                                       |
|     | 2.2 –<br>18 GHz            | 50ns–<br>1ms& CW                                                                                                                                                                                     |
|     | 18 -<br>40 GHz<br>Accuracy | 50ns –<br>1ms                                                                                                                                                                                        |

SHAKTI : UHB\Ch1 Page 10 of 614

| Ser | Requirements                    | Specification                                                                                                                                                                                                                                                                                                                                    |
|-----|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     | 0.175 –<br>2.2 GHz              | 10% or 30 ns whichever is higher for PW <=                                                                                                                                                                                                                                                                                                       |
|     | 2.2 –<br>40 GHz                 | 1 µs                                                                                                                                                                                                                                                                                                                                             |
|     |                                 | 1% or 100 ns whichever is higher for PW > 1                                                                                                                                                                                                                                                                                                      |
|     |                                 | µs                                                                                                                                                                                                                                                                                                                                               |
| 21  | Amp Measurement Accuracy        | + 2 dB                                                                                                                                                                                                                                                                                                                                           |
| 22  | PRF Range                       | 50 Hz to 500 KHz                                                                                                                                                                                                                                                                                                                                 |
| 23  | PRF Types                       | Fixed, Jitter, stagger, Dwell & Switch, Slide<br>and Wobulated PRI                                                                                                                                                                                                                                                                               |
| 24  | PRF Accuracy                    | 1 Hz up to 500 Hz,                                                                                                                                                                                                                                                                                                                               |
|     |                                 | 0.4% in 501 Hz to 20 KHz                                                                                                                                                                                                                                                                                                                         |
|     |                                 | 2 % above 20 KHz                                                                                                                                                                                                                                                                                                                                 |
| 25  | Emitter In Warner Library       | 500                                                                                                                                                                                                                                                                                                                                              |
| 26  | Emitters Identification Library | 20,000 emitters                                                                                                                                                                                                                                                                                                                                  |
| 27  | Processing Time                 | < 500 ms for wide open mode                                                                                                                                                                                                                                                                                                                      |
| 28  | Environmental and EMI/EMC       | As per JSS 55555 and                                                                                                                                                                                                                                                                                                                             |
|     |                                 | MIL STD 461 E                                                                                                                                                                                                                                                                                                                                    |
| 29  | Software                        | As per IEEE 12207                                                                                                                                                                                                                                                                                                                                |
| 30  | BITE / Diagnostics              | RF Analog and digital-<br>PCB and module<br>level                                                                                                                                                                                                                                                                                                |
| 31  | Power Supply                    | Platform compatible                                                                                                                                                                                                                                                                                                                              |
| 32  | Antenna Housing                 | Suitable protection from weather elements.                                                                                                                                                                                                                                                                                                       |
| 33  | Modes of Operation              | Wide open, LPI, Scan, Mission Directed<br>search                                                                                                                                                                                                                                                                                                 |
| 34  | Display                         | Standard display consoles for following:-<br>(i) ES Display for presenting tactical data in<br>Tabular, Tactical or Situational formats for<br>system controller operations<br>(ii) Finger printing display for controlling<br>modes of LPI and RFPS processor and<br>displaying intra-pulse features in graphical<br>as well as textual formats |
| 35  | Field Data Loader               | Compatible<br>field<br>data<br>loader<br>for<br>uploading/downloading<br>of<br>library<br>data                                                                                                                                                                                                                                                   |

SHAKTI : UHB\Ch1 Page 11 of 614

| Ser | Requirements          | Specification                                                                                                                                                                  |  |
|-----|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
|     |                       | (including RFPS data)                                                                                                                                                          |  |
|     |                       | EA System :                                                                                                                                                                    |  |
| 36  | Frequency Range       | 6-40 GHz                                                                                                                                                                       |  |
| 37  | Jammer Type           | 6-40 GHz Using latest Jammer technologies                                                                                                                                      |  |
| 38  | Sensitivity           | -60 ±5 dBm in 6-40 GHz                                                                                                                                                         |  |
| 39. | Selectable Band Width | 100 MHz, 300 MHz, 500 MHz , 1000 MHz                                                                                                                                           |  |
| 40  | DRFM                  | 8 threats in 6-18 GHz and 2 threats in 18 to<br>40 GHz.                                                                                                                        |  |
|     |                       | IBW of 1 GHz.                                                                                                                                                                  |  |
|     |                       | Storage length 6 ms per unit.                                                                                                                                                  |  |
| 41  | PRF Range             | 50 Hz -<br>250 KHz.                                                                                                                                                            |  |
| 42  | Min pulse width       | 50 ns to 100 ns (Noise Jamming and Angle<br>Deception).<br>100nsec to 125ns for remaining jamming<br>modes.                                                                    |  |
| 43  | ERP                   |                                                                                                                                                                                |  |
|     | 6-18 GHz              | 50<br>KW<br>(average<br>over<br>the<br>selected<br>bandwidth) in adjustable power output levels<br>of 10KW, 25KW & 50KW.                                                       |  |
|     | 18-40 GHz             | 10 KW                                                                                                                                                                          |  |
| 44  | Threat Handling       | Simultaneous handling of 8 threats for<br>6-<br>18 GHz band and 2 threats for 18-40 GHz<br>band.                                                                               |  |
| 45  | Noise Jamming         | Spot, barrage, multiple simultaneous spots,<br>DBN, cover pulse.<br>{Each JPL should have at least 3 responses<br>with response time (in sec) programmer<br>selectable}        |  |
| 46  | Deception Jamming     | RGPO,<br>RGPI,<br>VGPO,<br>VGPI,<br>RANRAP,<br>Range FT (16 Nos), Velocity FT (4 Nos),<br>Scan Rate Modulation, Swept Scan Rate<br>Modulation, Blink & combination techniques. |  |

SHAKTI : UHB\Ch1 Page 12 of 614

| Ser | Requirements                                                            | Specification                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |  |
|-----|-------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|     |                                                                         | {Each JPL should have at least 3 responses<br>with response time (in sec) programmer<br>selectable).                                                                                                                                                                                                                                                                                                                                                                                                                                 |  |  |
| 47  | Beam Width                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  |  |
|     | 6-18 GHz                                                                | Min in Elevation =<br>10°±1°<br>Min in Azimuth<br>=<br>6.5°±1°                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |  |  |
|     | 18-40 GHz                                                               | Min in Elevation & Azimuth = 6.5°±1°                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |  |  |
| 48  | Polarization                                                            | Slant 45°                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |  |  |
| 49  | Reaction Time from Standby<br>Mode.                                     | 02 Sec (Max) for Multi-Beam jammer.<br>05 Sec (Max) for 18-40 GHz (if servos are<br>used, then this time shall be inclusive of the<br>time required for servos to position the<br>jammer towards the threat direction). Note: -<br>If<br>servos<br>are<br>provided<br>for<br>18-40<br>GHz,<br>operator shall be able to preposition the<br>jammer in desired direction even without the<br>availability of threat signal. This facility shall<br>be provided to ensure better reaction times if<br>the direction of threat is known. |  |  |
| 50  | Steering Accuracy                                                       | 1° (One degree)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  |  |
| 51  | in library.                                                             | Manual mode Jamming as well as Auto mode Jamming for designated threat                                                                                                                                                                                                                                                                                                                                                                                                                                                               |  |  |
|     | Jammer programming, Jammer tuning capability and validation capability. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  |  |
|     | manually even in absence of any threat signal.                          | Capability to transmit jamming signal on desired frequency and direction                                                                                                                                                                                                                                                                                                                                                                                                                                                             |  |  |
|     | & RGPO                                                                  | Availability of pre-programmed jammer programs for Noise jamming, AGPO<br>for use against threats where programmed JPLs are not available.                                                                                                                                                                                                                                                                                                                                                                                           |  |  |

## **1.4.2 Technical Specifications of RFPS**.The Technical Specifications of RFPS are as follows.

**Table-1.3: Technical Specifications of RFPS**

|  | Ser | Parameter | Specification |
|--|-----|-----------|---------------|
|--|-----|-----------|---------------|

SHAKTI : UHB\Ch1 Page 13 of 614

| Ser | Parameter                                                        | Specification                                                                                                                                                                                                                            |
|-----|------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | Input Signal Frequency<br>Range                                  | 0.175 GHz to 40 GHz                                                                                                                                                                                                                      |
| 2   | Operational Sensitivity<br>(160 MHz IF with 40 MHz<br>bandwidth) | 0.175-0.5 GHz : -45 ± 5 dBm<br>0.5-2.2 GHz<br>:<br>-60 ± 5 dBm<br>2.2-18 GHz<br>: -70 ± 5 dBm (Omni path)<br>2.2-6 GHz<br>: -75 ± 5 dBm (Narrow Band path)<br>6-18 GHz<br>: -80 ± 5 dBm (Narrow Band path)<br>18-40 GHz<br>: -55 ± 5 dBm |
| 3   | Dynamic Range                                                    | 40 dB                                                                                                                                                                                                                                    |
| 4   | Frequency Measurement<br>Accuracy                                | 500 KHz RMS                                                                                                                                                                                                                              |
| 5   | Signal Types:                                                    |                                                                                                                                                                                                                                          |
|     | Frequency Types                                                  | Pulsed, CW, FMCW, Frequency Agile, (Pulse<br>Pulse Agility / Scan-<br>Scan Agility).                                                                                                                                                     |
|     | PRF Types                                                        | Fixed, Jitter (30%), Stagger (128 Levels), Dwell &<br>Switch (32 Levels), Sliding and Wobulated.                                                                                                                                         |
|     | Intra pulse Modulation<br>Types                                  | Phase coded, P3 &Poly Phase<br>Stepped FM, Linear Chirp (Up/Down)                                                                                                                                                                        |
|     | Scan Types                                                       | Circular, Sector & Lock-on.                                                                                                                                                                                                              |
| 6   | Signal Density                                                   | 500 Kilo Pulses Per Second                                                                                                                                                                                                               |
| 7   | Pulse Width Range                                                | 50nsec -<br>1ms                                                                                                                                                                                                                          |
| 8   | Pulse Width Accuracy                                             | 20 ns RMS                                                                                                                                                                                                                                |
| 9   | PRI                                                              | 2 µs to 50 ms                                                                                                                                                                                                                            |
| 10  | PRI Accuracy                                                     | 10 ns RMS                                                                                                                                                                                                                                |
| 11  | Emitter Records in RFPS<br>Identification Library                | 10,000                                                                                                                                                                                                                                   |
| 12  | Processing Time                                                  | Less than 3 seconds for feature extraction of 128<br>pulses of 1 µs pulse width of lock on emitter.                                                                                                                                      |
| 13  | Track<br>Designation<br>for<br>Finger Printing                   | (a)<br>ESM track designation mode for finger printing<br>in 0.175-40 GHz.                                                                                                                                                                |

SHAKTI : UHB\Ch1 Page 14 of 614

| Ser | Parameter            | Specification                                                                                                                                                                                              |
|-----|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     |                      | (b)<br>Auto scan designated mode for 2.2-18 GHz.                                                                                                                                                           |
| 14  | MMI                  | Separate display for RFPS for displaying inter/intra<br>pulse features in graphical as well as textual<br>formats.                                                                                         |
| 15  | Field Data Loader    | Uploading/downloading of RFPS Library data.                                                                                                                                                                |
| 16  | IF Signal Processing | 1000 MHz IF with 500 MHz bandwidth & 160 MHz<br>IF with bandwidth of 40 MHz.                                                                                                                               |
| 17  | Display Formats      | Inter & Intra pulse data to be presented in textual &<br>graphical<br>formats.<br>Tabular,<br>Histograms<br>&<br>Overlapped formats to be used for presenting the<br>data, Activity display and 3-D plots. |
| 18  | Data Storage         | Provision to store digitized IF samples for off-line<br>analysis.                                                                                                                                          |

- **1.5 Power Supply Requirement**.The system accepts 380V (phase to phase), 50 Hz, 3 Ø, 4 Wire Configuration power supply from Ship's Mains. Additionally, 115V AC, 400Hz 1ø and 380V AC 50Hz 3ø are required directly from the Ship. Also, unregulated 230V AC supply from the ship is required for anti condensation heaters.
- 1.5.1 Shakti System has ES and EA segments. The ES segment requires only 230 V AC, 50 Hz, 1Ø power supply. The EA segment requires 230 V, AC, 50 Hz, 1Ø, 380 V (phase to phase), 50 Hz, 3Ø and 115 V, AC, 400 Hz, 1 Ø.
- 1.5.2 Three in Number transformers are supplied as part of Installation Material for the system. Two Isolation Transformers (380V-380V) each of 30 KVA and one Step down Transformer (380V-230V) of 30 KVA provides the required power supplies to the SHAKTI system. These units are used to provide the isolation between the ship's supply and the system units. Additionally, 115V AC, 400Hz 1Ø is required directly from the ship for Transmitters (HB) for EA Section of Shakti system.
- 1.5.3 The output of the transformer are fed to Power Distribution Panels (PDPs) to provide desired power supplies to different units/modules of Shakti System. The power consumption details of Shakti System are given at **Table 1.4**. The Block Diagrams of Power Supply Requirement for ES & EA are given in **Figure 1.4** & **Figure 1.5**.

SHAKTI : UHB\Ch1 Page 15 of 614

**Table-1.4: Power Consumption Details of Shakti System**

| Ser | Sub-System<br>Description                         | Location                                                   | Type of Power<br>Supply | Approx. Load in<br>KVA                        |
|-----|---------------------------------------------------|------------------------------------------------------------|-------------------------|-----------------------------------------------|
| 1   | ES AHU-1                                          | Around the top<br>section of the<br>Pole Mast in<br>Basket | ±15V                    | DC Supply is from<br>ES Rack-2                |
| 2   | ES AHU-2                                          | On the Pole<br>Mast in basket                              | 5V, ±9V, ±15V           | DC Supply is from<br>ES Rack-2                |
| 3   | ES AHU-3<br>.(4 Nos)                              | On Yardarms                                                | ±9V,+15V                | DC Supply is from<br>ES AHU-4                 |
| 4   | ES AHU-4                                          | At the Base of<br>the Pole Mast                            | 5V, ±9V, ±15V           | DC Supply is from<br>ES Rack-2                |
| 5   | ES-RACK 1                                         | EWER<br>Compartment                                        | 230V AC, 50Hz,<br>1Ø    | 1.2 KVA                                       |
| 6   | ES-RACK 2                                         | EWER<br>Compartment                                        | 230V AC, 50Hz,<br>1Ø    | 3.0 KVA                                       |
| 7   | System<br>Controller &<br>Display (SCD)<br>Rack   | EWO<br>Compartment                                         | 230V AC, 50Hz,<br>1Ø    | 1.0 KVA                                       |
| 8   | External<br>System<br>Interface (ESI)<br>Unit     | EWER & EWTR<br>Compartments                                | 230V AC, 50Hz,<br>1Ø    | 0.5 KVA                                       |
| 9   | Rugged<br>Ethernet Switch<br>(Type-1) (2<br>No's) | EWER<br>Compartment                                        | +24V                    | DC Supply is from<br>ES RACK-1 & EA<br>RACK-1 |
| 10  | Rugged<br>Ethernet Switch<br>(Type-2) (2<br>No's) | EWO<br>Compartment                                         | +24V                    | DC Supply is from<br>SCD RACK                 |

SHAKTI : UHB\Ch1 Page 16 of 614

| Ser | Sub-System<br>Description | Location    | Type of Power<br>Supply | Approx. Load in<br>KVA   |
|-----|---------------------------|-------------|-------------------------|--------------------------|
| 11  | EA Rack-1                 | EWTR        | 230V AC, 50Hz,          | 5.0 KVA                  |
|     |                           | Compartment | 1Ø                      |                          |
| 12  | EA Rack-2                 | EWTR        | 230V AC, 50Hz,          | 4.0 KVA                  |
|     |                           | Compartment | 1Ø                      |                          |
| 13  | MB2 JAMMER                | Port & STBD | +5V, ±15V, +28V,        | DC Supply is from        |
|     | (2 No's)                  | Diaphragm   | -48V                    | EA RACK-1 by             |
|     |                           |             |                         | taking 230V AC Input     |
|     |                           |             | 270V                    | DC Supply is from        |
|     |                           |             |                         | Tx-PS(MB2) by            |
|     |                           |             |                         | taking 415V AC<br>Input. |
|     |                           |             |                         |                          |
| 14  | Tx-PS(MB2)                | -           | 380V AC, 50Hz,          | 6 KVA each               |
|     | (4 No's)                  |             | 3Ø                      |                          |
| 15  | HB JAMMER                 | Port & STBD | +5V, ±15V, +28V         | DC Supply is from        |
|     | (2 No's)                  | Jammer      |                         | EA RACK-1 by             |
|     |                           | Platform    |                         | taking 230V AC Input     |
|     |                           |             | 380V AC, 50Hz,          | 380V AC –<br>1.5KVA      |
|     |                           |             | 3Ø                      | each                     |
|     |                           |             | 115V AC, 400Hz,         | 115V AC –<br>0.7 KVA     |
|     |                           |             | 1Ø                      | each                     |
| 16  | Heat Exchanger            | EWTR        | 230V AC, 50Hz,          | 3 KVA each               |
|     | Unit (HEU)<br>(2 No's)    | Compartment | 1Ø                      |                          |

- **1.6 Environmental Specifications**.The guidelines for conducting ETs for electrical and electronic items/equipment's have been promulgated Vide PROTECTED (CLASS N1) & EXPOSED (CLASS N2) OF JSS 55555 -2012 (REV 3) as applicable to major ship borne systems. Shock Test as per NSS Guidelines as per NSS Gr.II or Gr.II.
- **1.7 Environmental Stress Screening (ESS) Standards**.ESS will be complied to DQA(N) Guidelines Promulgated Vide Letter No. 66301/Policy-07/DQA(N)/Qa-07 dated 09 Aug 16.
- **1.8 EMI/EMC Considerations**.Shakti System will be compliant to MIL Standards 461 E/F.

SHAKTI : UHB\Ch1 Page 17 of 614

**1.9 Dimensions and Weights of Subsystem**.The dimensions and weight details of Shakti units are provided in the Table-1.5 given below.

**Table-1.5: Dimensions and Weights of Shakti Subsystems**

| Item |                                           |     |       | Dimensions in mm |        | Weight  |
|------|-------------------------------------------|-----|-------|------------------|--------|---------|
| No.  | Subsystem Description                     | Qty | Depth | Width            | Height | in KGs  |
| 1    | ES AHU-1                                  | 1   |       |                  |        | 25      |
|      | (a)<br>Antenna Array(LB1)                 | 1   |       | Dia 1556         | 302    | 18.0    |
|      | (b)<br>Antenna Switching Unit<br>(LB1)    | 1   | 90    | 340              | 281    | 7.0     |
| 2    | ES AHU-2                                  | 1   |       |                  |        | 295     |
|      | (a)<br>BB & NB Rx (LB2-MB)                | 1   | 1350  | 1350             | 556    | 265     |
|      | (b)<br>OMNI Rx (MB-HB)<br>Module          | 2   | 189   | 340              | 494    | 10 each |
|      | (c)OMNI MASS (MB-HB)<br>Module            | 1   | 197   | 340              | 281    | 10      |
| 3    | ES AHU-3                                  | 4   | 357   | 240              | 330    | 10 each |
| 4    | ES AHU-4                                  | 1   | 840   | 600              | 374    | 51      |
| 5    | ES Rack 1                                 | 1   | 884   | 680              | 1229   | 170     |
| 6    | ES Rack 2                                 | 1   | 884   | 680              | 1637   | 272     |
| 7    | System Controller & Display<br>(SCD) Rack | 1   | 1057  | 648              | 1686   | 175     |
| 8    | External System Interface<br>(ESI) Unit   | 1   | 160   | 350              | 285    | 11      |
| 9    | Field Data Loader (FDL)                   | 1   | 400   | 400              | 100    | 5       |
| 10   | Rugged Ethernet Switch<br>(TYPE-1)        | 2   | 50    | 330              | 250    | 8 each  |
| 11   | Rugged Ethernet Switch<br>(TYPE-2)        | 2   | 50    | 330              | 250    | 8 each  |

SHAKTI : UHB\Ch1 Page 18 of 614

| Item |                                                     |     |       | Dimensions in mm |        | Weight      |
|------|-----------------------------------------------------|-----|-------|------------------|--------|-------------|
| No.  | Subsystem Description                               | Qty | Depth | Width            | Height | in KGs      |
| 12   | EA Rack-1                                           | 1   | 884   | 680              | 1014   | 150         |
| 13   | EA Rack-2                                           | 1   | 884   | 680              | 1014   | 150         |
| 14   | MB2 JAMMER                                          | 2   | 1400  | 1450             | 1850   | 550<br>each |
| 15   | HB JAMMER                                           | 2   | 900   | 1244             | 1300   | 180<br>each |
| 16   | Heat Exchanger Unit (HEU)                           | 2   | 650   | 650              | 900    | 150<br>each |
| 17   | Transmitter-Power Supply<br>(MB2)                   | 4   | 610   | 340              | 200    | 28 each     |
| 18   | Fault Diagnostic Rack (FDR)                         | 1   | 717   | 680              | 1229   | 120         |
| 19   | Uninterrupted Power Supply-I<br>(UPS-I)             | 1   | 560   | 250              | 447    | 31          |
| 20A  | Isolation Transformer 380V<br>380V, 3Ph, ∆-∆, 30KVA | 2   | 450   | 650              | 725    | 229<br>each |
| 20B  | Step Down Transformer<br>380V-230V, 3Ph, ∆-∆, 30KVA | 1   | 450   | 650              | 725    | 229         |
| 21A  | Power Distribution Panel<br>(PDP) (Type-1)          | 1   | 212   | 550              | 485    | 20          |
| 21B  | Power Distribution Panel<br>(PDP) (Type-2)          | 1   | 212   | 660              | 856    | 40          |
| 21C  | Power Distribution Panel<br>(PDP) (Type-3)          | 1   | 157   | 350              | 256    | 10          |

#### **Note:**

- **(1) The dimensions & weights indicated in the above table are on not exceeding basis.**
- **(2) The dimensions of MB2 Jammer given in the table are including the Roll stabilization platform. The low power unit (MB2) of MB2 Jammer shall be mounted under the stabilization platform.**

SHAKTI : UHB\Ch1 Page 19 of 614

- **(3) The dimensions of HB Jammer given in the table are including the Servo Drive Assy (SDA) (2-Axis). The low power unit (HB) of HB Jammer shall be mounted under the SDA (2-Axis) on mounting stand. Yard to manufacture the stand as per outline drawings provided by BEL.**
- **(4) SPTA Boxes of 3000 mm (width) x 2200 mm (Height) x 800 mm (Depth) is to be catered. Access space of 1000 mm (Min) on the front side is required.**

SHAKTI : UHB\Ch1 Page 20 of 614

![](_page_20_Figure_1.jpeg)

**Figure-1.1: Block Diagram of Shakti System**

SHAKTI : UHB\Ch1 Page 21 of 614

![](_page_21_Picture_0.jpeg)

**This page is Intentionally Left Blank.**

![](_page_22_Figure_1.jpeg)

**Figure-1.2: Configuration Diagram of ES System**

SHAKTI : UHB\Ch1 Page 23 of 614

![](_page_23_Picture_0.jpeg)

**This page is Intentionally Left Blank.**

![](_page_24_Figure_1.jpeg)

**Figure-1.3: Configuration Diagram of EA System**

SHAKTI : UHB\Ch1 Page 25 of 614

![](_page_25_Picture_0.jpeg)

**This page is Intentionally Left Blank**

![](_page_26_Figure_1.jpeg)

**Figure 1.4: ES Power Supply**

SHAKTI : UHB\Ch1 Page 27 of 614

![](_page_27_Picture_0.jpeg)

**This page is Intentionally Left Blank.**

![](_page_28_Figure_1.jpeg)

**Figure 1.5: EA POWER Supp**

SHAKTI : UHB\Ch1 Page 29 of 614

**This page is Intentionally Left Blank**

# **CHAPTER II BRIEF TECHNICAL DESCRIPTION**

#### **CHAPTER-II**

#### **BRIEF TECHNICAL DESCRIPTION**

- **2.1 Introduction**.Shakti is a Ship-borne EW Suite (consisting of both ES & EA) developed in association with Defence Electronics Research Laboratory (DLRL)- Hyderabad. The ES system covers a frequency range of 0.175 -40 GHz and EA system covers 6-40 GHz. In order to provide enhanced parameter specifications, functional features and modularity for ease of installation & maintenance, the system is configured with subsystems. The ES system provides integrated Radar Finger Printing capability. The ECM segment provides improved jamming features with incorporation of Digital Radio Frequency Memory (DRFM).
- 2.1.1 The principle objective of this system is to provide a powerful capability of interception, detection, direction finding, and classification of all RF signals in 175 MHz to 40 GHz frequency range in a high density environment with high sensitivity to provide adequate range advantage factor (RAF) and Comprehensive Threat Parameter Measurement, Threat Identification, Threat Prioritization.
- 2.1.2 An adequate and quick reaction automated EA response in 6 to 40 GHz frequency range for jamming various kinds of Radars encountered in modern naval battle field scenario.
- 2.1.3 In order to meet the above objectives, the ES segment of Shakti is realized using the technologies like Homodyne Receiver, Narrowband Receiver, Digital Receiver, Digital Instantaneous Frequency Measurement (DIFM), Base Line Interferometer (BLI) principle and TDOA principle of DF measurement, advanced processing algorithms for sorting/ Deinterleaving, Software Controlled Display System etc.
- 2.1.4 The EA segment covers 6 40 GHz in two split bands 6 18 GHz and 18 40 GHz to counter the threats for self-protection of naval ships in multiple threat environments using Digital Radio Frequency Memory (DRFM) based technique generator in addition to the noise jamming techniques. In 6 -18 GHz band, the system is capable of handling eight threats simultaneously (four in each sector of Port and Starboard) using electronic beam steering concept with minimum overall reaction time of less than 2 Sec. In 18 -40 GHz band, the system can handle two threats (one in each sector of 180°) using servo driven pedestal with a reaction time of less than 5 sec. The EA system employs DRFM for generating effective Jamming technique thus enhancing the effectiveness of the jamming many fold in comparison with the conventional Jammer.
- 2.1.5 This Chapter describes the System Description, Functions and Subsystem/PCB

SHAKTI : UHB\Ch2 Page 31 of 614

Module description of the Shakti system.

**2.2 ES System Description**.List of ES Units is given in **Table 2.1**. The description of each unit is explained in succeeding paragraphs. Configuration diagram of Shakti-ES is given in **Figure 2.1**.

**Table-2.1: List of ES Units**

| Ser. | Unit / Sub-units                                       | Part No.        |
|------|--------------------------------------------------------|-----------------|
|      | ES AHU-1                                               | 1723 003 525 18 |
| 1    | (a)<br>LB (175-500 MHz) Antenna Array                  | 1723 006 856 16 |
|      | (b)<br>ASU (LB1-Shakti)                                | 1723 006 769 83 |
| 2    | ES AHU-2                                               | 1723 003 526 15 |
|      | (a)<br>Omni Rx Module                                  | 1723 003 473 77 |
|      | (i)<br>Bi-Conical Omni Antenna Stack                   | 1723 003 561 07 |
|      | (ii)<br>Omni Receiver PCB                              | 1723 006 616 57 |
|      | (iii)<br>Down Converter 18-40 GHz                      | 4766 782 001 53 |
|      | (iv)<br>Front End Module (2.2-18 GHz)                  | 4769 775 502 04 |
|      | (v)<br>Limiter(18-40 GHz)                              | 4544 721 701 85 |
|      | (b)<br>Omni Mass Module(MB-HB)                         | 1723 003 474 74 |
|      | (i)<br>Omni Driver PCB                                 | 1723 006 615 60 |
|      | (ii)<br>EDLVA 18-40 GHz                                | 4556 787 501 78 |
|      | (iii)<br>Mass Logic & Band Control Generator PCB       | 4766 786 901 97 |
|      | (c)<br>BB & NB Rx(LB2-MB)                              | 1723 006 463 31 |
|      | (i)<br>Integrated Homodyne Receiver (2.2-18<br>GHz)    | 1723 003 562 04 |
|      | (ii)<br>Quad Super Heterodyne Receiver (0.5-18<br>GHz) | 1723 003 564 95 |
|      | (iii)<br>Receiver Processor Unit                       | 4766 786 701 18 |

SHAKTI : UHB\Ch2 Page 32 of 614

| Ser. | Unit / Sub-units                                  | Part No.        |
|------|---------------------------------------------------|-----------------|
|      | (iv)<br>Bite Distribution Unit-<br>N              | 4773 726 901 80 |
|      | (v)<br>Driver PCB (BB & NB RX AHU)                | 1723 006 535 09 |
|      | (vi)<br>Receiver PCB (BB & NB RX AHU)             | 1723 006 536 06 |
|      | (vii)<br>Synthesizer                              | 4560 720 401 70 |
|      | (viii) LO Distribution Module                     | 4773 726 801 89 |
|      | (ix)<br>Antenna Array 2.2-18 GHZ (CBS<br>ANTENNA) | 4767 779 601 91 |
|      | (x)<br>Spiral Antenna(0.4-2.2 GHZ)                | 4767 780 701 89 |
|      | (xi)<br>Antenna CBS Array 2.2-6 GHZ               | 4767 777 501 86 |
|      | (xii) Antenna Array Sectoral 6-18 GHZ             | 4767 772 105 75 |
| 3    | ES AHU-3                                          | 1723 003 527 12 |
|      | (a)<br>18-40 GHz Biconical Antenna                | 4767 781 201 44 |
|      | (b)<br>Limiter(18-40 GHz)                         | 4544 721 701 85 |
|      | (c)<br>EDLVA 18-40 GHz                            | 4556 787 501 78 |
|      | (d)<br>Amplifier LMT With Video Module 18-40 GHz  | 4562 720 401 05 |
| 4    | ES AHU-4                                          | 1723 003 528 09 |
|      | (a)<br>Type-3 BITE Unit (18-40 GHz)               | 1100 050 801 27 |
|      | (b)<br>TDOA Processor PCB                         | 4766 787 001 88 |
|      | (c)<br>Receiver Processor Board                   | 4766 787 101 79 |
|      | (d)<br>BITE Source Monitor PCB                    | 1723 006 586 50 |
|      | (e)<br>DIFM Receiver 2-18 GHz                     | 4556 788 601 76 |
|      | (f)<br>FREQ Synthesizer 2-18 G 488.28 K           | 4560 720 202 85 |
|      | (g)<br>FREQ Synthesizer 0.5-2 G 10 dBm            | 4560 720 301 79 |
| 5    | ES Rack-1                                         | 1723 003 529 06 |

SHAKTI : UHB\Ch2 Page 33 of 614

| Ser. | Unit / Sub-units                               | Part No.        |
|------|------------------------------------------------|-----------------|
|      | (a)<br>Receiver Processor                      | 1723 003 476 68 |
|      | (i)<br>H/W RIB & QDR VPX Chassis               | 4805 784 301 82 |
|      | (ii)<br>Monitor Signal PCB                     | 4806 779 101 81 |
|      | (iii)<br>Quad Digital Receiver                 | 1723 003 569 80 |
|      | (b)<br>ESM Processor                           | 1723 003 477 65 |
|      | (c)<br>Control Unit(ES RACK-1)                 | 1723 003 480 56 |
| 6    | ES Rack-2                                      | 1723 003 530 03 |
|      | (a)<br>Multi<br>Channel RF Unit (LB1-SHAKTI)   | 1723 006 834 82 |
|      | (b)<br>Receiver Processor (LB1)                | 1723 006 833 85 |
|      | (c)<br>LVPS-1                                  | 1723 003 478 62 |
|      | (d)<br>LVPS-2                                  | 1723 003 479 59 |
|      | (e)<br>RFPS WBT & Processor                    | 1723 006 542 85 |
|      | (f)<br>Power Supply (AHU 1-LB1)                | 1723 007 057 92 |
| 7    | System Controller and Display Rack             | 1723 003 531 97 |
|      | (a)<br>SCD Processor                           | 1723 003 481 53 |
|      | (b)<br>Display LCD 20" Flat Panel (DRIP PROOF) | 4461 723 601 41 |
|      | (c)<br>RFPS SBC                                | 1723 003 578 53 |
| 8    | Rugged Ethernet Switch –Type-1                 | 1723 003 534 88 |
| 9    | External System Interface Unit (ESI)           | 1723 003 532 94 |
| 10   | Fault Diagnostic Rack                          | 1723 003 536 82 |
| 11   | Rugged Ethernet Switch (TYPE-2)                | 1723 003 535 85 |

SHAKTI : UHB\Ch2 Page 34 of 614

![](_page_35_Figure_1.jpeg)

**Figure-2.1: Configuration of Shakti-ES System**

SHAKTI : UHB\Ch2 Page 35 of 614

**2.2.1 ES AHU-1**.ES AHU-1 is the Antenna Head Unit for the 0.175-0.5 GHz. It consists of an LB1 Antenna array (5 No's antenna elements in 0.175-0.5 GHz) and Antenna Switching Unit. LB1 antenna array elements will be mounted around top section of the pole mast in circular fashion. Antenna switching unit will be located on the square frame on the top section of the pole mast.

![](_page_36_Picture_2.jpeg)

**Figure-2.2: Pictorial View of ES AHU-1**

**2.2.1.1 LB (175-500 MHz) Antenna Array**.LB Antenna Array is part of ES AHU-1 and Placed at top of Pole Mast. The dual fed dual polarized antennas for DF applications are used in Low Band system 0.175 – 0.5 GHz. These antennas are designed to receive both horizontal and vertical polarized signals from any direction in Azimuth. Two antenna elements dipole and loop with separate connectors are integrated in a single antenna structure. Dipole antenna exhibits omni directional radiation characteristics for vertically polarized waves in azimuth plane for its vertical mounting. Similarly loop antenna placed horizontally in azimuth plane (loop axis vertical), provides omni directional radiation characteristics in azimuth plane for horizontally polarized waves. These antennas are designed to have large frequency bandwidth covering 175-500 MHz respectively without any tuning mechanism. This is accomplished by incorporating specially designed broadband impedance matching network.

2.2.1.1.1 The antenna has omni directional radiation pattern for both vertical and horizontal polarizations and is suitable for direction finding applications. The antenna is enclosed in a suitably designed and developed FRP radome to protect the antenna from environmental severities and offer minimum drag.

SHAKTI : UHB\Ch2 Page 36 of 614

![](_page_37_Picture_1.jpeg)

**Figure-2.3: LB (175-500 MHz) Antenna Array**

**Table-2.2: Low Band (175-500 MHz) Antenna Array Specifications**

| Ser | Parameter                                              |                                                                                     | Specification                                                               |
|-----|--------------------------------------------------------|-------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| 1   | Type of the antenna                                    | Dipole Antenna                                                                      | Loop Antenna                                                                |
| 2   | Frequency coverage                                     | 175-500 MHz                                                                         | 175-500 MHz                                                                 |
| 3   | VSWR                                                   | 3.8:1 (max)                                                                         | 3.5:1 (max)                                                                 |
| 4   | Polarization                                           | Linear (Vertical)                                                                   | Linear (Horizontal)                                                         |
| 5   | Radiation Characteristics<br>(a)<br>Elevation coverage | ≥40°                                                                                | ≥40°                                                                        |
|     | (b)<br>Azimuth coverage                                | 360°                                                                                | 360°                                                                        |
|     | (c)<br>Omni deviation                                  | ≤ ±3 dB                                                                             | ≤ ±3 dB (175-400 MHz)<br>≤ ±4 dB (Above 400 MHz)                            |
| 6   | Gain                                                   | -24 dBi to<br>-2 dBi<br>(Range of Minimum<br>Gain<br>over<br>the<br>frequency band) | -30 dBi to -17 dBi<br>(Range of<br>Minimum Gain<br>over the frequency band) |
| 7   | *Phase Matching<br>*Amplitude Matching                 | ≤ ± 7°<br>≤ ± 1.5 dB                                                                | ≤ ± 7°<br>≤ ± 1.5 dB                                                        |
| 8   | Connector                                              | BMA (Jack)                                                                          | BMA (Jack)                                                                  |

SHAKTI : UHB\Ch2 Page 37 of 614

| Ser | Parameter                                                                                          |                  | Specification                                                     |
|-----|----------------------------------------------------------------------------------------------------|------------------|-------------------------------------------------------------------|
| 9   | Length X Diameter<br>(Approx)                                                                      | 301±3mm x 16±2mm | ø 122±3mm (Loop dia.)<br>Loop Cross section dia:<br>ø 13mm ± 2 mm |
| 10  | Weight (integrated Dipole<br>and<br>Loop<br>Antenna<br>element)                                    | ≤ 1 Kg           |                                                                   |
| 11  | Overall<br>Weight (5 antenna<br>elements<br>with<br>bay<br>arm<br>Assy and split mounting<br>ring) | ≤ 18 Kg          |                                                                   |
| 12  | Final Finish                                                                                       | finish.          | Antenna to be painted with RAL-7040 Semi Gloss                    |

**2.2.1.2 ASU (LB1-Shakti)**. The ASU is an independent unit, which is installed near the DF antenna array. ASU switches among the Dipole and Loop Antennas in DF antenna arrays in 175-500MHz to select the RF signal inputs and Calibration/BITE signal, based on the commands from the DF receiver. The ASU operates from built-in power supplies with 15V DC as input and is provided by DF receiver.

**2.2.1.2.1 ASU**.ASU consists of five SP3T switches. Each SP3T switch has two RF inputs and one CAL/BITE input, where only one input is selected at a time. ASU selects the particular polarization in antenna to be received based on commands from Receiver Processor (LB1) and connects the selected antenna bay to the DF Receiver. It accepts a calibration signal from the synthesized source for calibrating the RF cables and DF Receiver. ASU can be commanded to either connect antenna bay or inject calibration signals into the DF receiver. In the presence of external high power RF signal the receivers are connected to Cal/BITE port through a 'blanking pulse' control. Inside the CAL source receivers are further terminated to 50 ohms.

SHAKTI : UHB\Ch2 Page 38 of 614

![](_page_39_Picture_1.jpeg)

**Figure-2.4: Pictorial View of ASU (LB1-Shakti)**

![](_page_39_Figure_3.jpeg)

**Figure-2.5: Block Diagram of ASU (LB1-Shakti)**

**2.2.2 ES AHU-2**.AHU-2 is the Antenna Head Unit for 0.5-40 GHz receiver and it consists of 0.5-18 GHz band Omni Receiver-1 & 2, Omni Mass and Broad Band & Narrow Band AHU Units.

SHAKTI : UHB\Ch2 Page 39 of 614

![](_page_40_Figure_1.jpeg)

**Figure-2.6: Pictorial View of ES AHU-2**

**2.2.2.1 Omni Receiver**.Omni Receiver Unit is a sub module of 18-40 GHz ESM Receiver and 2.2-18 GHz RFPS chain. Shakti System consists of two Omni Receivers, which will be fitted on either side of pole mast to provide interception over 360°. Two RF Signals (one down converted 18-40 GHz RF signal and other 2.2-18 GHz RF Signal) from each of the omni receiver is given to Omni Mass module. In Omni Mass module there is an SP4T switch which will select one of the four RF Signals (two each from two omni receivers) and route to RFPS Chain.

SHAKTI : UHB\Ch2 Page 40 of 614

![](_page_41_Figure_1.jpeg)

**Figure-2.7: Functional Block Diagram of Omni Receiver**

**2.2.2.1.1 Biconical Omni Antenna Stack**.A stack of Bi Conical Omni antennas is used in the frequency range of 2.2 – 18 & 18 – 40 GHz. Specifications of the antenna are as follows.

**Table-2.3: Biconical Omni Antenna Stack Specifications**

|     |                    | Specifications                                       |           |
|-----|--------------------|------------------------------------------------------|-----------|
| Ser | Parameter          | Unit 1                                               | Unit 2    |
| 1   | Frequency Range    | 2.2-18 GHz                                           | 18-40 GHz |
| 2   | VSWR               | 3:5:1 Over (Max)                                     |           |
| 3   | Coverage           | Azimuth-360°, Elevation-<br>>20°<br>(3 dB Beamwidth) |           |
| 4   | On-Axis Gain (Min) | -2.0 dBi                                             | 0 dBi     |

SHAKTI : UHB\Ch2 Page 41 of 614

| Ser | Parameter      |                  | Specifications |
|-----|----------------|------------------|----------------|
|     |                | Unit 1           | Unit 2         |
| 5   | Omni Deviation | ±3 dB            |                |
| 6   | Polarization   | Slant Linear 45° |                |

- **2.2.2.1.2 Omni Receiver PCB**.Omni Receiver PCB generates the +5VDC from the +9VDC to interface the other circuitry and converts the differential inputs to the single ended outputs. Input and output connectors are with micro-D connectors.
- **2.2.2.1.3 18-40 GHz Down Converter**. The 18-40 GHz down converter is used for down converting the RF signal and the down converted RF Signal from two of the omni receivers is selected based on the sector (i.e. direction) in which the emitter is present and given to DIFM for frequency measurement.
- 2.2.2.1.3.1 The 18-40 GHZ Down converter internally will have diplexer which separates received RF signals in to two bands i.e. 18-29 GHz and 29-40 GHz. Two LO frequencies, namely, 35 GHz and 46 GHz, are used to down convert the 18-29 GHz or 29-40 GHz to 6- 17 GHz band. Down converter also generates the band videos i.e. band video-L for 18-29 GHz and band video-H for 29-40 GHz. These Band videos are routed to Omni Mass Module for generation of Omni Band Selection.
- **2.2.2.1.4 Front End Receiver (2-18GHz**).2.2-18 GHz RF is passed through the FER module of RFPS Chain, Programmable Attenuator and LNA. The Programmable Attenuator is having two bits for attenuation levels from 0 to 24dB in step of 8dB for each bit. This signal is further amplified using a LNA and given to Omni Mass module.
- **2.2.2.2 Omni Mass Module**. Omni Mass Module is the sub module of 18-40 GHz band of shakti ES System.18-40 GHz band consists of two Omni Receivers and will be fitted on either side of pole mast to cover 360° receptions. Both Omni Receivers down converted RF will be passed through omni mass module which consists of EDLVAs to convert RF and video. Omni Mass Module provides amplitude data, band selection and RFP TO AHU-4 to measure the incoming pulse parameters.

SHAKTI : UHB\Ch2 Page 42 of 614

![](_page_43_Figure_1.jpeg)

**Figure-2.8: Functional Block Diagram of Omni Mass**

SHAKTI : UHB\Ch2 Page 43 of 614

- **2.2.2.2.1 Omni Mass Sub Modules**.The Omni mass module consists of two EDLVAs (18-40 GHz), Mass board, SP4T switch and BITE components for 18-40 GHz and 2.2-18 GHz BITE distribution as shown in functional diagram. The Omni mass module receives two 18-40GHz RF outputs, two 18-40 GHz down converted 6-17 GHz RF and band videos from Omni Rx modules, and two RFPS Omni Chain 2.2-18 RF signals from two Omni receivers. 18-40 GHz RF signals are routed to EDLVAs, and 6-17 GHz down converted RF and 2.2-18 GHz RFPS RF are routed to SP4T switch for RFPS and band videos are routed to Mass board for Band Selection.
- **2.2.2.2.2 Omni Driver PCB**.The OMNI DRIVER PCB would be responsible to convert the incoming Differential signals to corresponding TTL signals along with some decoding logic and OR logic. The OR logic and the decoded logic output shall again be given as the input for the Differential Drivers, whose output is made external from the Omni Driver Board. The OMNI DRIVER PCB will be operated on +5V DC, required other internal power supplies will be generated from input +9V DC.
- **2.2.2.2.3 EDLVAs (18-40 GHz)**.Two EDLVAs receives an 18-40 GHz RF signal and generates a video signal as an output. These video signals are routed to Mass board to validate with threshold level and measure the amplitude. After amplitude measurement Mass board compares the amplitude level of both the Omni receivers for selecting one receiver which will have maximum amplitude and band selection for 18-29 GHz or 29-40 GHz. Then the processed data is sent to AHU-4 for further processing.
- **2.2.2.2.4 Mass Logic & Band Control Generator PCB**.Mass Logic & Band control generator PCB has following features:
  - (a) One Xilinx Spartan-6 FPGA.
  - (b) Six Low Speed ADC Interface 6 Channels (Resolution: 8-Bit, Sampling: 40Msps, Input Range: 0 - 5V).
  - (c) Four Comparator Interface Single supply comparators.
  - (d) Communication Interface: RS-232.
  - (e) Communication Interface: RS-422 16 Channels.
  - (f) Digital Input & Output: 32 Channels.
  - (g) Configuration PROM & JTAG Interface.
  - (h) 40 MHz on board Crystal Oscillator, External Clock Input.
  - (j) +9V Power Supply Interface (Required for supply should be generated on

SHAKTI : UHB\Ch2 Page 44 of 614

board).

![](_page_45_Picture_2.jpeg)

**Figure-2.9: Pictorial View of Mass Logic & Band Control Generator PCB**

**2.2.2.3 BB & NB RX (LB2-MB)**.Broadband and Narrow Band Receiver AHU is configured to achieve a wide frequency coverage of 0.5-18 GHz with selectable modes of operation for better interception ranges and higher accuracy of direction finding. BB & NB Rx AHU is the integration of Broad Band and Narrow Band Receivers. It consists of 2.2 - 18 GHz Broad Band Receivers and 0.5-18 GHz Narrow Band Receivers which measures Direction of Arrival (DOA) using 4 channel Base Line Interferometry (BLI) technique.

SHAKTI : UHB\Ch2 Page 45 of 614

![](_page_46_Figure_1.jpeg)

**Figure-2.10: Block diagram of Bite Network Components**

SHAKTI : UHB\Ch2 Page 46 of 614

![](_page_47_Figure_1.jpeg)

**Figure-2.11: Block Diagram of Broadband & Narrowband Receiver**

SHAKTI : UHB\Ch2 Page 47 of 614

- **2.2.2.3.1 Integrated Homodyne Receiver**.Integrated Homodyne Receiver consists of the Switch Filter Bank (SFB), BITE RF Input Distribution (4-Way Power Divider), Homodyne Receiver and Data Interface Unit (DIU) all together as a single module. **Figure 2.12** shows the configuration of 2.2-18 GHz Integrated Homodyne Receiver. It takes four RF input from a BLI antenna array for high accuracy DF measurement. All other parameter measurements are derived from the four RF inputs internal to the Homodyne Receiver.
- 2.2.2.3.1.1 This receiver configuration consists of RF section, IF section, Video Section, Digital section and DC regulation & distribution section. The RF section takes all four RF input from the BLI antenna array and converts in to an 160 MHz IF through the Homodyne LO derived in the same section. The detection of RF signal is also carried in the same section using three RF detectors. The IF section conditions the IF signal for phase detection. The video section condition the Sin & Cos phase detected videos for digitization. The digital section does the digitization of all the Sin & Cos videos and then resolves the frequency and DF (resolved phase data) for the final output.
- 2.2.2.3.1.2 The BITE feature is incorporated through an RF injection using SPDT switch at all the four RF input ports. This present configuration has the feature of CW and POCW identity Flags. All the data is outputted with a latch derived from the RF Presence (RFP) identity.

SHAKTI : UHB\Ch2 Page 48 of 614

![](_page_49_Figure_1.jpeg)

**Figure-2.12: Block Diagram of Integrated Homodyne Receiver**

SHAKTI : UHB\Ch2 Page 49 of 614

- **2.2.2.3.2 Quad Super Heterodyne Receiver 0.5-18 GHz**.The Narrow band receiver is configured with Four Channel Super heterodyne Receivers. One up-conversion and three down conversion approach is employed to convert 2-18 GHz RF to IFs of 1 GHz & 160 MHz with enhanced performance on spurious, image rejection and LO re-radiation. All the four super heterodyne receivers are housed in single mechanical housing with common LO and Synthesizer inputs.
- 2.2.2.3.2.1 The Quad Superhet Receiver (QSR) accepts the 0.5-18 GHz inputs in three bands of 0.5-2.2 GHz, 2-6.25 GHz and 6-18 GHz. The QSR is configured to receive in three bands in view that three BLI linear antenna arrays in 0.5-2.2GHz, 2-6.25 GHz and 6- 18 GHz are employed to cover 0.5-18 GHz.
- 2.2.2.3.2.2 The Channelization approach is incorporated in this receiver with three Switch Filter Banks (SFBs), which are designed to cover the input frequency bands of 0.5-2.2 GHz, 2.2-6.25 GHz and 6.0-18.0 GHz. These Switched filter banks are used as preselector filters in-place of YIG tuned filters. These SFBs will minimize the spurious (harmonically & non-harmonically related), image rejection & LO radiation performances of QSR. Detailed Block diagram of QSHR is as given in **Figure-2.13**.

SHAKTI : UHB\Ch2 Page 50 of 614

![](_page_51_Figure_1.jpeg)

**Figure-2.13: Block Diagram of Quad Super Heterodyne Receiver 0.5-18 GHz**

SHAKTI : UHB\Ch2 Page 51 of 614

**2.2.2.3.3 Receiver Processor Unit**.Receiver Processor unit is located in the ES AHU-2 and distributes all controls to Homodyne Receivers, QSHRs and RF BITE N/W unit as shown in **Figure 2.14**. The interface between the unit and the front end is TTL in single ended form. The interface between the unit and the back end is on fiber optic interface for high speed PDWs data transfer and the unit also has Ethernet interface for command transfer.

2.2.2.3.3.1 The Receiver Processor unit is a standalone unit which receives Phase, Frequency and Amplitude data along with RF Presence (RFP) pulse from front end receivers on pulse to pulse basis and in turn measures Pulse Width (PW) and Time of Arrival (TOA) parameters. It receives data from four quadrants of homodyne receivers and Maximum amplitude quadrant data will be processed further. It also generates various timing controls, computes final DF covering 360° over azimuth and intra pulse flags will be appended in PD data. Finally it generates 192 bit parallel PD Word. This 192 bit parallel PD Word is converted into high speed serial data using AURORA 8B/10B protocol and transmits at the rate of 3.125Gbps.

2.2.2.3.3.2 It has two Rocket I/O transceivers for sending the 192 bit pulse descriptor word (PDW) at a speed of 3.125 Gbps to ESM processor on OFC for further processing. In addition, this unit also receives commands from ESMP on Ethernet, decodes the received commands and generates the relevant control data for NB & BB front end receivers. It has the connection with ESI through RS 422 lines to switch front ends into Bite port when Blanking Pulse is present. It has the connection with NB Rx RIB board also through RS 422 lines because PD formation done in RIB board and NB Rx front controls generated by RPU. In order to synch these two boards RIB will be functioned as Master and RPU will be Slave. It has the connection with RPB board through RS 422 lines. Here RPB generates Bite source controls for both NB Rx (LB2-MB) & BB Rx (MB) Bite mode. In Auto Bite mode RPU functions as master and other RPB and RIB boards will be slaves.

SHAKTI : UHB\Ch2 Page 52 of 614

![](_page_53_Figure_1.jpeg)

**Figure-2.14: Controls Distribution of RPU**

SHAKTI : UHB\Ch2 Page 53 of 614

**2.2.2.3.4 Bite Distribution Unit- N**.The system can be tested in Bite mode for internal Testing and Trouble shooting. In order to test in bite mode, a simple bite path is provisioned in BB & NBrx with RF Bite Distribution Modules and Power dividers. Four BDUs were placed each on top of QSHR Stack assembly to feed Bite RF generated from DTO to QSHR.

## **2.2.2.3.4.1 Key features of BDU are:**

- (a) Wide Frequency coverage of 0.5 to 18 GHz.
- (b) Dedicated four equal Channels for each of all three Bands 0.5-2 GHz,
- 2-6 GHz and 6-18 GHz.
- (c) Amplitude and Phase matched among all Channels.
- (d) High Switching Speed of 200 nsec.

SHAKTI : UHB\Ch2 Page 54 of 614

![](_page_55_Figure_1.jpeg)

**Figure-2.15: Block Diagram of Distribution Module Network**

SHAKTI : UHB\Ch2 Page 55 of 614

#### **2.2.2.3.5 Driver PCB**.Key features of Driver PCB are:

- (a) Same Controls from RPU are Routed to all Quadrants of BB & NB Rx through different connectors of Driver PCB. So That Connectors can be interchanged for easier Trouble shooting.
- (b) Feedback controls were incorporated for assurance from Narrowband Receiver.
- (c) It Accepts LVTTL input and converts to TTL within the board for Power good Indication.
- (d) Accepts some Differential inputs also.
- (e) Large No. of Differential Pair Outputs.

## **2.2.2.3.6 Receiver PCB**.Key features of Receiver PCB are:

- (a) Feedback Control Circuitry for controls of each Quadrant.
- (b) Uniformity among all Receiver PCBs maintained in order to replace one with any other for quick trouble shooting.
- **2.2.2.3.7 Synthesizer**.Different LO Frequencies ranging from 1.16 GHz to 18.5 GHz are required for operation of QSHR. To fulfil the requirement high accuracy programmable frequency Synthesizer is used. Key features of Synthesizer are mentioned below.
  - (a) Tuning Speed between any two frequencies irrespective of step size is around 2usec.
  - (b) High Frequency Accuracy of 50KHz
  - (c) In built Local Oscillator with High stability of 0.05ppm/°C
  - (d) Wide Frequency range of 1-18 GHz
  - (e) 100KHz Step Size
- **2.2.2.3.8 Distribution Module**.LO Power Distribution Module will be used over the frequency range of 6–18.0 GHz. It takes input from LO source and generates 4 outputs. It consists of a 4-way Power Divider (6-18 GHz) and Low Noise Amplifiers.

SHAKTI : UHB\Ch2 Page 56 of 614

![](_page_57_Figure_1.jpeg)

**Figure-2.16: Block Diagram of LO Distribution Module (6.0-18.0 GHz)-N**

2.2.2.3.8.1 The 4-way Power Divider divides the input LO signal into 4 paths equally where the Driver Amplifiers amplify the signal to the required power level in each path for distribution.

**2.2.2.3.9 Antenna arrays (2.2-18 GHz)**.Linear Antenna Arrays with spiral antenna are used to estimate the DF (AOA) information employing BLI technique. There are 4 Antennas in Each Linear Array. Specifications of the antenna are as given in **Table 2.4** below.

**Table-2.4: Antenna Array Specifications**

| Ser | Parameter       | Specification                       |
|-----|-----------------|-------------------------------------|
| 1   | Type of Antenna | Archimedean Spiral                  |
| 2   | Frequency       | 2.2-18 GHz                          |
| 3   | VSWR (Max.)     | 2.5: 1                              |
| 4   | Polarization    | Circular (LHCP)                     |
| 5   | Gain            | -7.5dBLi to 0dBLi from 2.2-4<br>GHz |

SHAKTI : UHB\Ch2 Page 57 of 614

| Ser | Parameter                                      | Specification                                                    |
|-----|------------------------------------------------|------------------------------------------------------------------|
|     |                                                | -2dBLi to 2dBLi from 4-18<br>GHz                                 |
| 6   | Gain Tracking among a set<br>of 4 antennas     | ± 1dB (2dB window) On Axis<br>± 1.5dB (3dB window) ±45˚ Off Axis |
| 7   | Phase Tracking among a<br>set of 4 antennas    | ± 10˚ (20˚ window) On Axis<br>± 15˚ (30˚ window) ±45˚ Off Axis   |
| 8   | Gain Tracking among set of<br>5 Antenna Arrays | ± 2dB                                                            |
| 9   | 3 dB Beam width                                | 50˚ (Min), 110˚ (Max)                                            |
| 10  | Axial Ratio (Max.)                             | 2 dB (On Axis), 3 dB (±45˚ Off Axes)                             |
| 11  | Beam Squint (Max.)                             | ±10°                                                             |
| 12  | Back lobe level (Max.)                         | –<br>9.5 dB                                                      |
| 13  | Connector                                      | SMA female                                                       |
| 14  | No. of Antennas in Array                       | Four                                                             |

**2.2.2.3.10 Spiral Antenna (0.4-2.2 GHz)**.Cavity Backed Spiral Antenna maintains essentially constant impedance and pattern performance over the operating band of 0.4 to 2.2 GHz. The basic Spiral has got bi-directional characteristics, radiating equally in both directions. It is backed up by a cavity for achieving unidirectional characteristics. The cavity is loaded with absorbing materials to absorb back radiation. Suitable Balun (balance to unbalanced transformer) is used for feeding the spiral.

**2.2.2.3.11 Antenna CBS Array 2.2-6 GHz**.Four sets of Direction finding antenna arrays housed in an Antenna Head Unit (AHU) are mounted on the Pole mast of the platform. Sectoral horn based Base Line Interferometric technique is employed in the 2-6 GHz band for interception, analysis and high accuracy DOA measurement and sensitivity.

**Table-2.5: CBS Array Antenna Specifications**

| Ser | Description        | Specification Value |
|-----|--------------------|---------------------|
| 1   | Type of Antenna    | Archimedean Spiral  |
| 2   | Frequency Coverage | 2.2-6 GHZ           |

SHAKTI : UHB\Ch2 Page 58 of 614

| Ser | Description                                        | Specification Value                                                |
|-----|----------------------------------------------------|--------------------------------------------------------------------|
| 3   | VSWR(MAX)                                          | 2.5:1                                                              |
| 4   | Polarization                                       | Circular(LHCP)                                                     |
| 5   | Gain                                               | -4.5 dBi to 2 dBi                                                  |
| 6   | Gain Tracking Among Set of 4<br>Antennas in Array  | ±1 dB (2 dB Window) ON AXIS<br>±1.5 dB (3 dB Window) ±45° OFF AXIS |
| 7   | Phase Tracking Among Set Of 4<br>Antennas in Array | ±10°(20° WINDOW) ON AXIS<br>±15°(30° WINDOW) ±45° OFF AXIS         |
| 8   | 3dB beam width                                     | 50°(MIN),110° (MAX)                                                |
| 9   | Axial Ratio (MAX)                                  | 3 dB (ON AXIS), 4 dB(±45° OFF AXIS)                                |
| 10  | Beam SQUINT (MAX)                                  | ±10°                                                               |
| 11  | Back lobe Level(MAX)                               | -9.5 dB                                                            |
| 12  | Connector                                          | SMA Female                                                         |
| 13  | Size of Antenna                                    | 61.7<br>mm<br>Ø,<br>42.5<br>mm<br>Height<br>Without<br>Connector   |
| 14  | No. Of Antennas in Array                           | Four                                                               |
| 15  | Inter Element Spacing in The<br>Array              | 1:2:1.5 62 mm :124 mm :93 mm)                                      |
| 16  | RADOME                                             | Thin Wall (RT Duroid 5880)                                         |

**2.2.2.3.12 Antenna Array Sectoral Horn 6-18 GHz**.These are compact size, light weight BLI arrays comprising sectoral horn as basic radiating elements to realize high accuracy DOA measurement and sensitivity in 6-18 GHz Band. Specifications of the antenna are as given below:

**Table-2.6: Specifications of Sectoral Horn 6-18 GHz**

| Ser | Parameter             | Specification                   |
|-----|-----------------------|---------------------------------|
| 1   | Antenna Configuration | Sectoral Horn BLI Array Antenna |
| 2   | Frequency Coverage    | 6-18 GHZ                        |

SHAKTI : UHB\Ch2 Page 59 of 614

| Ser | Parameter                                              | Specification                                                   |
|-----|--------------------------------------------------------|-----------------------------------------------------------------|
| 3   | VSWR(MAX)                                              | 3.1                                                             |
| 4   | Polarisation                                           | Slant Linear 45°                                                |
| 5   | Gain (ON AXIS)                                         | 7dBi (MIN)                                                      |
| 6   | Amplitude Tracking Among Set of 4<br>Antennas in Array | ±1 dB (2dB Window) ON AXIS<br>±1 5dB (3dB Window) ±45° OFF AXIS |
| 7   | Phase Tracking Among Set Of 4<br>Antennas in Array     | ±10°(20° Window) ON AXIS<br>±15°(30° Window) ±45° OFF AXIS      |
| 8   | 3dB Beam Width                                         | Azimuth :110° (MAX),65°(MIN)<br>Elevation: 36°(MAX),24°(MIN)    |
| 9   | Output Connector                                       | SMA Female                                                      |
| 10  | RADOME Element Array                                   | Polarizer Embedded RADOME Overall<br>RADOME                     |

**2.2.3 ES AHU-3**.AHU-3 consists of 18-40 GHz frontend electronics. It receives the RF intercepted by 18-40 GHz biconical antenna and amplifies the RF/video. The output of these units is used for measurement of DOA of the intercepted emitters in 18-40 GHz band using TDOA technique. Four AHU-3 units are mounted on yard arms with 10mtrs spacing to calculate DOA of intercepted signal. ES AHU-3 is a frontend RF module to intercepts the external emissions in 18-40 GHz band. It can be operated either in RF mode or in BITE mode.

![](_page_60_Picture_3.jpeg)

**Figure-2.17: Pictorial View of ES AHU-3**

SHAKTI : UHB\Ch2 Page 60 of 614

![](_page_61_Figure_1.jpeg)

**Figure-2.18: Function Block Diagram of ES AHU-3**

**Table-2.7: 18-40 GHz Bi conical Antenna Specifications**

| Ser | Description           | Specification                                      |
|-----|-----------------------|----------------------------------------------------|
| 1   | Type of Antenna       | Biconical Antenna                                  |
| 2   | Frequency             | 18-40 GHz                                          |
| 3   | VSWR (Max.)           | 3.0:1 (Max.) 90% band<br>3.5:1 (Max.) 100% band    |
| 4   | Polarization          | Slant Linear 45°                                   |
| 5   | Gain                  | ≥0.0dBi                                            |
| 6   | Coverage              | Azimuth: 360°<br>Elevation :>20°                   |
| 7   | Omni deviation (Max.) | ±3 dB over 90% band<br>±4 dB over 100% of the band |

SHAKTI : UHB\Ch2 Page 61 of 614

| Ser | Description                               | Specification                         |
|-----|-------------------------------------------|---------------------------------------|
| 8   | Connector                                 | K (F)                                 |
| 9   | Size<br>of<br>the<br>Antenna<br>(Approx.) | Ø50mm X 50.0 mm (Diameter x Height)   |
| 10  | Weight of the Antenna                     | 400 gms.<br>(Max.) with Mounting Boom |
| 11  | Radome                                    | C-Sandwich Radome                     |

- **2.2.3.1 EDLVA 18-40 GHz.** The EDLVA is basically an amplifier with detector and it has RF/BITE mode selection provision based on controls received by it. It amplifies the received RF signal in the frequency range of 18-40 GHz. The RF output of EDLVA is passed through Gain Equaliser and Limiting Amplifier with Video Module.
- **2.2.3.2 Amplifier LMT with Video Module 18-40GHz**. The Limiting amplifier with Video output module receives the incoming signals in the frequency range 18-40 GHz and gives output amplitude of 0.05-1.5V with fast rise time in the order of 5 ns.
- **2.2.4 ES AHU-4.** ES AHU-4 is a sub module of 18-40 GHz band of Shakti ES system. ES AHU4 receives down converted RF signal (6-17 GHz) from Omni Rx to measure incoming frequency. Omni Mass module provides the Amplitude data, Band selection and RFP to AHU-4 to measure the incoming pulse parameters. AHU-4 receives saturated video from four AHU-3 and measures the DF of incoming signal based on TDOA technique. Internally 18-40 GHz bite source is available to check the 18-40 GHz band health status in bite mode. 18-40 GHz bite source will provide 24 GHz and 36 GHz frequencies to conduct bite checks. In addition to 18-40 GHz band hardware, AHU-4 consists of 0.5 - 2 GHz and 2-18 GHz band bite hardware. Based on the ESMP bite command AHU-4 will send the bite RF to AHU-2 to process BB & NB Rx bite.

![](_page_62_Picture_5.jpeg)

**Figure-2.19: Pictorial View of ES AHU-4**

SHAKTI : UHB\Ch2 Page 62 of 614

![](_page_63_Figure_1.jpeg)

**Figure-2.20: Functional Block Diagram of ES AHU-4**

SHAKTI : UHB\Ch2 Page 63 of 614

**2.2.4.1 BITE Unit (18-40 GHz)**.Bite Unit is used as source of bite signal in 18-40 GHz band. Block diagram of the type-3 bite unit is as shown in **Figure.2.21**. It consists of 4 GHz PLO which is multiplied by 3 to generate 12 GHz signal. This signal is divided into 2 signals using 2 way power divider. Further, signal is multiplied by 2 to generate 24 GHz signal whereas second 12 GHz signal is multiplied by 3 to generate 36 GHz signal.

SHAKTI : UHB\Ch2 Page 64 of 614

![](_page_65_Figure_1.jpeg)

**Figure-2.21: Block Diagram of RF BITE Unit**

SHAKTI : UHB\Ch2 Page 65 of 614

**2.2.4.2 TDOA Processor PCB**.TDOA Processor PCB consists of Comparators, FPGA, Memory Chips, input/output Level Translators, Dual comparators, clock distribution, Ethernet along with the other supporting Ics. Further it contains VPX interface for data transfer & monitoring. Virtex-6 FPGA for processing, control, configuration. Controlling DAC's 1 to 3 from FPGA's for generating threshold/BITE voltages ranging 0-4V.Controlling Clock Distribution Unit to generate sampling clock for ADC's. Clock generation (500MHz) of ADC with 1 PPM will be done by using Clock Synthesizer. Reference clock for FPGA and Clock synthesizer shall be of 40MHz and 20MHz respectively. Board shall operate on +5V input power supply &on board power supply voltages are generated by using DC-DC converters. Rocket I/O communication shall be established from VIRTEX-6 FPGA on VPX backplane through Backplane LVDS Buffers. Ethernet PHY interface is provided through VPX Backplane. The test jig is used for testing the TDOA processor board by providing the mating connectors to interface with the main board.

SHAKTI : UHB\Ch2 Page 66 of 614

![](_page_67_Figure_1.jpeg)

**Figure-2.22: Block Diagram of TDOA Processor Board**

SHAKTI : UHB\Ch2 Page 67 of 614

**2.2.4.3 Receiver Processor Board**. The Receiver Processor Board is a VPX based board which is used for parameter measurement and generates 192 bit PD word. The RPB converts the 192 bit parallel PDW data into high speed serial data using RIO interface on AURORA protocol and finally sends the data through back plane. This board also receives commands from ESMP, decodes the received commands and generates the relevant control data for ADF & NB front end receivers and sends acknowledgement to ESMP. The Receiver Processor Board is 233.5 mmx160 mm x 20 mm (Double Euro with 6U form factor and should fit into a 6U VPX chassis) with conduction cooled board and wedge locking for fixing. The Receiver Processor Board Block Diagram as shown in **Figure 2.23**.

![](_page_68_Figure_2.jpeg)

**Figure-2.23: Block Diagram of Receiver Processor Board**

- **2.2.4.4 BITE Source Monitor PCB**.The BITE Source Monitor PCB would be responsible to convert the incoming Analog signals to corresponding Differential signals accordingly. The BITE Source Monitor will be operated on 5V DC input power, required other internal power supplies will be generated from incoming 5V.
- 2.2.4.4.1 It has threshold 1 and threshold 2 which can be adjustable. This voltage is generated by using the voltage divider rule with the resistors. The output of this threshold voltage is given to the comparator. The output of comparator will be logic 1 when the amplifier output voltage is greater than the threshold voltage and logic 0 for when the amplifier output voltage is lesser than the threshold voltage.
- **2.2.4.5 DIFM Receiver 2-18 GHz**.The 2.2-18 GHz Digital Instantaneous Frequency

SHAKTI : UHB\Ch2 Page 68 of 614

Measurement (DIFM) Receiver consists of RF Front End, Delay Lines, Phase Correlators, Video Processing circuit, Digitizers and Frequency Resolving Hardware using FPGA.

- 2.2.4.5.1 The DIFM Receiver measures the frequency of the input signal in the band of 6- 17 GHz for 18-40 GHz band by detecting the phase shifts magnitudes produced in multiple calibrated delay lines. The received RF signal is divided and simultaneously introduced into a non-delayed path and a delay line of known length. Since the phase difference between the delayed and non-delayed receiver paths is a function of input signal frequency, conversion of the phase difference signals to video signals provides signals whose amplitudes are related to phase delay. The processing circuit that follows makes use of resolving ambiguity of higher delay line phases and declaring that frequency O/P from the highest delay.
- **2.2.4.6 Freq Synthesizer 2-18G 488.28K**. Freq Synthesizer 2-18 GHz 10dBm is used in Shakti-BB & NB Rx AHU. The unit has a Video input, and a RF output port (SMA-F connectors: J4 and J1) Power Supply and control connector (D-sub connectors: J2 and J3). It generates an RF signal corresponding to input tuning word in frequency range of 2- 18 GHz. The Video port is used for FM modulation, but is not used in the system. **Table-2.8** gives the details for frequency selection.
- 2.2.4.6.1 The "Tuning word" relation with "Tuning frequency" is as follows:

Tuning Word (in Decimal) = [Set Frequency (in MHz) – 1975]\*2

**VCO Freq Tuning Word (in Dec) V0 BIT** 1 2000 3670 50 3390 0 2 3630 6020 3310 8090 1 3 5098 8020 8010 12090 0 4 7980 10002 12010 16090 1 5 9980 12720 16010 21490 0 6 12680 15320 21410 26690 1 7 15250 18000 26610 32050 0

**Table-2.8: Frequency selection of 2-18 GHz Synthesizer**

**2.2.4.7 Freq Synthesizer 0.5-2G 10dBm**.Freq Synthesizer 0.5-2 GHz 10dBm is used in Shakti BB& NB Rx AHU. The unit has a RF output port (J1, SMA), Video input (J2, SMC), Power Supply and control connector (D-sub connectors: J3 and J4). It generates an RF signal corresponding to input tuning word in frequency range of 0.5-2 GHz. The Video

SHAKTI : UHB\Ch2 Page 69 of 614

port is used for FM modulation, but is not used in the system. Below **Table-2.9** gives the details for frequency selection.

2.2.4.4.2 The "Tuning word" relation with "Tuning frequency" is as follows:

Tuning Word (in Decimal) = [Set Frequency (in MHz) – 475]\*2

**Table-2.9: Frequency selection of 0.5-2 GHz Synthesizer**

| Output Freq (MHz) |      | VCO     | Control |
|-------------------|------|---------|---------|
| From              | To   | V1(MSB) | V2(LSB) |
| 500               | 810  | 0       | 0       |
| 790               | 1240 | 0       | 1       |
| 1220              | 2000 | 1       | 0       |

- **2.2.5 ES Rack-1**.Pictorial view and block diagrams of ES Rack-1 shown below in **Figure 2.24** and **Figure 2.25**. The ES Processor Rack is 19" Rack and houses Rx Processor, ESM processor and ES Rack-1 Control Unit. The ES Rack-1 contains following hardware.
  - (a) Receiver Processor LRU
  - (b) ESM Processor LRU
  - (c) ES Rack-1 Control Unit
- 2.2.5.1 This LRU consists of the following PCBs:
  - (a) Receiver Interface Board
  - (b) Quad Digital Receiver
  - (c) Signal Monitoring Board
  - (d) Emitter Processor (EP) Board
  - (e) Pulse Processor & De-interleaver (PPD) Board -1
  - (f) Pulse Processor & De-interleaver (PPD) Board -2
  - (g) Rack-1 Interface PCB Board

SHAKTI : UHB\Ch2 Page 70 of 614

![](_page_71_Picture_1.jpeg)

**Figure-2.24: Pictorial view of ES Rack-1**

![](_page_71_Figure_3.jpeg)

**Figure-2.25: Block Diagram of ES Rack-1**

SHAKTI : UHB\Ch2 Page 71 of 614

**2.2.5.1 Receiver Processor**.Receiver Processor LRU is part of the NBRx (0.5-18 GHz) chain of Shakti ES system. Receiver Processor LRU mainly consists of 4 Quad Digital Receiver (QDR) boards, one Receiver Interface Board (RIB) and one Signal Monitoring Board (SMB). This LRU receives 16 IF (1000 ± 250 MHz or 160 ± 20 MHz) inputs from AHU2 and internally 4 IFs will be routed to each QDR card. Each QDR card will measure the pulse parameters and computes DOA and will send the Pulse Descriptor Word (PDW) to RIB. RIB will resolve the DOA ambiguity and will send the final PDW to ESM processor through optical link. ESMP will process the PDW and generates the track and will send the track to SCD for the display. It has also got one Signal Monitoring Board. This board receives differential status signals (RFPs & BLK) from other Units/Racks converts it into TTLs and the same signals can be monitored on front Panel Monitoring Connectors.

#### 2.2.5.1.1 Receiver Processor LRU consists the following hardware

- (a) H/W RIB&QDR VPX Chassis
- (b) Quad Digital Receiver Board
- (c) Receiver Interface Board
- (d) Signal Monitoring Board

![](_page_72_Figure_7.jpeg)

**Figure-2.26: Functional Block Diagram of Receiver Processor LRU**

**2.2.5.2 H/W RIB &QDR VPX Chassis**.The QDR RIB System is an air cooled 19" chassis with a custom designed VPX backplane. Four conduction cooled boards (QDR) with VPX connectors will be top loaded on to the back plane. The data transfer between the boards and the external receivers which are outside the VPX Chassis is carried out

SHAKTI : UHB\Ch2 Page 72 of 614

through the Back Panel connectors. The data transfer from/to Back Panel to the mother board (backplane) is carried out through interface cable.

#### **2.2.5.2.1 The QDR RIB System Houses the following modules:**

- (a) 19'' rack mount air cooled Chassis
- (b) VPX Based passive Backplane
- (c) Power Supply
- (d) Receiver Interface Board
- (e) Quad Digital Receiver 4No
- (f) Signal Monitor Board
- **2.2.5.3 Quad Digital Receiver**.The Quad Digital Receiver (QDR) is a sub-system of an ELINT system and measures the pulse parameters of radar in real time. The radar signal of 0.5 –18 GHz will be down converted to an IF using suitable Front End Receiver and fed to Quad Digital Receiver. This sub-system is built around Ultra High speed, Low Power, High Performance 10 bit ADC's and Xilinx 7 series FPGAs.
- 2.2.5.3.1 The Quad Digital Receiver hardware accepts 4 IF inputs in the frequency range of 750-1250MHz (IBW: 500MHz) /140-180 MHz (IBW: 40MHz) and input frequency will be in one of the above Two bands at any given time. These 4 inputs in various bandwidths will be passed through switched filter i.e.DC-1250MHz (LPF) as given in specifications. The inputs are amplified and filtered to eliminate any spurious signals with a chain gain of 12dB to meet the input power level requirements of ADC. These signals are fed to ADCs which operate at 1350MHz of sampling rate. The sampled data will be fed to theVirtex-7 FPGAs. FPGAs receive the sampled data in real time for further processing. The processed data is given out to a third FPGA and the results of the processing are fed as an output through a 51 pin 'D' Connector and also VPX connectors.
- 2.2.5.3.2 Basically Quad Digital Receiver Hardware will have two sub modules. i.e
  - (a) The IF section
  - (b) Quad Digital Rx Main Board
- **2.2.5.4 ESM Processor**.ESM Processor Chassis is a part of Shakti ES system. It mainly consists of three Pulse Processor (PP) boards, three Pulse Processor Rear Transition Module (PPRTM) boards, one Emitter Processor (EP) Board, one Emitter Processor Rear Transition Module (EPRTM) Board, one 5-slot VPX backplane and one AC-DC Power supply module. This LRU receives Pulse Descriptor Word (PDW) data from RPU, RIB, RPB and LBP through optical link. It processes the PDW and generates the track data and sends the track data to SCD for the display.

SHAKTI : UHB\Ch2 Page 73 of 614

![](_page_74_Figure_1.jpeg)

**Figure-2.27: Block Diagram of ESM Processor**

SHAKTI : UHB\Ch2 Page 74 of 614

- **2.2.5.5 Control Unit(ES Rack-1)**.ES Rack-1 Control Unit provides the 24V DC supply to Switch ON the ES Sub systems and distributes the Reset control to all ES Sub systems. It receives the health status of all ES sub systems and displays the Health status through front panel LED indications.
- 2.2.5.5.1 By pressing the ES ON Switch on the SCD, Remote ON control reaches to Control Unit and Control Unit distributes the Remote ON Control to all the sub systems as per system configuration.
- 2.2.5.5.2 By pressing the ES Reset on the SCD, Reset Control reaches to Control Unit and Control Unit distributes the Reset control to all ES sub systems as per system configuration.
- 2.2.5.5.3 Control Unit receives the health status of all ES sub systems through RS422 lines and display the status through LED indication on the front panel of control unit.
- **2.2.6 ES RACK-2**.This consists of 0.175-0.5 GHz band hardware (Low Voltage Power Supply, Multi Channel RF Unitand Low Band Processor Unit) and RFPS Processor LRU and Low Voltage Power Supply-1 and 2 for 0.5-40 Ghz band.
- 2.2.6.1 Low band Low voltage power supply provides the DC supply to ASU and MCRFU units. MCRFU unit receives the 0.175-0.5 GHz band RF 5 channels from ASU and converts RF to IF 70MHz.Low band processor unit measures the pulse parameters and sends the track data to ESMP.
- 2.2.6.2 RFPS processor internally consists of wide band tuner and processor section. Wide Band Tuner converts the 2.2-18 GHz RF to IF of 1 GHz/160MHz and sends to the processor section. Processor section consists of SBC, DAU and DSP cards processes the IF and displays the finger print details of the radar pulse.
- 2.2.6.3 LVPS-1 and 2 provides the DC supplies to 0.5-18 GHz and 18-40 GHz band mast mount sub systems.

SHAKTI : UHB\Ch2 Page 75 of 614

![](_page_76_Picture_1.jpeg)

**Figure-2.28: Pictorial View of ES Rack-2**

SHAKTI : UHB\Ch2 Page 76 of 614

![](_page_77_Figure_1.jpeg)

**Figure-2.29: Block Diagram of ES Rack-2**

SHAKTI : UHB\Ch2 Page 77 of 614

- **2.2.6.1 Multi Channel RF Unit (LB1-Shakti)**. Multi Channel RF Unit employs double conversion super heterodyne technique to meet high sensitivity, spurious free dynamic range, better image rejection and good selectivity over the frequency range of 175 – 500 MHz All the 5 independent receivers are identical in all respect for maintaining the gain and phase matching. It consists of five-channel gain and phase matched RF Tuner, PLL synthesized local oscillators, Calibration source (FSM), Embedded Receiver Controller (ERC) and Power Supply Unit (PSU). These modules are mounted in an ATR form factor chassis and it is powered from 15 Volts DC. Calibration source signal from FSM and RS422 interface commands from ERC to control ASU.
- 2.2.6.1.1 The MCRFU unit consists of five phase matched V/UHF Tuner modules, one Frequency Synthesizer module, one Embedded Receiver Controller module and one Power supply module. The five parallel outputs of the ASU is fed to Multi channel RF unit.The received signal in MCRFU is passed through five designated switch filter bank (SFB) , the selected output signal are initially up converted to 1755 MHz, with the use of variable LO-1(Step size-2MHz) and then the up converted RF signals are down converted to 70 ± 5MHz IF signals with the use of fixed LO-2 of 1685 MHz.Thus the final output of the MCRFU is the 5 in no. 70MHz IF signal.

![](_page_78_Picture_3.jpeg)

**Figure-2.30: Pictorial View of MCRFU**

SHAKTI : UHB\Ch2 Page 78 of 614

![](_page_79_Figure_1.jpeg)

**Figure-2.31: Block Diagram of MCRFU**

**2.2.6.2 Receiver Processor (LB1)**.The configuration of Receiver Processor Unit is based on Direct Digital DF & DIFM principle where IF signal is sampled by Analog-to-Digital Converter (ADC) and processed in Field Programmable Gate Arrays (FPGA) after passing through Multi Ch. RF Unit and IF Module between the starting element – antennae and last element – A/D converter in direct digital receiver. It consists of Penta -Channels DF Processor Board having High End FPGA of Virtex 6 with LX series for developing DF/DIFM detection algorithm, the Rx and Amp Processor board having High End FPGA of Virtex 6 with LX series for amplitude , pulse width measurement and final processing, IF module to provide I and Q outputs Power supply board, Mother Board ,PPD Card with rocket I/Os, Ethernet , FO and VPX Chassis.

SHAKTI : UHB\Ch2 Page 79 of 614

![](_page_80_Picture_1.jpeg)

**Figure-2.32: Pictorial View of Receiver Processor (LB1)**

**2.2.6.3 LVPS-1**. The Low Voltage Power Supply-1 is rugged in construction and designed to comply for MIL-810F (as applicable) Environmental Standards, and MIL-461E/F (as applicable) EMI/EMC Standards. All the components used are MIL-Grade only and will be capable to withstand the temperature variations and humidity. The LVPS-1 caters for DC power supply requirements of all components of BB & NB Receiver AHU.

**Table-2.10: O/P Voltage Details of LVPS-1**

| LVPS-1                   |     |                   |                   |     |                       |     |                         |     |     |      |      |
|--------------------------|-----|-------------------|-------------------|-----|-----------------------|-----|-------------------------|-----|-----|------|------|
| AHU-2<br>Connec-<br>-tor |     | J304<br>(PS1,PS5) | J305<br>(Ps3,PS7) |     | J306<br>(PS2,PS6,PS9) |     | J307<br>(Ps4&8,Ps10&11) |     |     |      |      |
| Rated                    | +9V | -9V               | +9V               | -9V | +9V                   | -9V | +5V                     | +9V | -9V | +15V | -15V |
| Supply<br>(A)            | 25A | 4A                | 30A               | 4A  | 25A                   | 4A  | 20A                     | 20A | 4A  | 20A  | 8A   |

**2.2.6.4 LVPS-2.** The LVPS-2 caters for DC power supply requirements of all components of ES AHU-4 and ES AHU-3 . O/p voltage details are given as below.

**Table-2.11: O/P Voltage Details of LVPS-2**

| LVPS-2             |               |     |      |                   |     |  |
|--------------------|---------------|-----|------|-------------------|-----|--|
| AHU-2<br>Connector | J204(PS1,PS3) |     |      | J206(PS5,PS6,PS7) |     |  |
|                    | +9V           | -9V | +15V | -15V              | +5V |  |
| Rated Supply(A)    | 20A           | 6A  | 28A  | 18A               | 20A |  |

**2.2.6.5 RFPS Processor**.RFPS WBT & Processor present in ES Rack-2, provides the

SHAKTI : UHB\Ch2 Page 80 of 614

in-built radar finger printing capabilities across 0.175 – 40 GHz band. This LRU houses the Wide Band Tuner and RFPS Electronics encapsulated into a common rack mount enclosure. The RFPS has a 3 slot VPX back plane and houses the following hardware:

- (a) Data Acquisition Board (DAC)
- (b) Quad Digital Signal Processing Board (QDSP)
- (c) Single Board Computer (SBC)
- (d) SP3T switch for selection of IF of appropriate band
- (e) MUX Board for selection of DRTG of appropriate band
- **2.2.6.6 Wide Band Tuner**.The RF in put to Wide Band Tuner is from 2.2-18 GHz (Omni) or 18-40 GHz (Omni) down converted to 6-17 GHz. The Wide Band Tuner generates corresponding 160 MHz/1 GHz IF based on command. In addition to this, LRU receives IF of 70 MHz from 0.175-0.5 GHz Tuned Receiver, IF of 160 MHz/1 GHz from Narrow Band Receiver NBRx.
- **2.2.6.7 Power Supply Unit**.The Power Supply Unit (AHU1) is designed to comply with a wide range of military standards for 230Vin systems. It is designed to provide +15V DC Output voltage with all protections like input over voltage / under voltage (OV/ UV), output over voltage, over load, short circuit and thermal protections. The Power Supply Unit (AHU1) is rugged in construction and designed to comply for MIL-810F (as applicable) Environmental Standards and MIL-461E (as applicable) EMI/EMC Standards. All the components used are MIL-Grade only and will be capable to withstand the temperature variations and humidity.
- **2.2.7 System Controller & Display (SCD) Rack**.This is a single operator controlled Integrated console for both EW and RFPS. This Rack consists of an integrated Processor LRU which houses two independent processors for System Controller & RFPS), two 20.1'' LCD monitors (for System Controller & RFPS) and System Control Panel LRU. The keyboard and mouse are shared between System Controller (EW) and RFPS processors. The integrated processor LRU is configured on VME back plane with built-in power supply modules. The application s/w and the user friendly MMI enables exploitation of the entire system from this rack.

SHAKTI : UHB\Ch2 Page 81 of 614

![](_page_82_Picture_1.jpeg)

**Figure-2.33: Pictorial View of SCD Rack**

SHAKTI : UHB\Ch2 Page 82 of 614

![](_page_83_Figure_1.jpeg)

**Figure-2.34: Block Diagram of SCD rack**

- **2.2.8 Ethernet Switch**.The Ethernet switch provides connectivity among the subsystem of ES system, EA system and external interfaces (through) ESI unit.
- **2.2.9 External System Interface (ESI) Unit**.This unit interfaces SHAKTI system with other systems/interfaces of the platform. The data/signals from the platform like Ship's heading, vertical gyro, GPS data, onboard radars etc., required by the system are interfaced through this unit. The external data of the platform received by this unit is converted into the format suitable to the various subsystems and distributed to the respective subsystem.

SHAKTI : UHB\Ch2 Page 83 of 614

![](_page_84_Picture_1.jpeg)

**Figure-2.35: Pictorial View of ESI**

- 2.2.9.1 The ESI interfaces with GPS for navigation data consisting of latitude, longitude and time information. It interfaces with Gyro for getting Roll, Pitch and Yaw information. These GPS and Gyro data is received in a Single packet of Data called SHHD-Ship House Hold Data through RS422 serial link. This information, i.e., both navigational and gyro data, is passed on to the Shakti EW system.
- 2.2.9.2 The ESI interfaces with on-board Radar for blanking the EW system during own Radar transmission. For this Radar pre-triggers will be taken from the on-board Radars and blanking signals are generated by ESI and given to Shakti EW System. In a Particular configuration, Pre-Trigger inputs of ESI are allotted for different frequency of Bands in the range of 0.175-40 GHz and respective Blanking outputs will be generated for different receivers of Shakti EW System.
- **2.2.10 Fault Diagnostic Rack**.This rack houses the standard test equipment (up to 40 GHz) required for testing and tuning of both ES & EA subsystems. The test equipment includes RF Signal Generator, Spectrum analyzer, Power Meter, Logic State Analyzer and an Oscilloscope.
- **2.2.11 Uninterrupted Power Supply (UPS)**.A pictorial view of UPS is shown in **Figure 2.36**. Uninterrupted Power Supply (UPS) constantly monitors power conditions and regulates voltage and frequency. Even when presented with the most severe power problems, UPS's output remains within 3% of nominal voltage. High 0.9 output power factor enables the UPS to provide its full power capability to modern IT equipment. Highest efficiency to reduce utility and cooling spending. When power conditions are within acceptable limits, the UPS can operate in a high-efficiency mode providing 95 percent efficiency. The internal bypass allows service continuity in case of internal fault, a maintenance bypass is also available (as option) for easy replacement of the UPS without

SHAKTI : UHB\Ch2 Page 84 of 614

powering down critical systems.

![](_page_85_Picture_2.jpeg)

**Figure-2.36: Uninterrupted Power Supply (UPS)**

**Table-2.12: Technical Specifications of UPS**

| Ser | Attribute           | Value                                                         |
|-----|---------------------|---------------------------------------------------------------|
| 1   | Warranty            | 2 Year(s)                                                     |
| 2   | Output Power        | 1 Watt                                                        |
| 3   | Recharge Time       | 5 to 8 Hr(s)                                                  |
| 4   | Features            | 15-20 Minutes At Battery Full Charge Condition<br>Backup Time |
| 5   | Techno Features     | In Built ZPD Technology                                       |
| 6   | Protection Features | Off Mode Battery Charging With High Voltage<br>Protection     |
| 7   | Wave Form           | Pseudo Sine Wave                                              |
| 8   | UPS Type            | Online                                                        |
| 9   | Segment             | Office                                                        |
| 10  | Size and Dimension  | Weight 8.9 kilos.                                             |
| 11  | Color               | Black outer body.                                             |
| 12  | Output Voltage      | UPS is 230V AC±10%.                                           |
| 13  | Output Frequency    | 50Hz±1%.                                                      |
| 14  | General Capacity    | This UPS can be applied on two computers with                 |

SHAKTI : UHB\Ch2 Page 85 of 614

| Ser | Attribute | Value              |
|-----|-----------|--------------------|
|     |           | 430cm TFT monitors |

**2.3 EA System Description**.The List of EA Units is given in **Table 2.13**. The description of each unit is explained in succeeding paragraphs. Configuration diagram of Shakti-EA is given in **Figure 2.37**.

SHAKTI : UHB\Ch2 Page 86 of 614

![](_page_87_Figure_1.jpeg)

**Figure-2.37: Configuration Diagram of Shakti-EA**

SHAKTI : UHB\Ch2 Page 87 of 614

**TABLE-2.13: LIST OF EA UNITS**

| Ser   | Description                              | BEL Part No. |
|-------|------------------------------------------|--------------|
| 1     | EA RACK-1                                | 172300353779 |
| 1.1   | EA Control Panel                         | 172300346989 |
| 1.2   | EA Processor Module                      | 172300358823 |
| 1.3   | Control Panel I/F PCB                    | 172300364158 |
| 1.4   | Low Voltage Power Supply (EACP)          | 172300532938 |
| 1.5   | Low Voltage Power Supply (MB2)           | 172300441176 |
| 1.6   | Low Voltage Power Supply (HB)            | 172300441273 |
| 2     | EA RACK-2                                | 172300353876 |
| 2.1   | Servo Control Unit (1-AXIS)              | 172300452428 |
| 2.2   | Servo Control Unit (2-AXIS)              | 172300452525 |
| 3     | MB2 JAMMER                               | 172300353973 |
| 3.1   | Low Power Unit (MB2)                     | 172300346407 |
| 3.1.1 | High Speed ADC/DAC Module                | 172300358241 |
| 3.1.2 | RFC& NG Module                           | 172300358629 |
| 3.1.3 | LP(MB2) Filter PCB                       | 172300564754 |
| 3.1.4 | DDUC 4 CH 6-18 GHz                       | 476678340124 |
| 3.1.5 | Freq synthsizer 6-18 GHZ 100 KHZ         | 456072040267 |
| 3.1.6 | MW OSC VC DGTL tuned 6-18G+10DBM         | 453572650288 |
| 3.1.7 | DET 50 OHMS 6-18G                        | 455872390114 |
| 3.2   | MB2-Transmitter Unit                     | 172300785526 |
| 3.2.1 | High Power Linear Array ANT. With Radome | 172300176560 |
| 3.2.2 | BMPM C-Ku 100 W                          | 113060006663 |

SHAKTI : UHB\Ch2 Page 88 of 614

| Ser    | Description                               | BEL Part No. |
|--------|-------------------------------------------|--------------|
| 3.2.3  | SW RF SPDT 6-18G 300W                     | 454277350147 |
| 3.2.4  | ROTMAN lens beam forming N/W(6-18<br>GHz) | 172300243102 |
| 3.2.5  | Control I/F Module                        | 172300695413 |
| 3.2.6  | AMP PWR 6-18G 27dBm                       | 456172430126 |
| 3.2.7  | Switch CO SPST 1-18G 2.5DB                | 454272870105 |
| 3.2.8  | SW RF CO17P 6-18G 50dB 27dBm              | 454277340156 |
| 3.2.9  | DET 50OHMS 6-18G                          | 455872390114 |
| 3.2.10 | AMP PWR 6-18G 20dBm                       | 456172430223 |
| 3.2.11 | MB2-Tx FILTER MODULE                      | 172300785720 |
| 3.2.12 | Cable Assy RF 50 SMA ST /SMA ST           | 488072920133 |
| 3.2.13 | Cable Assy RF 50 Z TNC                    | 488072930318 |
| 3.3    | MB2-Front End Assy                        | 172300785429 |
| 3.3.1  | Sectoral Horn Rx Ant (6-18<br>GHz)        | 172300292184 |
| 3.3.2  | MBJ-FE                                    | 455678780151 |
| 3.4    | Servo Drive Assembly (1-AXIS)             | 172300452234 |
| 4      | HB JAMMER                                 | 172300354070 |
| 4.1    | Low Power Unit (HB)                       | 172300346795 |
| 4.1.1  | High Speed ADC/DAC Module                 | 172300358241 |
| 4.1.2  | RFC& NG Module                            | 172300358629 |
| 4.1.3  | LP(HB) Filter Module                      | 172300564560 |
| 4.1.4  | DDUC 1CH 18-40<br>GHz                     | 476678350115 |
| 4.1.5  | OSC DR 10<br>GHz +10dBm                   | 453572730119 |
| 4.1.6  | Harmonic Detection Module(18-40<br>GHz)   | 476672990380 |
| 4.1.7  | Isolator 18-40<br>GHz 14dB                | 454172310108 |

SHAKTI : UHB\Ch2 Page 89 of 614

| Ser    | Description                              | BEL Part No. |  |
|--------|------------------------------------------|--------------|--|
| 4.1.8  | FREQ SYNTHSR 6-18<br>GHZ 100KHZ          | 456072040267 |  |
| 4.1.9  | MW OSC VC DGTL TUNED 6-18G+10DBM         | 453572650288 |  |
| 4.1.10 | DET 50OHMS 18-40G                        | 455872400105 |  |
| 4.2    | Front End Unit (HB)                      | 172300346601 |  |
| 4.2.1  | Pyramidal Horn Rx Antenna (18-40<br>GHz) | 172300322836 |  |
| 4.2.2  | MMJ-FE                                   | 455678790142 |  |
| 4.3    | Transmitter Unit (HB)                    | 172300346892 |  |
| 4.3.1  | Pyramidal Horn Tx Antenna(18-40 GHz)     | 172300292087 |  |
| 4.3.2  | MMJ-Tx INTERFACE PCB                     | 172300384819 |  |
| 4.3.3  | TRANSMITTER HVPS (HB)                    | 172300452719 |  |
| 4.3.4  | MWT TWT 18-40G 40W                       | 418972130264 |  |
| 4.3.5  | AMP LN 18-40G 20dB 5DB                   | 453777020170 |  |
| 4.3.6  | DET 50 OHMS 18-40G                       | 455872400105 |  |
| 4.4    | Transmitter Power Supply (HB)            | 172300452622 |  |
| 4.5    | Servo Drive Assembly (2-AXIS)            | 172300452331 |  |
| 5      | Transmitter Power Supply (MB2)           | 172300354264 |  |
| 6      | Heat Exchanger Unit                      | 172300354167 |  |

**2.3.1 MB2 Jammer**.This EA sub-system receives the threat signal from the environment for which jamming action is initiated by ES system, using two sectoral horn antennas, each covering quadrant of a sector (i.e. an angle of 90 X 10). One of the Antennae can be selected based on the measured DOA data from the ES system. The sub-system is mounted on a single axis servo system covering an angle of 180 sector. The received signal is amplified to the required level in the front-end receiver and down converted to the base band of Digital RF Memory (DRFM) i.e. 1.5-2.5 GHz using a Double down/up converter module (DDUC). For handling four threats simultaneously, the DDUC module is configured with a four channel activity detection module to detect the leading edge of the each threat signal. A dedicated Synthesized Local oscillator for each threat

SHAKTI : UHB\Ch2 Page 90 of 614

with better phase noise characteristic and frequency stability is used as a Local oscillator to down/up convert the received signal to/from the base band of DRFM. Double down/up conversion mechanism is adopted to reduce the harmonic/spurious signals generated by the system to the required level at both IF output and final RF output. The stored data is, then read out and re-constructed to an Analog IF signal after applying suitable jamming modulations. The IF signal is then up converted to its original frequency using double up conversion process, amplified to high power signal level using MPM and transmitted through Rotman lens and Phased Array Antenna by electronically beam steering in the direction of threat signal. This sub-system is configured with the following modules.

- (a) MB2-Front End Assy
- (b) Low Power Unit (MB2)
- (c) MB2-Transmitter Unit
- (d) Servo Drive Assembly (1-Axis)
- **2.3.1.1 MB2-Front End Assy**.To receive the RF signal in 6-18 GHz band, Front-end Unit (MB2) is configured with two Front-end (MB2) modules and two sectoral horn antennae for covering 180 sector. This module intercepts the radar threat signals of slant, vertical, horizontal and circular polarizations from the environment through two independent sectoral horn antenna switch polarizer embedded Radome having minimum gain of 7 dB, each covering an angle of 90 X 10, in the frequency range of 6-18 GHz. The received signal from each quadrant is amplified to the required level in the respective front-end units. This Unit is located on the top of the Transmitter Unit to improve the sensitivity of the EA system.
- 2.3.1.1.1 Front-end (MB2) consists of high power limiter and low noise amplifier. The high power limiter protects the microwave components of the receiver from excessive RF power received by the system from the environment. The front-end amplifier with low noise figure improves the signal amplitude to the required level enabling proper detection of intercepted threat signal across the dynamic range. Pictorial view and block diagrams of Front End Module (MB2) are shown below in **Figure 2.38** and **Figure 2.39**.

SHAKTI : UHB\Ch2 Page 91 of 614

![](_page_92_Picture_1.jpeg)

**Figure-2.38: Pictorial View of MB2-Front End Assy**

![](_page_92_Figure_3.jpeg)

**Figure-2.39: Block Diagram of MB2-Front End Assy**

- **2.3.1.2 Low Power Unit (MB2)**.This Unit receives the threat signals from the Front End Unit (MB2) for which jamming action is initiated by ES system, using two sectoral receiving horn antennae and two front end Units, each covering 90 thus covering 180 sector in total. As each LP Unit requires handling of four threats simultaneously on each sector side, a double down/up converter module with a 4-channel activity detection module is configured to handle the threat signals on pulse-by-pulse basis, leading to an improvement in jamming effectiveness.
- 2.3.1.2 As the modern radars transmit pulse signals with coherent intra-pulse modulation characteristics, this unit is configured based on state-of-art Digital RF Memory (DRFM) technology with a maximum Instantaneous band width (IBW) of 1000 MHz to effectively counter these radars using advanced jamming techniques. The DRFM module covers a narrow frequency band of 1.5 GHz to 2.5 GHz compared to the 6-18 GHz wide frequency band covered by most of the tracking & weapon guidance radars. Hence, the received

SHAKTI : UHB\Ch2 Page 92 of 614

radar/missile signal is down converted to the base band of DRFM using double down conversion process for sampling and storing in DRFM memory. The stored data is, then read out and re-constructed to an analog IF signal after applying suitable jamming modulations. The IF signal is then up converted to it's original frequency using double up conversion process, amplified to high power signal level in Transmitter (MB2) and transmitted in the direction of threat signal.

- 2.3.1.2 The LP Unit (MB2) generates both Noise and Deception jamming techniques and their combinational techniques.As the radar can change it's frequency during jamming, a 'LOOK THROUGH' mechanism is implemented to periodically update with the latest threat frequency signal being transmitted by the radar.
- 2.3.1.3 Block diagram and Pictorial view of Low Power Unit (MB2) are shown below in **Figure 2.40** and **Figure 2.41**.

![](_page_93_Picture_4.jpeg)

**Figure-2.40: Pictorial View of Low Power Unit (MB2)**

SHAKTI : UHB\Ch2 Page 93 of 614

![](_page_94_Figure_1.jpeg)

**Figure-2.41: Block Diagram of Low Power Unit (MB2)**

SHAKTI : UHB\Ch2 Page 94 of 614

This sub-system is configured with the following modules.

- (a) 4-channel Double down/up converter with Synthesizer LO's.
- (b) Digital RF Memory (with 1000 MHz Instantaneous Band Width (IBW) & Techniques Generator).
- (c) Noise Generation Module with Digitally Tuned Oscillator
- (d) RF Controller Module
- **2.3.1.2.1 4-Channel Double Down/Up Converter**.It receives the threat signals from the environment for which jamming action is initiated by ES system, using two sectoral receiving horn antennae and two front end Units, each covering 90 thus covering 180 sector in total. The amplified signal of respective quadrant from the front-end Module is down converted to the base band of Digital RF Memory (DRFM) i.e. 1.5-2.5 GHz using a Double down/up converter module (DDUC). The DDUC module is configured with four channel activity detection module with each channel dedicated for each threat signal being handled by the system. A dedicated 6-18 GHz Synthesized Local oscillator with a phase noise characteristic of -90 dBc/Hz @ 1KHz away from carrier and a frequency stability of 0.05 PPM/C is used for the threat handled by the system. As each 6-18 GHz MB2 Jammer is required to handle four threats, four such synthesized local oscillators are used to meet the system requirements. Double down/up conversion mechanism is adopted to reduce the harmonic/spurious signals generated by the system to the required level at both IF output and final RF output. Block diagram of 6-18 GHz 4-channel DDUC module is shown in **Figure 2.42**.

SHAKTI : UHB\Ch2 Page 95 of 614

![](_page_96_Figure_1.jpeg)

**Figure-2.42: Block Diagram of 6-18 GHz 4-Channel DDUC Module**

SHAKTI : UHB\Ch2 Page 96 of 614

- 2.3.1.2.1.1 Once jamming command is initiated by the ES system, the Synthesized Local oscillator (LO-1 to 4) is tuned to a frequency based on the frequency data from ES system such that the down converted frequency IF-1 is always around 4.0 GHz. Switch filter modules are selected to open the required Instantaneous band width (IBW) based on the band width of frequencies covered by the threat radar. The Switch-delay module is selected to store the RF signal in the delay line enabling sampling and storing of threat pulse signal in the DRFM from the leading pulse itself.
- 2.3.1.2.1.2 Based on the DoA information, the threat signal is received by the receiving antenna and fed to the front-end module. The received RF signal is amplified and fed to both Activity detection module and double down converter module. The RF signal in activity detection module is down converted to an IF-1 of 4 GHz using a double balanced mixer (M1) and detected from the video output (V1) of EDLVA-1. The LO selection module selects the Synthesized local oscillator (LO1) for 1st down conversion of RF signal in the double down converter module (DDC module). The received pulse signal is stored in the delay line of Switch delay module so that the RF signal can be stored in Digital RF Memory from the leading edge of the received pulse. Then, switch filter module (SFM-12) is selected to reject the image frequency and the second harmonics of the front-end amplifiers to reduce the level of inter-mod products within the pass band due to the second down conversion process.
- 2.3.1.2.1.3 The RF signal from the receiver module is fed to a double balanced mixer (M5) and down converted to an IF-1 of 4.0 GHz. The IF-1 signal is amplified and fed to another Double balanced mixer (M6) to down convert to 2nd IF (IF-2) of 2 GHz using a Di-electric Resonant Oscillator (DRO) / Digitally Tuned Oscillator (DTO) at a frequency of 6.0 GHz. The DRO is selected as second LO when deception jamming techniques are to be applied on the threat signal and DTO is selected when spot noise technique is to be applied on the threat frequency. Then, the IF-2 signal is amplified to a constant signal level using a high gain limiting amplifier and fed to DRFM Module.
- 2.3.1.2.1.4 As the isolation between the receiver and transmitter antennae of EA system is not adequately high, the threat signal cannot be received and transmitted simultaneously during jamming. Hence, the complete pulse length of a selected radar signal is stored in DRFM initially and no transmission occurs during this period. Based on the leading edge detection of the next pulse, the frequency of the received pulse is validated in DRFM and the corresponding data is read out from DRFM for re-construction to an analog IF signal.
- 2.3.1.2.1.5 Then the IF-2 signal is fed to a double balanced mixer (M7) in Double up converter module (DUC module) for up conversion to an IF-1 signal (4.0 GHz) using either a DRO or a DTO. In case of spot noise jamming technique, the DTO is tuned to a frequency of 6.0 GHz and then modulated with a FM signal to generate a spot noise signal of required band width. The spot noise signal is then used as a LO signal to the mixer M7 for up conversion. DRO is selected for up conversion to IF-1 signal during the application of deception jamming techniques. The IF-1 signal then up converted to original radar frequency using a double balanced mixer (M8) with the same Synthesized Local Oscillator

SHAKTI : UHB\Ch2 Page 97 of 614

frequency signal that is already used for down conversion process.

- 2.3.1.2.1.6 During Barrage noise jamming technique, the noise jamming signal is directly generated at the radar frequency using the DTO (unlike in the case of spot noise signal) and then directly fed to SPDT switch (SPDT-4) for further amplification and transmission. This mechanism is implemented to achieve flat frequency response of barrage noise signal to counter Least Jam Frequency (LJF) Electronic Protection (EP) of radar.
- 2.3.1.2.1.7 A final SPST switch (SPST-3) is used to generate angular deception jamming techniques like Scan Rate Modulation (SRM), Swept Scan Rate Modulation (SSRM) and Blink technique. The final modulated RF signal is then fed to MBTU for further amplification.
- **2.3.1.2.2 Digital RF Memory (DRFM) with 1000 MHz IBW**.As the modern radars have a wider frequency agility of 1000 MHz, DRFM is configured to have such wider instantaneous band width (IBW) meeting the requirements. DRFM can effectively handle Pulse compression / coherent radar signals and can repeat the threat signals without any degradation in their intra-pulse modulation characteristics thus compensating the processing gain of the modern radars on the ship-borne platforms. Each DRFM Module can handle 4 threats. The Block Diagram of DRFM Module is shown in **Figure 2.43**.

![](_page_98_Figure_5.jpeg)

**Figure-2.43: Block Diagram of DRFM**

2.3.1.2.2.1 The DRFM module operates in the frequency range of 1500 MHz to 2500 MHz with built-in Techniques Generator. DRFM is mainly configured with an IQ De-modulator, a modulator, High Speed dual ADC, two high speed DACs, Quad Data Rate (QDR) memory and Field Programmable Gate Array (FPGAs). The Radar signals in 6-18 GHz band are down-converted to the base band of DRFM using a down/up converter module

SHAKTI : UHB\Ch2 Page 98 of 614

realized as a RF super-component module. The input signal of 1500 MHz to 2500 MHz is Quadrature down converted to DC - 500 MHz, I & Q baseband signals using a 2 GHz inband stable Local oscillator.

- 2.3.1.2.2.2 I & Q baseband signals are sampled using High speed ADCs meeting the Nyquist sampling rate. The ADCs output data is captured using Virtex-7 FPGA and stored in the dual-port memory. During transmission, the stored data is read-out from the memory and sent to high speed DACs to re-construct back to I & Q analog signals. These Analog IQ signals are in turn quadrature up-converted back to the base band of DRFM i.e. 1500 MHz to 2500 MHz band using the same 2 GHz Local Oscillator. The output of DRFM module in converted to original radar frequency using the up converter part of RF Super component module.
- 2.3.1.2.2.3 The DRFM is configured with built-in Techniques Generator that can generate both Noise and Deception jamming techniques and their combinational techniques. A suitable combinational technique with appropriate parameters can be selected against each radar to be handled by the system to achieve jamming effectiveness. TG is configured around Virtex-7 FPGA and controlled by Black-fin processor. DRFM IP core & TG hardware are realized within the FPGA. The black-fin processor interfaces with EA processor and configures TG hardware to realize appropriate jamming techniques.
- 2.3.1.2.2.4 Deception Jamming Techniques that are realized are Range Gate Pull Off/ In (RGPO / RGPI), Velocity Gate Pull Off / In (VGPO/ VGPI), Synchronous RGPO/VGPI, Synchronous RGPI/VGPO and Multiple Range/velocity False Targets and Random Range False Targets (RANRAP).
- 2.3.1.2.2.5 Noise jamming techniques that are realized are narrow band noise (Doppler band noise), Cover pulse noise, Spot noise and Wide band noise (Barrage noise).
- 2.3.1.2.2.6 Angular deception jamming techniques like Scan Rate Modulation (SRM), Swept Scan Rate Modulation (SSRM) and blink techniques are generated by the system along with Noise/Range/velocity deception techniques to deceive the threat radar in angle.
- **2.3.1.2.3 RFC & NG Module**.This RFC & NG Module is used as an interface to the EA Processor and MB2 Jammer. This module is configured with the following Submodules.
  - (a) Noise generation Module
  - (b) RF Controller Module
- **2.3.1.2.3.1 Noise Generation Module along with DTO**.DTO based Noise jamming techniques (Spot / Barrage) will be implemented by applying either digital or Analog noise added with DDS based ramp signal to the FM modulation port of DTO. In case of spot noise technique, the DTO tuned at 6 GHz, is used as a local oscillator in DDUC for down converting the intercepted signal to the base band of DRFM. During up conversion, the

SHAKTI : UHB\Ch2 Page 99 of 614

FM noise signal of required band width generated by Noise Generation Module along with DTO is used as LO signal to generate the spot noise technique at victim radar frequency. As the same DTO is used for down/up conversion process, the tuning frequency error of DTO is automatically compensated, avoiding additional hardware for AFC correction. The Automatic frequency correction of jammer signal frequency is not required for barrage technique as the jamming signal bandwidth is large compared to the tuning frequency error of the DTO. During barrage noise jamming, the DTO is directly tuned to radar frequency covering 6-18 GHz and the band width varies from 60 MHz to 400 MHz covering the frequency range of agile radar/multiple radars to be encountered.

- 2.3.1.2.3.1.1 Noise generation Module generates a high resolution digital ramp waveform using high speed DAC added with either Digital noise of pseudo random nature or Analog white Gaussian noise. The amplitude of ramp signal is made programmable using a variable gain amplifier and is applied to the FM modulation port of DTO to have various noise bandwidths. Block diagram of Noise generation Module is as shown in **Figure 2.44**.
- 2.3.1.2.3.1.2 Noise Generation Module receives the video signals from the 4-CH DDUC for the intercepted radar signals based on the commanded threats. These video signals will be further compared with the threshold using DAC, and generates the TTL signals for corresponding threats for storing / retrieving the radar RF signals in the DRFM.

![](_page_100_Figure_4.jpeg)

**Figure-2.44: Block Diagram of Noise Generation Module**

**2.3.1.2.3.2 RF Controller Module**. RF controller Module is used to generate the requisite control signals and tuning command which are required for all the other modules of Low power unit (MB2) for the operation of 6-18 GHz.

SHAKTI : UHB\Ch2 Page 100 of 614

2.3.1.2.3.2.1 RF Controller Module is configured with Artix-7 FPGA to control functions of RF super component, DTO and Synthesized LO Bank. The Module also functions as interface between EA processor and Low Power EA system through RS422 interface. System commands are received through serial link using RS422 lines. System commands received by RF controller Module will be sent to DRFM and CIB Module. The block diagram of RF controller Module is shown in **Figure 2.45.**

![](_page_101_Figure_2.jpeg)

**Figure-2.45: Block Diagram of RF Controller Module**

**2.3.1.3 MB2-Transmitter Unit**.This unit works on spatial power combination technique. The RF signal radiated from n number of elements of linear array is combined in the space and forms the beam perpendicular to the wave front. The beam can be steered in the space by controlling the phase of the RF signal applied to the elements of the linear array. Multi beam transmitter employs Rotman Lens fed Linear Array concept to produce fixed contiguous beams in the coverage angle of the array.

2.3.1.3.1 To produce high Effective Radiated Power from MBT each element of the 16 element linear antenna array is fed with medium output power of 100 watts generated by using state of the art Microwave Power Modules (MPM) with phase & gain matching characteristics which is introduced between Rotman Lens and Linear array. The output power of each antenna element is combined in space to form a jammer beam with a beam width of 6 X 10 @ 18 GHz achieving the required ERP of 50 KW in the direction of the

SHAKTI : UHB\Ch2 Page 101 of 614

threat radar to be countered. The direction of the jammer beam can be switched at a faster rate in a quadrant of 90 using a Rotman lens and SP16T switch. The output power of each MPM can be switched between the corresponding elements of two linear antenna array using a high power SPDT switch. Thus, 16 nos. of high power SPDT switches are used to switch the MPM output simultaneously so that the jammer beam can be switched between two quadrants at a speed of 2 µs, thus reducing the system overall size & weight. Pictorial view and block diagram of Transmitter Unit (MB2) are shown below in **Figure 2.46** and **Figure 2.47**.

![](_page_102_Picture_2.jpeg)

**Figure-2.46: Pictorial View of Transmitter Unit (MB2)**

SHAKTI : UHB\Ch2 Page 102 of 614

![](_page_103_Figure_1.jpeg)

**Figure-2.47: Block Diagram of Transmitter Unit (MB2)**

SHAKTI : UHB\Ch2 Page 103 of 614

**2.3.1.4 Transmitter-Power Supply Unit (MB2)**.The input supply required for Tx-PS (MB2) units is derived from ship supply of 380V, 50 Hz, 3Ø through Isolation Transformers. The output DC voltage is 270V which is required for MPM modules of Tx (MB2). Each Tx-PS (MB2) unit provides DC voltages to eight MPM modules. Hence two Tx-PS (MB2) units are configured for the system on the Port side and two on the Star Board side. These units can be switched ON from EA Rack-1. The Pictorial view of Tx-PS (MB2) is shown in **Figures 2.48**.

![](_page_104_Picture_2.jpeg)

**Figure-2.48: Pictorial View of Transmitter-Power Supply Unit (MB2)**

**2.3.1.5 Servo Drive Assembly (1-Axis)**.The 6-18 GHz transmitter unit employs electronic beam scanning concept using the Transmitter unit (MB2), the azimuth directional alignment is taken care by proper beam switching. The elevation plane alignment has to be done using a 'Roll stabilization platform'. The Tx (MB2) hardware is placed on this platform which gets Roll information data from ship's SHHD through ESI. In the design, the Pitch information is not taken for stabilization as the maximum effect is achieved using roll data itself. The Roll stabilization will be applied in accordance with Roll data ensuring the alignment of the Tx antennae in the elevation plane. The Block diagram and Pictorial view of Servo Drive Assembly (1-Axis) is shown in **Figure 2.49 & Figure 2.50.**

SHAKTI : UHB\Ch2 Page 104 of 614

![](_page_105_Figure_1.jpeg)

**Figure-2.49: Block Diagram of Servo Drive Assembly (1-Axis)**

![](_page_105_Picture_3.jpeg)

**Figure-2.50: Pictorial View of Servo Drive Assembly (1-Axis)**

**2.3.2 HB Jammer**.This EA sub-system receives the threat signal from the environment for which jamming action is initiated by ES system, using a pyramidal receiving horn antenna having a beam width of 7 X 7 @ 37 GHz and positioned towards the direction of threat based on the measured DOA data from the ES system. The sub-system is mounted on a two-axis servo system covering an angle of 180 sector. The received signal is amplified to the required level in the front-end receiver and down converted to the base band of Digital RF Memory (DRFM) i.e. 1.5-2.5 GHz using a Double down/up converter

SHAKTI : UHB\Ch2 Page 105 of 614

module (DDUC). The DDUC module is configured with a single channel activity detection module to detect the leading edge of the threat signal. A dedicated Synthesized Local oscillator with better phase noise characteristic and frequency stability is used as a Local oscillator to down/up convert the received signal to/from the base band of DRFM. Double down/up conversion mechanism is adopted to reduce the harmonic/spurious signals generated by the system to the required level at both IF output and final RF output. The stored data is, then read out and re-constructed to an analog IF signal after applying suitable jamming modulations. The IF signal is then up converted to its original frequency using double up conversion process, amplified to high power signal level using a conventional TWT based amplifier and transmitted in the direction of threat signal.

- 2.3.2.a This sub-system is configured with the following modules.
  - (a) Front End Unit (HB)
  - (b) Low Power Unit (HB)
  - (c) Transmitter Unit
  - (d) Transmitter Power Supply
  - (e) 2-Axis Servo Drive Assembly
- **2.3.2.1 Front End Unit (HB)**. To receive the RF signal in 18-40 GHz band, this Unit is configured with a pyramidal horn antenna and Front End module. Pyramidal horn antenna is mounted with 45º to provide slant linear 45º polarization and having a gain of 24 dB, covering an angle of 7 X 7 @ 37 GHz. Front End module is configured with a Limiter and Amplifier. A limiter is used to protect the MMW down/up converter module against any high power signal received by the system. A front-end amplifier with low noise figure is used after the limiter to achieve better sensitivity and dynamic range. The block diagram and pictorial view of Front End Module (HB) is shown below in **Figure 2.51 & Figure 2.52**.

![](_page_106_Figure_9.jpeg)

**Figure-2.51: Block Diagram of FE Unit (HB)**

SHAKTI : UHB\Ch2 Page 106 of 614

![](_page_107_Picture_1.jpeg)

**Figure-2.52: Pictorial View of FE Unit (HB)**

**2.3.2.2 Low Power Unit (HB)**.This Unit receives the 18-40 GHz threat signal from the environment for which jamming action is initiated by ES system, using sectoral horn antenna and front end Unit covering 180sector.As each LP Unit requires handling of single threat simultaneously on each sector, a double down/up converter module with a 1-channel activity detection module is configured to handle the threat signal on pulse-by-pulse basis, leading to an improvement in jamming effectiveness.

2.3.2.2.a As the modern radars transmit pulse signals with coherent intra-pulse modulation characteristics, this unit is configured based on state-of-art Digital RF Memory (DRFM) technology with a maximum Instantaneous band width (IBW) of 1000 MHz to effectively counter these radars using advanced jamming techniques. The DRFM module covers a narrow frequency band of 1.5 GHz to 2.5 GHz compared to the 6-18 GHz wide frequency band covered by most of the tracking & weapon guidance radars. Hence, the received radar/missile signal is down converted to the base band of DRFM using double down conversion process for sampling and storing in DRFM memory. The stored data is, then read out and re-constructed to an analog IF signal after applying suitable jamming modulations. The IF signal is then up converted to it's original frequency using double up conversion process, amplified to high power signal level in Transmitter (HB) and transmitted in the direction of threat signal.

2.3.2.2.b The LP Unit (HB) generates both Noise and Deception jamming techniques and their combinational techniques. As the radar can change it's frequency during jamming, a 'LOOK THROUGH' mechanism is implemented to periodically update with the latest threat

SHAKTI : UHB\Ch2 Page 107 of 614

frequency signal being transmitted by the radar.

- 2.3.2.2.c Block diagram and Pictorial view of Low Power Unit (HB) are shown in the **Figure 2.53 and Figure 2.54**.
- 2.3.2.2.d This sub-system is configured with the following modules:
  - (a) 1-channel Double down/up converter with Synthesizer LO's.
  - (b) Digital RF Memory (with 1000 MHz Instantaneous Band Width (IBW) & Techniques Generator).
  - (c) Noise Generation Module with Digitally Tuned Oscillator.
  - (d) RF Controller Module.

SHAKTI : UHB\Ch2 Page 108 of 614

![](_page_109_Figure_1.jpeg)

**Figure-2.53: Block Diagram of Low Power Unit (HB)**

SHAKTI : UHB\Ch2 Page 109 of 614

![](_page_110_Picture_1.jpeg)

**Figure-2.54: Pictorial View of Low Power Unit (HB)**

**2.3.2.2.1 1-Channel Double Down/Up Converter**.Once jamming command is initiated, the receiver antenna located on the 2-axis servo pedestal is positioned towards the direction of threat to be handled by the system based on the measured DOA information from the ES system. The Synthesized Local oscillator (LO) with doubler is tuned to a frequency such that the down converted frequency (IF-1) is always around 8.0 GHz. For the input frequencies between 18-28 GHz, the LO output frequency is tuned between 26- 36 GHz and for the input frequencies above 28 GHz and up to 40 GHz, the LO output frequency is tuned between 20-32 GHz so that the IF-1 is always at 8 GHz. Then, one of the four band pass filters in Switch filter module (SFM-1) i.e. 18-25 GHz, 24-31 GHz, 30- 35 GHz and 34-40 GHz bands, is selected to receive the threat signal frequency and reject it's image frequency. Simultaneously, one of the four band pass filters in Switch filter modules SFM-2& SFM-3 are selected to open the EA receiver for the required Instantaneous band width (IBW) depending on the band width of frequencies covered by the threat radar. The SPST switch in delay line path of Switch-delay module is selected to store the RF signal, enabling sampling and storing of threat pulse signal in the DRFM from the leading pulse itself. Now, the EA receiver is set ready to receive and detect the threat radar pulse signal for initiation of jamming action. The BPF selected in Switch filter module (SFM-2) will also be useful for gating the required frequencies and reject the unwanted signal frequencies avoiding the spurious signal detection. The Block Diagram of 1-CH Down/Up Converter shown in **Figure 2.55**.

SHAKTI : UHB\Ch2 Page 110 of 614

![](_page_111_Figure_1.jpeg)

**Figure-2.55: Block Diagram of 1-Channel D/U Converter**

SHAKTI : UHB\Ch2 Page 111 of 614

- **2.3.2.2.2 Digital RF Memory with 1000 MHz IBW**.This module is used in the configuration to handle the radars with a wide frequency agility band width. The DRFM used is similar to the one used in 6-18 GHz band and can generate the required Range, velocity and their combinational techniques.
- **2.3.2.2.3 RFC & NG Module**.This RFC & NG Module used is similar to the one used in 6-18 GHz band and acts as an interface to the EA Processor and HB Jammer. This module is configured with the following Sub-modules.
  - (a) Noise generation Module
  - (b) RF Controller Module
- **2.3.2.2.3.1 Noise Generation Module along with DTO**.DTO based Noise jamming techniques (Spot / Barrage) will be implemented by applying either digital or analog noise added with DDS based ramp signal to the FM modulation port of DTO. The Module used is similar to the one used in 6-18 GHz band and can generate the required Noise Jamming Techniques (Spot / Barrage).
- **2.3.2.2.3.2 RF Controller Module**. RF controller Module is used to generate requisite control signals and tuning command which are required for all the other modules of Low power unit (HB) for the operation of 18-40 GHz. System commands which are received through serial link using RS422 lines by RF controller Module will be sent to DRFM and Tx-HVPSM Module. The Module used is similar to the one used in 6-18 GHz band and can generate the required controls for other modules of Lower Power Unit.
- 2.3.2.2.3.2.1 RF controller Module is used to generate the requisite control signals and tuning command which are required for all the other modules of Low power unit (MB2) for the operation of 6-18 GHz.
- 2.3.2.2.3.2.2 RF Controller Module is configured with Artix-7 FPGA to control functions of RF super component, DTO and Synthesized LO. The Module also functions as interface between EA processor and Low Power Unit (HB) through RS422 interface. System commands are received through serial link using RS422 lines. System commands received by RF controller Module will be sent to DRFM and Tx-HVPS Module.
- **2.3.2.3 Transmitter Unit (HB)**.This sub-system employs a Servo based transmitter with 10KW ERP to handle conventional and exotic Radars. The transmitter amplifies the modulated jammer RF signal using TWT, and radiates through narrow beam jammer antenna having a beam width of 7 X 7 @ 37 GHz, to achieve the required ERP. Two transmitters will be positioned, one each on Port & Starboard side of the Foremast and each transmitter covering 180 sector, capable of handling one threat per sector. These transmitters are positioned on two axis servo pedestal to position the narrow jammer beam on the threat radar based on DOA information and to compensate the roll, pitch and yaw

SHAKTI : UHB\Ch2 Page 112 of 614

motions of the ship platform. Block diagram and pictorial view of Transmitter Unit (HB) are shown below in **Figure 2.56** and **Figure 2.58**.

2.3.2.3.1 Due to requirement of high DC Voltages of the order of 10 KV and operating in both pulsed & CW mode of operation depending on application of Noise/Deception Jamming techniques for the transmitter, Tx-HVPS Unit with a fast modulator is used to control the electron beam of the TWT. This Tx-HVPS Unit is mounted along with the Transmitter Unit (HB). Pictorial view of Tx-HVPS Unit (HB) is shown below in **Figure 2.57**.

![](_page_113_Picture_3.jpeg)

**Figure-2.56: Pictorial View of Transmitter Unit (HB)**

![](_page_113_Picture_5.jpeg)

**Figure-2.57: Pictorial View of Tx-HVPS (HB)**

SHAKTI : UHB\Ch2 Page 113 of 614

![](_page_114_Figure_1.jpeg)

**Figure-2.58: Block Diagram of Transmitter Unit (HB)**

SHAKTI : UHB\Ch2 Page 114 of 614

**2.3.2.4 Transmitter-Power Supply Unit (HB)**.The input supply required for Tx-PS (HB) unit is derived from ship supply of 380V, 50 Hz, 3Ø through Isolation Transformers. This Unit generates the output DC voltages which are required for Tx-HVPS (HB). Two Tx-PS (HB) Units are configured for the system on the Port side and Star Board side. The Pictorial view for AC-DC Converter module is shown in below **Figure 2.59**.

![](_page_115_Picture_2.jpeg)

**Figure-2.59: Pictorial View of Transmitter-Power Supply Unit (HB)**

**2.3.2.5 Servo Drive Assembly (2-Axis)**. The Two-axis servo consists of two units as a pair – one on Starboard side and other on Port side. These units carry electronic payloads. Purpose of TAS is to move these payloads in azimuth and elevation axis. Both the units have common 'Home' reference i.e. bow of the ship as '0'. Unit on starboard side can rotate from 350 to +190 in azimuth, whereas unit on port side rotate from 170 to +10 in azimuth. Thus together these two units provide 360º coverage for tracking and an overlap angle of 10 in both -clockwise and anti-clockwise direction. Block diagram and pictorial view of Transmitter Unit (HB) are shown below in **Figure 2.60** and **Figure 2.61**.

SHAKTI : UHB\Ch2 Page 115 of 614

![](_page_116_Figure_1.jpeg)

**Figure-2.60: Block Diagram of Servo Drive Assy (2-Axis)**

![](_page_116_Picture_3.jpeg)

**Figure-2.61: Pictorial View of SDA (2-Axis)**

- **2.3.3 EA Rack-1**.Pictorial view of EA RACK-1 is shown below in **Figure 2.62**. This sub-system is configured with the following modules.
  - (a) EACP LRU
  - (b) LVPS (MB2) (2 No's)

SHAKTI : UHB\Ch2 Page 116 of 614

(c) LVPS (HB)

![](_page_117_Picture_2.jpeg)

**Figure-2.62: Pictorial View of EA RACK-1**

- **2.3.3.1 EACP LRU**.This LRU is the main controller of the EA system. The Main Function of this LRU is:
  - (a) Interacts with other EA Subsystems and ES system for Effective Management of jammer resources
  - (b) Generates relay controls which are required for powering ON the EA Subsystems
  - (c) Generates power ON status to SCD Rack and EACP LRU itself
- 2.3.3.1.a This sub-system is configured with the following modules:
  - (a) EA Processor Module
  - (b) LVPS (EACP)
  - (c) Control Panel I/F PCB
- 2.3.3.1.b Block diagram of EACP LRU is shown below in **Figure 2.63**.
- **2.3.3.1.1 EA Processor Module**.It interacts with the ES Processor or System Controller

SHAKTI : UHB\Ch2 Page 117 of 614

- & Display to get the threat parameters and the jamming technique to be employed against each threat. Based on the threat information appropriate subsystems will be controlled to counter the threat Radar. The EA Processor is common to both 6-18 GHz and 18-40 GHz EA sub-systems. Block diagram of EA Processor Module is shown below in **Figure 2.64**.
  - (a) Interact with ES system to get the threat parameters and jamming techniques to be employed against the threat.
  - (b) Control Other EA Systems for Effective Management of jammer resources.
  - (c) Generate Look through signals for interception of the new Radar signals or for update of engaged threat radar signal parameters during jamming.
  - (d) Generate control signals to share the jammer resources among multiple threats.
  - (e) Interacts with the EA Control Panel to provide the status of the transmitters.
  - (f) Perform health checks of the EA Subsystem and sends the health report to ESM Display.
  - (g) Predict and Track the time of arrival of threat Radar signal (i.e. PRI Tracker)
- **2.3.3.1.2 LVPS (EACP)**.The input supply 230V, 50 Hz, 1Ø required for LVPS (EACP) is derived from ship supply of 415V, 50 Hz, 3Ø through Step down Transformer. This unit generates Output DC Voltages of +5V& 28V, which is required for the EACP LRU itself.
- **2.3.3.1.3 Control Panel I/F PCB**.The Main function of this PCB is to generate the relay controls, which are required for switching on the EA Subsystems. Block diagram of Control Panel I/F PCB is shown below in **Figure 2.65**.

SHAKTI : UHB\Ch2 Page 118 of 614

![](_page_119_Figure_1.jpeg)

**Figure-2.63: Block Diagram of EACP LRU**

SHAKTI : UHB\Ch2 Page 119 of 614

![](_page_120_Figure_1.jpeg)

**Figure-2.64: Block Diagram of EA Processor Module**

SHAKTI : UHB\Ch2 Page 120 of 614

![](_page_121_Figure_1.jpeg)

**Figure-2.65: Block Diagram of Control Panel I/F PCB**

SHAKTI : UHB\Ch2 Page 121 of 614

- **2.3.3.2 LVPS (MB2)**. The input supply 230V, 50 Hz, 1Ø required for LVPS (MB2) is derived from ship supply of 415V, 50 Hz, 3Ø through Step down Transformer. This unit generates Output DC Voltages of ±5V, ±15V, and 28V which are required for the Lower Power (MB2) & Transmitter (MB2) Units. Hence two LVPS (MB2) units are configured, which are required for the Lower Power (MB2) & Transmitter (MB2) Units on the Port side and Star Board side.
- **2.3.3.3 LVPS (HB)**.The input supply 230V, 50 Hz, 1Ø required for LVPS (HB) is derived from ship supply of 415V, 50 Hz, 3Ø through Step down Transformer. This unit generates Output DC Voltages of ±5V, ±15V and 28V which are required for the Lower Power (HB) & Transmitter (HB) Units. Single LVPS (HB) caters the DC Voltages, which are required for the Lower Power (HB) & Transmitter (HB) Units on the Port side and Star Board side.
- **2.3.4 EA Rack-2**.Pictorial view of EA RACK-2 is shown below in **Figure 2.66**. This sub-system is configured with the following Units.
  - (a) SCU (1-Axis)
  - (b) SCU (2-Axis)

![](_page_122_Figure_6.jpeg)

**Figure-2.66: Pictorial View of EA Rack-2**

**2.3.4.1 Servo Control Units (1-Axis).** SCU (1-Axis) along with SDA (1-Axis) is mainly

SHAKTI : UHB\Ch2 Page 122 of 614

used for the Roll Stabilization of the Tx (MB2) unit. After receiving command from EA Processor, Stabilization correction will take place according to the roll information supplied by the ship. Single SCU catering for both Port and the Star board pedestals. Block diagram of SCU (1-Axis) is shown below in **Figure. 2.67**.

**2.3.4.2 Servo Control Units (2-Axis)**.SCU (2-Axis) basically controls the movement of SDA (2-Axis) in azimuth and elevation planes. It receives the commands from ECM processor and moves the pedestal in the required direction. Also 2-Axis servo system stabilizes the pedestal based on roll & pitch information. The stabilization correction will take place according to the roll and pitch information supplied by the ship. Single SCU catering for both Port and the Star board pedestals. Block diagram of SCU (1-Axis) is shown below in **Figure. 2.68**.

SHAKTI : UHB\Ch2 Page 123 of 614

![](_page_124_Figure_1.jpeg)

**Figure-2.67: Block Diagram of Servo Control Unit (1-Axis)**

SHAKTI : UHB\Ch2 Page 124 of 614

![](_page_125_Figure_1.jpeg)

**Figure-2.68: Block Diagram of Servo Control Unit (2-Axis)**

SHAKTI : UHB\Ch2 Page 125 of 614

![](_page_126_Picture_0.jpeg)

**This page is Intentionally Kept Blank**

# **CHAPTER III UNPACKING AND REMOVAL OF PRESERVATIVES**

#### **CHAPTER – III**

#### **UNPACKING AND REMOVAL OF PRESERVATIVES**

**3.1 Introduction**.This chapter describes about the general instructions of unpacking with step by step procedure, initial checks and removal of preservatives.

#### **3.2 Unpacking**.

#### **3.2.1 General Instructions**.

- (a) Equipment is dispatched in professionally made high standard packing cases, wherever required additional wooden support structure, shock absorbers etc., are provided inside the packing cases to ensure safety of the equipment's.
- (b) Detailed list identifying the equipment parts is provided in the packing cases. This will be useful during installation and should be preserved along with the packing case.
- (c) Heavy units are provided with conveniently placed hoisting hooks. Procedures for handling and hoisting are described in the installation manuals.
- (d) Units should be carefully unpacked from the transit case. Before opening the packed case on receipt, it is essential to have the packing details.
- (e) The details regarding the total number of packing cases and contents of each packing case are given in the master packing note accompanying each consignment. After unpacking, check whether the unit/assembly details conform to the mentioned in the packing list.
- **3.2.2 Unpacking Procedure**.Shakti system is provided as per the deliverables mentioned in contract properly packed in the packing cases. These items include main equipment, sub assemblies, modules and LRU's etc. All items shall be mounted onboard as per the bp's and procedure mentioned in installation manual.
  - (a) Identify the item by part number available in packing note attached to the packing boxes or look for list of packing cases and list of units packed in it.
  - (b) Use proper tools for opening packing case and ensure sharp edges or tool tips should not touch/hit the items packed inside packing case.
  - (c) Observe symbols (fragile, handle with care) marked on packing case and

SHAKTI : UHB\Ch3 Page 127 of 614

handle them accordingly while unpacking.

- (d) All the Items are wrapped with bubble sheet around, placed in packing box. In case of PCBs, Items are wrapped with bubble sheet around, placed in an antistatic cover, covering box and packed in packing case.
- (e) Unlock pad lock/lock by key provided along with packing cases.
- (f) Open door available on the top side and ensure door opened completely and locked.
- (g) Unwrap the bubble sheet wrapped around the unit and identify eye bolts or hooks or handles for holding the unit.
- (h) Based on nature and weight of the unit, use proper crane for lifting the unit from inside the packing box.
- (j) Hold the unit by its eye bolts or hooks or handles and lift the item till it crosses the packing level of the packing box.
- (k) Use lifting frame provided along with installation materials for lifting some of the units (ref installation manual for lifting frame handled items).
- (l) Move slowly away from packing case and keep it on dry and clean horizontal base.
- (m) Verify the unit part number mentioned in name plate available on unit and find any physical damages.
- (n) Packing cases are professionally made for reuse. Ensure packing cases are stored safely for reuse.

## **3.2.3 Unpacking of Equipment**.

- (a) The subunit will be mounted on special made transport frames which are bolted to the wooden base of the packing case. The top slides of the packing cases are to be removed to get the access to the equipment inside.
- (b) The necessary accessories will be packed in the separate packing case. These shall be provided with packing lists clearly identifying the items contained within.
- (c) Unit should be carefully unpacked from the transit case. Before Opening the

SHAKTI : UHB\Ch3 Page 128 of 614

packed case on receipt, it is essential to have the packing details.

- (d) The details regarding the total number of packing cases and the content of each packing case are given in the master packing note accompanying each consignment. After unpacking, check whether the unit /assembly details conform to the details mentioned in the packing list.
- **3.3 Initial Checks**.Carryout the following checks immediately after unpacking.
  - (a) Inspect the equipment and accessories for any external damages such as bends, cracks, dents and any other abnormalities.
  - (b) Inspect all controls, connectors, and external fittings for loose fittings, misplacements, missing parts and damages.
  - (c) Operate all the knobs, controls and switches and check for their smooth operation without applying excessive force.
  - (d) Check the security of the panels and ensure that they are properly secured in the rack/cabinet.
- **3.4 Removal of Preservatives**.Preservatives are not used in this system.

SHAKTI : UHB\Ch3 Page 129 of 614

![](_page_131_Picture_0.jpeg)

**This Page is Intentionally Kept Blank.**

SHAKTI : UHB\Ch3 Page 130 of 614

# **CHAPTER IV PREPARATION FOR USE AND INSTALLATION SPECIFICATIONS**

#### **CHAPTER – IV**

## **PREPARATION FOR USE AND INSTALLATION SPECIFICATIONS**

- **4.1 Introduction**.This chapter describes about the initial inspection, setting instructions, interconnection details, installation instructions, and installation check list.
- **4.2 Initial Inspection**.Remove all the drawers / units / cabinets from the wooden packing boxes and keep the packing boxes safely for reuse. Observe the list of packing material for each wooden box and identify the number of items including quantity and serial numbers. Identify the material and perform physical inspection of each item for damages, scratches, paints etc. in case of any damage, intimate to the concerned officer of the organization for immediate action along with the inspection report. For further detail description Ref. to Installation Manual Chapter I Para 1.19
- **4.3 Setting Instructions**.The detailed setting instructions for Shakti system equipment are covered in installation specification manual separately. The details include installation procedures, preparation of EW Cables, and cabinet fixation including foundation diagrams and setting to work. The installation manual also includes the different tools to be used for fixing the cabinets, the limitations on the location and position of each cabinet / drawer / unit. The configuration diagram is also provided as part of installation specification manual. For further detail description Ref. to Installation Manual Chapter V and VI.
- **4.4 Interconnection Details**.The interconnection details indicating EW cables and connector designations are shown in installation manual. It provides the interconnection details between different units including external interfaces. The type of connectors, accessories and method of connection is explained in installation specification manual. While cabling the connectors, care should be taken against accidental shorting due to stray wire pieces, solder drops etc. These extra connections may not be revealed during inspection and can result in costly failures.
- 4.4.1 Only trained personnel are permitted to install the equipment. The personnel performing the operation must strictly adhere to safety precautions mentioned in the installation manuals. For further detail description Ref. to Installation Manual Chapter III Para 3.3
- **4.5 Installation Instructions**. The information on installation of the system is briefly described in the following.

SHAKTI : UHB\Ch4 Page 131 of 614

- **4.5.1 ES AHU-1 & ES AHU-2**.Clear field of view (-15° to +90°) in elevation and 360° in azimuth) is required for all the antennae in AHU-1 & 2. Datum alignment accuracy of ±0.1 deg is to be ensured for ES AHU-1 & 2. Surface flatness (levelling) of mounting base for ES AHU-1 and ES AHU-2 is to be ensured to the accuracy of 100 microns.
- 4.5.1.1 The Installation Sequence to be followed for installation of ES AHU-1 & ES AHU-2 is given below.
  - (a) Installation of Mounting Frame-1 onboard by matching its pre aligned flange to the prefabricated flange available inside the basket.
  - (b) Tighten nuts and bolts of M16 size with suitable spanner.
  - (c) Installation of BB-NB Rx unit of ES AHU-2 on the seating plate of Mounting Frame-1.
  - (d) Installation of BB & NB Rx is to be done by using lifting frame supplied as installation material.
  - (e) Installation of Mounting Frame-2 of pole mast assembly on pre welded SS screws available on seating plate of Mounting Frame-1.
  - (f) Tighten the Nuts/Screws (M8 & M12) by using lengthy T- spanner/box spanner with handle.
  - (g) Antenna array (LB-1) is having 5 elements shall be fixed to the mounting rings (2 no's) by using torque wrench supplied along with antenna.
  - (h) Mounting rings (2 no's) shall be mounted on pre machined and aligned flange available on mounting frame-2 of pole mast.
  - (j) Cables for Omni Modules and ES AHU-1 units are to be drawn through the crevices at the centre plate of Mounting Frame-1.
  - (k) Securing of maintenance platform & detachable Ladder on Mounting Frame-2 (above BB-NB Rx unit).
  - (l) Installation of units of ES AHU-1 & Omni Modules on mounting frame-2 of pole mast in following orientation.

SHAKTI : UHB\Ch4 Page 132 of 614

**Table-4.1: Units Orientation**

| Ser | Description                  | Location |
|-----|------------------------------|----------|
| 1   | Antenna Switching Unit (LB1) | NW       |
| 2   | OMNI Rx (MB-HB)              | SW       |
| 3   | Omni Mass (MB-HB)            | SE       |
| 4   | OMNI Rx (MB-HB)              | NE       |

- (m) Securing of cables on BB-NB Rx unit (A6) of ES AHU-2 and ES-AHU-1 using cable tray.
- (n) The top location of the mounting frame is left open for any other sensor as required by platform.
- (p) Refer installation manual for detail installation procedure for mounting the units.
- **4.5.2 ES AHU-3**.ES AHU-3 consists of sensitive electronic components and antenna and it caters to high band ESM segment of system. The four No's of ES AHU-3 Shall be mounted at the tip of the four-yard arms constructed at 45 deg angle w.r.t fore-aft axis. The yardarms shall be such that the antennae mounted on them, at the tip, form a perfect square of 10m side (14.14 meters diagonal).
  - (a) Installation of ES AHU-3 (4 no's) is to be done on tip of four yard arms available on ship platform.
  - (b) Each unit to be fixed to the pre aligned raised platform available on tip of the yard arm by driving captive screws in to the holes provided on it.
  - (c) Unit's connector points orient towards ship platform in which yard arm is welded as per the layouts.
  - (d) ES AHU-3 antenna points towards top from its base.
  - (e) Refer installation manual for detail installation procedure for mounting the units.
- **4.5.3 ES AHU-4**.ES AHU-4 consists of processing units for ESM segment of Shakti system. ES AHU-4 is to be mounted at the base of the pole mast on a raised platform of

SHAKTI : UHB\Ch4 Page 133 of 614

height 500 mm (min) to accommodate for cable bending radii. The unit is to be mounted on shock mounts supplied as a part of installation materials.

- (a) Installation of ES AHU-4 is to be done on raised platform available at base of the pole mast.
- (b) For movement of ES AHU-4 lifting frame which is supplied along with installation materials is to be used.
- (c) Remove brackets from the unit and keep screws for reassemble the brackets to the unit.
- (d) Assemble shock mounts to the brackets.
- (e) Reassemble Brackets along with shock mounts to the Unit.
- (f) Fix the Shock mounts to the base of the raised platform.
- **4.5.4 ES Rack-1**.ES RACK-1 consists of processing LRU's and control panel unit of ESM segment on slides. The rack is mounted on four no's of shock mount to the base and supported by 2 no's of shock mounts from rear. The seating arrangements & foundations shall be prepared as per binding data. ES RACK-1 houses three LRU are which are listed below in the order of its location from top to bottom.

**Table-4.2: List of LRU's in ES Rack-1**

| Ser | Item Description         | BEL part No.    | Qty  |
|-----|--------------------------|-----------------|------|
| 1   | Receiver processor       | 1723 003 476 68 | 1 No |
| 2   | ESM Processor            | 1723 003 477 65 | 1 No |
| 3   | Control Unit (ES Rack-1) | 1723 003 480 56 | 1 No |

- (a) Installation of ES RACK-1 is to be done on raised platform available at EWER compartment.
- (b) The shock mounts to be fixed to the foundations and to the top stays using M6x30 & M6 nuts along with plain & spring washers (four each for each shock mount).
- (c) Place the wired rack (without sub systems) on the shock mounts.
- (d) Secure the rack by using M10x20, M10x25 screws with plain and spring

SHAKTI : UHB\Ch4 Page 134 of 614

washers at rack top & bottom respectively.

- (e) Insert all the sub systems on to the slides in respective locations as shown above.
- (f) Connect all the connections of sub systems as per connector designations.
- (g) Secure each sub system by tightening front panel captive screws.
- (h) Connect all connections terminating on rack top (hat section) as per connector designation after removing the dust caps.
- (j) Ensure Rack Earthing stud (provided at Side) is connected to the ship ground using copper cable (Not in the scope of OEM supply).
- **4.5.5 ES Rack-2**.ES RACK-2 consists of processing units for low band, RFPS and low voltage power supplies for ESM segment of the system. The seating arrangements & foundations shall be prepared as per binding data. ES RACK-2 houses six LRU's which are listed below in the order of its location from top to bottom.

**Table-4.3: List of LRU's in ES Rack-2**

| Ser | Item description               | Bel part No.    | Qty  |
|-----|--------------------------------|-----------------|------|
| 1   | Power Supply (LB-1)            | 1723 007 057 92 | 1 No |
| 2   | Multi Ch RF Unit (LB-1)        | 1723 006 834 82 | 1 No |
| 3   | Receiver Processor Unit (LB-1) | 1723 006 833 85 | 1 No |
| 4   | RFPS WBT & Processor           | 1723 006 542 85 | 1 No |
| 5   | LVPS-2                         | 1723 003 479 59 | 1 No |
| 6   | LVPS-1                         | 1723 003 478 62 | 1 No |

- (a) Installation of ES RACK-2 is to be done on raised platform available at EWER compartment.
- (b) The shock mounts to be fixed to the foundations and to the top stays using M6x30 & M6 nuts along with plain & spring washers (four each for each shock mount).

SHAKTI : UHB\Ch4 Page 135 of 614

- (c) Place the wired rack (without sub systems) on the shock mounts.
- (d) Secure the rack by using M10x20, M10x25 screws with plain and spring washers at rack top & bottom respectively.
- (e) Insert all the sub systems on to the slides in respective locations as shown above.
- (f) Connect all the connections of sub systems as per connector designations.
- (g) Secure each sub system by tightening front panel captive screws.
- (h) Connect all connections terminating on rack top (hat section) as per connector designation after removing the dust caps.
- (j) Ensure Rack Earthing stud (provided at Side) is connected to the ship ground using copper cable (Not in the scope of OEM supply).
- **4.5.6 SCD Rack**.SCD Rack consists of two 20.1'' monitors, Operator console desk and SCD processor LRU and RFPS display processor LRU on slides. SCD rack mounting locations along with seating arrangements & foundations shall be prepared as per binding data. The console desk portion of SCD rack can be detached or ease of shipment to EWO compartment.
  - (a) The mounting procedure and installation instructions for all the racks are similar in all respect.
  - (b) The shock mounts to be fixed to the foundations and to the top stays using M6x30 & M6 nuts along with plain & spring washers (four each for each shock mount).
  - (c) Place the wired rack (without sub systems) on the shock mounts.
  - (d) Secure the rack by using M10x20, M10x25 screws with plain and spring washers at rack top & bottom respectively.
  - (e) Insert all the sub systems on to the slides in respective locations as shown above.
  - (f) Connect all the connections of sub systems as per connector designations.
  - (g) Secure each sub system by tightening front panel captive screws.
  - (h) Connect all connections terminating on rack top (hat section) as per connector designation after removing the dust caps.

SHAKTI : UHB\Ch4 Page 136 of 614

(j) Ensure Rack Earthing stud (provided at Side) is connected to the ship ground using copper cable (Not in the scope of OEM supply).

**Table-4.4: List of LRU's in SCD Rack**

| Ser | Item description      | BEL Part No.    | Qty  |
|-----|-----------------------|-----------------|------|
| 1   | Display Monitor       | 1723 003 570 77 | 2 No |
| 2   | Foldable Console Desk | 1723 003 701 72 | 1 No |

- **4.5.7 Rugged Ethernet Switch (TYPE-1 & 2)**.Rugged Ethernet Switches are used for providing network interface within the system and to the external platform units. The locations of the units along with seating arrangements & foundations shall be prepared as per binding data.
  - (a) Rugged Ethernet Switches Type-1 to be mounted in EWTR compartment.
  - (b) Rugged Ethernet Switch Type-2 (2 Nos.) to be mounted in EWO compartment.
  - (c) Routing should be aligned to the connector mounting of both switches available on the front face.
  - (d) RES's should be mounted in accessible location as per BP's.
- **4.5.8 External System Interface Unit (ESI)**.External System Interface (ESI) interface between Shakti EW system and various other onboard external sensors like Radars, Gyro & GPS, etc,. The bulk head seating arrangements shall be prepared as per OEM binding data. the unit is to be mounted close to ES RACK-1.
  - (a) ESI is to be mounted in EWER compartment.
  - (b) Unit to be mounted in accessible location as per BP's.
  - (c) Suitable maintenance space should also be maintained.
- **4.5.9 EA Rack-1**.EA Rack-1 consists of control panel and low voltage power supplies for EA segment of the system. The seating arrangements & foundations shall be prepared as per binding data. EA Rack-1 houses four LRU's which are listed below in the order of its location from top to bottom.

SHAKTI : UHB\Ch4 Page 137 of 614

## **Table-4.5: List of LRU's in EA Rack-1**

| Ser | Item Description                   | Bel Part No.    | Qty  |
|-----|------------------------------------|-----------------|------|
| 1   | EA Control Panel                   | 1723 003 469 89 | 1 No |
| 2   | Low Voltage Power Supply (MB2) (S) | 1723 004 411 76 | 1 No |
| 3   | Low Voltage Power Supply (MB2) (P) | 1723 004 411 76 | 1 No |
| 4   | Low Voltage Power Supply (HB)      | 1723 004 412 73 | 1 No |

- (a) Installation of EA Rack-1 is to be done on raised platform available at EWTR compartment.
- (b) EA Rack-1 requires more maintenance space compared to EA Rack-2.
- (c) The shock mounts to be fixed to the foundations and to the top stays using M6x30 & M6 nuts along with plain & spring washers (four each for each shock mount).
- (d) Place the wired rack (without sub systems) on the shock mounts.
- (e) Secure the rack by using M10x20, M10x25 screws with plain and spring washers at rack top & bottom respectively.
- (f) Insert all the sub systems on to the slides in respective locations as shown above.
- (g) Connect all the connections of sub systems as per connector designations.
- (h) Secure each sub system by tightening front panel captive screws.
- (j) Connect all connections terminating on rack top (hat section) as per connector designation after removing the dust caps.
- (k) Ensure Rack Earthing stud (provided at Side) is connected to the ship ground using copper cable (Not in the scope of OEM supply).
- **4.5.10 EA Rack-2**.EA Rack-2 consists of servo units for EA segment of the system. Seating arrangements & foundations shall be prepared as per binding data. EA Rack-2 houses LRU are which are listed below in the order of its location from top to bottom.

SHAKTI : UHB\Ch4 Page 138 of 614

## **Table-4.6: List of LRU's in EA Rack-2**

| Ser | Item Description            | Bel Part No.    | Qty  |
|-----|-----------------------------|-----------------|------|
| 1   | Switch Panel –<br>2U        | -               | 1 No |
| 2   | Servo Control unit (2-Axis) | 1723 004 525 25 | 1 No |
| 3   | Servo Control unit (1-Axis) | 1723 004 524 28 | 1 No |

- (a) Installation of EA RACK-2 is to be done on raised platform available at EWTR compartment.
- (b) The shock mounts to be fixed to the foundations and to the top stays using M6x30 & M6 nuts along with plain & spring washers (four each for each shock mount).
- (c) Place the wired rack (without sub systems) on the shock mounts.
- (d) Secure the rack by using M10x20, M10x25 screws with plain and spring washers at rack top & bottom respectively.
- (e) Insert all the sub systems on to the slides in respective locations as shown above.
- (f) Connect all the connections of sub systems as per connector designations.
- (g) Secure each sub system by tightening front panel captive screws.
- (h) Connect all connections terminating on rack top (hat section) as per connector designation after removing the dust caps.
- (j) Ensure Rack Earthing stud (provided at Side) is connected to the ship ground using copper cable (Not in the scope of OEM supply).
- **4.5.11 MB2 Jammer**. Two no's of Jammers each for port and STBD side of the ship as per installation and alignment requirements brought out earlier in the chapter is to be ensured. MB2 Jammer mounting locations along with seating arrangements & foundations shall be prepared as per the binding data.
- 4.5.11.1 MB2 Jammer has five sub units; these are listed below in sequence to be followed while installation.

SHAKTI : UHB\Ch4 Page 139 of 614

**Table-4.7: List of Sub units in MB2 Jammer**

| Ser | Item Description              | Bel Part No.    | Qty  | Total<br>Qty/System |
|-----|-------------------------------|-----------------|------|---------------------|
| 1   | Servo Drive Assembly (1-Axis) | 1723 004 522 34 | 1 No | 2 No                |
| 2   | MB2-Tx UNIT                   | 1723 007 855 26 | 1 No | 2 No                |
| 3   | Low Power Unit (MB2)          | 1723 003 464 07 | 1 No | 2 No                |
| 4   | MB2-<br>Front End Assy        | 1723 007 854 29 | 1 No | 2 No                |

- (a) Servo drive assembly (1-Axis) will be mounted on raised or aligned mounting frame available on ship platform.
- (b) Transmitter unit (MB2) shall then be mounted on servo drive assembly (1 axis) by matching holes available on both units.
- (c) Ensure the orientation of all sub units as per BP's and installation manual.
- (d) Low power unit will be mounted on bottom mounting holes of servo drive assembly (1-axis).
- (e) Utmost care should be taken while handling Rx horn assembly.
- (f) Both front end unit and Rx horn assembly will be mounted on the Transmitter Unit (MB2)
- (g) Connect all the connections of sub systems as per connector designations.
- (h) Secure each sub unit by tightening fasteners.
- **4.5.12 HB Jammer**.For Shakti system, HB Jammer's are to be mounted at 45 degrees offset w.r.t Fore-Aft Axis (Standby Position to alleviate the field of View obstructions due to Navigation Radars). HB Jammer (STBD) should be oriented towards forward side while HB Jammer (Port) should be oriented towards the aft side.
- 4.5.12.1 HB Jammer has six sub units; these are listed below in sequence to be followed while installation.

SHAKTI : UHB\Ch4 Page 140 of 614

**Table-4.8: List of Sub units in HB2 Jammer**

| Ser | Item Description              | Bel Part No.    | Qty  | Total<br>Qty/System |
|-----|-------------------------------|-----------------|------|---------------------|
| 1   | Front End Unit (HB)           | 1723 003 466 01 | 1 No | 2 No                |
| 2   | Low Power Unit (HB)           | 1723 003 467 95 | 1 No | 2 No                |
| 3   | Transmitter Unit (HB)         | 1723 003 468 92 | 1 No | 2 No                |
| 4   | Transmitter-HVPS (HB)         | 1723 004 527 19 | 1 No | 2 No                |
| 5   | Servo Drive Assembly (2-Axis) | 1723 004 523 31 | 1 No | 2 No                |
| 6   | Transmitter Power Supply (HB) | 1723 004 526 22 | 1 No | 2 No                |

- (a) Servo drive assembly (2-Axis) will be mounted on raised or aligned mounting frame available on ship platform.
- (b) Transmitter unit (HB) shall be mounted on servo drive assembly (2-axis) by matching holes available on both units.
- (c) Ensure the orientation & installation of all sub units as per BP's and Installation Manual.
- (d) Connect all the connections of sub systems as per connector designations.
- (e) Secure each sub unit by tightening fasteners called in installation manual.
- **4.5.13 Transmitter Power Supply (MB2)**. The SHAKTI system consists of 4 No's of Tx-PS, Two No's each for PORT&STBD MB2 jammers. The units are tray mounted from Bulkhead & foundations and locations shall be prepared as per as per Annex - H & I of the installation manual.
- **4.5.14 Heat Exchanger Unit (HEU)**.Heat Exchanger Unit (HEU) is used for cooling the jammer units of the system by circulating chilled water in closed loop. HEU employs mixture of Distilled water & Ethylene glycol in ratio 70:30. HEU works on principle of heat transfer between ship chilled water supply to its internal fluid mixture and send it to the Jammer units.
- 4.5.14.1 HEU Qty 2 Nos are used each dedicated for Jammer units in PORT/STBD configuration. The mounting foundations shall be as per prepared as per binding data.
  - (a) Lift the HEU using crane to the mounting location.

SHAKTI : UHB\Ch4 Page 141 of 614

- (b) Unit is to be mounted by using fasteners given in installation manual.
- (c) Ensure proper ventilation is available towards the condenser side of the unit.
- (d) Water Pipes are to be push fitted to the HEU as per markings and colour codes indicated in piping details given below.
- (e) Water pipes between HEU and Jammer units are to be routed on trays / conduits and thermally insulated.
- (f) Colour codes, lengths, & diameters of the pipes mentioned in installation manual.
- (g) Connectors terminating on each of the HEU are to be connected as per respective connector designations.
- (h) Flows in individual pipe lines is to be adjusted through gate valves in HEU based on pressure head loss beds & length while routing
- (j) Check for leakage at adaptor end before usage of unit. Use Teflon sheet and RTV at adaptor end of pipes to arrest any leakages.
- **4.5.15 Transformer Isolation & Step-Down 30KVA 380/415V-230V 3-PH**.Two Nos of Isolation Transformers (30 KVA each) provides isolated power supply to the SHAKTI system the mounting foundations shall be prepared as per binding data.
- 4.5.15.1 One No of 30 KVA Step down Transformer provides power supply to the Shakti system. It is used to provide 380/415-230V step-down power supply. The mounting arrangement & foundations shall be prepared as per binding data. Transformer Isolation 30KVA 380/415V 3-PH is a part of set of transformers (BEL Part no: 1723 003 551 37) under installation material.
  - (a) Lift the items using crane by using eyebolts provided on the unit
  - (b) Units to be mounted on raised platforms available in jammer compartment.
  - (c) Units are to be mounted by using fasteners given in installation manual.
  - (d) Ensure proper grounding is done from the stud available with the unit.
  - (e) Connect the terminals from the ship supply.

SHAKTI : UHB\Ch4 Page 142 of 614

**4.5.16 Power Distribution Panel Type 1 (PDP-1), Type-2 (PDP-2) & Type-3 (PDP-3)**.

Power Distribution Panel's are Power distribution units between transformers supply and units/sub systems of EA & ES segments. The mounting arrangement & foundations shall be prepared as per binding data.

- 4.5.16.1 Power Distribution Panel (PDP) Type-1, Type-2 & Type-3 is a part of Set of power supply accessories (BEL Part No: 1723 003 552 34) which is supplied as installation material.
  - (a) The units can be moved manually/crane by using handles provided on the units.
  - (b) Unit is to be mounted by using fasteners given in installation manual.
  - (c) Ensure proper grounding is done from the stud available with the unit.
  - (d) Wires routed through glands will be connected using lugs as per respective wire list.
  - (e) Tighten the glands to secure the cables and avoid any strain on the lugs.
- **4.5.17 Uninterrupted Power Supplies-1&2 (UPS-1 & UPS-2)**.Uninterrupted Power Supply (UPS-1) has inbuilt battery to provide online backup power for processor units used in SCD Rack. The mounting arrangement & foundations shall be prepared as per binding data. Uninterrupted Power Supply (UPS-1) is a part of installation materials.
- 4.5.17.1 Uninterrupted Power Supply (UPS-II) has inbuilt battery to provide online backup power for processor units in ES racks. The mounting arrangement & foundations shall be prepared as per the binding data. Uninterrupted Power Supply (UPS-II) is a part of installation materials.
  - (a) The units can be moved manually
  - (b) The bottom bracket of both units is the part of supply.
  - (c) The bracket provided along with the Unit is to be mounted on deck using fasteners given in installation manual.
  - (d) Ensure proper grounding is done from the stud available with the unit.
  - (e) Ensure clearance for air ventilation through fans provided on the rear of the

SHAKTI : UHB\Ch4 Page 143 of 614

unit.

**4.5.18 FDR Rack**.Fault Diagnostic Rack consists of test instruments used during maintenance and diagnosing faults in system. These units are mounted on standard hard mount/slides. FDR RACK mounting locations along with seating arrangements & foundations shall be prepared as per Annex - H & I of the installation manual. The Test instruments must be moved separately and carefully to compartment. The following Test instruments and LRUs are the part of FDR Rack.

**Table-4.9: List of Test Units and LRU's in FDR Rack**

| Ser | Item Description     | Bel Part No.    | Qty     |
|-----|----------------------|-----------------|---------|
| 1   | Digital Oscilloscope | 4736 726 201 36 | 1 No    |
| 2   | Signal Generator     | 4738 800 301 92 | 1 No    |
| 3   | Spectrum Analyser    | 4737 760 501 69 | 1<br>No |
| 4   | Storage Drawer-5u    | 1729 100 596 95 | 1 No    |

- (a) Installation of FDR RACK is to be done on raised platform available at EWER compartment.
- (b) The shock mounts to be fixed to the foundations and to the top stays using M6x30 & M6 nuts along with plain & spring washers (four each for each shock mount).
- (c) Place the wired rack (without sub systems) on the shock mounts.
- (d) Secure the rack by using M10x20, M10x25 screws with plain and spring washers at rack top & bottom respectively.
- (e) Insert all the sub systems on to the slides in respective locations as shown above.
- (f) Connect all the connections of sub systems as per connector designations.
- (g) Secure each sub system by tightening front panel captive screws.
- (h) Connect all connections terminating on rack top (hat section) as per connector designation after removing the dust caps.
- (j) Ensure Rack Earthing stud (provided at Side) is connected to the ship ground using copper cable (Not in the scope of OEM supply).

SHAKTI : UHB\Ch4 Page 144 of 614

For further detail description Ref. to Installation Manual Chapter V Para 5.3

- **4.6 Installation Check List**.The following paragraphs describe the checks to be done prior to the commencement of installation. The tests / checks to be conducted after installation prior to setting to work operations are also included.
- **4.6.1 Pre-Installation Checks**. Perform the following checks [Tick (V) if checked and found correct].

## **4.6.1.1 All Antenna Assemblies:**

- (a) Check that the seating holes of the antenna mounting plate fitted on the ship's mast matches with the antenna assembly.
- (b) Check that all cable lengths are as specified.

## **4.6.1.2 BB RX & NB RX, ES Rack-1&2, EA Rack-1&2 SCD Rack, ESI Unit & Ethernet Switches, MB2 & HB Jammers, Isolation/Step Down Transformers, LCU, Power Panels & UPS Assemblies**.

- (a) Check that the seating holes of the base plate fitted on the deck / bulkhead matches with the Racks / units assembly.
- (b) Check that all cable lengths are as specified.
- **4.6.2 Post Installation Checks**. Perform the following checks [Tick (V)'if checked and found correct]. Check that all units and subunits are installed.
  - (a) Check that all inter unit drawer connections are connected
  - (b) Check that cable continuity is good
  - (c) Check that all external cables are connected to the units/subunits as per inter unit cabling diagram.
  - (d) Check that earthing is connected.
  - (e) Check that power supplies both AC and DC available at the connector end as per specifications.
- **4.6.2.1 Cable Runs**.Check that connections to cables are made as per the interconnection details. Check that correct cable tags are fitted on the cable and the cables are mated to the correct connectors on the various units. Ensure that the cables

SHAKTI : UHB\Ch4 Page 145 of 614

are provided with an extra length of at least one meter, for use during possible future rework.

- **4.6.3 Earthing**.Check that the following units are earthed to ship's hull.
  - (a) AHU BB & NB Rx
  - (b) OMNI Modules (Mass &Rx)
  - (c) AHU-3
  - (d) AHU-4
  - (e) ASU
  - (f) EA Rack-1 & 2
  - (g) ES Rack-1 & 2
  - (h) SCD Rack
  - (j) ESI Unit
  - (k) Rugged Ethernet Switch modules
  - (l) MB2 Jammer & its sub units
  - (m) HB Jammer & its sub units
  - (n) Transformers (Isolation/step down)
  - (p) Power distributions panels (PDP-1,2&3)
  - (q) UPS -1 & 2
  - (r) HEU's
  - (s) FDR
  - (t) Power Supplies
- 4.6.3.1 For further detail description Ref. to Installation Manual Chapter IX.

# **CHAPTER V OPERATING INSTRUCTIONS**

#### **CHAPTER – V**

## **OPERATING INSTRUCTIONS**

- **5.1 Introduction**.This chapter describes the precautions and safety measures (dos and don'ts), the control and indicator details, the setting instructions, the sequence of operation of the Shakti system.
- **5.1.1 System Controller & Display Overview**.The system controller controls and configures the ES processor, EA processor, External System Interface (ESI), Radar Finger Printing System (RFPS), Combat Management System (CMS) and FDL. SCD will also be interfaced with LRSAM and KAVACH if the platform is equipped with them. The intercepted and analysed data of the ESM processor along with the results of identity search and the receiver activity status will be presented in graphical and alphanumeric formats. SCD presents HMI to the operator to configure and control receiver sub-systems through ES processor, perform jamming activities through EA processor of the EA sub-system. SCD will be interfaced with ESI for time, platform heading, positional information etc. Operator can select an ESM track on SCD HMI and send it to RFPS for finger printing. SCD will be interfaced with CMS for centralized command & controlling of Shakti EW system. The system controller and display also presents health status, diagnostics of the sub systems and the detailed library parameters for selected emitters. SCD will be connected to Field Data Loader (FDL) laptop for uploading/ downloading emitter library data, recorded scenario data files, map files etc. Conventions of this manual are:
  - (a) All the operations are described as step-by-step procedures with appropriate.
  - (b) Screen shots.
  - (c) The commands are written in bold letters.
  - (d) Notes are included for special attention in the applicable areas.
  - (e) For the similar type of operational procedures, the procedure is explained once and the section numbers are provided as reference to carry out the procedure further.
- **5.1.2 System Controller & Display Directories**.The following Table 5.1 gives details of the default directories of the system controller used for storing of data, i.e. ESM library files, recorded files, snapshot files, configuration files, map files and audio files.

SHAKTI : UHB\Ch5 Page 147 of 614

**Table: 5.1 Description of Default Directories used by System Controller**

| Ser | Directory          | Directory                              | Purpose of Directory                                                                                                                                                                                                                                                                                      |
|-----|--------------------|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | Audio<br>tones     | /home/Shakti<br>SCD/ShaktiSCD<br>1.4.5 | This<br>directory<br>contains<br>all<br>audio file in .wav format which<br>are used to generate tones on<br>receipt of Warned, Lock-<br>On,<br>CW, FCR type of emitters.                                                                                                                                  |
| 2   | Configuration      | /home/ShaktiSCD/<br>ShaktiSCD-1.4.5    | This directory stores Shakti<br>system configuration file.                                                                                                                                                                                                                                                |
| 3   | Database<br>backup | /home/ShaktiSCD/<br>ShaktiSCD-1.4.5    | This<br>directory<br>stores<br>Shakti<br>system database backup files.                                                                                                                                                                                                                                    |
| 4   | Elint<br>returns   | /home/ShaktiSCD/<br>ShaktiSCD-1.4.5    | This directory contains ELINT<br>returns files. ELINT returns file<br>contains intercepted emitters<br>that are added by operator<br>during mission in online mode.                                                                                                                                       |
| 5   | Emitter<br>library | /home/ShaktiSCD/<br>ShaktiSCD-1.4.5    | This directory contains the ES<br>library files.                                                                                                                                                                                                                                                          |
| 6   | Ewossformat        | /home/ShaktiSCD/<br>ShaktiSCD-1.4.5    | This directory contains emitter<br>libraries in the form of sanchay<br>format files.                                                                                                                                                                                                                      |
| 7   | Help               | /home/ShaktiSCD/<br>ShaktiSCD-1.4.5/   | This directory contains three<br>subdirectories i.e. login, offline<br>& Shakti_online.<br>(a)<br>The login subdirectory<br>stores the login help files.<br>(b)<br>The offline stores the<br>offline related help files.<br>(c)<br>Shakti_online<br>subdirectory stores the online<br>related help files. |
| 8   | Map                | /home/ShaktiSCD/<br>ShaktiSCD-1.4.5    | This directory contains all tiff<br>map related files.                                                                                                                                                                                                                                                    |
| 9   | Recording          | /home/ShaktiSCD/                       | The<br>directory<br>contains<br>all                                                                                                                                                                                                                                                                       |

SHAKTI : UHB\Ch5 Page 148 of 614

| Ser | Directory                   | Directory                           | Purpose of Directory                                                                                 |
|-----|-----------------------------|-------------------------------------|------------------------------------------------------------------------------------------------------|
|     |                             | ShaktiSCD-1.4.5                     | recorded files.                                                                                      |
| 10  | Print                       | /home/ShaktiSCD/<br>ShaktiSCD-1.4.5 | The directory contains operator<br>saved copy of printout pdf files.                                 |
| 11  | RFPS<br>files               | /home/ShaktiSCD/<br>ShaktiSCD-1.4.5 | The<br>directory<br>contains<br>exported/ imported RFPS<br>files<br>from RFPS subsystem.             |
| 12  | Screenshots                 | /home/ShaktiSCD/<br>ShaktiSCD-1.4.5 | This<br>directory<br>contains<br>all<br>image files of<br>the screen shots<br>taken by the operator. |
| 13  | Simulation                  | /home/ShaktiSCD/<br>ShaktiSCD-1.4.5 | The<br>directory<br>contains<br>user<br>generated simulated data files.                              |
| 14  | Simulation<br>configuration | /home/ShaktiSCD/<br>ShaktiSCD-1.4.5 | The<br>directory<br>contains<br>simulated<br>sub-system<br>configuration files.                      |
| 15  | Style<br>sheet              | /home/ShaktiSCD/<br>ShaktiSCD-1.4.5 | This<br>directory<br>contains<br>GUI<br>controls<br>colour<br>and<br>font<br>information.            |

- **5.1.3 System Controller & Display Interfaces**.The interface details of the system controller with other subsystems are as shown in **Figure 5.1**.
  - (a) **ES Processor**.The ES Processor subsystem is connected through an Ethernet switch to exchange data from ES for system operation. System controller configures & control receiver Front Ends through ESM processor.
  - (b) **EA Processor**.The EA Processor subsystem is connected through an Ethernet switch to exchange data from EA for system operation. System controller command & control the EA sub-system for jamming operations through user initiated commands.
  - (c) **RFPS**.The RFPS system is connected to the System Controller through Ethernet switch in the SCD Processor chassis in the operator's console.
  - (d) **ESI**.The ESI sub system is interfaced with the System Controller through Ethernet switch. System controller receives platform latitude, longitude and Gyro information from ESI.

SHAKTI : UHB\Ch5 Page 149 of 614

- (e) **CMS**.This system on the ship is interfaced to Shakti system through Ethernet/HDLC.
- (f) **C link**.SCD in 'Integrated' Mode of operation, CMS operator to take control of Shakti EW system and performs EW operations from CMS console.
- (g) **ESI**. The ESI sub system is interfaced with the System Controller through Ethernet switch.
- (h) **FDL**.This system on the ship is interfaced to Shakti system through Ethernet switch to exchange Shakti EW system related files between FDL computer & SCD/ RFPS computer. FDL application software shall support the 'Offline Mode' functionalities of Shakti SCD system such as Replay and Simulation.
- (j) **LRSAM**. This system is platform dependent. SCD will be interfaced with LRSAM system through Ethernet for transmitting ESM track data, Shakti operational status data to LRSAM system.
- (k) **KAVACH**. This system is platform dependent. SCD will be interfaced with KAVACH system through Ethernet for transmitting ESM track data, Shakti operational status data to KAVACH system.

**Table: 5.2 Sub System Interfaces and Its Protocols**

| Ser | Interface             | Protocol                             |
|-----|-----------------------|--------------------------------------|
| 1   | SCD –<br>ES Processor | TCP/IP                               |
| 2   | SCD –<br>EA Processor | TCP/IP                               |
| 3   | SCD –<br>RFPS         | TCP/IP                               |
| 4   | SCD –<br>ESI          | TCP/IP, UDP/IP ( Unicast, Broadcast) |
| 5   | SCD –<br>CMS          | SCD-CMS-TCP/IP or HDLC*              |
| 6   | SCD – FDL             | TCP/IP. FTP                          |
| 7   | FDL - RFPS            | TCP/IP. FTP                          |
| 8   | SCD -<br>LRSAM        | TCP/IP                               |
| 9   | SCD -<br>KAVACH       | TCP/IP                               |

SHAKTI : UHB\Ch5 Page 150 of 614

![](_page_154_Figure_1.jpeg)

**Figure 5.1: SCD Sub System Interface Diagram**

- **5.1.4 Software Development Environment**.The software development environment for Shakti system controller and display is as follows.
  - (a) Operating System: Red Hat Enterprise Linux (RHEL) version 7.2
  - (b) Development Framework &Programming Languages: Qt 4.8.7 in C++.
- **5.1.5 Target Hardware**.Shakti SCD will be a software intensive system. It is a VME based Single Board Computer (SBC) having the following key specifications/ features:

(a) Processor : Intel 4th Generation i7 Quad Core.

(b) RAM : 16GB.

(c) Onboard Flash Disk : 32GB.

(d) Hard disk drive : 1 TB.

(e) Form Factor : 6U.

(f) Ethernet : 4 Gigabit Ethernet ports.

SHAKTI : UHB\Ch5 Page 151 of 614

(g) Audio : High Definition Audio.

(h) Graphics & Video : 1600x1200 resolution graphics card.

5.1.5.1 There will be two independent LCD monitors in Shakti Console with minimum of 1600x1200 resolutions, one for SCD system and the other for RFPS. Keyboard with track ball will be shared between the SCD and RFPS systems. The SCD system hardware will be positioned in a 19" Rack (vertical mounting) with independent power supply operating in 230V@ 50Hz.

- **5.2 Precautions and Safety Measures (DOs and Don'ts)**.The following precautions and safety measures are to be ensured while operating the Shakti system.
  - (a) All sub-units of the system are grounded properly.
  - (b) The external interfaces are switched ON before switching ON the system.
  - (c) The system is not operated in harbour in the presence of high power radiating sources.
  - (d) The cable connectors are properly tightened.
  - (e) The cable assemblies are not damaged while removing or inserting the drawers.
  - (f) The correct tools are used for tightening / loosening screws.
  - (g) The torque wrench is used for connecting SMA connectors.
  - (h) The semi rigid cables are not bent.
  - (j) The power supply connectors are not touched when the power is ON.
  - (k) The connectors are not disconnected / connected when the power is ON.
  - (l) The Radome is handled carefully, and is not touched with bare hands and not to be painted.
  - (m) Before switching off the power supply to the console, ensure that the operating system is shutdown properly.
- **5.2.1 High Voltage**.The sign in Figure 5.2 is used to indicate danger where special precautions must be taken. This sign is used to indicate excess/high voltage, which is beyond the present 'voltage value'. The expected voltage is indicated on the sign.

SHAKTI : UHB\Ch5 Page 152 of 614

![](_page_156_Picture_1.jpeg)

**Figure-5.2: Safety Sign for High Voltage**

**5.2.2 Antenna Movement**.The ESM antenna of the Shakti system is stationary and does not move.

![](_page_156_Picture_4.jpeg)

**Figure-5.2a: Safety Sign for Antenna.**

**5.2.3 Cleaning Solvents**.Certain cleaning agents and solvents are hazardous to the health, if they are not used under the right conditions. Pay careful attention to the following information as shown in Figure 5.3 when handling these items.

> **PERSONNEL SHOULD PAY ATTENTION TO SAFETY DURING HANDLING OR CLEANING AGENTS, ADHESIVES, SOLVENTS, SEALING AGENTS, LOCKING AGENTS, HUMISEAL 1B31, BERYLLIUM OXIDE AND TEFLON.**

**Figure 5.3: Caution**

#### **5.2.4 Microwave Radiation**.

(a) The Microwaves are electromagnetic oscillations, which have a frequency ranging between 300 MHz and 300 GHz. Some high power devices like, klystrons, magnetrons and TWTs etc, produce dangerous microwaves of high frequency which are harmful to human beings.

SHAKTI : UHB\Ch5 Page 153 of 614

![](_page_157_Picture_1.jpeg)

**Figure-5.3a: Safety sign for Microwave Radiation.**

- (b) The microwaves are used in the following applications:
  - (i) Communication Systems
  - (ii) Detection Systems (radar)
  - (iii) Measuring Equipment
  - (iv) Heating Systems
- **5.2.5 Fire Hazards and Extinguishing**.When a fire starts in a cabinet of the installation, the cabinet must be switched off immediately. The fire must be isolated and extinguished by means of a carbon dioxide extinguisher. It is advised not to fight a fire in a cabinet with a Dry chemical powder (DCP) or water type since electronic circuits and wiring will be severely damaged. To shut off oxygen, the area must be sealed and the electrical officer / HOD are informed as quickly as possible.

#### **5.2.6 Important Notes:**

- **5.2.6.1 Microwave Components**.Microwave Components like Front end receiver (FER) unit, RF Switch, Detector, Low Noise Amplifier needs proper care while replacing. Ensure proper grounding before handling these components.
- **5.2.6.2 Semi-Rigid Cables**.To minimize the loss semi-rigid cables used in AHU, the cables should not be bent excessively. The cables like Video and RF need proper handling, else they get damaged.
- **5.2.6.3 Precautions for EMI**.Always ensure proper grounding of the power supply. There should be no voltage present between neutral and ground before switching ON the system. IC's like CMOS, Processor chips should not be touched with bare hands, to prevent the loss of stored data, EPROM masking should not be removed.

SHAKTI : UHB\Ch5 Page 154 of 614

- **5.2.6.4 Use of Line Filters**. In case of failures, proper rating of line filters should be ensured before replacing.
- **5.2.6.5 Read Configuration control document**.Before replacing any item/components the technician/user should read the Configuration control document, since the Shakti system contains calibration data.
- **5.2.6.6 EPROMS**.While placing or replacing the EPROMS, proper polarity should be ensured.

#### **5.2.7 Safety Warnings**.

## **SAFETY WARNING**

The voltage employed in this equipment are sufficiently high to endanger human life**.**

#### **POWER MUST BE SWITCHED OFF**

Before servicing the equipment

**&**

## **GREAT CARE**

must be taken when making internal adjustments etc.

**5.3 Control and Indicator Details**.The controls & indicators located on the front panel of various subsystems and their significance are given in Table 5.3.

**Table: 5.3 Controls & Indicator**

| Ser | Control<br>Switch/LEDs | Description                                                                                              |
|-----|------------------------|----------------------------------------------------------------------------------------------------------|
| 1   | AC Mains ON<br>(LED)   | This indicates the status of A/C supply from Mains.                                                      |
| 2   | ACH (LED)              | This indicates the status of Anti Condensation Heater<br>supply.                                         |
| 3   | 24V (LED)              | This indicates the status of 24V supply from AC-DC<br>converter.                                         |
| 4   | ES ON                  | Press 'ES ON' switch and observe ES Rack-1, ES Rack<br>2 & ESI Health Status indication on console desk. |

SHAKTI : UHB\Ch5 Page 155 of 614

| Ser | Control<br>Switch/LEDs | Description                                                                                                                                    |
|-----|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
|     |                        | Ethernet switch #1 also powered on remotely.                                                                                                   |
| 5   | EA ON                  | Press 'EA ON' switch and observe EA Rack-1, EA Rack<br>2, MMJ AC/DC units, MBJ AC/DC units and CU health<br>status indication on console desk. |
| 6   | SCD ON                 | Press 'SCD ON' switch and observe SCD processor,<br>Monitor1 and Monitor2 are powered ON.                                                      |
| 7   | BATTLE SHOT            | Set the key lock in 'ON' position for routing DC (24V) to<br>EA RACK1 unit.                                                                    |
| 8   | ES STATUS              | This indicates the status of ES processor health status.                                                                                       |
| 9   | EA STATUS              | This indicates the status of EA processor health status.                                                                                       |
| 10  | JAM INIT               | Press 'JAM INIT' switch and observe that the internal<br>LED of the switch glows and the control voltage (24VDC)<br>is routed to jammer Unit.  |
| 11  | ES RESET               | Press 'ES RESET' button and observe ES and its LRUs<br>are powered on once again.                                                              |
| 12  | EA RESET               | Press 'EA RESET' button and observe EA and its LRUs<br>are powered on once again.                                                              |

**5.4 Setting Instructions**.The detailed setting instructions for the Shakti equipment are covered in installation specification manual separately. The details include installation procedures, preparation of EW cables, and cabinet fixation including foundation diagrams and setting to work. The installation manual also includes the different tools to be used for fixing the cabinets, the limitations on the location and position of each cabinet / drawer / unit. The configuration diagram is also provided as part of installation specification manual.

#### **5.5 Sequence of Operation:**

- **5.5.1 System Power On**.This section describes the procedure for switching on the Shakti system and its sub system health status indications that appear on console are displayed during the system power ON.
  - (a) Ensure that all the Racks are kept in the remote operate mode and the MCBs of all the Racks & UPS are switched ON from respective PDPs and ensure that the selection switch at the rear panel of the SCD Rack is in UPS mode. Incase UPS is

SHAKTI : UHB\Ch5 Page 156 of 614

not used keep the switch in PDP mode.

- (b) Switch ON MCB on the side of the console desk and observe that '**Mains ON**' **LED** on console desk indication panel is glowing indicating availability of mains supply to the Rack and also observe that **24V LED** is glowing.
- (c) Press "SCD ON" and observe the following:
  - (i) SCD on switch LED is glowing.
  - (ii) Monitor- 1 &Monitor-2 are powered ON.
  - (iii) SCD Processor is powered ON.
  - (iv) Ethernet SW-2 & SW-3 are powered ON.
- (d) To switch ON ES Rack press 'ES ON' switch on the console desk and observe the switch indication is glowing and ES Rack-1, ES Rack-2, ES1 &Ethernet switch-1 is powered ON. Observe ES Rack-1, ES Rack-2 & ESI Health Status indication console desk.
- (e) To switch ON EA Press 'EA ON' switch and observe that switch LED glows and EA Rack-1, EA Rack-2, MMJ AC/DC units, MBJ AC/DC units and LRU are powered ON and the respective power ON indication LEDs glows one after another.
- (f) After SCD powered ON, we can individually Power on the ES and EA subunits.
- (g) Press "ESM ON" switch and observe that the internal LED of the switch glows and the control voltage (24VDC) is routed to ES Rack-1 and ESI Unit. The ES Rack-1, AHU-On and ESI On will glow after the respective units get powered on and the health of the units is received in the SCD rack.
- (h) Press "ECM ON" switch and observe that the internal LED of the switch glows and the control voltage (24VDC) is routed to EA Rack-1, HEU(P), and HEU(STBD). The EA Rack-1, HEU(P), and HEU(STBD) will glow after the respective units get powered ON and the health of the units is received in the SCD rack.
- (j) After the ECM has been powered on, the jammer unit can be switched ON.
- (k) Press "Jammer Init" switch and observe that the internal LED of the switch glows and the control voltage (24VDC) is routed to jammer Unit.

SHAKTI : UHB\Ch5 Page 157 of 614

(l) Now 'Shakti EW System - SCD' application will start automatically and User Authentication screen will be displayed as shown in **Figure 5.4**. The operator has to enter 'User Name' and 'Password' to login into the application as shown in **Figure 5.5**. Simultaneously, RFPS Display Application will start automatically and its login details will be taken from SCD.

![](_page_161_Picture_2.jpeg)

**Figure-5.4: Shakti Start-up Window**

(m) User shall enter user name and password. System authenticates the user name and password. Both user name and password are case sensitive.

![](_page_161_Picture_5.jpeg)

**Figure-5.5: Login Window**

(n) After successfully logged into the Shakti SCD application, "Mode & Configuration

SHAKTI : UHB\Ch5 Page 158 of 614

Selection" dialog will be displayed (**Figure 5.6**). Click 'Go online' button to enter into the online mode, and the system is ready to interact with sub systems. In online mode, external emissions will be received and displayed on the GUI's.

(p) To switch over controls of keyboard and track ball from SCD Display to the RFPS Display, press 'Middle' button (placed above the track ball) and vice versa to switch back.

#### **5.5.2 System Power Off:**

- (a) Close the RFPS Display application by pressing close button '**X'**. This is located on the right side of the RFPS Display application.
- (b) To shut down the RFPS display computer, go to "Kick off Application Launcher → Leave" and press "Shutdown" button.
- (c) Close the Shakti EW display application by pressing 'Logout' button from System menu. If successfully logged out, 'User Authentication' GUI will be displayed. To shut down the SCD click on 'Power off SCD' button. This is located on the right side of the tool bar window on 'User Authentication' GUI.
- (d) Press "Jammer Init" switch to cut off the 24V to Jammer Unit.
- (e) On console desk, press 'EA ON' switch to power off the EA and its sub systems.
- (f) On console desk press 'ES ON' switch to power off the ES and its sub systems including Ethernet switch #1 also.
- (g) On console desk press 'SCD ON' switch to power off the console.
- (h) Switch off the MCB on the side of the console desk.
- (j) Switch off the MCBs of all the Racks from respective PDPs.
- (k) Switch OFF the ACH.

SHAKTI : UHB\Ch5 Page 159 of 614

![](_page_163_Figure_1.jpeg)

**Figure-5.6: Mode & Configuration Selection Dialog**

**5.5.3 States and Modes of SCD Software Application**.Operation wise, the SCD system shall be controlled in either standalone mode or integrated mode as shown in Figure 5.7.

![](_page_163_Figure_4.jpeg)

**Figure-5.7: Required States and Modes of SCD System**

SHAKTI : UHB\Ch5 Page 160 of 614

- **5.5.3.1 Offline Mode**.In 'Offline' mode, Shakti EW system will not be open to EW environment hence no emitter data shall be received and presented on display at SCD. In this mode, system readiness related operations shall be supported. In start-up of SCD application, 'Offline' mode option shall be presented. When selected, this mode shall present a GUI for carrying out 'Offline' mode activities such as:
  - (a) Replay.
  - (b) Simulation.
  - (c) Emitter Library Management.
  - (d) User Management.
  - (e) System Configuration.
  - (f) Application File Management.
- **5.5.3.2 Online Mode**.In 'Online' mode, the SCD system will be connected other subsystems of the EW system through Ethernet on Shakti LAN. SCD system will perform health checks with all the sub-systems connected to it after establishing the connection. SCD system will declare the link status of a sub-system as 'Down' if data is not received from it within 'Link-Down Timeout' defined in the application. The link status between SCD system & the sub-systems will be displayed and updated in application main window.
- 5.5.3.2.1 SCD system will initiate data recording, Auto BITE & application related logs in this mode. SCD application will start with default system configuration, if no other configuration is selected by the user at start of the application. Configuration related commands will be sent to a sub-system (if not default configuration) as part of 'Start-up Sequence'. The data received from ES Processor will be presented in different formats on the display.
- 5.5.3.2.2 In this mode, Shakti EW system will be open to EW environment and the spectral activity captured by the receivers will be sent to ES Processor in the form of Pulse Descriptor Words (PDWs). ES Processor will de-interleave PDWs and form emitter track files which will be sent to SCD system for presentation on display to the user. The intercepted emitters will be matched with a pre-loaded emitter library and the emitter identity will be displayed to user. Jamming commands will be issued automatically by ES Processor for Warned & Lock-On type of emitters and manually from SCD console by the user for other types of emitters. In this mode, user will be able to designate an emitter for detailed inter & intra pulse parameter analysis using RFPS and the results of the same activity will be displayed to user. In this mode, the Shakti EW system will be accessible

SHAKTI : UHB\Ch5 Page 161 of 614

remotely by CMS for carrying out EW operations from there.

- 5.5.3.2.3 Shakti EW System will be command & controlled in 'Standalone' or 'Integrated' mode. By default, it will be operated in 'Standalone' mode.
- 5.5.3.2.4 Shakti system will be interfaced with LRSAM and KAVACH depending on platform on which they are equipped. ESM track data, EW system health and operational status will be sent to those systems periodically at every 1 second.
- **5.5.3.3 Standalone Mode**.In 'Standalone' mode of SCD system operation, command & controlling of complete Shakti EW system shall be carried out through user initiated commands from Shakti Console. Local (Shakti Console) user shall have complete control over the EW system. By default, on power-on, the SCD system shall be functioning in this mode. The application shall switch to Integrated Mode on command from CMS.
- **5.5.3.4 Integrated Mode (CMS Controlled)**.In 'Integrated' mode, CMS user (CMS Console) shall take control of Shakti EW system in conjunction with the EW system user. Initially, Shakti EW system shall be in 'Standalone' mode of operation. It shall be put into 'Integrated' mode by CMS user after establishing connection with SCD system. While in 'Integrated' mode of operation, CMS user alone can put Shakti EW system back into 'Standalone' mode. However, Shakti EW system user shall have the facility to send a request (through application command) to CMS to put Shakti EW system back into 'Standalone' mode.
- **5.5.4 HMI Requirement Description**.Emphasis of Shakti SCD HMI will be to reduce load on the user and to enable him/her to react to fast changing EW scenario. Analyzed data from ES processor along with the results of identity search performed in 'warner emitter library' will be presented in graphical and alphanumeric formats on the display. The emitter for which the match is not found in the 'warner emitter library' will be searched in priority & non-priority library in SCD application.
  - (a) Judicious colours will be associated with the tactical data to draw immediate attention of the user in dense EW environment.
  - (b) Shakti SCD application will be based on a main window with menu bar with drop-down menus, tool bar and status bar. The SCD application shall start on system power on.
  - (c) HMI requirements of Shakti SCD system are categorized into three groups, for ease of understanding and better appreciation, as mentioned below:
    - (i) User Authentication (Login) GUIs.

SHAKTI : UHB\Ch5 Page 162 of 614

- (ii) Offline Mode GUIs.
- (iii) SCD Main Window GUIs.
- (iv) Replay Mode GUIs.
- (v) Simulation Mode GUIs.
- (d) These GUIs and their HMI requirements are described in the following sections.
- (e) The GUIs presented in this HMI document are provisional and have been designed using Qt (4.8.7) framework under RHEL (7.2) Operating System to meet the GUI functional requirements of Shakti SCD system. NTDS symbology & color scheme is used for emitter data presentation in all the relevant GUIs.
- (f) All the values in data fields shown in all the GUIs are simulated and some of the values may not be correct for interpretation.
- (g) The layout of HMI of 'SCD Main Window' of the SCD application is shown in **Figure 5.8**.

![](_page_166_Figure_9.jpeg)

**Figure-5.8: HMI of Layout of Shakti SCD Main Window**

**5.5.4.1 User Authentication (Login) GUIS**.The underlying operating system, after completion of booting process, shall be configured to start SCD application automatically in full screen mode. Operating system related applications/ tools shall not be visible to user when SCD application is executing. By default, 'login' GUI shall be displayed immediately

SHAKTI : UHB\Ch5 Page 163 of 614

after starting SCD application. The following sections describe 'user authentication' related GUIs and their HMI requirements.

- **5.5.4.1.1 Register Administrator**.If SCD application is executed for the very first time or if there are no user account details present in SCD computer then this GUI (as shown in Figure 5.9) shall be displayed to user for creating the first user (administrator) of the application. The administrator shall be the super user with access to all the commands including modifying EW system configuration parameters.
- 5.5.4.1.1.1 The user name shall be maximum of 15 characters and minimum of 5 characters in length. It shall be case sensitive and can be a combination of alpha-numeric characters. Password shall be maximum of 15 characters and minimum of 5 characters in length. It shall be case sensitive and can be a combination of alpha, numeric and special characters.

![](_page_167_Picture_4.jpeg)

**Figure-5.9: Administrator Registration GUI**

- 5.5.4.1.1.2 User shall enter input for 'Username', 'Password' and 'Answer for Security Question' after selecting a security question. Security question will be helpful in recovering a forgotten password. By default, 'User Type' option will be selected as 'Administrator'. User shall click on 'Add Administrator' option to create the user account in SCD application. If successful, 'User Authentication' GUI (described in the flowing section) shall be displayed to user to login into SCD application using that account information.
- 5.5.4.1.1.3 User shall click on 'Shutdown SCD' option to close this GUI and shutdown (power off) SCD computer.
- **5.5.4.1.2 Authenticate User**.After successful installation of SCD application and the creation of 'Administrator' type of user, 'User Authentication' GUI (as shown in Figure 5.10) shall be displayed to user for logging into SCD Application. On The GUI To Recover Forgotten Password Facility Has Provided to The User And Option To Shutdown SCD

SHAKTI : UHB\Ch5 Page 164 of 614

Computer.

![](_page_168_Figure_2.jpeg)

**Figure-5.10: User authentication GUI**

- (a) User shall enter the 'User Name' & 'Password' (which were entered during user registration) and click on 'Login' option. SCD application shall proceed with next stage of GUI for carrying out EW operations if user authentication is successful.
- (b) User shall click on 'Power OFF SCD/ Restart SCD' option to close this GUI and shutdown (power off)/ restart SCD computer (SBC).
- (c) User shall click on 'Help' option to see 'User Authentication' GUI related help document.
- **5.5.4.1.3 Mode & Configuration Selection**.On successful User Login, SCD application shall display 'Mode & Configuration Selection' GUI as shown in Figure 5.11 for selecting Shakti SCD Mode & EW system configuration (stored in a file).
  - (a) User shall select 'Online Mode/ Offline Mode' option for 'Online/ Offline Mode' of operation of SCD application and display their respective GUIs.
  - (b) User shall select 'Default' option to select default (factory level) configuration parameters for the sub-systems of Shakti EW system before going to 'Online/ Offline' mode of operation.
  - (c) User shall select 'Recent' option to select last logout (from 'Online' mode) configuration parameters for the sub-systems of Shakti EW system before going to 'Online/ Offline' mode of operation.

SHAKTI : UHB\Ch5 Page 165 of 614

![](_page_169_Figure_1.jpeg)

**Figure-5.11: Mode & Configuration Selection GUI**

- (d) User shall select 'Saved' option to select a previously saved configuration file & apply those settings on the sub-systems of Shakti EW system before going to 'Online/ Offline' mode of operation.
- (e) User shall click on 'Go Online' option to start SCD application in 'Online' mode with selected configuration and display 'SCD Main Window' GUI.
- (f) User shall click on 'Go Offline' option to start SCD application in 'Offline' mode with selected configuration and display 'Offline Mode' GUI.
- (g) User shall click on 'Logout' option to exit from this GUI and go to 'User Authentication' GUI for logging again.
- **5.5.4.2 Offline Mode GUIs**.Shakti SCD application shall display 'Offline Mode' GUI as shown in Figure 5.12, to perform 'Offline' mode related activities are as follows.
  - (a) Replay
  - (b) Simulation
  - (c) Emitter Library Management

SHAKTI : UHB\Ch5 Page 166 of 614

- (d) User Management
- (e) System Configuration
- (f) Application File Management
- 5.5.4.2.a The options on the GUI, if selected, shall display corresponding GUI for the operations mentioned above. For example, if user clicks on 'Replay' option, 'Replay' GUI shall be displayed. User shall click on 'Go Online' option to start SCD application in 'Online' mode with selected configuration and display 'SCD Main Window' GUI.

![](_page_170_Picture_5.jpeg)

**Figure 5.12: Offline Mode GUI**

- 5.5.4.2.b Following section describes 'Offline' mode related GUIs and their HMI features.
- **5.5.4.2.1 Replay**.Replay GUI, as shown in Figure 5.13, shall facilitate the user to replay an existing recorded file(already recorded scenarios/ missions) and view the events/ data on SCD application in 'replay mode'.
  - (a) User shall click on 'Replay' option in 'Offline Mode' GUI to active this GUI.
  - (b) User shall select a recording file from the list of files on the GUI and click on 'Load Selected File' option to load into SCD application. Alternately, user shall double click on a file to load it.
  - (c) User shall click on 'Start Replay' option to go to SCD Main Window in 'Replay' mode.

SHAKTI : UHB\Ch5 Page 167 of 614

![](_page_171_Figure_1.jpeg)

**Figure-5.13: Replay GUI**

SHAKTI : UHB\Ch5 Page 168 of 614

- (d) User can select 'Speed Level', 'Start Time' or 'End Time' before start of replay.
- (e) 'Close' option shall be clicked to close 'Replay' GUI and return to 'Offline' mode GUI.
- (f) User shall click on 'Start EWOSS Conversion' option to convert the selected recording file to EWOSS (Sanchay-II) format. The status of conversion process shall be displayed, as shown in **Figure 5.14**. This conversion process can be stopped, in the middle, by clicking on 'Cancel' option.

![](_page_172_Picture_4.jpeg)

**Figure 5.14: EWOSS conversion process status GUI in Replay-Offline mode**

- **5.5.4.2.2 Simulation**.Simulation GUI, as shown in Figure 5.15, shall facilitate the user carry out EW operations on simulated data in SCD application. This is required for the user to get acquainted with SCD application.
- 5.5.4.2.2.1 Simulation mode of operation shall facilitate the user to perform EW operations on simulated data and view the results for those operations on SCD Main Window. Provision has made on the GUI to generate EW data (track data) related to ESM, ECM & RFPS, as per user requirement. Provision on the GUI to save user generated/ selected simulation data & settings into a file.

SHAKTI : UHB\Ch5 Page 169 of 614

![](_page_173_Figure_1.jpeg)

**Figure-5.15: Simulation GUI in Offline Mode**.

SHAKTI : UHB\Ch5 Page 170 of 614

- (a) User shall click on 'Simulation' option in 'Offline Mode' GUI to activate this GUI.
- (b) User shall select a simulation file from the list of files on the GUI and click on 'Show' option to load simulation data on to the GUI. Alternately, user shall double click on a file to load it. Simulation file is pre-defined file containing randomly simulated emitters.
- (c) User shall check 'ES Processor', 'EA Processor' or 'RFPS' options to simulate their track data & controls in SCD Main Window.
- (d) User shall click on 'Start' option to go to SCD Main Window in 'Simulation' mode.
- (e) User shall click on 'Close Simulation' option to close this GUI and go to 'Offline Mode' GUI.
- (f) SCD application will start in Simulation mode and simulated track parameters will be displayed in the main window GUI. In Simulation mode, the HMI will remain same as 'Online' mode GUI's except that the emissions are not the actual emissions from environment but are simulated with random emitter parameters.
- **5.5.4.2.3 Emitter Library Management**.Emitter Library Management GUI, as shown in **Figure 5.16**, shall facilitate the user to manage (add/ modify/ delete/ view) emitter library records of SCD application. Emitter library will be provided by EWOSC (Navy). Modification of this library on the platform is not suggested. However if it is inevitable and necessary to add new entries to this library, there should be space available in it, i.e. all the 20000 entries should not be filled. If the no. of entries is less than 20000, then Operator can add new entries to the library provided by EWOSC (Navy) otherwise Operator has to delete some existing entries (which are not so important) and make new entries. In SCD application, options are provided to Operator to delete/modify/existing entries in Emitter library, but it is not suggested to exercise these operations using SCD on the platform.

SHAKTI : UHB\Ch5 Page 171 of 614

![](_page_175_Figure_1.jpeg)

**Figure-5.16: Emitter Library Management GUI**

SHAKTI : UHB\Ch5 Page 172 of 614

- (a) User shall select an emitter library file from the list of files on the GUI and click on 'Show' option to load emitter records data on to the GUI. Alternately, user shall double click on a file to load it.
- (b) Shakti emitter library consists of 20000 records (emitters) of which 500 will be of Warner type and rest of the records will be of Priority & Non-Priority type. Warner entries will be numbered from 1-500. Priority records will be from 501-12000 and Non-Priority will be numbered from 12001-20000.
- (c) User shall select required search options (such as type of records (Warner/ Priority/ Non-Priority), record number etc.) and click on 'Show Records' option to display emitter records (matching the search criteria) in table on the GUI.
- (d) User shall click on 'Close' option to exit from this GUI and go to 'Offline' mode GUI.
- (e) The following sections describe the GUIs required for viewing/ modifying an emitter library.
- **5.5.4.2.3.1 Add Emitter Record**: User shall click on 'Add Record' option from 'Emitter Library Management' GUI. A separate GUI, as shown in Figure 5.17, shall be displayed to user.
  - (a) User shall provide all input parameters and click on 'Add Record' button; entered record details are added in the selected emitter library file. After record addition, 'Record added successfully' message will be displayed.
  - (b) An emitter record consists of the following parameters: "Library Record Parameters: Record Number, Record Type (Warner, Priority, Non-Priority), Radar Name, Emitter Type (Known, Hostile, Unknown), Radar ID Confidence, Radar Mode, Central Library Record Number, Frequency Attributes, Pulse Details, Scan Type, Platform, Symbol, ASP, Threat Amplitude, Threat Level, JPRO Number etc."
  - (c) User shall click on 'Close' option to exit from this GUI and go to 'Emitter Library Management' GUI.

SHAKTI : UHB\Ch5 Page 173 of 614

![](_page_177_Picture_1.jpeg)

**Figure-5.17: Add Record GUI – Emitter Library Management**.

**5.5.4.2.3.2 Modify Emitter Record:** User shall select a record from the table in the GUI and click on 'Modify Record' option from 'Emitter Library Management' GUI. A separate GUI, as shown in **Figure 5.18**, shall be displayed to user.

SHAKTI : UHB\Ch5 Page 174 of 614

![](_page_178_Picture_1.jpeg)

**Figure-5.18: Modify Record GUI**

- (a) User shall modify required parameters and click on 'Modify Record' option on GUI to update record to the selected emitter library file. After record addition, 'Record updated successfully' message shall be displayed.
- (b) User shall click on 'Close' option to exit from this GUI and go to 'Emitter Library Management' GUI.
- **5.5.4.2.3.3 Delete Emitter Record**.User shall select a record from the table in the GUI and click on 'delete record' option from 'emitter library management' GUI. A confirmation GUI, as shown in Figure 5.19, shall be displayed to user before deleting it.

![](_page_178_Picture_6.jpeg)

**Figure-5.19: Delete Record Confirmation GUI.**

SHAKTI : UHB\Ch5 Page 175 of 614

**5.5.4.2.3.4 Delete All Emitter Records**.User shall click on 'delete all' in 'emitter library management' GUI to delete all the records of the selected emitter library file. A confirmation GUI, as shown in Figure 5.20, shall be displayed to user before deleting all records.

![](_page_179_Picture_2.jpeg)

**Figure 5.20: Delete All Records Confirmation GUI.**

**5.5.4.2.3.5 View Emitter Record**.User shall select a record from the table in the GUI and click on 'view record' option from 'Emitter Library Management' GUI. A separate GUI, as shown in Figure 5.21, shall be displayed to user.

![](_page_179_Picture_5.jpeg)

**Figure-5.21: View Record GUI.**

(a) User can traverse through the records of the emitter library by click on

SHAKTI : UHB\Ch5 Page 176 of 614

'Previous Record' or 'Next Record'.

- (b) User shall click on 'Close' option to exit from this GUI and go to 'Emitter Library Management' GUI.
- **5.5.4.2.3.6 Save Changes in Emitter Library**.Any modifications made to the selected emitter library shall be saved if user clicks on 'save changes' option on the GUI. A confirmation GUI, as shown in Figure 5.22, shall be displayed to user.

![](_page_180_Picture_4.jpeg)

**Figure-5.22: Save Changes Confirmation GUI**.

**5.5.4.2.3.7 Save Emitter Library To Another File**.User can save the selected emitter library (with modifications, if any) to another file on SCD storage by clicking on 'Save to Another File' option on the GUI. A confirmation GUI, as shown in Figure 5.23, shall be displayed to user. A file selection GUI shall be displayed to user for entering file name & user shall click on 'Save' option to save.

![](_page_180_Picture_7.jpeg)

**Figure-5.23: Save to Another File Confirmation GUI**.

**5.5.4.2.3.8 Save Selected Records to File**.There is an option to save the records (even filtered records) that are displayed in the table on 'Emitter Library Management' GUI. This option will be useful to save only selected records. User shall right click on the table in the GUI and click on 'save these records to a file' option. A confirmation GUI, as shown in Figure 5.24, shall be displayed to user.

SHAKTI : UHB\Ch5 Page 177 of 614

![](_page_181_Figure_1.jpeg)

**Figure-5.24: GUI to Save Selected Records to File**

**5.5.4.2.3.9 Print - Emitter Library Records**.User shall click on 'Print' option on 'Emitter Library Management' GUI. A separate GUI, as shown in Figure 5.25, shall be displayed. On this GUI, user shall select 'Printer Name', 'properties', 'options' etc., and click on 'print' option to take print out on network printer. User shall click on 'cancel' option to exit from this GUI and go to 'Emitter Library Management' GUI.

![](_page_181_Picture_4.jpeg)

**Figure-5.25 : Print Records GUI**.

**5.5.4.2.3.10 Print Preview - Emitter Library Records**.User shall click on 'print preview' option on 'emitter library management' GUI. A separate GUI, as shown in Figure 5.26,

SHAKTI : UHB\Ch5 Page 178 of 614

shall be displayed with a print preview of selected emitter library file. User shall click on 'print' icon on this GUI to take print out on network printer. Note: only user selected emitter parameters will be displayed in print preview. User shall click on 'exit' icon on this o close print preview and go to 'emitter library management' GUI.

SHAKTI : UHB\Ch5 Page 179 of 614

![](_page_183_Picture_1.jpeg)

**Figure-5.26: Print Preview GUI.**

SHAKTI : UHB\Ch5 Page 180 of 614

**5.5.4.2.4 User Management**. User management GUI, as shown in **Figure 5.27**, shall facilitate the user manage (add/ modify/ delete/ view) user accounts of SCD application. User shall click on 'user management' option in 'offline mode' GUI to active this GUI. The following table lists out the user types and their access rights in SCD application.

![](_page_184_Picture_2.jpeg)

**Figure-5.27: User Management GUI**.

**Table: 5.4 User Types & Access Rights of SCD Application**

| User Type     | Operations Allowed in SCD Application                        |  |
|---------------|--------------------------------------------------------------|--|
|               | All EW operations including:                                 |  |
|               | (a)<br>Modification to Application Configuration in 'Offline |  |
| Administrator | Mode',                                                       |  |
|               | (b)<br>Maintenance Operations.                               |  |
|               | All EW operations except:                                    |  |
|               | (a)<br>Modification to Application Configuration in 'Offline |  |
| Commander     | Mode'.                                                       |  |
|               | (b)<br>Maintenance Operations.                               |  |
| Operator      | All EW operations except:                                    |  |

SHAKTI : UHB\Ch5 Page 181 of 614

| User Type | Operations Allowed in SCD Application                         |  |  |
|-----------|---------------------------------------------------------------|--|--|
|           | (a)<br>Modification to Application Configuration in 'Offline  |  |  |
|           | Mode'.                                                        |  |  |
|           | (b)<br>Maintenance Operations.                                |  |  |
|           | (c)<br>Any other restrictions enforced by 'Administrator/     |  |  |
|           | Commander' type of user, with 'Restrict Access Rights' option |  |  |
|           | after logging into SCD application.                           |  |  |

- (a) By default, list of active existing users shall be displayed on the GUI. User shall click on 'Close' option to exit from this GUI and go to 'Offline' mode GUI.
- (b) The following sections describe the GUIs required for user management.
- **5.5.4.2.4.1 Add User**.User shall click on 'add user' option from 'user management' GUI. A separate GUI, as shown in Figure 5.28, shall be displayed to user..

![](_page_185_Picture_5.jpeg)

**Figure-5.28: Add User GUI**

- (a) User shall enter 'User Name', 'Password', select 'User Type', 'Security Question' & 'Answer for Security Question' and click on 'Add User' option on this GUI. If successful, 'User added successfully' message shall be displayed.
- (b) User name shall be maximum of 15 characters and minimum of 5 characters in length. It shall be case sensitive and combination of alpha-numeric characters. Password shall be maximum of 15 characters and minimum of 5 characters in length. It shall be case sensitive and can be a combination of alpha, numeric & special characters.
- (c) User shall click on 'Close' option on this GUI to exit from here and go to 'User Management' GUI.

SHAKTI : UHB\Ch5 Page 182 of 614

## **5.5.4.2.4.2 Modify User**.

- (a) User Shall Click On 'Modify User' Option From 'User Management' GUI. A Separate GUI, As Shown In **Figure 5.29**, Shall Be Displayed To User.
- (b) User shall enter 'Password', select 'User Type', 'Security Question' & 'Answer for Security Question' and click on 'Modify User' option on this GUI. If successful, 'User details updated successfully' message shall be displayed.
- (c) User shall click on 'Close' option to exit from this GUI and go to 'User Management' GUI.

![](_page_186_Picture_5.jpeg)

**Figure-5.29: Modify User GUI**.

**5.5.4.2.4.3 Delete User**.User shall click on 'delete user' option from 'user management' GUI. A confirmation GUI, as shown in **Error! Reference source not found.**, shall be displayed to user. If successful, 'user deleted successfully' as shown in Figure 5.31 message shall be displayed to the user.

![](_page_186_Picture_8.jpeg)

**Figure-5.30: Confirmation GUI to Delete User**.

![](_page_186_Picture_10.jpeg)

**Figure-5.31: User deleted successfully confirmation message**.

SHAKTI : UHB\Ch5 Page 183 of 614

**5.5.4.2.4.4 User Login History**.User shall click on 'User Login History' option from 'User Management' GUI. A separate GUI, as shown in **Figure 5.32**, shall be displayed to user.

![](_page_187_Picture_2.jpeg)

**Figure-5.32: User Login History GUI.**

- (a) If user selects a 'User Name', its login history details such as 'User Name', 'Login Date', 'Login Time', 'Logout Date', 'Logout Time' & 'Active Time' shall be displayed on the GUI.
- (b) User shall click on 'Close' option to exit from this GUI and go to 'User Management' GUI.
- **5.5.4.2.4.5 Deleted Users List**. User shall click on 'Deleted Users List' option from 'User Management' GUI. A separate GUI, as shown in **Figure 5.33**, shall be displayed to user with details such as 'Deleted User Name', 'User Type', 'Deletion Date', 'Deletion Time' & 'Deleted By' (Who deleted this user).
- 5.5.4.2.4.5.1 User shall click on 'Close' option to exit from this GUI and go to 'User Management' GUI.

SHAKTI : UHB\Ch5 Page 184 of 614

![](_page_188_Picture_1.jpeg)

**Figure-5.33: Deleted Users List GUI.**

- **5.5.4.2.4.6 Restrict User Access in SCD Application**.User shall select a 'User Name' from 'User Management' GUI and click on 'Restrict User Access' option from. A separate GUI, as shown in **Figure 5.34**, shall be displayed to user.
  - (a) List of operations (activities) of Shakti SCD, along with provision to select/ deselect them, shall be displayed on the GUI.
  - (b) User shall check/ un-check required operations for the selected user and click on 'Apply' option. These changes will be effective when user enters SCD Main Window.
  - (c) User shall click on 'Close' option to exit from this GUI and go to 'User Management' GUI.

SHAKTI : UHB\Ch5 Page 185 of 614

![](_page_189_Picture_1.jpeg)

**Figure-5.34: Restrict User Access GUI.**

**5.5.4.2.5 System Configuration**.System Configuration' GUI, as shown in **Figure 5.35**, shall facilitate the user modify 'Network Settings' of sub-systems in 'Offline' mode. Modification of OEM specific 'Configuration Settings' of sub-systems shall be restricted to only 'Administrator' type of user. User shall click on 'System Configuration' option in 'Offline Mode' GUI to active this GUI.

SHAKTI : UHB\Ch5 Page 186 of 614

![](_page_190_Picture_1.jpeg)

**Figure-5.35: System Configuration GUI.**

SHAKTI : UHB\Ch5 Page 187 of 614

- 5.5.4.2.5.a By default, a list of available system configuration files on SCD storage shall be displayed on the GUI.
- 5.5.4.2.5.b User shall select a configuration file from the list of files on the GUI and click on 'Show' option to load configuration data on to the GUI. Alternately, use shall double click on a file to load it.
- 5.5.4.2.5.c Sub-sections of system configuration shall be displayed as tab GUIs and user shall select a sub-section & modify required configuration parameters.
- 5.5.4.2.5.d User shall click on 'Close' option to close this GUI and go to 'Offline' mode GUI. A confirmation GUI, as shown in **Figure 5.36**, shall be displayed to user with 'Yes, No & Cancel' options. User shall click on 'Yes' option to save any changes to the selected system configuration file & exit from 'System Configuration' GUI and go to 'Offline Mode' GUI. User shall click on 'No' option to discard any changes made in the selected system configuration file & exit from 'System Configuration' GUI and go to 'Offline Mode' GUI. User shall click on 'Cancel' option to remain there in 'System Configuration' GUI, without saving/ discarding any changes.

![](_page_191_Picture_5.jpeg)

**Figure-5.36 : Close Confirmation GUI.**

- 5.5.4.2.5.e The following sections describe system configuration of SCD application:
- (a) **ES Processor Configuration GUI**.By default, this tab GUI shall be displayed when 'System Configuration' GUI is activated.

User can modify network settings (Port, IP address, Connection Retry Interval, Link-Down Declaration Timeout.

(b) **ES Receivers Configuration GUI**.User shall click on 'ES Receivers' tab GUI to view the configuration parameters of ES Receivers.

Only 'Administrator' type of user can modify operation mode & mode parameters of NB Rx1 (0.175-0.5GHz), NB Rx2 (0.5-18GHz) or BB Rx1 (2.2-18GHz).

SHAKTI : UHB\Ch5 Page 188 of 614

- (c) **RFPS Configuration GUI**.User shall click on 'RFPS' tab GUI to view the configuration parameters of RFPS. User can modify network settings (Port, IP address, Connection Retry Interval, Link-Down Declaration Timeout).
- (d) **ESI Configuration GUI**.User shall click on 'ESI' tab GUI to view the configuration parameters of ESI.
- (e) User can modify network settings (Port, IP address, Connection Retry Interval, Link-Down Declaration Timeout).
- (f) **CMS Configuration GUI**.User shall click on 'CMS' tab GUI to view the configuration parameters of CMS. User can modify network settings (Port, IP address, Connection Retry Interval, Link-Down Declaration Timeout).
- (g) **Printer Configuration GUI**.User shall click on 'Printer' tab GUI to view the configuration parameters of Printer.
- (h) **LRSAM Configuration GUI**. User shall click on 'LRSAM' tab GUI to view the configuration parameters of LRSAM. User can modify network settings (Port, IP address, Connection Retry Interval, Link-Down Declaration Timeout).
- (j) **KAVACH Configuration GUI**. User shall click on 'KAVACH' tab GUI to view the configuration parameters of KAVACH. User can modify network settings (Port, IP address, Connection Retry Interval, Link-Down Declaration Timeout).
- (k) **Map Configuration GUI**. User shall click on 'Map' tab GUI to view map related configuration parameters.
  - (i) User shall select 'Default Zoom Level', 'Default Map Mode', 'No. of Points for Latest Path' and 'Show/ Hide' options for 'Spokes', 'Annotations', 'Tactical Picture', 'Way Points'.
  - (ii) User shall click 'Load All Map Files from SCD Storage' option to load all map files into SCD application.
  - (iii) To unload a map from SCD application, user shall click on 'Unload Map File' option.
- (l) **General Configuration GUI**. User shall click on 'General' tab GUI to view application related settings such as:
  - (i) System Recording: Enable/ Disable 'System Recording'.

SHAKTI : UHB\Ch5 Page 189 of 614

- (ii) Logs: Enable/ Disable 'User Activity Log', 'System Error Log', 'User Login History' etc.
- (iii) Library Matching: Enable/ Disable 'Library Matching' in SCD Application in 'Online' Mode, Select an Emitter Library File.
- (iv) Audio Alarm Feature: Enable/ Disable Audio Alarm in SCD Application in 'Online' Mode. Select audio tone file for a particular signal type.
- (v) Database: Update Database (for storing emitter data & SCD application settings) Details.
- (vi) Look & Feel: Select a theme file for SCD application look & feel.
- (m) **SCD SBC Configuration GUI**. User shall click on 'SCD SBC' tab GUI to view the network interface settings SBC. User can modify network settings (IP Addresses) and 'Date Time Correction Threshold' for updating SBC system time.
- **5.5.4.2.5.1 Save Changes in System Configuration**.Any modifications made to the selected system configuration shall be saved if user clicks on 'Save Changes' option on the GUI. A confirmation GUI, as shown in **Figure 5.37**, shall be displayed to user.

![](_page_193_Picture_8.jpeg)

**Figure-5.37: Save Changes Confirmation GUI.**

**5.5.4.2.5.2 Save Configuration to Another File**.User can save the selected system configuration (with modifications, if any) to another file on SCD storage by clicking on 'Save to Another File' option on the GUI. A confirmation GUI, as shown in **Figure 5.38**, shall be displayed to user. A file selection GUI shall be displayed to user for entering file name & user shall click on 'Save' option to save.

SHAKTI : UHB\Ch5 Page 190 of 614

![](_page_194_Picture_1.jpeg)

**Figure-5.38: Save to Another File Confirmation GUI.**

**5.5.4.2.5.3 Set as Current System Configuration**.User shall click on 'Set as Current Configuration' option to save the displayed configuration (selected file) and use this in 'Online' mode when user enters 'Online' mode. A confirmation GUI, as shown in **Figure 5.39**, shall be displayed to user. If user wants to go to 'Online' mode with a particular configuration, then a configuration file must be selected, changes to be made (if any) then click on 'Set as Current Configuration' option.

![](_page_194_Picture_4.jpeg)

**Figure-5.39: Set as Current Configuration Confirmation GUI.**

**5.5.4.2.5.4 Reset to Default System Configuration**.User shall click on 'Reset to Default Configuration' option to erase all the configuration settings of the selected file and reload it with default (factory level) settings. A confirmation GUI, as shown in **Figure 5.40**,

SHAKTI : UHB\Ch5 Page 191 of 614

shall be displayed to user.

![](_page_195_Picture_2.jpeg)

**Figure-5.40: Reset to Default Configuration Confirmation GUI.**

**5.5.4.2.6 File Management**.File Management GUI, as shown in **Figure 5.41**, shall facilitate the user to delete unnecessary files of SCD application from SCD storage. User shall click on 'File Management' option in 'Offline Mode' GUI to active this GUI.

SHAKTI : UHB\Ch5 Page 192 of 614

![](_page_196_Figure_1.jpeg)

**Figure-5.41: File Management GUI.**

SHAKTI : UHB\Ch5 Page 193 of 614

5.5.4.2.6.a Files related to the following shall be allowed for file management:

- (a) System Emitter Library.
- (b) System Configuration.
- (c) Simulation.
- (d) System Recording.
- (e) Login History.
- (f) Error Logs.
- (g) User Activity Log.
- (h) System Messages Log.
- (j) Map.
- (k) Database Backup & Restore.

5.5.4.2.6.b A separate tab GUI shall be provided for accessing/ viewing/ deleting these files. A confirmation message shall be displayed to user before deleting any SCD application file. In each tab GUI, user shall click on 'Delete/ Delete All' option to delete a single file/ all files at once. User shall click on 'Show' option to view the contents of the file before deleting it. There shall be options on the GUI to filter out or browse through the contents a file.

5.5.4.2.6.c User shall click on 'Close' option to exit from this GUI and go to 'Offline' mode GUI.

**5.5.4.2.7 SCD Main Window GUI**. This section describes the SCD Main window GUIs & HMI requirements of SCD application.

5.5.4.2.7.1 SCD Main Window GUIs shall provide options for:

- (a) Online Mode:
  - (i) Exchange message between SCD & other sub-systems of Shakti EW system.
  - (ii) Display & update data (live EW spectral activity, status etc.) received

SHAKTI : UHB\Ch5 Page 194 of 614

from sub-system in different formats.

- (iii) Command & control of complete Shakti EW system.
- (iv) Data recording.
- (b) Replay Mode:
  - (i) Read 'recorded EW scenario' from a recording file on SCD storage.
  - (ii) Display & update system events and user activity from it.
  - (iii) No network connection with sub-systems and hence, no command & controlling of the EW system.
  - (iv) Controls for start/ stop/ pause of replay activity.
  - (v) No data recording.
- (c) Simulation Mode:
  - (i) Read data from a simulation file on SCD storage.
  - (ii) Display & update system events and user activity from it.
  - (iii) Accept & respond to user activity on SCD Main Window.
  - (iv) No network connection with sub-systems and hence, no command & controlling of the EW system.
  - (v) No data recording.
- (d) The space within SCD Main Window shall be categorized and customized into sub-windows as given below:
  - (i) Application Menu Bar & Drop-Down Menus.
  - (ii) EW Activity Window.
  - (iii) EW System Status Window.
  - (iv) Application Tool Bar.
  - (v) Graphics Window (Tactical Display/ Situational Display / Map Display).

SHAKTI : UHB\Ch5 Page 195 of 614

- (vi) Emitter Report Window.
- (vii) Latest Emitters Window.
- (viii) Link Status Window (Initially this window is hidden but after selecting 'show link and self status window' it remains continuously)
- (ix) RFPS Results Window.
- (x) EA Parameters Window.
- (xi) System Messages Window (Initially this window is hidden but after selecting 'show system message window' it remains continuously)
- (xii) Application Status Bar.
- 5.5.4.2.7.2 These same GUIs shall be used in 'Replay' & Simulation Mode with restrictions which will be described in the coming sections.
- 5.5.4.2.7.3 SCD Main Window GUI is shown in **Figure 5.42**.
- 5.5.4.2.7.4 This GUI shall be displayed after successful login into SCD application either in 'Online', 'Replay' or 'Simulation' mode.
- 5.5.4.2.7.5 The following sections describe SCD Main Window related GUIs and their HMI requirements.

SHAKTI : UHB\Ch5 Page 196 of 614

![](_page_200_Figure_1.jpeg)

**Figure-5.42: Main Window Menu Bar**

SHAKTI : UHB\Ch5 Page 197 of 614

**5.5.4.2.8 Application Menu Bar & Drop-Down Menus**.Operational and configuration related functionalities of Shakti EW system shall be distributed among dropdown menus (command menus) in SCD application menu bar. These menus shall present GUI controls to configure & control the system/ sub-systems and view the EW spectral activity data in various display formats (described in the coming sections). Each menu/ menu item shall have short cut keys assigned to it. User shall be able to access the functionality of menu item (without using mouse & only using keyboard) with the help of this short cut keys. For example, to switch display to 'Situational' mode, user shall press 'D' & 'S' keys in combination with 'Alt' key, i.e., 'Alt +D+S'. Moreover, user can also use specialized short cut keys, if assigned any, to access the same functionality. Drop-down menus of SCD Main Window are described in the following sections. All the HMI commands shall logically be grouped into menus (as shown in **Figure 5.43**) for easy appreciation by the user as given below:

| (b) | Display Filters. |
|-----|------------------|
| (c) | Map.             |
| (d) | ES Processor.    |
| (e) | ES Receivers.    |
| (f) | EA System.       |
| (g) | RFPS.            |
| (h) | CMS.             |
| (j) | ESI.             |
| (k) | LRSAM.           |
| (l) | KAVACH.          |
| (m) | Print.           |
| (n) | System.          |

(p) Help.

(a) Display.

![](_page_202_Picture_1.jpeg)

**Figure-5.43: Menu Bar**

**5.5.4.2.8.1 Display Menu**.This menu (as shown in **Figure 5.44**) shall include controls for switch display type ('Tactical/ Situational/ Tabular/ Map'), display mode ('True/ Relative'), select display zoom (based on sector, threat type), display screen shot (take new one, show existing images). Refer section '5.5.4.2.25.1' for description on 'Tactical', 'Situational', 'Tabular' & 'Map Display'. The following sections describe the menu items available under this menu.

![](_page_202_Picture_4.jpeg)

**Figure-5.44: Display Menu**

**5.5.4.2.8.2 Tactical**.User shall click this menu item to switch to 'Tactical Display' and features related to this display type shall be enabled/ disabled accordingly. The GUI is shown in **Figure 5.45**. Refer section '5.5.4.2.25.1 Tactical Display' for description on 'Tactical Display'.

SHAKTI : UHB\Ch5 Page 199 of 614

![](_page_203_Figure_1.jpeg)

**Figure-5.45: Tactical Display GUI**

**5.5.4.2.8.3 Situational**.User shall click this menu item to switch to 'Situational Display' and features related to this display type shall be enabled/ disabled accordingly. The GUI is shown in **Figure 5.46**. Refer section '5.5.4.2.25.2' 'Situational Display' for description on 'Situational Display'.

SHAKTI : UHB\Ch5 Page 200 of 614

![](_page_204_Figure_1.jpeg)

**Figure-5.46: Situational Display GUI**

**5.5.4.2.8.4 Map**.User shall click this menu item to switch to 'Map Display' in Graphics Window. The features related to this display type shall be enabled/ disabled accordingly. The GUI is shown in **Figure 5.47**. Refer section '5.5.4.2.25.3 Map Display' for description on 'Map Display'.

SHAKTI : UHB\Ch5 Page 201 of 614

![](_page_205_Figure_1.jpeg)

**Figure-5.47: Map Display GUI**

**5.5.4.2.8.5 Tabular**.User shall click this menu item to switch to 'Tabular Display' which shall stretch horizontally, hiding Graphics Window. The features related to this display type shall be enabled/ disabled accordingly. The GUI is shown in **Figure 5.48**.Refer section '5.5.4.2.25.4 Tabular Display' for description on 'Tabular Display'.

SHAKTI : UHB\Ch5 Page 202 of 614

![](_page_206_Picture_1.jpeg)

**Figure-5.48: Tabular Display GUI**

**5.5.4.2.8.6 Zoom / Select in Tactical Sector**.In 'Tactical Display', tracks shall be zoomed within a sector range. When user clicks on this menu item, a GUI **(Figure 5.49)**  shall be displayed.

![](_page_207_Picture_2.jpeg)

**Figure-5.49: GUI for Sector Zoom in Tactical Display**

5.5.4.2.8.6.1 User shall enter start & stop angles of a sector range and click on 'Apply' option on this GUI. The selected sector shall be expanded and displayed in complete 360 degree area & only emitters falling within this sector shall be displayed; rest of the emitters shall not be visible, as shown in **Figure 5.50**. If user selects a sector of 360 degrees, then there will be no difference between a normal area and zoomed area on 'Tactical Display'.

SHAKTI : UHB\Ch5 Page 204 of 614

![](_page_208_Figure_1.jpeg)

**Figure-5.50: Tactical Display GUI with Sector Zoom**

**Note: This zoom will be applied only in 'Tactical Display' & rest of the displays will be not affected**.

**5.5.4.2.8.7 Zoom / Select in Tactical Track**.In 'Tactical Display', tracks shall be zoomed around a track DOA. When user clicks on this menu item, a GUI (as shown in **Figure 5.51**) shall be displayed.

![](_page_208_Picture_5.jpeg)

**Figure-5.51: GUI for Track DOA Zoom in Tactical Display**

SHAKTI : UHB\Ch5 Page 205 of 614

5.5.4.2.8.7.1 User shall select an emitter and click on 'Apply' option on this GUI. Area around the track DOA shall be expanded into 360-degree sector & only emitters falling within that sector shall be displayed; rest of the emitters shall not be visible, as shown **Figure 5.52**.

![](_page_209_Figure_2.jpeg)

**Figure-5.52: Tactical Display GUI with Track DOA Zoom**

**Note**: **This zoom will be applied only in 'Tactical Display' & rest of the displays will be not affected.**

**5.5.4.2.8.8 Zoom / Select in Tactical Hostile**.User shall click this menu item to view only 'Hostile' type of emitters within whole 'Tactical Display' region of 360 degrees, as shown in **Figure 5.53**.

**Note: This zoom will be applied only in 'Tactical Display' & rest of the displays will be not affected.**

SHAKTI : UHB\Ch5 Page 206 of 614

![](_page_210_Figure_1.jpeg)

**Figure-5.53: Tactical Display GUI with Zoom on Hostile Tracks**

**5.5.4.2.8.9 Zoom / Select in Tactical Known**.User shall click this menu item to view only 'Known' type of emitters within whole 'Tactical Display' region of 360 degrees, as shown in **Figure 5.54**.

**Note: This zoom will be applied only in 'Tactical Display' & rest of the displays will be not affected.**

SHAKTI : UHB\Ch5 Page 207 of 614

![](_page_211_Figure_1.jpeg)

**Figure-5.54: Tactical Display GUI with Zoom on Known Tracks**

5.5.4.2.8.11 **Zoom / Select in Tactical Unknown**.User shall click this menu item to view only 'Unknown' type of emitters within whole 'Tactical Display' region of 360 degrees, as shown in **Figure 5.55**. This zoom will be applied only in 'Tactical Display' & rest of the displays will be not affected.

SHAKTI : UHB\Ch5 Page 208 of 614

![](_page_212_Figure_1.jpeg)

**Figure-5.55: GUI Tactical Display GUI with Zoom on Unknown Tracks**

**5.5.4.2.8.11 Zoom / Select in Tactical Default**.User shall click this menu item to remove any zoom applied in 'Tactical Display' and reset it to default view.

#### **Note**:

- **(i) This zoom will be applied only in 'Tactical Display' & rest of the displays will be not affected.**
- **(ii) To apply zoom in 'Situational Display', user shall use rubber-band zoom to zoom in a particular frequency band & sector and use 'Display Filters' to view only 'Hostile/ Known/ Unknown' type of emitters.**
- **(iii)User shall use 'Display Filters' to view emitters of interest in 'Tabular Display'**

SHAKTI : UHB\Ch5 Page 209 of 614

**in a particular frequency band and sector.**

**5.5.4.2.8.12 Mode True**.User shall click this menu item to switch display to 'True' mode. In 'True' mode, the DOA of all the emitters in all emitter presentation windows shall be displayed w.r.t. 'True North'. For example: Platform heading (bearing) line in 'Situational Display' will be moved (as shown in **Figure 5.56**) as per the value received from ESI. This indicates Platform & emitters are shown (positioned) and updated on display w.r.t. to 'True North'.

![](_page_213_Figure_3.jpeg)

**Figure-5.56: GUI for True Mode in Situational Display – Display Menu.**

**5.5.4.2.8.13 Mode-Relative**.User shall click this menu item to switch display to 'Relative' mode. In 'Relative' mode, the DOA of all the emitters in all emitter presentation windows shall be displayed w.r.t. Platform heading. For example: Platform heading (bearing) line in 'Situational Display' will always be fixed at 0 degree (as shown in **Figure 5.57**). This indicates emitters are shown (positioned) & updated on display w.r.t. Platform heading.

SHAKTI : UHB\Ch5 Page 210 of 614

![](_page_214_Figure_1.jpeg)

**Figure-5.57: GUI for Relative Mode in Situational Display – Display Menu**

**5.5.4.2.8.14 Screen Shot – Capture Full Screen**.User shall click this menu item to capture image of the full screen of SCD Main Window GUI. A GUI, as shown in **Figure 5.58,** shall be displayed with a preview of captured image.

5.5.4.2.8.14.1 User shall a file name and click on 'Save Screen Shot' option to save it in a predefined folder on SCD storage.

5.5.4.2.8.14.2 User shall click on 'Cancel' option to discard the captured image without saving it, exit this GUI and go to SCD Main Window GUI.

SHAKTI : UHB\Ch5 Page 211 of 614

![](_page_215_Figure_1.jpeg)

**Figure-5.58: GUI for Saving Full Screen Image – Display Menu.**

SHAKTI : UHB\Ch5 Page 212 of 614

- **5.5.4.2.8.15 Screen Shot – Capture Active Window**.User shall click this menu item to capture image of active (currently open) GUI in SCD Main Window. A GUI, as shown in **Figure 5.59**, shall be displayed with a preview of captured image.
- 5.5.4.2.8.15.1 User shall a file name and click on 'Save Screen Shot' option to save it in a predefined folder on SCD storage.
- 5.5.4.2.8.15.2 User shall click on 'Cancel' option to discard the captured image without saving it, exit this GUI and go to SCD Main Window.

![](_page_216_Picture_4.jpeg)

**Figure-5.59: GUI for Saving Active Window Image – Display Menu.**

- **5.5.4.2.8.16 Screen Shot – Show Existing**.User shall click this menu item to view the existing screen shot images of SCD Main Window GUIs. A GUI, as shown in the **Figure 5.60,** shall be displayed to user to select an image file and view its image.
- 5.5.4.2.8.16.1 User shall select a file from the list of files on this GUI and click on 'Show Image' option.
- 5.5.4.2.8.16.2 User shall click on 'Close' option to exit from this GUI and go to SCD Main Window.

SHAKTI : UHB\Ch5 Page 213 of 614

![](_page_217_Figure_1.jpeg)

**Figure-5.60: GUI for Showing Existing Screen Shots – Display Menu.**

SHAKTI : UHB\Ch5 Page 214 of 614

- **5.5.4.2.8.17 Show/Hide Windows – Show System Message Window**.User shall click on this menu item to show/ hide 'System Messages Window' in SCD Main Window. This shall be a toggling menu item and shall switch between 'Show System Messages Window' & 'Hide System Messages Window' options. By default, 'System Messages Window' shall be hidden. Details of 'System Messages Window' are described in 5.5.4.2.30sections.
- **5.5.4.2.8.18 Show/Hide Windows – Hide Activity Window**.User shall click on this menu item to show/ hide 'Activity Window' in SCD Main Window. This shall be a toggling menu item and shall switch between 'Show Activity Window' & 'Hide Activity Window' options. By default, 'Activity Window' shall be visible. Details of 'Activity Window' are described in 5.5.4.2.22sections.
- **5.5.4.2.8.19 Show/ Hide Windows – Show / Hide Sub Window Titles**.User shall click on this menu item to show/ hide titles of sub-windows (Graphics Window, Emitter Report Window, Latest Emitters Window, EA Parameters Window, Link & Self-Test Status & System Messages) in SCD Main Window. This shall be a toggling menu item and shall switch between 'Show Sub-Window Titles' & 'Hide Sub-Window Titles' options. By default, all titles shall be hidden.
- **5.5.4.2.8.20 Show/ Hide Windows – Show / Hide Link &Self Test Status Window**. User shall click on this menu item to show/ hide 'Link & Self-Test Status' GUI in SCD Main Window. This shall be a toggling menu item and shall switch between 'Show Link & Self-Test Status Window' & 'Hide Link & Self-Test Status Window' options. By default, 'Link & Self-Test Status Window' GUI shall be hidden. Details of this GUI are described in the following sections.
- **5.5.4.2.8.21 Show/ Hide Windows – Show / Hide Hook Up Emitters Window**.User shall click on this menu item to show/ hide 'Hook Up Emitter Window' GUI in SCD Main Window. This shall be a toggling menu item and shall switch between 'Show Hook Up Emitters Window' & 'Hide Hook Up Emitters Window' options. By default, 'Hook Up Emitters Window' GUI shall be hidden. Operator designated emitters will be shown in this window and maximum of 10 tracks/emitters shall be shown. Operator has the facility to Add/Delete tracks to the list in this window.
- **5.5.4.2.8.22 Show/ Hide Windows – Show / Hide Tool Bar**. User shall click on this menu item to show/ hide 'Application Tool Bar' GUI in SCD Main Window. This shall be a toggling menu item and shall switch between 'Show Tool Bar' & 'Hide Tool Bar' options. By default, 'Application Tool' GUI shall be visible. Details of this GUI are described in the

SHAKTI : UHB\Ch5 Page 215 of 614

following sections.

**5.5.4.2.8.23 Show/ Hide Auto BITE Tracks**.User shall click on this menu item to view/hide Auto BITE tracks from all receivers.

5.5.4.2.8.23.1 Auto BITE tracks are shown in Cyan colour. NBRx2 receiver's Auto BITE tracks are shown in **Figure 5.61**. NBRx1 receiver's Auto BITE tracks are shown in **Figure 5.62**.

5.5.4.2.8.23.2 This shall be a toggling menu item and shall switch between 'Show Auto BITE Tracks' & 'Hide Auto BITE Tracks' options. By default, 'Show Auto BITE Tracks' shall be visible.

5.5.4.2.8.23.2 If all the parameters of Auto BITE track are OK & matching with reference data then Auto BITE tracks are shown in cyan colour.

5.5.4.2.8.23.3 If some or all the parameters of Auto BITE track are NOT OK & not matching with reference data then Auto BITE tracks are shown in orange colour.

![](_page_219_Picture_7.jpeg)

**Figure-5.61: Auto BITE tracks (NBRx2) in Tabular window**

SHAKTI : UHB\Ch5 Page 216 of 614

![](_page_220_Picture_1.jpeg)

**Figure-5.62: Auto BITE tracks (NBRx1) in Tabular window**

**5.5.4.2.8.24 Show/ Hide Windows – Show / Hide Emitters Watch Window**.User shall click on this menu item to show/ hide 'Emitters Watch Window' GUI in SCD Main Window. This shall be a toggling menu item and shall switch between 'Show Emitters Watch Window' & 'Hide Emitters Watch Window' options. By default, 'Emitters Watch Window' GUI shall be hidden. Emitters based on Operator selected filters (Freq, PW and PRF) will be shown in this window. Operator has the facility to modify filters.

**5.5.4.2.9 Display Filter Menu**.This menu (as shown in **Figure 5.63**) shall include controls for selecting and applying display filters w.r.t. 'Track Status', 'Bands & Sectors', 'Receiver Type', 'Time of Arrival', 'Scan Type', 'PRF Type', 'Signal Type', 'Threat Type', 'Operational Role', 'Platform Type', 'Emitter Labels' etc.

5.5.4.2.9.a Display filters are data domain specific and shall be applicable only at SCD Main Window thus by de-cluttering the display during highly dense scenarios. When a filter is enabled & applied, emitters with that filter parameter shall be displayed on SCD Main Window. When a filter is disabled & applied, emitters with that filter parameter shall be hidden on SCD Main Window. This mechanism shall be followed for all the menu items & GUIs under this menu.

5.5.4.2.9.b Features like individual or multiple filter selection, setting all filters on/ off etc., shall be provided through the GUIs under this menu.

**Note: No display filter will be applied by default**.

5.5.4.2.9.c The following sections describe the menu items available under this menu.

SHAKTI : UHB\Ch5 Page 217 of 614

![](_page_221_Picture_1.jpeg)

**Figure-5.63: Display Filters Menu – SCD Main Window.**

**5.5.4.2.9.1 Track Status**.When user clicks on this menu item a GUI, as shown in **Figure 5.64**, shall be displayed. User shall check 'Enable' option, select required filter parameter (Track Status: Active or Passive) & and click on 'Apply' option to enforce this filter or shall click on 'Disable' option to remove this filter on SCD Main Window. User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

![](_page_221_Picture_4.jpeg)

**Figure-5.64: Track Status Filter GUI – Display Filters Menu**

**5.5.4.2.9.2 Bands & Sectors**.When user clicks on this menu item a GUI, as shown in **Figure 5.65**, shall be displayed. User shall check 'Enable' option, select required

SHAKTI : UHB\Ch5 Page 218 of 614

filter parameter (frequency band & sector) and click on 'Apply' option to enforce this filter or shall click on 'Disable' option to remove this filter on SCD Main Window.

5.5.4.2.9.2.1 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

![](_page_222_Figure_3.jpeg)

**Figure-5.65: Bands & Sectors Filter GUI – Display Filters Menu**

**5.5.4.2.9.3 Receiver Type**.When user clicks on this menu item a GUI, as shown in **Figure 5.66**, shall be displayed. User shall check 'Enable' option, select required filter parameter (NBRx1: 0.175-0.5 GHz , NBRx2: 0.5-18 GHz, BBRx1: 2.2-18 GHz or BBRx2:

SHAKTI : UHB\Ch5 Page 219 of 614

18-40GHz) & and click on 'Apply' option to enforce this filter or shall click on 'Disable' option to remove this filter on SCD Main Window.

5.5.4.2.9.3.1 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

![](_page_223_Picture_3.jpeg)

**Figure-5.66: Receiver Type Filter GUI – Display Filters Menu.**

**5.5.4.2.9.4 Time of Arrival**.When user clicks on this menu item a GUI, as shown in **Figure 5.67**, shall be displayed. User shall check 'Enable' option, select TOFA (Time of First Arrival of a track) limits and click on 'Apply' option to enforce this filter or shall click on 'Disable' option to remove this filter on SCD Main Window.

5.5.4.2.9.4.1 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

SHAKTI : UHB\Ch5 Page 220 of 614

![](_page_224_Picture_1.jpeg)

**Figure-5.67: Time of Arrival Filter GUI – Display Filters Menu**

**5.5.4.2.9.5 Scan Type**.When user clicks on this menu item a GUI, as shown in **Figure 5.68**, shall be displayed. User shall check 'Enable' option, select required filter parameter (Scan Type: Circular, Conical, Lock-On etc.,) & and click on 'Apply' option to enforce this filter or shall click on 'Disable' option to remove this filter on SCD Main Window.

5.5.4.2.9.5.1 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

![](_page_224_Picture_5.jpeg)

**Figure-5.68: Scan Type Filter GUI – Display Filters Menu**

**5.5.4.2.9.6 PRF Type**.When user clicks on this menu item a GUI, as shown in **Figure 5.69**, shall be displayed. User shall check 'Enable' option, select required filter parameter

SHAKTI : UHB\Ch5 Page 221 of 614

(PRF Type: Staggered, Jittered, Fixed, Unknown etc.,) & and click on 'Apply' option to enforce this filter or shall click on 'Disable' option to remove this filter on SCD Main Window.

5.5.4.2.9.6.1 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

![](_page_225_Picture_3.jpeg)

**Figure-5.69: PRF Type Filter GUI – Display Filters Menu.**

**5.5.4.2.9.7 Frequency Type**. When user clicks on this menu item a GUI, as shown in **Figure 5.70**, shall be displayed. User shall check 'Enable' option, select required filter parameter (Signal Type: Pulsed, CW, Chirp, Poly Phase etc.,) & and click on 'Apply' option to enforce this filter or shall click on 'Disable' option to remove this filter on SCD Main Window.

5.5.4.2.9.7.1 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

SHAKTI : UHB\Ch5 Page 222 of 614

![](_page_226_Picture_1.jpeg)

**Figure-5.70: Frequency Type Filter GUI – Display Filters Menu**

**5.5.4.2.9.8 Threat Type**.When user clicks on this menu item a GUI, as shown in **Figure 5.71**, shall be displayed. User shall check 'Enable' option, select required filter parameter (Threat Type: Unknown, Hostile or Known) & and click on 'Apply' option to enforce this filter or shall click on 'Disable' option to remove this filter on SCD Main Window.

**Note**: **Applying this display filter is same as applying 'Hostile/ Known, Unknown' zoom in 'Emitter Presentation Windows'. Any existing zoom will be removed and this display filter will be applied in 'Emitter Presentation Windows'.**

5.5.4.2.9.8.1 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

SHAKTI : UHB\Ch5 Page 223 of 614

![](_page_227_Picture_1.jpeg)

**Figure-5.71: Threat Type Filter GUI – Display Filters Menu**

**5.5.4.2.9.9 Operational Role**.When user clicks on this menu item a GUI, as shown in **Figure 5.72**, shall be displayed. User shall check 'Enable' option, select required filter parameter (Operational Role: Navigation, Surface Search, Missile Fire Control etc.,) & and click on 'Apply' option to enforce this filter or shall click on 'Disable' option to remove this filter on SCD Main Window.

5.5.4.2.9.9.1 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

.

SHAKTI : UHB\Ch5 Page 224 of 614

![](_page_228_Picture_1.jpeg)

**Figure-5.72: Operational Role Filter GUI – Display Filters Menu**

**5.5.4.2.9.10 Platform Type**. When user clicks on this menu item a GUI, as shown in **Figure 5.73**, shall be displayed. User shall check 'Enable' option, select required filter parameter (Platform Type: Ship, Submarine, Aircraft, Missile etc.,) & and click on 'Apply' option to enforce this filter or shall click on 'Disable' option to remove this filter on SCD Main Window.

5.5.4.9.10.1 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

SHAKTI : UHB\Ch5 Page 225 of 614

![](_page_229_Picture_1.jpeg)

**Figure-5.73: Platform Type Filter GUI – Display Filters Menu.**

**5.5.4.2.9.11 Emitter Labels**.When user clicks on this menu item a GUI, as shown in **Figure 5.74**, shall be displayed. User shall check 'Enable' option, select required filter parameter (Emitter Labels: Track Number, NTDS Symbol or Library Match Number) & and click on 'Apply' option to enforce this filter or shall click on 'Disable' option to remove this filter on SCD Main Window.

5.5.4.2.9.11.1 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

SHAKTI : UHB\Ch5 Page 226 of 614

![](_page_230_Picture_1.jpeg)

**Figure-5.74: Emitter Labels Filter GUI – Display Filters Menu**

**5.5.4.2.9.12 Manage Filters**. When user clicks on this menu item a GUI, as shown in **Figure 5.75**, shall be displayed. User shall check a filter type (Track Status, Scan Type, Receiver Type etc.,) and click on 'Apply' option to enforce those filter categories or shall uncheck a filter type & click on 'Apply' option to remove those filters categories on SCD Main Window.

5.5.4.2.8.12.1 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

![](_page_230_Picture_5.jpeg)

**Figure-5.75: Manage Filters GUI – Display Filters Menu.**

SHAKTI : UHB\Ch5 Page 227 of 614

**5.5.4.2.9.13 Reset All Filters to Default**.User shall click this menu item to reset (remove) all existing filters on SCD Main Window. A confirmation message shall be displayed to user before resetting any filters.

![](_page_231_Picture_2.jpeg)

**Figure-5.76: Reset All Filters to Default– Display Filters Menu**

**5.5.4.2.10 Map Menu**.Map related functionalities such as: loading maps into SCD application, selecting map mode, showing Platform path, Zoom, 'Tactical' superimpose, spokes, annotations, way points etc., shall be grouped under this menu (as shown in **Figure 5.77**). Refer section 5.5.4.3.16.3 for description on 'Map Display'. 'Map Display' shall be active in Graphics Window for performing any map related operations. The following sections describe the menu items available under this menu.

![](_page_231_Picture_5.jpeg)

**Figure-5.77: Map Menu – SCD Main Window**

**5.5.4.2.10.1 Load Maps**.When user clicks on this menu item a GUI, as shown in **Figure-5.78**, shall be displayed for selecting a map file from SCD storage. User shall select a map file and click on 'Load File' option. Selected map file shall be loaded and updated on 'Map Display' in Graphics Window.

5.5.4.2.10.1.1 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

SHAKTI : UHB\Ch5 Page 228 of 614

![](_page_232_Picture_1.jpeg)

**Figure-5.78: GUI for Loading Maps into SCD Application – Map Menu.**

- **5.5.4.2.10.2 Mode – Moving Platform**.User shall click on this menu item to switch 'Map Display' to 'Moving Platform' mode. In this mode, position of the Platform shall be updated on map as per information received from ESI. Map data and co-ordinates of the map shall be adjusted and updated automatically if Platform moves out of view on 'Map Display'. This shall be the default mode when 'Map Display' is activated.
- **5.5.4.2.10.3 Mode – Moving Map**.User shall click on this menu item to switch 'Map Display' to 'Moving Map' mode. In this mode, position of the Platform shall always be centered in the 'Map Display' and the map data and map co-ordinates shall be moved and updated accordingly.
- **5.5.4.2.10.4 Mode – Pan**. User shall click on this menu item to switch 'Map Display' to 'Pan' mode. In this mode, neither map nor the Platform shall be moved on map. In this mode, map data along with map context shall be moved and the map coordinates shall be updated accordingly if user drags mouse by pressing mouse left button down on map area.
- **5.5.4.2.10.5 Platform Path – Show Full Path**.When user shall click on this menu item, complete (during the session from the start of SCD application execution) trace of the

SHAKTI : UHB\Ch5 Page 229 of 614

Platform shall be plotted & updated on map, as shown in **Figure-5.79**

![](_page_233_Figure_2.jpeg)

**Figure-5.79: GUI with Full Path Trace of Platform on Map – Map Menu.**

**5.5.4.2.10.6 Platform Path – Show Latest Path**.When user clicks on this menu item, only the recent path points of the Platform shall be plotted & updated on map, as shown in **Figure-5.80**. Latest path contains the recent latitude & longitude traces points of Platform and the number of points in this path can be restricted by user in 'System Configuration' in 'Offline' mode.

SHAKTI : UHB\Ch5 Page 230 of 614

![](_page_234_Figure_1.jpeg)

**Figure-5.80: GUI with Latest Path Trace of Platform on Map – Map Menu**

- **5.5.4.2.10.7 Platform Path – Hide Path**.When user clicks on this menu item, no trace of the Platform shall be plotted & updated on map. By default, Platform path shall be hidden.
- **5.5.4.2.10.8 Zoom – In**.User shall click on this menu item to 'Zoom In' on map area in 'Map Display' with a zoom step value of 1NM (default value).
- **5.5.4.2.10.9 Zoom – Out**.User shall click on this menu item to 'Zoom Out' on map area in 'Map Display' with a zoom step value of 1NM (default value).
- **5.5.4.2.10.10 Zoom Reset**.User shall click on this menu item to reset map area to default view in 'Map Display'. The default zoom level is 100 NM of map scale.
- **5.5.4.2.10.11 Tactical Picture – Superimpose**.User shall click on this menu item to superimpose 'Tactical' picture (emitter data) on map, as shown in **Figure-5.81**. A maximum of 500 emitters, map scale of 100NM and Platform speed of 50NM/ hour shall be presented

SHAKTI : UHB\Ch5 Page 231 of 614

on map when 'Superimpose' option is selected.

![](_page_235_Figure_2.jpeg)

**Figure-5.81: GUI with Tactical Picture Superimposed on Map – Map Menu**

**5.5.4.2.10.12 Tactical Picture – Remove**.User shall click on this menu item to remove existing 'Tactical' picture on map. By default, 'Tactical' picture shall not be displayed.

**5.5.4.2.10.13 Spokes – Show**.User shall click on this menu item to view 'Spokes' (bearing lines of emitters) on map, as shown in **Figure-5.82**. Colour of 'Spokes' shall be as per the colour scheme of the respective emitter category, which will be described in the coming sections.

SHAKTI : UHB\Ch5 Page 232 of 614

![](_page_236_Figure_1.jpeg)

**Figure-5.82: GUI with Spokes on Map – Map Menu**

**5.5.4.2.10.14 Spokes – Hide**.User shall click on this menu item to remove existing 'Spokes' on map. By default, 'Spokes' shall not be displayed.

**5.5.4.2.10.15 Annotations – Add**. Annotations are information texts/ comments displayed as text symbols, at specified locations (latitude & longitude) on the map. When user clicks on this menu item, a GUI (as shown in **Figure-5.83**) with help text about 'how to place annotations on map', shall be displayed. User shall use mouse left button & keep on clicking in map area where the annotations are to be placed. When finished adding annotations, user shall click mouse right button. Map annotations shall be marked with default annotation description (short text) and latitude & longitude values as shown in **Figure-5.84**.

![](_page_236_Figure_5.jpeg)

**Figure-5.83: GUI with Help to Add Annotations on Map – Map Menu**

SHAKTI : UHB\Ch5 Page 233 of 614

![](_page_237_Figure_1.jpeg)

**Figure-5.84: GUI with Annotations on Map – Map Menu**

- **5.5.4.2.10.16 Annotations – Show All**. User shall click on this menu item to show all the existing annotations in map area on 'Map Display'.
- **5.5.4.2.10.17 Annotations – Hide – All**.User shall click on this menu item to hide all the existing annotations in map area on 'Map Display'. By default, all annotations shall be hidden on map.
- **5.5.4.2.10.18 Annotations – Manage**.When user clicks on this menu item a GUI, as shown in **Figure-5.85**, shall be displayed to manage (view, add, modify or delete) the annotations of map. This GUI shall contain a list of already existing map annotations.

SHAKTI : UHB\Ch5 Page 234 of 614

![](_page_238_Figure_1.jpeg)

**Figure 5.85: Manage Annotations GUI – Map Menu**

- (a) **Add Annotation**: To add an annotation, user shall enter 'Latitude & Longitude' values, 'Description' (brief) of it and click on 'Add Annotation' option on this GUI. This annotation shall be added to the 'List of Annotations'.
- (b) **Edit Annotation**: To edit (modify) an existing annotation, user shall select it and click on 'Edit Annotation' option. After making changes to it, user shall click on 'Update' option.
- (c) **Delete Annotation**: To delete an existing annotation, user shall select it and click on 'Delete Selected' option. User shall click on 'Delete All' option to remove all the annotations from map. 'List of Annotations' table shall be updated for any addition/ modification/ deletion of annotations.
- (d) **Display Annotations**: After making any modifications to annotations, user shall click on 'Show Selected Annotations on Map' option to display selected annotations on map. Note: only selected annotations shall be displayed on map.User shall click on 'Cancel'

SHAKTI : UHB\Ch5 Page 235 of 614

option to exit from this GUI and go to SCD Main Window.

**5.5.4.2.10.19 Way Points – Add**. Way points represent navigation points/ land marks (with latitude & longitude) and shall be displayed as way point symbols on map. This feature of adding way points on map will be available only 'Pan' mode.

5.5.4.2.10.19.1 When user clicks on this menu item, a GUI (as shown in **Figure-5.86**) with help text about 'how to place way points on map', shall be displayed.

![](_page_239_Figure_4.jpeg)

**Figure-5.86: GUI with Help to Add Way Points on Map – Map Menu**

5.5.4.2.10.19.2 User shall use mouse left button & keep on clicking in map area where the way points are to be placed. When finished adding way points, user shall click mouse right button and a GUI, as shown in **Figure-5.87**, shall be displayed for entering route name for these way points. No route with way points will be added if user clicks on 'Cancel' option at this stage.

![](_page_239_Picture_7.jpeg)

**Figure-5.87: GUI for Selecting Route Name on Map – Map Menu**

5.5.4.2.10.19.3 Map way points shall be marked with point names (such as WP1, WP2, WP3 etc.,) and route name, as shown in **Figure-5.88**.

SHAKTI : UHB\Ch5 Page 236 of 614

![](_page_240_Figure_1.jpeg)

**Figure-5.88: GUI with Way Points on Map – Map Menu**

- **5.5.4.2.10.20 Way Points – Show All**. User shall click on this menu item to show all the existing way points in map area on 'Map Display'.
- **5.5.4.2.10.21 Way Points – Hide All**. User shall click on this menu item to hide all the existing way points in map area on 'Map Display'. By default, all way points shall be hidden on map.
- **5.5.4.2.10.22 Way Points – Manage**.When user clicks on this menu item a GUI, as shown in **Figure-5.89**, shall be displayed to manage (view, add, modify or delete) the way points of map. This GUI shall contain a list of already existing map way points.
- (a) **Add Way Points**. User shall enter 'Latitude & Longitude' values and click on 'Add Point'; the point will be added to way points table. Minimum of two way points will be required to create a route.
- (b) **Add Route**. User shall enter 'Route Name' and click on 'Add Route' to create route on map with way points. The new route will be added to the 'List of Routes' table on the GUI.

SHAKTI : UHB\Ch5 Page 237 of 614

![](_page_241_Figure_1.jpeg)

**Figure-5.89: Manage Way Points GUI – Map Menu**

- (c) **Edit Way Points**. To edit (modify) an existing way point, user shall select it and click on 'Edit Point' option. After making changes to it, user shall click on 'Update Point' option.
- (d) **Edit Route**. To edit (modify) an existing route of way points, user shall select it and click on 'Edit Route' option. After making changes to it, user shall click on 'Update Route' option.
- (e) **Delete Way Point**. To delete an existing way point, user shall select it and click on 'Delete Point' option.
- (f) **Delete Route**. To delete an existing way point, user shall select it and click on 'Delete Selected' option. User can delete all the routes by clicking on 'Delete All' option. 'List of Annotations' table shall be updated for any addition/ modification/ deletion of way points.
- (g) **Display Way Points**. After making any modifications to way points, user shall click on 'Show Selected Way Points on Map' option to display selected way points on map. Note: only selected way points shall be displayed on map. User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

SHAKTI : UHB\Ch5 Page 238 of 614

**5.5.4.2.10.23 Find Distance & Bearing – Using Mouse between Two Points**.User shall click on this menu item to find distance & bearing between any two points on map using mouse, and display it. When user activates this menu item, a GUI (as shown in **Figure-5.90**) with help text about 'how to measure distance & bearing on map', shall be displayed.

![](_page_242_Picture_2.jpeg)

**Figure-5.90: Help GUI to Find Distance & Bearing using Mouse – Map Menu**

5.5.4.2.10.23.1 User shall use mouse left button and select two points on map as shown in **Figure-5.91** GUI with Distance & Bearing between Two Point – Map Menu. User can repeat this activity for any other two points on map and when finished, user shall click mouse right button to end this activity.

![](_page_242_Figure_5.jpeg)

**Figure-5.91: GUI with Distance & Bearing between Two Point – Map Menu**

SHAKTI : UHB\Ch5 Page 239 of 614

## **5.5.4.2.10.24 Find Distance & Bearing – Using Mouse between Platform & Points**.

User shall click on this menu item to find distance & bearing between the Platform & a point on map using mouse, and display it. When user activates this menu item, a GUI (as shown in **Figure-5.92**) with help text about 'how to measure distance & bearing on map', shall be displayed.

5.5.4.2.10.24.1 User shall use mouse left button and select a point on map. The distance & bearing between the Platform & the point shall be displayed on map as shown in **Figure-5.92**. User can repeat this activity for any other point on map and when finished, user shall click mouse right button to end this activity.

![](_page_243_Figure_4.jpeg)

**Figure-5.92: GUI with Distance & Bearing between Platform & Point – Map Menu**

**5.5.4.2.10.25 Find Distance & Bearing – Manual Entry**. User shall click on this menu item to find distance & bearing between any two points on map by entering their 'Latitude & Longitude' values manually.

5.5.4.2.10.25.1 A GUI, as shown in **Figure-5.93**, shall be displayed for entering point data. Alternately, user can click mouse left button on map area to fetch its latitude & longitude values and display them on this GUI.

SHAKTI : UHB\Ch5 Page 240 of 614

5.5.4.2.10.25.2 User shall click on 'Calculate & Show' option to find the distance & bearing between the selected points and display the details on this GUI and on map also.

![](_page_244_Picture_2.jpeg)

**Figure-5.93: GUI to Find Distance & Bearing with Manually Entry – Map Menu**

**5.5.4.2.10.26 Find Distance & Bearing – Remove Line**.User shall click on this menu item to remove an existing line (with distance & bearing) on map. This will be required to un-clutter the map area for clear view. This menu item shall be enabled only when a line (distance & bearing) is drawn on map.

**5.5.4.2.10.27 Find Distance & Bearing – Stop Measurement**.User shall click on this menu item to stop the process of finding distance & bearing on map area. This will be an alternate option in addition to clicking of mouse right button for the same function. This menu item shall be enabled only when finding distance & bearing on map is in progress.

**5.5.4.2.10.28 Reset to Default**.User shall click on this menu item to reset 'Map Display'

SHAKTI : UHB\Ch5 Page 241 of 614

with default map context from default map configuration on SCD storage. 'Map Display' shall be reset a default working state & start updating with default map settings.

**5.5.4.2.11 ES Processor Menu**.ES Processor menu (as shown in **Figure-5.94**) shall include GUI controls for configuring & controlling ES Processor, tracking management, Warner Library management etc., from SCD application. The following sections describe the menu items available under this menu.

![](_page_245_Picture_3.jpeg)

**Figure 5.94: ES Processor Menu – SCD Main Window**

- **5.5.4.2.11.1 Load Warner Library**. User shall click on this menu item to view Warner Emitter Library and load or delete it at ES Processor. A GUI (as shown in **Figure-5.95**) containing Warner entries shall be displayed to user.
- 5.5.4.2.11.1.1 User can filter out records of the library by selecting record parameters and click on 'Show Records' option.
- 5.5.4.2.11.1.2 User shall click on 'Load Entire Warner Library at ES Processor' option to send the library to ES Processor.

SHAKTI : UHB\Ch5 Page 242 of 614

![](_page_246_Figure_1.jpeg)

**Figure-5.95: Warner Emitter Library GUI – ES Processor Menu**

5.5.4.2.11.1.3 User shall click on 'Delete Warner Library at ES Processor' option to delete the library at ES Processor.

**Note: No library matching will take place at ES Processor if library is deleted.**

5.5.4.2.11.1.4 User shall click on 'Close' option to exit from this GUI and go to SCD Main Window.

**5.5.4.2.11.2 Set Lockout frequency Bands**.User shall click on this menu item to view existing lockout frequency bands or set new ones at ES Processor. A GUI (as shown in **Figure-5.96**) containing frequency bands shall be displayed. The emitters falling within lockout frequency bands will not be reported by ES Processor to SCD system.

SHAKTI : UHB\Ch5 Page 243 of 614

![](_page_247_Figure_1.jpeg)

**Figure-5.96: GUI to Set Lockout Frequency Bands – ES Processor Menu**

5.5.4.2.11.2.1 User shall check 'Spectrum Band', 'Receiver Band' or 'Custom Band' option to select a lockout frequency band and click on 'Apply' option to enforce it at ES Processor. If successful, the lockout band region in 'EW Activity Window' & 'Situational Display' shall be painted in 'Grey' colour (transparent). 'Situational Display' GUI with lockout frequency bands applied is shown in **Figure-5.97**.

5.5.4.2.11.2.2 User shall click on 'Reset' option to remove any existing lockout frequency bands at ES Processor, thereby allowing ES Processor to report all emitter data to SCD system. Lockout region (grey) shall be removed from display, if reset is successfully done.

5.5.4.2.11.2.3 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

SHAKTI : UHB\Ch5 Page 244 of 614

![](_page_248_Figure_1.jpeg)

**Figure-5.97: Situational Display GUI with Lockout Frequency Bands Applied**

**5.5.4.2.11.3 Set Lockout Sectors**.User shall click on this menu item to view existing lockout sectors or set new ones at ES Processor. A GUI containing sectors (as shown in **Figure-5.98**) shall be displayed. The emitters falling within lockout sectors will not be reported by ES Processor to SCD system.

SHAKTI : UHB\Ch5 Page 245 of 614

![](_page_249_Picture_1.jpeg)

**Figure-5.98: GUI to Set Lockout Sectors – ES Processor Menu**

5.5.4.2.11.3**.**1 User shall check 'Sector' or 'Sector Range' option to select a lockout sector and click on 'Apply' option to enforce it at ES Processor. If successful, the lockout sector region in 'Tactical Display' & 'Situational Display' shall be painted in 'Grey' colour (transparent) as shown in **Figure-5.99**.

5.5.4.2.11.3**.**2 User shall click on 'Reset' option to remove any existing lockout sectors at ES Processor, thereby allowing ES Processor to report all emitter data to SCD system. Lockout region (grey) shall be removed from display, if reset is successfully.

5.5.4.2.11.3**.**3 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

SHAKTI : UHB\Ch5 Page 246 of 614

![](_page_250_Figure_1.jpeg)

**Figure-5.99: Tactical Display GUI with Lockout Sectors Applied**

**5.5.4.2.11.4 Set Track Build Criteria**.User shall click on this menu item to view existing track build criteria or set new one at ES Processor. A GUI containing track build criteria (as shown in **Figure-5.100**) shall be displayed. Track build criteria is meant for configuring ES Processor for building tracks from emitter data collected from ES receivers and report a library match.

5.5.4.2.11.4.1 User shall select a receiver, select 'Track Build Pulse Count', 'Maintenance Pulse Count', select 'De-interleaving Tolerances for Frequency, PW & DOA' and click on 'Apply' option to set these criteria at ES Processor.

5.5.4.2.11.4.2 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

SHAKTI : UHB\Ch5 Page 247 of 614

![](_page_251_Figure_1.jpeg)

**Figure-5.100: GUI to Set Track Build Criteria at ES Processor – ES Processor Menu**

**5.5.4.2.11.5 Set Auto Purge Time**.User shall click on this menu item to view existing auto purge time or set new one at ES Processor. A GUI with auto purge on/ off & time (as shown in **Figure-5.101**) shall be displayed. ES Processor will purge passive tracks automatically, based on auto purge time, if enabled.

![](_page_251_Picture_4.jpeg)

**Figure-5.101: GUI to Set Auto Purge Time at ES Processor – ES Processor Menu**

- 5.5.4.2.11.5.1 User shall check 'Auto Purge On' option, enter 'Track Age' and click on 'Apply' option to enforce auto purge activity at ES Processor.
- 5.5.4.2.11.5.2 User shall check 'Auto Purge Off' and click on 'Apply' option to stop auto purge activity at ES Processor.
- 5.5.4.2.11.5.3 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.
- **5.5.4.2.11.6 Rebuilt Tracks**.When user clicks on this menu item, a GUI, as shown in

SHAKTI : UHB\Ch5 Page 248 of 614

**Figure-5.102**, shall be displayed with selected tracks, if any, for rebuilding them at ES Processor. Rebuilding a track will remove its existing pulse data and a new track will be formed afresh.

![](_page_252_Picture_2.jpeg)

**Figure-5.102: GUI to Rebuild Tracks at ES Processor – ES Processor Menu**

- 5.5.4.2.11.6.1 User shall check 'All Tracks' option and click on 'Rebuild' option to rebuild them.
- 5.5.4.2.11.6.2 User shall check 'Selected Track' option, select a track number, and click on 'Add to List' & 'Apply' option to rebuild it.
- 5.5.4.2.11.6.3 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.
- **5.5.4.2.11.7 Purge Passive Tracks**. When user clicks on this menu item, a GUI, as shown in **Figure-5.103**, shall be displayed with selected passive tracks, if any, for purging (deleting) them at ES Processor.
- 5.5.4.2.11.7.1 User shall check 'All Tracks' option and click on 'Purge' option to purge them.
- 5.5.4.2.11.7.2 User shall check 'Selected Track' option, select a track number, and click on 'Add to List' & 'Apply' option to purge it.

SHAKTI : UHB\Ch5 Page 249 of 614

![](_page_253_Picture_1.jpeg)

**Figure-5.103: GUI to Purge Passive Tracks at ES Processor**

- 5.5.4.2.11.7.3 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.
- **5.5.4.2.11.8 Merge Tracks**.When user clicks on this menu item, a GUI, as shown in **Figure-5.104**, shall be displayed with selected active tracks, if any, for merging them into a single track at ES Processor.
- 5.5.4.2.11.8.1 User shall select 'Track No', click on 'Add to List' and click on 'Merge' option to merge tracks at ES Processor. Minimum 2 & maximum 8 tracks shall be allowed for merging.
- 5.5.4.2.11.8.2 Merge status shall be displayed with 'Merged Track Details', 'No of Merged Tracks' and their 'Track Numbers'.
- 5.5.4.2.11.8.3 User shall click on 'Cancel/ Close' option to exit from this GUI and go to SCD Main Window.

SHAKTI : UHB\Ch5 Page 250 of 614

![](_page_254_Figure_1.jpeg)

**Figure-5.104: GUI to Merge Tracks at ES Processor – ES Processor Menu**

- **5.5.4.2.11.9 Get PD Data**.User shall click on this menu item and a GUI, as shown in **Figure-5.105**, shall be displayed with options to get Pulse Descriptor (PD) data from ES Processor for a selected track.
- 5.5.4.2.11.9.1 User shall select 'Track No.', 'No. of PDs' and 'One Snap Shot' option and click on 'Get PD Data' option.
- 5.5.4.2.11.9.2 The result fetched from ES Processor shall be displayed on this GUI as emitter profile in textual & graph notation. The emitter profile shall include: 'Pulses vs DOA, TOA, Amplitude, Frequency and Pulse Width.
- 5.5.4.2.11.9.3 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

SHAKTI : UHB\Ch5 Page 251 of 614

![](_page_255_Figure_1.jpeg)

**Figure-5.105: PD Data GUI – ES Processor Menu**

**5.5.4.2.11.10 Auto Jam at ES Processor**.User shall click on this menu item and a GUI, as shown in **Figure-5.106**, shall be displayed with options to enable/ disable auto jamming at ES Processor. Auto jamming command will be issued by ES Processor on tracks with 'Warner Emitter Library' match. By default, auto jamming at ES Processor shall be enabled.

![](_page_255_Picture_4.jpeg)

**Figure-5.106: GUI for Auto Jamming at ES Processor – ES Processor Menu**

5.5.4.2.11.10.1 User shall select 'Enable/ Disable' and click on 'Apply' option to enable/ disable auto jamming at ES Processor.

SHAKTI : UHB\Ch5 Page 252 of 614

5.5.4.2.11.10.2 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

**5.5.4.2.11.11 Auto Merging of Tracks in 2.2-18 GHz ES Processor**.User shall click on this menu item and a GUI, as shown in **Figure-5.107**, shall be displayed with options to enable/ disable auto merging of mid band tracks of NB Rx2 (2.2-18GHz) & BB Rx1 (2.2- 18GHz) into a single track at ES Processor.

![](_page_256_Picture_3.jpeg)

**Figure-5.107: GUI for Auto Merge of Mid-Band Tracks – ES Processor Menu**

5.5.4.2.11.11.1 By default, auto merging of mid band tracks at ES Processor shall be disabled.

5.5.4.2.11.11.2 User shall select 'Enable/ Disable' and click on 'Apply' option to enable/ disable auto merging at ES Processor.

5.5.4.2.11.11.2 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

**5.5.4.2.11.12 Auto Merging of Agile at ES Processor**.User shall click on this menu item and a GUI, as shown in **Figure-5.108**, shall be displayed with options to enable/ disable auto merging of agile tracks into a single track at ES Processor.

![](_page_256_Picture_9.jpeg)

**Figure-5.108: GUI for Auto Merge of Agile Tracks – ES Processor Menu**

5.5.4.2.11.12.1 By default, auto merging of agile tracks at ES Processor shall be disabled.

SHAKTI : UHB\Ch5 Page 253 of 614

- 5.5.4.2.11.12.2 User shall select 'Enable/ Disable' and click on 'Apply' option to enable/ disable auto merging at ES Processor.
- 5.5.4.2.11.12.3 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.
- **5.5.4.2.11.13 PRI Tracker at ES Processor**. User shall click on this menu item and a GUI, as shown in **Figure-5.109**, shall be displayed with options to enable/ disable PRI Tracker at ES Processor for effectiveness of EA Jamming.
- 5.5.4.2.11.13.1 During Semi auto mode of EA jamming, without knowing the exact pulse interval, jamming will be applied for the user selected / Auto jamming emitters(s). When user shall apply the PRI tracker at ES processor, specified PRI gate will be predicted by ES processor and same shall be given to EA processor for effective jamming.

![](_page_257_Picture_5.jpeg)

**Figure-5.109: PRI Tracker at ES Processor**

- 5.5.4.2.11.13.2 By default, PRI Tracker at ES Processor shall be disabled.
- 5.5.4.2.11.13.3 User shall select 'Enable/ Disable' and click on 'Apply' option to enable/ disable PRI Tracker at ES Processor.
- 5.5.4.2.11.13.4 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.
- **5.5.4.2.11.14 Get Scan Type**.User shall select a track from emitter presentation windows and click on this menu item. A confirmation GUI, as shown in **Figure-5.110**, shall be displayed to user to get scan type from ES Processor. The scan type, if received from ES Processor, shall be updated on emitter presentation windows.

SHAKTI : UHB\Ch5 Page 254 of 614

![](_page_258_Picture_1.jpeg)

**Figure-5.110: Confirmation GUI to Get Scan Type – ES Processor Menu.**

**5.5.4.2.11.15 Reset**.User shall click on this menu item to reset ES Processor. Resetting ES Processor will remove all the existing tracks/ PDs and ES Processor will start rebuilding tracks afresh". Hence, user shall be aware of the operation and use it only when necessary. A confirmation GUI, as shown in **Figure-5.111**, shall be displayed to user. If ES Processor is reset successfully, all the tracks shall be removed from emitter presentation windows.

![](_page_258_Picture_4.jpeg)

**Figure-5.111: Confirmation GUI to Reset ES Processor – ES Processor Menu**

**5.5.4.2.12 ES Receivers Menu**.ES Receivers menu (as shown in **Figure-5.112**) shall include GUI controls for configuring & controlling ES Receivers from SCD application.

5.5.4.2.12.a The following sections describe the menu items available under this menu.

![](_page_258_Picture_8.jpeg)

**Figure-5.112: ES Receivers Menu – SCD Main Window**

**5.5.4.2.12.1 NBRx1 (0.175-0.5 GHz) – Directed Mode**.User shall login into SCD application in 'Online Mode' and SCD Main Window shall be displayed to access this GUI. When user clicks on this menu item, a GUI (as shown in **Figure-5.113**) shall be displayed to put NB Rx1 (0.175-0.5GHz) in 'Directed' mode of operation. The GUI shall retain the

SHAKTI : UHB\Ch5 Page 255 of 614

previous configuration parameters entered by user.

![](_page_259_Picture_2.jpeg)

**Figure-5.113: NBRx1 (0.175- 0.5 GHz) Directed Mode GUI – ES Receivers Menu**

- 5.5.4.2.12.1.1 User shall enter required mode parameters such as 'Frequency', 'RF Attenuation', 'IF Attenuation', 'Threshold', 'IF Band Width' & 'Scan Quadrant' and click on 'Apply' option to set them at the receiver.
- 5.5.4.2.12.1.2 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.
- 5.5.4.2.12.1.3 When Directed Mode is selected the receiver is continuously tuned to freq band.
- **5.5.4.2.12.2 NB RX1 (0.175-0.5 GHz) – Directed Search Mode**.When user clicks on this menu item, a GUI (as shown in **Figure-5.114**) shall be displayed to put NB Rx1 (0.175- 0.5GHz) in 'Directed Search' mode of operation. The GUI shall retain the previous configuration parameters entered by user.
- 5.5.4.2.12.2.1 User shall select required mode parameters such as 'Freq. Band', 'Dwell Time', Threshold', 'Polarization' and click on 'Apply' option to set them at the receiver.
- 5.5.4.2.12.2.2 User can select all the frequency bands by checking 'Select All' option on this GUI but at a time user can move only 24 frequencies for scanning.
- 5.5.4.2.12.2.3 User shall enter, if required, 'Common Dwell Time', 'Common Threshold' value to set for all the frequency bands.
- 5.5.4.2.12.2.4 Number of total frequency bands available and number of frequency bands selected by user shall be displayed on the GUI. Note, only user selected frequency bands will be scanned by the receiver and emitters falling only in those bands will be reported by

SHAKTI : UHB\Ch5 Page 256 of 614

the receiver.

- 5.5.4.2.12.2.5 User shall click on 'Save Config. to File option', to save selected receiver configuration to a file on SCD storage. A file selection GUI shall be displayed to user for entering a file name for the configuration.
- 5.5.4.2.12.2.6 User shall click on 'Load Config. From File' option, to load & display (on this GUI) previously saved configuration from a file on SCD storage. A file opening GUI shall be displayed to user for selecting a file.
- 5.5.4.2.12.2.7 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

![](_page_260_Picture_5.jpeg)

**Figure-5.114: NBRx1 Directed Search Mode GUI – ES Receivers Menu**

**5.5.4.2.12.3 NB RX1 (0.175-0.5 GHz) – Scan Mode**.When user clicks on this menu item, a GUI (as shown in **Figure-5.115**) shall be displayed to put NB Rx1 (0.175-0.5GHz) in 'Scan' mode of operation. The GUI shall retain the previous configuration parameters

SHAKTI : UHB\Ch5 Page 257 of 614

entered by user. This shall be the default mode for the receiver.

![](_page_261_Figure_2.jpeg)

**Figure-5.115: NBRx1 (0.175-0.5 GHz) Scan Mode GUI – ES Receivers Menu**

- 5.5.4.2.12.3.1 User shall select required mode parameters such as 'Dwell Time', Threshold', 'Polarization' and click on 'Apply' option to set them at the receiver. Note, all the sub-bands will be scanned by the receiver in this mode. And no individual band selection shall be allowed in this mode.
- 5.5.4.2.12.3.2 User shall enter, if required, 'Common Dwell Time', 'Common Threshold' value to set for all the frequency bands.
- 5.5.4.2.12.3.3 User shall click on 'Save Config. to File' option, to save selected receiver configuration to a file on SCD storage. A file selection GUI shall be displayed to user for entering a file name for the configuration.
- 5.5.4.2.12.3.4 User shall click on 'Load Config. From File' option, to load & display (on this GUI) previously saved configuration from a file on SCD storage. A file opening GUI shall

SHAKTI : UHB\Ch5 Page 258 of 614

be displayed to user for selecting a file.

5.5.4.2.12.3.5 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

**5.5.4.2.12.4 NB RX1 (0.175-0.5 GHz) – Mission Mode**.When user clicks on this menu item, a GUI (as shown in **Figure-5.116**) shall be displayed to put NB Rx1 (0.175-0.5GHz) in 'Mission' mode of operation. The GUI shall retain the previous configuration parameters entered by user.

![](_page_262_Figure_4.jpeg)

**Figure-5.116: NBRx1 (0.175-0.5GHz) Mission Mode GUI – ES Receivers Menu**

5.5.4.2.12.4.1 User shall select required mode parameters such as 'Dwell Time', Threshold', 'Polarization' and click on 'Apply' option to set them at the receiver. Note, the sub-bands will be selected automatically based on frequency entries in 'System Emitter Library'. And no individual band selection shall be allowed in this mode. The receiver will be scanning & reporting emitters only for these bands. The number of frequencies ('#Lib.

SHAKTI : UHB\Ch5 Page 259 of 614

Freqs') found in 'System Emitter Library' for a sub-band shall be displayed on the GUI. Maximum of 24 frequencies are required to be marked.

5.5.4.2.12.4.2 User shall enter, if required, 'Common Dwell Time', 'Common Threshold' value to set for all the frequency bands.

5.5.4.2.12.4.3 User shall click on 'Save Config. to File' option, to save selected receiver configuration to a file on SCD storage. A file selection GUI shall be displayed to user for entering a file name for the configuration.

5.5.4.2.12.4.4 User shall click on 'Load Config. From File' option, to load & display (on this GUI) previously saved configuration from a file on SCD storage. A file opening GUI shall be displayed to user for selecting a file.

5.5.4.2.12.4.5 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

**5.5.4.2.12.5 NB RX1 (0.175-0.5 GHz) – Updated Attenuation Data**.User shall login into SCD application in 'Online Mode' and SCD Main Window shall be displayed to access this GUI. User shall click on 'NB Rx1 (0.175-0.5GHz)->Update Attenuation Data' menu item from 'ES Receiver' menu and a GUI (as shown **Figure-5.117**: NBRx1 Attenuation Data Dialog) shall be displayed to update the receiver attenuation data in SCD application. The GUI shall retain the previous configuration parameters selected & applied by user.

![](_page_263_Figure_7.jpeg)

**Figure-5.117: NBRx1 Attenuation Data Dialog**

SHAKTI : UHB\Ch5 Page 260 of 614

- 5.5.4.2.12.5.1 Factory level settings (attenuation data) shall be listed in a table on the GUI, if not modified by user. Each row shall contain attenuation data for a frequency band.
- **5.5.4.2.12.6 NB RX1 (0.175-0.5 GHz) – Manage Receiver**. User shall click on this menu item and a GUI as shown in **Figure-5.118**, shall be displayed with options to block, unblock or reset NBRx1 (0.175-0.5GHz).

![](_page_264_Picture_3.jpeg)

**Figure-5.118: Manage NB Rx1 (0.175-0.5 GHz) GUI – ES Receivers Menu**

- 5.5.4.2.12.6.1 User shall check 'Block' and click on 'Apply' option to block the receiver data at ES Processor. If blocked, the receiver shall not send any PDs to ES Processor; hence no tracks will be formed by ES Processor and reported to SCD system.
- 5.5.4.2.12.6.2 User shall check 'Unblock' and click on 'Apply' option to unblock the receiver data at ES Processor. If unblocked, the receiver shall start sending (if blocked earlier) PDs to ES Processor, hence tracks will be formed by ES Processor and reported to SCD system.
- 5.5.4.2.12.6.3 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.
- **5.5.4.2.12.7 NB RX2 (0.5-18GHz) – Directed Mode**.User shall login into SCD application in 'Online Mode' and SCD Main Window shall be displayed to access this GUI. When user clicks on this menu item, a GUI (as shown in **Figure-5.119**) shall be displayed to put NB Rx2 (0.5-18GHz) in 'Directed' mode of operation. The GUI shall retain the previous configuration parameters entered by user.
- 5.5.4.2.12.7.1 User shall enter required mode parameters such as 'Frequency', 'RF Attenuation', 'IF Attenuation', 'Threshold', 'IF Band Width' & 'Scan Quadrant' and click on 'Apply' option to set them at the receiver.

SHAKTI : UHB\Ch5 Page 261 of 614

![](_page_265_Picture_1.jpeg)

**Figure-5.119: NBRx2 (0.5-18 GHz) Directed Mode**

**5.5.4.2.12.8 NB RX2 (0.5-18 GHz) – Directed Search Mode**.When user clicks on this menu item, a GUI (as shown in **Figure-5.120**) shall be displayed to put NB Rx2 (0.5-18 GHz) in 'Directed Search' mode of operation. The GUI shall retain the previous configuration parameters entered by user.

![](_page_265_Figure_4.jpeg)

**Figure-5.120: NB Rx2 Directed Search Mode GUI – ES Receivers Menu.**

SHAKTI : UHB\Ch5 Page 262 of 614

- 5.5.4.2.12.8.1 User shall select required mode parameters such as 'Freq. Band', 'Dwell Time', Threshold' and click on 'Apply' option to set them at the receiver.
- 5.5.4.2.12.8.2 User can select all the frequency bands by checking 'Select All' option on this GUI.
- 5.5.4.2.12.8.3 User shall enter, if required, 'Common Dwell Time/ High PRF (500ms), Low PRF (1000ms)', 'Common Threshold' value to set for all the frequency bands.
- 5.5.4.2.12.8.4 Number of total frequency bands available and number of frequency bands selected by user shall be displayed on the GUI. Note, only user selected frequency bands will be scanned by the receiver and emitters falling only in those bands will be reported by the receiver.
- 5.5.4.2.12.8.5 User shall click on 'Save Config. To File' option, to save selected receiver configuration to a file on SCD storage. A file selection GUI shall be displayed to user for entering a file name for the configuration.
- 5.5.4.2.12.8.6 User shall click on 'Load Config. From File' option, to load & display (on this GUI) previously saved configuration from a file on SCD storage. A file opening GUI shall be displayed to user for selecting a file.
- 5.5.4.2.12.8.7 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.
- **5.5.4.2.12.9 NB RX2 (0.5-18 GHz) – Scan Mode**.When user clicks on this menu item, a GUI (as shown in **Figure-5.121**) shall be displayed to put NB Rx2 (0.5-18GHz) in 'Scan' mode of operation. The GUI shall retain the previous configuration parameters entered by user. This shall be the default mode for the receiver.
- 5.5.4.2.12.9.1 User shall select required mode parameters such as 'Dwell Time', Threshold' and click on 'Apply' option to set them at the receiver. Note, all the sub-bands will be scanned by the receiver in this mode. And no individual band selection shall be allowed in this mode.
- 5.5.4.2.12.9.2 User shall enter, if required, 'Common Dwell Time', 'Common Threshold' value to set for all the frequency bands.
- 5.5.4.2.12.9.3 User shall click on 'Save Config. To File' option, to save selected receiver configuration to a file on SCD storage. A file selection GUI shall be displayed to user for entering a file name for the configuration.
- 5.5.4.2.12.9.4 User shall click on 'Load Config. From File' option, to load & display (on this

SHAKTI : UHB\Ch5 Page 263 of 614

GUI) previously saved configuration from a file on SCD storage. A file opening GUI shall be displayed to user for selecting a file.

5.5.4.2.12.9.5 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

|     | NBRx2 (500-18000MHz)-Scan Mode           |              |             |                   |    |  |  |  |
|-----|------------------------------------------|--------------|-------------|-------------------|----|--|--|--|
| ✓ 8 | Common <u>D</u> well Time<br>& Threshold | well Time    | ms Thresh   | old(-)            | dB |  |  |  |
|     |                                          |              |             |                   | À  |  |  |  |
|     | CenterFreq.                              | С            | wellTime    | Threshold         |    |  |  |  |
| 1   | <b>✓</b> 17750                           | 250          |             | -85               |    |  |  |  |
| 2   | <b>✓</b> 17250                           | 250          |             | -85               | ı  |  |  |  |
| 3   | √ 16750                                  | 250          |             | -85               | Ш  |  |  |  |
| 4   | <b>✓</b> 16250                           | 250          |             | -85               | ı  |  |  |  |
| 5   | ✓ 15750                                  | 250          |             | -85               | U  |  |  |  |
| 6   | ✓ 15250                                  | 250          |             | -85               |    |  |  |  |
| 7   | <b>✓</b> 14750                           | 250          |             | -85               |    |  |  |  |
| 8   | <b>✓</b> 14250                           | 250          |             | -85               |    |  |  |  |
| 9   | ✓ 13750                                  | 250          |             | -85               |    |  |  |  |
| 10  | ✓ 13250                                  | 250          |             | -85               |    |  |  |  |
| 11  | <b>✓</b> 12750                           | 250          |             | -85               |    |  |  |  |
| 12  | ✓ 12250                                  | 250          |             | -85               |    |  |  |  |
| 13  | <b>✓</b> 11750                           | 250          |             | -85               |    |  |  |  |
| 14  | ✓ 11250                                  | 250          |             | -85               | Ļ  |  |  |  |
| -   |                                          |              |             |                   | ,  |  |  |  |
| #Se | lected Bands: 37                         |              |             |                   |    |  |  |  |
| Sav | e Config. To <u>F</u> ile                | Load Config. | from File A | pply <u>C</u> anc | el |  |  |  |

**Figure-5.121: NB Rx2 (0.5-18GHz) Scan Mode GUI – ES Receivers Menu**

**5.5.4.2.12.10 NB RX2 (0.5-18GHz) – Mission Mode**.When user clicks on this menu item, a GUI (as shown in **Figure-5.122**) shall be displayed to put NB Rx2 (0.5-18GHz) in 'Mission' mode of operation. The GUI shall retain the previous configuration parameters entered by user.

5.5.4.2.12.10.1 User shall select required mode parameters such as 'Dwell Time', Threshold' and click on 'Apply' option to set them at the receiver. Note, the sub-bands will be selected automatically based on frequency entries in 'System Emitter Library'. And no individual band selection shall be allowed in this mode. The receiver will be scanning & reporting emitters only for these bands. The number of frequencies ('#Lib.Freqs') found in 'System Emitter Library' for a sub-band, shall be displayed on the GUI.

SHAKTI : UHB\Ch5 Page 264 of 614

User shall enter, if required, 'Common Dwell Time', 'Common Threshold' value to set for all the frequency bands.

5.5.4.2.12.10.2 User shall click on 'Save Config. To File' option, to save selected receiver configuration to a file on SCD storage. A file selection GUI shall be displayed to user for entering a file name for the configuration.

5.5.4.2.12.10.3 User shall click on 'Load Config. From File' option, to load & display (on this GUI) previously saved configuration from a file on SCD storage. A file opening GUI shall be displayed to user for selecting a file.

5.5.4.2.12.10.4 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

![](_page_268_Figure_5.jpeg)

**Figure-5.122: NB Rx2 (0.5-18GHz) Mission Mode GUI – ES Receivers Menu**

SHAKTI : UHB\Ch5 Page 265 of 614

**5.5.4.2.12.11 NB RX2 (0.5-18GHz) – Attenuation Data**.User shall login into SCD application in 'Online Mode' and SCD Main Window shall be displayed to access this GUI. User shall click on 'NB Rx2 (0.5-18GHz)->Update Attenuation Data' menu item from 'ES Receiver' menu and a GUI (as shown in **Figure-5.123**) shall be displayed to update the receiver attenuation data in SCD application. The GUI shall retain the previous configuration parameters selected & applied by user.

![](_page_269_Figure_2.jpeg)

**Figure-5.123: NBRx2 (0.5-18GHz) Attenuation Data Dialog**

5.5.4.2.12.11.1 Factory level settings (attenuation data) shall be listed in a table on the GUI, if not modified by user. Each row shall contain attenuation data for a frequency band.

**5.5.4.2.12.12 NB RX2 (0.5-18GHz) – Manage Receiver**.User shall click on this menu item and a GUI as shown in **Figure-5.124**, shall be displayed with options to block, unblock or reset NBRx2 (0.5-18GHz).

![](_page_269_Picture_6.jpeg)

**Figure-5.124: Manage NB Rx2 (0.5-18GHz) GUI – ES Receivers Menu**

SHAKTI : UHB\Ch5 Page 266 of 614

- (a) **Block**. User shall check 'Block' and click on 'Apply' option to block the receiver data at ES Processor. If blocked, the receiver shall not send any PDs to ES Processor; hence no tracks will be formed by ES Processor and reported to SCD system.
- (b) **Un-Block**. User shall check 'Un-Block' and click on 'Apply' option to unblock the receiver data at ES Processor. If unblocked, the receiver shall start sending (if blocked earlier) PDs to ES Processor, hence tracks will be formed by ES Processor and reported to SCD system.
- (c) User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.
- **5.5.4.2.12.13 NB RX2 (0.5-18 GHz) – Calibration Mode**.User shall click on this menu item and a GUI as shown in **Figure-5.125**, shall be displayed with Calibration On / Off options. This is an Administrative level command. When Calibration is On, NBRx2 will go in calibration mode and NBRx2 link with ESMP will be disconnected. In this mode, calibration programming will be done in digital boards (RIB, RPU, RPB, Quad superhet. and etc). When operator selects Calibration Off, NBRx2 will in calibration off mode and NBRx2 link with ESMP will be connected.

![](_page_270_Picture_5.jpeg)

**Figure-5.125: Calibration Mode (NBRx2 (0.5-18GHz)**

- **5.5.4.2.12.14 BB RX1 (2.2-18GHz) – SFB Selection**. When user clicks on this menu item, a GUI (as shown in Figure-5.126) shall be displayed to select SFB (Switch Filter Bank) at BB Rx1 (2.2-18GHz). The GUI shall retain the previous configuration parameters entered by user.
- 5.5.4.2.12.14.1 User shall select an SFB (1, 2, 3 or 4), enter 'Threshold' value and click on 'Apply' option to set them at the receiver.
- 5.5.4.2.12.14.2 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

SHAKTI : UHB\Ch5 Page 267 of 614

![](_page_271_Picture_1.jpeg)

**Figure-5.126: BB Rx1 (2.2-18GHz) SFB Select GUI – ES Receivers Menu.**

**5.5.4.2.12.15 BB RX1 (2.2-18GHz) – Raw PD Mode (Specific to OEM)**.User shall login into SCD application in 'Online Mode' and SCD Main Window shall be displayed to access this GUI. User shall click on 'BB Rx1 (2.2-18GHz)->Raw PD Mode' menu item from 'ES Receiver' menu and a GUI (as shown in **Figure-5.127**) shall be displayed to enable/ disable raw PD mode at BB Rx1 (2.2-18GHz). The GUI shall retain the previous configuration parameters selected & applied by user.

![](_page_271_Picture_4.jpeg)

**Figure-5.127: BBRx1 (2.2-18GHz) Raw PD Mode**

SHAKTI : UHB\Ch5 Page 268 of 614

5.5.4.2.12.15.1 User shall select 'Enable' option, select 'Scan Quadrant' and click on 'Apply' option to enable raw PD mode at the receiver.

5.5.4.2.12.15.2 User shall select 'Disable' and click on 'Apply' option to disable raw PD mode at the receiver.

**Note: Enabling raw PD mode may change the current configuration at the receiver, hence user shall ensure to disable raw PD mode manually**.

5.5.4.2.12.15.3 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

**5.5.4.2.12.16 BB RX1 (2.2-18GHz) – Calibration Mode(Specific to OEM)**.User shall login into SCD application in 'Online Mode' and SCD Main Window shall be displayed to access this GUI. User shall click on 'BB Rx1 (2.2-18GHz)->Calibration' menu item from 'ES Receiver' menu and a GUI (as shown in **Figure-5.128**) shall be displayed to enable/ disable calibration at BB Rx1 (2.2-18GHz). The GUI shall retain the previous configuration parameters selected & applied by user.

![](_page_272_Picture_6.jpeg)

**Figure-5.128: BBRx1 (2.2-18 GHz) Calibration Mode Dialog**

5.5.4.2.12.16.1 User shall select 'Enable' option, check 'Frequency Calibration', 'Amplitude

SHAKTI : UHB\Ch5 Page 269 of 614

Calibration', 'Channel Calibration' or all of them, 'select 'Scan Quadrant' and click on 'Apply' option to set selected calibration at the receiver.

5.5.4.2.12.16.2 User shall select 'Disable' and click on 'Apply' option to disable calibration mode at the receiver.

**Note**: **Enabling calibration may change the current configuration at the receiver, hence user shall ensure to disable calibration manually.**

5.5.4.2.12.16.3 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

**5.5.4.2.12.17 BB RX1 (2.2-18GHz) – SFB Selection for RFPS**.When user clicks on this menu item, a GUI (as shown in **Figure-5.129**) shall be displayed to select SFB (Switch Filter Bank) at Omni BB Rx1 (2.2-18 GHz). The GUI shall retain the previous configuration parameters entered by user.

![](_page_273_Picture_6.jpeg)

**Figure-5.129: Omni BB Rx1 (2.2-18 GHz) SFB**

5.5.4.2.12.17.1 User shall select an SFB (1, 2, 3 or 4) and click on 'Apply' option to set them at the omni receiver.

5.5.4.2.12.17.2 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

**5.5.4.2.12.18 BB RX1 (2.2-18GHz) – Manage Receiver**.User shall click on this menu item and a GUI as shown in **Figure-5.130**, shall be displayed with options to block, unblock

SHAKTI : UHB\Ch5 Page 270 of 614

or reset BBRx1 (2.2-18 GHz).

![](_page_274_Picture_2.jpeg)

**Figure-5.130: Manage BB Rx1 (2.2-18GHz) GUI – ES Receivers Menu.**

- (a) **Block**. User shall check 'Block' and click on 'Apply' option to block the receiver data at ES Processor. If blocked, the receiver shall not send any PDs to ES Processor; hence no tracks will be formed by ES Processor and reported to SCD system.
- (b) **Un-Block**. User shall check 'Un-Block' and click on 'Apply' option to unblock the receiver data at ES Processor. If unblocked, the receiver shall start sending (if blocked earlier) PDs to ES Processor, hence tracks will be formed by ES Processor and reported to SCD system.
- 5.5.4.2.12.18.1 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.
- **5.5.4.2.12.19 BB RX2 (18-40GHz) – Broad Band Mode**.User shall click on this menu item to put BBRx2 (18-40GHz) in 'Broad Band (BB) Mode'. A confirmation GUI (as shown in **Figure-5.131**) shall be displayed.

![](_page_274_Picture_8.jpeg)

**Figure-5.131: Confirmation GUI to Put BBRx2 in BB Mode – ES Receivers Menu**

**5.5.4.2.12.20 BB RX2 (18-40GHz) – Raw PD Mode**.User shall login into SCD application in 'Online Mode' and SCD Main Window shall be displayed to access this GUI. User shall click on 'BB Rx2 (18-40GHz)->Raw PD Mode' menu item from 'ES Receiver' menu and a GUI (as shown in **Figure-5.132**) shall be displayed to enable/ disable raw PD mode at BB Rx2 (18-40GHz). The GUI shall retain the previous configuration parameters selected & applied by user.

SHAKTI : UHB\Ch5 Page 271 of 614

![](_page_275_Picture_1.jpeg)

**Figure-5.132: BBRx2 (18-40 GHz) Raw PD Mode**

5.5.4.2.12.20.1 User shall select 'Enable' option, select 'Scan Quadrant' and click on 'Apply' option to enable raw PD mode at the receiver.

5.5.4.2.12.20.2 User shall select 'Disable' and click on 'Apply' option to disable raw PD mode at the receiver.

**Note: Enabling raw PD mode may change the current configuration at the receiver, hence user shall ensure to disable raw PD mode manually.**

5.5.4.2.12.20.3 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

**5.5.4.2.12.21 BB RX2 (18-40GHz) – Calibration Mode**.User shall login into SCD application in 'Online Mode' and SCD Main Window shall be displayed to access this GUI. User shall click on 'BB Rx2 (18-40GHz)->Calibration' menu item from 'ES Receiver' menu and a GUI (as shown in **Figure-5.133**) shall be displayed to enable/ disable calibration at BB Rx2 (18-40GHz). The GUI shall retain the previous configuration parameters selected & applied by user.

5.5.4.2.12.21.1 User shall select 'Enable' option, check 'Frequency Calibration', 'Amplitude Calibration', 'Channel Calibration' or all of them, 'select 'Scan Quadrant' and click on 'Apply' option to set selected calibration at the receiver.

5.5.4.2.12.21.2 User shall select 'Disable' and click on 'Apply' option to disable calibration mode at the receiver.

SHAKTI : UHB\Ch5 Page 272 of 614

**Note: Enabling calibration may change the current configuration at the receiver, hence user shall ensure to disable calibration manually.**

![](_page_276_Picture_2.jpeg)

**Figure-5.133: BBRx2 (18-40 GHz) Calibration Dialog**

5.5.4.2.12.21.3 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

**5.5.4.2.12.22 BB RX2 (18-40GHz) – Manage Receiver**.User shall click on this menu item and a GUI as shown in **Figure-5.134**, shall be displayed with options to block, unblock or reset the receiver.

![](_page_276_Picture_6.jpeg)

**Figure-5.134: Manage Receiver GUI BB Rx2 (18-40GHz) – ES Receivers Menu**

SHAKTI : UHB\Ch5 Page 273 of 614

- (a) **Block**. User shall check 'Block' and click on 'Apply' option to block the receiver data at ES Processor. If blocked, the receiver shall not send any PDs to ES Processor; hence no tracks will be formed by ES Processor and reported to SCD system.
- (b) **Unblock**. User shall check 'UnBlock' and click on 'Apply' option to unblock the receiver data at ES Processor. If unblocked, the receiver shall start sending (if blocked earlier) PDs to ES Processor, hence tracks will be formed by ES Processor and reported to SCD system.
- 5.5.4.2.12.22.1 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.
- **5.5.4.2.12.23 BB RX2 (18-40GHz) – Set Threshold**.User shall click on this menu item and a GUI as shown in **Figure-5.135**, shall be displayed with receiver threshold. Default threshold value will be –55 dBm. Range will be from 0 to -55 dBm.

![](_page_277_Picture_5.jpeg)

**Figure-5.135: BB RX2 (18-40GHz) – Set Threshold Menu**

- **5.5.4.2.13 EA System Menu**.'EA System' menu (as shown in **Figure-5.136**) shall include GUI controls for configuring & controlling EA Processor, EA transmitters, ECM operations (track & jam etc.,) from SCD application.
- 5.5.4.2.13.a The following sections describe the menu items available under this menu.

SHAKTI : UHB\Ch5 Page 274 of 614

![](_page_278_Picture_1.jpeg)

**Figure-5.136: EA System Menu – SCD Main Window.**

**5.5.4.2.13.1 Semi Auto Mode – Track**.User shall click on this menu item to 'Track' selected emitter (s) at EA system (Processor). A GUI (as shown in **Figure-5.137**) shall be displayed to user for selecting emitter & JPRO number (Jammer Program). In 'Semi-Auto' mode, user can perform ECM related operations only on emitters intercepted by ES Processor.

![](_page_278_Picture_4.jpeg)

**Figure-5.137: GUI to Track Emitter in Semi-Auto Mode – EA Processor Menu**

SHAKTI : UHB\Ch5 Page 275 of 614

5.5.4.2.13.1.1 User shall select 'Emitter No.' select a jam technique & its associated parameters from 'Technique Selection' GUI, select 'Technique Duration' and click on 'Apply' to perform 'Track' operation at EA Processor. Jamming techniques shall be grouped logically on the GUI for easy appreciation by user as mentioned below:

#### (a) **Noise Based**:

- (i) DRFM Barrage.
- (ii) DRFM Spot Noise.
- (iii) DTO Spot.
- (iv) DTO Barrage.
- (v) Multi Spot Noise.
- (vi) Doppler Noise.

#### (b) **Deception Based**:

- (i) Range Gate Pull Off (RGPO).
- (ii) Range Gate Pull In (RGPI).
- (iii) Velocity Gate Pull Off (VGPO).
- (iv) Velocity Gate Pull In(VGPI).
- (v) Sync. Velocity Receding.
- (vi) Sync. Velocity Approaching.

#### (c) **False Targets**:

- (i) Range False Targets.
- (ii) Velocity False Targets.

#### (d) **Angle Deception**:

- (i) Blink.
- (ii) SRM.
- (iii) SSRM.
- (iv) None.
- 5.5.4.2.13.1.2 This grouping shall be followed in other (wherever required) GUIs under EA Menu.
- 5.5.4.2.13.1.2 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

SHAKTI : UHB\Ch5 Page 276 of 614

**5.5.4.2.13.2 Semi Auto Mode – Jam**.User shall click on this menu item to 'Jam' emitters which were already under tracking at EA Processor. A GUI (as shown in **Figure-5.138**) shall be displayed to user for selecting emitter & jam duration.

![](_page_280_Picture_2.jpeg)

**Figure-5.138: GUI to Jam Emitter – EA Processor Menu**

- 5.5.4.2.13.2.1 There shall be option to select more than one emitter to a list on the GUI and perform 'Jam' operation on them.
- 5.5.4.2.13.2.2 User shall check 'All Emitters' option to add all the emitters to the list on the GUI, and click on 'Apply' option to jam the emitters at EA system.
- 5.5.4.2.13.2.3 User can select a single emitter by checking on 'Selected Emitter', select 'Emitter No.' and click on 'Add to List' option to add it to a list of emitters. User shall repeat this procedure to select other emitters (maximum 10 emitters) to the list and when finished, enter 'Jam Duration' value and click on 'Apply' option.
- 5.5.4.2.13.2.3 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.
- **5.5.4.2.13.3 Semi Auto Mode – Track& Jam**.User shall click on this menu item to 'Track & Jam' selected emitter (s) at EA Processor (EA System). A GUI (as shown in **Figure-5.139**) shall be displayed to user for selecting emitter, JPRO number (Jammer Program) & jam duration. In 'Semi-Auto' mode, user can perform ECM related operations

SHAKTI : UHB\Ch5 Page 277 of 614

only on emitters intercepted by ES Processor.

![](_page_281_Picture_2.jpeg)

**Figure-5.139: GUI to Track & Jam Emitter in Semi-Auto Mode – EA Processor Menu**

- 5.5.4.2.13.3.1 User shall select 'Emitter No.', select a jam technique & its associated parameters from 'Technique Selection' GUI, select 'Technique Duration', select 'Jam Duration' and click on 'Apply' option to perform 'Track & Jam' operation at EA Processor.
- 5.5.4.2.13.3.2 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.
- **5.5.4.2.13.4 Semi Auto Mode – Stop Jam**.User shall click on this menu item to 'Stop Jam' emitters which were already jammed by EA Processor. A GUI (as shown in **Figure-5.140)** shall be displayed to user for selecting emitters.
- 5.5.4.2.13.4.1 There shall be option to select more than one emitter to a list on the GUI and perform 'Stop Jam' operation on them.
- 5.5.4.2.13.4.2 User shall check 'All Emitters' option to add all the emitters to the list on the GUI, and click on 'Apply' option to 'Stop Jam' the emitters at EA system.
- 5.5.4.2.13.4.3 User can select a single emitter by checking on 'Selected Emitter', select 'Emitter No.' and click on 'Add to List' option to add it to a list of emitters. User shall repeat this procedure to select other emitters (maximum 10 emitters) to the list and when finished, click on 'Apply' option.

SHAKTI : UHB\Ch5 Page 278 of 614

5.5.4.2.13.4.4 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

![](_page_282_Picture_2.jpeg)

**Figure-5.140: GUI to Stop Jam – EA Processor Menu**

- **5.5.4.2.13.5 Semi Auto Mode – Break Track**.User shall click on this menu item to 'Break Track' emitters which were already handled (track/ track & jam) by EA Processor. A GUI (as shown in **Figure-5.141**) shall be displayed to user for selecting emitters.
- 5.5.4.2.13.5.1 There shall be option to select more than one emitter to a list on the GUI and perform 'Break Track' operation on them.
- 5.5.4.2.13.5.2 User shall check 'All Emitters' option to add all the emitters to the list on the GUI, and click on 'Apply' option to 'Break Track' the emitters at EA system.
- 5.5.4.2.13.5.3 User can select a single emitter by checking on 'Selected Emitter', select 'Emitter No.' and click on 'Add to List' option to add it to a list of emitters. User shall repeat this procedure to select other emitters (maximum 10 emitters) to the list and when finished, click on 'Apply' option.
- 5.5.4.2.13.5.4 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

SHAKTI : UHB\Ch5 Page 279 of 614

![](_page_283_Picture_1.jpeg)

**Figure-5.141: GUI to Break Track Emitter – EA Processor Menu.**

- **5.5.4.2.13.6 Semi Auto Mode – Modify Jamming Technique**.User shall click on this menu item to modify jamming technique of an emitter which was already handled (track/ track & jam) by EA Processor in 'Semi-Auto' mode. A GUI shall be (as shown in **Figure-5.142**) displayed to user for selecting an emitter.
- 5.5.4.2.13.6.1 User shall check 'All Emitters' option and click on 'Apply' option to 'Modify Jamming Technique' at EA system.
- 5.5.4.2.13.6.2 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window

SHAKTI : UHB\Ch5 Page 280 of 614

![](_page_284_Picture_1.jpeg)

**Figure-5.142: GUI to Modify Jamming Technique – EA Processor Menu**

**5.5.4.2.13.7 Manual Mode – Track**.User shall click on this menu item to 'Track' an emitter at the EA Processor in manual mode. A GUI (as shown in **Figure-5.143**) shall be displayed to user for entering emitter details manually on the GUI. No emitter details will be provided by ES Processor for EA Processor in manual mode.

5.5.4.2.13.7.1 User shall select 'Emitter No.' and enter other emitter parameters such as 'Frequency', 'DOA', 'PW', 'PRF', 'Signal Type' etc., select a jam technique & its associated parameters from 'Technique Selection', select 'Technique Duration' and click on 'Apply' option to perform 'Track' operation at EA Processor.

5.5.4.2.13.7.2 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

SHAKTI : UHB\Ch5 Page 281 of 614

![](_page_285_Picture_1.jpeg)

**Figure-5.143: GUI to Track Emitter in Manual Mode – EA Processor Menu**

- **5.5.4.2.13.8 Manual Mode – Jam Track**.Refer section '5.5.4.2.28 Semi-Auto Mode- >Jam'.
- **5.5.4.2.13.9 Manual Mode – Track & Jam**. User shall click on this menu item to 'Track & Jam' an emitter at EA Processor (EA System) in manual mode. A GUI (as shown in **Figure-5.144**) shall be displayed to user for entering emitter details manually on the GUI. No emitter details will be provided by ES Processor for EA Processor in manual mode.
- 5.5.4.2.13.9.1 User shall select 'Emitter No.' and enter other emitter parameters such as 'Frequency', 'DOA', 'PW', 'PRF', 'Signal Type' etc., select a jam technique & its associated parameters from 'Technique Selection', select 'Technique Duration', 'Jam Duration' and click on 'Apply' option to perform 'Track' operation at EA Processor.

SHAKTI : UHB\Ch5 Page 282 of 614

5.5.4.2.13.9.2 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

![](_page_286_Picture_2.jpeg)

**Figure-5.144: GUI to Track & Jam Emitter in Manual Mode – EA Processor Menu**

- **5.5.4.2.13.10 Manual Mode – Stop Jam**.Refer section '5.5.4.2.28.2 Semi-Auto Mode->Stop Jam'.
- **5.5.4.2.13.11 Manual Mode – Break Track**.Refer section '5.5.4.2.28.2 Semi-Auto Mode->Break Track'.
- **5.5.4.2.13.12 Manual Mode – Update Track Information**.User shall click on this menu item to update parameters of emitter that is handled (track/ track & jam) by EA Processor in 'Manual' mode. A GUI (as shown in **Figure-5.145**) shall be displayed to user for modifying emitter details manually on the GUI. No emitter details will be provided by ES

SHAKTI : UHB\Ch5 Page 283 of 614

Processor for EA Processor in manual mode.

![](_page_287_Picture_2.jpeg)

**Figure-5.145: GUI to Update Track Info in Manual Mode – EA Processor Menu**

- 5.5.4.2.13.12.1 User shall check only required emitter parameters which are to be updated at EA system.
- 5.5.4.2.13.12.2 User shall select 'Emitter No.' and update the required emitter parameters such as 'Frequency', 'DOA', 'Elevation', 'Scan Type' 'Threat Level', 'PW', 'PRF' and etc., select a jpro. technique & its associated parameters and click on 'Apply' option.
- 5.5.4.2.13.12.3 Click 'Modify' option to change JPRO number.
- 5.5.4.2.13.12.4 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.
- **5.5.4.2.13.13 Power On/Off Transmitter**.User shall click on this menu item & a GUI (as shown in **Figure-5.146**) shall be displayed to set status of EA transmitter (s) to 'On/ Off' from SCD application. By default, EA transmitters will be in 'Off' state.
- 5.5.4.2.13.13.1 User shall select 'On' or 'Off' option for EA transmitter on Port & Starboard side of the Platform and click on 'Apply' option to switch it 'On' or 'Off'.

SHAKTI : UHB\Ch5 Page 284 of 614

5.5.4.2.13.13.2 User can set all EA transmitters on Port & Starboard side to 'On/ Off' state by selecting 'On/ Off' in 'All Port Side Tx' & 'All Starboard Side Tx' option.

5.5.4.2.13.13.3 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

![](_page_288_Picture_3.jpeg)

**Figure-5.146: GUI to On/ Off EA Transmitter – EA Processor Menu**

**5.5.4.2.13.14 High Voltage On/ Off**. User shall click on this menu item & a GUI (as shown in **Figure-5.147**) shall be displayed to set 'High Voltage' (HV) state of EA transmitter (s) to 'On/ Off' from SCD application. By default EA HV will be in 'Off' state at EA transmitters.

![](_page_288_Picture_6.jpeg)

**Figure-5.147: GUI to on/ Off High Voltage of EA Transmitter – EA Processor Menu**

5.5.4.2.13.14.1 User shall select 'On' or 'Off' option for EA transmitter on Port & Starboard side of the Platform and click on 'Apply' option to set HV to 'On' or 'Off' state.

5.5.4.2.13.14.2 User can set HV of all EA transmitters on Port & Starboard side to 'On/ Off' state by selecting 'On/ Off' in 'All Port Side Tx' & 'All Starboard Side Tx' option.

5.5.4.2.13.14.3 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

SHAKTI : UHB\Ch5 Page 285 of 614

**5.5.4.2.13.15 Select ERP**.User shall click on this menu item & a GUI (as shown in **Figure-5.148**) shall be displayed to select ERP (Effective Radiation Power) EA transmitter (s) from SCD application. By default 50KW ERP shall be selected for both the transmitters on Port & Starboard side.

![](_page_289_Picture_2.jpeg)

**Figure-5.148: GUI to Select ERP of EA Transmitter – EA Processor Menu**

5.5.4.2.13.15.1 User shall select ERP value (50KW, 25KW or 10KW) and click on 'Apply' option to set at EA transmitter.

5.5.4.2.13.15.2 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

**5.5.4.2.13.16 Reset Transmitter**.User shall click on this menu item & a GUI (as shown in **Figure-5.149**) shall be displayed to reset EA transmitters from SCD application. This command is for resetting/ clearing the fault (if any) of the transmitter.

![](_page_289_Picture_7.jpeg)

**Figure-5.149: GUI to Reset EA Transmitter – EA Processor Menu**

5.5.4.2.13.16.1 User shall select 'RESET/ NO RESET' option for EA transmitter on Port & Starboard side of the Platform and click on 'Apply' option to make it effective at EA Processor.

SHAKTI : UHB\Ch5 Page 286 of 614

5.5.4.2.13.16.2 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

**5.5.4.2.13.17 Set Servo Position**. User shall click on this menu item & a GUI (as shown in **Figure-5.150**) shall be displayed to set servo position of EA system from SCD application.

![](_page_290_Picture_3.jpeg)

**Figure-5.150: GUI to Set EA Servo Position – EA Processor Menu**

5.5.4.2.13.17.1 User shall enter servo angle for EA transmitter on Port & Starboard side of the Platform and click on 'Apply' option to make it effective at EA Processor.

5.5.4.2.13.17.2 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

**5.5.4.2.13.18 Show EA Link & Status**.User shall click on this menu item & a GUI (as shown in **Figure-5.151**) shall be displayed with link & self-test status of EA system.

5.5.4.2.13.18.1 Judicious colour codes shall be used to represent the status. User shall click on the 'Legend' option to see the colour codes and see the link type notation as shown in **Figure-5.152**.

5.5.4.2.13.18.2 User shall click on 'Close' option to exit from the GUI.

SHAKTI : UHB\Ch5 Page 287 of 614

![](_page_291_Picture_1.jpeg)

**Figure-5.151: EA Link & Self-Test Status GUI – EA Processor Menu**

![](_page_291_Picture_3.jpeg)

**Figure-5.152: EA Link & Self-Test Status Legend GUI – EA Processor Menu.**

**5.5.4.2.13.19 Set Forbidden Frequency Bands**.User shall click on this menu item to view existing forbidden frequency bands or set new ones at EA Processor. A GUI (as shown in **Figure-5.153**) containing frequency bands shall be displayed. The emitters falling

SHAKTI : UHB\Ch5 Page 288 of 614

within forbidden frequency bands will not be engaged by EA system.

![](_page_292_Picture_2.jpeg)

**Figure-5.153: GUI to Set Forbidden Frequency Bands – EA Processor Menu.**

5.5.4.2.13.19.a User shall check 'Spectrum Band', 'Receiver Band' or 'Custom Band' option to select a forbidden frequency band and click on 'Apply' option to enforce it at EA Processor. If successful, the forbidden band region in 'EW Activity Window' & 'Situational Display' shall be painted in 'Red' colour (transparent) as shown in **Figure-5.154**.

5.5.4.2.13.19.b User shall click on 'Reset' option to remove any existing forbidden frequency bands at EA Processor, thereby allowing EA Processor to 'Track/ Track & Jam' emitters within those bands again. Forbidden region (red) shall be removed from display, if reset is successfully.

5.5.4.2.13.19.c User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

SHAKTI : UHB\Ch5 Page 289 of 614

![](_page_293_Figure_1.jpeg)

**Figure-5.154: Situational Display GUI with Forbidden Frequency Bands Applied**

**5.5.4.2.13.20 Set Forbidden Sectors**. User shall click on this menu item to view existing forbidden sectors or set new ones at EA Processor. A GUI containing sectors (as shown in **Figure-5.155**) shall be displayed. The emitters falling within forbidden sectors will not be engaged by EA system.

5.5.4.2.13.20.1 User shall check 'Sector' or 'Sector Range' option to select a forbidden sector and click on 'Apply' option to enforce it at EA Processor. If successful, the forbidden sector region in 'Tactical Display' & 'Situational Display' shall be painted in 'Red' colour (transparent) as shown in **Figure-5.156**.

5.5.4.2.13.20.2 User shall click on 'Reset' option to remove any existing forbidden sectors at EA Processor, thereby allowing EA Processor to 'Track/ Track & Jam' emitters within those sectors again. Forbidden region (red) shall be removed from display, if reset is successfully.

5.5.4.2.13.20.3 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

SHAKTI : UHB\Ch5 Page 290 of 614

![](_page_294_Figure_1.jpeg)

Figure-5.155: GUI to Set Forbidden Sectors – EA Processor Menu.

SHAKTI: UHB\Ch5 Page 291 of 614

![](_page_295_Figure_1.jpeg)

**Figure-5.156: Tactical Display GUI with Forbidden Sectors Applied.**

**5.5.4.2.13.21 Reset**.User shall click on this menu item to reset EA Processor. Resetting EA system will force EA Processor to 'Break Track' all the emitters (if any handled by EA) and reset EA Processor to its default configuration". Hence, user shall be aware of the operation and use it only when necessary. A confirmation GUI, as shown in **Figure-5.157**, shall be displayed to user.

![](_page_295_Figure_4.jpeg)

**Figure-5.157: Confirmation GUI to Reset EA Processor – ES Processor Menu**

**5.5.4.2.14 RFPS Menu**.RFPS menu (as shown in **Figure-5.158**) shall include GUI controls for finger printing/ recording a selected track at RFPS, set 'Auto RFPS' settings etc., from SCD application.

SHAKTI : UHB\Ch5 Page 292 of 614

The following sections describe the menu items available under this menu.

![](_page_296_Picture_2.jpeg)

**Figure-5.158: RFPS Menu – SCD Main Window**

**5.5.4.2.14.1 Finger Prints Track**.User shall click on this menu item to perform radar finger printing on selected track. A confirmation GUI, as shown in **Figure-5.159**, shall be displayed to user. User shall select 'Yes' option to perform radar finger printing at RFPS and show results (if received any) for the same in 'Manual RFPS Results' Window, as shown in **Figure-5.160**.

![](_page_296_Picture_5.jpeg)

**Figure-5.159: Confirmation GUI for Radar Finger Printing – RFPS Menu**

![](_page_296_Picture_7.jpeg)

**Figure-5.160: Manual RFPS Results Window GUI – RFPS Menu**

**5.5.4.2.14.2 Fingerprint Track with DRTG**.User shall click on this menu item and a GUI as shown in **Figure-5.161**, shall be displayed with DRTG configurable parameters (DOA, Frequency and Pulse Width) and with selectable window size.

5.5.4.2.14.2.1 In a dense environment, Finger printing of selected Emitter from SCD main window will not capture pulses accurately for the given parameters. In this case, Finger Print with DRTG command will be issued to RPU for generating DRTG signal to the WBT of RFPS system and Omni BBRx will be captured at RFPS system and displayed to the

SHAKTI : UHB\Ch5 Page 293 of 614

RFPS main window.

![](_page_297_Picture_2.jpeg)

**Figure-5.161: DRTG-RFPS Menu**

**5.5.4.2.14.3 Record Data at RFPS**.User shall click on this menu item to capture & record finger print data for a selected track at RFPS. A confirmation GUI, as shown in **Figure-5.162**, shall be displayed to user. User shall select 'Yes' option to start recording data.

![](_page_297_Picture_5.jpeg)

**Figure-5.162: Confirmation GUI to Record Data at RFPS – RFPS Menu**

- **5.5.4.2.14.4 Reset Auto RFPS Tracks**.User shall click on this menu item to reset (or remove) the existing (if any) emitters in 'Auto RFPS' queue. A GUI as shown in **Figure-5.163**, shall be displayed to user to select track numbers.
- 5.5.4.2.14.4.1 User shall select 'Track No.', click 'Add to List' option to add to list on the GUI. User shall repeat this procedure to select other tracks of interest and when finished, click on 'Delete at RFPS' option shall be clicked.
- 5.5.4.2.14.4.2 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

SHAKTI : UHB\Ch5 Page 294 of 614

![](_page_298_Picture_1.jpeg)

**Figure-5.163: GUI to Reset Auto RFPS Tracks at RFPS – RFPS Menu.**

**5.5.4.2.14.5 Auto RFPS Setting**. User shall click on this menu item to view/ modify 'Auto RFPS' settings enforced in SCD application. A GUI, as shown in **Figure-5.164**, shall be displayed to user to select emitter parameters for which 'Auto RFPS' is to be performed.

5.5.4.2.14.5.1 User shall check 'Enable Auto RFPS' and select 'Frequency Min', 'Frequency Max', 'Signal Type', 'Track Type', 'PW Min', 'PW Max', 'PRI Min', 'PRI Max' values and click on 'Apply' option to enforce these parameters in SCD application. Note: SCD application shall send the emitters (which fall within the range of user selected parameters) to RFPS for finger print automatically in the background, without user intervention.

5.5.4.2.14.5.2 Auto RFPS' results (if received any) for the same, shall be displayed in 'Auto RFPS Results' Window GUI, as shown in **Figure-5.165**.

SHAKTI : UHB\Ch5 Page 295 of 614

![](_page_299_Picture_1.jpeg)

**Figure-5.164: Auto RFPS Settings GUI – RFPS Menu**

![](_page_299_Picture_3.jpeg)

**Figure-5.165: Auto RFPS Results Window GUI – RFPS Menu**

5.5.4.2.14.5.3 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

**5.5.4.2.14.6 Shutdown RFPS**.User shall click on this menu item to shutdown (or power off) RFPS computer from the SCD application. A confirmation GUI, as shown in **Figure-5.166**, shall be displayed to user. User shall select 'Yes' option to shutdown RFPS computer.

SHAKTI : UHB\Ch5 Page 296 of 614

![](_page_300_Picture_1.jpeg)

**Figure-5.166: Confirmation GUI to Shutdown RFPS – RFPS Menu**

**5.5.4.2.15 CMS Menu**. CMS menu (as shown in **Figure-5.167**) shall include GUI controls for sending a track to CMS, sending text message to CMS operator etc., from SCD application.

**Note: This menu shall be enabled only in 'Integrated Mode' of SCD operation. The following sections describe the menu items available under this menu.**

![](_page_300_Picture_5.jpeg)

**Figure-5.167: CMS Menu – SCD Main Window**

**5.5.4.2.15.1 Send Track to CMS**.User shall click on this menu item to send a track of interest to CMS. A confirmation GUI, as shown in **Figure-5.168**, shall be displayed to user. User shall select 'Yes' option to send the track and the status of the same shall be updated in 'Emitter Report Window' GUI, as shown in **Figure-5.169**. If successful, letter 'NC' will be displayed in 'Status' field.

![](_page_300_Picture_8.jpeg)

**Figure-5.168: Confirmation GUI to Send Track to CMS – CMS Menu**

![](_page_300_Picture_10.jpeg)

**Figure-5.169: GUI for CMS Track Status in Tabular Display – SCD Main Window**

SHAKTI : UHB\Ch5 Page 297 of 614

5.5.4.2.15.1.1 To send track to CMS, if track number is not selected by user an information popup shall be displayed as shown below **Figure-5.170**.

![](_page_301_Picture_2.jpeg)

**Figure-5.170: Information regarding Send Track to CMS**

**5.5.4.2.15.2 Send Text Message to CMS**.User shall click on this menu item to send a short text message to CMS operation. A GUI, as shown in **Figure-5.171**, shall be displayed to user to enter text and send. This feature will be helpful for the users of the EW system and CMS to communicate with each other while handing over and taking over control of the EW system to perform EW operations.

![](_page_301_Picture_5.jpeg)

**Figure-5.171: Confirmation GUI to Send Track to CMS – CMS Menu**

5.5.4.2.15.2.1 User shall enter text message in 'line edit' field and click on 'Send to CMS' option. The status of the messages exchanged shall be displayed in a list on the GUI.

5.5.4.2.15.2.2 User shall click on 'Close' option to exit from this GUI and go to SCD Main Window.

**5.5.4.2.15.3 Switch to Standalone Mode**.User shall click on this menu item to send

SHAKTI : UHB\Ch5 Page 298 of 614

a request to CMS operator to release control of EW system and put it back into 'Standalone' mode. A confirmation GUI, as shown in **Figure-5.172**, shall be displayed to user.

![](_page_302_Picture_2.jpeg)

**Figure-5.172: Confirmation GUI to Switch to Standalone Mode – CMS Menu**

5.5.4.2.15.3.1 'Standalone' text will be displayed in 'Status Bar' of SCD GUI (bottom right corner). The track data, if any, will not be reported to CMS. Also, the colour of link status between CMS & SCD will turn to yellow from green.

5.5.4.2.15.3.2 CMS operator sends a request to EW system, change to integrated mode; SCD GUI will be switched to 'Integrated Mode'. 'Integrated' text will be displayed in 'Status Bar' of SCD GUI (bottom right corner). The track data if any will be reported to CMS and the same can be seen in CMS GUI. Also, the colour of link status between CMS & SCD will turn to green from yellow.

**5.5.4.2.15.4 Send 'Purge Track Request' to CMS**.User shall click on this menu item to send a request to CMS operator purge passive tracks at ES Processor from CMS console. A GUI, as shown in **Figure-5.173**, shall be displayed to user to select a passive track.

5.5.4.2.15.4.1 User shall select existing passive tracks and click on 'Send Purge Request' option to send the request to CMS operator. If accepted, selected passive tracks will be removed from emitter presentation windows in SCD Main Window.

![](_page_302_Picture_8.jpeg)

**Figure-5.173: GUI to Send 'Purge Passive Tracks' Request to CMS – CMS Menu**

**5.5.4.2.15.5 Send 'Reset Tracks' to CMS**. User shall click on this menu item to send a request to CMS operator reset tracks at ES Processor from CMS console. A confirmation GUI, as shown in **Figure-5.174**, shall be displayed to user. User shall select

SHAKTI : UHB\Ch5 Page 299 of 614

'Yes' option to reset ES Processor.

5.5.4.2.15.5.1 If 'Reset Tracks' request message is accepted by CMS user and if the command is executed successfully, then all the tracks at ES Processor will be removed & emitter presentation windows in SCD Main Window will be cleared.

5.5.4.2.15.5.2 "Note: Resetting ES Processor will remove all the existing tracks/ PDs and ES Processor will start rebuilding tracks afresh". Hence, user shall be aware of the operation and use it only when necessary. If ES Processor is reset successfully, all the tracks shall be removed from emitter presentation windows in SCD Main Window.

![](_page_303_Picture_4.jpeg)

**Figure-5.174: GUI to Send 'Reset Tracks' Request to CMS**

**5.5.4.2.16 LRSAM Menu.** LRSAM menu (as shown in **Figure-5.175**) shall include GUI controls for sending a track to LRSAM from SCD application.

![](_page_303_Picture_7.jpeg)

**Figure-5.175: LRSAM Menu**

**5.5.4.2.16.1 Send Track to LRSAM**.User shall click on this menu item to send a track of interest to LRSAM. A confirmation GUI, as shown in **Figure-5.176**, shall be displayed to user. User shall select 'Yes' option to send the track and the status of the same shall be updated in 'Emitter Report Window' GUI. If successful, letter 'NL' will be displayed in 'Status' field.

![](_page_303_Picture_10.jpeg)

**Figure-5.176: Confirmation GUI to Send Track to LRSAM – LRSAM Menu**.

SHAKTI : UHB\Ch5 Page 300 of 614

| TOFA     | TOLA     | Platform | Op.Role | TL | AC | Age | Latitude | Longitude | Status | Ch.Rate | Freq.Min. |
|----------|----------|----------|---------|----|----|-----|----------|-----------|--------|---------|-----------|
| 02:12:00 | 20:24:06 |          |         |    | 0  | 0   |          |           | -N-L-  |         | 10000     |
| 02:12:00 | 20:24:06 |          |         |    | 0  | 0   |          |           | -N-L-  | 9       | 15000     |
| 02:12:00 | 20:24:06 |          |         |    | 0  | 0   |          |           | -N-L-  |         | 18000     |
| 02:12:00 | 20:24:06 |          |         |    | 0  | 0   |          |           | -N-L-  |         | 2100      |
| 02:12:00 | 20:24:06 |          |         |    | 0  | 0   |          |           | -N-L-  |         | 495       |
| 02:12:00 | 20:24:06 |          |         |    | 0  | 0   |          |           | N-L    |         | 493       |

**Figure 177: GUI for LRSAM Track Status in Tabular Display – SCD Main Window**

5.5.4.2.16.1.1 To send track to LRSAM, if track number is not selected by user an information popup shall be displayed as shown below **Figure-5.178**.

![](_page_304_Picture_4.jpeg)

**Figure-5.178: Information regarding Send Track to LRSAM**.

**5.5.4.2.17 KAVACH Menu**.KAVACH menu (as shown in **Figure-5.179**) shall include GUI controls for sending a track to KAVACH from SCD application.

**Figure-5.179: KAVACH Menu**

**5.5.4.2.17.1 Send Track to KAVACH**.User shall click on this menu item to send a track of interest to KAVACH. A confirmation GUI, as shown in **Figure-5.180**, shall be displayed to user. User shall select 'Yes' option to send the track and the status of the same shall be updated in 'Emitter Report Window' GUI. If successful, letter 'NK' will be displayed in 'Status' field.

![](_page_304_Picture_10.jpeg)

**Figure-5.180: Confirmation GUI to Send Track to KAVACH – KAVACH Menu**

![](_page_304_Picture_12.jpeg)

**Figure-5.181: GUI for KAVACH Track Status in Tabular Display – SCD Main Window**

SHAKTI : UHB\Ch5 Page 301 of 614

5.5.4.2.17.1.1 To send track to KAVACH, if track number is not selected by user an information popup shall be displayed as shown below **Figure-5.182**.

![](_page_305_Picture_2.jpeg)

**Figure-5.182: Information regarding Send Track to KAVACH**

- **5.5.4.2.18 ESI Menu**.ESI menu (as shown in **Figure-5.183**) shall include GUI controls to set 'Blanking Mode' & control Gyro at ESI from SCD application.
- 5.5.4.2.18.1 The following sections describe the menu items available under this menu.

![](_page_305_Picture_6.jpeg)

**Figure-5.183: ESI Menu – SCD Main Window**

**5.5.4.2.18.1 Blanking Mode – Harbour**.User shall click on this menu item to enforce 'Blanking Mode' to 'Harbour' mode at External System Interface (ESI). A confirmation GUI, as shown in **Figure-5.184**, shall be displayed to user.

![](_page_305_Picture_9.jpeg)

**Figure-5.184: Confirmation GUI to Select 'Harbour' Blanking Mode**

**5.5.4.2.18.2 Blanking Mode – Deep Sea**.User shall click on this menu item to enforce 'Blanking Mode' to 'Deep Sea' mode at External System Interface (ESI). A confirmation GUI, as shown in **Figure-5.185**, shall be displayed to user.

![](_page_305_Picture_12.jpeg)

**Figure-5.185: Confirmation GUI to Select 'Deep Sea' Blanking Mode**

SHAKTI : UHB\Ch5 Page 302 of 614

**5.5.4.2.18.3 Gyro On/ Off**.User shall click on this menu item and a GUI, as shown in **Figure-5.186**, shall be displayed with options to enable/ disable 'Gyro' controls at ESI..

![](_page_306_Picture_2.jpeg)

**Figure-5.186: GUI to Enable/ Disable Gyro at ESI**

5.5.4.2.18.3.1 By default, 'Gyro' controls shall be enabled at ESI.

5.5.4.2.18.3.2 User shall check 'On/ Off' option for 'Heading', 'Roll' & 'Pitch' and click on 'Apply' option to 'On/ Off' enforce respective controls at ESI. The status of the same, if received, shall be displayed & updated in SCD Main Window. By default, Gyro controls shall be in 'On' mode at ESI.

5.5.4.2.18.3.3 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

**5.5.4.2.19 Print Menu**.Print menu (as shown in **Figure-5.187**) shall include GUI controls that would facilitate use to take print out of SCD application related data on a network printer. A network printer should be connected to SCD computer, on Shakti LAN, for taking print outs on paper.

5.5.4.2.19.a The following sections describe the menu items available under this menu.

![](_page_306_Picture_9.jpeg)

**Figure-5.187: Print Menu – SCD Main Window**

**5.5.4.2.19.1 Print Emitter Data**.User shall click on this menu item to select an emitter & take print out of its data. A GUI, as shown in **Figure-5.188**, shall be displayed to user with available emitter data.

SHAKTI : UHB\Ch5 Page 303 of 614

![](_page_307_Picture_1.jpeg)

**Figure-5.188: Print Emitter Data – Print Menu**

SHAKTI : UHB\Ch5 Page 304 of 614

- 5.5.4.2.19.1.1 User shall click on 'Close' option to exit from 'Print Emitter Data' GUI and go to SCD Main Window GUI.
  - (a) **Show/Hide filters Options**. User shall select 'Emitter No.', 'Emitter State', 'Threat Type', 'PRF Type', 'Signal Type', 'Scan Type', 'Pulse Width' & 'Frequency' and click on 'Apply' option filter out the parameters of interest.

The following print options will be applicable for the GUIs under 'Print Menu'.

- (b) **Print**. User shall click on 'Print' option on 'Print Emitter Data' GUI. A separate GUI, as shown in **Figure-5.189**, shall be displayed. On this GUI, user shall select 'Printer Name', 'Properties', 'Options' etc., and click on 'Print' option to take print out on Network Printer.
- 5.5.4.2.19.1.2 User shall click on 'Cancel' option to exit from this GUI and go to 'Print Emitter Data' GUI.

![](_page_308_Picture_6.jpeg)

**Figure-5.189: Printer Selection GUI – Print Menu.**

(c) **Print Preview**. User shall click on 'Print Preview' option on 'Print Emitter Data' GUI. A separate GUI, as shown in **Figure-5.190**, shall be displayed with a print preview of selected emitter data. User shall click on 'Print' icon on this GUI to take print out on network printer. User shall click on 'Exit' icon on this o close print preview and go to 'Print Emitter Data' GUI.

SHAKTI : UHB\Ch5 Page 305 of 614

![](_page_309_Picture_1.jpeg)

**Figure-5.190: GUI for Print Preview of Emitter Data – Print Menu**

SHAKTI : UHB\Ch5 Page 306 of 614

- **5.5.4.2.19.2 Print Emitter Library Records**.User shall click on this menu item to take print out of emitter library records. Refer section '5.5.4.2.3.9 Print Emitter Library Records'.
- **5.5.4.2.19.3 Print PD Data**.User shall click on this menu item to select an emitter & take print out of its Pulse Descriptor (PD) data. A GUI, as shown in **Figure-5.191**, shall be displayed to user.
- 5.5.4.2.19.3.1 User shall select 'Emitter No.', enter 'No. of PDs' and click on 'Get PD Data' to fetch current PD data for the emitter from ES Processor. PD data shall be displayed in textual format.
- 5.5.4.2.19.3.2 **Refer section '5.5.4.3.10.1' for '**Print' and 'Print Preview' procedure.
- 5.5.4.2.19.3.3 User shall click on 'Close' option to exit from 'Print Emitter Data' GUI and go to SCD Main Window GUI.

SHAKTI : UHB\Ch5 Page 307 of 614

![](_page_311_Picture_1.jpeg)

**Figure-5.191: Print PD Data – Print Menu**

SHAKTI : UHB\Ch5 Page 308 of 614

**5.5.4.2.19.4 Print ELINT Returns**.User shall click on this menu item to take print out of data of ELINT Returns files from SCD storage. A GUI, as shown in **Figure-5.192**, shall be displayed to user.

![](_page_312_Figure_2.jpeg)

**Figure-5.192: Print ELINT Returns Data – Print Menu**

5.5.4.2.19.4.1 List of existing ELINT Returns files shall be displayed on the GUI. User shall select a file and click on 'Show' option to view the contents of the file. User can browse through pages of recording file and filter out required recording data for print. **Refer section '5.5.4.3.10.1' for 'Print'** and 'Print Preview' procedure.

5.5.4.2.19.4.2 User shall click on 'Close' option to exit from 'Print Emitter Data' GUI and go to SCD Main Window GUI.

**5.5.4.2.20 System Menu**.System menu (as shown in **Figure-5.193**) shall include GUI controls to for generic functionalities of SCD system & Shakti EW system such as 'BITE', 'Self-Test', 'Start/ Stop Application Logs' etc.,.

5.5.4.2.20.1 The following sections describe the menu items available under this menu.

SHAKTI : UHB\Ch5 Page 309 of 614

![](_page_313_Picture_1.jpeg)

**Figure-5.193: System Menu – SCD Main Window**

- **5.5.4.2.20.1 BITE – Start ES Auto BITE**. User shall click on this menu item to start ES auto BITE (Built In Test Equipment) on selected ES receivers. A GUI, as shown in **Figure-5.194**, shall be displayed to user.
- 5.5.4.2.20.1.1 ES auto BITE, at RF level, will be performed for detection of faults and health checking of sub-systems/ LRUs of the EW system. Auto BITE shall be activated to run at regular intervals as per the system default time interval (every 5 minutes) or as defined by user. For performing BITE operations, the sub-systems/ LRUs (on which BITE test shall be performed) should be switched on. The following sub-systems shall be included under ES auto BITE configuration:
  - (a) NB-Rx1 (0.175-0.5GHz).
  - (b) NB-Rx2 (0.5-18GHz).
  - (c) BB-Rx1 (2.2-18GHz).
  - (d) BB-Rx2 (18-40GHz).

SHAKTI : UHB\Ch5 Page 310 of 614

- 5.5.4.2.20.1.2 A GUI shall be displayed to the user for selecting individual receiver LRUs along with auto BITE timer interval.
- 5.5.4.2.20.1.3 By default, ES auto BITE shall be enabled and shall be initiated on start of SCD application with all the receivers and a default time interval of 5 minutes.
- 5.5.4.2.20.1.4 User shall check the receiver under test, enter 'Time Interval' value and click on 'Start' option.
- 5.5.4.2.20.1.5 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

![](_page_314_Picture_5.jpeg)

**Figure-5.194: GUI to Start ES Auto BITE – System Menu**

**5.5.4.2.20.2 BITE – Stop ES Auto BITE**.User shall click on this menu item to stop ongoing ES auto BITE. A confirmation GUI, as shown in **Figure-195**, shall be displayed to user. User shall select 'Yes' option to stop ES Auto BITE.

![](_page_314_Picture_8.jpeg)

**Figure-5.195: Confirmation GUI to Stop ES Auto BITE – System Menu**

**5.5.4.2.20.3 BITE– Show ES Auto BITE Status**.User shall click on this menu item to view ES auto BITE status (as shown in **Figure-5.196**). ES Processor will send auto BITE

SHAKTI : UHB\Ch5 Page 311 of 614

status as tracks to SCD system and the same shall be displayed in this GUI.

**Figure-5.196: ES Auto BITE Status GUI – System Menu**

5.5.4.2.20.3.1 BITE tracks received from ES Processor shall be displayed in a tabular view on the GUI. Colour codes for representing BITE tracks shall be as given in **Table-5.5**.

**Table-5.5: Colour Code –ES Auto BITE Track**

| Ser | Colour | Status                                                        | Remarks      |
|-----|--------|---------------------------------------------------------------|--------------|
| 1   | Cyan   | All the parameters<br>of Auto BITE track<br>are OK & matching | Auto BITE OK |

SHAKTI : UHB\Ch5 Page 312 of 614

| Ser | Colour | Status                                                                                                   | Remarks          |
|-----|--------|----------------------------------------------------------------------------------------------------------|------------------|
|     |        | with reference data.                                                                                     |                  |
| 2   | Orange | Some or all the<br>parameters of Auto<br>BITE track are NOT<br>OK & not matching<br>with reference data. | Auto BITE NOT OK |

5.5.4.2.20.3.2 Consolidated status of BITE parameters (DOA, Frequency, PW, PRF, Amplitude) in a quadrant of a receiver, shall be displayed on the GUI. If a parameter (example: frequency) is not correct in 'all' or 'some of' the tracks of a quadrant, then the parameter (frequency) indicator shall be painted in 'red' color as shown in the GUI. If DOA is not correct in for all the tracks in a quadrant, then all the parameters including DOA indicators shall be painted in 'red' color.

5.5.4.2.20.3.3 Track time stamp along with the time at which the status is updated shall also be displayed on the GUI.

5.5.4.2.20.3.4 Auto BITE missing tracks will also be displayed in a separate section in the same window.

5.5.4.2.20.3.5 User shall click on 'Close' option to exit from this GUI and go to SCD Main Window.

**5.5.4.2.20.4 Update ES Auto BITE Reference Data**.User shall click on this option under BITE menu to update the Auto BITE reference data (as shown **Figure-5.197** : Update ES Auto BITE reference data GUI User shall provide required receiver type, DOA, Frequency, PW, PRF and amplitude values then click on 'Add' button. Entered details are updated in respective receiver type spreadsheet. System controller will conclude the Auto BITE status with this reference details.

SHAKTI : UHB\Ch5 Page 313 of 614

![](_page_317_Figure_1.jpeg)

**Figure-5.197: Update ES Auto BITE reference data GUI**

**5.5.4.2.20.5 BITE – Perform EA Manual BITE**.User shall click on this menu item to start EA manual BITE on EA system. A confirmation GUI, as shown in **Figure-5.198**, shall be displayed to user. User shall click on 'Yes' option to proceed with manual BITE test. After issuing BITE test, the status GUI, as shown in **Figure-5.199**, shall be displayed immediately to user. The BITE status will be updated on this GUI as on when received from EA Processor. The GUI shall retain the previous BITE status, if any, when opened. User shall click on 'Test Again' option to perform BITE again on EA system. The test is not periodic, hence user shall perform this test as on when required.

5.5.4.2.20.5.1 LRUs of EA system on Port & Starboard side shall be included for manual BITE test.

SHAKTI : UHB\Ch5 Page 314 of 614

5.5.4.2.20.5.2 The aim of manual BITE is for detection of faults and health checking of subsystems/ LRUs of EA system.

5.5.4.2.20.5.3 User shall click on 'Close' option to exit from this GUI and go to SCD Main Window.

![](_page_318_Picture_3.jpeg)

**Figure-5.198: Confirmation GUI to Perform EA Manual BITE – System Menu**

**5.5.4.2.20.6 BITE – Show EA Manual BITE Status**.User shall click on this menu item to view the status of manual BITE on EA system. A GUI, as shown in **Figure-5.199**, shall be displayed with BITE status. The BITE status, along with start & stop time stamps, shall be updated on this GUI as on when received from EA Processor. User can perform manual BITE test on EA system again by clicking on 'Test Again' option.

5.5.4.2.20.6.1 BITE status of LRUs of EA system on Port & Starboard side shall be displayed on the GUI.

![](_page_318_Figure_7.jpeg)

**Figure-5.199: EA Manual BITE Status GUI – System Menu**

SHAKTI : UHB\Ch5 Page 315 of 614

5.5.4.2.20.6.2 The colour code of EA manual BITE status shall be as given in **Table-5.6**.

**Table-5.6: EA Manual BITE Colour Codes**

| Ser | Colour | BITE Status                |
|-----|--------|----------------------------|
| (a) | Green  | BITE OK.                   |
| (b) | Red    | BITE NOT OK.               |
| (c) | Grey   | BITE Status NOT Available. |

5.5.4.2.20.6.3 User shall click on 'Close' option to exit from this GUI and go to SCD Main Window.

**5.5.4.2.20.7 BITE – RFPS Manual BITE**. User shall click on this menu item to perform ES & RFPS manual BITE on selected ES receivers & RFPS. A GUI, as shown in **Figure-5.200**, shall be displayed to user for selecting ES receivers/ RFPS.

![](_page_319_Figure_6.jpeg)

**Figure-5.200: GUI to Perform ES & RFPS Manual BITE – System Menu**

5.5.4.2.20.7.a The aim of this manual BITE is for detection of faults and health checking of sub-systems/ LRUs of ES receivers & RFPS.

5.5.4.2.20.7.b ES manual BITE can be performed to check:

- (a) ES Processor-ES Receivers Path.
- (b) ES Processor-RFPS-ES Receivers Path.
- (c) RFPS-Omni Path.

SHAKTI : UHB\Ch5 Page 316 of 614

**5.5.4.2.20.7.1 Manual BITE in ES Processor-ES Receivers Path:** User shall check NB Rx1 (0.175-2.2GHz), NB Rx2/ BB Rx1 (2.2-18GHz), BB Rx2 (18-40GHz) or all of these options to troubleshoot this RF chain. The result of this test will be interpreted in the form of manual BITE tracks that will be received from ES Processor & displayed on emitter presentation windows in SCD Main Window.

**5.5.4.2.20.7.2 Manual BITE in ES Processor-RFPS-ES Receivers Path:** User shall check RFPS (0.175-2.2GHz), RFPS (18-40GHz) or both of these options to troubleshoot this RF chain. Note: If RFPS option is checked, NB Rx1 & BB Rx2 will automatically be checked. The result of this will be interpreted in the form of manual BITE tracks that will be received from ES Processor & displayed on emitter presentation windows in SCD Main Window.

5.5.4.2.20.7.2.1 Manual BITE tracks shall be represented in 'Orange' colour as shown in **Figure-5.201**

SHAKTI : UHB\Ch5 Page 317 of 614

![](_page_321_Figure_1.jpeg)

**Figure-5.201: GUI Showing Manual BITE Tracks – System Menu**

- **5.5.4.2.20.7.3 Manual BITE in RFPS-Omni Path:** User shall check only RFPS (2.2- 18GHz) to troubleshoot this RF chain. The result of this test will be interpreted on 'RFPS Manual BITE Status' GUI (as shown in **Figure-5.202**), which is described in the following section.
- 5.5.4.2.20.7.3.1 User shall select/ enter 'BITE Parameters/ Receiver Parameters, Quadrant' and click on 'Start' option to perform manual BITE on selected LRUs.
- 5.5.4.2.20.7.3.2 The test once, issued will be continuing, unless stopped by user.
- 5.5.4.2.20.7.3.3 User shall check the LRU (receiver or RFPS) under test and click on 'Stop' option to stop ongoing manual BITE.
- 5.5.4.2.20.7.3.4 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.
- **5.5.4.2.20.8 BITE – Show RFPS BITE Status**.User shall click on this menu item to view the status of manual BITE on RPFS. A GUI, as shown in **Figure-5.202**, shall be displayed with BITE status. The BITE status, along with time stamp at which the status was reported, shall be updated on this GUI as on when received from RFPS.

![](_page_322_Picture_7.jpeg)

**Figure-5.202: RFPS Manual BITE Status GUI – System Menu**

5.5.4.2.20.8.1 The color code of RFPS manual BITE status shall be as given in **Table 5.7**.

SHAKTI : UHB\Ch5 Page 319 of 614

**Table-5.7: RFPS Manual BITE Status Colour Codes**

| Ser | Colour | BITE Status                |
|-----|--------|----------------------------|
| (a) | Green  | BITE OK.                   |
| (b) | Red    | BITE NOT OK.               |
| (c) | Grey   | BITE Status NOT Available. |

5.5.4.2.20.8.2 User shall click on 'Close' option to exit from this GUI and go to SCD Main Window.

**5.5.4.2.20.9 Self-Test**.User shall click on this menu item to perform self-test on subsystems of the EW system. A GUI, as shown in **Figure-5.203**, shall be displayed to user for selecting sub-systems.

![](_page_323_Picture_5.jpeg)

**Figure-5.203: GUI to Perform Self-Test – System Menu**

SHAKTI : UHB\Ch5 Page 320 of 614

5.5.4.2.20.9.1 Self-test functionality shall be exercised cautiously by the user as this may remove transient data at the LRU level. Self-test shall not be allowed on RFPS when it is capturing or analysing data for a selected ES track. There shall be provision for selecting complete system or individual sub-systems. The following sub-systems shall be included for performing self-test:

- (a) ES Processor.
- (b) NB Rx1 (0.175-0.5GHz).
- (c) NB Rx2 (0.5-18GHz).
- (d) BB Rx1 (2.2-18GHz).
- (e) BB Rx2 (18-40GHz).
- (f) RFPS.
- (g) EA Processor.
- (h) ESI.

5.5.4.2.20.9.2 The status of 'Self-Test' shall be displayed in 'Link & Self-Test Status' GUI, which will be described in the coming sections.

User shall check a sub-system and click on 'Perform Self-Test' option.

5.5.4.2.20.9.3 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

**5.5.4.2.20.10 Temporary Emitter Library – Add Track to Library**.'Temporary Emitter Library' shall contain the emitter interceptions selected and added by the user from 'Emitter Presentation Windows' in SCD Main Window during system operation. This library is required as the 'System Emitter Library' given by EWOSS shall not be modified by adding new emitter entries into it. Basically, 'Temporary Emitter Library' will be appended to 'System Emitter Library' (provided by EWOSC) if the number of entries in 'System Emitter Library' is lesser than 20,000. The total number of entries in 'Temporary Emitter Library' & 'System Emitter Library' shall not exceed 20,000. This means, if there is no space is left (20,000 entries are already filled) in 'System Emitter Library' then new emitter cannot be added to 'Temporary Emitter Library'. By default, library matching shall be performed in this library also.

5.5.4.2.20.10.1 User shall click on this menu item to add a track to 'Temporary Emitter

SHAKTI : UHB\Ch5 Page 321 of 614

Library'. A GUI, as shown in **Figure-5.204**, shall be displayed to user.

5.5.4.2.20.10.2 User shall select/ enter 'Emitter Identity Details' and click on 'Add this Record to Library' option. User can modify JPRO technique, if required, by clicking on 'Update JPRO Technique'.

5.5.4.2.20.10.3 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

![](_page_325_Figure_4.jpeg)

**Figure-5.204: GUI to Add Track to Temporary Emitter Library – System Menu**

**5.5.4.2.20.11 Temporary Emitter Library – View/ Modify Library**.User shall click on this menu item to view/ modify existing tracks in 'Temporary Emitter Library'. A GUI, as shown in **Figure-5.205**, shall be displayed to user.

5.5.4.2.20.11.1 By default, existing library records shall be listed out on the GUI.

5.5.4.2.20.11.2 User shall check 'Modify Library' option & select/ modify 'Emitter Identity Details' and click on 'Update this Record in Library' option. User can modify JPRO technique, if required, by clicking on 'Update JPRO Technique'.

5.5.4.2.20.11.3 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

SHAKTI : UHB\Ch5 Page 322 of 614

![](_page_326_Figure_1.jpeg)

**Figure-5.205: GUI to View/ Modify Temporary Emitter Library – System Menu**

**5.5.4.2.20.12 System Emitter Library – Sort Identities by Threat Level**.User shall check this menu item to enable sorting of emitter identity details based on 'Threat Level'. Emitter with highest 'Threat Level' will be listed first in order as shown in GUI **Figure-5.206**.

SHAKTI : UHB\Ch5 Page 323 of 614

![](_page_327_Figure_1.jpeg)

**Figure-5.206: GUI with Emitter Identities Sorted by Threat Level – System Menu**

**5.5.4.2.20.13 System Emitter Library – Sort Identities by Confidence Level**.User shall check this menu item to enable sorting of emitter identity details based on 'Confidence Level' when displayed as shown in **Figure-5.207**. The 'Confidence Level' shall be configurable in SCD application. Emitter with highest 'Confidence Level' will be listed first in order.

SHAKTI : UHB\Ch5 Page 324 of 614

![](_page_328_Figure_1.jpeg)

**Figure-5.207: GUI with Emitter Identities Sorted by Confidence Level – System Menu**

**5.5.4.2.20.14 System Emitter Library – Search in Priority Library**. User shall check this menu item to enable searching of emitters in 'Priority' entries of 'Emitter Library'. By default, emitter library searching shall be performed in 'Priority' entries only. Emitters which are matched with priority library records are shown in **Figure-5.208**.

SHAKTI : UHB\Ch5 Page 325 of 614

![](_page_329_Figure_1.jpeg)

**Figure-5.208: Priority library matched emitters GUI**

**5.5.4.2.20.15 System Emitter Library – Search in Non Priority Library**. User shall check this menu item to enable searching (library matching) of emitters in 'Non-Priority' entries of 'Emitter Library' also. By default, searching shall be performed in 'Priority' entries. User can appreciate this difference by looking at emitter presentation windows as shown in Figure-5.209&Figure-5.210.

SHAKTI : UHB\Ch5 Page 326 of 614

![](_page_330_Figure_1.jpeg)

**Figure-5.209: GUI without Non-Priority Library Search – System Menu**

SHAKTI : UHB\Ch5 Page 327 of 614

![](_page_331_Figure_1.jpeg)

**Figure-5.210: GUI with Non-Priority Library Search – System Menu**

**5.5.4.2.20.16 System Emitter Library – Show All Records**. User shall click on this menu item to view the entire 'Emitter Library' records (maximum 20,000) in a GUI as shown in **Figure-5.211**. User can filter out records of interest by selecting options in 'Search Records' field and clicking on 'Show Records' option.

5.5.4.2.20.16.1 User shall click on 'Close' option to exit from this GUI and go to SCD Main Window.

SHAKTI : UHB\Ch5 Page 328 of 614

![](_page_332_Figure_1.jpeg)

Figure-5.211: Emitter Library Records GUI - System Menu

SHAKTI: UHB\Ch5 Page 329 of 614

**5.5.4.2.20.17 ELINT Return – Add Track**.User shall click on this menu item to add selected Emitter details into ELINT Return file.

5.5.4.2.20.17.1 After selection of this menu item, 'ELINT Returns – Add Track' GUI will be displayed with suggested Radar name and Platform name as shown in **Figure-5.212** . Radar & Platform names are derived from existing HUMINT definitions file. User have the facility to change any other Radar name or enter new Radar and Platform names and click on 'Add' button. Selected emitter details are added to ELINT Return file.

![](_page_333_Picture_3.jpeg)

**Figure-5.212: Add Track – ELINT Returns GUI**

**5.5.4.2.20.18 ELINT Return – View/ Modify Existing Entries**.User shall click on this menu item to view /modify the Emitter details in the ELINT Return file.

5.5.4.2.20.18.1 User has the facility to view the already added emitter details and he can modify the Emitter parameters as shown in **Figure-5.213**.

5.5.4.2.20.18.2 User has the facility to delete the selected emitter details from ELINT Return file.

5.5.4.2.20.18.3 User has the facility to save the selected emitter details to another ELINT Return file.

SHAKTI : UHB\Ch5 Page 330 of 614

![](_page_334_Figure_1.jpeg)

**Figure-5.213: View/Modify – ELINT Return GUI**

**5.5.4.2.20.19 ELINT Return – Update HUMINT Definitions**.User shall click on this menu item to update the new ELINT Return definition file into the Shakti project. User shall select the desired file in 'ELINT Returns Definitions File' GUI as shown in the **Figure-5.214**. And click on 'Update' button to update the selected HUMINT definition file. System Controller shall search for Radar name and Platform name from HUMINT definition file whenever User add the new emitter to the ELINT Reruns file.

SHAKTI : UHB\Ch5 Page 331 of 614

![](_page_335_Picture_1.jpeg)

**Figure-5.214: HUMINT definitions file updation GUI**

**5.5.4.2.20.20 Show Passive Track History**.User shall click on this menu item to view the all passive tracks details. User has the facility to take print out of the passive track's details. User can view the passive tracks by using filter options i.e. (by track no, TOFA, TOLA, Freq., PW, PRF, DOA and etc). Operator has the facility to select the desired track parameters for taking printout. History of passive tracks GUI is as shown in **Figure-5.215**.

SHAKTI : UHB\Ch5 Page 332 of 614

![](_page_336_Picture_1.jpeg)

**Figure-5.215: History of Passive Tracks GUI**

SHAKTI : UHB\Ch5 Page 333 of 614

**5.5.4.2.20.21 Emitters – Show List**.User shall click on this menu item to view emitters of interest in a separate GUI as shown in **Figure-216**.

![](_page_337_Picture_2.jpeg)

**Figure-216: Emitters List GUI – System Menu**

- 5.5.4.2.20.21.1 User shall select 'Emitter No.', 'Emitter State', 'Threat Type', 'PRF Type', 'Signal Type', 'Scan Type', 'Pulse Width' & 'Frequency' and click on 'Apply' option filter out the parameters of interest.
- 5.5.4.2.20.21.2 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.
- 5.5.4.2.20.21.3 User shall click on 'Show Detailed Parameters' option to view detailed emitter parameters as shown in **Figure-5.183** (section '5.5.4.3.17 Detailed Parameters Window).
- 5.5.4.2.20.21.4 User shall click on 'Close' option to exit from that GUI and go to 'Emitters List' GUI.
- **5.5.4.2.20.22 Emitter – Search Identity**.User shall click on this menu item to search identity of an emitter in entire 'Emitter Library' of 20,000 records (maximum) and display its details. A GUI, as shown in **Figure-5.217**, shall be displayed to user to select an emitter.
- 5.5.4.2.20.22.1 User shall click on 'Search Identity' option.
- 5.5.4.2.20.22.2 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

SHAKTI : UHB\Ch5 Page 334 of 614

![](_page_338_Picture_1.jpeg)

**Figure-5.217: GUI to Select Emitter for Identity Search – System Menu**

5.5.4.2.20.22.3 Emitter identity details if found shall be displayed in a GUI as shown in **Figure-5.260** (section '5.5.4.3.17 Detailed Parameters Window').

**5.5.4.2.20.23 Set Date and Time**. User shall click on this menu item to set the Date & Time of the system. A GUI, as shown in **Figure-5.218**, shall be displayed to user.

![](_page_338_Picture_5.jpeg)

**Figure 5.218: Set Date and Time – System Menu**

**5.5.4.2.20.24 Start/ Stop System Recording**.User shall click on this menu item to start/ stop 'System Recording' in SCD application. This shall be a toggling menu item and shall switch between 'Stop Recording' & 'Start Recording' options. By default, 'System

SHAKTI : UHB\Ch5 Page 335 of 614

Recording' shall be on.

5.5.4.2.20.24.1 When the 'System Recording' is ON, all track data sent by ES Processor, application commands exercised by the user and scan configurations of ES receivers, messages exchanged between sub-systems & SCD system etc., will be stored in a file in a pre-defined location on SCD storage. The file name will automatically be assigned by SCD application for each new recoding. Whenever the SCD application is closed, the recorded file also will be closed. Restarting the SCD application will open a new file for storing recorded data.

5.5.4.2.20.24.2 A confirmation GUI, as shown in **Figure-5.219**, shall be displayed to user to start/ stop recording activity. The status of recording shall be displayed in 'EW System Status Window', which will be described in the coming sections.

![](_page_339_Picture_4.jpeg)

**Figure-5.219: Confirmation GUI to Start System Recording – System Menu**

**5.5.4.2.20.25 Audio Alarm – Enable/ Disable**.User shall click on this menu item to enable Audio alarm for particular signal type /frequency band /sector. By default Audio alarm is disabled state. Audio alarm shall be enabling, when alarm set to any of following selection.

- (a) Set Alarm for Frequency Type
- (b) Set Alarm for Frequency band
- (c) Set Alarm for Sector.

5.5.4.2.20.25 .1 Audio alarm enabled/disabled status shall be shown in status window.

5.5.4.2.20.25 .2 If audio alarm is enabled in SCD application & auto tones are assigned to particular signal type then number of alarming tracks shall be shown in place of enable/disabled status.

**5.5.4.2.20.26 Audio Alarm – Show Alarming Tracks**.User shall click on this menu item to view alarming emitters list. User can view only when Audio Alarm should be in

SHAKTI : UHB\Ch5 Page 336 of 614

'Enable' state and audio tones are assigned to particular signal type or frequency band or sector.

5.5.4.2.20.26 .1 If user selects this option without Audio alarm enable condition, a warning pop up 'No alarming tracks available at present' a window shall be displayed as shown in the **Figure-5.220**.

5.5.4.2.20.26.2 If user selects 'Show Alarming Tracks' option, at present all Audio alarming emitters shall be shown in a window as shown in **Figure-5.221**.

![](_page_340_Picture_4.jpeg)

**Figure-5.220: No alarming tracks GUI**

![](_page_340_Picture_6.jpeg)

**Figure-5.221: Audio Alarming Emitters GUI**

**5.5.4.2.20.27 Audio Alarm – Set Alarm for Freq. Band / Freq. Type / Sector**.User shall click on this menu item to set the Audio alarm tone for any frequency type /frequency band /sector selections.

5.5.4.2.20.27.1 If user wants to assign Audio tones to emitter's w.r.t frequency type, he should select 'Audio Alarm ->Set Alarm for Frequency Type' then 'Audio Alarm Tones' GUI will be displayed as shown in **Figure-5.222**.

SHAKTI : UHB\Ch5 Page 337 of 614

![](_page_341_Picture_1.jpeg)

**Figure-5.222: Audio Alarm Tones for Signal Type**

5.5.4.2.20.27.2 If user wants to assign Audio tones to emitter's w.r.t frequency bands, he should select 'Audio Alarm ->Set Alarm for Frequency band' then 'Audio Alarm Tones' GUI will be displayed as shown in **Figure-5.223**.

![](_page_341_Figure_4.jpeg)

**Figure-5.223: Audio Alarm Tones for Frequency Bands**

SHAKTI : UHB\Ch5 Page 338 of 614

5.5.4.2.20.27.3 If user wants to assign Audio tones to emitter's w.r.t sectors, he should select Audio 'Alarm ->Set Alarm for Sectors' then 'Audio Alarm Tones' GUI will be displayed as shown in **Figure-5.224**.

![](_page_342_Figure_2.jpeg)

**Figure-5.224: Audio Alarm Tones for Sectors**

- **5.5.4.2.20.28 Show User Activity Log**.User shall click on this menu item to view activity log of user on SCD application. User activity log file will contain the EW system operations (along with time stamps) exercised by the user in SCD Main Window in 'Online Mode'.
- 5.5.4.2.20.28.1 A GUI shall be displayed, as shown in **Figure-5.225**, listing activity log file names existing on SCD storage.
- 5.5.4.2.20.28.2 User shall select a file and click on 'Show' option to view its contents. Alternately, user can double click on mouse left button.
- 5.5.4.2.20.28.3 User can filter out activity log between two dates by selecting dates & clicking on 'Search' option for a particular 'Sub-System'.
- 5.5.4.2.20.28.4 User shall click on 'Close' option to exit from this GUI and go to SCD Main Window.

SHAKTI : UHB\Ch5 Page 339 of 614

![](_page_343_Figure_1.jpeg)

**Figure-5.225: User Activity Log GUI – System Menu**

**5.5.4.2.20.29 Show System Error Log**. User shall click on this menu item to view error log of SCD application. The error log (error messages history) file will contain accumulated list of all system/ sub-system generated error messages.

5.5.4.2.20.29.1 A GUI shall be displayed, as shown in **Figure-5.226**, listing error log file names existing on SCD storage.

![](_page_344_Picture_3.jpeg)

**Figure-5.226: System Error Log GUI – System Menu**

5.5.4.2.20.29.2 User shall select a file and click on 'Show' option to view its contents. Alternately, user can double click on mouse left button.

5.5.4.2.20.29.3 User can filter out error log between two dates by selecting dates & clicking on 'Search' option for a particular 'Sub-System'. If the log is empty, no contents will be listed out on the GUI.

5.5.4.2.20.29.4 User shall click on 'Close' option to exit from this GUI and go to SCD Main Window.

**5.5.4.2.20.30 Current Configuration – View**.User shall click on this menu item to view current system configuration (i.e ES, EA, RFPS, ESI, CMS, LRSAM, KAVACH and SCD).

SHAKTI : UHB\Ch5 Page 341 of 614

![](_page_345_Figure_1.jpeg)

**Figure-5.227: Current System configuration**

SHAKTI : UHB\Ch5 Page 342 of 614

**5.5.4.2.20.31 Current Configuration – Save to Another File**. User shall click on this menu item to save the current (after login) configuration of the EW system to a file selected by user on SCD storage. User can select this same file at the login and start SCD application with this configuration. Description on SCD application configuration is given in section '5.5.4.2.5 System Configuration'. A GUI, as shown in **Figure-5.228**, shall be displayed to user to select a file name on SCD storage.

5.5.4.2.20.31.1 Use shall click enter/ select a file name and click on 'Save' option.

5.5.4.2.20.31.2 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window without saving configuration to a file.

![](_page_346_Figure_4.jpeg)

**Figure-5.228: File Selection GUI for Saving Configuration to a File – System Menu**

**5.5.4.2.20.32 Reset System Links**. User shall click on this menu item to Reset Ethernet link of other subsystems and reconnects once again. Before resetting the Ethernet links user confirmation dialog shall be displayed as shown in **Figure-5.229**. Subsystems like ES, EA, RFPS, ESI and CMS are disconnected and re-connected once again. This operation is required whenever User has doubts on the emitter's updation and any improper link connection has detected in the Shakti system.

SHAKTI : UHB\Ch5 Page 343 of 614

![](_page_347_Picture_1.jpeg)

**Figure-5.229: System Links Rest GUI**

**5.5.4.2.20.33 Enable Encryption / Decryption**.User shall click on this menu item to enable or disable Encryption/Decryption for required sub-systems. A GUI, as shown in **Figure-5.230**, shall be displayed to user. If Operator selects 'Enable' for subsystem, data and commands between SCD and the selected sub system will be encrypted & decrypted. In case of 'Disable' option encryption and decryption will not happen between SCD and the selected subsystem.

SHAKTI : UHB\Ch5 Page 344 of 614

![](_page_348_Picture_1.jpeg)

**Figure 5.230: Encryption/Decryption GUI - System Menu**

**5.5.4.2.20.34 Go Offline**.User shall click on this menu item to go to 'Offline Mode' GUI from SCD Main Window. Going to 'Offline Mode' will disconnect SCD system from all other sub-systems &stop all logging activities including system recording. A confirmation GUI, as show in **Figure-5.231**, shall be displayed to user. If user clicks on 'Yes' option, 'SCD Main Window' GUI shall be closed & 'Offline Mode' GUI shall be displayed.

![](_page_348_Picture_4.jpeg)

**Figure-5.231: Confirmation GUI to Go Offline – System Menu**

SHAKTI : UHB\Ch5 Page 345 of 614

**5.5.4.2.20.35 Logout**. User shall click on this menu item to logout of SCD application from SCD Main Window and go to 'User Authentication' GUI. Logging out from ''SCD application will disconnect SCD system from all other sub-systems & stop all logging activities including the system recording. A confirmation GUI, as show in **Figure-5.232**, shall be displayed to user. If user clicks on 'Yes' option, 'SCD Main Window' GUI shall be closed & 'User Authentication' GUI shall be displayed.

![](_page_349_Picture_2.jpeg)

**Figure-5.232: Confirmation GUI to Logout from SCD Main Window – System Menu**

**5.5.4.2.21 Help Menu**. Help menu (as shown in **Figure-5.233**) shall include GUI controls for displaying SCD application related help. The help document shall display description of SCD application functionalities (in SCD Main Window) for configuring & controlling the EW system. The help document shall include GUI snap shots of relevant functionalities in SCD Main Window with content indexing and keyword search.

5.5.4.2.21.a The following sections describe the menu items available under this menu.

![](_page_349_Picture_6.jpeg)

**Figure-5.233: Help Menu – SCD Main Window**

**5.5.4.2.21.1 Help – SCD Help Manual***.*User shall click on this menu item to view help document (SCD Main Window) of SCD application. A GUI shall be displayed to user, as shown in **Figure-5.234**.

5.5.4.2.21.1.1 List of entries in help document shall be displayed to the left on the GUI. When user selects an entry in the list, its help description shall be displayed to the right on the GUI. User can search for help of a particular topic by typing the initial letter in the 'line edit' field provided on top of the list of help topics.

5.5.4.2.21.1.2 User shall click on 'Close' option to exit from this GUI and go to SCD Main

SHAKTI : UHB\Ch5 Page 346 of 614

Window.

![](_page_350_Figure_2.jpeg)

**Figure-5.234: SCD Main Window Help Document GUI – Help Menu**

**5.5.4.2.21.2 Help – About Shakti SCD**.User shall click on this menu item to see overview of Shakti EW system & SCD system, as shown in **Figure-5.235**.

5.5.4.2.21.2.1 User shall click on 'OK' option to exit from this GUI and go to SCD Main Window.

SHAKTI : UHB\Ch5 Page 347 of 614

![](_page_351_Figure_1.jpeg)

**Figure-5.235: About Shakti SCD GUI – Help Menu**

**5.5.4.2.21.3 Help – About QT & RHEL**. User shall click on this menu item to see brief overview (as shown in **Figure 5.236**) of 'Qt & RHEL (Red Hat Enterprise Linux)', the frame work & operating system on which SCD application will be hosted.

![](_page_351_Figure_4.jpeg)

**Figure 5.236: About RHEL & Qt GUI –Help menu**

User shall click on 'OK' option to exit from this GUI and go to SCD Main Window.

SHAKTI : UHB\Ch5 Page 348 of 614

**5.5.4.2.22 EW Activity Window**. 'EW Activity Window' GUI shall be displayed below 'Application Menu Bar & Drop-Down Menus'. This GUI shall present the spectral activity captured by ES segment in a graph in a frequency scale of 0.175-40GHz. Activity Window for frequency range 175-18000 MHz is shown in **Figure-5.237**. Tracks received from ES Processor shall be presented as fixed length bar lines with track numbers below the lines. Colour notation for depicting the tracks in this GUOI shall be same as followed in other emitter presentation windows (described in the coming sections). There shall be provision to show/ hide this GUI. Activity.

![](_page_352_Figure_2.jpeg)

**Figure-5.237: EW Activity Window – SCD Main Window**

- **5.5.4.2.22.1 Zoom Band in EW Activity Window**. Rubber band zooming (in frequency range) shall be provided on the GUI for viewing tracks in a sub-band of interest.
  - (a) **Rubber Band Zoom**. User shall place mouse cursor in frequency range of interest in 'EW Activity Window', press & hold mouse left button and drag in the region to zoom-in.
  - (b) **Zoom Current Band**. User shall place mouse cursor in frequency range of interest in 'EW Activity Window' and click on mouse right button. A context menu, as shown in **Figure-5.238**, will be displayed & user shall click on 'Zoom Current Band' option to zoom-in within a frequency band of 1GHz to the left & 1 GHz to the right of mouse cursor position.

![](_page_352_Picture_7.jpeg)

**Figure-5.238: Context Menu GUI in EW Activity Window – SCD Main Window.**

(c) **Zoom Band**. User shall place mouse cursor in 'EW Activity Window' and click on mouse right button. A context menu, as shown in **Figure-5.238**, will be displayed & user shall click on 'Zoom Band-><Spectrum Band>' option to zoom-in that band. '<Spectrum Band>' denotes a predefined spectrum band letter as shown in the GUI.

SHAKTI : UHB\Ch5 Page 349 of 614

- (d) **Zoom In/ Out/ Reset**. User shall place mouse cursor in 'EW Activity Window' and click on the mouse right button. A context menu will be displayed , as shown in **Figure-5.238**, user shall click on 'Zoom In/ Zoom Out' option to zoom-in/ zoom-out within a frequency range 10GHz, 5GHz, 3GHz and so on. Click on 'Reset Zoom' option to reset 'EW Activity Window' to its default zoom range (0.175-40GHz).
- **5.5.4.2.23 EW System Status Window.** 'EW System Status Window' GUI (as shown in **Figure-5.239**) shall display the status of important parameters of the EW System for drawing attention of user.

| A: 020, P: 000   | DisplayMode:   | Zoom:      | AudioAlarm: | Merge MB:   | LinkStatus:     | NBRx1PC: 936137, NBRx2PC: 815321 | AutoBITE: | LockoutFreq:  | Lat: 15° 50′ 20.00″N   | Heading:   | SCD UpTime: |
|------------------|----------------|------------|-------------|-------------|-----------------|----------------------------------|-----------|---------------|------------------------|------------|-------------|
| T: 020           | TRUE           | OFF        | DISABLED    | OFF         | <mark>UP</mark> | BBRx1PC: 746009, BBRx2PC: 133209 | ON        | NOT SET       | Long: 082° 12′ 54.00″E | 350°       | 01m 35s     |
| CW: 002, WR: 010 | DisplayFilter: | AutoPurge: | WarnerLib.: | MergeAgile: | Recording:      | NBRx1Mode: DIR, NBRx2Mode: DIR   | Man.BITE: | LockoutSect.: | Roll: <b>20.72°</b>    | MapStatus: | DB Status:  |
| LO: 003          | OFF            | OFF        | 3 Entries   | OFF         | ON              | BBRx1Mode: SFB1,BBRx2Mode: BB    | OFF       | NOT SET       | Pitch: <b>20.72°</b>   | IN RANGE   | ACTIVE      |

**Figure-5.239: EW System Status Window GUI – SCD Main Window**

The parameters and their status to be displayed in this window are given in the following **Table 5.8**.

**Table-5.8: Parameters in EW System Status Window**

| Parameter                              | Status        | Description                                                         | Status GUI |
|----------------------------------------|---------------|---------------------------------------------------------------------|------------|
| Active,<br>Passive,<br>Total Tracks    | 'Track Count' | Track count received from<br>ES Processor.                          |            |
| CW,<br>Lock<br>On,<br>Warner<br>Tracks | 'Track Count' | Track count received from<br>ES Processor.                          |            |
| Display Mode                           | TRUE          | When SCD Main Window<br>is switched to 'True' mode.                 |            |
|                                        | RELATIVE      | When SCD Main Window<br>is switched to 'Relative'<br>mode.          |            |
| Display Filter                         | ON            | When a display filter is<br>applied<br>in<br>SCD<br>Main<br>Window. |            |
|                                        | OFF           | When NO display filter is<br>applied<br>in<br>SCD<br>Main           |            |

SHAKTI : UHB\Ch5 Page 350 of 614

| Parameter                                | Status                 | Description                                                                                                                          | Status GUI |
|------------------------------------------|------------------------|--------------------------------------------------------------------------------------------------------------------------------------|------------|
|                                          |                        | Window.                                                                                                                              |            |
| Zoom                                     | ON                     | When zoom is applied in<br>'Tactical,<br>Situational<br>or<br>Map' display in SCD Main<br>Window.                                    |            |
|                                          | OFF                    | When zoom removed or<br>reset<br>to<br>default<br>in<br>all<br>displays<br>(Tactical,<br>Situational & Map).                         |            |
| Auto Purge                               | ON                     | If auto purge activity is<br>enforced at ES Processor.                                                                               |            |
|                                          | OFF                    | If auto purge is disabled at<br>ES Processor.                                                                                        |            |
| Audio Alarm                              | 'Track Count'          | If audio alarm notification<br>is<br>enabled<br>in<br>SCD<br>application & auto tones<br>are assigned to particular<br>signal types. |            |
|                                          | DISABLED               | If audio alarm notification<br>is<br>enabled<br>in<br>SCD<br>application.                                                            |            |
| Warner<br>Library                        | 'No.<br>of<br>Entries' | If 'System Emitter Library'<br>is<br>loaded<br>into<br>SCD<br>application.                                                           |            |
|                                          | NONE                   | If<br>NO<br>emitter<br>library<br>is<br>selected.                                                                                    |            |
| Auto<br>Merge<br>Mid-Band<br>(2.2-18GHz) | ON                     | If auto merging of mid<br>band tracks is enforced at<br>ES Processor.                                                                |            |
| Tracks                                   | OFF                    | If auto merging of mid<br>band tracks is disabled at<br>ES Processor.                                                                |            |

SHAKTI : UHB\Ch5 Page 351 of 614

| Parameter                                                                   | Status                                                  | Description                                                                                                                                               | Status GUI |
|-----------------------------------------------------------------------------|---------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| Auto<br>Merge<br>Agile Tracks                                               | ON                                                      | If auto merging of agile<br>tracks is enforced at ES<br>Processor.                                                                                        |            |
|                                                                             | OFF                                                     | If auto merging of agile<br>tracks is disabled at ES<br>Processor.                                                                                        |            |
| Link Status<br>(Consolidate                                                 | UP                                                      | If<br>all<br>the<br>links<br>are<br>established & up.                                                                                                     |            |
| d Link Status<br>of<br>Interfaces<br>(Shakti<br>Sub<br>systems) with<br>SCD | DOWN                                                    | If<br>'All'<br>the<br>links<br>are<br>disconnected/ down. The<br>background color of the<br>status button will be 'Red'.                                  |            |
| Computer)                                                                   | DOWN                                                    | If only 'Some' the links are<br>disconnected/ down. The<br>background colour of the<br>status<br>button<br>will<br>be<br>'Yellow'.                        |            |
| System<br>Recording                                                         | ON                                                      | If 'System Recording' is<br>enabled & started in SCD<br>application.                                                                                      |            |
|                                                                             | OFF                                                     | If 'System Recording' is<br>disabled<br>or<br>stopped<br>in<br>SCD<br>application.<br>Background colour of the<br>indicator will be flashing in<br>'Red'. |            |
| Receiver<br>Pulse Count                                                     | 'Pulse Count'                                           | Receiver<br>pulse<br>count<br>received<br>from<br>ES<br>Processor.                                                                                        |            |
| Receiver<br>Mode                                                            | DIR/<br>DS/<br>SCN/<br>MSN/<br>RFPS/<br>BB/<br>SFB/ BLK | Receiver mode in which a<br>receiver<br>currently<br>operating:<br>DIR: Directed Mode.<br>DS:<br>Directed<br>Search                                       |            |

SHAKTI : UHB\Ch5 Page 352 of 614

| Parameter              | Status                      | Description                                                                                                                                                                                                                                                                                                                                                                                                       | Status GUI |
|------------------------|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
|                        |                             | Mode.<br>SCN: Scan Mode.<br>MSN: Mission Mode.<br>RFPS: RFPS Mode.<br>SFB: Switch Filter Bank.<br>BB: Broad Band Mode.<br>BLK: Receiver Blocked.                                                                                                                                                                                                                                                                  |            |
| Receiver<br>Duty Cycle | 'Duty<br>Cycle<br>% Values' | 'Duty Cycle' information of<br>receiver<br>received<br>from<br>ESI. 'Duty Cycle %' will be<br>split into two values for<br>NBRx2<br>(2.2-18GHz)<br>for<br>2.2-6GHz band & for 6-<br>18GHz band. Note: This<br>indicator will be a toggle<br>indicator<br>to<br>switch<br>between 'Receiver Mode<br>&<br>Receive<br>Duty<br>Cycle'<br>statuses.<br>By<br>default,<br>it<br>shall<br>display<br>'Receiver<br>Mode'. |            |
| Auto BITE              | ON                          | Current<br>state<br>of<br>'Auto<br>BITE'. If 'Auto BITE' is<br>enabled & started in SCD<br>application.                                                                                                                                                                                                                                                                                                           |            |
|                        | OFF                         | If 'Auto BITE' is disabled or<br>stopped<br>in<br>SCD<br>application.<br>Background<br>colour of the indicator will<br>be flashing in 'Red'.                                                                                                                                                                                                                                                                      |            |
| Manual BITE            | ON                          | If<br>ES<br>manual<br>BITE<br>is<br>initiated & is in progress.                                                                                                                                                                                                                                                                                                                                                   |            |
|                        | OFF                         | If<br>ES<br>manual<br>BITE<br>is<br>stopped.<br>Background<br>colour of the indicator will                                                                                                                                                                                                                                                                                                                        |            |

SHAKTI : UHB\Ch5 Page 353 of 614

| Parameter                              | Status                           | Description                                                                                                                                                                                                                                                                                                             | Status GUI |
|----------------------------------------|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
|                                        |                                  | in 'Red'.                                                                                                                                                                                                                                                                                                               |            |
| Lockout<br>Frequencies                 | SET                              | If<br>'Lockout<br>Frequencies'<br>are set (enforced) at ES<br>Processor.                                                                                                                                                                                                                                                |            |
|                                        | NOTSET                           | If<br>'Lockout<br>Frequencies'<br>reset<br>(removed)<br>at<br>ES<br>Processor.                                                                                                                                                                                                                                          |            |
| Lockout<br>Sectors                     | SET                              | If 'Lockout Sectors' are set<br>(enforced)<br>at<br>ES<br>Processor.                                                                                                                                                                                                                                                    |            |
|                                        | NOTSET                           | If 'Lockout Sectors' reset<br>(removed)<br>at<br>ES<br>Processor.                                                                                                                                                                                                                                                       |            |
| Platform<br>Latitude<br>&<br>Longitude | 'Latitude,<br>Longitude<br>Data' | The background shadow<br>will<br>be<br>blinking<br>in<br>green/yellow<br>colour<br>as<br>long as data is received<br>from ESI and updated at<br>SCD. If there is "No" data<br>update<br>from<br>ESI.<br>The<br>background show will be<br>in red colour and there will<br>not<br>be<br>any<br>blinking<br>of<br>shadow. |            |
|                                        | ERROR                            | Error<br>in<br>latitude<br>&<br>longitude<br>data<br>received<br>from<br>ESI.<br>Latitude<br>&<br>longitude values will be<br>replaced by 'ERROR' text<br>in 'Red' colour.                                                                                                                                              |            |
|                                        | OFF                              | No<br>latitude<br>&<br>longitude<br>data<br>from<br>source.<br>Background shadow will<br>change to 'Red' colour.                                                                                                                                                                                                        |            |

SHAKTI : UHB\Ch5 Page 354 of 614

| Parameter           | Status                   | Description                                                                                                                                                                                                                                                                                                             | Status GUI |
|---------------------|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| Platform<br>Gyro    | 'Roll,<br>Pitch<br>Data' | The background shadow<br>will<br>be<br>blinking<br>in<br>green/yellow<br>colour<br>as<br>long as data is received<br>from ESI and updated at<br>SCD. If there is "No" data<br>update<br>from<br>ESI.<br>The<br>background show will be<br>in red colour and there will<br>not<br>be<br>any<br>blinking<br>of<br>shadow. |            |
|                     | ERROR                    | 'Error' flag is reported for<br>roll & pitch data from ESI.<br>Background shadow will<br>change to 'Red' colour.                                                                                                                                                                                                        |            |
|                     | STOPPED                  | User stopped 'Gyro' data<br>from<br>SCD<br>application.<br>Background shadow will<br>change to 'Red' colour.                                                                                                                                                                                                            |            |
|                     | NODATA                   | 'No Data' flag is reported<br>for roll & pitch data from<br>ESI. Background shadow<br>will change to 'Red' colour.                                                                                                                                                                                                      |            |
| Platform<br>Heading | 'Heading<br>Data'        | The background shadow<br>will<br>be<br>blinking<br>in<br>green/yellow<br>colour<br>as<br>long as data is received<br>from ESI and updated at<br>SCD. If there is "No" data<br>update<br>from<br>ESI.<br>The<br>background show will be<br>in red colour and there will<br>not<br>be<br>any<br>blinking<br>of<br>shadow. |            |

SHAKTI : UHB\Ch5 Page 355 of 614

| Parameter          | Status                          | Description                                                                                                                                                  | Status GUI |
|--------------------|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
|                    | ERROR                           | 'Error' flag is reported for<br>heading data from ESI.<br>Background shadow will<br>change to 'Red' colour.                                                  |            |
|                    | STOPPED                         | User<br>stopped<br>heading<br>data<br>from<br>SCD<br>application.<br>Background<br>shadow<br>will<br>change<br>to<br>'Red' colour.                           |            |
|                    | NODATA                          | 'No Data' flag is reported<br>for heading data from ESI.<br>Background shadow will<br>change to 'Red' colour.                                                |            |
| Map Status         | IN RANGE                        | If a map is loaded into<br>SCD application and if the<br>reported<br>latitude<br>&<br>longitude of the Platform is<br>falling within map range.              |            |
|                    | OUT OF<br>RANGE                 | If a map is loaded into<br>SCD application but the<br>reported<br>latitude<br>&<br>longitude of the Platform is<br>NOT<br>falling<br>within<br>map<br>range. |            |
|                    | NOT<br>AVAILABLE                | If NO map is loaded into<br>SCD application.                                                                                                                 |            |
| SCD Up Time        | 'Elapsed<br>Time<br>(hh:mm:ss)' | When SCD application is<br>started in 'Online/ Replay/<br>Simulation' mode.                                                                                  |            |
| Database<br>Status | ACTIVE                          | If<br>SCD<br>application<br>database<br>is<br>active<br>and<br>running.                                                                                      |            |
|                    | NOT<br>ACTIVE                   | If<br>SCD<br>application<br>database is NOT active or                                                                                                        |            |

SHAKTI : UHB\Ch5 Page 356 of 614

| Parameter | Status | Description                                                                          | Status GUI |
|-----------|--------|--------------------------------------------------------------------------------------|------------|
|           |        | down. Background color<br>of<br>the<br>indicator<br>will<br>be<br>flashing in 'Red'. |            |

- 5.5.4.2.23.1 User shall place mouse cursor on any one these status indicators to see explanation (tool tip text) about that indicator.
- 5.5.4.2.23.2 The following status indicator buttons will act as action buttons to show their corresponding GUI or to switch modes:
- 5.5.4.2.23.3 "Display Mode, Display Filter, Auto Purge, Audio Alarm, Warner Lib, Merge MB, Merge Agile, Link Status, Recording, 'Receiver Modes', AutoBITE, Man.BITE, Lockout Freq., Lockout Sect., Roll Pitch, Map Status, SCD Up Time".
- 5.5.4.2.23.4 Example 1: If user clicks on 'Lockout Sect.' status indicator button, 'GUI to Set Lockout Sectors at ES Processor' will be displayed with existing settings.
- 5.5.4.2.23.5 Example 2: If user clicks on 'Display Mode' status indicator button, display mode of SCD Main Window will be switched to 'RELATIVE' (if it was in 'TRUE' mode earlier) & vice versa.
- 5.5.4.2.23.6 When default settings of SCD application are changed (altered) then the status shall be displayed to draw attention of user.
- 5.5.4.2.23.7 Background of shadow of a status indicator button shall be shown in 'Red' color if there is a change in its default state. For example: If a display filter is applied in SCD Main Window, then 'Display Filter' status button will be displayed as shown in **Figure-5.240**.

![](_page_360_Picture_9.jpeg)

**Figure-5.240: Status Indicator with Display Filter ON – SCD Main Window**

**5.5.4.2.24 Application Tool Bar**.Tool bar (as shown in **Figure-5.241**) of SCD Main Window shall contain short cut buttons (tool buttons) to the most recently used (executed) EW operations. Tool buttons representing similar (logically related) functionalities shall be grouped together on this tool bar. Each tool button shall have a tool tip text and it shall be displayed when user places mouse cursor on it. These tool buttons shall be in sync with

SHAKTI : UHB\Ch5 Page 357 of 614

'EW System Status Indicator Buttons' & menu items of drop-down menus.

![](_page_361_Picture_2.jpeg)

**Figure-5.241: Application Tool Bar – SCD Main Window.**

5.5.4.2.24.1 The functionalities of tool buttons are described in **Table 5.9**. Refer 'Application Menu Bar & Drop-Down Menus' **section (5.5.4.3.1**) for description on the terms mentioned in this table.

**Table-5.9: SCD Tool Bar Buttons & their Functions**

| Tool Button | Description                        | Expected Behaviour after<br>Mouse Click                                                                                                                      |
|-------------|------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
|             | Switch to 'Tabular<br>Display'     | 'Tabular Display' shall be displayed. The tool<br>button shall be highlighted (default).                                                                     |
|             | Switch to 'Tactical<br>Display'    | 'Tactical Display' shall be displayed. The tool<br>button shall be highlighted.                                                                              |
|             | Switch to 'Situational<br>Display' | 'Situational Display' shall be displayed. The<br>tool button shall be highlighted.                                                                           |
|             | Switch to 'Map<br>Display'         | 'Map Display' shall be displayed. The tool<br>button shall be highlighted.                                                                                   |
|             | Apply 'Sector Zoom'                | 'Zoom Sector' GUI shall be displayed to user.<br>If sector zoom is applied, emitters falling only<br>in the sector<br>shall be displayed.                    |
|             | Remove 'Sector<br>Zoom'            | Sector zoom shall be removed &all<br>emitters<br>(which were under sector zoom) shall be<br>displayed again. By default, no sector zoom<br>shall be applied. |
|             | Zoom on 'Known<br>Emitters'        | Show only 'Known'<br>emitters in all emitter<br>presentation windows.                                                                                        |
|             | Zoom on 'Unknown<br>Emitters'      | Show only 'Unknown'<br>emitters in all emitter<br>presentation windows.                                                                                      |
|             | Zoom on 'Hostile<br>Emitters'      | Show only 'Hostile'<br>emitters in all emitter<br>presentation windows.                                                                                      |
|             | Reset 'Zoom'                       | Remove zoom (including sector zoom) on all                                                                                                                   |

SHAKTI : UHB\Ch5 Page 358 of 614

| Tool Button | Description                                                         | Expected Behaviour after                                                                                                                                                                                                                                                     |
|-------------|---------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|             |                                                                     | Mouse Click                                                                                                                                                                                                                                                                  |
|             |                                                                     | emitter presentation windows and display all<br>emitters. By default, no zoom shall be applied.                                                                                                                                                                              |
|             | Switch to 'True'<br>/'Relative' Mode                                | Switch all 'Emitter Presentation Windows' to<br>'True Mode' otherwise switch all 'Emitter<br>Presentation Windows' to 'Relative Mode'. By<br>default True mode                                                                                                               |
|             | Capture Full Screen<br>Image                                        | Screen shot image of complete SCD Main<br>Window screen shall be captured and stored in<br>a file on SCD storage with auto generated file<br>name.                                                                                                                           |
|             | Capture Active<br>Window Image                                      | Screen shot image of currently opened GUI on<br>SCD Main Window shall be captured and<br>stored in a file on SCD storage with auto<br>generated file name.                                                                                                                   |
|             | Apply 'Display Filters'                                             | Apply<br>user<br>selected<br>filters<br>on<br>'Emitter<br>Presentation Windows'.                                                                                                                                                                                             |
|             | Remove 'Display<br>Filters'                                         | Remove all the displays filters applied by user.<br>By default, no display filters shall be applied.                                                                                                                                                                         |
|             | Enable 'Auto Purge'/<br>Disable 'Auto Purge'                        | 'Enable/ Disable Auto Purge' GUI shall be<br>displayed to user. If user select 'Auto Purge<br>ON', it is enable & applied at ES Processor. If<br>user select 'Auto Purge' OFF', passive tracks<br>shall be disabled at ES Processor. By default,<br>this shall be the state. |
|             | NB Rx1 (0.175-<br>2.2GHz) Directed<br>Mode/ Directed<br>Search Mode | 'NB<br>Rx1<br>(0.175-2.2GHz)<br>Directed<br>Mode/<br>Directed Search Mode' GUI shall be displayed<br>to user put the receiver in 'Directed Mode/<br>Directed Search Mode' when user is logged<br>with 'Administrator'/ 'Commander or Operator'<br>access rights.             |
|             | NB Rx2 (2.2-18GHz)                                                  | 'NB Rx2 (2.2-18GHz) Directed Mode/ Directed                                                                                                                                                                                                                                  |

SHAKTI : UHB\Ch5 Page 359 of 614

| Tool Button | Description                                                                              | Expected Behaviour after                                                                                                                                                                                                            |
|-------------|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|             |                                                                                          | Mouse Click                                                                                                                                                                                                                         |
|             | Directed Mode/<br>Directed Search<br>Mode                                                | Search Mode' GUI shall be displayed to user<br>put the receiver in 'Directed Mode/ Directed<br>Search<br>Mode'<br>when<br>user<br>is<br>logged<br>with<br>'Administrator'/<br>'Commander<br>or<br>Operator'<br>access rights.       |
|             | Set Lockout<br>Frequency Bands                                                           | GUI to set 'Lockout Frequency Bands' shall be<br>displayed to user. If set successfully, the same<br>shall<br>be<br>applied<br>in<br>'Emitter<br>Presentation<br>Windows'.                                                          |
|             | Remove Lockout<br>Frequency Bands                                                        | GUI to remove (reset) 'Lockout Frequency<br>Bands' shall be displayed to user. If set<br>successfully, the same shall be applied in<br>'Emitter Presentation Windows'. By default, no<br>lockout frequency bands shall be enforced. |
|             | Set Lockout Sectors                                                                      | GUI to set 'Lockout Sectors' shall be displayed<br>to user. If set successfully, the same shall be<br>applied in 'Emitter Presentation Windows'.                                                                                    |
|             | Remove Lockout<br>Sectors                                                                | GUI to remove (reset) 'Lockout Sectors' shall<br>be displayed to user. If set successfully, the<br>same shall be applied in 'Emitter Presentation<br>Windows'. By default, no lockout sectors shall<br>be enforced.                 |
|             | Purge Passive<br>Tracks                                                                  | 'Purge Passive Tracks' message shall be sent<br>to ES Processor. If successful, passive tracks<br>shall be purged.                                                                                                                  |
|             | Rebuild Tracks                                                                           | 'Rebuild Tracks' message shall be sent to ES<br>Processor. ES tracks shall be removed from<br>'Emitter Presentation Windows' if successful.                                                                                         |
|             | Enable 'Auto Merge<br>of Mid-Band Tracks'/<br>Disable 'Auto Merge<br>of Mid-Band Tracks' | GUI to 'Merge Mid-Band Tracks' shall be<br>displayed to user. If auto merge is enabled &<br>applied,<br>the<br>same<br>shall<br>be<br>sent<br>to<br>ES<br>Processor.                                                                |

SHAKTI : UHB\Ch5 Page 360 of 614

| Tool Button | Description                                  | Expected Behaviour after<br>Mouse Click                                                                                                                                                                                                               |
|-------------|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|             |                                              | Auto merging of mid-band tracks shall be<br>disabled at ES Processor. This shall be the<br>default state.                                                                                                                                             |
|             | Set Forbidden<br>Frequency Bands             | GUI to set 'Forbidden Frequency Bands' shall<br>be displayed to user. If set successfully, the<br>same shall be applied in 'Emitter Presentation<br>Windows'.                                                                                         |
|             | Remove Forbidden<br>Frequency Bands          | GUI to remove (reset) 'Forbidden Frequency<br>Bands' shall be displayed to user. If set<br>successfully, the same shall be applied in<br>'Emitter Presentation Windows'. By default, no<br>forbidden frequency bands shall be enforced.               |
|             | Set Forbidden<br>Sectors                     | GUI<br>to<br>set<br>'Forbidden<br>Sectors'<br>shall<br>be<br>displayed to user. If set successfully, the same<br>shall<br>be<br>applied<br>in<br>'Emitter<br>Presentation<br>Windows'.                                                                |
|             | Remove Lockout<br>Sectors                    | GUI to remove (reset) 'Forbidden Sectors'<br>shall be displayed to user. If set successfully,<br>the<br>same<br>shall<br>be<br>applied<br>in<br>'Emitter<br>Presentation<br>Windows'.<br>By<br>default,<br>no<br>forbidden sectors shall be enforced. |
|             | Add Track to<br>Temporary Emitter<br>Library | 'Temporary<br>Emitter<br>Library'<br>GUI<br>shall<br>be<br>displayed to user for adding selected track to<br>the library.                                                                                                                             |
|             | Start /Stop 'System<br>Recording'            | SCD 'System Recording' shall be started, if not<br>started already. By default, recording shall be<br>started.<br>SCD 'System Recording' shall be stopped, if<br>already started.                                                                     |
|             | Show/ Hide 'Link &<br>Self-Test Status' GUI  | This shall be a toggling button. By<br>default, 'Link<br>&<br>Self-Test<br>Status'<br>GUI<br>shall<br>be<br>hidden<br>whenever SCD Main Window is activated.                                                                                          |

SHAKTI : UHB\Ch5 Page 361 of 614

| Tool Button | Description                                | Expected Behaviour after<br>Mouse Click                                                                                                                                                                                         |
|-------------|--------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|             | Show/ Hide 'Replay<br>Controls' GUI        | This shall be a toggling button. When toggled,<br>'Replay Controls' GUI shall be visible/ hidden.<br>This<br>button<br>&<br>the<br>GUI<br>shall<br>be<br>visible,<br>whenever SCD Main Window is activated in<br>'Replay Mode'. |
|             | Show/ Hide<br>'Simulation Controls'<br>GUI | This shall be a toggling button. When toggled,<br>'Simulation Controls' GUI shall be visible/<br>hidden. This button & the GUI shall be visible,<br>whenever SCD Main Window is activated in<br>'Simulation Mode'.              |

**5.5.4.2.25 Graphical Window**.Intercepted emitter data shall be presented in 'Graphics Window' for easy appreciation and fast reaction by the user. Graphics Window shall contain the following displays and only one display shall be active at any given time when selected by the user.

- (a) Tactical Display.
- (b) Situational Display.
- (c) Map Display.

5.5.4.2.25.a Graphics Window shall be hidden when 'Tabular Window' (explained in the coming section) is selected and shall be visible when any one of these displays is selected. In each display of 'Graphics Window', appropriate context menus shall be provided for quick access to functionalities.

5.5.4.2.25.b Active/ passive tracks (500 maximum), manual BITE tracks (minimum 4) & auto BITE (minimum 88 tracks) shall be presented in this display. The emitter data update rate will be @1 second. Symbols and Color Scheme of Tracks (Emitters)

5.5.4.2.25.c The following color codes shall be used for different types of emitters on the display as shown in **Table 5.10**.

SHAKTI : UHB\Ch5 Page 362 of 614

**Table-5.10: Types of Emitters and their Colour Codes**

| Track Type                        | Color  |
|-----------------------------------|--------|
| Hostile/ Warned/<br>Lock-On Track | Red    |
| Unknown Track                     | Yellow |
| Known Track                       | Green  |
| Passive Track                     | White  |
| Spurious Track                    | Grey   |
| Manual BITE Track                 | Orange |
| Auto BITE Track                   | Cyan   |

5.5.4.2.25.d Library match identity details shall be displayed along with tracks. Track labels, if selected by user', such as' Platform Type, Library Match Number or Track Number' shall be displayed with along with a track on the display. List of Naval Tactical Display System (NTDS) symbols used for Platform representation are shown in **Figure-5.242**. The colour of these emitter labels shall be same as track colour. Manual BITE & Auto BITE tracks will be represented with 'Unknown' NTDS symbol.

![](_page_366_Figure_4.jpeg)

**Figure-5.242: NTDS Symbols in Graphics Display – SCD Main Window**

**5.5.4.2.25.1 Tactical Display**.'Tactical Display' in 'Graphics Window' shall present emitter data in a Polar chart with axes being DOA & amplitude of the emitter. The display shall be divided into three concentric annular regions each circle divided into four quadrants covering 360 degrees in polar co-ordinate system format. The GUI for 'Tactical Display' is

SHAKTI : UHB\Ch5 Page 363 of 614

shown in **Figure-5.243.**

![](_page_367_Figure_2.jpeg)

**Figure-5.243: Tactical Display GUI – SCD Main Window**

- (a) Each annular region shall hold a particular category of intercepted emitters (tracks). In the inner most annular region 'Warner' and high potential threats (CW & Lock-On emitters) shall be presented in 'Red' color. In the intermediate annular region 'Unknown' (un-identified emitters other than CW & Lock-On)shall be presented in 'Yellow' color. In the outer annular region 'Known' emitters (other than CW & Lock-On)shall be presented 'Green' color. Passive emitters in all the three regions shall be presented in 'White' color. Spurious emitters in all the three regions shall be presented in 'Grey' color. The emitters under jamming shall be enclosed by a flashing square with 'Red' border lines. Each of the intercepted emitter shall be represented by emitter number, NTDS symbol and a matching entry number in 'System Emitter Library'.
- (b) The intercepted emitters shall be plotted with:
- (c) Angular position given by difference of Direction of Arrival (DOA) of the signal

SHAKTI : UHB\Ch5 Page 364 of 614

with respect to 'True North' (in case of 'True' mode) or Platform's heading (in case of 'Relative' mode).

- (d) Radial distance from its inner circle, which shall be proportional to the amplitude of the intercepted signal. The signal with higher amplitude shall be closer to the center of the circle (but within its circle).
- (e) The heading of the Platform with respect to 'True North' (with letter 'H' at the end of the line) shall be presented as a pink radius line away from the north line by its value in true mode or at the north line (0 degree, with letter 'N' at the end of the line) itself in case of 'Relative' mode. There shall be provision to swap alignment of the emitters from 'True North' to Platform's heading ('Relative' Mode). Emitters shall be displayed as per the display filters selected.
- **5.5.4.2.25.1.1 Context Menu in Tactical Display**.If user clicks mouse right button on a track in this display, a context menu (as shown in **Figure-5.244**) shall be displayed with the following of options:
  - (a) Show Emitters Watch Window.
  - (b) Add Track to Hook Up Window.
  - (c) Add Track to Temp. Library.
  - (d) Add Track to ELINT Returns
  - (e) ESM Operations:
    - (i) Get PD Data.
    - (ii) Get Scan Type.
    - (iii) Rebuild Tracks.
    - (iv) Purge Passive Tracks.
    - (v) Set Track Build Criteria.
    - (vi) Set Lockout Frequency Bands.
    - (vii) Set Lockout Sectors.
    - (viii) Load Warner Library.
  - (f) RPFS Operations:
    - (i) Finger Print a Track.
    - (ii) Finger Print Track with DRTG

SHAKTI : UHB\Ch5 Page 365 of 614

- (iii) Record Data at RFPS.
- (g) ECM Operations:
  - (i) Track.
  - (ii) Track & Jam.
  - (iii) Jam.
  - (iv) Stop Jam.
  - (v) Break Track.
  - (vi) Modify Jamming Technique.
- (h) Send Track to LRSAM.
- (j) Send Track to KAVACH.
- (k) DOA Trace.

![](_page_369_Picture_12.jpeg)

**Figure-5.244: Track Context Menu in Tactical Display – SCD Main Window.**

5.5.4.2.25.1.1.1 If user clicks mouse right button in non-track area (not on a particular track), a context menu (as shown in **Figure-5.245**) shall be displayed with the following of options:

- (l) Display Filters.
  - (i) Track Status.
  - (ii) Bands & Sectors.
  - (iii) Receiver Type.

SHAKTI : UHB\Ch5 Page 366 of 614

- (iv) Time of Arrival.
- (v) Scan Type.
- (vi) PRF Type.
- (vii) Frequency Type.
- (viii) Threat Type.
- (ix) Operational Type.
- (x) Platform Type.
- (xi) Emitter Labels.
- (xii) Manage All Filters.
- (xiii) Reset All Filters to Default.
- (m) Zoom/ Select.
  - (i) Sector.
  - (ii) Track.
  - (iii) Hostile.
  - (iv) Known.
  - (v) Unknown.

![](_page_370_Picture_17.jpeg)

**Figure-5.245: Non-Track Context Menu in Tactical Display – SCD Main Window**

**5.5.4.2.25.2 Situational Display**.'Situational Display' in 'Graphics Window', shall present emitter data in Cartesian chart with axes being DOA & frequency of the emitter. The GUI for 'Situational Display' is shown in **Figure-5.246**.

SHAKTI : UHB\Ch5 Page 367 of 614

![](_page_371_Figure_1.jpeg)

**Figure-5.246: Situational Display GUI – SCD Main Window**

- (a) In this display, each intercepted emitter shall symbolically be presented in Cartesian Co-ordinate system with frequency along Y – axis and DOA along X – axis. Y – Axis shall cover the frequency range from 0.175 to 40 GHz in four bands, each band occupying proportionate space on the graph. X – Axis shall represent DOA from 0 to 360 degrees in four columns:
- (b) Beginning from 0 to 360 degrees (0-90, 90-180, 180-270 & 270-360) in 'True' mode.
- (c) Beginning from 180 to 180 degrees (180-270, 270-0, 0-90 & 90-180) in 'Relative' mode. The colour code and identification scheme for presenting emitters in this display shall be same as that of 'Tactical Display'.

SHAKTI : UHB\Ch5 Page 368 of 614

**5.5.4.2.25.2.1 Context Menu in Situational Display**.If user clicks mouse right button on a track in this display, a context menu (as shown in **Figure-5.247**) same as shown in 'Tactical Display' shall be displayed.

![](_page_372_Picture_2.jpeg)

**Figure-5.247: Track based Context Menu in Situational Display**

5.5.4.2.25.2.a If user clicks, mouse right button in non-track area (not on a particular track), a context menu (as shown in **Figure-5.248**) shall be displayed with the following of options:

- (a) Display Filters.
  - (i) Track Status.
  - (ii) Bands & Sectors.
  - (iii) Receiver Type.
  - (iv) Time of Arrival.
  - (v) Scan Type.
  - (vi) PRF Type.
  - (vii) Frequency Type.
  - (viii) Threat Type.
  - (ix) Operational Type.
  - (x) Platform Type.

SHAKTI : UHB\Ch5 Page 369 of 614

- (xi) Emitter Labels.
- (xii) Manage All Filters.
- (xiii) Reset All Filters to Default.
- (b) Zoom/ Select.
  - (i) Zoom Current Band
  - (ii) A-Band (0 250MHz).
  - (iii) B-Band (250 500MHz).
  - (iv) C-Band (500 1000MHz).
  - (v) D-Band (1 2GHz).
  - (vi) E-Band (2 3GHz).
  - (vii) F-Band (3 4GHz).
  - (viii) G-Band (4 6GHz).
  - (ix) H-Band (6 8GHz).
  - (x) I-Band (8 10GHz).
  - (xi) J-Band (10 20GHz).
  - (xii) K-Band (20 40GHz).
  - (xiii) Reset Zoom

![](_page_374_Picture_1.jpeg)

**Figure-5.248: Context Menu Display Filters in Situational Display**

![](_page_374_Picture_3.jpeg)

**Figure-5.249: Context menu Zoom option in Situational display**

5.5.4.2.25.2.b Rubber Band Zooming: There shall be provision for rubber band zooming of selected area in this display. User shall place mouse cursor in the area of interest, press & hold mouse left button and drag it. Display region will be zoomed and tracks falling only in that region will be displayed. User shall click 'Reset Zoom' option to reset (remove) any zoom applied in this display.

SHAKTI : UHB\Ch5 Page 371 of 614

**5.5.4.2.25.3 Map Display**. 'Map Display' in 'Graphics Window' shall present the instantaneous tactical picture of intercepted emitters as on overlay on 'Geo Tiff' based to user. The same colour code and identification scheme followed in 'Tactical Display' shall be followed here in 'Map Display' for representing track data. Map specific features, as mentioned below, shall be provided on this display.

- (a) Moving Map or Moving Platform.
- (b) Zooming & Panning on Map.
- (c) Downloading/ Unloading of Maps into/ from the SCD System.
- (d) Measuring Distance between Two Points of Interest.
- (e) Show/ Hide Annotations, Way Points, Platform Path on Map.
- (f) Show and Update Platform Position on Map.

5.5.4.2.25.3.a Platform latitude, longitude & heading will be received from Ship Data Network (SDN) through External System Interface (ESI) of Shakti EW system.

**Note**: **For performing map related functionalities, user shall active 'Map Display' from 'Display' menu.**

5.5.4.2.25.3.b The GUI for 'Map Display' is shown in **Figure-5.250**.

![](_page_375_Figure_11.jpeg)

**Figure-5.250: Map Display GUI**

SHAKTI : UHB\Ch5 Page 372 of 614

| 5.5.4.2.25.3.1 | Context Menu in Map Display.<br>If user clicks mouse right button in non<br>track area (not on a particular track), a context menu (as shown in Figure 5.251) shall be<br>displayed with the following of options: |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| (a)            | Mode.                                                                                                                                                                                                              |
|                | (i)<br>Moving Platform.                                                                                                                                                                                            |
|                | (ii)<br>Moving Map.                                                                                                                                                                                                |
|                | (iii)<br>Pan Mode.                                                                                                                                                                                                 |
| (b)            | Zoom.                                                                                                                                                                                                              |
|                | (i)<br>Zoom In.                                                                                                                                                                                                    |
|                | (ii)<br>Zoom Out.                                                                                                                                                                                                  |
|                | (iii)<br>Reset Zoom.                                                                                                                                                                                               |
| (c)            | Tactical Impose.                                                                                                                                                                                                   |
| (d)            | Spokes.                                                                                                                                                                                                            |
|                | (i)<br>Show.                                                                                                                                                                                                       |
|                | (ii)<br>Hide.                                                                                                                                                                                                      |
| (e)            | Annotations.                                                                                                                                                                                                       |
|                | (i)<br>Add Annotations.                                                                                                                                                                                            |
|                | (ii)<br>Show All.                                                                                                                                                                                                  |
|                | (iii)<br>Hide All.                                                                                                                                                                                                 |
|                | (iv)<br>Manage.                                                                                                                                                                                                    |
| (f)            | Way Points.                                                                                                                                                                                                        |
|                | (i)<br>Add Way Points.                                                                                                                                                                                             |
|                | (ii)<br>Show All.                                                                                                                                                                                                  |
|                | (iii)<br>Hide All.                                                                                                                                                                                                 |
|                | (iv)<br>Manage.                                                                                                                                                                                                    |
| (g)            | Find Distance & Bearing.                                                                                                                                                                                           |
|                | (i)<br>Using Mouse.                                                                                                                                                                                                |

SHAKTI : UHB\Ch5 Page 373 of 614

(ii) Between Two Points.

- (iii) Between Platform & Point.
- (iv) Manual Entry.
- (v) Remove Line.
- (vi) Reset to Default.

![](_page_377_Picture_5.jpeg)

**Figure 5.251: Map Specific Context Menu in Map Display**

**Note: Map specific context menu will only be provided when tactical imposition is not applied in this display. The functionalities pertaining to the menu items in this context menu shall be same as 'Map' menu items in SCD application menu bar.**

**5.5.4.2.25.3.2 Rubber Band Zooming**.There shall be provision for rubber band zooming of selected area in this display. User shall place mouse cursor in the area of interest, press & hold mouse left button and drag it. User shall click 'Reset Zoom' option to reset (remove) any zoom applied in this display.

**5.5.4.2.25.3.3 Map Specific Tool Bar**.Map specific tool bar, as shown in **Figure-5.252**, shall be provided on this display.

SHAKTI : UHB\Ch5 Page 374 of 614

![](_page_378_Picture_1.jpeg)

**Figure-5.252: Tool Bar in Map Display – SCD Main Window**

5.5.4.2.25.3.3.1 The functionalities of tool buttons are described in **Table 5.11**. Refer 'Map' menu section (5.5.4.3.1.3) for description on the terms mentioned in this table.

**Table-5.11: Map Tool Bar Buttons & their Functions**

SHAKTI : UHB\Ch5 Page 375 of 614

| Tool Button | Description        | Expected Behaviour after                                                    |
|-------------|--------------------|-----------------------------------------------------------------------------|
|             |                    | Mouse Click                                                                 |
|             | Show Latest        | Latest path of Platform shall be shown on                                   |
|             | Platform Path      | 'Map Display' if user selects this tool                                     |
|             |                    | button.                                                                     |
|             | Pan on Map         | Map mode shall be switched to 'Pan'                                         |
|             |                    | mode and user shall use mouse left                                          |
|             |                    | button to pan on map.                                                       |
|             | Zoom Out           | Selected area shall be zoomed out on                                        |
|             |                    | map.                                                                        |
|             | Zoom In            | Selected area shall be zoomed in on                                         |
|             |                    | map.                                                                        |
|             | Reset Zoom         | Zoom shall be reset (removed) on map.                                       |
|             |                    |                                                                             |
|             | List of Map Layers | A GUI shall be displayed with list of map                                   |
|             |                    | layers (selected map files, way points) for                                 |
|             |                    | selecting/ deselecting them.                                                |
|             | Load Maps          | A GUI shall be displayed with list of map                                   |
|             |                    | available maps<br>on SCD<br>storage<br>for                                  |
|             |                    | loading them into SCD application.                                          |
|             | Super Impose       | This will be a toggle button. Tactical                                      |
|             | Tactical Picture   | picture shall be displayed/ hidden if user                                  |
|             |                    | checks/ unchecks this tool button.                                          |
|             | Show/ Hide         | This will be a toggle button. Spokes                                        |
|             | Spokes             | (emitter DOA lines) shall be displayed/                                     |
|             |                    | hidden if user checks/ unchecks this tool                                   |
|             |                    | button.                                                                     |
|             | Show/ Hide         | This will be a toggle button. Annotations                                   |
|             | Annotations        | shall be displayed/ hidden if user checks/                                  |
|             |                    | unchecks this tool button.                                                  |
|             | Show/ Hide Way     | This will be a toggle button. Way points                                    |
|             | Points             | shall be displayed/ hidden if user checks/                                  |
|             | Switch to Moving   | unchecks this tool button.<br>This will be tri-state toggle button. If user |
|             | Platform/ Moving   | clicks on this tool button; display shall be                                |
|             | Map/ Pan Mode      | switched to 'Moving Platform, Moving                                        |
|             |                    | Map or Pan' mode w.r.t. state of the tool                                   |
|             |                    | button.                                                                     |
|             |                    |                                                                             |

SHAKTI : UHB\Ch5 Page 376 of 614

| Tool Button | Description                                              | Expected Behaviour after<br>Mouse Click                                                                                                                                       |
|-------------|----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|             | Show Full Map                                            | Show complete map on display with full<br>extents of map fitting into 'Map Display'<br>area.                                                                                  |
|             | Show/ Hide Grid<br>Lines on Map                          | This will be toggle button. Grid lines<br>(latitude<br>&<br>longitude<br>lines)<br>shall<br>be<br>displayed/<br>hidden<br>if<br>user<br>checks/<br>unchecks this tool button. |
|             | Measure Distance<br>Between Two<br>Points on Map         | User shall be allowed to select two points<br>on map using mouse to find distance &<br>bearing between them.                                                                  |
|             | Measure Distance<br>Between Platform<br>& a Point on Map | User shall be allowed to select a point on<br>map using mouse to find distance &<br>bearing of this point from current Platform<br>position.                                  |
|             | Show Mouse<br>Pointer on Map                             | Mouse point shall be displayed on map.<br>Any functionality if assigned to mouser<br>cursor shall cease to work.                                                              |

**5.5.4.2.25.4 Tabular Display**.Parameters of all the intercepted emitters shall be presented in textual format in 'Tabular Display' mode, as shown in **Figure-5.253**. The colour codes and identification scheme for displaying emitters in this display shall be same as that of 'Tactical & Situational Display'. 'Tabular Display' shall include 'Emitter Report Window' & 'Latest Emitters Window' which are described below.

SHAKTI : UHB\Ch5 Page 377 of 614

| TNo | BRG   | Rx.   | Freq.    | F.Type | P.Type | PW     | PRF    | PRFType | RadarName | CL | Amp. | ST  | ASP    | TOFA     | TOLA     | Platform |
|-----|-------|-------|----------|--------|--------|--------|--------|---------|-----------|----|------|-----|--------|----------|----------|----------|
| 15  | 22    | BBRx2 | 37154.34 | CH     | LU     | 990.4  | 226130 | D10     |           |    | -64  | CR  | 3.415  | 00:06:27 | 00:07:12 |          |
| 14  | 357.1 | BBRx2 | 37154.34 | AGP    | RG     | 719.67 | 92727  | J28%    |           |    | -61  |     | 14.376 | 00:06:27 | 00:07:11 |          |
| 13  | 331.4 | BBRx2 | 31465.06 | CH     | LD     | 879.41 | 199586 | J5%     |           |    | -58  | HE  | 19.483 | 00:06:27 | 00:07:11 |          |
| 12  | 305.7 | BBRx2 | 31465.06 | AGP    | LU     | 393.78 | 161544 | H6%     |           |    | -55  | TWS | 12.324 | 00:06:27 | 00:07:11 |          |
| 11  | 281   | NBRx2 | 493      | AGP    |        | 690.84 | 102991 |         |           |    | -53  |     |        | 00:06:27 | 00:07:13 |          |
| 10  | 255.3 | NBRx2 | 495      | AGP    |        | 552.22 | 451642 |         |           |    | -50  |     |        | 00:06:27 | 00:07:13 |          |
| 9   | 229.6 | NBRx2 | 2100     | AGP    | LD     | 844.07 | 271156 | W30%    |           |    | -47  | SS  | 11.995 | 00:06:27 | 00:07:12 |          |
| 8   | 203.9 | BBRx2 | 18000    | F      | RG     | 499.93 | 193811 | H27%    |           |    | -90  | CR  | 13.937 | 00:06:27 | 00:07:12 |          |
| 7   | 178.2 | NBRx2 | 15000    | CW     | FMC    | 752.22 | 203499 |         |           |    | -87  |     |        | 00:06:27 | 00:07:12 |          |
| 6   | 152.5 | BBRx1 | 10000    | AGP    | PM     | 623.82 | 362889 | H14%    |           |    | -84  | HE  | 16.678 | 00:06:27 | 00:07:12 |          |
| 5   | 126.8 | NBRx2 | 500      | CH     | LD     | 24.18  | 423304 | H25%    |           |    | -81  | TWS | 13.598 | 00:06:27 | 00:07:12 |          |
| 4   | 101.1 | NBRx1 | 400      | AGS    | FM     | 337.76 | 134137 |         |           |    | -78  | CS  | 8.01   | 00:06:27 | 00:07:12 |          |
| 3   | 75.4  | NBRx1 | 350      | F      | PM     | 128.37 | 158467 | W12%    |           |    | -75  | LK  |        | 00:06:27 | 00:07:12 |          |
| 2   | 49.7  | NBRx1 | 250      | AGP    |        | 642.34 | 468227 |         |           |    | -72  |     | 7.99   | 00:06:27 | 00:07:12 |          |
| 1   | 24    | NBRx1 | 200      | AGP    | RG     | 816.94 | 56512  | J8%     |           |    | -69  | CR  | 5.377  | 00:06:27 | 00:07:12 |          |
|     |       |       |          |        |        |        |        |         |           |    |      |     |        |          |          |          |
| TNo | BRG   | Rx.   | Freq.    | F.Type | P.Type | PW     | PRF    | PRFType | RadarName | CL | Amp. | ST  | ASP    | TOFA     | TOLA     | Platform |
| 1   | 24    | NBRx1 | 200      | AGP    | RG     | 816.94 | 56512  | J8%     |           |    | -69  | CR  | 5.377  | 00:06:27 | 00:07:12 |          |
| 2   | 49.7  | NBRx1 | 250      | AGP    |        | 642.34 | 468227 |         |           |    | -72  |     | 7.99   | 00:06:27 | 00:07:12 |          |
| 3   | 75.4  | NBRx1 | 350      | F      | PM     | 128.37 | 158467 | W12%    |           |    | -75  | LK  |        | 00:06:27 | 00:07:12 |          |
| 4   | 101.1 | NBRx1 | 400      | AGS    | FM     | 337.76 | 134137 |         |           |    | -78  | CS  | 8.01   | 00:06:27 | 00:07:12 |          |
| 5   | 126.8 | NBRx2 | 500      | CH     | LD     | 24.18  | 423304 | H25%    |           |    | -81  | TWS | 13.598 | 00:06:27 | 00:07:12 |          |
| 6   | 152.5 | BBRx1 | 10000    | AGP    | PM     | 623.82 | 362889 | H14%    |           |    | -84  | HE  | 16.678 | 00:06:27 | 00:07:12 |          |

**Figure-5.253: Tabular Display GUI – SCD Main Window**

SHAKTI : UHB\Ch5 Page 378 of 614

**5.5.4.2.25.4.1 Emitter Report Window**. **'**Emitter Report Window' shall display & update the parameters of intercepted emitters in text format in table.The GUI for this window is shown in **Figure-5.254**.

| TNo | BRG   | Rx.   | Freq.    | F.Type | P.Type | PW     | PRF    | PRFType | RadarName | CL | Amp.            | ST  | ASP    | TOFA     | TOLA     | Platform |
|-----|-------|-------|----------|--------|--------|--------|--------|---------|-----------|----|-----------------|-----|--------|----------|----------|----------|
| 15  | 59    | BBRx2 | 37154.34 | CH     | LU     | 990.4  | 226130 | D10     |           |    | <b>-</b> 55     | CR  | 3,415  | 00:06:27 | 00:08:07 |          |
| 14  | 34    | BBRx2 | 37155.34 | AGP    | RG     | 719.67 | 92727  | J28%    |           |    | -52             |     | 14.376 | 00:06:27 | 00:08:07 |          |
| 13  | 8     | BBRx2 | 31465.06 | CH     | LD     | 879.41 | 199586 | J5%     |           |    | <b>-</b> 49     | HE  | 19.483 | 00:06:27 | 00:08:07 |          |
| 12  | 342.7 | BBRx2 | 31466.06 | AGP    | LU     | 393.78 | 161544 | H6%     |           |    | <b>-</b> 46     | TWS | 12.324 | 00:06:27 | 00:08:07 |          |
| 11  | 317   | NBRx2 | 493      | AGP    |        | 690.84 | 102991 |         |           |    | -89             |     |        | 00:06:27 | 00:08:07 |          |
| 10  | 291.3 | NBRx2 | 495      | AGP    |        | 552,22 | 451642 |         |           |    | -86             |     |        | 00:06:27 | 00:08:07 |          |
| 9   | 265.6 | NBRx2 | 2100     | AGP    | LD     | 844.07 | 271156 | W30%    |           |    | <b>-</b> 83     | SS  | 11.995 | 00:06:27 | 00:08:06 |          |
| 8   | 239.9 | BBRx2 | 18000    | F      | RG     | 499,93 | 193811 | H27%    |           |    | -80             | CR  | 13,937 | 00:06:27 | 00:08:06 |          |
| 7   | 214.2 | NBRx2 | 15000    | CW     | FMC    | 752.22 | 203499 |         |           |    | -77             |     |        | 00:06:27 | 00:08:06 |          |
| 6   | 188.5 | BBRx1 | 10000    | AGP    | PM     | 623,82 | 362889 | H14%    |           |    | <b>-7</b> 4     | HE  | 16.678 | 00:06:27 | 00:08:06 |          |
| 5   | 162.8 | NBRx2 | 500      | CH     | LD     | 24.18  | 423304 | H25%    |           |    | <b>-71</b>      | TWS | 13,598 | 00:06:27 | 00:08:06 |          |
| 4   | 137.1 | NBRx1 | 400      | AGS    | FM     | 337.76 | 134137 |         |           |    | -68             | CS  | 8.01   | 00:06:27 | 00:08:06 |          |
| 3   | 111.4 | NBRx1 | 350      | F      | PM     | 128.37 | 158467 | W12%    |           |    | <del>-</del> 65 | LK  |        | 00:06:27 | 00:08:06 |          |
| 2   | 86.7  | NBRx1 | 250      | AGP    |        | 642.34 | 468227 |         |           |    | -63             |     | 7.99   | 00:06:27 | 00:08:07 |          |
| 1   | 61    | NBRx1 | 200      | AGP    | RG     | 816.94 | 56512  | J8%     |           |    | -60             | CR  | 5.377  | 00:06:27 | 00:08:07 |          |

**Figure-5.254: Emitter Report Window GUI – SCD Main Window**

The columns of the table shall include emitter parameters as given below in Table 5.12.

**Table-5.12: Emitter Parameters in Emitter Window**

| Parameter | Description       | Expected Values              | Units |
|-----------|-------------------|------------------------------|-------|
| TNo.      | 'Track Number' of | 1 to 500:<br>Active/ Passive | None  |
|           | Emitter           | Tracks,                      |       |
|           |                   | 501-510:<br>Manual Mode EA   |       |
|           |                   | Tracks,                      |       |
|           |                   | 511-600:<br>Manual BITE      |       |
|           |                   | Tracks,                      |       |
|           |                   | 601-700:<br>NBRx1 Auto BITE  |       |
|           |                   | Tracks.                      |       |
|           |                   | 701-800:<br>NBRx2 Auto BITE  |       |
|           |                   | Tracks.                      |       |
|           |                   | 801-900:<br>BBRx1 Auto BITE  |       |
|           |                   | Tracks.                      |       |
|           |                   | 901-999:<br>BBRx2 Auto BITE  |       |
|           |                   | Tracks.                      |       |

SHAKTI : UHB\Ch5 Page 379 of 614

| Parameter  | Description                                                                | Expected Values                                                                                                                                                                                                                                                                                                        | Units  |
|------------|----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| BRG        | 'Platform Bearing<br>(Heading)' Reported<br>by ESI through ES<br>Processor | 0-360.0.                                                                                                                                                                                                                                                                                                               | Degree |
| Rx.        | 'Name of Receiver'<br>from which the<br>Emitter is Reported                | NBRx1: Narrow Band<br>Receiver1 (0.175-0.5GHz),<br>NBRx2: Narrow Band<br>Receiver2 (0.5-18GHz),<br>BBRx1:<br>Broad Band<br>Receiver1 (2.2-18GHz),<br>BBRx2: Broad Band<br>Receiver2 (18-40GHz),<br>*BBRx1:<br>Emitter is reported<br>in both BB Rx1 & NB Rx2.                                                          | None   |
| Freq.      | 'Frequency' of<br>Emitter                                                  | 175-40000.                                                                                                                                                                                                                                                                                                             | MHz    |
| Freq. Type | Frequency Type                                                             | AGP :Pulse to Pulse Agile<br>AGS :Pulse to Scan Agile<br>CH: Chirp<br>CW: Continuous Wave<br>F: Fixed                                                                                                                                                                                                                  | None   |
| P.Type     | Pulse type                                                                 | CW:<br>Continuous Wave,<br>FM:<br>Freq. Modulation on<br>Pulse (Bi-Linear Chirp),<br>FMC: Frequency Modulation<br>on Pulse CW (FMCW),<br>LD: Linear FM Down on<br>Pulse (Down Chirp),<br>LU: Linear FM Up on Pulse<br>(Up Chirp),<br>RM: Phase Modulation on<br>Pulse (Barker),<br>RG: Regular (Fixed),<br>U: Unknown. | None   |
| PW         | 'Pulse Width' of                                                           | 0, 50ns-1000000.                                                                                                                                                                                                                                                                                                       | ns     |

SHAKTI : UHB\Ch5 Page 380 of 614

| Parameter  | Description                                                                         | Expected Values                                                                                                                                                                                                                                                                     | Units |
|------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
|            | Emitter                                                                             |                                                                                                                                                                                                                                                                                     |       |
| PRF        | 'Pulse Repetition<br>Frequency' of<br>Emitter                                       | 0, 50-500000.                                                                                                                                                                                                                                                                       | Hz    |
| PRF Type   | 'PRF Type' of<br>Emitter                                                            | FIX:<br>Fixed,<br>STA:<br>Staggered,<br>JIT:<br>Jittered,<br>DSW:<br>Dwell & Switched,<br>SLI:<br>Sliding,<br>WOB: Wobulated,<br>UN:<br>Unknown.<br>Value: PRF/ Freq Type<br>0:<br>Fixed or CW Variants,<br>1-256:<br>Staggered,<br>1-16:<br>Dwell & Switched,<br>0-30%:<br>Jitter. | None  |
| Radar Name | 'Name of Radar'<br>found in 'Emitter<br>Library' after Library<br>Match for Emitter | Alphanumeric characters<br>(maximum 8 characters).                                                                                                                                                                                                                                  | None  |
| CL         | 'Confidence Level' of<br>Emitter after Library<br>Match                             | 1-9.                                                                                                                                                                                                                                                                                | None  |
| Amp.       | 'Amplitude' of Emitter                                                              | 0-100.                                                                                                                                                                                                                                                                              | dB    |
| ST         | 'Scan Type' of<br>Emitter                                                           | CIR:<br>Circular,<br>SEC:<br>Sectorial,<br>LOC:<br>Lock-On,<br>UN:<br>Unknown.                                                                                                                                                                                                      | None  |
| ASP        | 'Antenna Scan<br>Period' of emitter                                                 | 0, 30-20000.                                                                                                                                                                                                                                                                        | ms    |
| TOFA       | 'Time of First Arrival'<br>of Emitter                                               | Time in 'hh:mm:ss'<br>format.                                                                                                                                                                                                                                                       | None  |
| TOLA       | 'Time of Last Arrival'                                                              | Time in 'hh:mm:ss'<br>format.                                                                                                                                                                                                                                                       | None  |

SHAKTI : UHB\Ch5 Page 381 of 614

| Parameter | Description                                                                                                              | Expected Values                                                                                                               | Units                         |
|-----------|--------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
|           | of Emitter                                                                                                               |                                                                                                                               |                               |
| Platform  | 'Name of Platform'<br>found in 'Emitter<br>Library' after Library<br>Match for Emitter                                   | Alphanumeric characters<br>(maximum 6 characters).                                                                            | None                          |
| Op. Role  | 'Operational Role'<br>found in 'Emitter<br>Library' after Library<br>Match for the Emitter                               | Alphanumeric characters<br>(maximum 13 characters).                                                                           | None                          |
| TL        | 'Threat Level' found<br>in 'Emitter Library'<br>after Library Match<br>for Emitter                                       | 0-9.                                                                                                                          | None                          |
| AC        | 'Activity Count' of<br>Emitter                                                                                           | 0-65535.                                                                                                                      | None                          |
| Age       | 'Track Age' of<br>Emitter. Number of<br>Seconds Elapsed<br>from last<br>Active<br>to<br>Passive<br>Status<br>of Emitter. | 20-65535.                                                                                                                     | ns                            |
| Latitude  | 'Latitude of Platform'<br>when Emitter is<br>Intercepted                                                                 | Latitude value in<br>'dd mm ss.ss N/S'<br>format,<br>where<br>dd: degree,<br>mm: minute,<br>ss: second,<br>N/S: North/ South. | degree,<br>minute,<br>second. |
| Longitude | 'Longitude' of<br>Platform' when<br>Emitter is Intercepted                                                               | Longitude value in<br>'ddd mm ss.ss E/W'<br>format,<br>where<br>ddd: degree,<br>mm: minute,<br>ss: second,                    | degree,<br>minute,<br>second. |

SHAKTI : UHB\Ch5 Page 382 of 614

| Parameter | Description                                                    | Expected Values                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Units |
|-----------|----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
|           |                                                                | E/W: East/ West.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |       |
| Status    | 'Status Code' of<br>Emitter                                    | Max 5 Characters:<br>C:<br>Emitter is being Reported<br>to CMS,<br>M:<br>Being Tracked and<br>Jammed.<br>N:<br>Radar Finger Print NOT<br>initiated from SCD.<br>P:<br>Radar Finger Print Results<br>Pending from RFPS,<br>R:<br>Radar Finger Print Results<br>Received,<br>T:<br>Emitter is being 'Tracked'<br>by EA System,<br>J:<br>Emitter being is 'Jammed'<br>by EA System.<br>L: Emitter is being Reported<br>to LRSAM,<br>K: Emitter is being Reported<br>to KAVACH, | None  |
| Ch.Rate   | 'Chirp Rate' of<br>Emitter                                     | 1-100.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | MHz   |
| Freq.Min. | 'Minimum Frequency'<br>of Emitter                              | 175-40000.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | MHz   |
| Freq.Max. | 'Maximum<br>Frequency' of<br>Emitter                           | 175-40000.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | MHz   |
| PWMin.    | 'Pulse Width<br>Minimum' of Emitter                            | 0, 50ns-1000000.                                                                                                                                                                                                                                                                                                                                                                                                                                                            | ns    |
| PWMax.    | 'Pulse Width<br>Maximum' of Emitter                            | 0, 50ns-1000000.                                                                                                                                                                                                                                                                                                                                                                                                                                                            | ns    |
| HC        | 'Track Hit Count' of<br>Emitter. Number of<br>Times Emitter is | 1-65535.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | None  |

SHAKTI : UHB\Ch5 Page 383 of 614

| Parameter | Description  | Expected Values | Units |
|-----------|--------------|-----------------|-------|
|           | Intercepted. |                 |       |

- 5.5.4.2.25.4.1.1 Emitter Report Window shall present the parameters of all the intercepted emitters in the order of emitter number.
- 5.5.4.2.25.4.1.2 Context (pop-up) menu shall be provided within the context of Emitter Window for operations related to track functionalities/ engagement etc.
- **5.5.4.2.25.4.2 Context Menu in Emitter Report Window**. A context menu shall be provided in this window, for performing track related operations. If user clicks mouse right button on a track (other than BITE tracks) in this window, a context menu (as shown in **Figure-5.255**) shall be displayed with the following of options:
  - (a) Show Emitters Watch Window
  - (b) Add Track to Temp. Library.
  - (c) Add Track to HookUp Window.
  - (d) ESM Operations.
    - (i) Get PD Data.
    - (ii) Get Scan Type.
    - (iii) Rebuild Tracks.
    - (iv) Purge Passive Tracks.
    - (v) Set Track Build Criteria.
    - (vi) Set Lockout Frequency Bands.
    - (vii) Set Lockout Sectors.
    - (viii) Load Warner Library.
  - (e) RPFS Operations.
    - (i) Finger Print Track.
    - (ii) Finger Print Track with DRTG.
    - (iii) Record Data at RFPS.
  - (f) ECM Operations.
    - (i) Track.
    - (ii) Track & Jam.

- (iii) Jam.
- (iv) Stop Jam.
- (v) Break Track.
- (vi) Modify Jamming Technique.
- (g) Send Track to CMS.
- (h) Send Track to LRSAM
- (j) Send Track to KAVACH
- (k) DOA Trace:
  - (i) Show Track on Chart
  - (ii) Enable
  - (iii) Disable

**5.5.4.2.25.4.3 Latest Emitters Window**. 'Latest Emitters Window' shall present the parameters of latest 6 emitters (ordered as per TOFA with recent first) in a tabular format as shown **Figure-5.255** Latest Emitters Window GUI – SCD Main Window. Columns of this window shall be same as 'Emitter Report Window'.

| TNo | BRG   | Rx.   | Freq. | F.Type | P.Type | PW     | PRF    | PRFType | RadarName | CL | Amp.            | ST  | ASP    | TOFA     | TOLA     | Platform |
|-----|-------|-------|-------|--------|--------|--------|--------|---------|-----------|----|-----------------|-----|--------|----------|----------|----------|
| 1   | 187   | NBRx1 | 200   | AGP    | RG     | 816.94 | 56512  | J8%     |           |    | <del>-</del> 48 | CR  | 5,377  | 00:06:27 | 00:11:16 |          |
| 2   | 212.7 | NBRx1 | 250   | AGP    |        | 642.34 | 468227 |         |           |    | <b>-</b> 51     |     | 7.99   | 00:06:27 | 00:11:16 |          |
| 3   | 238.4 | NBRx1 | 350   | F      | PM     | 128.37 | 158467 | W12%    |           |    | <b>-</b> 54     | LK  |        | 00:06:27 | 00:11:16 |          |
| 4   | 264.1 | NBRx1 | 400   | AGS    | FM     | 337.76 | 134137 |         |           |    | <b>-</b> 57     | CS  | 8.01   | 00:06:27 | 00:11:16 |          |
| 5   | 289.8 | NBRx2 | 500   | CH     | LD     | 24.18  | 423304 | H25%    |           |    | <b>-</b> 60     | TWS | 13,598 | 00:06:27 | 00:11:17 |          |
| 6   | 315.5 | BBRx1 | 10000 | AGP    | PM     | 623,82 | 362889 | H14%    |           |    | <b>-</b> 63     | HE  | 16.678 | 00:06:27 | 00:11:17 |          |

**Figure-5.255: Latest Emitters Window GUI – SCD Main Window**

#### **5.5.4.2.25.4.4 Context Menu in Emitter Report Window**.

(a) **Hooking Emitters Window**. This window will present the emitters added by the operators from Emitter Report/Latest Emitter/Emitters Watch Windows. This window will be useful for the operator to view emitters of importance in dense EW emission environment. Maximum of 50 emitters can be hooking and monitored in this window parameters of the emitters (ordered as per track as in ascending order) are displayed in a tabular format as shown in the **Figure-5.256**. Columns of this window will be same as 'Emitter Report Window'. Operator can add/delete entries from/to this window by using the controls shown on the GUI. This GUI can be hidden whenever it's not required by clicking on 'Hide Hook Window' on option on the GUI.

SHAKTI : UHB\Ch5 Page 385 of 614

![](_page_389_Picture_1.jpeg)

**Figure-5.256: Hook Up Emitter Window GUI.**

(b) **Emitters Watch Window**. This window will present emitters as per the fillers selected by operator as shown in the GUI in **Figure-5.257**. This window will be useful for the operator to look for emissions of interest as per the selected emitter parameters such as 'Rx Type, Freq, PW, and PRF' etc. Operator can alter the filter options as per requirement and emitters which fall in the selected ranges/options will be displayed in the window in real time. Parameters of the emitters are displayed in a tabular format and columns of this window will be same as 'Emitter Report Window'. Filter option is provided on the GUI and the Operator can show/hide them as and when required. This Emission Watch Window can be hidden by the operator when not required by clicking on 'Hide Watch Window' option on the GUI.

![](_page_389_Picture_4.jpeg)

**Figure-5.257: Emitters Watch Window GUI.**

- (c) **DOA Trace**. Operator has the facility to trace the selected emitters in a separate graphical window. DOA Trace provision is available in context menu of Tactical, Situational, and Tabular windows. In Context Menu of DOA Trace.
  - (i) **Show Track on Chart**. Operator has the facility to track the desired

SHAKTI : UHB\Ch5 Page 386 of 614

emitter and click on "Show Track on Chart" option from the context menu. On operator's confirmation message will be displayed as shown in the **Figure-5.258**.

![](_page_390_Picture_2.jpeg)

**Figure-5.258: DOA Trace Operator Confirmation**

5.5.4.2.25.4.4.1 After confirmation a separate "DOA Trace Window" will be displayed with selected emitter. DOA of selected emitter will be updated in this graphical window and plotting will be done automatically as shown in the **Figure-5.259**.

5.5.4.2.25.4.4.2 To remove selected emitter, operator has to right click on the track and choose "Delete" option.

5.5.4.2.25.4.4.3 To add a new track in DOA Trace window, operator has to select track from the combo box.

- (i) **Enable**: After user selection of tracks DOA Trace will be in Enabled state.
- (ii) **Disable**: Operator has the provision to disable the DOA Trace.
- (iii) Refer remaining context menu items in previous sections for further details.

![](_page_390_Figure_10.jpeg)

**Figure-5.259: DOA Trace Dialog**

SHAKTI : UHB\Ch5 Page 387 of 614

**5.5.4.2.26 Detailed Parameters Window**.This window shall present a GUI, as shown in **Figure-5.260**, to display & update the detailed list of emitter parameters received from ES Processor. Also, emitter identity details, if library matched, shall be displayed on this GUI. User shall double click on an emitter in 'Tabular Display' to activate this GUI. This GUI shall be displayed in the centre of SCD Main Window and shall be floatable (movable) to any place on SCD Main Window.

5.5.4.2.26.1 User shall click on 'Spot Freq's/ Spot PRFs/ Spot PWs' option to view spot frequencies/ spot PRFs/ spot PWs if any, of the selected emitter.

5.5.4.2.26.2 User shall click on 'Close' option to exit from this GUI and go to SCD Main Window.

![](_page_391_Picture_4.jpeg)

**Figure-5.260: Detailed Parameters Window GUI – System Menu.**

**5.5.4.2.27 RFPS Results Window**.'Radar Finger Printing' results received from RFPS shall be presented in tabular format in this window. There shall be provision to display 'Manual 'Radar Finger Printing' & 'Auto Radar Finger Printing' results in a tabbed GUI as show in **Figure-5.261**.

![](_page_391_Picture_7.jpeg)

**Figure-5.261: RFPS Results Window GUI – SCD Main Window**

SHAKTI : UHB\Ch5 Page 388 of 614

(a) **Manual RFPS Results Window**.User shall select an emitter (other than BITE tracks) from any one of the 'Emitter Presentation Windows' and perform radar finger printing operation on it. Results received from RFPS for this action shall be presented in this window. The parameters shown in this window shall be as mentioned below in **Table 5.13**.

**Table-5.13: Parameters of Manual RFPS Results**

| Parameter         | Description                                                                                                       | Expected Values                                                                                                                     | Units |
|-------------------|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|-------|
| ES TNo.           | 'Track Number' of<br>Emitter Reported by<br>ES Processor                                                          | 1 to 500.                                                                                                                           | None  |
| RFPS Tno.         | 'Track Number' of<br>Emitter Reported by<br>RFPS. All the<br>Following<br>Parameters will be<br>Reported by RFPS. | 1 to 255.                                                                                                                           | None  |
| Platform<br>Name  | 'Name of Platform' of<br>Emitter                                                                                  | Alphanumeric characters<br>(maximum 20 characters).                                                                                 | None  |
| Platform<br>Class | 'Class of Platform' of<br>Emitter                                                                                 | Alphanumeric characters<br>(maximum 20 characters).                                                                                 | None  |
| Radar Name        | 'Name of Radar' of<br>Emitter                                                                                     | Alphanumeric characters<br>(maximum 20 characters).                                                                                 | None  |
| Radar Mode        | 'Radar Mode' of<br>Emitter                                                                                        | Alphanumeric characters<br>(maximum 10 characters).                                                                                 | None  |
| CL                | 'Confidence Level' of<br>Emitter                                                                                  | 0,1.0 to 10.0                                                                                                                       | None  |
| Signal Type       | 'Signal Type' of<br>Emitter                                                                                       | CW,<br>FMCW,<br>QuasiCW,<br>Pulsed-NonAgile,<br>Pulsed-FreqAgile,<br>Pulsed-FreqDiversity,<br>IFF-Interrogation,<br>Pulsed-PWAgile, | None  |

SHAKTI : UHB\Ch5 Page 389 of 614

| Parameter | Description                                           | Expected Values                                                                                                                                                                                                                                                                                                                                                                                                         | Units |
|-----------|-------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
|           |                                                       | Pulsed-PWAgile-FreqAgile,<br>NoiseRadar.                                                                                                                                                                                                                                                                                                                                                                                |       |
| Avg.Freq. | 'Average Frequency'<br>of Emitter                     | 175-40000.                                                                                                                                                                                                                                                                                                                                                                                                              | MHz   |
| Avg.PW    | 'Average Pulse<br>Width' of Emitter                   | 2.00-10000.00.                                                                                                                                                                                                                                                                                                                                                                                                          | us    |
| Avg.PRF   | 'Average Pulse<br>Repetition<br>Frequency' of Emitter | 0, 50-500000.                                                                                                                                                                                                                                                                                                                                                                                                           | Hz    |
| PRF Type  | 'PRF Type' of Emitter                                 | DSW:<br>Dwell & Switched,<br>STA:<br>Staggered,<br>JIT:<br>Jittered,<br>FIX:<br>Fixed,<br>SLI:<br>Sliding,<br>WOB:Wobulated,<br>PGRI:<br>Pulse Group<br>Repetition Interval,<br>PseudoRandom,<br>STA-DSW:<br>Staggered and<br>Dwell & Switched,<br>JIT-DSW:<br>Jittered and Dwell<br>& Switched,<br>JIT-STA:<br>Jittered and<br>Staggered,<br>MultiplePRI:<br>Multiple Pulse<br>Repetition Interval,<br>UN:<br>Unknown. | None  |
| ST        | 'Scan Type' of<br>Emitter                             | CIR:<br>Circular,<br>SEC:<br>Sectorial,<br>LOC:<br>Lock-On,<br>CON:<br>Conical,<br>TWS:<br>Track While Scan,<br>HEL:<br>Helical,<br>Complex,<br>Raster,                                                                                                                                                                                                                                                                 | None  |

SHAKTI : UHB\Ch5 Page 390 of 614

| Parameter         | Description                         | Expected Values                                                                                                                                              | Units                       |
|-------------------|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
|                   |                                     | Palmer.                                                                                                                                                      |                             |
| Process<br>Status | 'Current Process<br>Status' at RFPS | Data Acquisition<br>Completed,<br>Data Acquisition Time Out,<br>Invalid Data,<br>Data Acquisition<br>Completed in Record Mode,<br>Finger Printing Completed. |                             |
| Reported At       | 'Status Report Time'                | Time in 'hh:mm:ss'<br>format.                                                                                                                                | hour,<br>minute,<br>second. |

5.5.4.2.27.1 For viewing detailed RFPS results, user shall double click on a row in the table. A GUI, as shown in **Figure-5.262**, shall be displayed with all the finger print parameters.

![](_page_394_Figure_3.jpeg)

**Figure-5.262: Detailed RFPS Results (Manual Radar Finger Printing) Window GUI.**

SHAKTI : UHB\Ch5 Page 391 of 614

- (b) **Auto RFPS Results Window**. 'Auto Radar Finger Printing' will be performed automatically by SCD application, in the background, on emitters (maximum 8) which match the 'Auto RFPS Settings' criteria. The results received from RFPS for this action shall be presented in this window. The parameters shown in this window shall be as given in **Table-5.12**.
- 5.5.4.2.27.2 For viewing detailed RFPS results, user shall double click on a row in the table. A GUI, as shown in **Figure-5.263**, shall be displayed with all the finger print parameters.

![](_page_395_Figure_3.jpeg)

**Figure-5.263: Detailed RFPS Results (Auto Radar Finger Printing) Window GUI.**

- **5.5.4.2.28 EA Parameters Window**. 'EA Parameters Window' shall display the status of emitters being handled by EA system. This window shall present the status of emitters handled by EA system & the status of EA Transmitters as shown in **Figure-5.264**.
- 5.5.4.2.28.1 Jamming operations on emitters will be carried out in three modes:

SHAKTI : UHB\Ch5 Page 392 of 614

![](_page_396_Picture_1.jpeg)

**Figure-5.264: EA Parameters Window GUI – SCD Main Window**

- (a) Auto Mode: Auto jamming by ES Processor for Warner/ Lock-On type of emitters after library match in 'Warner Library'. 'Auto Jam' shall be enabled at ES Processor for this operation.
- (b) Semi-Auto Mode: User shall select an emitter from any of the 'Emitter Presentation Windows' and perform 'Track & Jam/ Jam' operation. The parameters of the emitter will be provided and updated by ES Processor to EA system.
- (c) Manual Mode: User shall enter parameters of emitter manually at SCD application and perform 'Track & Jam/ Jam' operation it.

**5.5.4.2.28.1 Track/ Jam Status of Emitters**.The status of emitters received from EA system shall be presented in this window as shown in **Table 5.14**.

**Table-5.14: Status of Emitters Handled by EA System**

| Parameter | Description          | Expected Values                   | Units  |
|-----------|----------------------|-----------------------------------|--------|
| TNo.      | 'Track Number' of    | 1 -<br>500:<br>Tracks Reported by | None   |
|           | Emitter Reported by  | ES Processor.                     |        |
|           | ES Processor or      | 501-<br>510:<br>Tracks Manually   |        |
|           | Manually Entered by  | Entered by User.                  |        |
|           | User.                |                                   |        |
| BRG       | 'Bearing (Heading)'  | 0-360.0.                          |        |
|           | Reported by EA       |                                   | degree |
|           | System               |                                   |        |
| Freq.     | 'Frequency' of       | 6000-40000.                       | MHz    |
|           | Emitter              |                                   |        |
| El        | 'Elevation' Reported | -10.0-30.0.                       |        |
|           | by EA System         |                                   | degree |

SHAKTI : UHB\Ch5 Page 393 of 614

| Parameter      | Description                                                                                                                                                                                                                                 | Expected Values                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Units |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| EA Status      | 'Current Status' of<br>EA Activity on<br>Emitter                                                                                                                                                                                            | Desig.:<br>Emitter is<br>Designated,<br>Track.:<br>Emitter is being<br>Tracked,<br>PRISync.:<br>PRI Tracker is<br>Synced,<br>AngleTrack.:<br>Angle Tracking<br>is ON,<br>Jam.:<br>Emitter is being<br>Jammed.                                                                                                                                                                                                                                                                                                                                                                                                                                                       | None  |
| JPRO Technique | 'Name of JPRO<br>Technique' Currently<br>Applied by EA<br>System on Emitter.<br>Name Format:<br>Technique1, Angle1<br>+<br>Technique2, Angle2<br>+<br>Technique3, Angle3<br>One or more (max 3)<br>Techniques may be<br>Applied on Emitter. | Technique1, 2, 3:<br>DRFMSpot:<br>DRFM Spot<br>Noise,<br>DRFMBar:<br>DRFM Barrage<br>Noise,<br>DTOSpot:<br>DTO Spot Noise,<br>DTOBar:<br>DTO Barrage<br>Noise,<br>MultiSpot:<br>Multiple Spot<br>Noise,<br>DopplerN:<br>Doppler Noise,<br>VGPO:<br>Velocity Gate Pull<br>Off,<br>VGPI:<br>Velocity Gate Pull In,<br>SyncRec:<br>Synchronous<br>Range Velocity Receding,<br>SyncApro:<br>Synchronous<br>Range Velocity Approaching,<br>RGPO:<br>Range Gate Pull Off,<br>RGPI:<br>Range Gate Pull In,<br>RangeFT:<br>Range False<br>Targets,<br>Vel.FT:<br>Velocity False<br>Targets.<br>Angle1, 2, 3:<br>Blink:<br>Blink Deception,<br>SRM:<br>Swept Rate Modulation | None  |

SHAKTI : UHB\Ch5 Page 394 of 614

| Parameter | Description | Expected Values          | Units |
|-----------|-------------|--------------------------|-------|
|           |             | Deception,               |       |
|           |             | SSRM:<br>Synchronous SRM |       |
|           |             | Deception.               |       |

**5.5.4.2.28.2 Context Menu in EA Parameters Window.** A context menu shall be provided in this window, for performing track related operations. If user clicks mouse right button on a track in this window, a context menu (as shown in **Figure-5.265**) shall be displayed with the following of options:

- (a) Track.
- (b) Track and Jam.
- (c) Jam.
- (d) Stop Jam.
- (e) Break Track.
- (f) Modify Jamming Technique/ Update Track Info.

**Note**: **If the emitter number is between 1 & 500 (Semi-Auto Mode), 'Modify Jamming Technique' option shall be displayed in context menu. If the emitter number is between 501 & 510 (Manual Mode), 'Update Track Info.' option shall be displayed in context menu.**

![](_page_398_Picture_10.jpeg)

**Figure-5.265: Context Menu in EA Parameters Window – SCD Main Window**

**5.5.4.2.28.3 Status of EA Transmitters**.There shall be a provision for displaying operational status of MPMs of Tx (MB2)and Tx(HB) in the same window. By default, consolidated status of EA transmitters shall be displayed as shown in **Figure-5.266** with colour as shown in **Table-5.15**. User shall click this status button to view the details individual transmitters, as shown in **Figure-5.267**. This shall be toggling button and shall

SHAKTI : UHB\Ch5 Page 395 of 614

hide/ show 'Detailed Status of EA Transmitters' GUI when toggled.

![](_page_399_Picture_2.jpeg)

**Figure-5.266: Consolidated Status of EA Tx. GUI – EA Parameters Window.**

5.5.4.2.28.3.1 The following figure depicts the detailed status of EA transmitters (Port Side Transmitters in 'Ready' State & Starboard Side Transmitters in 'Off' State).

5.5.4.2.28.3.2 All the 16 MPMs of Tx(MB2) and Tx(HB) shall be displayed on the GUI for each sector, Start Board side (S) & Port (P) side. The status of each transmitter (On/ Off, Ready, HV On, Fault or Beam On) shall be displayed with colour codes as given below. By default, EA transmitters will be in 'OFF' state.

![](_page_399_Picture_6.jpeg)

**Figure-5.267: Detailed Status of EA Tx. GUI – EA Parameters Window.**

**5.5.4.2.28.4 Colour Scheme of EA Transmitters Status**.The following colour codes shall be used for depicting the current status of EA Transmitters as shown in **Table 5.15**.

**Table-5.15: Status of EA Transmitters & Their Color Codes.**

| EA Transmitter Status           | Color     | RGB Value in (R, G, B)<br>Format |
|---------------------------------|-----------|----------------------------------|
| OFF                             | Dark Grey | (89, 89, 89)                     |
| House Keeping (HK) Supply<br>ON | Cyan      | (190, 239, 255)                  |
| Heater ON                       | Blue      | (0, 0, 255)                      |

SHAKTI : UHB\Ch5 Page 396 of 614

| EA Transmitter Status | Color  | RGB Value in (R, G, B)<br>Format |
|-----------------------|--------|----------------------------------|
| Ready                 | Yellow | (255, 255, 0)                    |
| High Voltage (HV) ON  | Orange | (255, 192, 0)                    |
| Beam ON               | Green  | (0, 255, 0)                      |
| VSWR Fault            | Red    | (255, 0, 0)                      |

5.5.4.2.28.4.1 Common colour shall be used to depict fault status at EA transmitter and a tool tip text with 'EA Transmitter Status' shall be displayed to user if mouse cursor is placed over a transmitter symbol on this GUI.

**5.5.4.2.28.5 Status of EA Forbidden Frequency Bands & Sectors**.Status of 'Forbidden Frequency Bands & Sectors' enforced at EA system shall be displayed in 'EA Parameters Window' as described in **Table 5.16**.

**Table-5.16: Status of Forbidden Frequency Bands & Sectors at EA System**

| Forbidden<br>Frequencies | SET    | If 'Forbidden<br>Frequencies' are set<br>(enforced) at EA System. |  |
|--------------------------|--------|-------------------------------------------------------------------|--|
|                          | NOTSET | If 'Forbidden<br>Frequencies' reset<br>(removed) at EA System.    |  |
| Forbidden Sectors        | SET    | If 'Forbidden Sectors' are<br>set (enforced) at EA<br>System.     |  |
|                          | NOTSET | If 'Forbidden Sectors'<br>reset (removed) at EA<br>System.        |  |

**5.5.4.2.28.6 Status of Servo Position**.'Servo Position' angle received from EA system shall be displayed in 'EA Parameters Window' as shown in **Figure-5.268**. Servo angle will

SHAKTI : UHB\Ch5 Page 397 of 614

be in degrees with respect to 'True North'.

**Figure-5.268: GUI for Servo Position at EA System – EA Parameters Window**

**5.5.4.2.28.7 Status of ERP (Effective Radiation Power)**.'ERP' values of MMTs on port & starboard side received from EA system shall be displayed in 'EA Parameters Window' as shown in **Figure-5.269**. ERP value will be in KW (Kilo Watt).

![](_page_401_Picture_5.jpeg)

**Figure-5.269: GUI for ERP Values MMTs – EA Parameters Window.**

**5.5.4.2.28.8 Jam Status**. 'Current Jam Status' received from EA system shall be displayed in 'EA Parameters Window' as shown in **Table 5.17**.

**Table-5.17: Jamming Status – SCD Main Window**

| Jamming | ON  | If any emitter is being jammed, HV<br>ON should be applied and<br>maximum of the MPMs status<br>should be 'Beam ON' condition at<br>EA System. |  |
|---------|-----|------------------------------------------------------------------------------------------------------------------------------------------------|--|
|         | OFF | If no emitter is being jammed at EA<br>System.                                                                                                 |  |

**5.5.4.2.29 Link &Self Test Status Window**.This window shall present a GUI, as shown in **Figure-5.270**, to depict the 'Link & Self-Test Status' of all sub-systems connected to SCD system. This GUI shall be displayed at the right bottom corner of SCD Main Window and shall be floatable (movable) to any place on SCD Main Window. This window shall be hidden/ shown when user toggles 'LinkStatus' status button in 'EW System Status Window'.

SHAKTI : UHB\Ch5 Page 398 of 614

![](_page_402_Figure_1.jpeg)

**Figure-5.270: GUI for Link & Self-Test Status – SCD Main Window**

**5.5.4.2.29.1 Color Scheme of Link & Self-Test Status**.The following color codes shall be used for depicting the current status of 'Link & Self-Test' of Shakti EW system as shown in **Figure-5.271**.

![](_page_402_Picture_4.jpeg)

**Figure-5.271: GUI with Color Codes for Link & Self-Test Status – SCD Main Window**

5.5.4.2.29.1.1 Consolidated 'Self-Test' status of a sub-system shall be displayed in this

SHAKTI : UHB\Ch5 Page 399 of 614

GUI and If user clicks on 'ESP' (ES Processor), 'EAP' (EA Processor), 'RFPS' boxes, the status their LRUs shall be displayed in a separate GUI.

5.5.4.2.29.1.2 User shall click on mouse right button on 'ESP/ EAP/ RFPS/ ESI/ CMS' boxes on the GUI and click on 'Retry Connection with ESP/ EAP/ RFPS/ ESI/ CMS' option to reconnect to that sub-system.

**Note: Reconnecting to a sub-system will disconnect from it and establish network connection again and hence data pertaining to that sub-system may be cleared on SCD Main Window.**

5.5.4.2.29.1.3 User shall click on mouse right button on 'EAP' box on the GUI and click on 'Show EA Link Status' to view the internal link status of LRUs of EA system.

**5.5.4.2.30 System Messages Window**.In this window, messages related to system commands exercised by user on SCD Main Window & their responses/ results received from sub-systems shall be displayed in this window as on when they happen with the latest message being on top of the list. By default, this window shall be hidden and shall be shown when user selects 'Show System Messages Window' option in 'System' menu. The GUI for this window shall be as shown in **Figure-5.272** and shall contain GUI tabs to show each sub-system messages separately.

|     | All Messages ES Processor RFPS EA System            | m ESI | CMS LF | RSAM KAVACH          |
|-----|-----------------------------------------------------|-------|--------|----------------------|
| SNo | Message                                             | From  | То     | Date & Time          |
| 25  | Execution successful for 'ESP Start processing'     | ESP   | SCD    | 00:34:54 15 Sep 2022 |
| 24  | Start ESP Processing                                | SCD   | ESP    | 00:34:54 15 Sep 2022 |
| 23  | ACK received for 'Start Auto BITE'                  | ESP   | SCD    | 00:34:44 15 Sep 2022 |
| 22  | Execution successful for 'Select Operational Mode f | ESP   | SCD    | 00:34:44 15 Sep 2022 |
| 21  | Execution successful for 'Set NB Rx2 in Directed S  | ESP   | SCD    | 00:34:44 15 Sep 2022 |
| 20  | Execution successful for 'Set NB Rx1 in Mission Mo  | ESP   | SCD    | 00:34:44 15 Sep 2022 |
| 19  | ACK received for 'Set Track Build Criteria'         | ESP   | SCD    | 00:34:44 15 Sep 2022 |

**Figure-5.272: System Messages Window GUI – SCD Main Window**

5.5.4.2.30.1 The color scheme for the text of the messages displayed in this window shall be as shown in **Table 5.18**.

SHAKTI : UHB\Ch5 Page 400 of 614

**Table-5.18: Colour Codes for Messages in System Message Window**

| Message Type                                                                            |       | Color |
|-----------------------------------------------------------------------------------------|-------|-------|
| 'NACK' (Negative Acknowledgement), 'Execution<br>Unsuccessful' received from Sub-system | Red   |       |
| 'ACK' (Acknowledgement), 'Execution Successful' received<br>from Sub-system             | Green |       |
| All General Message                                                                     | White |       |

- 5.5.4.2.30.2 User shall click on mouse right button by placing mouse cursor in this window and click on 'Clear All' option to remove all the existing messages from the window. Note: messages will not be deleted permanently but will only be removed from this window.
- **5.5.4.2.31 Application Status Bar**.SCD application status bar shall display context based information as on when the user positions the mouse pointer / keyboard-key over a menu item in the menu bar/ tool bar. It shall also display 'Logged in User Name', 'System Mode' (CMS Controlled or Standalone), 'SCD Application Version', 'System Date & Time' as shown in **Figure-5.273.**

**Figure-5.273: Application Status Bar GUI – SCD Main Window**

**5.5.4.3 Replay Mode GUIs**.A GUI with replay controls, as shown in **Figure-5.274**, shall be displayed to user when SCD application is executed in 'Replay Mode'.

![](_page_404_Picture_8.jpeg)

**Figure-5.274: Replay Controls GUI in Replay Mode – SCD Main Window**

SHAKTI : UHB\Ch5 Page 401 of 614

- 5.5.4.3.a This GUI shall be displayed at the right bottom corner of SCD Main Window and shall be floatable (movable) to any place on SCD Main Window. This window shall be hidden/ shown when user clicks on 'Show/ Hide Replay Controls' menu item in 'System' menu or toggles 'Replay Controls' tool button in 'Application Tool Bar'. The following replay controls shall be provided on the GUI.
  - (a) **Play**. User shall click on 'Play' option on the GUI to start replay of a recording file. Data presentation on SCD Main Window shall start immediately after this action. This control shall be disabled after replay activity starts.
  - (b) **Stop**. User shall click on 'Stop' option on the GUI to stop ongoing replay of a recording file. Data presentation on SCD Main Window shall stop immediately after this action. Note: 'Emitter Report Windows' in SCD Main Window will be cleared and replay control will be at the beginning of file, if replay is stopped in between after starting it. This control shall be disabled after replay activity stops.
  - (c) **Pause**. User shall click on 'Pause' option on the GUI to pause ongoing replay activity. Data presentation on SCD Main Window shall be paused immediately after this action. This control shall be disabled after replay activity is paused.
  - (d) **Resume**. User shall click on 'Resume' option on the GUI to resume paused replay activity. Data presentation on SCD Main Window shall resume immediately after this action. This control shall be disabled after replay activity is resumed.
  - (e) **Speed Level**. User shall select required speed level (slow/ fast) of replay activity. More the speed level, faster will be the replay activity. Number of speed levels & maximum speed level value will be automatically calculated by SCD application depending on recording file size. This option shall be enabled only when replay activity is stopped or paused.
  - (f) **Slider Control for Replay Activity**. User shall press & hold the slider control on the GUI and drag it forward/ backward to move the starting point of replay activity. This control will be enabled only after replay activity starts.
  - (g) **Time Status of Replay Activity Progress**. Start, end and current time status of replay activity shall be displayed on the GUI. Start & end time of replay activity shall be updated after loading a recording file and current time status shall be updated as the replay activity progresses.
  - (h) **Select File**. User shall click on 'Select File' option on the GUI to stop ongoing replay activity, if started, and select another recording file from SCD

SHAKTI : UHB\Ch5 Page 402 of 614

storage. A file selection GUI, as shown in **Figure-5.275**, shall be displayed to user. If user selects a file and clicks on 'Load' option from the file selection GUI, a confirmation message shall be displayed and control shall return to SCD Main Window for replay activity with the new file.

5.5.4.3.b This control shall be disabled after replay activity starts and shall be enabled only when replay activity is stopped.

![](_page_406_Picture_3.jpeg)

**Figure-5.275: Replay File Selection GUI – SCD Main Window**

**5.5.4.4 Simulation Mode GUIs**.A GUI with simulation controls shall be displayed to user when SCD application is executed in 'Simulation Mode' as shown in **Figure-5.276**.

![](_page_406_Picture_6.jpeg)

**Figure-5.276: Simulation Controls GUI in Simulation Mode – SCD Main Window.**

5.5.4.4.1 This GUI shall be displayed at the right bottom corner of SCD Main Window and

SHAKTI : UHB\Ch5 Page 403 of 614

shall be floatable (movable) to any place on SCD Main Window. This window shall be hidden/ shown when user clicks on 'Show/ Hide Simulation Controls' menu item in 'System' menu or toggles 'Simulation Controls' tool button in 'Application Tool Bar'.

- 5.5.4.4.2 The following simulation controls shall be provided on the GUI.
  - (a) **Start**. User shall click on 'Start' option on the GUI to start simulation activity. Data presentation on SCD Main Window shall start immediately after this action. This will be a toggle option & shall switch to 'Stop' mode after simulation starts.
  - (b) **Stop**. User shall click on 'Stop' option on the GUI to stop ongoing simulation activity. Data presentation on SCD Main Window shall stop immediately after this action. This will be a toggle option & shall switch to 'Start' mode after simulation stops.
  - (c) **Pause**. User shall click on 'Pause' option on the GUI to pause ongoing simulation activity. Data presentation on SCD Main Window shall be paused immediately after this action. This will be a toggle option & shall switch to 'Resume' mode after simulation is paused.
  - (d) **Resume**. User shall click on 'Resume' option on the GUI to resume paused simulation activity. Data presentation on SCD Main Window shall resume immediately after this action. This will be a toggle option & shall switch to 'Pause' mode after simulation is resumed.
  - (e) **Modify**. User shall click on 'Modify' option on the GUI to stop ongoing simulation activity, if started, and modify or select another simulation file from SCD storage. 'Simulation' GUI (Figure-16, Section 5.5.4.2.2) will be displayed, if 'Modify' option is clicked from 'Simulation Controls' GUI. User shall modify existing simulation settings or select a new simulation file & click on 'Start Simulation' option from 'Simulation' GUI and control shall return to SCD Main Window for simulation activity with the new/ modified simulation file.
- 5.5.4.4.3 This control shall be disabled after simulation activity starts and shall be enabled only when simulation activity is stopped.
- **5.5.4.5 OEM Specific SCD HMI Requirement Description**.In this section, OEM (Original Equipment Manufacturer) related HMI requirements of Shakti SCD application are described. These requirements will only be visible & accessible to OEM user ('Administrator' type of user) while operating Shakti SCD application. These requirements of SCD application HMI will be useful in troubleshooting application specific functionalities during maintenance of Shakti EW system. OEM Rep. shall login into Shakti SCD

SHAKTI : UHB\Ch5 Page 404 of 614

application with 'Administrator' user name and password to access maintenance related functionalities of Shakti SCD application.

**5.5.4.5.1 Set Passive Track Time**.Set Passive User shall login into SCD application in 'Online Mode' and SCD Main Window shall be displayed to access this GUI. User shall click on this menu item to view existing passive track time or set new one at ES Processor. A GUI (as shown in **Figure-5.277**) with passive track time shall be displayed. Tracks will be marked by ES Processor as passive if they are not updated for passive time interval.

![](_page_408_Picture_3.jpeg)

**Figure-5.277: GUI to Set Passive Track Time at ES Processor – ES Processor Menu**

5.5.4.5.1.1 User shall enter 'Time' and click on 'Apply' option to set passive track time at ES Processor. For a value of '0' seconds, ES Processor will never mark tracks as passive.

5.5.4.5.1.2 User shall click on 'Cancel' option to exit from this GUI and go to SCD Main Window.

**5.5.4.5.2 NB RX1 (0.175-0.5 GHZ)->Directed Mode:** Refer section 5.5.4.2.12.1

**5.5.4.5.3 NB RX1 (0.175-0.5 GHZ)->Update Attenuation Data:** Refer section 5.5.4.2.12.5

**5.5.4.5.4 NB RX2 (0.5-18GHZ)->Directed Mode:** Refer section 5.5.4.2.12.7

**5.5.4.5.6 NB RX2 (0.5-18GHZ)->Update Attenuation Data:** Refer section 5.5.4.2.12.11

**5.5.4.5.8 BB RX1 (2.2-18GHZ)->Calibration:** Refer section5.5.4.2.12.16

**5.5.4.5.9 BB RX2 (18-40GHZ)->Raw PD Mode:** Refer section 5.5.4.2.12.20

**5.5.4.5.10 BB RX2 (18-40GHZ)->Calibration:** Refer section 5.5.4.2.12.21

SHAKTI : UHB\Ch5 Page 405 of 614

**5.5.4.5.11 Change JPRO Technique Configure Mode**.User shall login into SCD application in 'Online Mode' and SCD Main Window shall be displayed to access this GUI. This feature will be enabled and visible in 'Track or Track & Jam' related GUIs of EA system. User shall activate any of the 'Track or Track & Jam' related GUIs from 'EA System' menu and click on 'Configure Mode' option. A GUI, as shown in **Figure-5.278**, shall be displayed.

![](_page_409_Picture_2.jpeg)

**Figure-5.278: JPRO Technique Configure Mode GUI – Track/ Track & Jam GUIs.**

5.5.4.5.11.1 User shall select required configuration parameters from 'Validation Options', 'Multiple Simultaneous Spot', 'Frequency Hopping Mode', 'DFML Mode' or 'Recall Mode' and click on 'Apply' option.

5.5.4.5.11.2 User shall click on 'Cancel' option to exit from this GUI and go to 'Track or Track & Jam' related GUI from where this GUI is activated.

**5.5.4.5.12 BITE – Update ES Auto BITE Reference Data**.User shall login into SCD application in 'Online Mode' and SCD Main Window shall be displayed to access this GUI. User shall click on 'BITE->Update ES Auto BITE Reference Data' menu item from 'System' menu and a GUI (as shown in **Figure-5.279**) shall be displayed to update the BITE data in SCD application. The GUI shall retain the previous BITE data selected & applied by user.

5.5.4.5.12.1 ES Auto BITE track data received from ES Processor will be compared with this data and the results will be displayed as 'ES Auto BITE Status'. Note: This reference data shall not be modified/ deleted unless there is a change in ES System configuration.

SHAKTI : UHB\Ch5 Page 406 of 614

![](_page_410_Figure_1.jpeg)

**Figure-5.279: GUI to Update ES Auto BITE Reference Data – System Menu.**

- 5.5.4.5.12.2 Factory level settings (ES auto BITE reference data) shall be listed in table on the GUI, if not modified by user. Each row shall contain ES auto BITE track parameters.
- **5.5.4.5.12.1 Modify ES Auto BITE Reference Data**. User shall double click on a row in the table to modify it. User shall change the required ES auto BITE parameters ('DOA', 'Frequency', 'PW' 'PRF' or 'Amplitude') and click on 'Update' option to update it in the table. User shall repeat this procedure for modifying other rows in the table.
- **5.5.4.5.12.2 Remove ES Auto BITE Reference Data**.User shall click on a row in the table and click on 'Remove'. User shall repeat this procedure to remove others rows; alternately, user can click on 'Delete All' option to delete all the entries in the table. It is not suggested to remove a single row; if at all to remove, remove all the rows in the table and add new ES auto BITE reference data for all the receivers, afresh.
- **5.5.4.5.12.3 Add ES Auto BITE Reference Data**.User can add ES auto BITE reference data if no previous data exists or if there is a change in Auto BITE configuration.

SHAKTI : UHB\Ch5 Page 407 of 614

User shall remove all the existing ES auto BITE reference data from the table before entering new data. User shall select 'Receiver', 'DOA', 'Frequency', 'PW' 'PRF', 'Amplitude' and click on 'Add' option to add it in the table. User shall repeat this procedure for adding other reference data for all the receivers.

- 5.5.4.5.12.3.1 User shall click on 'Close' option to exit from this GUI and go to SCD Main Window.
- **5.5.4.5.13 System Configuration**.'System Configuration' GUI, as shown in **Figure 35.** (section 5.5.4.2.5), shall facilitate the user modify configuration parameters of subsystems in 'Offline' mode. User shall click on 'System Configuration' option in 'Offline Mode' GUI to active this GUI.
- 5.5.4.5.13.a By default, a list of available system configuration files on SCD storage shall be displayed on the GUI.
- 5.5.4.5.13.b User shall select a configuration file from the list of files on the GUI and click on 'Show' option to load configuration data on to the GUI. Alternately, use shall double click on a file to load it.
- 5.5.4.5.13.c Sub-sections of system configuration shall be displayed as tab GUIs and user shall select a sub-section & modify required configuration parameters.
- 5.5.4.5.13.d User shall click on 'Close' option to close this GUI and go to 'Offline' mode GUI. A confirmation GUI, as shown in **Figure 36**. (section 5.5.4.2.5), shall be displayed to user with 'Yes, No & Cancel' options. User shall click on 'Yes' option to save any changes to the selected system configuration file & exit from 'System Configuration' GUI and go to 'Offline Mode' GUI. User shall click on 'No' option to discard any changes made in the selected system configuration file & exit from 'System Configuration' GUI and go to 'Offline Mode' GUI. User shall click on 'Cancel' option to remain there in 'System Configuration' GUI, without saving/ discarding any changes.
- 5.5.4.5.13.e The following sections describe system configuration of SCD application:
- **5.5.4.5.13.1 ES Processor Configuration GUI**.By default, this tab GUI shall be displayed when 'System Configuration' GUI is activated.
- 5.5.4.5.13.1.1 User shall check 'Enable/ Disable' option to enable/ disable this interface in SCD application.
- 5.5.4.5.13.1.2 User can modify network settings (Port, IP address, Connection Retry Interval, Link Down Declaration Timeout), configuration settings (Auto BITE, Auto Purge,

SHAKTI : UHB\Ch5 Page 408 of 614

Passive Track Time, Track Build Criteria).

- **5.5.4.5.13.2 ES Receivers Configuration GUI**. User shall click on 'ES Receivers' tab GUI to view the configuration parameters of ES Receivers.
- 5.5.4.5.13.2.1 User can modify operation mode & mode parameters of NB Rx1 (0.175- 2.2GHz), NB Rx2 (2.2-18GHz) or BB Rx1 (2.2-18GHz).
- **5.5.4.5.13.3 RFPS Configuration GUI**.User shall click on 'RFPS' tab GUI to view the configuration parameters of RFPS.
- 5.5.4.5.13.3.1 User shall check 'Enable/ Disable' option to enable/ disable this interface in SCD application.
- 5.5.4.5.13.3.2 User can modify network settings (Port, IP address, Connection Retry Interval, Link-Down Declaration Timeout), configuration settings (RFPS Operation Time Out, Auto RFPS Settings).
- **5.5.4.5.13.4 ESI Configuration GUI**.User shall click on 'ESI' tab GUI to view the configuration parameters of ESI.
- 5.5.4.5.13.4.1 User shall check 'Enable/ Disable' option to enable/ disable this interface in SCD application.
- 5.5.4.5.13.4.2 User can modify network settings (Port, IP address, Connection Retry Interval, Link-Down Declaration Timeout).
- **5.5.4.5.13.5 CMS Configuration GUI**. User shall click on 'CMS' tab GUI to view the configuration parameters of CMS.
- 5.5.4.5.13.5.1 User shall check 'Enable/ Disable' option to enable/ disable this interface in SCD application.
- 5.5.4.5.13.5.2 User can modify network settings (Port, IP address, Connection Retry Interval, Link-Down Declaration Timeout).
- **5.5.4.5.13.6 LRSAM Configuration GUI**.User shall click on 'LRSAM' tab GUI to view the configuration parameters of LRSAM.
- 5.5.4.5.13.6.1 User shall check 'Enable/ Disable' option to enable/ disable this interface in SCD application.
- 5.5.4.5.13.6.2 User can modify network settings (Port, IP address, Connection Retry

SHAKTI : UHB\Ch5 Page 409 of 614

Interval, Link-Down Declaration Timeout).

- **5.5.4.5.13.7 KAVACH Configuration GUI**. User shall click on 'KAVACH' tab GUI to view the configuration parameters of KAVACH.
- 5.5.4.5.13.7.1 User shall check 'Enable/ Disable' option to enable/ disable this interface in SCD application.
- 5.5.4.5.13.7.2 User can modify network settings (Port, IP address, Connection Retry Interval, Link-Down Declaration Timeout).
- **5.5.4.5.13.8 Printer Configuration GUI**.User shall click on 'Printer' tab GUI to view the configuration parameters of Printer.
- 5.5.4.5.13.8.1 User shall check 'Enable/ Disable' option to enable/ disable this interface in SCD application.
- 5.5.4.5.13.8.2 User can modify network settings (Port, IP address).
- **5.5.4.5.13.9 Map Configuration GUI**. User shall click on 'Map' tab GUI to view the configuration parameters of map.
- 5.5.4.5.13.9.1 User shall check 'Enable/ Disable' option to enable/ disable map feature in SCD application.
- 5.5.4.5.13.9.2 User can modify map settings related to 'Default Zoom Level', 'Map Mode', 'Spokes', 'Annotations', 'Platform Path', 'Tactical Picture', 'Way Points' etc., by clicking on relevant option on the GUI.
- 5.5.4.5.13.9.3 User shall click 'Load All Map Files from SCD Storage' option to load all map files into SCD application.
- 5.5.4.5.13.9.4 To unload a map from SCD application, user shall click on 'Unload Map File' option.
- **5.5.4.5.13.10 General Configuration GUI**.User shall click on 'General' tab GUI to view application related settings such as:
  - (a) System Recording: Enable/ Disable 'System Recording'.
  - (b) Logs: Enable/ Disable 'User Activity Log', 'System Error Log', 'User Login History' etc.

SHAKTI : UHB\Ch5 Page 410 of 614

- (c) Library Matching: Enable/ Disable 'Library Matching' in SCD Application in 'Online' Mode, Select an Emitter Library File.
- (d) Audio Alarm Feature: Enable/ Disable Audio Alarm in SCD Application in 'Online' Mode. Select audio tone file for a particular signal type.
- (e) Database: Update Database (for storing emitter data & SCD application settings) Details.
- (f) Look & Feel: Select a theme file for SCD application look & feel.
- **5.5.4.5.13.11 SCD SBC Configuration GUI**.User shall click on 'SCD SBC' tab GUI to view the network interface settings SBC.
- 5.5.4.5.13.11.1 User can modify network settings (IP Addresses) and 'Date Time Correction Threshold' for updating SBC system time.
- **5.5.4.5.13.12 Save Changes in System Configuration**.Any modifications made to the selected system configuration shall be saved if user clicks on 'Save Changes' option on the GUI. A confirmation GUI, as shown in **Figure 37**.(section 5.5.4.2.5.1), shall be displayed to user.
- **5.5.4.5.13.13 Save To Another File**.User can save the selected system configuration (with modifications, if any) to another file on SCD storage by clicking on 'Save to Another File' option on the GUI. A confirmation GUI, as shown in **Figure 38** (section 5.5.4.2.5.2), shall be displayed to user. A file selection GUI shall be displayed to user for entering file name & user shall click on 'Save' option to save.
- **5.5.4.5.13.14 Set as Current System Configuration**.User shall click on 'Set as Current Configuration' option to save the displayed configuration (selected file) and use this in 'Online' mode when user enters 'Online' mode. A confirmation GUI, as shown in **Figure 39**.(section 5.5.4.2.5.3), shall be displayed to user. If user wants to go to 'Online' mode with a particular configuration, then a configuration file must be selected, changes to be made (if any) then click on 'Set as Current Configuration' option.
- **5.5.4.5.13.15 Reset to Default System Configuration**. User shall click on 'Reset to Default Configuration' option to erase all the configuration settings of the selected file and reload it with default (factory level) settings. A confirmation GUI, as shown in **Figure**

SHAKTI : UHB\Ch5 Page 411 of 614

**40**(section 5.5.4.2.5.4), shall be displayed to user.

#### **5.5.4.6 Operating Instructions – RFPS:**

- **5.5.4.6.1 Description of HMI of Radar Finger Printing System**.This section describes the Human Machine Interface details of the RFPS sub system. Press track ball "Middle" key to transfer the control of the keyboard and track ball from the System Controller to RFPS or vice versa.
- 5.5.4.6.1.1 This section provides description regarding Radar Finger Printing system (RFPS) operating procedures that can be performed by the user. This section describes all dialogs, buttons, inputs, and resulting views/actions including all the application messages and their meanings which are used for performing various operations of RFPS. The naming of menu/buttons is intuitive and assists the user in carrying out the tasks easily and conveniently.
- 5.5.4.6.1.2 All the operations are performed through the menu options from the menu bar / from the command buttons.
- **5.5.4.6.2 Radar Finger Printing Subsystem Overview**. To meet the built-in fingerprinting requirements of the system, the Radar Finger Printing System has been envisaged. This system shall have the capability to uniquely identify an emitter. The ability to uniquely identify an emitter would be of strategic advantage to the Electronic Warfare (EW) activity. The task of unique identification becomes even more challenging and daunting in dense complex environments consisting of a wide variety of agile emitters. The process of identification can be simplified if a unique characteristic can be ascribed to each emitter. This unique characteristic is the 'Radar Finger Print' of the emitter.
- 5.5.4.6.2.1 The Radar Finger Printing System (RFPS), which is one of the sub-systems of SAMUDRIKA-SHAKTI, has the capability to intercept, record, store, analyze and identify emitters unambiguously over a wide frequency band of 0.175 - 40 GHz. As emitter identification using the conventional ESM parameters are prone to ambiguities, this can be overcome by capturing the intentional and un-intentional variations in the radar waveforms by means of intra-pulse analysis, which measures the frequency, phase and amplitude variations within the pulse. Radar Fingerprinting System provides in-depth analysis of radar signals including complex Modern radars. Block diagram of RFPS subsystem shown in **Figure-5.280**.
- 5.5.4.6.2.2 The broad functional requirements of RFPS system are as follows:
  - (a) Analysis, classifying, identifying all types of radars conventional, exotic and

SHAKTI : UHB\Ch5 Page 412 of 614

also Low Probability of Intercept (LPI) radars.

- (b) Fine grain measurement frequency, pulse width, phase and PRI of the emitter.
- (c) Intra-pulse analysis with measurement instantaneous of amplitude, phase and frequency on a sample to sample basis.
- (d) Automatic detection of Barker-coded, polyphase coded, frequency modulated, frequency agile/ hop and burst radars.
- (e) Automatic emitter classification / identification based on statistical & graphical matching techniques along with the confidence of match
- (f) Provide platform identification through association of results of fine grain analysis.
- (g) Maintain emitter library of 10,000 emitters for emitter identification purpose.
- (h) Feature extraction ability for classification of low probability of intercept (LPI) radar modulations
- (j) Storage of IF data to facilitate off-line analysis of data
- (k) Auto scan operation to independently scan and detect the presence of RF emitters in the 2.2 to 18 GHz frequency band
- (l) Display of detected emitters in the scenario in RF activity display format.
- (m) Ability to take Track Data for initiation of RFPS from System Controller or self-generated Track Data in autonomous operation.

SHAKTI : UHB\Ch5 Page 413 of 614

![](_page_417_Figure_1.jpeg)

**Figure-5.280: Block diagram of RFPS**

SHAKTI : UHB\Ch5 Page 414 of 614

5.5.4.6.2.3 To carry out the above tasks, RFPS is configured as RF Tuner with demodulator, Data Acquisition Unit (DAU), Digital Signal Processing (DSP) Unit, Local Controller and Emitter Identification Unit (LCIU) and dedicated display to present the RFPS HMI.

5.5.4.6.2.4 The RFPS block diagram is shown in **Figure 5.1**. The DAU, DSP & LCIU communicates on VPX backplane. LCIU sends commands and gets feedback from RF Tuner on Ethernet. The inputs to the RF Tuner are signals in the range of:

- (a) 0.175-0.5 GHz from Tuned Receivers down converted to IF of 160 MHz
- (b) 0.5 -18 GHz from dedicated Omni chain.
- (c) 2.2-18 GHz from Homodyne Receiver down converted to IF of 160 MHz or 1 GHz.
- (d) 18 40 GHz from Frequency Receiver down converted to 6 17GHz.

5.5.4.6.2.5 RF Tuner tunes to specified frequency and generates the multiplexed IF signal of 1 GHz and 160 MHz and corresponding Log Video.

RFPS operates in three modes:

- (a) Auto Scan Mode.
- (b) System Finger Printing mode.
- (c) Local mode.

5.5.4.6.2.6 The default operation of RFPS is Auto Scan Mode. In Auto Scan Mode RFPS performs scan of the EM spectrum and displays the RF activity. For a particular RF activity, track is generated by RFPS and Finger printing can be performed on this track. On initiation of Finger printing, Auto Scan Mode is aborted. After successful Fingerprinting operation, Auto Scan can be reinitiated by clicking Restart Auto Scan icon from toolbar.

5.5.4.6.2.7 In System Finger Printing mode, the SCD designates emitter for which basic parameter extraction (track data) has already been done by the ESM processor. Based on track data LCIU sends controls to RF Tuner & DAU. DAU acquires & digitizes the IF, sends the digitized data along with TOA (Time of Arrival) information to DSP. The digitized IF data is processed in the DSP unit to extract the emitter Track Fine Grain Data (TFGD). The DSP Unit performs the job of feature extraction by employing signal processing algorithms. This is done by performing intra-pulse analysis in addition to the conventional inter-pulse analysis. This unit generates the Track Fine Grain Data (TFGD) and graphical data, which

SHAKTI : UHB\Ch5 Page 415 of 614

are sent to LCIU. The LCIU displays these results in various textual and graphical formats for operator. On the generated Track Fine Grain Data (TFGD) and graphical data, LCIU performs emitter identification. LCIU also handles the Human Machine Interface of RFPS.

5.5.4.6.2.8 Local mode can be used to perform RFPS on track which is known a priori but are not reported by ESM. RFPS operator initiates this mode of finger printing by entering the track data of the emitter using the keyboard for which FP is to be performed.

**5.5.4.6.3 RFPS Directories**. The default directories which are used by RFPS for storing files of RFPS library and log files is given below in the **Table 5.19**.

| Ser | Directory    | Directory Path             | Purpose of Directory                                 |
|-----|--------------|----------------------------|------------------------------------------------------|
| 1   | RFPS Library | C:\Shakti\<br>RFPS Library | This<br>directory<br>contains<br>RFPS library files. |

2 RFPS Data C:\ Shakti \ RFPS Data Contains all stored files

**Table-5.19: Default Directories of RFPS for Library/Log Files**

**5.5.4.6.4 RFPS Interfaces**.The RFPS interface diagram with external systems is as shown in **Figure-5.281**. The interface details of RFPS with other subsystems are as follows:

![](_page_419_Picture_7.jpeg)

**Figure-5.281: Interface diagram of RFPS**

**5.5.4.6.4.1 System Controller**. RFPS is connected to System Controller on LAN for receipt of command for Fine Grain Analysis and reporting of results of Fine Grain Analysis.

**5.5.4.6.4.2 Field Data Loader (FDL)**.RFPS is connected to FDL on LAN for importing

SHAKTI : UHB\Ch5 Page 416 of 614

and exporting of RFPS Library.

- **5.5.4.6.5 Software Development Environment**. The following software environment is used for RFPS software development
  - (a) Red Hat Linux Enterprise Edition Ver6.5 for X86\_64 bit
  - (b) QT Ver.5.3.1
  - (c) PostgreSQL 8.4
  - (d) Code Composer Studio IDE Ver.6.0
- **5.5.4.6.6 Radar Finger Printing System – HMI.** RFPS application provides graphic user interfaces (GUIs) based on Linux operating system to the operator. On Operating System boot up &system start-up RFPS application splash screen appears.
- **5.5.4.6.6.1 RFPS Login**.This feature shall enable the user to login into the RFPS Application. On Power-on, splash screen is displayed as shown in **Figure-5.282**. Facility to Common login for SCD and RFPS is provided, where User shall Login into SCD and SCD sends the details to RFPS on Power ON. During Power ON for cases SCD is not connected, RFPS shall come with Login facility. RFPS main application is launched, if login details are received from SCD.
- 5.5.4.6.6.1.1 The login dialog is shown in **Figure-5.283**.

![](_page_420_Picture_10.jpeg)

**Figure-5.282: Splash screen**

SHAKTI : UHB\Ch5 Page 417 of 614

![](_page_421_Picture_1.jpeg)

**Figure-5.283: Login Window**

5.5.4.6.6.1.2 On successful user authentication, if user has logged in with Administrator level privilege, User Management dialog shall be displayed to perform user management functionalities. In case user has logged in with Commander/Operator level privileges, RFPS Main Application window shall appear with Auto scan view.

5.5.4.6.6.1.3 If user enters invalid credentials then a message box shall appear indicating 'Invalid user credentials'. User fails to login in three attempts, a message box shall appear indicating "Login denied due to three failed attempts".

5.5.4.6.6.1.4 To cancel login operation, click on 'Cancel' button then the screen gets closed.

**5.5.4.6.6.2 RFPS Initialization**.On power ON RFPS performs health check of DAU, DSP unit and RF Tuner. It establishes connection with RFPS database. After successful link establishment SCD shall send date time to RFPS. In the Message/Status Window "SCD to RFPS- Set Date Time received" message shall be displayed. RFPS shall send power on health status of RFPS hardware to SCD. RFPS will go into Auto Scan Mode and displays activities in 'Activity Display Window'.

**5.5.4.6.6.3 RFPS Main Application Window**.As part of system initialization, the selfcheck of the RFPS sub-system and link check with external entities shall be performed and database connection shall be established.

5.5.4.6.6.3.a The RFPS Application shall be operated in System- Auto Scan and FP Modes. The RFPS Main Application window shall be displayed in the default mode.

5.5.4.6.6.3.b The data presentation in Screen 1 of RFPS Main Application Window is as shown in **Figure-5.284**. The screen is divided into following windows:

SHAKTI : UHB\Ch5 Page 418 of 614

- (a) Title Bar
- (b) Menu Bar
- (c) Tool Bar Window
- (d) ESM track Window
- (e) Water fall/Activity display Window
- (f) DAU raw data display Window
- (g) Command Window
- (h) Message/Status Window

![](_page_423_Figure_1.jpeg)

**Figure-5.284: Screen 1 of RFPS Main Application Window**

SHAKTI : UHB\Ch5 Page 420 of 614

**5.5.4.6.6.3.1 Title Bar**.The **Title bar** displays the title of the application, User Login, date & time.

**Figure-5.285: Title Bar**

**5.5.4.6.6.3.2 Menu Bar**. The **Menu bar** shall be displayed with Local, User Management, EI Library Management, Control Station (CS), Datalog and Help options.

![](_page_424_Figure_5.jpeg)

**Figure-5.286: Menu Bar**

**5.5.4.6.6.3.3 Tool Bar**.The **Tool bar** shall include important and frequently used commands in the form of icons. The toolbar commands shall be "Health, H-Grid ON/OFF, V-Grid ON/OFF, Foreground Colour, Background, Screen1 & Screen2 navigation and Restart Auto Scan." Tooltips shall be provided for each icon in order to view the name of the command. Hence, the toolbar includes various commands in the form of icons as shortcuts to perform functionalities, which are available in the Menu bar options. Tool bar also shall display the Link status with external systems SCD and RF Tuner. Tool Bar displays the following:

![](_page_424_Picture_8.jpeg)

**Figure-5.287: Tool Bar**

- (a) **Health** . When this icon is clicked, the RFPS health status shall be displayed in Subsystem Health Status.
- (b) **H-Grid** . When this icon is clicked, the horizontal grid lines in the graphical displays shall display or hide. This is a toggle button.
- (c) **V-Grid** . When this icon is clicked, the vertical grid lines in the graphical displays shall display or hide. This is a toggle button
- (d) **Foreground Color** . When this icon is clicked, the foreground colour of the graphical displays shall update with the selected colour.
- (e) **Background Colour** . When this icon is clicked, the background colour

SHAKTI : UHB\Ch5 Page 421 of 614

of the graphical displays shall update with the selected colour.

- (f) **Results view- Screen 2** . When this icon is clicked the fine grain analysis results Screen-2 of RFPS Main Application Window shall appear.
- (g) **FP view- Screen 1** . When this icon is clicked the FP View i.e., Screen-1 of RFPS Main Application Window shall appear.
- (h) **Restart Auto Scan** . When this icon is clicked the application view shall change to Auto Scan view and RFPS shall restart Auto Scan activity.
- (j) **SCD Link Status** .This shall display the status of link with SCD subsystem. Green color indicates Link OK, Red color indicates Link down.
- (k) **RF Tuner Link Status** .This shall display the status of link with RF Tuner. Green colour indicates Link OK, Red colour indicates Link down.
- **5.5.4.6.6.3.4 Graphical Tool Bar**.The DAU Raw Data Display has a separate mini tool bar to perform certain operations on the graphical raw data displayed in this window. It has icons on it, which can be used to perform operations like Zoom in, Zoom out, and Delete raw data.

![](_page_425_Picture_8.jpeg)

**Figure-5.288: DAU Raw Data Graphical Tool Bar**

- (a) **Previous** . When this icon is clicked RFPS FP View shall be displayed. This icon to be disabled in Auto Scan View and in RFPS FP View-Screen1.
- (b) **Next** . When this icon is clicked RFPS Results View is displayed. This icon is disabled in Auto Scan mode and Results View-Screen2.
- (c) **Delete Raw Data** . When this icon is clicked, the DAU Raw Data from the DAU Raw Data display and the log file shall be deleted. This icon is disabled when no DAU Raw Data exists.
- (d) **Zoom In** . When this icon is clicked, the selected graphical display is zoomed in 10% of the current view.

SHAKTI : UHB\Ch5 Page 422 of 614

- (e) **Zoom Out** . When this icon is clicked, the selected graphical display is zoomed out 10% of the current view.
- (f) **Undo Zoom** . When this icon is clicked the DAU raw data display window shall be undo zoom.
- **5.5.4.6.6.3.5 RFPS Health Window**.To get detailed RFPS hardware health, click on **Health** icon. The **Subsystem Health Status** Window shall appear (as shown in **Figure-5.289**) indicating the health status of hardware units like DAU, DSP, SBC and RF Tuner of RFPS, the healthy hardware will be shown in green colour and the faulty subsystem in red colour.

![](_page_426_Picture_4.jpeg)

**Figure-5.289: RFPS Health Window**

**5.5.4.6.6.3.6 Message / Status Window**.This **Message /Status Window** shall display the messages transferred between RFPS and SCD/RF Tuner or current Process status or other error information.

![](_page_426_Picture_7.jpeg)

**Figure-5.290: Message /Status Window**

**5.5.4.6.6.4 Auto Scan Mode**.Auto scan mode enables the user to find the Activity

SHAKTI : UHB\Ch5 Page 423 of 614

present in environment and report the activities in activity display. For Auto Scan configured with dwell time more than 200 msec, the Record activity feature shall be enabled to User.

5.5.4.6.6.4.1 On power on Auto Scan is initiated with default scan parameters, RFPS Main Application window shall appear with **Auto Scan** view is as shown in **Figure-5.291**.

SHAKTI : UHB\Ch5 Page 424 of 614

![](_page_428_Figure_1.jpeg)

**Figure-5.291: Auto Scan View**

SHAKTI : UHB\Ch5 Page 425 of 614

5.5.4.6.6.4.2 The Start, Stop frequency and other mandatory data in Scan Band Parameter window shall display. On clicking **Start** button, the auto scan shall be performed. The activities detected for the specified band of frequencies shall be logged and the activity report shall be displayed in **Activity Data** Window.

5.5.4.6.6.4.3 From Context menu of Activity Display, user shall choose **Select Record Frequency** option and select required activity from the **Activity Display** as shown in **Figure-5.292**. The activity window shows the band selected by the Operator for scan and it also shows the emitter activity reported.

![](_page_429_Figure_3.jpeg)

**Figure-5.292: Activity display**

**5.5.4.6.6.5 Finger Printing Mode**.This mode shall enable the user to perform Fine Grain Analysis to obtain fine grain data of the emitter**.** Fine Grain Analysis involves measuring the radar parameters to identify the radar. The following capabilities are associated with fine grain analysis:

- (a) Data Acquisition Capability
- (b) Feature Extraction Capability
- (c) Feature Identification/Emitter Identification Capability

5.5.4.6.6.5.a In System-Finger print mode RFPS shall send TFGD & matched parameters to SCD after successful completion of emitter identification.

- (a) In case of single track, TFGD results are sent automatically to SCD.
- (b) In case of multiple tracks for selected RFPS track the emitter identification

SHAKTI : UHB\Ch5 Page 426 of 614

shall be performed by selecting desired track from TFGD Track Data Display and click on **Initiate EI** button in TFGD Display. TFGD results can be sent to SCD on clicking Send to SCD button in Screen 2.

**Note: The RFPS also participates in system manual BITE. The BITE operation is similar to FP mode except in emitter identification. In BITE only BITE tracks from library are considered for matching.**

**5.5.4.6.6.5.1 Performing Data Acquisition**. It enables the user to perform the **Data Acquisition** process in FP Mode.

5.5.4.6.6.5.1.a In System mode - FP, the Data Acquisition shall be performed automatically based on the ESM track data received from the SCD.

5.5.4.6.6.5.1.b In BITE mode, the Data Acquisition shall be performed based on the BITE track received from the SCD.

5.5.4.6.6.5.1.c The track parameters shall be displayed in ESM Track Data Window and DAU, DSP and EI parameters shall be updated in **Command window**.

5.5.4.6.6.5.1.d The LCIU then generates command words for DAU and the DAU hardware is configured accordingly. The DAU starts acquiring the IF data.

5.5.4.6.6.5.1.e After data acquisition, a message shall be sent to SCD indicating the completion of acquisition. Then, LCIU stores digitized IF data with date and time affixed and the DAU Raw Data log file shall be created.

5.5.4.6.6.5.1.f The user shall be able to view the acquired Raw Data details in **DAU Raw Data Display Window** as shown in **Figure-5.293**and **Waterfall Display Window**.

SHAKTI : UHB\Ch5 Page 427 of 614

![](_page_431_Figure_1.jpeg)

**Figure-5.293: RFPS Screen 1 with DAU Raw data**

SHAKTI : UHB\Ch5 Page 428 of 614

**Note: On clicking Stop FGA button, RFPS shall terminate feature extraction and shall report to SCD through Process Status message.**

**5.5.4.6.6.5.1.1 ESM Track Data Window**.The **ESM Track Parameter Window** shall display the track parameters received from the SCD or track parameters of log files selected from the DAU Data Log. The parameters include Track No, Emitter Type, PRI Type, PRF(Hz), Scan Type, Freq Min, Freq Max, PW(µSec), Amp(dB), ASP(mSec), RF Attenuation, IF BW(MHz) and Mode.

![](_page_432_Picture_3.jpeg)

**Figure-5.294: ESM Track Data Window**

**5.5.4.6.6.5.1.2 Command Window**. In Finger Print mode, Command Window (as shown in **Figure-5.295**) includes **RFPS Configuration Parameters** window. This shall display the DAU, DSP, Emitter Identification parameters which shall be used to perform fine grain analysis of the selected track.

![](_page_432_Picture_6.jpeg)

**Figure-5.295: Command Window**

SHAKTI : UHB\Ch5 Page 429 of 614

**5.5.4.6.6.5.1.3 DAU Raw Data Display**. This shall display the digitized data acquired by the DAU after completion of data acquisition. The DAU Raw data plot shall be shown with respect to Sample Numbers (X-Axis) and Amplitude (Y-Axis).

![](_page_433_Figure_2.jpeg)

**Figure-5.296: DAU Raw Data Display**

5.5.4.6.6.5.1.3.1 Selective pulse processing shall be performed by entering **Stop Pulse** option from of DAU Raw Data Display controls for fine grain analysis. By default, all pulses are processed.

**Note: If the acquired data is not captured properly then user shall modify the DAU parameters and click on Capture Data button in DAU Raw Data Display to recapture the raw data.**

**5.5.4.6.6.5.1.4 Deleting Raw Data**.It enables the user to delete the acquired raw data along with the generated DAU log file on User's confirmation.

5.5.4.6.6.5.1.4.1 From Toolbar when user clicks on **Delete Raw Data** icon, the following screen shall appear.

SHAKTI : UHB\Ch5 Page 430 of 614

![](_page_434_Picture_1.jpeg)

**Figure-5.297: DAU Raw Data Confirmation**

5.5.4.6.6.5.1.4.2 When Yes button is clicked the corresponding raw data along with the generated log file shall be deleted. When No button is clicked, the delete raw data operation shall be cancelled.

**5.5.4.6.6.5.1.5 Waterfall Display**. The **Waterfall display** (as shown in **Figure -5.298**) shall be drawn with respect to PRI [msec], Freq [MHz] (X-Axis) and Pulse No. (Y-Axis).

![](_page_434_Figure_5.jpeg)

**Figure -5.298: Waterfall Display**

**5.5.4.6.6.5.2 Performing Feature Extraction**. It enables the user to perform the **Feature Extraction** process in System Mode – FP and BITE Mode.

5.5.4.6.6.5.2.a Feature extraction process is initiated automatically on completion of data acquisition or manually in off-line analysis by clicking the **Start FGA** button in **DAU Raw Data Display.** 

5.5.4.6.6.5.2.b Local Controller generates command words and provides IF data to the DSP to perform the job of feature extraction.

5.5.4.6.6.5.2.c When this processing is in progress, **Message/Status window** displays message indicating "**DSP processing is in progress**".

5.5.4.6.6.5.2.d On completion of this process, the TFGD will be stored in TFGD log file with

SHAKTI : UHB\Ch5 Page 431 of 614

date and time stamp affixed.

5.5.4.6.6.5.2.e The Results view as shown in **Figure-5.299**will be displayed as reported by DSP with the multiple tracks list if any. By default the TFGD of first track will appear in TFGD Display. The Graphical Displays will be displayed based on Graphical data obtained from the Fine Grain Analysis.

SHAKTI : UHB\Ch5 Page 432 of 614

![](_page_436_Figure_1.jpeg)

**Figure-5.299: Screen 2 of RFPS results view**

SHAKTI : UHB\Ch5 Page 433 of 614

**Note: Click on 'Send to SCD' button, RFPS Fine grain results of designated track details are sent to SCD.**

**5.5.4.6.6.5.2.1 RFPS Track Data Display**.The **RFPS Tracks window** shall display the multiple track fine grain data. After the completion of fine grain analysis, the tracks detected by RFPS shall be displayed in TFGD Track Data display (as shown in **Figure-5.300**) with the key parameters. RFPS can detect maximum of 8 tracks during the fine grain analysis of ESM track. For each track, type of emitter, type of modulation, type of Scan, type of PRI, frequency, PRI, pulse width and amplitude are displayed. Maximum, minimum and average values are displayed for frequency and PRI.

![](_page_437_Picture_3.jpeg)

**Figure-5.300: TFGD Track Data Display**

**5.5.4.6.6.5.2.2 Track Fine Grain Data (TFGD) Window**.The **Track Fine Grain Data (TFGD)** Window shall display the Track fine grain data generated from Feature Extraction process in TFGD Display and Pulse List Display.

SHAKTI : UHB\Ch5 Page 434 of 614

![](_page_438_Figure_1.jpeg)

**Figure-5.301: Track Fine Grain Data (TFGD) Window**

**5.5.4.6.6.5.2.3 Track Fine Grain Data (TFGD) – TFGD Display**. **Track Fine Grain Data** displays the parameters measured for the selected track (by default first track) as shown in **Figure-5.301**. The TFGD Window is dynamically set to display the relevant parameters based on the emitter details like Emitter Type, PRI Type, Intra Modulation type, Scan Type etc. Click on **Detailed TFGD** button to view detailed parameters of a particular track. When multiple tracks are detected by RFPS, **Initiate EI** button is enabled. On clicking this button, emitter identification will be performed for the selected track and EI results will be displayed in Emitter Identity Window.

- (a) **List Agile Freq** is enabled when type of emitter is Pulsed Frequency Agility or Pulsed – Frequency Diversity. Click **List Agile Freq.** Agile Frequency List is displayed.
- (b) **List Agile PW** is enabled when type of emitter is Pulsed PW Agility. Click **List Agile PW.** Pulse Width Agility is displayed.
- (c) **List Agile Freq** or **List Agile PW** is enabled when type of emitter is Frequency Agility or PW Agility. Click the respective buttons to view the respective lists.
- (d) **List Avg Spot PRI** is enabled if the type of PRI is Stagger and Sliding or Dwell & Switch. Click to view Spot PRI List and Dwell and Switch List respectively. Is able to display up to 128 spot PRIs.

SHAKTI : UHB\Ch5 Page 435 of 614

- (e) **Initiate EI** is enabled only when multiple tracks are present. Click to start emitter identification process for the selected track.
- (f) Detailed TFGD with Ensembles Avg Frequency and Amplitude profiles and track parameters is displayed when **Detailed TFGD** is clicked.
- (g) ESM value is displayed only if the processed track is received from SCD.

**Note: Upon selecting the required track from the RFPS Tracks the selected Track is highlighted and details of the track are displayed in the Results View.**

**5.5.4.6.6.5.2.4 Track Fine Grain Data (TFGD) Pulsed List**.This UI facilitates the user to view the TFGD data generated from the Fine Grain Analysis and the details of each pulse in a trace. This shall enable the user to look for any abnormal variations in these parameters on pulse-to-pulse basis.

5.5.4.6.6.5.2.4.1 Select Track Fine Grain Data (TFGD) – Pulsed list to view the Frequency, pulse width, amplitude, PRI and of each pulse.

![](_page_439_Picture_7.jpeg)

**Figure-5.302: Pulse List Display**

5.5.4.6.6.5.2.4.2 Select random pulses.

5.5.4.6.6.5.2.4.3 Click on **Get Statistics** to view the respective statistics Min, Max and Mean values updated in Frequency and Pulse width group-boxes.

SHAKTI : UHB\Ch5 Page 436 of 614

5.5.4.6.6.5.2.4.4 Click on **Get Intra Pulse Plot** to view the Graphical Displays – Intra-Pulse with the details of selected pulses.

5.5.4.6.6.5.2.4.5 When you do not select any pulse and click on **Get Statistics** or **Get Intra Pulse Plot** the respective validation messages are displayed.

**5.5.4.6.6.5.2.5 Detailed TFGD Display**. This UI will display the detailed TFGD of the track along with Ensembled average amplitude profile & Ensembled average frequency profile displays.

5.5.4.6.6.5.2.5.1 From **TFGD Display** when user clicks on **Detailed TFGD** button, the following dialog will be displayed with the details of Parameter, TFGD value, and ESM value.

![](_page_440_Figure_5.jpeg)

**Figure-5.303: Detailed TFGD dialog**

5.5.4.6.6.5.2.5.2 On clicking '**Print Preview'** button, a PDF file with the selected Detailed TFGD parameters and profiles are displayed which can be saved or printed.

5.5.4.6.6.5.2.5.3 On clicking '**Close'** button, the Detailed TFGD Display dialog will be

SHAKTI : UHB\Ch5 Page 437 of 614

closed.

**5.5.4.6.6.5.2.6 Emitter Identity**. This UI shall display the Emitter Identification Search results. This displays the list of Radars of RFPS library that match the intercepted emitter. Radars identified with the confidence threshold, and higher are displayed. EI results are prioritized based on confidence level. Radar ID, Radar Name, Mode, Platform and Confidence Level of Identification is displayed in Emitter Identity. On clicking View Parameters button, the View Parameters dialog box is displayed. The parameters of selected radar with intercepted emitter parameters are displayed in View Parameters dialog box.

![](_page_441_Picture_3.jpeg)

**Figure-5.304: Emitter Identity**

**5.5.4.6.6.5.2.6.1 View Parameters**. This GUI shall display the parameters of the selected radar in Emitter Identity with intercepted emitter parameters. This GUI shall allow the user to update matched emitter record of the RFPS library with intercepted emitter parameters after confirming on the Update Emitter dialog box, with or without the frequency profile. Click on 'View Parameters' in Emitter Identity. View Parameters displays Emitter parameters (incoming and library values), Ensembled Avg Freq profiles for incoming and library values.

SHAKTI : UHB\Ch5 Page 438 of 614

![](_page_442_Figure_1.jpeg)

**Figure-5.305: View Parameters dialog**

5.5.4.6.6.5.2.6.1.1 Click on '**Update Emitter'** to update RFPS library with the emitter details. Confirmation message is displayed.

![](_page_442_Picture_4.jpeg)

**Figure-5.306: Update Emitter Confirmation message**

5.5.4.6.6.5.2.6.1.2 Click on '**Close'** to cancel the update emitter operation.

#### **5.5.4.6.7 Graphical Display**.

**5.5.4.6.7.1 Intra-Pulse Display**. Intra-pulse Display facilitates the user to view the graphical data of emitter parameters in various intra-pulse graphical formats. User can view the plots in Time, Frequency and Time-Frequency domains using Graphic Display Query.

5.5.4.6.7.1.1 An option is provided to view previous and next pulse profiles in Graphical

SHAKTI : UHB\Ch5 Page 439 of 614

displays window of Intra-pulse display using previous (<<) and next (>>) buttons.

- 5.5.4.6.7.1.2 On completion of Fine Grain Analysis, Results View is updated with the TFGD data of the first RFPS Track. The time domain plots for the first pulse are displayed. Previous(<<) is disabled and Next (>>) is enabled.
- 5.5.4.6.7.1.3 Number of pulses processed and the current pulse number are displayed in the respective fields.
- 5.5.4.6.7.1.4 Select Intra-Pulse from Graphical Displays window. Graphic Display Query dialog is displayed or select a pulse from Track Fine Grain Data (TFGD) – Pulse list.
- 5.5.4.6.7.1.5 Click on '**GetIntra-Pulse Plot'** in Track Fine Grain Data (TFGD) Pulse List to display Graphic Display Query. Pulse number combo-box is disabled.

![](_page_443_Picture_6.jpeg)

**Figure-5.307: Graphic Display Query**

- 5.5.4.6.7.1.6 Select a domain and Pulse Number in Graphic Display Query.
- 5.5.4.6.7.1.7 Click on '**Ok'** button then the respective profiles is displayed in the graph as follows :

**Table-5.20: Intra-Pulse Display**

| Ser | Domain         | Pulse Number | Expected Result                                   |
|-----|----------------|--------------|---------------------------------------------------|
| 1   | Time           | 1            | Amplitude and Frequency profiles are<br>displayed |
| 2   | Frequency      | 1            | Spectrum and STFT profiles are<br>displayed       |
| 3   | Time-Frequency | 1            | Spectrogram and Contour profiles are<br>displayed |

SHAKTI : UHB\Ch5 Page 440 of 614

## 5.5.4.6.7.1.8 Click **Cancel** to close Graphic Display Query.

![](_page_444_Figure_2.jpeg)

**Figure-5.308: Intra-Pulse Display**

**5.5.4.6.7.2 Overlapped Display**.Over This feature enables the user to view the overlapped displays of Amplitude, Frequency and Spectrum in a trace. When this option is selected, the Graphic Display Query dialog box is displayed with the Continuous and Discrete options. If Continuous is selected, the user shall select Start Pulse No. and number of pulses to be overlapped and click the OK button. If discrete option is selected, the user shall select the pulse numbers randomly and click the Ok button. Based on the option selected by the user, LCIU shall send the corresponding plot ID to retrieve the graphical data from DSP, and displays it in the Overlapped Graphical Display. In the overlapped plot a colour coded legend is provided to indicate the pulse number. For CW, this tab must be disabled.

5.5.4.6.7.2.1 Select Overlapped in Graphical Displays. Graphic Display Query dialog is displayed.

SHAKTI : UHB\Ch5 Page 441 of 614

![](_page_445_Picture_1.jpeg)

**Figure-5.309: Graphic Query Box**

5.5.4.6.7.2.2 Select **Continuous** radio button to enable the continuous group box. Discrete group box is disabled.

- (a) Select the pulse number from **Start Pulse Number** combo box.
- (b) Select the Number of Pulses to be overlapped from the combo box. Based on the Start Pulse number this field is updated.
- (c) A maximum of 16 pulses can be selected
- (d) Select discrete radio button to enable the discrete group box.
- (e) Continuous group box is disabled.
- (f) Select Pulse number from the pulse numbers list box.
- (g) A minimum of four pulse numbers and maximum of 16 can be selected.
- (h) If the pulse numbers selected is less than four, an error message is displayed.
- 5.5.4.6.7.2.3 Click on '**Ok'** button.
- 5.5.4.6.7.2.3 Amplitude, Frequency and Spectrum profiles of selected pulses are overlapped and updated accordingly.
- 5.5.4.6.7.2.4 Click on '**Cancel'** to close Graphic Display Query.

SHAKTI : UHB\Ch5 Page 442 of 614

![](_page_446_Figure_1.jpeg)

**Figure-5.310: Overlapped Display**

**5.5.4.6.7.3 Ensembled Display**.This display feature facilitates the user to view the Average Amplitude & Average Frequency profiles on a sample-to-sample basis. When this option is selected, LCIU shall send the corresponding plot ID to DSP to retrieve the respective graphical data and display it in the Ensembled display window. For CW, this tab must be disabled.

5.5.4.6.7.3.1 Select Ensembled in Graphical Displays.

5.5.4.6.7.3.2 Average Amplitude and Average Frequency profiles are displayed for all the pulses on sample-to-sample basis.

SHAKTI : UHB\Ch5 Page 443 of 614

![](_page_447_Figure_1.jpeg)

**Figure-5.311: Ensembled Display**

**5.5.4.6.7.4 Inter Pulse Display**.This display feature facilitates the user to view the graphical data of emitter parameters in various inter-pulse graphical formats. When this option is clicked, LCIU shall send the corresponding plot ID to DSP to retrieve the graphical data and displays it in the Inter-Pulse Graphical Display. For CW track, this tab is disabled.

5.5.4.6.7.4.1 Select Inter-Pulse in Graphical Displays.

5.5.4.6.7.4.2 Amplitude, Frequency, Pulse Width and PRI data between successive pulses is displayed.

SHAKTI : UHB\Ch5 Page 444 of 614

![](_page_448_Figure_1.jpeg)

**Figure-5.312: Inter Pulse Display**

- **5.5.4.6.7.5 Histogram Display**.This display feature facilitates the user to view the graphical data of emitter parameters in various histogram graphical formats. When this option is clicked, LCIU shall send the corresponding plot ID to DSP to retrieve the graphical data and displays it in the Histogram Graphical Display.
- 5.5.4.6.7.5.a A facility is provided to the user to select the viewing options like Normal or Logarithmic and change the bin width of PW, Frequency and PRI to redraw the histogram displays. For CW, this tab is disabled.
- 5.5.4.6.7.5.b Select Histogram from Graphical Display.
- 5.5.4.6.7.5.c Select **Normal** to display the plots for the full pulse count.
- 5.5.4.6.7.5.d Select **Log** to display the plots for the logarithmic values. The line edits for Freq Bin Width, PW Bin Width and PRI Bin Width are disabled.
- 5.5.4.6.7.5.e Select **Normal** to display the plots for the normal values. The line edits for

Freq Bin Width, PW Bin Width and PRI Bin Width are enabled.

5.5.4.6.7.5.f By default the bin width is set to 10. User can update this when **Normal** is selected.

![](_page_449_Figure_3.jpeg)

**Figure-5.313: Histogram Display**

- 5.5.4.6.7.5.g Histogram is updated for Frequency, Pulse Width, and PRI as per the defined bin width.
- 5.5.4.6.7.5.h The bin widths can be changed by the user for each plot.
- 5.5.4.6.7.5.j The **Frequency Bin Width** range is 4 to 10. Error message is displayed if the entered value is not within the range.
- 5.5.4.6.7.5.k On focus out of **Frequency Bin Width** line edit, the Frequency plot is updated with the specified bin width.
- 5.5.4.6.7.5.l The **PW Bin Width** range is 4 to 10. Error message is displayed if the entered value is not within the range.
- 5.5.4.6.7.5.m On focus out of **PW Bin Width** line edit, the PW plot is updated with the

SHAKTI : UHB\Ch5 Page 446 of 614

specified bin width.

5.5.4.6.7.5.n The **PRI Bin Width** range is 4 to 10. Error message is displayed if the entered value is not within the range.

5.5.4.6.7.5.p On focus out of **PRI Bin Width** line edit, the PRI plot is updated with the specified bin width.

**5.5.4.6.7.6 User Defined Plots**.This display feature shall enable the user to view the graphical data for the user selected parameters in the Graphical Display. For CW, this tab is disabled.

5.5.4.6.7.6.1 Select User Defined Plots from Graphical Displays. User Defined PlotsQuery is displayed.

![](_page_450_Picture_6.jpeg)

**Figure-5.314: User Defined Plots query**

5.5.4.6.7.6.2 Select the options as mentioned in the Expected Result section.

5.5.4.6.7.6.3 Click **Ok**. The respective plots are displayed.

5.5.4.6.7.6.4 Click **Cancel** to close the window.

SHAKTI : UHB\Ch5 Page 447 of 614

![](_page_451_Figure_1.jpeg)

**Figure-5.315: User Defined Plots**

**5.5.4.6.8 Performing Emitter Identification**.This enables the user to perform the Emitter Identification process in System Mode – FP and BITE Mode. The Emitter identification will be performed by establishing the connection with the database of Emitter library, which will be built in Postgre SQL database. This will display the **Emitter Identification Search results** that are obtained by performing level search. The **Emitter Identity window** shows list of Emitters in library matching with intercepted emitter. Emitters matching with confidence level greater than set confidence threshold are only shown. **Emitter identification results** are prioritized based on confidence level of match. The details of Radar ID, Radar Name, Mode, Platform, and Confidence Level of Identification will be shown in **Emitter Identity window**. The results of feature extraction will be utilized to perform feature Identification, when either single track or multiple tracks are reported by DSP.

- (a) In case of **single track**, the emitter identification process will be performed automatically.
- (b) In case of multiple tracks, the emitter identification will be performed by selecting desired track from RFPS Tracks window and click on Initiate EI button in TFGD Display.
- 5.5.4.6.8.a When the Emitter Identification task is in progress, the **Message/Status window** will be displayed as "Emitter Identification in progress".
- **5.5.4.6.8.1 Emitter Identification – Failure Case**.If the emitters are matched with less confidence level than set confidence then **Set Confidence Level** dialog box will

SHAKTI : UHB\Ch5 Page 448 of 614

appear prompting the user to change the confidence level to proceed for EI.

![](_page_452_Picture_2.jpeg)

**Figure-5.316: Change Confidence Level Dialog**

5.5.4.6.8.1.1 User will select the confidence level from the respective combo box and click **Ok** button. After setting the confidence level, Emitter Identification will be performed and results are displayed in **Emitter identity** window.

5.5.4.6.8.1.2 If **Cancel** button is clicked, the **Change Confidence Level dialog** will be closed.

**5.5.4.6.8.2 Emitter Identification – Match Found Case**.After performing Emitter Identification if the match is found for intercepted emitter, the finger print data along with emitter identification results will be sent to SCD automatically.

5.5.4.6.8.2.1 The **Emitter Identification Display** will appear comprising of the Database S.No, Radar Type, Radar Name, Mode and Location along with the confidence of match at each level.

![](_page_452_Picture_8.jpeg)

**Figure-5.317: EI Search Results Display**

5.5.4.6.8.2.2 User will click on **View Parameters** button of required Radar from the list view, the **View parameters** dialog will appear with the matched radar parameter library value details along with the corresponding incoming values. User can update the emitter with or without frequency profile

SHAKTI : UHB\Ch5 Page 449 of 614

![](_page_453_Figure_1.jpeg)

**Figure-5.318: View Parameters dialog**

SHAKTI : UHB\Ch5 Page 450 of 614

5.5.4.6.8.2.3 If User selects **Update Emitter** button, a confirmation message will appear for updating emitter.

![](_page_454_Picture_2.jpeg)

**Figure-5.319: Message box for switch user**

5.5.4.6.8.2.4 If on confirmation emitter is updated after database authentication as show in **Figure 5.321.**

![](_page_454_Picture_5.jpeg)

**Figure-5.320: Database Authentication**

5.5.4.6.8.2.5 If user clicks on **Close** button the update emitter operation will be cancelled.

**5.5.4.6.8.3 Emitter Identification – Match Not Found**.After performing **Emitter Identification**, if match not found for intercepted emitter in Emitter library, the Finger Print data without **EI results** will be sent to SCD. A message box will appear indicating the same and if the user desires, the emitter details will be added as a new emitter to the database.

![](_page_454_Picture_9.jpeg)

**Figure-5.321: No Match Found Message**

SHAKTI : UHB\Ch5 Page 451 of 614

(a) On clicking **Yes** button, the Add New Emitter dialog will appear as shown below.

![](_page_455_Picture_2.jpeg)

![](_page_455_Picture_3.jpeg)

**Figure-5.322: Add New Emitter dialog**

5.5.4.6.8.3.1 User should enter Platform Class, Radar name, platform Name, Radar type, Mode & Country name and click on **Add Emitter** button, a confirmation box will appear before proceeding with the addition of new emitter.

![](_page_455_Picture_6.jpeg)

**Figure-5.323: Add Emitter Confirmation**

SHAKTI : UHB\Ch5 Page 452 of 614

- 5.5.4.6.8.3.2 If user clicks on **Yes** button, the radar parameters will be added as new emitter to the database.
- 5.5.4.6.8.3.3 If user clicks on **No** button, the Add Emitter operation will be cancelled.
- 5.5.4.6.8.3.4 If **Cancel** button is clicked, the Add New Emitter dialog will be closed.
- **5.5.4.6.9 System Record Feature**.This feature shall enable the user to capture and store the DAU raw data for designated ESM tracks. It shall be intimated to the SCD that the data has only been recorded. For this captured data the fine grain analysis shall be performed offline.
- **5.5.4.6.10 Datalog Menu**.This feature shall allow the user to select required **Datalog** menu options like TFGD and DAU Raw Data.
- 5.5.4.6.10.a From Menu bar when user selects **Datalog** Menu, the following sub-menu items shall be displayed.

![](_page_456_Picture_7.jpeg)

**Figure-5.324: Data log Menu**

Based on the option selected by the user, the corresponding actions shall be performed.

- **5.5.4.6.10.1 TFGD Data**.This feature shall allow the user to view Track Fine Grain Data that is stored in a log file with date and time stamp.
- 5.5.4.6.10.1.a From Datalog Menu when user selects **TFGD** option, Select TFGD Data Log file dialog shall appears.
- 5.5.4.6.10.1.b User shall select start and End dates from the respective combo box and click on **Browse** button to select the log files.
- 5.5.4.6.10.1.c The selected path shall be displayed in the Log Dir Edit box and the Log files stored between the specified dates shall be listed in the list control as show below.
- 5.5.4.6.10.1.d On selecting any one of the log file from the list, **Delete**, **Rename** and **OK** buttons shall be enabled.
- 5.5.4.6.10.1.e When user clicks on **Delete** button a delete confirmation message shall appear.

SHAKTI : UHB\Ch5 Page 453 of 614

(a) On clicking **Yes** button in confirmation message, the selected log file shall be deleted from the list view and TFGD log.

![](_page_457_Picture_2.jpeg)

**Figure-5.325: Select TFGD Log File dialog**

![](_page_457_Picture_4.jpeg)

**Figure-5.326: Select TFGD Log File dialog**

SHAKTI : UHB\Ch5 Page 454 of 614

5.5.4.6.10.1.f On clicking **No** button in confirmation, the delete operation shall be cancelled.

![](_page_458_Picture_2.jpeg)

**Figure-5.327: Delete Confirmation**

5.5.4.6.10.1.g When user clicks on **Rename** button, Rename dialog shall appear as shown below.

![](_page_458_Picture_5.jpeg)

**Figure-5.328: Rename Dialog**

- 5.5.4.6.10.1.h User shall enter the New File Name and click on **Rename** button, the file name shall be renamed excluding date and time and saved with the new file name.
- 5.5.4.6.10.1.j To cancel Rename operation, user shall click on **Cancel** button in Rename dialog.
- 5.5.4.6.10.1.k When user clicks on OK button, the View changes to Results View.
  - (a) RFPS Tracks Parameters, Track Fine Grain Data (TFGD) TFGD and Ensembled Display in Graphical Display are updated with the data from the TFGD Log file.
  - (b) Track Fine Grain Data (TFGD) Pulse List is disabled.
  - (c) Send to SCD and Detailed TFGD are disabled.
  - (d) In Graphical Display, Ensembled is enabled and all the other tabs are disabled.
  - (e) If multiple TFGDs are available in the TFGD Log file then RFPS Tracks is

SHAKTI : UHB\Ch5 Page 455 of 614

updated with the multiple tracks.

- (f) The TFGD info for the first RFPS Track is displayed in Fine Grain Data (TFGD) - TFGD and Ensembled Display.
- (g) Double click any other RFPS Track in RFPS Tracks to display the corresponding TFGD in the Fine Grain Data (TFGD) - TFGD and the profile in Ensembled Display.
- (h) Click Initiate EI to start emitter identification.
- 5.5.4.6.10.1.l On clicking **Cancel** Button, Select TFGD Log file dialog shall be closed without performing corresponding operation.
- **5.5.4.6.10.2 Reply DAU Raw Data**. This feature shall enable the user to perform Offline analysis on DAU Raw Data that is stored in a log file with date and time stamp.
- 5.5.4.6.10.2.a From Datalog Menu when user selects **DAU Raw Data** option, Select DAU Raw Data Log file dialog shall appears.

![](_page_459_Picture_8.jpeg)

**Figure-5.329: Select DAU Raw Data Log File**

5.5.4.6.10.2.b User shall select start and End dates from the respective combo box and click on **Browse** button to select the log files.

SHAKTI : UHB\Ch5 Page 456 of 614

5.5.4.6.10.2.c The selected path shall be displayed in the Log Dir Edit box and the Log files stored between the specified dates shall be listed in the list control as show below.

![](_page_460_Picture_2.jpeg)

**Figure-5.330: Select DAU Raw Data Log File**

**Note: The already processed Raw Data shall be indicated as dimming or graying to the operator. A pointer/ marker shall be provided to indicate the currently selected Raw Data file.**

- 5.5.4.6.10.2.d On selecting any one of the log file from the list, **Delete**, **Rename** and **Open** buttons shall be enabled.
- 5.5.4.6.10.2.e When user clicks on **Delete** button, a delete confirmation message shall appear.
  - (a) On clicking **Yes** button in confirmation message, the selected log file shall be deleted from the list view and DAU log.
  - (b) On clicking **No** button in confirmation, the delete operation shall be cancelled.
- 5.5.4.6.10.2.f When user clicks on **Rename** button, Rename dialog shall appear as shown below.

SHAKTI : UHB\Ch5 Page 457 of 614

![](_page_461_Picture_1.jpeg)

**Figure-5.331: Rename Dialog**

- 5.5.4.6.10.2.g User shall enter the New File Name and click on **Rename** button, the file name shall be renamed excluding date and time and saved with the new file name.
- 5.5.4.6.10.2.h To cancel Rename operation, use shall click on **Cancel** button in **Rename** dialog.
- 5.5.4.6.10.2.j When user clicks on **Open** button, the selected log file information shall be displayed in ESM Track Display, Waterfall Display, RFPS Configuration Parameter Window and DAU Raw Data Display.
- 5.5.4.6.10.2.k User shall initiate offline finger printing analysis on clicking **Start FGA** button of **DAU Raw Data Display**.
- 5.5.4.6.10.2.l When user clicks on **Cancel** Button, Select DAU Raw Data Log file dialog shall be closed without performing corresponding operation.
- **5.5.4.6.11 RFPS Library Management**.This feature shall allow the user to select required **RFPS Library Management** menu options like View database, List all Platforms, List All Radars, List Platforms for selected class, List Radars for given Platform, Add New

SHAKTI : UHB\Ch5 Page 458 of 614

Emitter, Delete Emitter, Update Emitter. Some of the options like Add New Emitter, Delete Emitter & Update Emitter options shall be accessible to the users with Commander Level privilege only.

5.5.4.6.11.a From Menu bar when user selects **RFPS Library Management** Menu, the following sub-menu items shall be displayed.

![](_page_462_Picture_3.jpeg)

**Figure-5.332: RFPS Library Management Menu**

5.5.4.6.11.b Based on the option selected by the user, the corresponding actions shall be performed.

**5.5.4.6.11.1 View Database**. This feature shall enable the user to view the database based on the Stored Records or Last Updated Records. Based on the Query inputs specified by the user, Query Results shall be displayed with the list of radar parameters.

5.5.4.6.11.1.1 From RFPS Library Management menu when user selects **View Database** option, the database records shall appear with default Start and End Date as shown below.

SHAKTI : UHB\Ch5 Page 459 of 614

![](_page_463_Figure_1.jpeg)

**Figure-5.333: View Database Dialog**

SHAKTI : UHB\Ch5 Page 460 of 614

- (a) By default **View All Records** option is selected.
- (b) User can select **Store** and choose Start and End dates from the respective combo box and click on **Fetch** button, to query database for stored records between specified dates.
- (c) User can select **Update** option, choose Start and End dates from the respective combo box and click on **Fetch** button, to query database for last update records between specified dates.
- 5.5.4.6.11.1.2 Based on the inputs specified by the user, the records will be retrieved from database and displayed in **RFPS library** List Control. The total number of records is also displayed.
  - (a) User can check Frequency option and enter Min & Max values.
  - (b) User can check PW option and enter Min & Max values.
  - (c) User can check PRI option and enter Min & Max values.
  - (d) User can check Frequency, PW, PRI options and enter Min and Max values for the respective parameters and select OR option.
  - (e) User can check Frequency, PW, PRI options and enter Min and Max values for the respective parameters and select AND option.
- 5.5.4.6.11.1.3 On clicking **Query** button, the Query results will be displayed with the list of radar parameters based on the inputs specified by the user.
- 5.5.4.6.11.1.4 When user clicks on **Print Preview** button, a PDF file with the Query Results is displayed which can be saved or printed.
- 5.5.4.6.11.1.5 When user clicks on **Close** button, the View Database dialog will be closed.
- **5.5.4.6.11.2 List All Platforms**.This feature shall enable the user to view the complete list of all platforms that are available in the RFPS Library.
- 5.5.4.6.11.2.1 From RFPS Library Management menu when user selects **List All Platforms** option, the following dialog shall appear.

SHAKTI : UHB\Ch5 Page 461 of 614

![](_page_465_Picture_1.jpeg)

**Figure-5.334: List All Platforms Dialog**

- 5.5.4.6.11.2.2 When user clicks on **Print** button, the result of the Query shall be printed or saved to a PDF file. Refer to **Print Section**.
- 5.5.4.6.11.2.3 When user clicks on **Ok** button, List All Platforms dialog shall be closed.
- **5.5.4.6.11.3 List All Radars**. This enables the user to view the complete list of radar classes that are available in the RFPS library.
- 5.5.4.6.11.3.1 From RFPS Library Management menu when user selects **List All Radars**  option, the following dialog shall appear.

![](_page_465_Picture_7.jpeg)

**Figure-5.335: List all Radar Dialog for Selected Radar Dialog**

- 5.5.4.6.11.3.2 When user clicks on **Print** button, the result of the Query shall be printed or saved to a PDF file. Refer to **Print Section**.
- 5.5.4.6.11.3.3 When user clicks on **Ok** button, List All Radars dialog shall be closed.

SHAKTI : UHB\Ch5 Page 462 of 614

- **5.5.4.6.11.4 List Platforms for Selected Radar Name**.This enables the user to view the complete list of platforms for a selected radar class that are available in the RFPS Emitter library.
- 5.5.4.6.11.4.1 From RFPS Library Management menu when user selects List Platforms for Selected Radar Name option, the following dialog will appear.

![](_page_466_Figure_3.jpeg)

**Figure-5.336: List Platforms for Selected Radar Dialog**

- 5.5.4.6.11.4.2 User can select the **Radar Name** from the list and accordingly list of platforms along with radar serial number will appear in the List control.
- 5.5.4.6.11.4.3 User can select Radar Serial number by double clicking on the required row of the list and click on **View Parameters** button. The **View Parameters** dialog will appear for the selected Radar as shown below.

SHAKTI : UHB\Ch5 Page 463 of 614

![](_page_467_Figure_1.jpeg)

**Figure-5.337: View Parameters Dialog**

- 5.5.4.6.11.4.4 When user clicks on **Print** button, the result of the Query shall be printed or saved to a PDF file. Refer to **Print Section**.
- 5.5.4.6.11.4.5 When user clicks on **Close** button, the List Platforms for selected class dialog shall be closed.
- **5.5.4.6.11.5 List Radars for Given Platform**. This enables the user to view the complete list of radars for a selected platform that are available in the Emitter library.
- 5.5.4.6.11.5.1 From **RFPS Library Management** menu when user selects **List Radars for Given Platform** option, the following dialog will appear.

SHAKTI : UHB\Ch5 Page 464 of 614

![](_page_468_Picture_1.jpeg)

**Figure-5.338: List Radars for Given Platform Dialog**

- 5.5.4.6.11.5.2 User can select the **Platform Name** from the list of Platforms and accordingly list of radars along with radar serial number will appear in the List control.
- 5.5.4.6.11.5.3 User can select **Radar Serial number** by double clicking on the required row of the list and click on **View Parameters** button. The View Parameters dialog will appear for the selected Radar.
- 5.5.4.6.11.5.4 When user clicks on **Close** button, the **View parameters** window for selected class dialog will be closed.
- **5.5.4.6.11.6 Add New Emitter**. This feature shall enable the user to add new emitter record to RFPS library from the TFGD log files. From RFPS Library Management menu when user selects Add New Emitter option, an open file dialog shall appear.

SHAKTI : UHB\Ch5 Page 465 of 614

![](_page_469_Figure_1.jpeg)

**Figure-5.339: Open File Dialog**

- 5.5.4.6.11.6.1 User shall browse and select the required log file, which consists of incoming parameters and click on **Add Emitter** button. The Add New Emitter dialog shall appear with the incoming Radar Parameters in a List control.
- 5.5.4.6.11.6.2 User can enter Radar Name, Carrier Name and other mandatory data by double clicking on the corresponding list cells and click on **Add Emitter** button.
- 5.5.4.6.11.6.3 On clicking this button, a confirmation message will appear before proceeding with the addition of new emitter as shown in **Figure 5.340**.
  - (a) If user clicks on **Yes** button, the incoming Radar parameters and the corresponding Frequency profile will be added to the database as New Emitter.
  - (b) If user clicks on **No** button, **Add New Emitter** operation will be cancelled.

SHAKTI : UHB\Ch5 Page 466 of 614

![](_page_470_Picture_1.jpeg)

**Figure-5.340: Add New Emitter Dialog**

- 5.5.4.6.11.6.4 When user click on '**Cancel'** Button, **Add New Emitter** dialog will be closed without performing corresponding operation.
- **5.5.4.6.11.7 Delete Emitter**. This feature shall enable the user with Commander Level Privilege to delete emitter details from RFPS library.
- 5.5.4.6.11.7.1 From **View Database** dialog when user selects a **record** from the list and clicks the **Delete** button, the following dialog shall appear.
- 5.5.4.6.11.7.2 A confirmation message appears before proceeding with deletion of emitter on database authentication.

SHAKTI : UHB\Ch5 Page 467 of 614

![](_page_471_Picture_1.jpeg)

**Figure-5.341: Delete Emitter Dialog**

SHAKTI : UHB\Ch5 Page 468 of 614

- (a) If user clicks on **Yes** button, the radar details for the selected radar shall be deleted from the database.
- (b) If user clicks on **No** button, Delete Emitter operation shall be cancelled.
- **5.5.4.6.11.8 Update Emitter**.This feature shall enable the user with Commander Level Privilege to edit the emitter information and update to the database.
- 5.5.4.6.11.8.1 From **View Database** dialog when user selects a record from the list and clicks the **Update** button, the following dialog shall appear.
- 5.5.4.6.11.8.2 User shall edit any of the editable Radar parameters in Modified Value column by double clicking on the cells of the list control and click on **Update Emitter** button.
- 5.5.4.6.11.8.3 On clicking this button, a confirmation message shall appear before proceeding with the update of library record.

![](_page_472_Picture_7.jpeg)

**Figure-5.342: Update Emitter Dialog**

SHAKTI : UHB\Ch5 Page 469 of 614

![](_page_473_Picture_1.jpeg)

**Figure-5.343: Update Emitter Confirmation**

- (a) If user clicks on **Yes** button, the selected radar details along with its Frequency profile shall be updated in the database.
- (b) If user clicks on **No** button, Update Emitter operation shall be cancelled.
- 5.5.4.6.11.8.4 When user click on '**Cancel'** button, Update Emitter dialog shall be closed without performing corresponding operation.
- **5.5.4.6.11.9 Load RFPS Library**.This enables the user to load the imported file as Emitter library for use in the current mission. The system automatically saves current Emitter library in use and loads the selected Emitter library for use. On successful completion of loading, appending, updating a message will be displayed in **Message/Status window**.
- 5.5.4.6.11.9.a From **RFPS Library Management menu** when user selects **Load RFPS Library** option, the dialog shall appear as shown in **Figure-5.344**.
- 5.5.4.6.11.9.b User shall select start and End dates from the respective combo box and click on **Browse** button to select the RFPS Library file.
- 5.5.4.6.11.9.c The selected path shall be displayed in the File path Edit box and the files stored between the specified dates shall be listed in the list control as show below.

SHAKTI : UHB\Ch5 Page 470 of 614

![](_page_474_Picture_1.jpeg)

**Figure-5.344: Load RFPS library Dialog with library files**

5.5.4.6.11.9.d On selecting any one of the RFPS Library file from the list, **Load** button shall be enabled.

5.5.4.6.11.9.e When user clicks on **Load** button, the imported Library records from the selected file shall be displayed in **RFPS Library Records** dialog along with the Existing RFPS library records.

5.5.4.6.11.9.f The **matched records** will be shown with yellow color indication in Imported Library list control. The total number of Imported Records and Existing Records will appear in the respective edit box.

5.5.4.6.11.9.g When user clicks on **View** button upon selecting one of the matched records, the **View Libraries dialog** will appear with the Emitter parameters of imported library along with the Existing Library.

SHAKTI : UHB\Ch5 Page 471 of 614

![](_page_475_Figure_1.jpeg)

**Figure-5.345: Load RFPS library Details Dialog**

- 5.5.4.6.11.9.h When user clicks on **Update Emitter** button, the imported library record will be updated into the existing Emitter library.
- 5.5.4.6.11.9.j To **cancel** this operation, user can click on **Close** button of View Parameters dialog.
- 5.5.4.6.11.9.k When user clicks on **Load** button, the existing library will be replaced with all the records from the imported library.
- 5.5.4.6.11.9.l When user clicks on **Append** button, the unmatched records from the imported library will be added to the existing library.
- 5.5.4.6.11.9.m When user clicks on **Close** button of Load Emitter library dialog,the dialog will be closed without performing corresponding operation.

SHAKTI : UHB\Ch5 Page 472 of 614

![](_page_476_Figure_1.jpeg)

**Figure-5.346: View Parameters Dialog**

**5.5.4.6.11.10 Store RFPS Library**.This feature shall enable the user to store the RFPS Library records into a library file. Click **Store** to store the records displayed in RFPS Library table widget into a library file with current date and time at a predefined location.

- (a) **Store** button is enabled only when the records are fetched from the database.
- (b) Click **Store** to store the fetched records to a text file.
- (c) A Process message is displayed when the records are stored to the file.
- (d) An Error Message is displayed if the store functionality fails.

SHAKTI : UHB\Ch5 Page 473 of 614

![](_page_477_Figure_1.jpeg)

**Figure-5.347: Process message on successful store.**

- **5.5.4.6.12 User Management**.This feature shall allow the users with three privilege levels; Administrator, Commander and Operator to perform user management operations like Add User, Modify User, Delete User, Reset User Password and Change Password.
- 5.5.4.6.12.a If user has logged in with Administrator level privilege, the following dialog shall appear.
- 5.5.4.6.12.b Based on the option selected by the user, the corresponding actions shall be performed.

SHAKTI : UHB\Ch5 Page 474 of 614

![](_page_478_Picture_1.jpeg)

**Figure-5.348: User Management Window**

**5.5.4.6.12.1 Add User**.This feature facilitates creating new user. When this button is clicked, the Add User dialog box is displayed. The Administrator specifies the username, privilege and clicks the **Add** button. The new user details are created and added to the database.

- (a) Click **Add User** in User Management. Add User is displayed.
- (b) Enter a user name.
- (c) Select a privilege for the user.
- (d) Click **Add**. New user details are added to the database.
- (e) Click **Cancel** to cancel the operation.

SHAKTI : UHB\Ch5 Page 475 of 614

![](_page_479_Picture_1.jpeg)

**Figure-5.349: Add User Dialog box**

**5.5.4.6.12.2 Modify User**.This feature facilitates modifying existing user. When this button is clicked, Modify User is displayed. The Administrator selects the username, modifies the privilege and clicks **Modify**. The selected user details are modified and updated in the database.

- (a) Click **Modify User**. Modify User is displayed.
- (b) Select a User Name.
- (c) Select a privilege.
- (d) Click **Modify**. The user privileges are modified as selected. A Confirmation Message is displayed. Click **Yes** to confirm the modify operation. Click **No** to cancel.
- (e) Click **Cancel** to cancel the operation.

SHAKTI : UHB\Ch5 Page 476 of 614

![](_page_480_Picture_1.jpeg)

**Figure-5.350: Modify User Dialog Box**

![](_page_480_Picture_3.jpeg)

**Figure-5.351: Modify User Confirmation**

**5.5.4.6.12.3 Delete User**.This feature facilitates deleting an existing user. When this button is clicked, Delete User is displayed. The Administrator selects the username and clicks **Delete**. The selected user details are deleted from the database.

- (a) Click **Delete User**. Delete User is displayed.
- (b) Select a User Name.
- (c) Click **Delete**. The details of the selected user are deleted from the database. A Confirmation Message is displayed. Click **Yes** to confirm delete operation. Click **No** to cancel the operation.
- (d) Click **Cancel** to cancel the operation.

SHAKTI : UHB\Ch5 Page 477 of 614

![](_page_481_Picture_1.jpeg)

**Figure-5.352: Delete User Dialog box**

![](_page_481_Picture_3.jpeg)

**Figure-5.353: Delete User Confirmation**

**5.5.4.6.12.4 Reset User Password**.This feature facilitates re-setting the selected user password. When this button is clicked, Reset User Password is displayed. The Administrator selects the username and clicks **Reset**. The selected user password is reset in the database as the user name.

(a) Click **Reset User Password**. Reset User Password is displayed.

SHAKTI : UHB\Ch5 Page 478 of 614

![](_page_482_Picture_1.jpeg)

**Figure-5.354: Reset User Password Dialog box**

- (b) Select a User Name.
- (c) Click **Reset**. The password of the selected user is reset to the user name. A Confirmation Message is displayed. Click **Yes** to confirm the reset password operation. Click **No** to cancel the operation.

![](_page_482_Picture_5.jpeg)

**Figure-5.355: Reset User Password Confirmation**

- (d) Click **Cancel** to cancel the operation.
- **5.5.4.6.12.5 Change Password**.This feature facilitates changing the selected user password. When this button is clicked, Changer Password is displayed. The Administrator selects the username and clicks **Ok**. The selected user password is modified as mentioned.
  - (a) Click **Change Password**. Change Password is displayed.

SHAKTI : UHB\Ch5 Page 479 of 614

![](_page_483_Picture_1.jpeg)

**Figure-5.356: Change Password Dialog box**

- (b) Enter Old Password**.**
- (c) Enter New Password and Confirm password fields.
- (d) Click **Ok.** The password is changed as specified. Validation messages are displayed for respective validations for the password.

![](_page_483_Picture_6.jpeg)

**Figure-5.357: Change Password Validation Message**

- (e) Click **cancel** to cancel the operation.
- **5.5.4.6.13 FDL**. The Administrator View has FDL as one of the tabs. This feature enables the administrator to perform FDL related operations.
  - (a) Select FDL in the Administrator View, to view the available FDL operations you can perform.
  - (b) Connect to FDL button is enabled and other buttons are disabled. After connection is established, Connect to FDL button is disabled and other buttons are enabled.
  - (c) Click **Exit** to exit the application.

SHAKTI : UHB\Ch5 Page 480 of 614

![](_page_484_Picture_1.jpeg)

**Figure-5.358: FDL Tab**

- **5.5.4.6.13.1 Connect to FDL**.This command facilitates connecting to FDL which allows you perform other FDL operations.
  - (a) Click **Connect to FDL**. Connect to FDL is displayed.
  - (b) IP/System Name exists. Enter User Name and Password for the FDL system.
  - (c) Click **Connect.** On successful connection with FDL, Connect to FDL closes and other buttons in FDL are enabled.
  - (d) If connection fails, the respective error messages are displayed.
  - (e) Click **Cancel** to cancel the operation.

SHAKTI : UHB\Ch5 Page 481 of 614

![](_page_485_Picture_1.jpeg)

**Figure-5.359: Connect to FDL**

**5.5.4.6.13.2 Import RFPS Library**. This command facilitates importing of RFPS library files from FDL to RFPS.

(a) Click **Import RFPS Library**. Import RFPS Library is displayed.

![](_page_485_Picture_5.jpeg)

**Figure-5.360: Import RFPS Library**

(b) Select Start Date and End Date fields, by default End Date is current date of the system and the Start Date is a year early.

SHAKTI : UHB\Ch5 Page 482 of 614

- (c) **Note: Start Date must be less than End Date. If not, the respective validation message is displayed.**
- (d) If files exist within the specified dates on the FDL system, list of file names is displayed in Files List. If not, Files List is empty. Select different dates.
- (e) Select one or more files from Files List.
- (f) Click **Import** to import the selected file(s) to a pre-defined location on RFPS System. A success message is displayed.
- (g) Click **Cancel** button to close Import RFPS Library.
- **5.5.4.6.13.3 Export RFPS Library**.This command facilitates exporting of RFPS library files to FDL from RFPS.

![](_page_486_Picture_7.jpeg)

**Figure-5.361: Export RFPS Library Dialog Box**

- (a) Click **Export RFPS Library**. Export RFPS Library is displayed.
- (b) Select Start Date and End Date fields, by default End Date is current date of the system and the Start Date is a year early.
- (c) **Note: Start Date must be less than End Date. If not, the respective validation message is displayed.**
- (d) If files exist within the specified dates on the FDL system, list of file names is

SHAKTI : UHB\Ch5 Page 483 of 614

displayed in Files List. If not, Files List is empty. Select different dates.

- (e) Select one or more files from Files List.
- (f) Click Export to Export the selected file(s) to a pre-defined location in FDL. A success message is displayed.
- (g) Click Cancel button to close Export RFPS Library.

## **5.5.4.6.13.4 Import RFPS Data**. This UI facilitates importing of RFPS data files from FDL to RFPS.

![](_page_487_Picture_6.jpeg)

**Figure-5.362: Import RFPS Data**

- (a) Click **Import RFPS Data**. Import RFPS Data is displayed.
- (b) Select Start Date and End Date fields, by default End Date is current date of the system and the Start Date is a year early.
- (c) **Note: Start Date must be less than End Date. If not, the respective validation message is displayed.**
- (d) If files exist within the specified dates on the FDL system, list of file names is displayed in Files List. If not, Files List is empty. Select different dates.

SHAKTI : UHB\Ch5 Page 484 of 614

- (e) Select one or more files from Files List.
- (f) Click **Import** to import the selected file(s) to a pre-defined location on RFPS System. A success message is displayed.
- (g) Click **Cancel** button to close Import RFPS Data.

**5.5.4.6.13.5 Export RFPS Data**.This command facilitates exporting of RFPS data files to FDL from RFPS.

![](_page_488_Picture_5.jpeg)

**Figure-5.363: Export RFPS Data**

- (a) Click **Export** RFPS **Data**. Export RFPS Data is displayed.
- (b) Select Start Date and End Date fields by default End Date is current date of the system and the Start Date is a year early.
- (c) **Note**: **Start Date must be less than End Date. If not, the respective validation message is displayed.**
- (d) If files exist within the specified dates on the FDL system, list of file names is displayed in Files List. If not, Files List is empty. Select different dates.
- (e) Select one or more files from Files List.

SHAKTI : UHB\Ch5 Page 485 of 614

- (f) Click **Export** to Export the selected file(s) to a pre-defined location in FDL. A success message is displayed.
- (g) Click Cancel button to close Export RFPS Data.
- **5.5.4.6.14 Backup**. This feature facilitates the Administrator take backup of the Raw Data files, TFGD files and RFPS library files created and stored between the selected start & end dates.

![](_page_489_Picture_4.jpeg)

**Figure-5.364: Backup**

- (a) Select Backup in the Administrator View. The following is displayed:
- (b) Click **Browse (...) Button** to select a destination location to which the data files are copied.
- (c) Select the Start Date and End Date fields. By default End Date is current date of the system and the Start Date is a year early.
- (d) **Note: Start Date must be less than End Date. If not, the respective validation message is displayed.**
- (e) Select one or more data types check box from TFGD, DAU, and Library.
- (f) Click **Copy**. Data files selected are copied to the specified location with the folder name as Backup\_current date (ddmmyyyy). A process success message is

SHAKTI : UHB\Ch5 Page 486 of 614

displayed.

- (g) Click **Exit** to exit the application.
- **5.5.4.6.15 Help**.This feature facilitates the user in operating and troubleshooting the RFPS system. This shall provide context sensitive help and also help in the form of compiled HTML file, where keywords can be searched. Also help is provided for inferences to be made from various plots of different types of emitters.
  - (a) Select Help from the menu. The available options are displayed.
  - (b) Select **Contents** to display Help Contents
  - (c) Select **What's This** option and click anywhere in the application to display brief description for the selected item as tooltip.
  - (d) Select **About RFPS** to display About RFPS

![](_page_490_Picture_8.jpeg)

**Figure-5.365: Help Menu**

- **5.5.4.6.16 Other Graphical Display Features**.The features provided in graphical display screens are described in following sections.
- **5.5.4.6.16.1 Enlarge Graphical Display**.This feature shall enable the user to enlarge and view the selected graphical displays to the central region of the application window.
- 5.5.4.6.16.1.1 User shall double click on required graphical display, the selected display shall be enlarged and displayed on the central region of RFPS Application window.
  - (a) A Toolbar shall be provided for the enlarged graphical displays which include options like Zoom In, Zoom Out, Undo Zoom, Export and Markers.
  - (b) Based on the user's selection, the corresponding actions shall be performed and displayed in the enlarged graphical display.

SHAKTI : UHB\Ch5 Page 487 of 614

![](_page_491_Figure_1.jpeg)

**Figure-5.366: Enlarge Graphical Display**

- **5.5.4.6.16.2 Resize**.This enables the user to adjust size of the selected graphical with the application window using mouse. This feature is enabled for DAU Raw data, Water fall, Intra pulse, Overlapped, Ensembled, Inter Pulse and Histogram displays. This feature will enable to adjust the **RFPS main application window** depending on the dimensions of the monitor.
- 5.5.4.6.16.2.1 User can place mouse on the edges of the graphical display to be resized, right click, hold till the required size then release.
- **5.5.4.6.16.3 Zoom**.This feature shall enable the user to zoom the required graphical displays by using various zoom options like Zoom In, Zoom Out, Undo Zoom and Zoom Window.
  - (a) If user selects **Zoom In** option from Toolbar, the graphical displays shall be zoomed in steps of 10% increase of the current view.
  - (b) If user selects **Zoom Out** option from Toolbar, the graphical displays shall be zoomed out in steps of 10% decrease of the current view.

SHAKTI : UHB\Ch5 Page 488 of 614

![](_page_492_Figure_1.jpeg)

**Figure-5.367: Zoom In**

SHAKTI : UHB\Ch5 Page 489 of 614

![](_page_493_Figure_1.jpeg)

**Figure-5.368: Zoom Out**

SHAKTI : UHB\Ch5 Page 490 of 614

| (c) | Zoom Window.          | is the default option. In Zoom window, user shall select the                           |
|-----|-----------------------|----------------------------------------------------------------------------------------|
|     |                       | required rectangular area in graphical display. The area selected by the user shall be |
|     | zoomed and displayed. |                                                                                        |

SHAKTI : UHB\Ch5 Page 491 of 614

![](_page_495_Figure_1.jpeg)

**Figure-5.369: Zoom Window**

SHAKTI : UHB\Ch5 Page 492 of 614

![](_page_496_Figure_1.jpeg)

SHAKTI : UHB\Ch5 Page 493 of 614

![](_page_497_Figure_1.jpeg)

**Figure-5.370: Undo Zoom**

SHAKTI : UHB\Ch5 Page 494 of 614

- **5.5.4.6.16.4 Change FG/ BG Color**.This feature shall enable the user to change the foreground and background colors of the graphical Displays.
- 5.5.4.6.16.4.1 If user selects **Foreground Colour** or **Background Colour** option from Toolbar, the following dialog shall appear.

![](_page_498_Picture_3.jpeg)

**Figure-5.371: Colours Dialog**

- (a) **Foreground colour:** User shall select required colour and click on Ok button. The selected colour shall be applied to the graphical displays as foreground colour.
- (b) **Background colour:** User shall select required colour and click on Ok button. The selected colour shall be applied to the graphical displays as background colour.

SHAKTI : UHB\Ch5 Page 495 of 614

![](_page_499_Figure_1.jpeg)

**Figure-5.372: Foreground Colour**

![](_page_499_Figure_3.jpeg)

**Figure-5.373: Background Colour**

SHAKTI : UHB\Ch5 Page 496 of 614

- **5.5.4.6.16.5 Cursor Position Readout**. This feature shall enable the user to view the X, Y values of cursor position on the Graphical Displays.
- 5.5.4.6.16.5.1 Based on the movement of cursor, the readouts for the selected position shall be displayed in the graphical displays.

![](_page_500_Figure_3.jpeg)

**Figure-5.374: Display Cursor Position**

- **5.5.4.6.16.6 Gridlines**.This feature shall enable the user to retain or remove the horizontal and vertical grid lines on the Graphical Displays.
- 5.5.4.6.16.6.1 If user selects **H-Grid** option from Toolbar when horizontal grid lines are displayed in the graphical displays then it shall be hidden; otherwise vice versa.

SHAKTI : UHB\Ch5 Page 497 of 614

![](_page_501_Figure_1.jpeg)

**Figure-5.375: Horizontal Grid lines hidden**

(a) If user selects **V-Grid** option from Toolbar when vertical grid lines are displayed in the graphical displays then it shall be hidden; otherwise vice versa.

SHAKTI : UHB\Ch5 Page 498 of 614

![](_page_502_Figure_1.jpeg)

**Figure-5.376: Vertical Grid Lines Hidden**

SHAKTI : UHB\Ch5 Page 499 of 614

- **5.5.4.6.16.7 Markers**.This feature shall enable the user to position the markers on the Graphical Displays and displays the marker values and marker differences.
- 5.5.4.6.16.7.1 User shall enable the markers by selecting **Markers** option from Toolbar and then choose required position on the Graphical Displays.
- 5.5.4.6.16.7.2 Based on the position selected by the user, marker values (X1, Y1) & (X2, Y2) and marker difference shall be displayed in the respective Edit boxes of graphical plots.

![](_page_503_Figure_4.jpeg)

**Figure-5.377: Markers**

- **5.5.4.6.16.8 Display of Statistical Value**. This feature shall enable the user to compute mean, minimum, maximum and standard deviation of the selected plot area. User shall select the required plot area by positioning the markers in the Graphical display.
- 5.5.4.6.16.8.1 The mean, minimum, maximum and standard deviation values of the selected region shall be computed and displayed in the respective controls.

SHAKTI : UHB\Ch5 Page 500 of 614

![](_page_504_Figure_1.jpeg)

**Figure-5.378: Display of Statistical Values**

#### **5.5.4.7 Operating Instructions – Field Data Loader (FDL):**

**5.5.4.7.1 Description of Field Data Loader**.Shakti Field Data Loader (FDL) system is a laptop based computer system. It is software intensive Human Machine Interface (HMI) system, for the EW user, for performing FDL related operations such as exchange of files with Shakti SCD/ RFPS computer and for performing Shakti SCD 'Offline Mode' functionalities (Replay, Simulation etc). Refer 'Human Machine Interface (HMI) Document Volume 1 - System Controller & Display (SCD)' for SCD related functionalities in FDL. FDL application software shall be loaded and executed on FDL computer. The FDL application shall start automatically on computer system power on.

**5.5.4.7.2 FDL Interface**.Interface diagram between FDL computer and SCD/ RFPS computer is shown in **Figure 1**.

5.5.4.7.2.1 FDL will be connected to SCD/ RFPS through Ethernet switch. FDL computer will be configured with IP address and port number that falls in the sub-net as that of SCD/ RFPS computer. The network connectivity status of between these two computers shall be displayed and updated on FDL GUI. SCD/ RFPS computer shall act as server and FDL computer as client. FDL and SCD/ RFPS applications shall preferably use FTP to communicate/ exchange data.

SHAKTI : UHB\Ch5 Page 501 of 614

- **5.5.4.7.3 FDL Software Functionalities**. The following is a list of main functionalities supported by FDL application software:
  - (a) **Import/ Export of Files from/ to SCD/ RFPS Computer**. Facilitate user to exchange Shakti EW system related files between FDL computer & SCD/ RFPS computer.
  - (b) **Offline Mode Operations of Shakti SCD System**. FDL application software shall support the 'Offline Mode' functionalities of Shakti SCD system such as:
    - (i) **Replay:** Provide 'Replay' facility for replaying previously recorded data files.
    - (ii) **Simulation**: Provide 'Simulation' facility to user to perform EW operations on simulated emitter data.
    - (iii) **Emitter Library Management**: Allow user to create/ modify/ delete emitter library.
    - (iv) **User Management**: Provide facility to create/ modify/ delete user accounts of FDL application.
    - (v) **Application File Management**: To facilitate the user to view or delete unnecessary application related files on FDL storage.
  - (c) **User Authentication**: Authenticate user to perform FDL related EW operations using user name & password.
- **5.5.4.7.4 FDL Hardware Configuration**.Shakti FDL will be a software intensive system. It is a laptop based computer system having the following key specifications/ features:
  - (a) Processor: Intel i7 Based, 2.9 GHz.
  - (b) RAM: 16 GB.
  - (c) Ethernet: 2 No. of Gigabit Ethernet Ports.
  - (d) Audio: High Definition Audio.
  - (e) Graphics & Video: Preferred 1900x1080 resolution graphics card.

#### **5.5.4.7.5 FDL Software Development Environment**.FDL application software shall

SHAKTI : UHB\Ch5 Page 502 of 614

be designed to meet all the requirements of Shakti EW System with the following frame work/ tools:

- (a) Operating System: Red Hat Enterprise Linux (RHEL) version 7.5.
- (b) Development Framework & Programming Languages: Qt 4.8.7 in C++.
- **5.5.4.7.6 FDL HMI**.HMI requirements of Shakti FDL application are categorized into two groups, for ease of understanding and better appreciation, as mentioned below:
  - (a) User Authentication (login) GUIs.
  - (b) FDL Mode GUIs.

GUIs and their HMI requirements are described in the following sections.

- **5.5.4.7.6.1 User Authentication (Login) GUIs**.The underlying operating system, after completion of booting process, shall be configured to start FDL application automatically in full screen mode. Operating System related applications/ tools shall not be visible to user when FDL application is executing. By default, 'Login' GUI shall be displayed immediately after starting FDL application.
- **5.5.4.7.6.1.1 Register Administrator**.If FDL application is executed for the very first time or if there are no user account details present in FDL computer then this GUI (as shown in **Figure-5.379**) shall be displayed to user for creating the first user (administrator) of the application. The Administrator shall be the super user with access to all the functionalities of FDL application.
- 5.5.4.7.6.1.1.1 Refer section '5.5.4.2.4 User Management' section for types of users and their access rights in using FDL application.
- 5.5.4.7.6.1.1.2 The user name shall be maximum of 15 characters and minimum of 5 characters in length. It shall be case sensitive and can be a combination of alpha-numeric characters. Password shall be maximum of 15 characters and minimum of 5 characters in length. It shall be case sensitive and can be a combination of alpha, numeric and special characters.
- 5.5.4.7.6.1.1.3 User shall enter input for 'Username', 'Password' and 'Answer for Security Question' after selecting a security question. Security question will be helpful in recovering a forgotten password. By default, 'User Type' option will be selected as 'Administrator'. User shall click on 'Add Administrator' option to create the user account in FDL application. If successful, 'User Authentication' GUI (described in the flowing section) shall be displayed

SHAKTI : UHB\Ch5 Page 503 of 614

to user to login into FDL application using that account information.

5.5.4.7.6.1.1.4 User shall click on 'Shutdown FDL' option to close this GUI and shutdown (power off) FDL computer (laptop).

![](_page_507_Picture_3.jpeg)

**Figure-5.379: GUI for Registering Administrator**

**5.5.4.7.6.1.2 Authenticate User**.After successful installation of FDL application and creation of 'Administrator' type of user, 'User Authentication' GUI shall be displayed to user for logging into FDL application as shown in **Figure-5.380**. There shall be option on the GUI to recover forgotten password and option to shutdown FDL computer.

![](_page_507_Picture_6.jpeg)

**Figure-5.380: User Authentication GUI**

5.5.4.7.6.1.2.1 User shall enter the 'User Name' & 'Password' (which were entered during user registration) and click on 'Login' option. FDL application shall proceed with next stage of GUIs for carrying out 'FDL Mode' operations if user authentication is successful.

5.5.4.7.6.1.2.2 User shall click on 'Forgot Password' option to recover a forgotten password for previously registered/added user.

5.5.4.7.6.1.2.3 User shall click on 'Shutdown FDL/ Restart FDL' option to close this GUI

SHAKTI : UHB\Ch5 Page 504 of 614

and shutdown (power off)/ restart FDL computer.

- 5.5.4.7.6.1.2.4 User shall click on 'Help' option to see 'User Authentication' GUI related help document.
- **5.5.4.7.6.2 FDL Mode GUIs**. After successful user login Shakti FDL application shall display a GUI as shown in **Figure-5.381**, to perform FDL mode related activities such as:
  - (a) Import/ Export Files between FDL & SCD/ RFPS Computers.
  - (b) Replay.
  - (c) Simulation.
  - (d) Emitter Library Management.
  - (e) User Management.
  - (f) Application File Management.
- 5.5.4.7.6.2.a The options on the GUI, if selected, shall display corresponding GUI for the operations mentioned above. For example, if user clicks on 'Replay' option, 'Replay' GUI shall be displayed. User shall click on 'Logout' option to exit from this GUI and go to 'User Authentication' GUI for logging again.
- 5.5.4.7.6.2.b User shall click on 'Help' option to see FDL mode GUI related help document.

SHAKTI : UHB\Ch5 Page 505 of 614

![](_page_509_Picture_1.jpeg)

**Figure-5.381: FDL Mode GUI**

SHAKTI : UHB\Ch5 Page 506 of 614

**5.5.4.7.6.2.1 Import/Export Files between FDL & SCD Computer**.A GUI, as shown in **Figure-5.382**, for importing/ exporting files between FDL & SCD computers shall be displayed to user.

5.5.4.7.6.2.1.a User shall click on 'Import/ Export Files' option in 'FDL Mode' GUI to active this GUI. User shall ensure that FDL computer is connected to SCD computer over Shakti LAN.

5.5.4.7.6.2.1.b 'File Transfer' GUI shall contain two tab controls with file transfer options for FDL-SCD computer & FDL-RFPS computer.

SHAKTI : UHB\Ch5 Page 507 of 614

![](_page_511_Figure_1.jpeg)

**Figure-5.382: GUI for Import/ Export of FDL & SCD Files.**

SHAKTI : UHB\Ch5 Page 508 of 614

- **5.5.4.7.6.2.1.1 File Transfer between SCD & FDL Computer**. User shall select 'File Transfer between FDL & SCD' option (by default it will be selected). FDL Login & File Access:
  - (a) User shall enter 'User Name of FDL Computer', 'Password of FDL Computer' and click on 'FDL Login' option on GUI to access files on FDL computer. If login is successful, user name & password fields shall be disabled and 'FDL Login' option shall be changed to 'FDL Logout'.
  - (b) User shall select 'FDL Data Source' (FDL Storage) on FDL GUI. Click on 'Show FDL Files' option.
  - (c) A folder selection GUI, as shown in **Figure-5.383**, will be popped up and user shall click on 'OK' option after selecting a folder. Folders/files will be listed on the GUI.
  - (d) Error message shall be displayed to user if invalid login credentials are entered.

![](_page_512_Picture_6.jpeg)

**Figure-5.383: File/ Folder Selection GUI (FDL-SCD) – FDL Application**

## **5.5.4.7.6.2.1.2 SCD Login & File Access**.

(a) User shall enter 'User Name of SCD Computer', 'Password of SCD Computer', 'IP Address of SCD Computer' and click on 'SCD Login' option on GUI to access files on SCD computer. If login is successful, user name & password fields shall be disabled and 'SCD Login' option shall be changed to 'SCD Logout'.

SHAKTI : UHB\Ch5 Page 509 of 614

- (b) User shall click on 'Show SCD Files' option on SCD GUI. A folder selection GUI, as shown in **Figure-5.384**, will be popped up and click on 'OK' option after selecting a folder. Folders/files will be listed on the GUI.
- (c) Error message shall be displayed to user if invalid login credentials or IP address are entered.

## **5.5.4.7.6.2.1.3 File Transfer**.

- (a) User has to select a file on 'FDL Computer' GUI and click on 'Copy from FDL to SCD' option to transfer selected file from FDL computer to SCD computer.
- (b) User shall click on 'Copy All from FDL to SCD' option on 'FDL Computer' GUI to copy all the listed files from FDL computer to SCD computer.
- (c) User shall click on 'Refresh' option to relist the files on 'FDL Computer' GUI, click on 'FDL Home' option to go to home folder of FDL computer.
- (d) User has to select a file on 'SCD Computer' GUI and click on 'Copy from SCD to FDL' option to transfer selected file from SCD computer to FDL computer.
- (e) User shall click on 'Copy All from SCD to FDL' option on 'SCD Computer' GUI to copy all the listed files from SCD computer to FDL computer.
- (f) User shall click on 'Refresh' option to relist the files on 'SCD Computer' GUI, click on 'SCD Home' option to go to home folder of SCD computer.
- 5.5.4.7.6.2.1.3.1 Status of network connectivity and file transfer between FDL computer & SCD computer shall be displayed on the GUI.
- 5.5.4.7.6.2.1.3.2 User shall click on 'close' option to close file transfer GUI and go to 'FDL Mode' GUI. Note: exiting from file transfer GUI, will disconnect network connection between FDL & SCD computers and user has to login again for file transfer.

#### **5.5.4.7.6.2.2 Import/Export Files between FDL & RFPS***.*

5.5.4.7.6.2.2.a A GUI, as shown in **Figure-5.385**, for importing/ exporting files between FDL & RFPS computers shall be displayed to user.

5.5.4.7.6.2.2.b User shall click on 'Import/ Export Files' option in 'FDL Mode' GUI to active this GUI. User shall ensure that FDL computer is connected to RFPS computer over Shakti LAN.

SHAKTI : UHB\Ch5 Page 510 of 614

![](_page_514_Figure_1.jpeg)

**Figure-5.384: GUI for Import/ Export of FDL & RFPS Files – FDL Application**

SHAKTI : UHB\Ch5 Page 511 of 614

5.5.4.7.6.2.2.c A warning message, as shown in **Figure-5.385**, shall be displayed to user if FDL application is not executed with 'root' (Administrator in RHEL OS) user permissions. User shall execute FDL application with 'root' permissions to access portable media (CD/ DVD/ Pen Drive) for file transfer.

![](_page_515_Picture_2.jpeg)

**Figure-5.385: Portable Media Warning Message**

5.5.4.7.6.2.2.d 'File Transfer' GUI shall contain two tab controls with file transfer options for FDL-SCD computer & FDL-RFPS computer.

**5.5.4.7.6.2.2.1 File Transfer between FDL & RFPS Computer**.User shall select 'File Transfer between FDL & RFPS' option (by default it will not be selected).

**5.5.4.7.6.2.2.2 FDL Login & File Access**.User shall enter 'User Name of FDL Computer', 'Password of FDL Computer' and click on 'FDL Login' option on GUI to access files on FDL computer. If login is successful, user name & password fields shall be disabled and 'FDL Login' option shall be changed to 'FDL Logout'. Error message shall be displayed to user if invalid login credentials are entered.

#### **5.5.4.7.6.2.2.3 SCD Login & File Access**.

- (a) User shall enter 'User Name of RFPS Computer', 'Password of RFPS Computer', 'IP Address of RFPS Computer' and click on 'RFPS Login' option on GUI to access files on RFPS computer. If login is successful, user name & password fields shall be disabled and 'RFPS Login' option shall be changed to 'RFPS Logout'.
- (b) User shall click on 'Show RFPS Files' option on RFPS GUI. A folder selection GUI will be popped up and click on 'OK' option after selecting a folder. Folders/files will be listed on the GUI.
- (c) Error message shall be displayed to user if invalid login credentials or IP address are entered.

#### **5.5.4.7.6.2.2.4 File Transfer**.

(a) User has to select a file on 'FDL Computer' GUI and click on 'Copy from FDL

SHAKTI : UHB\Ch5 Page 512 of 614

to RFPS' option to transfer selected file from FDL computer to RFPS computer.

- (b) User shall click on 'Copy All from FDL to RFPS' option on 'FDL Computer' GUI to copy all the listed files from FDL computer to RFPS computer.
- (c) User shall click on 'Refresh' option to relist the files on 'FDL Computer' GUI, click on 'FDL Home' option to go to home folder of FDL computer.
- (d) User has to select a file on 'RFPS Computer' GUI and click on 'Copy from RFPS to FDL' option to transfer selected file from RFPS computer to FDL computer.
- (e) User shall click on 'Copy All from RFPS to FDL' option on 'RFPS Computer' GUI to copy all the listed files from RFPS computer to FDL computer.
- (f) User shall click on 'Refresh' option to relist the files on 'RFPS Computer' GUI, click on 'RFPS Home' option to go to home folder of RFPS computer.
- 5.5.4.7.6.2.2.4.1 Status of network connectivity and file transfer between FDL computer &RFPS computer shall be displayed on the GUI.
- 5.5.4.7.6.2.2.4.2 User shall click on 'close' option to close file transfer GUI and go to 'FDL Mode' GUI. Note: exiting from file transfer GUI, will disconnect network connection between FDL &RFPS computers and user has to login again for file transfer.
- **5.5.4.7.6.2.3 Replay in FDL Application**.Replay operations in FDL application are similar to that of SCD application. Refer section '5.5.4.2.1 Replay' details.
- **5.5.4.7.6.2.4 Simulation in FDL Application**.Simulation operations in FDL application are similar to that of SCD application. Refer section '5.5.4.2.2 Simulation' details.
- **5.5.4.7.6.2.5 Emitter Library Management in FDL Application**.'Emitter Library Management' related operations in FDL application are similar to that of SCD application. Refer section '5.5.4.2.3 Emitter Library Management' details.
- **5.5.4.7.6.2.6 User Management in FDL Application**.'User Management' related operations in FDL application are similar to that of SCD application. Refer section '5.5.4.2.4 User Management' details.
- **5.5.4.7.6.2.7 File Management in FDL Application**.'File Management' related operations in FDL application are similar to that of SCD application. Refer section '5.5.4.2.6 details.

SHAKTI : UHB\Ch5 Page 513 of 614

## **5.6 Notes**.

- **5.6.1 List of Short Cut Keys for SCD**. The following is a list of short cut keys to be used in SCD Main Window of SCD application.
  - (a) Important Short Cut Keys in SCD Main Window.

**Table-5.21: Short Cut Keys in SCD Main Window**

|          | Shortcut Operation/ Description                         |
|----------|---------------------------------------------------------|
| F1       | Show Online Mode Help Document of SCD Application.      |
| F2       | Purge Passive Tracks at ES Processor.                   |
| F3       | Rebuild ALL Tracks at ES Processor.                     |
| F4       | Reset ALL Receivers.                                    |
| F5       | Reset ES Processor.                                     |
| F6       | Show Auto BITE Status.                                  |
| F7       | Reset EA Processor.                                     |
| F8       | Perform Radar Finger Print.                             |
| F9       | Take a Screen Shot of a GUI.                            |
| F10      | Freeze & Hold Emitter Report Window                     |
| F11      | Add Track to Temporary Emitter Library.                 |
| F12      | Show Alarming Tracks.                                   |
| Ctrl + A | Auto Purge ON/ OFF at ES Processor.                     |
| Ctrl + B | Auto Merge Agile Tracks at ES Processor.                |
| Ctrl + C | Auto Merge Mid-Band (2.2-18GHz) Tracks at ES Processor. |
| Ctrl + D | DOA Trace.                                              |
| Ctrl + E | Add Track to ELINT Returns                              |
| Ctrl + F | Enable/ Disable Display Filters.                        |
| Ctrl + G | System Recording ON/ OFF.                               |
| Ctrl + H | Hide HookUp Emitters Window.                            |
| Ctrl + I | Set Lockout Sectors at ES Processor.                    |

SHAKTI : UHB\Ch5 Page 514 of 614

|          | Shortcut Operation/ Description                                |  |  |  |
|----------|----------------------------------------------------------------|--|--|--|
| Ctrl + J | Track & Jam in Semi-Auto Mode with Default JPRO Technique.     |  |  |  |
| Ctrl + K | Break Track All Emitters Currently being Handled by EA System. |  |  |  |
| Ctrl + L | Show Link Status.                                              |  |  |  |
| Ctrl + M | Track &Jam Manual Mode with Default JPRO Technique.            |  |  |  |
| Ctrl + N | Track In Manual Mode.                                          |  |  |  |
| Ctrl + O | List of Shortcut Keys in Online Mode.                          |  |  |  |
| Ctrl + P | Jam All Emitters Currently being Tracked by EA System.         |  |  |  |
| Ctrl + Q | Logout from Online Mode.                                       |  |  |  |
| Ctrl + R | Toggle Status Display of Receiver 'Duty<br>Cycle &Mode'.       |  |  |  |
| Ctrl + S | Stop Jam All Emitters Currently being Jammed by EA System.     |  |  |  |
| Ctrl + T | Track in Semi Auto Mode with Default JPRO Technique.           |  |  |  |
| Ctrl + U | Show Hook<br>up Emitters Window.                               |  |  |  |
| Ctrl + W | Emitters Watch Window.                                         |  |  |  |
| Ctrl + X | Go to Offline Mode from Online Mode.                           |  |  |  |
| Ctrl + Y | Toggle Display to 'True/ Relative' Mode.                       |  |  |  |
| Ctrl + Z | Apply Zoom in Tactical Display w.r.t. Sector.                  |  |  |  |

SHAKTI : UHB\Ch5 Page 515 of 614

![](_page_519_Picture_0.jpeg)

**This Page is Intentionally Kept Blank.**

SHAKTI : UHB\Ch5 Page 516 of 614

# **CHAPTER VI USER'S / OPERATOR'S SERVICING AND MAINTENANCE INSTRUCTIONS**

#### **CHAPTER – VI**

## **USER'S OPERATOR'S SERVICING AND MAINTENANCE INSTRUCTIONS**

- **6.1 Introduction**. This chapter describes the maintenance procedures for Shakti (UET) system. A regular maintenance schedule will help to avoid expensive repairs and contribute to trouble free, reliable operation of the system with minimum of maintenance expenditure and work. Work on the unit must only be carried out with isolation of electric supply. The equipment is in a good state of preservation, when the equipment is clean, free from corrosion and damage. The general maintenance routines should be carried out periodically and strictly adhered to avoid costly failures. The following maintenance procedures are categorized by the periodic interval at which they need to be performed.
  - (a) Preventive Maintenance.
  - (b) Corrective Maintenance Fault Finding and Rectification.
- **6.1.1 Preventive Maintenance**. Preventive maintenance is systematic care, servicing and inspection of the equipment to prevent the occurrence of trouble, to reduce downtime and check that the system is always serviceable. The degradation / possibility of occurrence of faults in the system are detected by going through appropriate routine system checks. Some of these checks may require specific instruments for making test setups.
- **6.1.1.1 Preventive Maintenance Steps**.The Preventive Maintenance includes:
  - (a) Inspection and checking.
  - (b) Adjustment.
  - (c) Cleaning.
  - (d) Preservation.
  - (e) Sealing.
  - (f) Keep Alive Procedure
  - (g) BITE Checks.
- **6.1.1.1.1 Inspection & Checking**.This procedure consists of the following steps.
  - (a) Inspect the equipment for dust, dirt and corrosion. Check that all parts are well secured.
  - (b) Check all parts for any damage.

SHAKTI : UHB\Ch6 Page 517 of 614

- **6.1.1.1.2 Adjustment**.Electrical or mechanical adjustments normally follow the checking of adjustable items to return the part or assembly to within its correct operational limits.
- **6.1.1.1.3 Cleaning**.Consists of keeping the entire installation free from dust, dirt or corrosion.
- **6.1.1.1.4 Preservation**.The preservation state of the equipment must be carefully and regularly checked. The frequency of the checks depends on the usage or storage condition.
- **6.1.1.1.5 Sealing**.Sealing is intended to avoid:
  - (a) Penetration of moisture in to the equipment.
  - (b) Crevice corrosion or frost damage due to moisture in seams, splits and fissures, leakage lubricant etc.
  - (c) The area around antenna should be checked to avoid water penetration.
- **6.1.1.1.6 Keep Alive Procedure**.The UPS should be initially charged fully for 24 hours, thereafter if it is not used, it is advised to start the ups and the system for 15 minutes every week. For Detail procedures

Refer Maintenance Manual Chapter no I Para no 1.2.1.8.

- (a) Servos systems: Both the servos to be switched ON once in a week. Need to wait for the full BIT check. After becoming standby state Servos can be switched OFF.
- (b) MPM: TX MB2 Jammer needs to be power ON at least once in month. Initially power ON the TX MB2 Unit and wait for the heater ON (3 min) and apply HV ON. Then proceed for barrage jamming for 1 min.
- (c) TWT: TX HB Jammer needs to be power ON at least once in month. Initially power ON the TX HB Unit and wait for the heater ON (3 min) and apply HV ON. Then proceed for barrage jamming for 1 min.
- **6.1.1.1.7 BITE Checks**.Power on BITE for ES is performed initially when the display software is started.
- **6.1.1.1.8 Maintenance Mode**. When this mode is initiated, the system executes a detailed BITE of each of the groups, giving a numbered maintenance message. The

SHAKTI : UHB\Ch6 Page 518 of 614

operator also can initiate Manual BITE for both ES & EA, in order to check the health of the system at group level as well as at module level.

- **6.2 Unit Servicing Log and Maintenance Task**. The following scheme is proposed for maintenance of the system for this class of ships.
- **6.2.1 Level-1 Maintenance**.This level of maintenance includes daily routines, weekly routines, monthly routines, quarterly routines, half yearly routines and yearly routines. This level checks can be carried out on board itself. The operator runs the BITE (either auto BITE or maintenance BITE or both) and observes the status of the system and rectifies the problem on board itself using onboard spares. The defective PCB / subsystem / component should be given to shop floor for repair. For details refer Maintenance Manual Chapter no I Para no 1.2.1.9.
- 6.2.1.1 The following are details of this maintenance.

#### (a) **Daily Routines**:

- (i) Switch on the system in normal mode of operation and check that system health status is OK on monitor.
- (ii) Observe the link status on the monitor between the processors of both ES and EA are OK.
- (iii) Observe that the emitters are received and check that the Parameters measured are satisfactory by approximation. (Rough idea).
- (iv) Check the system health by BITE operation at regular intervals (at a period of 2 or 3 hours).

#### (b) **Weekly Routines**:

- (i) Check the tightness of EW cable connectors and check that connectors are physically OK.
- (ii) Check the EW cables physically and check that there is no damage on the cables.
- (iii) Perform maintenance BITE operation and check that the system / subsystem / PCB health status is OK.
- (iv) Stagnated rain water on connectors of exposed units to be cleaned.
- (v) Perform maintenance procedure for the following Units.
  - (aa) Servo System: Perform BIT checks for 1-axis and 2-axis SDAs.

SHAKTI : UHB\Ch6 Page 519 of 614

- (ab) HEU: Verify Water level should be 70%(min) and perform the BITE check.
- (ac) Tx (MB2) and Tx (HB) Units: Cooling pipes leakage to be verified. Switch ON the system and keep standby for 30 minutes and keep HV ON for 10 minutes.

## (c) **Monthly Routines**:

- (i) Clean all the radomes with clean cotton and with mild soap water to check good reception.
- (ii) Remove all the EW cable connectors and verify the connector pins are intact. Clean the connector pins with brush and alcohol.
- (iii) Check the power supply voltages at the EW connector ends as per wire lists for each unit.
- (iv) Restore back the connectors and perform weekly routines.
- (v) Perform maintenance procedure for the following Units.
  - (aa) Servo System: Emergency Button functionality checks.

Press the Emergency button and check MAINTENANCE mode is indicated on SCU Display in EA Rack 2. Release the Emergency button and check AUTO Mode is indicated on SCU Display.

(ab) HEU: Flow sensors and temperature sensors functionality checks to be carried out. Refer Maintenance Manual TM Part II, Table 1.10.

#### (d) **Half yearly Routines**:

- (i) Check the DC offset voltages for each front-end receiver channel and check that the DC offset voltage is within the specified limits.
- (ii) Check the RF and Video Tangential Signal Sensitivity (TSS) at AHU outputs in normal mode by feeding the RF signals at AHU.
- (iii) Check the radomes physically and check that there is no damage on the radomes.
- (iv) Perform maintenance procedure for the following Units.
  - (aa) Tx (MB2) and Tx (HB) Units: Switch ON the system and perform the re-activation procedure. Refer Maintenance Manual TM Part II, Table 1.12.

SHAKTI : UHB\Ch6 Page 520 of 614

### (e) **Yearly Routines**:

- (i) Remove the radomes, clean and keep safely.
- (ii) Remove all the connector both EW cable connectors and within rack connectors and check that the pins are intact.
- (iii) Check the EW cable wiring for both normal and coaxial wires and check that the continuities are OK.
- (iv) Check the wiring for rack connectors and check that they are OK.
- (v) Clean all RF connectors with alcohol and check that there are no damages on the connectors.
- (vi) Open the AHU back covers and observe all the semi-rigid cables are physically OK and check that they are tightened properly using torque wrench.
- (vii) Remove all the connectors and connect back and tight the connectors properly.
- (viii) Remove the PCBs from the drawers and observe physically and check that they are OK.
- (ix) Insert all the PCBs and check that they are properly aligned in the slots.
- (x) Replace the gaskets with new set and apply grease before closing the unit covers wherever applicable.
- (xi) Reassemble all the drawers and check the proper insertion of drawers into the cabinets.
- (xii) Check that the grounding is proper for all the units.

#### (f) **Two Yearly Routines**:

Refer to Overhaul and Reconditioning Instructions Technical Manual Part III.

- **6.2.2 Level - 2 Maintenance**.This level of maintenance includes the repair of the PCBs, replacement of components and subassemblies in the shop floor. These PCB / Components / subassemblies are completely checked as per the procedures. For this maintenance, test equipment and test jigs are required at naval dockyard.
- **6.2.3 Level - 3 Maintenance**. OEM is involved in carrying out this level of maintenance along with ship staff. This includes complete checking of the system including testing and tuning, sensitivity checks, parameter accuracy checks; verification

SHAKTI : UHB\Ch6 Page 521 of 614

of trial results etc., Some of the units and the systems are required to be brought back to factory for repair.

- **6.2.4 Spares Requirement**.The onboard (OB) spares are to be used for repair in level 2 or level 3 maintenance logging of maintenance record. The details of failures both electrical and mechanical should be noted and maintained for future references up to minute level in a log-book. These are useful for ascertaining the reliability and maintainability of the system. The copy of these details is to be forwarded to OEM.
- **6.2.5 Radiation Hazards Precautions**. Avoid standing near vicinity of transmitter radiation during jamming operation.
- **6.2.6 Special Instructions**.There are no special instructions required for exploiting the SHAKTI system.
- **6.3 Fault Diagnosis**.The possible faults in SHAKTI EW system is provided in the following **Table-6.1**.

**Table-6.1: Possible Faults in Shakti System**

| Ser. | Faults                   | Possible Cause                                      | Corrective action                                                                                                                                                                      |
|------|--------------------------|-----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|      |                          | System Controller<br>and Display                    |                                                                                                                                                                                        |
| 1    | SCD to ESMP link<br>DOWN | ESM processor May be<br>OFF                         | Check at ES Rack level , if<br>ESMP is ON or not<br>Ping<br>192.168.4.2<br>and<br>192.168.5.2.                                                                                         |
|      |                          | LAN Cable may not be<br>connected properly          | Check LAN Cable EW-28,<br>direct<br>link<br>from<br>SCD<br>to<br>ESMP at ES Rack-1.<br>Check LAN Cable EW-39,<br>Ethernet link from SCD to<br>ESMP<br>through<br>Ethernet<br>Switch-2. |
|      |                          | IP configured file may<br>be missing.               | Check<br>IP<br>config<br>file,<br>if<br>missing reload                                                                                                                                 |
|      |                          | SBCs<br>not<br>booting<br>Board<br>may<br>not<br>be | Check<br>that SBC is inserted<br>properly and giving correct                                                                                                                           |

SHAKTI : UHB\Ch6 Page 522 of 614

| Ser. | Faults                                               | Possible Cause                                                   | Corrective action                                                                                                |
|------|------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
|      |                                                      | inserted properly/Faulty                                         | Status LED indications.<br>If still not working Replace<br>SBC board.                                            |
|      |                                                      | ESM<br>processor<br>may<br>not be working.                       | Check at ESMP processor<br>follow ESMP fault diagnosis<br>procedure.                                             |
| 2    | No mains Indication<br>on Console.                   | Rack<br>MCB<br>might<br>be<br>OFF                                | Check MCB position of Rack<br>and the status on front panel                                                      |
|      | SCD<br>Processor/<br>LRU Power on LED<br>not glowing | Power<br>on<br>toggle<br>switches might be in off<br>position.   | Keep<br>it<br>in<br>ON<br>position.<br>(Switches are separate for<br>RFPS<br>and<br>SCD<br>on<br>front<br>Panel. |
|      |                                                      | Input power supply may<br>not be available                       | Check input power supply at<br>connector P301 (Between A<br>B pins)                                              |
|      |                                                      | Power ON LED may be<br>faulty                                    | Replace LED                                                                                                      |
|      |                                                      | PDIU<br>may<br>not<br>be<br>working                              | Troubleshoot<br>PDIU<br>unit<br>because AC supply routes<br>through it                                           |
| 3    | Blowers not working                                  | Supply not reaching to<br>blowers                                | Check if MCB /Toggle switch<br>are<br>ON<br>and<br>supply<br>is<br>reaching to blowers                           |
|      |                                                      | Blowers might be faulty                                          | Replace the blowers.                                                                                             |
| 4    | Display Not coming/<br>Blur                          | DVI cable may not be<br>working                                  | Replace the DVI cable                                                                                            |
|      |                                                      | Monitor<br>Resolution<br>settings<br>may<br>not<br>be<br>correct | Change<br>the<br>Resolution,<br>Make the correct resolutions<br>settings at OSD menu                             |
|      |                                                      | Monitor Might be faulty.                                         | Replace the Monitor                                                                                              |
|      |                                                      | External System Interface Unit (Esi)                             |                                                                                                                  |
| 1    | ESI to SCD Ethernet                                  | ESI may be faulty                                                | Carry<br>out<br>pinging<br>checks                                                                                |

SHAKTI : UHB\Ch6 Page 523 of 614

| Ser. | Faults                                                                         | Possible Cause                         | Corrective action                                                                                                                                                                            |  |  |
|------|--------------------------------------------------------------------------------|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|      | Link is Down                                                                   |                                        | 192.168.5.40. If<br>pinging<br>is<br>not ok from Ethernet Switch<br>1 replace the ESI.                                                                                                       |  |  |
|      |                                                                                | SCD<br>SBC<br>may<br>be<br>faulty      | Carry<br>out<br>pinging<br>checks<br>192.168.5.40. If pinging is ok<br>from Ethernet Switch-1 but<br>pinging is not coming from<br>SCD terminal then replace<br>SCD SBC.                     |  |  |
| 2    | GYRO<br>NO<br>DATA/NO<br>GPS<br>DATA in SCD.                                   | SDN may be faulty                      | Pinging<br>SDN<br>IP<br>address<br>(192.168.2.25) from Ethernet<br>Switch-4 using laptop may<br>not be ok. Then debug SDN<br>side.                                                           |  |  |
|      |                                                                                | ESI may be faulty                      | Pinging<br>ESI<br>IP<br>address<br>(192.168.2.45) from Ethernet<br>Switch-4 using laptop may<br>not be ok. Then replace ESI.                                                                 |  |  |
| 3    | Heading<br>is<br>not<br>coming but roll and<br>pitch data is coming<br>in SCD. | ESMP to SCD link may<br>be down        | Check<br>ESMP<br>to<br>SCD<br>Ethernet connections.                                                                                                                                          |  |  |
| 4    | Radar<br>Blanking is                                                           | Radar PRE SYNC may<br>be problem       | Radar PRE SYNC pulse is<br>not available at input of ESI.                                                                                                                                    |  |  |
|      | not taking<br>place at ESI output                                              | ESI may be faulty.                     | Pre-Sync<br>available<br>at<br>the<br>input<br>of<br>ESI<br>but<br>blanking<br>pulses are not observed at<br>corresponding pins of J3 and<br>J4 connectors then replace<br>ESI. Replace ESI. |  |  |
|      | 0.175-500MHz Narrow Band Chain                                                 |                                        |                                                                                                                                                                                              |  |  |
| 1    | Ethernet Link Down<br>No<br>Track<br>and<br>No<br>PD count                     | Power Supply (AHU1-<br>LB1) in ES RK-2 | Check PSU i/p A.C voltage<br>and DC Outputs.<br>Check A.C. Supply to Rx                                                                                                                      |  |  |

SHAKTI : UHB\Ch6 Page 524 of 614

| Ser. | Faults                                | Possible Cause                                                                           | Corrective action                                                                                                              |
|------|---------------------------------------|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
|      |                                       |                                                                                          | Processor (LB1)                                                                                                                |
| 2    | Ethernet Link is not<br>OK            | Receiver<br>processor<br>(LB1)<br>LRU<br>Rx<br>and<br>Amp<br>Card<br>may<br>be<br>faulty | Carry out pinging checks<br>192.168.5.9 (Rx and AMP )<br>If not OK replace Card                                                |
|      |                                       | Receiver<br>processor<br>(LB1) LRU PPD card<br>may be faulty                             | Carry out pinging checks<br>192.168.5.93 (PPD V5)<br>192.168.5.114 (PPD MPC)<br>If<br>no<br>ping<br>happens<br>replace<br>card |
| 3    | No<br>Track<br>and<br>PDcount OK      | Antenna Switching Unit<br>may be faulty                                                  | Initiate BITE command and<br>check<br>Antenna<br>Switching<br>Unit RF outputs. If not OK<br>Replace ASU                        |
|      |                                       | Multi Channel RF Unit                                                                    | Check IF output of MCRFU.<br>If not OK replace MCRFU                                                                           |
| 4    | No<br>Track<br>and<br>No<br>PD counts | ES RK2 Rx processor<br>(LB1) J8 input cable                                              | Check<br>blanking<br>signal<br>is<br>Low.<br>If<br>blanking<br>is<br>High,<br>Check Blanking input at ESI<br>Unit.             |
|      |                                       | Antenna Switching Unit<br>may be faulty                                                  | Initiate BITE command and<br>check<br>Antenna<br>Switching<br>Unit RF outputs. If not OK<br>Replace ASU                        |
| 5    | No<br>Maintenance<br>BITE<br>Track    | Antenna Switching Unit<br>may be faulty                                                  | Initiate BITE command and<br>check<br>Antenna<br>Switching<br>Unit RF outputs. If not OK<br>Replace ASU                        |
|      |                                       | Multichannel RF Unit                                                                     | Check IF output of MCRFU.<br>If not OK replace MCRFU                                                                           |
|      |                                       | Receiver processor<br>(LB1)LRU                                                           | Check<br>IF input cables to the<br>LRU are intact                                                                              |
| 6    | DF error in track                     | Antenna                                                                                  | Switching Unit Initiate BITE command and                                                                                       |

SHAKTI : UHB\Ch6 Page 525 of 614

| Ser. | Faults                                                 | Possible Cause                         | Corrective action                                                                                                                                                               |
|------|--------------------------------------------------------|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|      |                                                        | may be faulty                          | check<br>Antenna<br>Switching<br>Unit RF outputs. If not OK<br>Replace ASU                                                                                                      |
|      |                                                        | Multi Channel RF Unit                  | Check IF output of MCRFU.<br>If not OK replace MCRFU                                                                                                                            |
|      |                                                        | Receiver<br>processor<br>(LB1) LRU     | Check<br>IF input cables are<br>intact                                                                                                                                          |
|      | 2.2-18GHz Broadband Chain                              |                                        |                                                                                                                                                                                 |
| 1    | No Track on Display,<br>No<br>PD<br>Count<br>Available | FO LINK may be faulty                  | May be failure in FO Link.<br>Check LED D5 on PPD-2 . If<br>LED is not glowing fix FO<br>cable properly.                                                                        |
| 2    | Manual BITE<br>is not<br>OK                            | DTO in AHU-4 may be<br>faulty.         | Check<br>whether<br>2-18<br>GHz<br>DTO in AHU-4 is OK or NOT<br>OK.                                                                                                             |
| 3    | NO<br>DF<br>data<br>or<br>wrong DF Data                | Homodyne Rx may be<br>faulty           | Phase calibration to be done<br>for<br>the<br>corresponding<br>Quadrant<br>Homodyne<br>Rx.<br>Refer to TM Part-II, Ch3 for<br>the procedure.                                    |
| 4    | Frequency errors                                       | Homodyne<br>Receiver<br>may be faulty. | Frequency calibration to be<br>done for the corresponding<br>Quadrant<br>Homodyne<br>Rx.<br>Refer to TM Part-II , Ch3 for<br>the procedure.                                     |
| 5    | Power supply failure                                   | Any module in LVPS-1<br>may be faulty. | Observe the LEDS PS1 to<br>PS4 and PS11 on the LVPS<br>1. If any LED is not glowing<br>the<br>corresponding<br>output<br>voltage is NOT OK. Replace<br>the power supply module. |
|      | 0.5-18GHz Narrow band Chain                            |                                        |                                                                                                                                                                                 |

SHAKTI : UHB\Ch6 Page 526 of 614

| Ser. | Faults                                                  | Possible Cause                                                    | Corrective action                                                                                                                                                                 |
|------|---------------------------------------------------------|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1    | No Track on Display,<br>No<br>PD<br>Count<br>Available. | Controls<br>to<br>Receiver<br>may be faulty.                      | Check<br>that LEDs D1, D2, D3<br>and 'C' (CLK) on all QDRs<br>are<br>glowing.<br>Otherwise<br>Replace QDR.<br>Check<br>that<br>Pin '69' of J1 on ES Rack-1<br>is High.            |
| 2    | No Track on Display,<br>but<br>PD<br>Count<br>Available | Connection<br>between<br>RIB and ESMP may be<br>faulty.           | Verify<br>the<br>Connection<br>between<br>RIB<br>and<br>ESMP.<br>Check<br>LED D5 on PPD-2 is<br>glowing.                                                                          |
| 3    | Ethernet Link is not<br>OK                              | Processor<br>Boards<br>(ESMP-PPD3<br>or<br>RIB)<br>may be faulty. | Ping 192.168.5.90 (ESMP –<br>PPD3), 192.168.5.4 (RIB).If<br>any<br>IP<br>address<br>is<br>not<br>pinging, Replace the module.                                                     |
| 4    | Manual BITE<br>Track<br>not displayed                   | DTOs in AHU-4 may be<br>Faulty.                                   | Check whether o/p of 2-18<br>GHz<br>DTO<br>and<br>0.5-2GHz<br>DTO in AHU-4 are OK or<br>NOT OK.                                                                                   |
| 5    | No<br>DF<br>data<br>/DF<br>Errors                       | QDR may be faulty.                                                | Reload Phase Data in QDR.<br>If<br>Still<br>problem<br>exists,<br>Replace QDR.                                                                                                    |
| 6    | Frequency errors                                        | Synthesizer in BB and<br>NB RX AHU may be<br>faulty.              | Check<br>that LO i/p at QSHR<br>is<br>correct.<br>If<br>any problem<br>found, Replace Synthesizer.                                                                                |
| 7    | Power supply failure                                    | Any module in LVPS-1<br>may be faulty.                            | Observe the LEDS PS5 to<br>PS11on LVPS-1. If any LED<br>is<br>not<br>glowing<br>the<br>corresponding output voltage<br>is<br>NOT<br>OK.<br>Replace<br>the<br>power supply module. |
|      | 18-40GHz High band Chain                                |                                                                   |                                                                                                                                                                                   |

SHAKTI : UHB\Ch6 Page 527 of 614

| Ser. | Faults                                                                                       | Possible Cause                                                                          | Corrective action                                                                                                                                                                                                                                        |  |
|------|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| 1    | NO track on Display<br>and<br>No<br>PD<br>count<br>available                                 | No RF available at the<br>input of DIFM                                                 | Verify DIFM input frequency<br>on spectrum analyzer and if<br>not available, check the I/P<br>RF at J13 and<br>J14 ports of<br>AHU-4                                                                                                                     |  |
| 2    | No track on Display<br>but<br>PD<br>count<br>present                                         | One of the videos may<br>not be available from<br>AHU-3<br>(I/P<br>of<br>TDOA<br>board) | Verify<br>videos<br>(CH1,<br>CH2,<br>CH3 and<br>CH4) at input of<br>TDOA board on Oscilloscope                                                                                                                                                           |  |
| 3    | No Ethernet Link on<br>Display                                                               | Processor<br>Boards<br>(ESMP-PPD2 or RPB)<br>may be faulty.                             | Ping 192.168.5.91 (ESMP –<br>PPD2),<br>192.168.5.10<br>(RPB).If any IP address is<br>not<br>pinging,<br>Replace<br>the<br>module.                                                                                                                        |  |
| 4    | No<br>FO<br>Link<br>on<br>Display                                                            | There may be an issue<br>in<br>the<br>FO<br>link<br>connectivity                        | Check FO cable connectivity<br>to RPB board (all the 4 ports<br>A1, B1 & A2, B2)                                                                                                                                                                         |  |
| 5    | No BITE Track on<br>Display                                                                  | Type-III<br>BITE<br>unit<br>output<br>may<br>not<br>be<br>available                     | Monitor Type-3 BITE source<br>output RF (24 & 36 GHz) at<br>output<br>port<br>of<br>AHU4<br>on<br>spectrum analyzer based on<br>the<br>sector<br>selection<br>from<br>SCD (J16, J18 & J22 for 45°,<br>225° and<br>J16, J20 and<br>J24<br>for 135°, 315°) |  |
| 6    | Track<br>is<br>available<br>with<br>wrong<br>Band<br>code<br>(18-29<br>GHz<br>and 29-40 GHz) | RF cable Connectivity<br>issue<br>between<br>Omni<br>MASS<br>and<br>Omni<br>Receivers   | Verify<br>the<br>RF<br>cable<br>connectivity<br>between<br>Omni<br>Receiver<br>and<br>Omni MASS<br>From<br>To<br>Omni Rx1/J3<br>Omni<br>MASS/J7<br>Omni Rx1/J4<br>Omni<br>MASS/J8<br>Omni Rx2/J3<br>Omni                                                 |  |

SHAKTI : UHB\Ch6 Page 528 of 614

| Ser. | Faults                                                | Possible Cause                                                                                      | Corrective action                                                                                                                                                                                                                 |  |  |  |
|------|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|
|      |                                                       |                                                                                                     | MASS/J14<br>Omni Rx2/J4<br>Omni<br>MASS/J15                                                                                                                                                                                       |  |  |  |
|      | RFPS Chain                                            |                                                                                                     |                                                                                                                                                                                                                                   |  |  |  |
| 1    | RFPS Link Not OK<br>a.                                | RFPS Chassis may not<br>be powered ON.                                                              | Check<br>Power ON of RFPS<br>Chassis.                                                                                                                                                                                             |  |  |  |
|      | b.                                                    | Ping<br>to<br>IP<br>Address:<br>192.168.5.100 of RFPS<br>may not be OK                              | Check<br>Ethernet<br>cable<br>connectivity between RFPS<br>and Ethernet switch-1 (EW<br>27 from Rack-2 J22 and EW<br>64 from J24 of Rack-2) and<br>SCD<br>and<br>Ethernet<br>SW-3<br>(EW-40)<br>Connect<br>cable<br>properly<br>/ |  |  |  |
|      |                                                       |                                                                                                     | replace if faulty.<br>Ethernet Switch 1 or 3 may<br>not be OK or not Powered<br>ON.                                                                                                                                               |  |  |  |
|      | c.                                                    | RFPS IP address and<br>Port<br>number<br>in<br>SCD<br>MMI<br>may<br>not<br>be<br>entered correctly. | Go to Offline in MMI and<br>Verify<br>the<br>IP<br>Address<br>(192.168.5.100) and Port No<br>(3600) of RFPS.                                                                                                                      |  |  |  |
|      |                                                       |                                                                                                     | If Not OK correct it and go to<br>online and check the status<br>of Link.                                                                                                                                                         |  |  |  |
|      | d.                                                    | RFPS Application may<br>not<br>be<br>triggered<br>properly                                          | Restart<br>the<br>RFPS<br>Application<br>and<br>check<br>the<br>Link.                                                                                                                                                             |  |  |  |
| 2    | RFPS status is Red<br>and Link is Green in<br>SCD MMI | DAU/DSP card may be<br>faulty                                                                       | Re-load/Replace<br>the<br>defective card.                                                                                                                                                                                         |  |  |  |
| 3    | Key board or tracker<br>ball not detected in          | Synergy<br>link<br>faulty<br>between SCD SBC and                                                    | Check<br>Ethernet connection<br>"RFPS-SCD SYNERGY" in                                                                                                                                                                             |  |  |  |

SHAKTI : UHB\Ch6 Page 529 of 614

| Ser. | Faults                               | Possible Cause                                                                                                                     | Corrective action                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|      | RFPS<br>Display<br>at<br>SCD Rack    | RPFS<br>SBC<br>at<br>SCD<br>Rack due to improper<br>shutting<br>down<br>or<br>starting<br>of<br>SBCs<br>or<br>RFPS/SCD Application | SCD Display is established.<br>Shutdown both RFPS and<br>SCD SBCs at SCD Rack and<br>Power<br>ON<br>for<br>proper<br>establishment<br>of<br>Synergy<br>Link.                                                                                                                                                                                                                                                                                         |
| 4    | DSP SRIO Transfer<br>Failed          | Invalid data might have<br>been<br>processed<br>by<br>DSP.                                                                         | Re-capture data in RFPS<br>Application. If issue persists,<br>shut down RFPS Processor<br>Chassis and Power ON.                                                                                                                                                                                                                                                                                                                                      |
| 5    | DMA Access failed                    | Invalid data might have<br>been acquired by DAU                                                                                    | Re-capture data in RFPS<br>Application. If issue persists,<br>shut down RFPS Processor<br>Chassis and Power ON.                                                                                                                                                                                                                                                                                                                                      |
| 6    | RFPS<br>Data<br>Acquisition time out | RF/IF<br>Path<br>may<br>be<br>faulty or IF Attenuation<br>and<br>Threshold settings<br>are not appropriate for<br>present signal.  | Check<br>corresponding<br>parameters'<br>tracks<br>are<br>available in SCD Display.<br>Check<br>proper<br>settings<br>for<br>IF/RF Attenuation.<br>Verify<br>with<br>Manual<br>BITE<br>RFPS<br>Monitor<br>RF<br>in<br>Spectrum<br>analyzer at RFPS Chassis<br>LRU input. Repair/ Replace<br>corresponding<br>component<br>for<br>which<br>output<br>is<br>not<br>available.<br>Check<br>RF and IF path to be<br>error free to deliver IF for<br>RFPS |
|      | MB2 Jammer                           |                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

SHAKTI : UHB\Ch6 Page 530 of 614

| Ser. | Faults                                                                                                                                    | Possible Cause                               | Corrective action                                                                                                                                                                                                |
|------|-------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1    | Link failure between<br>EAP<br>and<br>MB2<br>Jammer                                                                                       | Inter Lock Issues                            | Observe any faults reported<br>at<br>LCU<br>like<br>TEMP<br>and<br>FLOW<br>errors.<br>TEMP<br>OK<br>and FLOW OK are the inter<br>locks<br>to<br>Switch<br>ON<br>the<br>power<br>supplies<br>of<br>MB2<br>Jammer. |
|      |                                                                                                                                           | Ethernet<br>switch<br>could<br>be defective  | Check ETH SW2 and its<br>connections                                                                                                                                                                             |
| 2    | Tracking<br>issue<br>during<br>Track<br>and<br>JAM<br>command<br>in<br>case<br>of<br>Deception<br>Jamming Technique<br>and Spot Technique | Track could be passive<br>on SCD             | For a given track and JAM<br>command<br>for<br>a<br>particular<br>intercepted track on SCD,<br>observe the Track should be<br>in<br>Active<br>condition<br>during<br>Track and<br>Jam command.                   |
|      |                                                                                                                                           | Any obstruction to the<br>receiving Antennae | Check<br>there<br>is<br>no<br>obstruction on RX antenna<br>such that all the time RF<br>illumination should be on Rx<br>antenna and also Check the<br>functionality<br>of<br>Front<br>End<br>Unit.               |
|      |                                                                                                                                           | Blanking<br>may<br>be<br>the<br>issue        | Check<br>the cable between<br>ESI to the EA RACK-1 to be<br>connected<br>properly<br>(Blanking signal from ESI to<br>the EA rack-1)                                                                              |
| 3    | Link failure between<br>RFC, NG and CIB                                                                                                   | LVPS(MB2)<br>could<br>be<br>problem          | Observe any power supply<br>failure in the LVPS-4 and<br>monitor the voltages in front<br>panel. if supplies found not<br>OK replace the supply.                                                                 |

SHAKTI : UHB\Ch6 Page 531 of 614

| Ser. | Faults                                                                                                                                    | Possible Cause                                | Corrective action                                                                                                                                                                              |  |
|------|-------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
|      |                                                                                                                                           | Serial link cable may be<br>defective         | Check<br>the serial link cable<br>between<br>low<br>power<br>unit(MB2)<br>and<br>Tx(MB2)<br>should<br>be<br>connected<br>properly<br>and<br>check<br>the<br>continuity.                        |  |
| 4    | Tx(MB2) related Jam<br>On LED not blinking<br>during jamming                                                                              | SOP may not followed                          | Check<br>all the commands are<br>given properly.                                                                                                                                               |  |
|      |                                                                                                                                           | JAM INIT switch might<br>be not pressed       | Check<br>HV ON command of<br>Tx(MB2) and Jam Init switch<br>is pressed                                                                                                                         |  |
| 5    | Maintenance BITE<br>is<br>not OK                                                                                                          | DTO could be defective                        | Check<br>the functionality of 6-<br>18 GHz DTO                                                                                                                                                 |  |
|      | HB Jammer                                                                                                                                 |                                               |                                                                                                                                                                                                |  |
| 1    | Link failure between<br>EAP<br>and<br>HB<br>Jammer                                                                                        | Inter Lock Issues                             | Observe any faults reported<br>at<br>LCU<br>like<br>TEMP<br>and<br>FLOW<br>errors.<br>TEMP<br>OK<br>and FLOW OK are the inter<br>lock to enable the power<br>supplies.                         |  |
|      |                                                                                                                                           | Ethernet<br>switch<br>could<br>be defective   | Check ETH SW2 and its<br>connections                                                                                                                                                           |  |
| 2    | Tracking<br>issue<br>during<br>Track<br>and<br>JAM<br>command<br>in<br>case<br>of<br>Deception<br>Jamming Technique<br>and Spot Technique | Track could be passive<br>on SCD              | For a given track and JAM<br>command<br>for<br>a<br>particular<br>intercepted track on SCD,<br>observe the Track should be<br>in<br>Active<br>condition<br>during<br>Track and<br>Jam command. |  |
|      |                                                                                                                                           | Any obstruction to the<br>receiving Antennae. | Check<br>there<br>is<br>no<br>obstruction on RX antenna<br>such that all the time RF<br>illumination should be on Rx                                                                           |  |

SHAKTI : UHB\Ch6 Page 532 of 614

| Ser. | Faults                                                           | Possible Cause                                                                                                                                                         | Corrective action                                                                                                                   |
|------|------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
|      |                                                                  |                                                                                                                                                                        | antenna and also Check the<br>functionality<br>of<br>Front<br>End<br>Unit.                                                          |
|      |                                                                  | Blanking<br>may<br>be<br>the<br>issue                                                                                                                                  | Check<br>the cable between<br>ESI to the EA RACK-1 to be<br>connected<br>properly<br>(Blanking signal from ESI to<br>the EA rack-1) |
| 3    | Link failure between<br>RFCNG<br>and<br>Transmitter-HVPS<br>(HB) | Serial link cable may be<br>Check<br>serial<br>link<br>cable<br>defective<br>between low power unit(HB)<br>and Transmitter-HVPS (HB)<br>is intact both sides properly. |                                                                                                                                     |
| 4    | Tx(HB) related Jam<br>On LED not blinking                        | SOP may not followed.                                                                                                                                                  | Check all the commands are<br>given properly.                                                                                       |
|      | while jamming                                                    | JAM INIT switch might<br>be not pressed                                                                                                                                | Check<br>HV ON command of<br>Tx(HB) and Jam Init switch<br>is pressed.                                                              |
| 5    | Tx(HB)<br>related<br>HV<br>ON is not happening                   | Blower is not running                                                                                                                                                  | Check supply of 115V AC<br>supply                                                                                                   |
| 6    | Maintenance BITE<br>is<br>not OK                                 | DTO could be<br>defective                                                                                                                                              | Check<br>the functionality of 6-<br>18 GHz DTO                                                                                      |
|      | EA RACK-1                                                        |                                                                                                                                                                        |                                                                                                                                     |
| 1    | Link failure between<br>SCD and EAP                              | 24V to switch may not<br>available.                                                                                                                                    | LVPS-6<br>may<br>be<br>found<br>defective. Check<br>the input<br>power<br>supply<br>to<br>the<br>ETHSW2                             |
|      |                                                                  | ETHSW2<br>might<br>be<br>issue.                                                                                                                                        | Check<br>the<br>LED<br>blinking<br>status of corresponding Port<br>in ETHSW2                                                        |
|      |                                                                  | LAN EW cable may be<br>issue                                                                                                                                           | Check<br>the<br>ETHSW2<br>inter<br>connections and continuity                                                                       |

SHAKTI : UHB\Ch6 Page 533 of 614

| Ser. | Faults                                                                                                            | Possible Cause                                                                                            | Corrective action                                                                                                                                                                                     |
|------|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2    | Link Failure between<br>EAP and ESMP                                                                              | 24V to switch may not<br>available to switch.                                                             | LVPS-6<br>may<br>be<br>found<br>defective. Check<br>the input<br>power<br>supply<br>to<br>the<br>ETHSW2.                                                                                              |
|      |                                                                                                                   | ETHSW2<br>might<br>be<br>issue                                                                            | Check<br>the<br>LED<br>blinking<br>status of corresponding Port<br>in<br>ETHSW2<br>and<br>its<br>connections.                                                                                         |
| 3    | Power supply failure                                                                                              | Corresponding<br>power<br>supply module could be<br>defective.                                            | Check<br>the power ON LEDs<br>of<br>individual<br>modules<br>in<br>LVPS units are glowing. If<br>any module related LED is<br>not glowing, corresponding<br>power supply module has to<br>be checked. |
|      |                                                                                                                   | Interlock Issue                                                                                           | Check<br>the interlock to the<br>LVPS and HEU functionality                                                                                                                                           |
|      |                                                                                                                   | AC input issue<br>Check the PDP 2                                                                         |                                                                                                                                                                                                       |
| 4    | Power<br>supply<br>(LVPS-4 and<br>5) is<br>not getting switched                                                   | Interlock Issue.<br>Check<br>the temperature and<br>flow Ok status of<br>LCUs is<br>received at EA RACK-1 |                                                                                                                                                                                                       |
|      | ON in the EA RACK<br>1.                                                                                           | LVPS-6 might be issue<br>Check<br>the<br>functionality<br>of<br>the LVPS-6                                |                                                                                                                                                                                                       |
|      | EA RACK-2 (SCU<br>and SDA)                                                                                        |                                                                                                           |                                                                                                                                                                                                       |
| 1    | Issue in Engaging of<br>2 Axis Servo position<br>to<br>desired<br>bearing<br>value with track and<br>JAM command. | SDA-2Axis<br>Homing<br>Issue.                                                                             | Observe<br>the<br>Servo<br>link<br>status to be in green color in<br>EA<br>window<br>of<br>SCD.<br>Check<br>all the servo related<br>cables should be connected<br>properly.                          |
|      |                                                                                                                   | Stow<br>lock<br>might<br>be<br>pressed                                                                    | Check<br>the Stow lock lever is<br>in released condition. Else,<br>do<br>the<br>necessary                                                                                                             |

SHAKTI : UHB\Ch6 Page 534 of 614

| Ser. | Faults                                                            | Possible Cause                                     | Corrective action                                                                                                                                                                                                                           |
|------|-------------------------------------------------------------------|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|      |                                                                   |                                                    | maintenance activity on 2-<br>Axis servo                                                                                                                                                                                                    |
| 2    | Roll<br>pitch<br>stabilization issue for<br>the single Axis servo | SDA-1Axis<br>Homing<br>Issue.                      | Observe<br>the<br>Servo<br>link<br>status to be in green color in<br>EA window of SCD.<br>Check<br>all the servo related cables<br>should<br>be<br>connected<br>properly.                                                                   |
|      |                                                                   | Stow<br>lock<br>might<br>be<br>pressed             | Check<br>the Stow lock lever is<br>in released condition. Else,<br>do<br>the<br>necessary<br>maintenance activity on 1-<br>Axis servo                                                                                                       |
| 3    | Servos link failure                                               | Stow<br>lock<br>might<br>be<br>pressed.            | Disengage the stow locks,<br>Emergency<br>switches<br>and<br>verify the links.                                                                                                                                                              |
|      |                                                                   | Might be switched on in<br>maintenance mode        | Put<br>the<br>mode<br>switch<br>in<br>AUTO mode                                                                                                                                                                                             |
| 4    | 2-axis servo display<br>is hanged                                 | 2-<br>axis<br>SDA<br>cables<br>might not connected | Check<br>the cable connectivity<br>of the SDA to SCU cables                                                                                                                                                                                 |
|      | HEAT EXCHANGER UNIT(HEU)                                          |                                                    |                                                                                                                                                                                                                                             |
| 1    | Interlock issue                                                   | Temperature sensor.                                | Monitor<br>the<br>input<br>temperature<br>reading<br>at<br>display<br>HEU<br>and<br>check<br>temperature<br>20º<br>2º<br>at<br><br>temperature sensor if it is<br>not equal to specified value<br>replace<br>the<br>temperature<br>sensor. |
|      |                                                                   | Pressure Sensors.                                  | Replace<br>the<br>pressure<br>sensor after checking outlet<br>water flow in good condition.                                                                                                                                                 |

SHAKTI : UHB\Ch6 Page 535 of 614

| Ser. | Faults                                                          | Possible Cause                                           | Corrective action                                                                                            |
|------|-----------------------------------------------------------------|----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| 2    | Out let temperature<br>exceeding<br>the<br>temperature<br>limit | Might be inlet water to<br>HEU not available             | Check<br>inlet water availability<br>with a temperature of 10<br>º<br>C<br>and flow of 40 lpm                |
| 3    | Power on issue                                                  | Might circuit breaker in<br>PDP2 in off condition        | Check<br>the<br>breaker<br>in<br>on<br>condition and monitor the<br>230V AC supply in the input<br>connector |
| 4    | Out<br>let<br>water<br>flow<br>low                              | Might be the DM water<br>in the HEU tank in low<br>level | Check<br>the<br>required<br>DM<br>water level in the HEU                                                     |

For Detail Fault Diagnosis Refer Maintenance Manual Chapter III and VI.

SHAKTI : UHB\Ch6 Page 536 of 614

# **CHAPTER VII MISCELLANEOUS**

## **CHAPTER – VII**

#### **MISCELLANEOUS**

- **7.1 Introduction**.This chapter describe about the list of Equipment, B & D Spares, O B Spares, Handling instructions, Packaging instructions, Stowage/Storage instructions, Transportation instructions, Typical radiation patterns of EA/ES antennas and Shakti MMI Application Menu.
- **7.2 Equipment's**.The required Equipment's are listed in the below tables.

**Table-7.1: List of Equipment**

| Ser | Description                              | Part No.     | Qty |
|-----|------------------------------------------|--------------|-----|
| 1   | ES AHU-1                                 | 172300352518 | 1   |
| 2   | ES AHU-2                                 | 172300352615 | 1   |
| 3   | ES AHU-3                                 | 172300352712 | 4   |
| 4   | ES AHU-4                                 | 172300352809 | 1   |
| 5   | ES-Rack 1                                | 172300352906 | 1   |
| 6   | ES-Rack 2                                | 172300353003 | 1   |
| 7   | System Controller &Display<br>(SCD) Rack | 172300353197 | 1   |
| 8   | External System Interface (ESI)<br>Unit  | 172300353294 | 1   |
| 9   | Field Data Loader (FDL)                  | 172300353391 | 1   |
| 10  | Rugged Ethernet Switch (Type-1)          | 172300353488 | 2   |
| 11  | Rugged Ethernet Switch (Type-2)          | 172300353585 | 2   |
| 12  | EA Rack-1                                | 172300353779 | 1   |
| 13  | EA Rack-2                                | 172300353876 | 1   |
| 14  | MB2 Jammer                               | 172300353973 | 2   |
| 15  | HB Jammer                                | 172300354070 | 2   |
| 16  | Heat Exchanger Unit                      | 172300354167 | 2   |
| 17  | Transmitter-Power Supply (MB2)           | 172300354264 | 4   |

SHAKTI : UHB\Ch7 Page 537 of 614

| Ser | Description                | Part No.     | Qty     |
|-----|----------------------------|--------------|---------|
| 18  | Fault Diagnostic Rack(FDR) | 172300353682 | 1       |
| 19  | Installation<br>Cables     | 172300350384 | One Set |
| 20  | Installation Material      | 172300350287 | One Set |

**Table-7.2: List of B & D Spares List**

| Ser. | Material No. | Item Description (As per Contract) | QTY | UOM |
|------|--------------|------------------------------------|-----|-----|
| 1    | 172300752837 | AMP LMT with Video Module 18-40GHz | 1   | NO  |
| 2    | 172300752158 | Front End Module 2.2-18GHz         | 1   | NO  |
| 3    | 172300356301 | TDOA Processor PCB -<br>TYPE 2     | 1   | NO  |
| 4    | 172300752255 | FREQ Synthesizer 0.5-2G            | 1   | NO  |
| 5    | 172300391027 | Receiver Interface Board(RIB)      | 1   | NO  |
| 6    | 172300752449 | FREQ Synthesizer<br>2-18G          | 1   | NO  |
| 7    | 172300752449 | 18-40GHz Biconical Antenna         | 1   | NO  |
| 8    | 172300357077 | Display Monitor                    | 1   | NO  |
| 9    | 172300357368 | SBC PCB-<br>TYPE 1                 | 1   | NO  |
| 10   | 172300357465 | DAU PCB                            | 1   | NO  |
| 11   | 172300357562 | DSP PCB                            | 1   | NO  |
| 12   | 172300357659 | Emitter Processor PCB              | 1   | NO  |
| 13   | 172300357756 | PPD PCB                            | 1   | NO  |
| 14   | 172300357853 | SBC PCB -<br>TYPE 2                | 1   | NO  |
| 15   | 172300358241 | High Speed<br>ADC/DAC Module       | 1   | NO  |
| 16   | 172300753225 | LO Synthesizer<br>6-18G            | 1   | NO  |
| 17   | 172300753322 | DTO 6-18G                          | 1   | NO  |
| 18   | 172300358629 | RFC & NG Module                    | 1   | NO  |
| 19   | 172300753419 | Threshold Detector<br>6-18G        | 1   | NO  |

SHAKTI : UHB\Ch7 Page 538 of 614

| Ser. | Material No. | Item Description (As per Contract)                 | QTY | UOM |
|------|--------------|----------------------------------------------------|-----|-----|
| 20   | 172300753613 | Power Amplifier-1 6-18G                            | 1   | NO  |
| 21   | 172300753807 | SPST Switch                                        | 1   | NO  |
| 22   | 172300753904 | SP16T Switch                                       | 1   | NO  |
| 23   | 172300754583 | Set Of<br>Low Power Cables(OB)                     | 1   | NO  |
| 24   | 172300754001 | Waveguide Coupler 18-40G                           | 1   | NO  |
| 25   | 172300754389 | Threshold Detector<br>18-40G                       | 1   | NO  |
| 26   | 172300356204 | 2.2-18 GHZ Integrated Homodyne RX                  | 1   | NO  |
| 27   | 113060006663 | BMPM C-Ku 100 W                                    | 2   | NO  |
| 28   | 172300757202 | Set of High Power<br>SPDT SWITCHES(OB)             | 1   | NO  |
| 29   | 172300753710 | Power Amplifier-2 6-18G                            | 1   | NO  |
| 30   | 172300356495 | 0.5-18 GHZ QUAD S/H RX with<br>BDU                 | 1   | NO  |
| 31   | 172300243102 | ROTMAN lens beam forming N/W(6-<br>18GHz)          | 1   | NO  |
| 32   | 172300356980 | Quad Digital<br>RX                                 | 1   | NO  |
| 33   | 172300176560 | High Power Linear Array Ant. with Radome           | 1   | NO  |
| 34   | 172300758851 | Set Of High Power TNC<br>Cables<br>(OB)            | 1   | NO  |
| 35   | 172300358823 | EA Processor Module                                | 1   | NO  |
| 36   | 172300695413 | Control<br>I/F Module                              | 1   | NO  |
| 37   | 172300292184 | Sectoral<br>Horn<br>Rx Ant (6-18 GHz)              | 1   | NO  |
| 38   | 172300754292 | Power Amplifier 18-40G                             | 1   | NO  |
| 39   | 172300350869 | Storage Rack for OB Spares                         | 1   | NO  |
| 40   | 172300701718 | Penta Channel<br>DF Processor Board<br>(10<br>BIT) | 1   | No  |
| 41   | 172300356592 | Synthesizer<br>for<br>0.5-18 GHZ QUAD S/H<br>RXS   | 1   | No  |

SHAKTI : UHB\Ch7 Page 539 of 614

| Ser. | Material No. | Item Description (As per Contract)             | QTY | UOM |
|------|--------------|------------------------------------------------|-----|-----|
| 42   | 172300702203 | PPD Board<br>(LB1)                             | 1   | No  |
| 43   | 110005080127 | Type-3 BITE Unit<br>(18-40 GHz)                | 1   | NO  |
| 44   | 172300356786 | Receiver Processor Board                       | 1   | No  |
| 45   | 172300702397 | Rx & AMP Processor Board                       | 1   | No  |
| 46   | 172300353488 | Rugged Ethernet Switch<br>(TYPE-1)             | 1   | No  |
| 47   | 172300357950 | Receiver Processor Unit                        | 1   | No  |
| 48   | 172300696480 | Set of<br>EA Filter Modules                    | 1   | No  |
| 49   | 172300384819 | MMJ-Tx Interface PCB                           | 1   | No  |
| 50   | 172300176560 | High Power Linear Array<br>ANT. with<br>RADOME | 1   | No  |
| 51   | 172300354264 | Transmitter Power Supply (MB2)                 | 1   | NO  |
| 52   | 172300364158 | Control Panel I/F PCB                          | 1   | No  |
| 53   | 172300452622 | Transmitter Power Supply (HB)                  | 1   | NO  |
| 54   | 172300452719 | Transmitter HVPS (HB)                          | 1   | NO  |
| 55   | 172300532928 | Low Voltage Power Supply<br>(EACP)             | 1   | No  |
| 56   | 172300356107 | Bi-Conical Omni Antenna Stack                  | 1   | No  |
| 57   | 172300752061 | EDLVA 18-40GHz                                 | 1   | No  |
| 58   | 172300752352 | Down Converter 18-40 GHz                       | 1   | No  |
| 59   | 172300357174 | Keyboard                                       | 1   | No  |
| 60   | 172300358047 | External System Interface (ESI) Unit           | 1   | No  |
| 61   | 172300701330 | ASU (LB1-SHAKTI)                               | 1   | No  |
| 62   | 172300752643 | DIFM Receiver<br>2-18GHZ                       | 1   | No  |
| 63   | 172300752740 | Wide Band Tuner 2-18GHz                        | 1   | No  |
| 64   | 172300701427 | 70 MHz IF Module (LB1)                         | 1   | No  |

SHAKTI : UHB\Ch7 Page 540 of 614

| Ser. | Material No. | Item Description (As per Contract)      | QTY | UOM |
|------|--------------|-----------------------------------------|-----|-----|
| 65   | 172300357271 | Set of Discrete Spares for ES<br>System | 1   | No  |
| 66   | 172300358144 | Set of Spares for<br>LVPS 1 & 2         | 1   | No  |
| 67   | 172300757590 | DDUC 6-18G                              | 1   | No  |
| 68   | 172300358920 | Set of Spares for Front End Unit(MB2)   | 1   | No  |
| 69   | 172300359114 | Set f Spares for Front End Unit(HB)     | 1   | No  |
| 70   | 172300754195 | DDUC 18-40G                             | 1   | No  |
| 71   | 172300388020 | Set of Spares for Servo                 | 1   | No  |
| 72   | 172300359211 | Set of Spares for<br>LVPS(MB2)          | 1   | No  |
| 73   | 172300359308 | Set of Spares for LVPS(HB)              | 1   | No  |
| 74   | 172300359502 | Set of Spares for<br>HEU                | 1   | No  |

**Table-7.3: List of OB Spares List**

| Ser. | Material     | Item Description                           | Ord<br>Qty | UoM |
|------|--------------|--------------------------------------------|------------|-----|
| 1    | 172300352712 | ES AHU-3                                   | 4          | NO  |
| 2    | 172300347377 | OMNI Rx Module (MB-HB)                     | 4          | NO  |
| 3    | 172300347474 | OMNI MASS Module(MB-HB)                    | 4          | NO  |
| 4    | 172300356301 | TDOA Processor PCB -<br>TYPE 2             | 4          | NO  |
| 5    | 172300752255 | FREQ SYNTHESIZER 0.5-2G                    | 4          | NO  |
| 6    | 172300752449 | FREQ SYNTHESIZER 2-18G                     |            | NO  |
| 7    | 110005080127 | Type-3 BITE UNIT (18-40 GHz)               | 4          | NO  |
| 8    | 172300752643 | DIFM Receiver<br>2-18GHZ                   | 4          | NO  |
| 9    | 172300356786 | Receiver<br>Processor Board                | 4          | NO  |
| 10   | 172300356592 | Synthesizer FOR 0.5-18 GHz QUAD S/H<br>RxS | 4          | NO  |

SHAKTI : UHB\Ch7 Page 541 of 614

| Ser. | Material     | Item Description                                 | Ord<br>Qty | UoM |
|------|--------------|--------------------------------------------------|------------|-----|
| 11   | 172300356204 | 2.2-18 GHZ Integrated Homodyne RX                | 4          | NO  |
| 12   | 172300356495 | 0.5-18 GHZ QUAD S/H RX WITH BDU                  | 4          | NO  |
| 13   | 172300357950 | Receiver<br>Processor UNIT                       | 4          | NO  |
| 14   | 172300676983 | ASU (LB1-SHAKTI)                                 | 4          | NO  |
| 15   | 172300683482 | Multi CH RF Unit (LB1-SHAKTI)                    | 4          | NO  |
| 16   | 172300705792 | Power Supply (AHU1-LB1)                          | 4          | NO  |
| 17   | 172300826945 | Set of Spares for RX Processor-LB1               | 4          | Set |
| 18   | 172300826460 | Set of Spares for ESM Processor                  | 4          | Set |
| 19   | 172300826848 | Set of Spares for RX Processor                   | 4          | Set |
| 20   | 172300348056 | Control Unit<br>(ES RACK-1)                      |            | NO  |
| 21   | 172300347571 | Wide Band Tuner                                  |            | NO  |
| 22   | 172300826363 | Set of Spares for RFPS Processor                 |            | Set |
| 23   | 172300347862 | LVPS-1                                           | 4          | NO  |
| 24   | 172300347959 | LVPS-2                                           | 4          | NO  |
| 25   | 172300826751 | Set of Spares for SCD Processor                  | 4          | Set |
| 26   | 172300353488 | Rugged Ethernet Switch (TYPE-1)                  | 4          | NO  |
| 27   | 172300353585 | Rugged Ethernet Switch (TYPE-2)                  | 4          | NO  |
| 28   | 172300358047 | External System Interface (ESI) Unit             | 4          | NO  |
| 29   | 172300826557 | Set of Discreet Spares for ES<br>System<br>(B&D) |            | Set |
| 30   | 446172360141 | Display LCD 20" Flat Panel (Drip Proof)          | 4          | NO  |
| 31   | 172300358823 | EA Processor Module                              | 4          | NO  |
| 32   | 172300364158 | Control Panel I/F PCB                            | 4          | NO  |

SHAKTI : UHB\Ch7 Page 542 of 614

| Ser. | Material     | Item Description                                  | Ord<br>Qty | UoM |
|------|--------------|---------------------------------------------------|------------|-----|
| 33   | 172300532938 | Low Voltage Power Supply (EACP)                   | 4          | NO  |
| 34   | 172300346989 | EA Control Panel                                  | 4          | NO  |
| 35   | 172300441176 | Low Voltage Power Supply (MB2)                    | 4          | NO  |
| 36   | 172300441273 | Low Voltage Power Supply (HB)                     | 4          | NO  |
| 37   | 172300855657 | Set of Spares for LVPS(MB2)(B&D)                  | 4          | Set |
| 38   | 172300855754 | Set of Spares for LVPS(HB)(B&D)                   | 4          | Set |
| 39   | 172300452428 | Servo Control Unit (1-AXIS)                       | 4          | NO  |
| 40   | 172300452525 | Servo Control Unit (2-AXIS)                       | 4          | NO  |
| 41   | 172300757590 | DDUC 6-18G                                        |            | NO  |
| 42   | 172300358920 | Set of Spares for Front End Unit(MB2)             |            | Set |
| 43   | 172300292184 | Sectoral Horn Rx Ant (6-18 GHz)                   |            | NO  |
| 44   | 172300753419 | Threshold Detector 6-18G                          | 4          | NO  |
| 45   | 113060006663 | BMPM C-Ku 100 W                                   | 8          | NO  |
| 46   | 172300176560 | High Power Linear Array Ant. With<br>Radome       |            | NO  |
| 47   | 172300855269 | Set<br>of<br>High Power SPDT<br>Switches<br>(B&D) | 4          | Set |
| 48   | 172300753613 | POWER AMPLIFIER-1 6-18G                           | 4          | NO  |
| 49   | 172300243102 | ROTMAN lens beam forming N/W(6-<br>18GHz)         |            | NO  |
| 50   | 172300695413 | CONTROL I/F Module                                | 4          | NO  |
| 51   | 172300753710 | Power Amplifier-2 6-18G                           | 8          | NO  |
| 52   | 172300753807 | SPST SWITCH                                       | 4          | NO  |
| 53   | 172300753904 | SP16T SWITCH                                      | 4          | NO  |

SHAKTI : UHB\Ch7 Page 543 of 614

| Ser. | Material     | Item Description                        | Ord<br>Qty | UoM |
|------|--------------|-----------------------------------------|------------|-----|
| 54   | 172300855366 | Set<br>OF High Power TNC Cables (B&D)   | 4          | Set |
| 55   | 172300855463 | Set<br>of<br>Low Power Cables(B&D)<br>4 |            | Set |
| 56   | 172300358241 | High Speed ADC/DAC Module               | 4          | NO  |
| 57   | 172300358629 | RFC & NG Module                         | 4          | NO  |
| 58   | 172300753225 | LO Synthesizer 6-18G                    | 8          | NO  |
| 59   | 172300753322 | DTO 6-18G                               | 4          | NO  |
| 60   | 172300696480 | Set<br>of<br>EA Filter Modules          | 4          | Set |
| 61   | 172300855851 | Set<br>OF SPARES FOR SERVO(B&D)         | 4          | Set |
| 62   | 172300322836 | Pyramidal Horn Rx Antenna (18-40GHz)    | 4          | NO  |
| 63   | 172300855560 | FRONT END Module(HB)                    | 4          | NO  |
| 64   | 172300754195 | DDUC 18-40G                             | 4          | NO  |
| 65   | 172300765350 | OSCILATOR 10GHz(HB)                     | 4          | NO  |
| 66   | 172300765447 | Harmonic Detection Module<br>(HB)       | 4          | NO  |
| 67   | 172300754389 | Threshold Detector 18-40G               | 4          | NO  |
| 68   | 172300754292 | Power Amplifier 18-40G                  | 4          | NO  |
| 69   | 474272210116 | RM Blower<br>155CFM 1.2A 115V 76.2D     | 4          | NO  |
| 70   | 172300754001 | Waveguide Coupler 18-40G                | 4          | NO  |
| 71   | 172300384819 | MMJ-Tx INTERFACE PCB                    | 4          | NO  |
| 72   | 172300765253 | Blower Current Sense PCB                | 4          | NO  |
| 73   | 172300292087 | Pyramidal Horn Tx Antenna(18-40GHz)     | 4          | NO  |
| 74   | 172300526536 | HB TWT ASSY                             | 4          | NO  |
| 75   | 172300452622 | Transmitter Power Supply (HB)           | 4          | NO  |

SHAKTI : UHB\Ch7 Page 544 of 614

| Ser. | Material     | Item Description               | Ord<br>Qty | UoM |
|------|--------------|--------------------------------|------------|-----|
| 76   | 172300452719 | Transmitter HVPS (HB)          | 4          | NO  |
| 77   | 172300354264 | Transmitter Power Supply (MB2) | 4          | NO  |
| 78   | 172300855948 | Set<br>OF SPARES FOR HEU(B&D)  | 4          | Set |

EW cable details Refer Installation Manual Chapter no III Para no. 3.10.

- **7.3 Handling, Packaging, Stowage/Storage and Transportation**.This Chapter describes the Handling, Packaging, Stowage/Storage and Transportation of the Shakti System.
- **7.3.1 Handling Instructions**.The following instructions must be strictly adhered to:
  - (a) The equipment handling is restricted to trained and qualified personnel only.
  - (b) Personnel must be trained to adopt the safety precautions prescribed in the technical manual.
  - (c) Handle with care and avoid breakages, damages and other costly failures.
  - (d) It is prohibited to violate the handling, packaging, storage and transportation instructions specified in the user hand book.
- **7.3.2 Handling Precautions**.Following precautions are to be undertaken whilst handling the Units Sub units / Modules / Spares / Components:
  - (a) All personnel who supervise or perform work in connection with the handling of the equipment must be familiar with the instructions and directives of agency concerned.
  - (b) All concerned personnel must become familiar with the equipment and support equipment before undertaking any operation or procedure. All concerned personnel must read the complete operation or procedure thoroughly before starting, to assure complete understanding by all involved.
  - (c) All personnel must understand that observance of all precautions that are applicable to any specific equipment will be ineffective unless all safety precautions that are applicable to its related equipment are not observed at the same time.

SHAKTI : UHB\Ch7 Page 545 of 614

- (d) Safely devices must always be used to minimize the possibility of accidents. Safety devices must be kept in good operating order.
- (e) Once the equipment is connected to the power supply, personnel must be aware that the system uses and generates voltages that can cause injury or death.
- (f) When working around movable components such as antennae, use caution, as unexpected movement may cause serious injury. Make sure that all safety precautions have been observed prior to working in these areas.
- (g) Proper care must be exercised when handling equipment or components. Many components are heavy and personnel should not try to handle them by hand.
- (h) Care must be exercised to use tools that are suitable for the task in order to avoid damage of parts or tools.
- (j) Avoid damage to parts and components during handling. Damage caused by careless handling can cause improper functioning. Replace all the defective parts.
- (k) Protect cable ends and connectors from penetrating moisture, grease or solvent.
- **7.3.3 Packaging**.The Equipment is packed either in wooden boxes or on wooden pallets or in crates of appropriate sizes as necessary. Before packing the equipment do not remove the drawers from the respective cabinets. Hence the cabinets along with PCBs and Modules are to be packed as per packing standards.
- 7.3.3.1 The Equipment Racks, Operation Console, Antennae, Transmitters and other subunits is properly secured to the base of the wooden box and appropriately strengthened to prevent any lateral / horizontal / vertical movements to prevent damages during loading, unloading operations and transit.
- 7.3.3.2 The PCBs are wrapped with bubble sheet around, placed in an anti-static cover and covering box.
- 7.3.3.3 These boxes are identified with the marking stickers that indicate the part number and serial number of the PCB and are plugged in the wooden boxes. The cabinets and drawers are also dispatched in reusable wooden storage cases with proper packing material.

SHAKTI : UHB\Ch7 Page 546 of 614

- 7.3.3.4 The storage case has fixed locations for equipment and accessories inside it. The packed unit is placed in the storage case in such a way that the top is towards the lid. The top lid of the storage case is closed and sealed. This storage case is reusable type for road/rail transportation and shall not be discarded.
- **7.3.4 Stowage / Storage**.After receipt and inspection for damage, the equipment should be restored to its packing cases and kept in a dry warehouse, well protected, until the time of installation.
- 7.3.4.1 After unpacking onboard ship/submarine and during installation, utmost care should be taken to protect the equipment from water, dust, paint, spray, etc., by covering the units with temporary covers.
- **7.3.5 Storage Instructions**.The following must be packed according to packaging instructions.
  - (a) Equipment detailed for storage must be packed according to the packaging instructions.
  - (b) The checks as given in Table-7.3 must be carried out on the equipment under storage.

**Table-7.3: Checks during Storage**

| Ser. | Detail of checks                                                                                                        | Frequency |
|------|-------------------------------------------------------------------------------------------------------------------------|-----------|
| 1.   | External Inspection of package for damages.                                                                             | Daily     |
| 2.   | Internal<br>visual<br>inspection<br>of<br>equipment<br>for<br>corrosion,<br>cracks, dents, or any other contaminations. | Monthly   |

- (c) Abnormalities observed during the above mentioned checks must be rectified before preparing the equipment for long term storage.
- (d) If on a component, rust or corrosion spots are detected, these should be removed immediately. If such a part can be disassembled easily without requiring re-adjustments or special aids, it is preferable to remove the part a substantial part around the corroded area must be made clear of preservative. Thereafter, remove the corrosive material with emery cloth, preventing the deposit of abrasive material on the surrounding components. Cover such components with a clean cloth. Finally, apply a thin layer of grease on the cleaned part.

7.3.5.1 If, on the equipment stored outside, contamination with soot or salt is observed

SHAKTI : UHB\Ch7 Page 547 of 614

then clean with water and soap.

- 7.3.5.2 Pest control should be conducted regularly for insects and rodents attacks.
- **7.3.6 Transportation Instructions**.The Shakti subsystems packed in the wooden boxes can be transported either by road or rail to the destination. Ensure that the wooden boxes are kept in such a way that the top is towards the lid. There is no special transportation is required for Shakti Subsystem.
- **7.4 Typical radiation patterns of EA antennas**.The following are the typical radiation patterns of EA antennas:

SHAKTI : UHB\Ch7 Page 548 of 614

#### **7.4.1 6-18GHz High Power Linear Array Antenna**:

**Item:** High Power linear Array With Radome

**Part No.** 172300176560

**Mounted On Assembly:** MB2-Tx Unit

**Part No.** 172300785526

**Frequency:** For Graph (a) 9 GHz.

For Graph (b) 6 GHz, 7 GHz, 8 GHz, 9 GHz, 10 GHz

**Graph:** Amplitude (dB) vs Azimuth (deg)

**Polarization:** VP

**Graph (a)** When all beams are over-laid.

![](_page_554_Figure_11.jpeg)

SHAKTI : UHB\Ch7 Page 549 of 614

![](_page_555_Figure_1.jpeg)

**Graph (b)** Elevation pattern of linear array.

#### **7.4.2 6-18GHz Sectoral Horn Rx Antenna**

**Item:** Sectorial Horn Rx Ant (6-18 GHz)

**Part No.** 172300292184

**Mounted On Assembly:** MB2-Front End Assy.

**Part No.** 172300785429

**Frequency:** For Graph (a) 13 GHz.

For Graph (b) 15 GHz

**Graph:** Amplitude (dB) vs Azimuth (deg)

**Polarization:** For Graph (a) VP

For Graph (b) HP

SHAKTI : UHB\Ch7 Page 550 of 614

**Graph (a)** Azimuth pattern of the Sectoral horn Rx antenna in both Vertical and Horizontal polarizations.

![](_page_556_Figure_2.jpeg)

**Graph (b)** Elevation Pattern of the Sectoral horn Rx antenna in both Vertical and Horizontal polarizations.

![](_page_556_Figure_4.jpeg)

SHAKTI : UHB\Ch7 Page 551 of 614

#### **7.4.3 18-40GHz Pyramidal Horn Transmitter Antenna**:

**Item:** Pyramidal Horn Tx Antenna (18-40 GHz)

**Part No.** 172300292087

**Mounted On Assembly:** Transmitter unit (HB)

**Part No.** 172300346892

**Frequency:** 23 GHz.

**Graph:** Amplitude (dB) vs Azimuth (deg)

**Polarization:** VP

![](_page_557_Figure_9.jpeg)

#### **7.4.4 18-40GHz Pyramidal Horn Receiving Antenna**:

**Item:** Pyramidal Horn Tx Antenna (18-40 GHz)

**Part No.** 172300322836

**Mounted On Assembly:** Front End Unit (HB)

**Part No.** 172300346601

**Frequency:** For Graph (a) 20 GHz

SHAKTI : UHB\Ch7 Page 552 of 614

For Graph (b) 23 GHz

**Graph:** Amplitude (dB) vs Azimuth (deg)

**Polarization:** HP

#### **Graph (a) 20 GHz**

![](_page_558_Figure_5.jpeg)

SHAKTI : UHB\Ch7 Page 553 of 614

#### **Graph (b) 20 GHz**

![](_page_559_Figure_2.jpeg)

SHAKTI : UHB\Ch7 Page 554 of 614

#### **7.5 Typical radiation patterns of ES antennas**.

**Item:** LB(175-500 MHz) ANTENNA ARRAY

**Part No.** 172300685616

**Mounted On Assembly:** AHU-1

**Part No.** 172300352518

**Frequency:** 180 MHz.

**Graph:** Angle Vs Magnitude

**Polarization:** H/H

**Antenna Type** DIPOLE

![](_page_560_Figure_10.jpeg)

SHAKTI : UHB\Ch7 Page 555 of 614

**Item:** LB(175-500 MHz) ANTENNA ARRAY

**Part No.** 172300685616

**Mounted On Assembly:** AHU-1

**Part No.** 172300352518

**Frequency:** 180 MHz.

**Graph:** Angle Vs Magnitude

**Polarization:** V/V

**Antenna Type** DIPOLE

![](_page_561_Figure_9.jpeg)

SHAKTI : UHB\Ch7 Page 556 of 614

**Item:** LB(175-500 MHz) ANTENNA ARRAY

**Part No.** 172300685616

**Mounted On Assembly:** AHU-1

**Part No.** 172300352518

**Frequency:** 180 MHz.

**Graph:** Angle Vs Magnitude

**Polarization:** H/H

**Antenna Type** LOOP

![](_page_562_Figure_9.jpeg)

SHAKTI : UHB\Ch7 Page 557 of 614

**Item:** LB(175-500 MHz) ANTENNA ARRAY

**Part No.** 172300685616

**Mounted On Assembly:** AHU-1

**Part No.** 172300352518

**Frequency:** 180 MHz.

**Graph:** Angle Vs Magnitude

**Polarization:** V/V

**Antenna Type** LOOP

![](_page_563_Figure_9.jpeg)

SHAKTI : UHB\Ch7 Page 558 of 614

**Item:** Antenna Array 2.2 - 18 GHz

**Part No.** 476777960191

**Mounted On Assembly:** BB & NBRx (LB2-MB)

**Part No.** 172300646331

**Frequency:** 9.4 GHz.

**Graph:** Magnitude (dB) vs Angle (deg)

**Polarization:** Vertical

**Antenna Type** CBS Antenna

![](_page_564_Figure_9.jpeg)

SHAKTI : UHB\Ch7 Page 559 of 614

**Item:** Spiral 0.818

**Part No.** 476777960191

**Mounted On Assembly:** BB & NBRx (LB2-MB)

**Part No.** 1723 006 463 31

**Frequency:** 3.0 GHz

**Graph:** Magnitude (dB) vs Angle (deg)

**Polarization:** Vertical

**Antenna Type** Spiral

![](_page_565_Figure_9.jpeg)

SHAKTI : UHB\Ch7 Page 560 of 614

**Item:** Spiral Antenna 0.4 – 2.2 GHz

**Part No.** 476778070189

**Mounted On Assembly:** BB & NBRx (LB2-MB)

**Frequency:** 1.27 GHz

**Graph:** Magnitude (dB) vs Angle (deg)

**Polarization:** Vertical

**Antenna Type** Spiral Antenna

![](_page_566_Figure_8.jpeg)

SHAKTI : UHB\Ch7 Page 561 of 614

**Item:** Biconical OMINI ANTENA STACK 2.2 TO 40 GHz

**Part No.** 1723 003 561 07

**Mounted On Assembly:** Omni Receiver Module

**Part No.** 1723 003 473 77

**Frequency:** 10. 500000GHz

**Graph:** Magnitude(dB) Vs Angle(deg)

**Polarization:** Vertical

**Antenna Type** Omini Antenna

![](_page_567_Figure_9.jpeg)

SHAKTI : UHB\Ch7 Page 562 of 614

**Item:** Biconical OMINI ANTENA STACK 2.2 TO 40 GHz

**Part No.** 1723 003 561 07

**Mounted On Assembly:** Omni Receiver Module

**Part No.** 1723 003 473 77

**Frequency:** 36. 500000GH2

**Graph:** Angle vs Magnitude

**Polarization:** H/H

**Antenna Type** Biconical

![](_page_568_Figure_9.jpeg)

SHAKTI : UHB\Ch7 Page 563 of 614

**Item:** Biconical ANTENA 18 TO 40 GHz

**Part No.** 4767 781 201 44

**Mounted On Assembly:** AHU-3

**Part No.** 1723 003 527 12

**Frequency:** 180 GHz.

**Graph:** Angle vs Magnitude

**Polarization:** Vertical

**Antenna Type** Biconical

![](_page_569_Figure_9.jpeg)

SHAKTI : UHB\Ch7 Page 564 of 614

## **7.6 Shakti MMI Application Menu**.

(xxx) Indicates the page no which contains corresponding menu.

![](_page_570_Figure_3.jpeg)

![](_page_571_Figure_1.jpeg)

SHAKTI : UHB\Ch7 Page 566 of 614

![](_page_572_Figure_1.jpeg)

SHAKTI : UHB\Ch7 Page 567 of 614

![](_page_573_Figure_1.jpeg)

SHAKTI : UHB\Ch7 Page 568 of 614

![](_page_574_Figure_1.jpeg)

SHAKTI : UHB\Ch7 Page 569 of 614

![](_page_575_Figure_1.jpeg)

SHAKTI : UHB\Ch7 Page 570 of 614

![](_page_576_Figure_1.jpeg)

SHAKTI : UHB\Ch7 Page 571 of 614

![](_page_577_Figure_1.jpeg)

SHAKTI : UHB\Ch7 Page 572 of 614

![](_page_578_Figure_1.jpeg)

SHAKTI : UHB\Ch7 Page 573 of 612

**This page is Intentionally Left Blank.**

![](_page_580_Figure_1.jpeg)

SHAKTI : UHB\ Ch7 Page 575 of 612

![](_page_581_Picture_0.jpeg)

**This page is Intentionally Left Blank.**

SHAKTI : UHB\Ch1 Page 576 of 612

![](_page_582_Figure_0.jpeg)

**This page is Intentionally Left Blank.**

# **CHAPTER VIII SAFETY PRECAUTIONS**

#### **CHAPTER - VIII**

## **SAFETY INSTRUCTIONS**

## **8 Introduction**.

- **8.1 General**. Maintenance can present danger if safety precautions are not observed. Whilst every precaution is taken when manufacturing the system to avoid danger to personnel, the human element can never be eliminated. This chapter gives an indication of the danger areas of the equipment, and instructions on how to avoid accidents or equipment damage when operating or maintaining the equipment.
- 8.1.1 The following details are given:
  - (a) Type of danger
  - (b) Consequences of the danger, in the case of injury
  - (c) Precautions to avoid danger or injury
  - (d) Possible locations of danger
  - (e) Indications of danger
  - (f) General precautions
  - (g) Precautions to avoid equipment damage
- 8.1.2 The likely hood of the physical injury depends, among other things, on the following factors
  - (a) The Professional skill of operating and maintenance personnel.
  - (b) The knowledge of the personnel concerning possible risks.
  - (c) The degree of concentration of these personnel during their work.
  - (d) The type of work.

SHAKTI : UHB\Ch8 Page 581 of 614

- 8.1.3 Personnel operating, maintaining or repairing the equipment, and people located in the near vicinity of this equipment must be in formed of possible risks. This advice in no way supersedes any instruction is sued from a higher authority or contained in Departmental Standing Orders.
- **8.2 Safety Signs**. This paragraph illustrates and explains where necessary, all signs which are used to indicate danger or specific areas where special precautions must be taken.
- **8.2.1 High Voltage**. These first signs are used where voltages in excess of voltage value are present. The expected voltage is indicated on the sign. The sign of the lower figure is self-explanatory.

![](_page_586_Picture_4.jpeg)

**Figure-8.1: Voltage Value**

![](_page_586_Picture_6.jpeg)

**Figure-8.2 High Voltage**

SHAKTI : UHB\Ch8 Page 582 of 614

![](_page_587_Picture_1.jpeg)

**Figure-8.3: Warning Local any Work**

**8.2.2 Ionizing Radiation These**.These signs are self-explanatory.

![](_page_587_Picture_4.jpeg)

**Figure-8.4-Safety Sign for Ionizing Radiation**

![](_page_587_Picture_6.jpeg)

**Figure-8.5: Safely Sign for Ionizing Radiation**

SHAKTI : UHB\Ch8 Page 583 of 614

**8.2.3 Microwave Radiation.** This sign is self-explanatory.

![](_page_588_Picture_2.jpeg)

**Figure-8.6: Safety Sign for Microwave Radiation**

**8.2.4 Laser Radiation**. This signs are self-explanatory.

![](_page_588_Picture_5.jpeg)

**Figure-8.7: Safety Sign for Laser Radiation**

**8.2.5 Poisonous Substances**. This sign indicates that the substance is poisonous if it is admitted to the body by swallowing, through breathing or via the skin. The sign is normally present on the packaging.

![](_page_588_Picture_8.jpeg)

**Figure-8.8: Safety Sign for Poisonous Substances**

SHAKTI : UHB\Ch8 Page 584 of 614

**8.2.6 Caustic Substances**.This sign indicates that a substance is caustic i.e. can cause skin or eye irritation. It is normally present on the packaging.

![](_page_589_Picture_2.jpeg)

**Figure-8.9: Safety Sign for Caustic Substances**

**8.2.7 Inflammable Substances**. This sign indicates that the flash point of the substance is below 21 °C. It is normally present on the packaging

![](_page_589_Picture_5.jpeg)

.**Figure-8.10: Safety Sign for Inflammable Substances**

**8.2.8 High Temperatures**.This sign is self-explanatory

![](_page_589_Picture_8.jpeg)

**Figure-8.11: Safety Sign for High Temperatures**

**8.2.9 Beryllium Oxide (a)**.This sign indicates that the product contains beryllium oxide. Beryllium oxide dust and fumes are highly toxic. Breathing them can result in

SHAKTI : UHB\Ch8 Page 585 of 614

serious personal injury or death. The sign is normally on the product and/or packaging.

![](_page_590_Picture_2.jpeg)

**Figure-8.12: Safety Sign for Beryllium Oxide**

**8.2.10 Beryllium Oxide(b)**. This sign indicates the same as 'a' but is placed on the equipment near to the part which contains beryllium oxide. The arrow points to the part concerned.

![](_page_590_Picture_5.jpeg)

**Figure-8.13: Safety Sign for Beryllium Oxide**

**8.2.11 Beryllium Oxide(c)**.This sign is used as alternative to 'a'.

![](_page_590_Picture_8.jpeg)

**Figure-8.14: Safety Sign for Beryllium Oxide**

**8.2.12 Ultra Violet Radiation**.This sign is self-explanatory

SHAKTI : UHB\Ch8 Page 586 of 614

![](_page_591_Picture_1.jpeg)

**Figure-8.15: Safety Sign for Ultra Violet Radiation**

#### **8.3 Personal Protection**.

- **8.3.1 General**. In spite of the many safety precautions taken, accidents can still occur. Utilizing protective clothing and other facilities for personal protection which are available can minimize the chance of personal injury when working in dangerous situations.
- 8.3.1.1 The chance of injury in potentially dangerous situation scan be minimized by performing the task by two persons, of which one is leading.
- **8.3.2 Working in Dangerous Situations**. Personal injury can be avoided by the use of protective clothing, etc. when working in the following situations
  - (a) when there is risk of injury to the eyes or face (welding, implosion of CRTs, etc.), when there is a risk of injury to the ears (explosion, high noise levels, etc.),
  - (b) when there is a risk of injury to the hands (handling chemical sand other dangerous substances),
  - (c) when there is a risk of injury to the respiratory system (breathing in poisonous fumes, gases, etc.),
  - (d) when there is a risk of injury to the head (falling objects, etc.), when there is a risk of falling.
- **8.3.2.1 Eye/Face Protection**. Injury to the eyes alone (i.e. blinding) can be avoided by the use of safety goggles. A face mask offers more complete protection, for the eyes,

SHAKTI : UHB\Ch8 Page 587 of 614

private spectacles and the rest of the face, from flying glass, sparks, spattering chemicals, etc.

- **8.3.2.2 Ear Protection**. When working in areas with a high noise level (engine room, etc.) ear defenders or ear plugs may be worn to avoid damage to hearing. As a guide, the ears must be protected where the permanent noise level is higher than 90 d Bs ,or levels higher than 90 d Bs will be experienced for short periods.
- **8.3.2.3 Hand Protection**. When handling chemicals, certain cleaning agents or adhesives, etc. it is advised to wear rubber gloves. When handling CRTs, etc., where there is a risk of flying glass due to implosion of the CRT, it is advised to wear leather gloves.
- **8.3.2.4 Respiratory System Protection**. When working with chemicals which give off poisonous gases, when cleaning up damaged. Radio - active components or other similar situations, it is advised to wear an adequate gas mask to avoid breathing in dangerous fumes.
- **8.3.2.5 Head Protection**. In situations where there is a risk of objects falling from above or bumping of the head due to low beams, etc., a suitable safety helmet should be worn.
- **8.3.2.6 Protection from Falling**. When working at great height, on radar antennas, etc., it is advised to wear a safety harness with safety line securely attached. When working with ladders, ensure that the ladder cannot slip.

**WARNING: The use of protective clothing, etc. does not mean that normal safety precautions can be ignored. The best protection against personal injury is care and attention when working**

#### **8.4 Electricity**.

**8.4.1 General**. In spite of the fact that the equipment has been provided with safety provisions, voltages inexcessof30 volts RMS or 50 VDC can be dangerous under certain circumstances, and higher voltage value scan be fatal. It is emphatically recommended to strictly observe the following instructions:

SHAKTI : UHB\Ch8 Page 588 of 614

- 8.4.1.1 Operation and maintenance of the system must only be carried out by fully qualified personnel, whenever possible maintenance activities must be performed with the equipment fully switched off (no voltages present).
- 8.4.1.2 To bring the equipment to a switched off state and to ensure that it remains so, the following precautions must be taken:
- **8.4.1.1 Switching Off**. To ensure complete safety, all supply voltages to the equipment to be maintained must be switched off including those for anti-condensation heating.
- **8.4.1.2 Protection Against Accidental Switch On**. To prevent the equipment accidentally being switched on while maintenance is in progress the following precautions should be taken:
  - (a) Lock the switches or remove the switch lever (if possible), remove
  - (b) The relevant supply fuses and store them in a safe place,
  - (c) Place a warning notice with the following text close to the switch off area.

| WARNING                                               |
|-------------------------------------------------------|
| DO NOT SWITCH ON MAINTENANCE IN<br>PROGRESS LOCATION  |
| REMOVE OF THIS WARNING NOTICE IS<br>ONLY PERMITTED BY |

## **8.4.1.3 Additional Safety Measures**.

- (a) Check that no voltage is present on all incoming wiring using an applicable
- (b) Volt meter. Discharge all capacitors, etc. to earth using a properly earthed discharge rod.
- (c) Do not override or short circuit safety interlocks on doors, panels or drawers. When performing a two man job, one must always be in charge.

SHAKTI : UHB\Ch8 Page 589 of 614

- **8.4.2 Working with Voltage Switched On**.It is stressed that where possible no voltages must be present when performing maintenance; where this is not possible e.g. when performing tests or making electrical adjustments, the following additional precautions must be taken
  - (a) Before beginning the task, ensure the whereabouts of the main supply
  - (b) Switch (es) is known, always work with a second man (safety man),
  - (c) Remove all jewelry (rings, watches, medallions. etc.) which can come into contact with live components. Tuck tie into shirt,
  - (d) Always work with one hand in pocket. Under no circumstances use the free hand to grasp the chassis (earth): this can result in electric shock across the heart,
  - (e) Do not switch on more voltages or parts of the equipment than are absolutely necessary.

#### **8.4.2.1 Additional Precautions to Avoid Damage to Equipment**.

Not only damage to the person can occur when voltage is present, but also damage to the equipment if the following general rules are not observed

- (a) Do not exchange components with voltage switched on. The extreme change in voltage can be very damaging to some components,
- (b) Do not try to discharge capacitors, etc. to earth with voltage present
- (c) Do not drop metallic objects in to the equipment with voltage switched on. Do not leave foreign objects such as nuts, bolts, lengths of wire, etc. behind in the equipment.
- **8.4.3 Tools**. Too ls must always be of the insulated type. All electric tools must be of the double insulated type, if possible. Otherwise check always if the earth-connection of the tool concerned is correct before starting the job.
- **8.4.4 Extinguishing Fires**. When a fire starts in a cabinet of the installation, the cabinet must be switched off immediately. The fire must be isolated and extinguished by

SHAKTI : UHB\Ch8 Page 590 of 614

means of a carbon dioxide extinguisher. It is better not to fight a fire in a cabinet with a powder extinguisher or water, since electronic circuits and wiring will become severely damaged. To shut off oxygen, the are a must be closed off as quick as possible.

- **8.4.5 Personal Injury**.Injuries caused by electricity are mostly shock sand burns. It is recommended to consult a doctor in all cases.
- **8.5 Working in Confined Spaces**. When working in confined spaces (such as radomes) fresh air can enter only by the small access hatch. Due to the lack off fresh air, maintainers may suffer some discomfort when working in the radome for long periods. Forced ventilation of the radome should be provided if men are to remain continuously in the radome for more than two hours. Ventilation may be provided by placing an electric fan close to the access hatch, or by ducting air in to the radome via a flexible pipe from a vacuum cleaner or the ventilation system.
- **8.6 Antenna Movement**. Unexpected movement of an antenna may cause consider able injuries to personnel near by. Injuries may result not only from direct contact with the antenna, but also from a subsequent fall from the antenna mounting platform. Therefore whenever work is to be carried out in the vicinity of a moving antenna, the man aloft switch/maintenance switch for that system must be set to SAFE. See also paragraph 3.1.2.
- **8.7 Vacuum Tubes**. To avoid personal injury when handling vacuum tubes (implosion danger) the following general safety precautions must be strictly observed.
  - (a) Only store vacuum tubes in their original packaging.
  - (b) Always wear protective clothing (i.e. leather gloves, apron and face mask) when handling
  - (c) Vacuum tubes.
  - (d) Never lift vacuum tubes by the neck or a mechanically sensitive part.
  - (e) Always discharge a used vacuum tube a couple of times, ifa high voltage was connected. Place a
  - (f) Vacuum tube on a soft surface.

SHAKTI : UHB\Ch8 Page 591 of 614

- (g) CRTs shall be placed with the screen facing down (where possible).
- (h) Use empty packaging for transport of the exchanged tube to a disposal place.

### **8.8 Radio Active Substances**.

- **8.8.1 Components Producing Ionising Radiation**. Ionizing radiation is either produced by radioactive substances or, artificially by high-voltage vacuum tubes in operation (X-ray radiation).
  - (a) Radioactive substances continuously produce radiation, which decreases in the course of time. This radiation may be injurious to health, requiring radioactive components to be handled with care. Examples are
    - (i) TR-cells,
    - (ii) Spark gaps (some types).
  - (b) High-voltage vacuum tubes examples are
    - (i) Travelling Wave Tubes,
    - (ii) Stabilization Tubes.
- 8.8.1.1 Under normal conditions, where the components are properly mounted in the unit, and the front plate sand doors are fitted, the radiation is less than 0.1m at a distance of IO cm from unit.
- **8.8.2 Danger of lionizing Radiation**. Ionizing grays may damage biological tissues and cells, the degree of damage depending on the kind of radiation and the energy level.
- 8.8.2.1 Human organs which generate new cells, such as the spleen, the sexual organs and bone marrow, are very sensitive to these rays.
- 8.8.2.2 Ionizing radiations not perceptible to the senses and the consequences are not immediately noticeable. Thus it is possible to receive a harmful dose of radiation whose effect will only be notice able after a longer term. To avoid this, the dose of radiation a

SHAKTI : UHB\Ch8 Page 592 of 614

person is permitted to receive during a certain period of time is limited. At this moment the limit is 2 mS/year

- 8.8.2.2 (0.2Rem/year), averaging lµS/hour(0.1mRem/hour)for 2000working hours per year. In addition to the above risks, radio active substances also include danger of contamination. This kind of danger occurs in those cases where the housing is absent or damaged, allowing the radio active matter to become dispersed to cause internal or external contamination. In the latter case the radioactive substance may be carried in the clothing or on the skin for a longer period of time, exposing the body incessantly to radiation.
- 8.8.2.3 Internal contamination may even occur through normal breathing, if a radioactive gas is involved.
- 8.8.2.4 Radioactive matter or liquid may cause contamination via the mouth or minor injuries.
- 8.8.2.5 internal contamination in particular is dangerous since the body is no longer protected by the skin. For these and other reasons, it is necessary to handle components containing radioactive substances with the utmost care to avoid breakage of the housing.
- **8.8.3 Disposal of Damaged Radioactive Components**. When the housing of a radioactive component is undamaged, the radiation risk has a limited character. If, on the other hand, the housing has somehow been damaged, the radiation risk is considerably higher. lt is recommended, therefore, to carry a dosimeter which registers the total dose of radiation received.
- 8.8.3.1 When a radioactive element has been damaged, the following measures must be observed
  - (a) Clear the area of personnel and switch off any inlet and exhaust ventilation to the compartment.
  - (b) Put on rubber gloves and, with the use of tweezers, place all parts of the broken/damaged component into an airtight container,

SHAKTI : UHB\Ch8 Page 593 of 614

- (c) Using adhesive tape, pickup all the small particles and place the adhesive tape, with particles attached, in the container.
- (d) Drag a damp cloth over the area to collect any dust, folding the cloth in wards, as necessary, until the cloth is too small to fold. Place the contaminated cloth in the container,
- (e) Place any tools used for the removal of the contaminated component into a separate container for decontamination,
- (f) Remove gloves with out touching the outside of the gloves and drop them in to the container with the broken parts.
- (g) Seal the containers with adhesive tape and Label 'Radio active Material',
- (h) Monitor the area of the accident with a geiger counter, including any personnel assisting
- (i) When the are a is free from contamination, wash hands thoroughly with soap and water.
- (j) If any injury has occurred during the operation, encourage bleeding from any cuts or abrasion sand obtain qualified medical advice as soon as possible.
- 8.8.3.2 On no account are personnel to eat, drink or smoke while disposing of broken or damaged radio -active components. Radioactive materials may only be transported in accordance with official directions.
- **8.8.4 Safety Sign**. Components, containing radioactive substances, are marked with the danger symbol accordingtoFig.2-2 (without the text part).

#### **8.8.5 Dosimeters**.

- **8.8.5.1 General**. It is recommended to use dosimeters for the measurement of the dose of ionizing radiation received. This applies in particular to the following personnel
  - (a) Technicians performing maintenance or repair work on units producing ionizing radiation, the exposure rate on any part of the body exceeding 5 µS/h (0.5 m Rem/h),

SHAKTI : UHB\Ch8 Page 594 of 614

- (b) Personnel performing activities usually involving radioactive substances, when it is likely that the persons in question may receive more than 2 mS/year (0.2 Rem/year),
- (c) Personnel performing maintenance and repair work on a radioactive source.
- **8.8.5.2 Use of Dosimeters**. Dosimeters are produced in different designs. The type to which the following rules are applicable is the 'film badge', containing a photographic film which shows, upon development, a certain blackening due to radiation on received. Personnel is obliged to observe the following instructions regarding the use of the film badge:
  - (a) During working hours the film badge must be carried as described (the position is stated when the film badge is provided),
  - (b) When the film badge is not carried, it must be so stored that it can not be irradiated.
  - (c) The place of storage must be cool and dry since moisture and high temperature may produce incorrect measuring results.
  - (d) It is for bidden to use another person's film badge.
- 8.8.5.2.1 The dose measured by means of the film badge must be registered on a' registration card for personal radiation check' by the safety officer.

#### **8.9 Microwave radiation**.

- **8.9.1 General**. Microwaves are electromagnetic oscillations, having a frequency range lying between 300MHz and 300GHz. Dangerous microwaves are produced by high power devices, e.g. klystrons, magnetron sand TWTs. Microwaves are used in the following applications:
  - (a) Communication systems, detection
  - (b) Systems(radar)
  - (c) Measuring equipment.

SHAKTI : UHB\Ch8 Page 595 of 614

- **8.9.2 Risks**. Direct exposure of the body to microwave radiation will cause
  - (a) A temperature rise of the internal organs, implying that, in particular, organs having a poor blood supply, such as the gall-bladder and the urinary tracts, maybe damaged.
  - (b) Development of turbidity of the eye lenses.
  - (c) Damage of the reproductive organs.
- 8.9.2.1 The degree of damage may vary considerably, depending on the intensity, frequency and duration of the radiation, thickness of bones, muscles and fat layers, the reflecting qualities of the skin, the absorption coefficient of the tissue exposed to radiation, the clothing and the irradiated surface. Intense heating may develop in small body cavities due to concentration of energy by resonance.
- **8.9.3 Permissible Radiation Level**. The starting point should always be, that the exposure of any part of the body to microwave radiation, even of low power, should be avoided as much as possible. When a radar system is transmitting, a microwave radiation hazard exists around the antenna and in waveguide circuits.
  - (a) Safe areas:
    - (i) Under normal operational conditions there is no RADHAZ danger to personnel.
    - (ii) In the vicinity of the antenna, the area below the plane through the foundation ring of the antenna can be considered as a safe area. Dangerous
  - (b) Areas:
    - (i) when servicing or repair work has to bed one close to the antenna, the following information must be observed
- 8.9.3.1 The dangerous areas are sub divided into four zones, dependent upon the power density (PD) of the radiation, see Fig.8-16

SHAKTI : UHB\Ch8 Page 596 of 614

![](_page_601_Figure_1.jpeg)

**Figure-8.16: Permissible Radiation Level (v is the frequency of the radiation)**

8.9.3.2 Transference of this figure in more practical values, gives the following four zones of danger as an indication.

**Zone A:** Extremely dangerous (PD>20mW/cm2). This are a must not been tered by personnel when there is radar transmission.

**Zone B:** Very dangerous (20mW/cm2>PD>10mW/cm2).This area should not be entered for periods longer than IO minutes per hour when there is radar transmission (total exposure should not exceed1hourper day).

**Zone C**: Dangerous (10mW/cm2>PD>ImW/cm2) This area should not be entered for periods longer than I hour per day when there is radar transmission.

**Zone D:** Not dangerous (PD<ImW/cm2). This are a is safe for continuous exposure.

SHAKTI : UHB\Ch8 Page 597 of 614

## **8.9.4 Safety Measures**.

- (a) Persons handling units which emit microwaves must be sufficiently trained in handling these units and must be aware of the risk involved in this radiation.
- (b) Under no conditions it is permitted to look toward the open end of a waveguide or a coaxial cable when the unit is operating, since otherwise temporary or permanent blindness may be suffered.
- (c) Operating personnel must not remain in a place where the heat produced by radiation can be felt. It is not permitted to check the functioning of an installation by checking the heat with the hand, since this action may cause injury.
- (d) Special attention must be paid to radar antennas in operation, because the radiation level is considerably high in the close vicinity of these sources.
- (e) If one has been exposed for some time to a microwave radiation exceeding10 mW/cm2,he must immediately consult a doctor.
- (f) When a radiation level of 10mW/cm2 is exceeded, warning notices must be used, stating: '**DANGER: Intensive Microwave Radiation**'.
- (g) The safety level around radiation sources must be determined by means of measurements at regular intervals and whenever a change has been introduced. Reflection from neighboring objects must also be taken into account.

#### **8.10. Laser Radiation**.

- **8.10.1 General**. A concentrated transfer of energy realized by a very narrow laser beam may cause damage to biological tissues, due to the development of heat when the radiation is absorbed. The eye lens may increase the effect of the radiation by a factor I05 to I06, resulting in blind spots on the retina within one microsecond.
- 8.10.1.1 Radiation lying outside the visible light range (infrared and ultra-violet) carries an additional risk since one is not aware of the existence of radiation. High-power lasers may cause burns on the skin by absorption of energy. These are not only effected by the laser beam proper, but also and in particular random reflections. When the laser energy is absorbed by an inflammable agent, a fire may start.

SHAKTI : UHB\Ch8 Page 598 of 614

**8.10.2 Safe Distance**. The safe distance to a laser is the distance at which the radiation intensity of the beam has decreased to the so-called Safe Viewing Distance (SVD) value. At this distance there is no longer any danger for eyes and skin.

8.10.2.1 For the determination of the safe distance, the following formula applies

SVD = 
$$\frac{1.13}{\varnothing} \sqrt{\frac{P}{E}} - a^2$$
  
where: SVD = Safe Viewing Distance (m),

E: radiation intensity in MPE value (W/m2). MPE=Maximum Pennissible Exposure value,

a: diameter of exit beam (m),see Fig.2-9.

**Note: If 'a' is unknown, its value is assumed to be zero.**

**WARNING:** If binoculars are used, the SYD is increased by a factor which is dependent on the lens magnification.

![](_page_603_Picture_9.jpeg)

**Figure-8.17: Determination of the Safe Viewing Distance**

SHAKTI : UHB\Ch8 Page 599 of 614

- **8.10.3 Safety Measures**. During maintenance or repair work the following rules must be observed.
  - (a) The 100,000 times attenuation filter must be fitted (SYD<= 0 m)
  - (b) Looking squarely into the laser beam(or reflections of the beam)must be avoided.
  - (c) If possible, switch to minimum output power during testing.
  - (d) Ensure that the laser beam does not strike reflecting surfaces,
  - (e) When the laser system is used in a closed room, the lighting level must be high(approx. 1500 lux), the pupil of the eyes being small under these conditions.
  - (f) Limit the number of persons in this room to a minimum.
  - (g) Mark the vicinity of the location by means of warning signs, taking into account the safe distance.
  - (h) The stops for the bearing and elevation motions of the laser system must be adjusted to minimum values during testing.
  - (i) Laser designed for surveillance and ranging must not be directed within the safe distance at vehicles, aircraft, vessels or other objects which do not officially serve as targets. If this is necessary, however, safety measures must be taken (for instance, safety goggles),and the crew of the objects in question must be informed of the potential risks.
  - (j) Care must be taken that during aligning and adjusting activities, the dose received by the eyes remains below the MPE level. If required, a reducing filter must be used. During these activities, the risks mentioned above must be borne in mind.
- **8.10.4 Laser Goggles**. If there is a chance that during working with a laser system the eyes are exposed to a radiation intensity which exceeds the applicable MPE level, properly constructed laser goggles must be used.

SHAKTI : UHB\Ch8 Page 600 of 614

- 9.4.1 Laser goggles contain filters, having a certain optical density to reduce the radiation generated by a laser system. The filters must be robust and capable of dissipating the heat produced by radiation striking a small surface.
- 9.4.2 The most widely used filter is the selective absorption filter which provides a satisfactory protection against radiation having a certain wave length(n), but permits the passage of light of other parts of the spectrum, so as to allow observations to be made.
- **8.10.4.1 Optical Density (DA)**. The optical density (or reduction), DA, of the laser goggles applies to certain wavelength(s).Laser systems are capable of generating radiation of more than one wavelength, necessitating protective means which sufficiently reduce the radiation in question.
- 9.4.1.1 If the radiation dose near the eye without laser goggles has an intensity of H(W/m2),the optical density of the filter required to reduce the radiation to the given MPE value is determined by the formula:

$$D\lambda = log \frac{H}{MPE}$$

9.4.1.2 The laser goggles must be provided with a clear indication concerning the wave length for which they may be used and the optical density of the goggles.

## **8.11 Ultraviolet Radiation**.

- **8.11.1 General**. UY-radiation is an electromagnetic oscillation phenomenon with a wave length between approximately I 00 nm and 380 nm.
- 8.11.1 Radiation with a wave length less than 180nm is strongly absorbed by the air. Safety instructions are only applicable for wavelengths from 180 to 380 nm.
- **8.11.2 Risks**.The eyes are very susceptible to UY-radiation with wavelengths below 310 nm, the strongest effect appears at 270 nm.
- 8.11.2.1 When a high amount is received, a very painful inflammation of the connective tissue and the cornea takes place (known as flash-eyes or shipyard eyes). It heals mostly within 24 to 28 hours without permanent damage. UV-radiation causes sunburn,

SHAKTI : UHB\Ch8 Page 601 of 614

and when a high amount is received, severe burning and blistering of the skin takes place.

- 8.11.2.2 In particular, radiation with a wavelength of approximately300 nm and below 270nmhas this property.
- 8.11.2.3 UV-radiation with a wavelength of less than 240 nm causes ozone (03)in the air, this gas is dangerous to the health (lungs).

## **8.12. Cleaning Agents/ Solvents**.

**8.12.1 General**. Certain cleaning agents and solvents are hazardous to the health if not used under the right conditions. Pay attention to the following information when handling these items:

#### **8.12.2 Safety Information**.

**Table-8.1: Cleaning Agents/Solvents**

| Cleaning Agents/Solvents    | Description                                                                                                                                                                    |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| White<br>Sprite             | inflammable                                                                                                                                                                    |
| Freon                       | if possible,<br>avoid                                                                                                                                                          |
| TE<br>Chloroethene<br>NU    | usage avoid inhalation do not use in<br>closed rooms<br>irritates the skin due to the<br>strong degreasing action heating<br>produces very poisonous gases avoid<br>inhalation |
| Isopropanol Ethanol         | do not use in closed rooms in flammable<br>inflammable avoid                                                                                                                   |
| MEK(methylphenyl<br>ketone) | inhalation do not use in closed rooms<br>irritates the skin due to the strong<br>degreasing action avoid inhalation                                                            |
| Nebol                       | inflammable                                                                                                                                                                    |
| Thinner                     | inflammable poisonous                                                                                                                                                          |

SHAKTI : UHB\Ch8 Page 602 of 614

#### **8.13 Sealing Agents**.

- **8.13.1 General**.It is recommended that personnel applying sealing agents pay attention to safety when handling these items.
- **8.13.2 Safety Information**. SealerEC800 inflammable (flash point 0 <sup>0</sup>C) avoid inhalation of the vapor Good ventilation of the work spot is necessary

## **8.14. Bonding Adhesives**

- **8.14.1 General**.It is recommended that personnel applying bonding adhesives pay attention to safety when handling these items
- **8.14.2 Epoxy Resin Adhesive**. Do not touch the uncured mixture to avoid skin irritation.

#### **8.14.3 Robber Contact Adhesives**.

- (a) Rubber contact adhesive is very inflammable.
- (b) Keep container closed when not in use.
- (c) Thorough ventilation of the work area is required.
- (d) Smoking of naked flames in the vicinity of the work spot is not allowed.
- (e) Inhalation of the vapour must be avoided.

#### **8.14.4 Cyanoacrylate Adhesive**.

- (a) Cyanoacrylate adhesive is inflammable above 50 °C. Naked flames and the presence of hot objects when using this adhesive is not allowed.
- (b) Uncured adhesives bonds immediately to the skin.
- (c) Great care should be taken to avoid contact with fingers and particularly the eyes.
- (d) Adhesives should be rinsed with water immediately, and NOT with a solvent. Vapour irritates the mucous membranes and particularly the eyes.

SHAKTI : UHB\Ch8 Page 603 of 614

#### **8.15 Locking Agents**.

- **8.15.1 General**.It is recommended that personnel applying locking agents pay attention to safety when handling these agents.
- **8.15.2 Safety Information**.Locking agent residue should be washed off with soap and water.

#### **8.16 HUMISEAL IB31**

- **8.16.1 General**.It is recommended that personnel, applying Humiseal 1B31, pay attention to safety during this part of the job.
- **8.16.2 Safety Information**.The main ingredient of Humiseal-thinner is toluene.
- 8.16.2.1 Toluene is poisonous and inflammable, so see to good ventilation at the work spot and avoid naked flames.

## **8.17 Beryllium Oxide (BeO)**.

- **8.17.1 General**.It is recommended that personnel working with this material pay attention to safety during handling. Beryllium oxide can be used as heat conducting material under power devices.
- **8.17.2 Safety Information**.Beryllium oxide dust and fumes are highly toxic and admission to the body can result in serious injury or even death. Avoid inhalation and contact with open wounds.
- 8.17.2.1 Tightening torques must be strictly observed due to the fact that the material is very brittle and particles are easily scattered in the open air.

#### **8.18 Teflon**.

- **8.18.1 General**.It is recommended that personnel working with this material pay attention to safety during handling.
- **8.18.2 Safety Information**.When Teflon is heated above 200 °C, toxic vapors are released which can cause serious injury or even death.
- 8.18.2.1 Pay strict attention to the following points during use:

SHAKTI : UHB\Ch8 Page 604 of 614

- (a) Personnel working with this material (cutting, stripping wire, etc.) should not smoke during the job.
- (b) Smoking attributes should not be carried in the work clothing nor be left in the work place during the job,
- (c) Material should be stored in closed packaging and waste products should be kept in closed containers
- (d) After handling Teflon, thoroughly brush off clothes and scrub face and hands.

#### **8.19 Safety And First Aid**.

- **8.19.1 General**.Because personnel working with electronic equipment are exposed to the hazard of high voltage, it is imperative that all safety instructions be consistently observed, and that each individual has a clear understanding of basic First Aid methods.
- 18.1.1 For their own protection, and the protection of others, all maintenance personnel should become thoroughly familiar with the approved First Aid treatment of burns and shock.
- **8.19.2 Burns**.There are three principal degrees of burns, recognizable as follows:
  - (a) A first degree burn colours the skin.
  - (b) A second degree burn blisters the skin.
  - (c) A third degree burn chars the flesh and frequently places the victim in a state of shock accompanied by respiratory paralysis.
- **8.19.3 Respiratory Paralysis**.Respiratory paralysis in the victim can cause death within seconds, by suffocation. For this reason it is imperative that the approved method of artificial respiration be initiated immediately and continued until the victim's breathing is normal.
- 8.19.3.1 A muscular spasm or unconsciousness may render the victim unable to free himself of the electric power. If this is the case, turn the power OFF immediately.

WARNING: DO NOT TOUCH HIM, OR YOU MAY SHARE HIS PREDICAMENT!

SHAKTI : UHB\Ch8 Page 605 of 614

8.19.3.2 If the power cannot be turned OFF immediately, very carefully loop a dry rope, article of clothing, length of strong cloth, or a rolled-up newspaper around the victim and pull him free of the power. Carefully avoid touching him or his clothing during this action.

8.19.3.3 The moment he is clear of the power, place him in a reclining position, cover him with a blanket (or newspapers) to keep him warm, and start artificial respiration. At the first opportunity, enlist help in the summoning of a doctor. If a doctor cannot be summoned, transport the victim to the doctor, infirmary, or hospital. Be sure that the victim is kept well covered and warm while awaiting professional aid and treatment.

#### **8.19.4 First Aid in Case of Electric Shock**.

**8.19.4.1 General**.First aid in case of electric shock starts with a check whether there is a breathing stop or a circulation stop.

8.19.4.1.1 To confirm this, the next procedure can be helpful.

SHAKTI : UHB\Ch8 Page 606 of 614

![](_page_611_Figure_1.jpeg)

## **8.19.4.2 Exhaled Air Method (kiss of life)**.If the victim has stopped breathing, then:

(a) Lay the victim face upwards on the floor.

SHAKTI : UHB\Ch8 Page 607 of 614

- (b) Unbutton his clothing: collar, neck-tie and remove his belt.
- (c) With your fingers remove any foreign objects from his mouth (false teeth, etc.), take up position beside the victim's head, preferably on his left.
- (d) Turn his head over backwards and chin up.
- (e) This action is vital, for it opens the victim's passage.

#### **Act as follows**:

8.19.4.2 Slip your left hand under the victim's neck and raise it, allowing the head to sag backwards.

8.19.4.2 With your right hand, pinch the victim's nose shut and use the remainder of your right hand to apply pressure to the victim's forehead, thus keeping in the 'chin-up' position.

![](_page_612_Picture_8.jpeg)

**Figure-8.18: Mouth-to-mouth Method Applied by One Person**

(a) After having filled your lungs completely, press your open mouth across the victim's mouth to produce a perfect air seal, then empty your lungs with force into his, until the victim's chest expands.

SHAKTI : UHB\Ch8 Page 608 of 614

- (b) Then withdraw your mouth to allow the victim to breath out, this will happen spontaneously because his chest will contract elastically,
- (c) Repeat this method of pumping up the victim's lungs and letting them deflate about.
- (d) 12 times per minute, and continue until the victim will spontaneously breath in and out at a steady rhythm and not too faintly, or until medical assistance arrives.
- **8.19.4.3 External Cardiac Massage**.If the victim's heart has stopped beating, then:
  - (a) Lay the victim on his back on the ground or on some other firm surface.
  - (b) Place the heel of one hand, with the other on top of it, on the lower part of the sternum (breast bone) in the mid line of the chest, see warning below.
  - (c) Apply firm pressure vertically downwards aided by the weight of the body, about 60 times a minute.
  - (d) At the end of each pressure stroke, the hands are to be lifted slightly to allow full recoil of the victim's chest.
  - (e) Sufficient pressure should be used to depress the sternum an inch or so towards the vertebral column (spine).

SHAKTI : UHB\Ch8 Page 609 of 614

![](_page_614_Picture_1.jpeg)

**Figure-8.19: Chest Massage Applied by One Person**

- (a) Artificial respiration must continue simultaneously with external cardiac massage at the rate of about 15 compressions of the heart to one inflation of the lungs.
- (b) Massage should continue until the victim's pulse is clearly felt and the colour returns to normal, or until medical assistance arrives.

WARNING: Do not attempt cardiac massage if there is obvious damage to the victim's chest wall.

8.19.4.3.1 If artificial respiration is done simultaneously with external cardiac massage by two persons the rate is about 5 compressions of the heart to two inflations of the lungs.

For position see Fig. 2-12.

SHAKTI : UHB\Ch8 Page 610 of 614

![](_page_615_Picture_1.jpeg)

**Figure-8.20: Person on the Right Applies External Heart Massage; Person on the left Gives the Kiss of life**

#### **8.20 Precautions To Avoid Equipment Damage**.

- **8.20.1 General**.When performing maintenance, the possibility arises that conditions can occur which bring damage to the equipment.
- **8.20.2 Types of Damage Conditions**.In this paragraph some of the more common types of damage conditions are described.
  - (a) Incorrect use of instruments, instrument leads or tools, improper mating of connectors, modules, fittings and/or couplings.
  - (b) Service actions in high voltage circuits without discharging residual voltages after the high voltage is switched off.
  - (c) Creating conditions in which polarity inversions of liquid tantalum capacitors can occur. Under this condition these capacitors may explode, expelling

SHAKTI : UHB\Ch8 Page 611 of 614

- a caustic electrolyte which may not only injure personnel but also damage other components.
- (d) The use of magnets or magnetic materials (tools) in the vicinity of for instance circulator units, can cause permanent damage to the magnetic characteristics of these units and lead to system loss or degradation.
- (e) Incompetent maintenance in the vicinity of moving parts such as: gearwheels, rotating shafts, couplings, hydraulic actuators, etc. can damage the driving system.
- (f) BSD-sensitive parts (i.e. all PCBs) must be handled with special precautions See paragraph I9.3.
- **8.20.3 ESD Sensitive Parts**.ESD sensitive parts or assemblies will be destroyed by a sudden discharge of static electricity. All modern designs use ESD sensitive parts. In practice all electronic circuitry must be considered as ESD sensitive.
- 8.20.3.1 Handle ESD sensitive parts or assemblies very carefully and apply the following measures (see Fig. 2-13):
  - (a) All personnel should be earthed using a special bracelet.
  - (b) Working surfaces must be electrically dissipative (surface resistance of 105 Q to I 09 Q) and earthed.
  - (c) Check at regular intervals the resistance of the bracelets and the surface of the working table, use ESD safe tools (if in doubt, earth the tool).
  - (d) Keep all synthetic materials/objects away from ESD sensitive parts and working areas, always use ESD safe package materials such as plastic bags and Cabelek boxes. Units or PCBs assembled with ESD sensitive parts and supplied by Signal, are always marked by an ESD sticker (see Fig. 2-14).
  - (e) Before opening package: ground yourself.
  - (f) Use ESD safe tools.

SHAKTI : UHB\Ch8 Page 612 of 614

![](_page_617_Picture_1.jpeg)

**Figure-8.21: ESD Safe Work Area**

![](_page_617_Picture_3.jpeg)

**Figure-8.22: Caution Label for ESD sensitive Parts**

**8.21 Pressurized Appliances**.Piping of hydraulic systems and fuel-piping of diesel engines are highly pressurized items during operation. In case of leakage do not expose any part of the human body to the leak. The high pressure can cause severe injury.

SHAKTI : UHB\Ch8 Page 613 of 614

![](_page_618_Picture_0.jpeg)

**This Page is Intentionally Kept Blank.**

SHAKTI : UHB\Ch8 Page 614 of 614

# **APPENDIX A LIST OF PRIVILEGED COMMANDS**

### **Appendix-A**

## **LIST OF PRIVILEGED COMMANDS (Access Rights to System Operations)**

Administrator Level users have the facility to configure system operations access rights to Commander and Operators level users. i.e In Offline mode under user management tab click on 'Restrict User Access' button, a separate GUI, as shown below figure, shall be displayed to the user.

**System operations access rights to Commander and Operator Level Users.**

![](_page_620_Picture_5.jpeg)

![](_page_620_Picture_6.jpeg)

List of operations (activities) of Shakti SCD, along with provision to select/ deselect them, shall be displayed on the GUI. Administrator can give access (system operations) to Commander Level as well as Operator level. Whenever Commander or Operator level user logged in those restricted system commands shall be disabled in the System Controller Application.

![](_page_621_Picture_0.jpeg)

**This page is intentionally left blank.**

Shakti: UHB\App A Page 2

# **APPENDIX B DETAILS OF SYSTEM DEFAULT CONFIGURATION**

### **DETAILS OF SYSTEM DEFAULT CONFIGURATION**

The details of default configuration of System are given in below **Table: B1**

**Table: B1 Default Configuration of System**

| Ser | Subsystem                    | Default Configuration                                                                                                                                                                      |
|-----|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     |                              | (a)<br>Scan Configuration:<br>Directed Search Mode                                                                                                                                         |
| 1   | Narrow Band<br>Receiver-1    | IF BW: 10 MHz<br>, Center Freq. : 170 MHz, Threshold : -<br>50dB, IF Attenuation: 0 dB<br>, RF Attenuation :0 dB, Dwell<br>Time : 1000 msec, Polarization : Horizontal                     |
|     | (0.175 –<br>0.5<br>GHz)      | (b)<br>In RFPS mode: Center Freq: 170 MHz, RF Attenuation:<br>0 dB, IF Attenuation: 0 dB, Threshold:<br>-40 dB, IF BW:<br>500 MHz, Polarization Type: Horizontal.                          |
|     |                              | (c)<br>Block/ Activate Rx: Activate Rx                                                                                                                                                     |
|     |                              | (a)<br>Scan Configuration: Directed Search Mode                                                                                                                                            |
|     | Narrow Band<br>Receiver-2    | IF BW: 10 MHz , Center Freq. : 1280<br>MHz, Threshold : -<br>80dB,<br>IF Attenuation: 10 dB , RF Attenuation :0 dB,<br>Dwell Time : 250<br>msec,                                           |
| 2   | (0.5 –<br>18<br>GHz)         | (b)<br>In RFPS mode: Center Freq: 1280<br>MHz, RF Attenuation:<br>0 dB, IF Attenuation: 10 dB, Threshold:<br>-80 dB, IF BW:<br>500 MHz, Quadrant selection:<br>Quadrant 1 (0 –<br>90 Deg). |
|     |                              | (c)<br>Block/ Activate Rx: Activate Rx                                                                                                                                                     |
|     |                              | (a)<br>Receiver Mode<br>: Broad Band                                                                                                                                                       |
|     | Broad Band                   | (b)<br>Threshold<br>: -63dBm                                                                                                                                                               |
| 3   | Receiver-1                   | (c)<br>Block/Activate Rx<br>: Activate Rx                                                                                                                                                  |
|     | (2.2 -18<br>GHz)             | (d)<br>Quadrant Data Select : Auto quadrant 0                                                                                                                                              |
|     |                              | (e)<br>Quadrant Enable<br>: ON                                                                                                                                                             |
|     |                              | (f)<br>Switch Filter Bank<br>: 2.2-<br>18 GHz                                                                                                                                              |
|     |                              |                                                                                                                                                                                            |
|     | Broad Band                   | (a)<br>Receiver Mode<br>: Broad Band<br>(b)<br>Threshold<br>: -60dBm                                                                                                                       |
| 4   | Receiver-1<br>(18<br>-<br>40 | (c)<br>Block/Activate Rx<br>: Activate Rx                                                                                                                                                  |
|     | GHz)                         | (d)<br>Calibration<br>: Off                                                                                                                                                                |
|     |                              |                                                                                                                                                                                            |
|     |                              | (a)<br>Track Build Count<br>: 8                                                                                                                                                            |
| 5   | ESM<br>Processor             | (b)<br>Track Maintenance Count : 5                                                                                                                                                         |
|     |                              | (c)<br>Confidence Level<br>: 5                                                                                                                                                             |

| Ser | Subsystem            | Default Configuration                                                                                  |  |  |  |  |
|-----|----------------------|--------------------------------------------------------------------------------------------------------|--|--|--|--|
|     |                      | (d)<br>Order Criterion<br>: CL                                                                         |  |  |  |  |
|     |                      | (e)<br>DOA Tolerance<br>: 3σ                                                                           |  |  |  |  |
|     |                      | (f)<br>PW Tolerance<br>: 3 σ                                                                           |  |  |  |  |
|     |                      | (g)<br>Frequency Tolerance<br>: 3 σ                                                                    |  |  |  |  |
|     |                      | (h)<br>Auto Purge Time<br>: 0                                                                          |  |  |  |  |
|     |                      | (j)<br>Passive Time<br>: 20                                                                            |  |  |  |  |
|     |                      | (k)<br>Auto BITE Interval<br>:30 min                                                                   |  |  |  |  |
|     |                      | (a)<br>Mode of Operation<br>:<br>Semi Auto                                                             |  |  |  |  |
|     |                      | (b)<br>Transmitter Power<br>: 0 dB                                                                     |  |  |  |  |
|     |                      | (c)<br>ERP<br>:<br>50<br>KW (For Both Port and<br>Start Board side)                                    |  |  |  |  |
|     |                      | (d)<br>Servo Position<br>: 0 Deg                                                                       |  |  |  |  |
|     |                      | (e)<br>Jamming Time Duration<br>: 0 msec                                                               |  |  |  |  |
|     | EA<br>Processor      | (f)<br>Frequency<br>: 6000 MHz                                                                         |  |  |  |  |
| 6   |                      | (g)<br>DOA<br>: 35 Deg                                                                                 |  |  |  |  |
|     |                      | (h)<br>Elevation<br>: 5 Deg                                                                            |  |  |  |  |
|     |                      | (j)<br>Amplitude<br>:9<br>dB                                                                           |  |  |  |  |
|     |                      | (k)<br>PW<br>:1000<br>nsec                                                                             |  |  |  |  |
|     |                      | (l)<br>PRF<br>:1000<br>Hz                                                                              |  |  |  |  |
|     |                      | (m)Scan Type<br>:<br>Lock-on                                                                           |  |  |  |  |
|     |                      | (n)<br>Scan Period<br>:30 msec                                                                         |  |  |  |  |
|     |                      | (p)<br>Threat Level<br>:5                                                                              |  |  |  |  |
|     |                      | (q)<br>JPRO Number<br>:DRFM<br>Barrage<br>100<br>MHz<br>Tech. Duration 1000 msec with Noise Technique. |  |  |  |  |
|     |                      | (a)<br>Display Mode<br>: Tabular                                                                       |  |  |  |  |
|     |                      | (b)<br>Frequency Bands<br>: ALL Selection                                                              |  |  |  |  |
|     |                      | (c)<br>Filters<br>: No                                                                                 |  |  |  |  |
|     |                      | (d)<br>Zoom<br>: No                                                                                    |  |  |  |  |
|     |                      | (e)<br>Freeze<br>: Off                                                                                 |  |  |  |  |
|     | System<br>Controller | (f)<br>Auto BITE<br>: On                                                                               |  |  |  |  |
| 7   | (ESM                 | (g)<br>True/Relative<br>: True                                                                         |  |  |  |  |
|     | Display)             | (h)<br>Raw/Synthetic<br>: Synthetic                                                                    |  |  |  |  |
|     |                      | (j)<br>Label Blank<br>: Off                                                                            |  |  |  |  |
|     |                      | (k)<br>Sector Blanking<br>: Off                                                                        |  |  |  |  |
|     |                      | (l)<br>Audio Alarm<br>: Off                                                                            |  |  |  |  |
|     |                      | (m)Library Search In<br>: Priority and Temporary Libraries                                             |  |  |  |  |

| Ser | Subsystem | Default Configuration                                                                                                                                                                                                                                                                                                                                                            |
|-----|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     |           | (a)<br>RFPS Mode of Operation<br>: Auto RFPS<br>(b)<br>Normal RFP Timeout<br>:180<br>(c)<br>Freq. Min<br>: 2200 MHz                                                                                                                                                                                                                                                              |
| 8   | RFPS      | (d)<br>Freq. Max<br>: 18000 MHz<br>(e)<br>PW Min<br>: 50 nsec<br>(f)<br>PW Max<br>: 25000<br>nsec<br>(g)<br>PRI Min<br>: 2 usec<br>(h)<br>PRI Max<br>: 20000 usec                                                                                                                                                                                                                |
|     | ESI       | (a)<br>Longitude<br>: 72.7 Deg<br>(b)<br>Latitude<br>:18.3 Deg<br>(c)<br>Heading<br>:45 Deg                                                                                                                                                                                                                                                                                      |
| 9   | MAP       | (a)<br>Default Zoom Level<br>: 185000<br>(b)<br>Default Map Mode<br>: Moving Platform<br>(c)<br>Zoom Scale<br>: 10<br>(d)<br>Default Map Files<br>: Base_Map_India.tif,<br>Layer_Bay_of_Bengal_N_India.tif,Layer_Bay_of_Bengal<br>_S_India.tif<br>(e)<br>Spokes<br>: Hide<br>(f)<br>Annotation<br>: Hide All<br>(g)<br>Tactical Impose<br>: 0<br>(h)<br>Way Points<br>: Hide All |

**This page is intentionally left blank.**

Shakti: UHB\APP B Page 6

# **APPENDIX C AUTO BITE REFERENCE TRACK DETAILS**

## **AUTO BITE REFERENCE TRACK DETAILS**

**Table C1: Auto Bite Reference Track Details** 

| <u>Ser</u> | Ref.Trk<br>No | Rx.Type | <u>Freq</u><br>(MHz) | DOA(Deg) | PRF<br>(KHz) | PW<br>(nsec) |
|------------|---------------|---------|----------------------|----------|--------------|--------------|
| 1          | 601           | NB Rx1  | 2100                 | 45       | 100          | 1000         |
| 2          | 602           | NB Rx1  | 5500                 | 45       | 100          | 1000         |
| 3          | 603           | NB Rx1  | 7500                 | 45       | 100          | 1000         |
| 4          | 604           | NB Rx1  | 15500                | 45       | 100          | 1000         |
| 5          | 605           | NB Rx1  | 2100                 | 135      | 100          | 1000         |
| 6          | 606           | NB Rx1  | 5500                 | 135      | 100          | 1000         |
| 7          | 607           | NB Rx1  | 7500                 | 135      | 100          | 1000         |
| 8          | 608           | NB Rx1  | 15500                | 135      | 100          | 1000         |
| 9          | 609           | NB Rx1  | 2100                 | 225      | 100          | 1000         |
| 10         | 610           | NB Rx1  | 5500                 | 225      | 100          | 1000         |
| 11         | 611           | NB Rx1  | 7500                 | 225      | 100          | 1000         |
| 12         | 612           | NB Rx1  | 15500                | 225      | 100          | 1000         |
| 13         | 613           | NB Rx1  | 2100                 | 315      | 100          | 1000         |
| 14         | 614           | NB Rx1  | 5500                 | 315      | 100          | 1000         |
| 15         | 615           | NB Rx1  | 7500                 | 315      | 100          | 1000         |
| 16         | 616           | NB Rx1  | 15500                | 315      | 100          | 1000         |
| 17         | 701           | NB Rx2  | 2250                 | 45       | 100          | 1000         |
| 18         | 702           | NB Rx2  | 3250                 | 45       | 100          | 1000         |
| 19         | 703           | NB Rx2  | 4250                 | 45       | 100          | 1000         |
| 20         | 704           | NB Rx2  | 5250                 | 45       | 100          | 1000         |
| 21         | 705           | NB Rx2  | 7750                 | 45       | 100          | 1000         |
| 22         | 706           | NB Rx2  | 11750                | 45       | 100          | 1000         |
| 23         | 707           | NB Rx2  | 13750                | 45       | 100          | 1000         |
| 24         | 708           | NB Rx2  | 15750                | 45       | 100          | 1000         |
| 25         | 709           | NB Rx2  | 2250                 | 135      | 100          | 1000         |
| 26         | 710           | NB Rx2  | 3250                 | 135      | 100          | 1000         |
| 27         | 711           | NB Rx2  | 4250                 | 135      | 100          | 1000         |
| 28         | 712           | NB Rx2  | 5250                 | 135      | 100          | 1000         |
| 29         | 713           | NB Rx2  | 7750                 | 135      | 100          | 1000         |

| <u>Ser</u> | Ref.Trk<br>No | Rx.Type | Freq<br>(MHz) | DOA(Deg) | PRF<br>(KHz) | PW<br>(nsec) |
|------------|---------------|---------|---------------|----------|--------------|--------------|
| 30         | 714           | NB Rx2  | 11750         | 135      | 100          | 1000         |
| 31         | 715           | NB Rx2  | 13750         | 135      | 100          | 1000         |
| 32         | 716           | NB Rx2  | 15750         | 135      | 100          | 1000         |
| 33         | 717           | NB Rx2  | 2250          | 225      | 100          | 1000         |
| 34         | 718           | NB Rx2  | 3250          | 225      | 100          | 1000         |
| 35         | 719           | NB Rx2  | 4250          | 225      | 100          | 1000         |
| 36         | 720           | NB Rx2  | 5250          | 225      | 100          | 1000         |
| 37         | 721           | NB Rx2  | 7750          | 225      | 100          | 1000         |
| 38         | 722           | NB Rx2  | 11750         | 225      | 100          | 1000         |
| 39         | 723           | NB Rx2  | 13750         | 225      | 100          | 1000         |
| 40         | 724           | NB Rx2  | 15750         | 225      | 100          | 1000         |
| 41         | 725           | NB Rx2  | 2250          | 315      | 100          | 1000         |
| 42         | 726           | NB Rx2  | 3250          | 315      | 100          | 1000         |
| 43         | 727           | NB Rx2  | 4250          | 315      | 100          | 1000         |
| 44         | 728           | NB Rx2  | 5250          | 315      | 100          | 1000         |
| 45         | 729           | NB Rx2  | 7750          | 315      | 100          | 1000         |
| 46         | 730           | NB Rx2  | 11750         | 315      | 100          | 1000         |
| 47         | 731           | NB Rx2  | 13750         | 315      | 100          | 1000         |
| 48         | 732           | NB Rx2  | 15750         | 315      | 100          | 1000         |
| 49         | 801           | BB Rx1  | 2250          | 45       | 100          | 1000         |
| 50         | 802           | BB Rx1  | 3250          | 45       | 100          | 1000         |
| 51         | 803           | BB Rx1  | 4250          | 45       | 100          | 1000         |
| 52         | 804           | BB Rx1  | 5250          | 45       | 100          | 1000         |
| 53         | 805           | BB Rx1  | 7750          | 45       | 100          | 1000         |
| 54         | 806           | BB Rx1  | 11750         | 45       | 100          | 1000         |
| 55         | 807           | BB Rx1  | 13750         | 45       | 100          | 1000         |
| 56         | 808           | BB Rx1  | 15750         | 45       | 100          | 1000         |
| 57         | 809           | BB Rx1  | 2250          | 135      | 100          | 1000         |
| 58         | 810           | BB Rx1  | 3250          | 135      | 100          | 1000         |
| 59         | 811           | BB Rx1  | 4250          | 135      | 100          | 1000         |
| 60         | 812           | BB Rx1  | 5250          | 135      | 100          | 1000         |
| 61         | 813           | BB Rx1  | 7750          | 135      | 100          | 1000         |
| 62         | 814           | BB Rx1  | 11750         | 135      | 100          | 1000         |

Shakti: UHB\App C

| <u>Ser</u> | Ref.Trk<br>No | Rx.Type | Freq<br>(MHz) | DOA(Deg) | PRF<br>(KHz) | PW<br>(nsec) |
|------------|---------------|---------|---------------|----------|--------------|--------------|
| 63         | 815           | BB Rx1  | 13750         | 135      | 100          | 1000         |
| 64         | 816           | BB Rx1  | 15750         | 135      | 100          | 1000         |
| 65         | 817           | BB Rx1  | 2250          | 225      | 100          | 1000         |
| 66         | 818           | BB Rx1  | 3250          | 225      | 100          | 1000         |
| 67         | 819           | BB Rx1  | 4250          | 225      | 100          | 1000         |
| 68         | 820           | BB Rx1  | 5250          | 225      | 100          | 1000         |
| 69         | 821           | BB Rx1  | 7750          | 225      | 100          | 1000         |
| 70         | 822           | BB Rx1  | 11750         | 225      | 100          | 1000         |
| 71         | 823           | BB Rx1  | 13750         | 225      | 100          | 1000         |
| 72         | 824           | BB Rx1  | 15750         | 225      | 100          | 1000         |
| 73         | 825           | BB Rx1  | 14500         | 315      | 100          | 1000         |
| 74         | 826           | BB Rx1  | 14500         | 315      | 100          | 1000         |
| 75         | 827           | BB Rx1  | 14500         | 315      | 100          | 1000         |
| 76         | 828           | BB Rx1  | 14500         | 315      | 100          | 1000         |
| 77         | 829           | BB Rx1  | 14500         | 315      | 100          | 1000         |
| 78         | 830           | BB Rx1  | 14500         | 315      | 100          | 1000         |
| 79         | 831           | BB Rx1  | 15500         | 315      | 100          | 1000         |
| 80         | 832           | BB Rx1  | 15500         | 315      | 100          | 1000         |
| 81         | 901           | BB Rx2  | 24000         | 45       | 100          | 1000         |
| 82         | 902           | BB Rx2  | 36000         | 45       | 100          | 1000         |
| 83         | 903           | BB Rx2  | 24000         | 225      | 100          | 1000         |
| 84         | 904           | BB Rx2  | 36000         | 225      | 100          | 1000         |
| 85         | 905           | BB Rx2  | 24000         | 135      | 100          | 1000         |
| 86         | 906           | BB Rx2  | 36000         | 135      | 100          | 1000         |
| 87         | 907           | BB Rx2  | 24000         | 315      | 100          | 1000         |
| 88         | 908           | BB Rx2  | 36000         | 315      | 100          | 1000         |

![](_page_631_Picture_0.jpeg)

**This page is intentionally left blank.**