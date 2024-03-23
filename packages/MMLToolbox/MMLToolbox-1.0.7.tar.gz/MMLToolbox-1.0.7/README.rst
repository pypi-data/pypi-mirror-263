This is MMLToolbox!
===================

.. note::

   The package is currently under development and the documentation is adapted along with the features implemented.

This package is a collection of usefule classes, that help access diffrent API's 
in ortder to use the diffrent devices of the MML-laboratory.
It also includes utility classes to enable a easier measurement processes.

Devices:
--------

Digitalmultimeter by NI:
~~~~~~~~~~~~~~~~~~~~~~~~
The system at IGTE comes with two different models of DMMs: the PXI-4071 and the newer version PXI-4081. 
There are three DMMs of the model 4071 and one model 4081. The differences in their specifications are
relatively small and mostly irrelevant when using the MMLToolbox library. However it should be noted, that 
you should put the specifications of the PXIe-4081 on the beginning of the specification dictionary 
not doing this has lead to bugs inside the NI python API in the past. 

When using the MMLToolbox library, you have the option to use any number of the available DMMs.
You can start all connected DMMs at once independently of everything else, or 
start their acquisitions once the DAQMX card outputs an analog signal. 
Starting connected DMMs independently of each other is not possible. 
The measurement mode will always be a voltage waveform acquisition.


DAQMX-card by NI:
~~~~~~~~~~~~~~~~~
The provided card is the BNC-2110, which has 2 channels that can be used as analog outputs and
8 channels that can be used as analog inputs. 
We did not provide any support for its other functionalities.


Switch by NI:
~~~~~~~~~~~~~

The switch is used to synchronize DMMs so that they all start at the same time. To achieve this,
the switch is given a meaningless task that only takes a short time to finish.
Once the task is done, the switch sends a signal to the trigger line that the DMMs are connected to.
This signal starts all DMMs at the same time.

Precsission mesurement tabel by Galil:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The KDT380 by Galil is a can be used to position object in a range of 155*155*155 mm
on the X Y Z axis. The Coord module of MMLToolbox simplyfies the control of the device 
through the gclib API. The module also provides a manual posistioning utilityy 
that lets th euser control the table via keyboard (WASD).





   







